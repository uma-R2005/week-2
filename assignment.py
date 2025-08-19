from collections import Counter
import re

def word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    # Remove punctuation using regex and split into words
    words = re.findall(r'\b\w+\b', text)
    
    # Count frequency of each word
    word_counts = Counter(words)
    
    # Get the 10 most common words
    top_10 = word_counts.most_common(10)
    
    print("Top 10 words by frequency:")
    for word, count in top_10:
        print(f"{word}: {count}")

# Example usage:
filename = input("Enter filename: ")
word_frequency(filename)
