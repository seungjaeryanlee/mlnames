import random

import mlnames


def main():
    # Basic functionality
    print(mlnames.get_name())
    print(mlnames.get_name(n_words=2))
    print(mlnames.get_name(prefix="1-", suffix="-2"))

    # Separate seeding from random module
    random.seed(1)
    print(mlnames.get_name())

    random.seed(1)
    print(mlnames.get_name())

    # You can explicitly set seed
    mlnames.set_seed(1)
    print(mlnames.get_name())

    mlnames.set_seed(1)
    print(mlnames.get_name())


if __name__ == "__main__":
    main()
