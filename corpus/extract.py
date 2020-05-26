from collections import Counter
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
    url = 'http://export.arxiv.org/api/query?search_query=cat:stat.ML+OR+cat:cs.AI+OR+cat:cs.LG&start=0&max_results=100'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, features="lxml")

    counter = Counter()
    for summary in tqdm(soup.findAll("summary")):
        words = nltk.word_tokenize(summary.text)
        words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in en_stopwords and word.isalpha()]
        tagged = nltk.pos_tag(words)
        words = [word[0] for word in tagged if word[1] in ["NN", "NNS", "NNP", "NNPS", "FW"]]
        counter += Counter(words)

    common_words_with_freq = counter.most_common(1000)
    common_words = [p[0] for p in common_words_with_freq]
    with open("corpus", "w") as f:
        f.write("\n".join(common_words))


if __name__ == "__main__":
    main()
