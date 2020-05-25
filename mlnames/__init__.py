import os
import random


rng = random.Random()

with open(os.path.join(os.path.dirname(__file__), "corpus"), "r") as f:
    corpus = [vocab.rstrip() for vocab in f.readlines()]


def set_seed(seed):
    rng.seed(seed)


def get_name(n_words=1, prefix="", suffix=""):
    return prefix + "-".join(rng.sample(corpus, n_words)) + suffix
