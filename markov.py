#!/usr/bin/env python

#import sys



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
     

    f = open("sherlock.txt")

    words = []
    chain_dict = {}

    for line in f:
        line = line.rstrip()
        words.extend(line.split())

        #tuple(words[int(incrementor)], words[int(incrementor+1)])
        #incrementor = incrementor + 1
        print words

    for each_number in range(len(words)-1):
        #current_word=words[each_number]
        chain_dict[(words[each_number], words[each_number+1])] = [words[each_number+2]]
        print chain_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    pass
    #return "Here's some random text."

def main():
#    args = sys.argv

    # Change this to read input_text from a file
    input_text = "A Scandal in Bohemia"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()