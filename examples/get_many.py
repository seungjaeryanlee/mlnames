"""
Script that prints multiple generated names.

Used to check if some words should be excluded.
"""
import mlnames


def main():
    for i in range(10):
        print(mlnames.get_name(n_words=2, word_max_len=10))


if __name__ == "__main__":
    main()
