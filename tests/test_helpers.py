import random
from markov.helpers import build_graph_bigram, generate_output, normalize_graph_weights
from unittest import TestCase


class TestHelpers(TestCase):
    def test_normalize_graph_weights(self):
        graph = {"hello": {"world": 2, "there": 2}, "world": {"hello": 2}}
        normalized_graph = normalize_graph_weights(graph)

        self.assertAlmostEqual(normalized_graph["hello"]["world"], 0.5)
        self.assertAlmostEqual(normalized_graph["hello"]["there"], 0.5)
        self.assertAlmostEqual(normalized_graph["world"]["hello"], 1.0)

    def test_build_graph_bigram(self):
        words = ["the", "cat", "sat", "on", "the", "mat"]
        graph = build_graph_bigram(words)

        self.assertIn("cat", graph["the"])
        self.assertIn("mat", graph["the"])
        self.assertAlmostEqual(graph["the"]["cat"] + graph["the"]["mat"], 1.0)

        self.assertEqual(list(graph["sat"].keys()), ["on"])
        self.assertAlmostEqual(graph["sat"]["on"], 1.0)

    def test_generate_output_deterministic(self):
        random.seed(0)

        graph = {
            "a": {"b": 1.0},
            "b": {"c": 1.0},
            "c": {"a": 1.0},
        }
        output = generate_output(graph, 5)

        words = output.split()
        self.assertEqual(len(words), 5)
        for w in words:
            self.assertIn(w, ["a", "b", "c"])

    def test_generate_output_handles_dead_end(self):
        random.seed(1)

        graph = {
            "x": {},
            "y": {"z": 1.0},
            "z": {"y": 1.0},
        }
        output = generate_output(graph, 5)
        words = output.split()
        self.assertEqual(len(words), 5)
        for w in words:
            self.assertIn(w, ["x", "y", "z"])
