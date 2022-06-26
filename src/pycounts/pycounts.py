from string import punctuation
from collections import Counter


def load_text(file):
    """load text from a text file and return a string""" 
    with open(file, 'r') as f:
        text = f.read()
        return text

def clean_text(text):
    """lower and  remove punctuation from a text"""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, '')
    return text

def count_words(file):
    """count unique worl in a string"""
    load_texts = load_text(file)
    clean_text = clean_text(load_texts)
    words = clean_text.split()
    return Counter(words)
