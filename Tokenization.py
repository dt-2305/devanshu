#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk
from nltk import word_tokenize, FreqDist, pos_tag
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def text_tokenization(text):
    return word_tokenize(text)

def count_word_frequency(tokens):
    return FreqDist(tokens)

def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word.lower() not in stop_words]

def pos_tagging(tokens):
    return pos_tag(tokens)

# Get user input
text = input("Enter a sentence or a paragraph: ")

# Ask user for operations
operations = input("Enter operations separated by commas (a. Tokenization, b. Word Frequency, c. Remove Stop Words, d. POS Tagging): ").lower().split(',')

print("\nPerforming selected operations:\n")

# Perform the selected operations
for operation in operations:
    operation = operation.strip()  # Remove leading/trailing whitespace
    if operation == 'a':
        tokens = text_tokenization(text)
        print("\nTokenization:")
        print("Tokens:", tokens)
    elif operation == 'b':
        tokens = text_tokenization(text)
        word_frequency = count_word_frequency(tokens)
        print("\nWord Frequency:")
        for word, freq in word_frequency.items():
            print(f"{word}: {freq}")
    elif operation == 'c':
        tokens = text_tokenization(text)
        tokens_without_stopwords = remove_stop_words(tokens)
        print("\nRemove Stop Words:")
        print("Tokens without Stop Words:", tokens_without_stopwords)
    elif operation == 'd':
        tokens = text_tokenization(text)
        pos_tags = pos_tagging(tokens)
        print("\nPOS Tagging:")
        print("POS Tags:", pos_tags)
    else:
        print(f"\nInvalid operation '{operation}'. Please select a, b, c, or d.")


# In[ ]:




