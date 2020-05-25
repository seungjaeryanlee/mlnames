import random


with open("corpus", "r") as f:
    corpus = [vocab.rstrip() for vocab in f.readlines()]


def get_name(n_words=1, prefix="", suffix=""):
    return prefix + "-".join(random.sample(corpus, n_words)) + suffix
