from fileinput import input
from preprocessor import get_words


def main():
    with input() as corpus:
        words = get_words(corpus)

    print(words)


if __name__ == "__main__":
    main()
