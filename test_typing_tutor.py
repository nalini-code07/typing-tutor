import unittest
from typing_tutor import (
    clean_text,
    count_correct,
    total_letters,
    accuracy,
    check_attempt,
    average_accuracy,
)


class TestTypingTutor(unittest.TestCase):

    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World!"), ["hello", "world"])

    def test_count_correct(self):
        self.assertEqual(count_correct("Hello", "Hello"), 5)

    def test_total_letters(self):
        self.assertEqual(total_letters("Hello, World!"), 10)

    def test_accuracy(self):
        self.assertEqual(accuracy("Hello", "Hello"), 100.0)

    def test_check_attempt(self):
        result = check_attempt("Hello", "Hello", 2.345)
        self.assertEqual(result["sentence"], "Hello")
        self.assertEqual(result["typed"], "Hello")
        self.assertEqual(result["accuracy"], 100.0)
        self.assertEqual(result["time"], 2.35)

    def test_average_accuracy(self):
        records = [
            {"accuracy": 80.0},
            {"accuracy": 100.0},
        ]
        self.assertEqual(average_accuracy(records), 90.0)

    def test_empty_average(self):
        self.assertEqual(average_accuracy([]), 0.0)

    def test_case_and_punctuation(self):
        self.assertEqual(
            accuracy("Hello, World!", "HELLO WORLD"),
            100.0,
        )


if __name__ == "__main__":
    unittest.main() 