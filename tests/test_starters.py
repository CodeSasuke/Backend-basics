"""Small behavior checks for every module starter."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sqlite3
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load(module_number: str, folder: str):
    matches = list(ROOT.glob(f"{module_number}-*/code/main.py"))
    path = matches[0]
    spec = spec_from_file_location(folder, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StarterTests(unittest.TestCase):
    def test_01_state_transition(self):
        module = load("01", "state")
        balance, output = module.apply_command(0, "deposit 10")
        self.assertEqual((balance, output), (10, "10"))

    def test_02_resource_worker(self):
        module = load("02", "resources")
        path = ROOT / "tests" / "jobs.txt"
        path.write_text("a:1\nbad\n", encoding="utf-8")
        try:
            self.assertEqual(module.process_jobs(path), (1, ["line 2: malformed job"]))
        finally:
            path.unlink()

    def test_03_protocol_round_trip(self):
        module = load("03", "protocol")
        message = {"type": "create", "title": "A", "body": "B"}
        self.assertEqual(module.parse_message(module.encode_message(message)), message)

    def test_04_http_handler_exists(self):
        module = load("04", "http")
        self.assertTrue(hasattr(module, "Handler"))

    def test_05_contract_rejects_empty_title(self):
        module = load("05", "contract")
        self.assertFalse(module.validate_create_note({"title": "", "body": "body"})[0])

    def test_06_domain_creates_note(self):
        module = load("06", "structure")
        note = module.create_note(module.NoteRepository(), " title ", " body ")
        self.assertEqual(note.title, "title")

    def test_07_database_constraint(self):
        module = load("07", "persistence")
        database = module.open_database()
        try:
            database.execute("INSERT INTO accounts (balance) VALUES (10)")
            with self.assertRaises(sqlite3.IntegrityError):
                database.execute("INSERT INTO accounts (balance) VALUES (-1)")
        finally:
            database.close()

    def test_08_transfer_is_atomic(self):
        module = load("08", "transactions")
        database = sqlite3.connect(":memory:")
        database.executescript("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL);")
        database.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 100), (2, 0)])
        try:
            module.transfer(database, 1, 2, 25)
            self.assertEqual(database.execute("SELECT balance FROM accounts ORDER BY id").fetchall(), [(75,), (25,)])
        finally:
            database.close()

    def test_09_duplicate_job_is_ignored(self):
        module = load("09", "queues")
        self.assertEqual(module.run_jobs(["a", "a"]), ["completed:a"])

    def test_10_retry_is_bounded(self):
        module = load("10", "retry")
        attempts = [0]

        def operation():
            attempts[0] += 1
            raise TimeoutError("down")

        with self.assertRaises(RuntimeError):
            module.retry(operation, attempts=3, delay=0)
        self.assertEqual(attempts[0], 3)

    def test_11_concurrency_limit_is_validated(self):
        module = load("11", "concurrency")
        with self.assertRaises(ValueError):
            module.run_bounded([], workers=0)

    def test_12_observability_handler_runs(self):
        module = load("12", "observability")
        module.handle_request()

    def test_13_authorization(self):
        module = load("13", "security")
        self.assertTrue(module.can_read_note("alice", "alice"))
        self.assertFalse(module.can_read_note("bob", "alice"))

    def test_14_normalization(self):
        module = load("14", "testing")
        self.assertEqual(module.normalize_title("  a   b "), "a b")

    def test_15_capacity_estimate(self):
        module = load("15", "scaling")
        self.assertEqual(module.estimate_requests_per_second(20, 0.2), 100)

    def test_16_capstone_has_slices(self):
        module = load("16", "capstone")
        self.assertGreaterEqual(len(module.CAPSTONE_SLICES), 5)


if __name__ == "__main__":
    unittest.main()
