from collections import deque
import fileinput
import string


def main():
    sentences: list[str] = []
    with fileinput.input() as corpus:
        for line in corpus:
            if not (line := line.strip().split()):
                continue

            for word in line:
                start_puncs: list[str] = []
                i = 0
                while i < len(word) and word[i] in string.punctuation:
                    start_puncs.append(word[i])
                    i += 1

                end_puncs: deque[str] = deque([])
                j = len(word) - 1
                while j > i and word[j] in string.punctuation:
                    end_puncs.appendleft(word[j])
                    j -= 1

                word = word[i : j + 1]

                if start_puncs:
                    sentences.extend(start_puncs)
                if word:
                    sentences.append(word)
                if end_puncs:
                    sentences.extend(end_puncs)


if __name__ == "__main__":
    main()
