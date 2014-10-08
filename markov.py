#!/usr/bin/env python

#import sys
import random


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    
# This section reads the corpus file in to the program and splits the words in a words list.     
    text = corpus.read() #this is functionally the same as the more complicated stuff below
    words = text.split()

    chain_dict = {}
    """
    for line in f:
        line = line.rstrip()
        words.extend(line.split())
     """   
#This looks at each word entry in the list that we made from original text - if the tuple does not yet exist,
#it appends it to the dictionary as a key. If it does exist, it appends the value to the existing key.

    for each_number in range(len(words)-2): 
        if (words[each_number], words[each_number+1]) not in chain_dict.keys():
            chain_dict[(words[each_number], words[each_number+1])] = [words[each_number+2]]
        else:
            chain_dict[(words[each_number], words[each_number+1])].append(words[each_number+2])
       
    return chain_dict

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

# This selects the first random key to begin the chain.
    
    random_key = random.choice(chain_dict.keys())
    print "Here's the original random key:"
    print random_key

# This creates a random text list to append a random value from the original random key.
# The random key is then reassigned to a tuple containing the second key in the random keys tuple,
# and adds the randomly generated value of the earlier random key tuple as the second tuple value. 
# MAGIC
    random_text_list = []

    for i in chain_dict.iteritems():    
        next = random.choice(chain_dict[random_key]) 
        
        random_text_list.append(next)
        print random_text_list

        random_key = random_key[1:] + (next,)
        print random_key


    
    
    #return random_key

def main():

#    args = sys.argv

    input_text = open("sherlock_test.txt")

    chain_dict = make_chains(input_text)


    random_text = make_text(chain_dict)
    print random_text, chain_dict[random_text] 


if __name__ == "__main__":
    main()