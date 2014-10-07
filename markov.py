#!/usr/bin/env python

#import sys
import random


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
     

    f = corpus

    words = []
    chain_dict = {}

    for line in f:
        line = line.rstrip()
        words.extend(line.split())

    for each_number in range(len(words)-2): #does this actually solve the range problem?
        chain_dict[(words[each_number], words[each_number+1])] = [words[each_number+2]]
        each_number = each_number + 1

    return chain_dict

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    random_key = random.choice(chain_dict.keys())
   
    print "Here's some random text: %s and %s" % (random_key, chain_dict[random_key])

    return random_key

def main():
#    args = sys.argv

    # Change this to read input_text from a file
    input_text = open("sherlock.txt")

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)

    print random_text, chain_dict[random_text]

if __name__ == "__main__":
    main()