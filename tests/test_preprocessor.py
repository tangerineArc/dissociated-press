from fileinput import FileInput
from markov.preprocessor import get_words
from tempfile import NamedTemporaryFile
from unittest import TestCase


class TestPreprocessor(TestCase):
    def test_get_words(self):
        with NamedTemporaryFile(mode="w+", delete=False) as tmp:
            tmp.write(
                " ! Hello, World. (.).\n\n'These are not words. Are they?' \tasked the \r\n masked warrior. \"It's OK!\""
            )
            tmp_name = tmp.name

        corpus = FileInput(files=[tmp_name])
        words = get_words(corpus)
        self.assertListEqual(
            words,
            [
                "!",
                "Hello",
                ",",
                "World",
                ".",
                "(",
                ".",
                ")",
                ".",
                "'",
                "These",
                "are",
                "not",
                "words",
                ".",
                "Are",
                "they",
                "?",
                "'",
                "asked",
                "the",
                "masked",
                "warrior",
                ".",
                '"',
                "It's",
                "OK",
                "!",
                '"',
            ],
        )
