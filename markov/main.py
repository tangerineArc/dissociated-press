from argparse import ArgumentParser
import fileinput
from helpers import build_graph_bigram, generate_output
from preprocessor import get_words
import sys


def main():
    parser = ArgumentParser(
        prog="Bigram Markov Chain Text Generator",
        description="Reads text from stdin (use `< file` or pipe input) and generates random text.",
        epilog="Example: ./runner -l 100 < small.corpus",
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=50,
        help="Number of words to generate (default: 50)",
    )
    args = parser.parse_args()

    with fileinput.input(files=("-",)) as corpus:
        words = get_words(corpus)

    if not words:
        sys.stderr.write("Error: received an empty file\n")
        sys.exit(1)

    word_network = build_graph_bigram(words)

    output = generate_output(word_network, args.length)
    print(output)


if __name__ == "__main__":
    main()
