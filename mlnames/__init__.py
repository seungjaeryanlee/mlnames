import random


with open("corpus", "r") as f:
    corpus = [vocab.rstrip() for vocab in f.readlines()]


def get_name(n_words=1):
    return "-".join(random.sample(corpus, n_words))
