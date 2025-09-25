from pathlib import Path
import subprocess
import sys
from unittest import TestCase


class TestCLI(TestCase):
    def setUp(self):
        self.corpus_path1 = Path("tests") / "sample1.corpus"
        self.corpus_path2 = Path("tests") / "sample2.cotpus"

        self.corpus_path1.write_text(
            "the cat sat on the mat\nthe cat ate a rat\nthe dog barked at the cat\n"
        )
        self.corpus_path2.write_text("")

    def tearDown(self) -> None:
        if self.corpus_path1.exists():
            self.corpus_path1.unlink()
        if self.corpus_path2.exists():
            self.corpus_path2.unlink()

    def test_help(self):
        result = subprocess.run(
            [sys.executable, "markov/main.py", "--help"], capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("stdin", result.stdout.lower())

    def test_sample1_corpus_no_crash(self):
        with self.corpus_path1.open("r") as f:
            result = subprocess.run(
                [sys.executable, "markov/main.py", "-l", "20"],
                stdin=f,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0)
        words = result.stdout.strip().split()
        self.assertEqual(len(words), 20)

    def test_sample2_corpus_no_crash(self):
        with self.corpus_path2.open("r") as f:
            result = subprocess.run(
                [sys.executable, "markov/main.py", "-l", "20"],
                stdin=f,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.stderr, "Error: received an empty file")
