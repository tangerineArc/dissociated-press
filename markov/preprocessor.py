from collections import deque
from fileinput import FileInput
from string import punctuation


def get_words(corpus: FileInput[str]) -> list[str]:
    words: list[str] = []
    for line in corpus:
        if not (line := line.strip().split()):
            continue

        for word in line:
            start_puncs: list[str] = []
            i = 0
            while i < len(word) and word[i] in punctuation:
                start_puncs.append(word[i])
                i += 1

            end_puncs: deque[str] = deque([])
            j = len(word) - 1
            while j > i and word[j] in punctuation:
                end_puncs.appendleft(word[j])
                j -= 1

            word = word[i : j + 1]

            if start_puncs:
                words.extend(start_puncs)
            if word:
                words.append(word)
            if end_puncs:
                words.extend(end_puncs)

    return words
