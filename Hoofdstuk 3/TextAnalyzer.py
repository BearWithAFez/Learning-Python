#!/usr/bin/env python3
from urllib.request import urlopen
import sys
import collections


# Get the animals
def fetch_text(url):
    """Get a list of lines (text) from a given URL.

    Args:
        url: The URL of a utf-8 text

    Returns:
        A list of lines.
    """
    with urlopen(url) as data:
        text = []
        for line in data:
            text.append(line.decode('utf-8').rstrip())
    return text


# Count all chars from given url text
def char_count(url):
    text = fetch_text(url)
    count = 0
    for line in text:
        count += len(line)

    return count


# Count all lines from given url text
def line_count(url):
    text = fetch_text(url)
    return len(text)


# Split given lines-text into words
def lines_to_words(lines):
    words = []
    for line in lines:
        for word in line.split():
            words.append(word)
    return words


# Count numbers of words
def word_count(url):
    lines = fetch_text(url)
    words = lines_to_words(lines)
    return len(words)


# makes a dict of [word][int]
def sort_by_unique_words(words):
    count = collections.defaultdict(int)
    for word in words:
        count[word] += 1
    return count


# Count the number of Unique words
def unique_word_count(url):
    lines = fetch_text(url)
    words = lines_to_words(lines)
    unique = sort_by_unique_words(words)
    return len(unique)


# Counts the number a given word is repeated
def word_repeated(word, url):
    lines = fetch_text(url)
    words = lines_to_words(lines)
    unique = sort_by_unique_words(words)
    return unique[word]


# Print the text given
def print_items(text):
    """Prints all items from given collection.

        Args:
            text: The collection to print.
        """
    for line in text:
        print(line)


# make a word of all first letters
def first_letters(url):
    lines = fetch_text(url)
    words = lines_to_words(lines)
    first = ''
    for word in words:
        first += word[0]
    return first


# Main method
def main(url):
    """Prints all lines (text) from a given URL.

    Args:
        url: The URL of a utf-8 text
    """
    print('Loaded.')
    text = fetch_text(url)
    print_items(text)
    print('Char count:')
    print(char_count(url))
    print('Line count:')
    print(line_count(url))
    print('Word count:')
    print(word_count(url))
    print('Unique word count:')
    print(unique_word_count(url))
    print('First letters combined')
    print(first_letters(url))


example_url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(word_repeated(sys.argv[1], example_url))
    else:
        main(example_url)
