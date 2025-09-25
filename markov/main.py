from fileinput import input
from helpers import build_graph_bigram, generate_output
from preprocessor import get_words


def main():
    with input() as corpus:
        words = get_words(corpus)

    word_network = build_graph_bigram(words)

    output = generate_output(word_network, 100)
    print(output)


if __name__ == "__main__":
    main()
