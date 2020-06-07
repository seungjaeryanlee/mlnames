import pytest

import mlnames


class TestSetSeed:
    @pytest.mark.parametrize("seed", [1, 2, 3, 4, 5])
    def test_set_seed(self, seed):
        names = []
        for _ in range(10):
            mlnames.set_seed(seed)
            name = mlnames.get_name()
            names.append(name)
        assert len(set(names)) == 1


class TestGetName:
    @pytest.mark.parametrize("n_words", [1, 2, 3, 4, 5])
    def test_n_words(self, n_words):
        name = mlnames.get_name(n_words=n_words, separator="-")
        assert len(name.split("-")) == n_words

    @pytest.mark.parametrize("prefix", ["", "ABCabc", "123", "!@#", "\"\'\t\n "])
    def test_prefix(self, prefix):
        name = mlnames.get_name(prefix=prefix)
        assert name[:len(prefix)] == prefix

    @pytest.mark.parametrize("suffix", ["", "ABCabc", "123", "!@#", "\"\'\t\n "])
    def test_suffix(self, suffix):
        name = mlnames.get_name(suffix=suffix)
        assert name[len(name)-len(suffix):] == suffix

    @pytest.mark.parametrize("word_max_len", [3, 4, 5, 6])
    def test_word_max_len(self, word_max_len):
        name = mlnames.get_name(n_words=10, word_max_len=word_max_len, separator="-")
        words = name.split("-")
        assert all(len(word) <= word_max_len for word in words)

    @pytest.mark.parametrize("n_words", [1, 2, 3, 4, 5])
    @pytest.mark.parametrize("separator", ["-", " ", "!@"])
    def test_separator(self, n_words, separator):
        name = mlnames.get_name(n_words=n_words, separator=separator)
        assert len(name.split(separator)) == n_words
