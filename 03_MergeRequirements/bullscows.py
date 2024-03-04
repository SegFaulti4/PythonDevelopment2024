from collections import defaultdict
from random import choice
import argparse
import os.path


def bullscows(guess: str, secret: str) -> (int, int):
    assert len(guess) == len(secret)

    bulls, cows = 0, 0
    guess_chars = defaultdict(int)
    secret_chars = defaultdict(int)

    for g, s in zip(guess, secret):
        if g == s:
            bulls += 1
        else:
            guess_chars[g] += 1
            secret_chars[s] += 1

    for k in guess_chars.keys():
        g, s = guess_chars.get(k, 0), secret_chars.get(k, 0)
        cows += min(g, s)

    return bulls, cows


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = choice(words)
    tries, b, c = 0, 0, 0

    while b != len(word):
        inp = ask("Введите слово: ", words)
        b, c = bullscows(inp, word)
        inform("Быки: {}, Коровы: {}", b, c)

    return tries


def _arg_parser() -> argparse.ArgumentParser:
    default_dictionary = os.path.join(os.path.dirname(__file__), "sgb-words.txt")
    p = argparse.ArgumentParser()
    p.add_argument(
        "dictionary",
        nargs="?",
        type=str,
        default=default_dictionary,
        help="path to dictionary",
    )
    p.add_argument(
        "length",
        nargs="?",
        type=int,
        default=5,
        help="words length, any words from dictionary with different length will be excluded",
    )
    return p


def _ref_ask(prompt: str, valid: list[str] = None) -> str:
    return input(prompt).strip()


def _ref_inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


if __name__ == "__main__":
    parser = _arg_parser()
    args = parser.parse_args()

    with open(args.dictionary, "r") as inF:
        words = list(
            filter(lambda x: len(x) == args.length, map(str.strip, inF.readlines()))
        )

    tries = gameplay(_ref_ask, _ref_inform, words)
    print(f"Затрачено попыток: {tries}")
