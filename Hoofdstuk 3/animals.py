#!/usr/bin/env python3
from urllib.request import urlopen
import sys


# Get the animals
def fetch_animals(url):
    """Get a list of lines (animals) from a given URL.

    Args:
        url: The URL of a utf-8 text

    Returns:
        A list of lines.
    """
    with urlopen(url) as data:
        animals = []
        for animal in data:
            animals.append(animal.decode('utf-8').rstrip())
    return animals


# Print the animals given
def print_items(animals):
    """Prints all items from given collection.

        Args:
            animals: The collection to print.
        """
    for animal in animals:
        print(animal)


# Main method
def main(url):
    """Prints all lines (animals) from a given URL.

    Args:
        url: The URL of a utf-8 text
    """
    animals = fetch_animals(url)
    print_items(animals)


"""A list of lines printed from the given URL

Args:
    1: the URL to a UTF-8 text to print
    
Usage:
    python3 animals.py
"""
animalsUrl = 'https://raw.githubusercontent.com/BearWithAFez/Learning-Python/master/Hoofdstuk%202/animals.txt'
if __name__ == '__main__':
    main(sys.argv[1])
