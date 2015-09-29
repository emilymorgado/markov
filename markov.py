from random import choice
from sys import argv

input_file = argv[1]


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_contents = open(file_path).read()
    # your code goes here

    return file_contents


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) in chains:
            chains[words[i], words[i + 1]].append(words[i + 2])
        else:
            chains[words[i], words[i + 1]] = [words[i + 2]]

    return chains

    # (would, you) [could]
    # (you, could) [you]


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    random_key = choice(chains.keys())
    text = random_key[0] + " " + random_key[1]
    list_of_words = chains[random_key]
    next_word = choice(list_of_words)
    text += " " + next_word

    while True:
        text_split = text.split()
        new_pair = (text_split[-2], text_split[-1])
        if new_pair in chains:
            new_pair_list_of_words = chains[new_pair]
            new_next_word = choice(new_pair_list_of_words)
            text += " " + new_next_word
        else:
            break
            
    print text
    # print text
    # your code goes here

    # return text

    #random.choice(seq) = returns random element from non-empty seq


input_path = input_file

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
