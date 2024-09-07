import re
from collections import Counter

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)     # Replace multiple spaces with single space
    return text.lower().strip()

# Full paths to your text files on desktop
amharic_file_path = './Amharic_2_utf8.txt'
tigrigna_file_path = './Tigrigna_2_utf8.txt'

# Read text files
with open(amharic_file_path, 'r', encoding='utf-8') as file:
    amharic_text = file.read()
with open(tigrigna_file_path, 'r', encoding='utf-8') as file:
    tigrigna_text = file.read()

# Preprocess texts
amharic_text = preprocess_text(amharic_text)
tigrigna_text = preprocess_text(tigrigna_text)

# Function to count word frequency
def word_frequency(text):
    words = text.split()
    return Counter(words)

# Compute word frequency
amharic_word_freq = word_frequency(amharic_text)
tigrigna_word_freq = word_frequency(tigrigna_text)

# Compute word overlap
amharic_words = set(amharic_word_freq.keys())
tigrigna_words = set(tigrigna_word_freq.keys())
word_overlap = amharic_words.intersection(tigrigna_words)

# Function to transcribe text into phonemes (placeholder)
def g2p_convert(text):
    # Placeholder function, actual implementation needed for phoneme conversion
    return text

# Transcribe texts into phonemes
amharic_phonemes = g2p_convert(amharic_text)
tigrigna_phonemes = g2p_convert(tigrigna_text)

# Function to compute phoneme distribution
def phoneme_distribution(text):
    phonemes = text.split()
    return Counter(phonemes)

# Compute phoneme distribution
amharic_phoneme_dist = phoneme_distribution(amharic_phonemes)
tigrigna_phoneme_dist = phoneme_distribution(tigrigna_phonemes)

# Compute phoneme overlap
amharic_phoneme_set = set(amharic_phoneme_dist.keys())
tigrigna_phoneme_set = set(tigrigna_phoneme_dist.keys())
phoneme_overlap = amharic_phoneme_set.intersection(tigrigna_phoneme_set)

# Print results
print("Word frequency count:")
print("Amharic:", amharic_word_freq)
print("Tigrigna:", tigrigna_word_freq)
print("Word overlap:", word_overlap)
print("Number of overlapping words:",len(word_overlap))
