# Dissociated Press

This a _bigram_ (order-2) Markov Chain Sentence Generator.

## Usage

> [!NOTE]
> Requires: Python 3.13+

Generate:
```sh
python3 markov/main.py -l OUTPUT_LENGTH < CORPUS
```

For help:
```sh
python3 markov/main.py --help
```

Run tests:
```sh
python3 -m unittest
```

## How it works?

1. corpus analysis: parse the source text and create a dictionary of word-to-word transitions with normalized frequency values
2. random generation: use a pseudo-random number generator to select the next word based on calculated probabilities (weights)

## What needs to be worked on?

- a better CLI experience
- enforce grammatical rules and proper punctuations up to some extent
- control the order with a parameter and appropriate implementation
- add a proper shitposting mode

