#!/usr/bin/env python

#import sys
import random


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
     

    text = corpus.read() #this is functionally the same as the more complicated stuff below
    words = text.split()

    chain_dict = {}
    """
    for line in f:
        line = line.rstrip()
        words.extend(line.split())
     """   

    for each_number in range(len(words)-2): #does this actually solve the range problem?
        if words[each_number] not in chain_dict.keys():
            chain_dict[(words[each_number], words[each_number+1])] = [words[each_number+2]]
            print "New word added!"
        else:
            words[each_number+2].append(words[each_number+2])
            #chain_dict[(words[each_number], words[each_number+1])] = [words[each_number+2].append()]
            print "This should be appending!"
       #(add in things for when it exists)

    return chain_dict

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    random_key = random.choice(chain_dict.keys())
    
    return random_key

def main():
#    args = sys.argv

    # Change this to read input_text from a file
    input_text = open("sherlock_test.txt")

    chain_dict = make_chains(input_text)


    for i in range (1,100):
        random_text = make_text(chain_dict)
        print random_text, chain_dict[random_text] 


if __name__ == "__main__":
    main()