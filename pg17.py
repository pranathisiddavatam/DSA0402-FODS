import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from collections import Counter
stop_words = set(stopwords.words('english'))
def load_dataset(file_path):
    try:
        dataset = pd.read_csv('C:/Users/DELL/OneDrive/Documents/feedback.csv')
        return dataset['feedback']
    except FileNotFoundError:
        print("File not found. Please make sure 'feedback.csv' exists in the specified path.")
        exit(1)
def preprocess_text(text):
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!?()[]{}"\'') for word in words if word not in stop_words]
    return words
def calculate_word_frequencies(feedback_data):
    word_freq = Counter()
    for feedback in feedback_data:
        words = preprocess_text(feedback)
        word_freq.update(words)
    return word_freq
def display_top_words(word_freq, top_n):
    top_words = word_freq.most_common(top_n)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(top_words))
    print(f"Top {top_n} Most Frequent Words:")
    for word, freq in top_words:
        print(f"{word}: {freq}")
    plt.figure(figsize=(12, 6))
    plt.bar(*zip(*top_words))
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f'Word Cloud of Top {top_n} Words')
    plt.show()
def main():
    dataset = load_dataset('C:/Users/DELL/OneDrive/Documents/feedback.csv')
    top_n = int(input("Enter the number of top words to display: "))
    word_freq = calculate_word_frequencies(dataset)
    display_top_words(word_freq, top_n)
if __name__ == "__main__":
    main()
