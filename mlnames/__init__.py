import os
import random


rng = random.Random()


with open(os.path.join(os.path.dirname(__file__), "corpus"), "r") as f:
    corpus = [vocab.rstrip() for vocab in f.readlines()]

with open(os.path.join(os.path.dirname(__file__), "exclude_words"), "r") as f:
    exclude_words = [w.rstrip() for w in f.readlines()]
exclude_words = set(exclude_words)

corpus = [word for word in corpus if word not in exclude_words]


def set_seed(seed):
    rng.seed(seed)


def get_name(n_words=1, prefix="", suffix=""):
    return prefix + "-".join(rng.sample(corpus, n_words)) + suffix
