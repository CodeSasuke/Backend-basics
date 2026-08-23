"""Learner tests for Module 1.

These tests are expected to fail until exercise.py is implemented.
"""

import unittest

from exercise import apply_command


class LedgerExerciseTests(unittest.TestCase):
    def test_deposit_changes_balance(self):
        self.assertEqual(apply_command(0, "deposit 10"), (10, "10"))

    def test_withdraw_changes_balance(self):
        self.assertEqual(apply_command(10, "withdraw 4"), (6, "6"))

    def test_overdraft_does_not_change_balance(self):
        self.assertEqual(apply_command(10, "withdraw 11"), (10, "error: insufficient funds"))

    def test_reset_returns_zero(self):
        self.assertEqual(apply_command(10, "reset"), (0, "0"))

    def test_invalid_amount_does_not_change_balance(self):
        self.assertEqual(apply_command(10, "deposit -1"), (10, "error: amount must be positive"))


if __name__ == "__main__":
    unittest.main()
