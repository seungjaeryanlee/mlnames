from collections import Counter
import os
import time
import urllib.request

from bs4 import BeautifulSoup
import nltk
nltk.download("averaged_perceptron_tagger")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tqdm import tqdm


en_stopwords = set(stopwords.words('english'))
en_stopwords.add("")
lemmatizer = WordNetLemmatizer()


def main():
    # Populate counter
    counter = Counter()
    for i in tqdm(range(2)):
        url = f"http://export.arxiv.org/api/query?search_query=cat:stat.ML+OR+cat:cs.AI+OR+cat:cs.LG&start={2000*i}&max_results={2000*(i+1)}"
        with urllib.request.urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, features="lxml")

        for summary in soup.findAll("summary"):
            words = nltk.word_tokenize(summary.text)
            words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in en_stopwords and word.isalpha()]
            tagged = nltk.pos_tag(words)
            words = [word[0] for word in tagged if word[1] in ["NN", "NNS", "NNP", "NNPS", "FW"]]
            counter += Counter(words)

        # To give time for arXiv API
        time.sleep(3)

    common_words_with_freq = counter.most_common(1000)
    common_words = [p[0] for p in common_words_with_freq]
    with open("corpus", "w") as f:
        f.write("\n".join(common_words))


if __name__ == "__main__":
    main()
