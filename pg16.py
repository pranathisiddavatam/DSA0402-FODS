import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
def preprocess_text(text):
    words = word_tokenize(text.lower())  
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return words
def calculate_word_frequency(reviews):
    word_freq = Counter()
    for review in reviews:
        words = preprocess_text(review)
        word_freq.update(words)
    return word_freq
if __name__ == "__main__":
    reviews = [
        "This product is amazing. I love it!",
        " It is a waste of money. Not Worth for anyone",
        "Great value for the price.I love Quality. ",
    ]
    word_freq = calculate_word_frequency(reviews)
    print("Top 10 Most Common Words:")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")
