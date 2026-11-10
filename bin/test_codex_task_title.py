import importlib.machinery
import importlib.util
from pathlib import Path
import unittest


loader = importlib.machinery.SourceFileLoader("task_title", str(Path(__file__).with_name("codex-task-title")))
spec = importlib.util.spec_from_loader(loader.name, loader)
titles = importlib.util.module_from_spec(spec)
loader.exec_module(titles)


class Server:
    def __init__(self, name=None, **metadata):
        self.thread = {"name": name, **metadata}
        self.writes = []

    def read(self, thread_id):
        return self.thread.copy()

    def initial_task(self, thread_id):
        return ""

    def recent_messages(self, thread_id):
        return ""

    def rename(self, thread_id, name):
        self.thread["name"] = name
        self.writes.append((thread_id, name))


def prompt(text):
    return {"hook_event_name": "UserPromptSubmit", "prompt": text}


def answer(label="CI speedups", ticket=None, substantive=True, pr=None):
    return lambda _: {"label": label, "ticket": ticket, "pr": pr, "substantive": substantive}


class TaskTitleTests(unittest.TestCase):
    def test_pr_arrives_later_and_persists_without_a_new_reference(self):
        for ticket in (None, "SMS-4321"):
            with self.subTest(ticket=ticket):
                server = Server()
                state = titles.update({}, prompt(f"Fix CI {ticket or ''}"), server, "one", answer(ticket=ticket))
                # Existing state written before PR support must still accept a PR.
                state.pop("pr")

                def generate(context):
                    self.assertEqual(context["candidate_prs"], ["1234"])
                    return answer(ticket=ticket, pr="1234")(context)

                state = titles.update(state, {"hook_event_name": "Stop", "last_assistant_message": "Created https://github.com/semgrep/kp/pull/1234"},
                                      server, "one", generate)
                self.assertEqual(state["pr"], "1234")
                state = titles.update(state, prompt("Run the checks"), server, "one", generate)
                expected = "PR #1234 - CI speedups"
                self.assertEqual(server.thread["name"], f"{ticket} - {expected}" if ticket else expected)
                self.assertEqual(len(server.writes), 2)

    def test_pr_requires_evidence_and_examples_can_be_rejected(self):
        server = Server()
        for text in ("Fix CI", "Fix issue #1234", "See https://github.com/semgrep/kp/issues/1234"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                titles.update({}, prompt(text), server, "one", answer(pr="1234"))

        def generate(context):
            self.assertEqual(context["candidate_prs"], ["1234", "5678"])
            return answer()(context)

        state = titles.update({}, prompt("Fix CI; PR #1234 and PR #5678 are just examples"), server, "one", generate)
        self.assertIsNone(state["pr"])
        self.assertEqual(server.thread["name"], "CI speedups")

    def test_task_name_stays_stable_and_ticket_can_arrive_in_assistant_update(self):
        server = Server()
        state = titles.update({}, prompt("Investigate slow CI"), server, "one", answer())
        state = titles.update(state, prompt("Now run the tests"), server, "one",
                              answer())
        state = titles.update(state, {"hook_event_name": "Stop", "last_assistant_message": "Created SMS-4321 to track this CI work."},
                              server, "one", answer(ticket="SMS-4321"))
        self.assertEqual(server.thread["name"], "SMS-4321 - CI speedups")
        state = titles.update(state, prompt("Also see SMS-5555"), server, "one",
                              answer(ticket="SMS-4321"))
        self.assertEqual(len(server.writes), 2)

    def test_changed_task_replaces_label_and_ticket_using_recent_session(self):
        server = Server()
        state = titles.update({}, prompt("Fix CI for SMS-4321 in PR #1234"), server, "one", answer(ticket="SMS-4321", pr="1234"))
        server.recent_messages = lambda _: "Switch to the Jobs migration, tracked by SMS-5555 in PR #5555"

        def generate(context):
            self.assertEqual(context["existing_label"], "CI speedups")
            self.assertEqual(context["existing_ticket"], "SMS-4321")
            self.assertEqual(context["existing_pr"], "1234")
            self.assertEqual(context["candidate_prs"], ["1234", "5555"])
            self.assertIn("Jobs migration", context["recent_messages"])
            self.assertEqual(context["candidate_tickets"], ["SMS-4321", "SMS-5555"])
            return answer("Jobs migration", "SMS-5555", pr="5555")(context)

        state = titles.update(state, prompt("continue"), server, "one", generate)
        self.assertEqual(server.thread["name"], "SMS-5555 - PR #5555 - Jobs migration")
        state = titles.update(state, prompt("Switch to improving local task titles; no ticket"), server, "one", answer("Task titles"))
        self.assertEqual(server.thread["name"], "Task titles")
        self.assertIsNone(state["ticket"])
        self.assertIsNone(state["pr"])

    def test_identical_context_is_skipped_but_repeated_prompt_with_new_context_is_not(self):
        server = Server()
        state = titles.update({}, prompt("Fix CI"), server, "one", answer())
        state = titles.update(state, prompt("continue"), server, "one", answer())
        state = titles.update(state, prompt("continue"), server, "one",
                              lambda _: self.fail("identical context"))
        server.recent_messages = lambda _: "Instead investigate Jobs"
        titles.update(state, prompt("continue"), server, "one", answer("Jobs investigation"))
        self.assertEqual(server.thread["name"], "Jobs investigation")
        self.assertEqual(len(server.writes), 2)

    def test_diagnosis_can_clarify_title_without_new_prompt_or_ticket(self):
        server = Server()
        state = titles.update({}, prompt("Investigate slow CI"), server, "one", answer("Investigate CI"))

        def generate(context):
            self.assertEqual(context["existing_label"], "Investigate CI")
            self.assertIn("cache key", context["assistant_update"])
            return answer("Fix CI cache misses")(context)

        titles.update(state, {"hook_event_name": "Stop", "last_assistant_message": "The cache key changes on every run; fixing that will address the slowdown."},
                      server, "one", generate)
        self.assertEqual(server.thread["name"], "Fix CI cache misses")

    def test_guidance_is_removed_and_non_task_is_deferred(self):
        text = '# AGENTS.md instructions for /repo\n<INSTRUCTIONS>Read repository guidance</INSTRUCTIONS><environment_context>cwd=/repo</environment_context>'
        server = Server()
        state = titles.update({}, prompt(text), server, "one", lambda _: self.fail("only guidance"))
        state = titles.update(state, prompt("hello"), server, "one", answer("", substantive=False))
        state = titles.update(state, prompt("Fix slow CI SMS-4321"), server, "one", answer(ticket="SMS-4321"))
        self.assertEqual(server.thread["name"], "SMS-4321 - CI speedups")

    def test_manual_rename_wins_including_during_generation(self):
        server = Server()
        state = titles.update({}, prompt("Fix CI"), server, "one", answer())
        server.thread["name"] = "My label"
        result = titles.update(state, prompt("Track as SMS-4321 in PR #1234"), server, "one",
                               lambda _: self.fail("manual rename"))
        self.assertTrue(result["manual"])
        self.assertEqual(server.thread["name"], "My label")
        server = Server()
        state = titles.update({}, prompt("Fix CI"), server, "one", answer())

        def rename_during_generation(context):
            server.thread["name"] = "User renamed during inference"
            return answer()(context)

        state = titles.update(state, prompt("Fix CI cache misses"), server, "one", rename_during_generation)
        titles.update(state, {"hook_event_name": "Stop", "last_assistant_message": "Finished"},
                      server, "one", lambda _: self.fail("concurrent manual rename must persist"))
        self.assertEqual(server.thread["name"], "User renamed during inference")
        self.assertEqual(server.writes, [("one", "CI speedups")])

    def test_initial_title_race_defers_without_disabling_future_updates(self):
        server = Server()
        server.initial_task = lambda _: "Fix CI"

        def initial_title_during_generation(context):
            server.thread["name"] = "Inspect repository guidance"
            return answer()(context)

        state = titles.update({}, prompt("Fix CI"), server, "one", initial_title_during_generation)
        self.assertFalse(state.get("manual"))
        self.assertEqual(server.thread["name"], "Inspect repository guidance")
        self.assertEqual(server.writes, [])
        state = titles.update(state, prompt("Fix CI"), server, "one", answer())
        self.assertEqual(server.thread["name"], "CI speedups")
        self.assertEqual(state["applied_name"], "CI speedups")

    def test_ticket_must_have_evidence_and_example_can_be_rejected(self):
        server = Server()
        with self.assertRaises(ValueError):
            titles.update({}, prompt("Fix CI"), server, "one", answer(ticket="SMS-9999"))
        state = titles.update({}, prompt("Fix CI; SMS-4321 is just an example"), server, "one", answer())
        self.assertIsNone(state["ticket"])
        self.assertEqual(server.thread["name"], "CI speedups")

    def test_subagents_ephemeral_threads_and_other_sessions_are_isolated(self):
        for metadata in ({"parentThreadId": "parent"}, {"source": {"subAgent": {}}}, {"ephemeral": True}):
            server = Server(**metadata)
            titles.update({}, prompt("Fix CI"), server, "one", lambda _: self.fail("excluded thread"))
            self.assertEqual(server.writes, [])
        first, second = Server(), Server()
        titles.update({}, prompt("Fix CI"), first, "one", answer())
        titles.update({}, prompt("Fix Jobs"), second, "two", answer("Jobs migration"))
        self.assertEqual(first.writes, [("one", "CI speedups")])
        self.assertEqual(second.writes, [("two", "Jobs migration")])

    def test_existing_session_uses_original_task_instead_of_continue(self):
        server = Server("Read repository guidance")
        server.initial_task = lambda _: "Speed up CI for SMS-4321"

        def generate(context):
            self.assertEqual(context["task"], "Speed up CI for SMS-4321")
            self.assertEqual(context["follow_up"], "continue")
            self.assertEqual(context["candidate_tickets"], ["SMS-4321"])
            return answer(ticket="SMS-4321")(context)

        titles.update({}, prompt("continue"), server, "one", generate)
        self.assertEqual(server.thread["name"], "SMS-4321 - CI speedups")

    def test_stop_can_finish_before_prompt_hook(self):
        server = Server()
        server.initial_task = lambda _: "Speed up CI"
        state = titles.update({}, {"hook_event_name": "Stop", "last_assistant_message": "Created SMS-4321 for CI work"},
                              server, "one", answer(ticket="SMS-4321"))
        titles.update(state, prompt("Speed up CI"), server, "one", answer(ticket="SMS-4321"))
        self.assertEqual(server.writes, [("one", "SMS-4321 - CI speedups")])

    def test_recent_messages_are_chronological_and_exclude_guidance_and_tool_output(self):
        rpc = object.__new__(titles.Rpc)
        rpc.call = lambda *_: {"data": [
            {"items": [{"type": "userMessage", "content": [{"type": "text", "text": "Switch to Jobs"}]}]},
            {"items": [
                {"type": "userMessage", "content": [{"type": "text", "text": "<INSTRUCTIONS>guidance</INSTRUCTIONS>Fix CI"}]},
                {"type": "commandExecution", "output": "untrusted tool output"},
                {"type": "agentMessage", "phase": "commentary", "text": "Looking into CI"},
                {"type": "agentMessage", "phase": "final_answer", "text": "CI cache misses confirmed"},
            ]},
        ]}
        self.assertEqual(rpc.recent_messages("one"), "User: Fix CI\n\nAssistant: CI cache misses confirmed\n\nUser: Switch to Jobs")


if __name__ == "__main__":
    unittest.main()
