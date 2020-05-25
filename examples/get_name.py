import mlnames


def main():
    print(mlnames.get_name())
    print(mlnames.get_name(n_words=2))
    print(mlnames.get_name(prefix="1-", suffix="-2"))


if __name__ == "__main__":
    main()
