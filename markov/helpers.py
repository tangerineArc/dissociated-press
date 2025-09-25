import random


def normalize_graph_weights(
    word_graph: dict[str, dict[str, int]],
) -> dict[str, dict[str, float]]:
    normalized_graph: dict[str, dict[str, float]] = {}
    for word in word_graph:
        s = sum(map(lambda x: x[1], word_graph[word].items()))
        normalized_graph[word] = {}
        for next_word in word_graph[word]:
            normalized_graph[word][next_word] = word_graph[word][next_word] / s

    return normalized_graph


def build_graph_bigram(words: list[str]) -> dict[str, dict[str, float]]:
    word_network: dict[str, dict[str, int]] = {}
    for idx, word in enumerate(words[:-1]):
        next_word = words[idx + 1]

        word_network.setdefault(word, {})
        word_network[word].setdefault(next_word, 0)
        word_network[word][next_word] += 1

    normalized_graph = normalize_graph_weights(word_network)
    return normalized_graph


def generate_output(word_graph: dict[str, dict[str, float]], output_limit: int) -> str:
    all_words = list(word_graph.keys())

    curr = random.choice(all_words)
    output: list[str] = []
    for _ in range(output_limit):
        next_options = list(word_graph.get(curr, {}).keys())
        next_weights = list(map(lambda x: x[1], word_graph.get(curr, {}).items()))

        if next_options and next_weights:
            curr = random.choices(next_options, next_weights)[0]
        else:
            curr = random.choice(all_words)

        output.append(curr)

    return " ".join(output)
