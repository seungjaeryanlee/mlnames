import os
import random


with open(os.path.join(os.path.dirname(__file__), "corpus"), "r") as f:
    corpus = [vocab.rstrip() for vocab in f.readlines()]


def get_name(n_words=1, prefix="", suffix=""):
    return prefix + "-".join(random.sample(corpus, n_words)) + suffix
