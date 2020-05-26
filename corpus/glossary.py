import glob


def glossary_to_words(filename):
    with open(filename) as f:
        words = f.readlines()
        words = [word.strip() for word in words]

    # Remove sentence number
    words = [word.split(",")[0].strip() for word in words]
    # Remove phrases
    words = [word for word in words if " " not in word]
    # Remove non-alphabet words
    words = [word for word in words if word.isalpha()]
    # Use lowercase
    words = [word.lower() for word in words]
    # Remove duplicates
    words = list(set(words))

    return words


def main():
    filenames = glob.glob("glossary/*")
    corpus = []
    for filename in filenames:
        corpus += glossary_to_words(filename)
    corpus = sorted(set(corpus))

    with open("corpus", "w") as f:
        f.write("\n".join(corpus))

    print(f"Extracted {len(corpus)} words from glossary files.")


if __name__ == "__main__":
    main()
