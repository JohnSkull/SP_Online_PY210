#!/usr/bin/env python3

'''
Objectives
Katas are about trying something many times. In this one, what we’re experimenting with is not just the code, but the heuristics of processing the text. What do we do with punctuation? Paragraphs? Do we have to implement backtracking if we chose a next word that turns out to be a dead end?

I’ll fire the signal and the fun will commence…
'''

import random
import sys

filename = (r"C:\Users\cliff\SP_Online_PY210\students\clifford_butler\lesson04\sherlock.txt")
word_limit = 100

def read_in_data(filename):
    '''
    read and clean the data to be used for the process
    starting with the header and ending with the footers
    skipping the header and ensuring the programs reads 
    until the end of the text
    '''
    lines = list()
    chars = str.maketrans(',.?!;()', '       ')
    header = ('*** START OF THIS PROJECT GUTENBERG EBOOK')

    for line in read_file:
        if line.find(header) != -1:
            break
    for line in read_file:
        if line.isspace():
            continue
        elif line.find('End of the Project Gutenberg EBook') != -1:
            break
        else:
            line = line.translate(chars)
            line = line.replace('"', '')
            line = line.replace('--', ' ')
            lines.append(line.lower())
    return lines

def make_words(in_data):
    '''
    build a list of words based on the text file
    returns a list to be used for building the trigrams
    '''
    words = list()
    for line in in_data:
        words.extend(line.split())
    return words

def build_trigrams(words):
    '''
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    '''
    trigrams = {}
    for i in range(len(words) -2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        trigrams.setdefault(tuple(pair),[]).append(follower)
    return trigrams
    
def build_text(trigrams):
    '''
    build the text based on the trigrams dict
    picks a random first pair of words
    adding new words to the list using the
    last two words in teh list as wor pairs
    '''
    first_pair = random.choice(list(trigrams))
    new_list = list(first_pair)
    new_list.append(random.choice(trigrams[first_pair]))
    count = 3
    while count < word_limit:
        if tuple(new_list[-2:]) in trigrams:
            new_list.append(random.choice(trigrams[tuple(new_list[-2:])]))
            count += 1
        elif count == word_limit-1:
            new_list.append(first_pair[0])
            count += 1
        elif count == word_limit-2:
            new_list.append(first_pair[0])
            new_list.append(first_pair[1])
            count += 2
        else:
            new_list.append(first_pair[0])
            new_list.append(first_pair[1])
            new_list.append(random.choice(trigrams[first_pair]))
            count += 3
    new_text = " ".join(new_list)
    return new_text 

if __name__ == "__main__":
    '''
    Runs the main funtion. Validating the file chosen exist. 
    If the file does not exists, the program will prompt so and exit.
    '''    
    try:
        read_file = open(filename, 'r')
    except FileNotFoundError:
        print(filename, ': this file was not found.')
        sys.exit()
    # runs throough the functions to generate new text    
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)