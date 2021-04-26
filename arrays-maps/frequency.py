# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Word Frequency
#
# NAME:         FIXME
# ASSIGNMENT:   Technical HW: Arrays & Maps

from operator import itemgetter
import string

import json

# Create a function word_frequencies that takes
# a string filename as a parameter and returns a
# dictionary mapping each word in the text file
# to the total number of times it occurs. All
# letters should be treated as lower case, and both
# punctuation and numbers should be ignored.
# Letters separated by apostrophes should be left together.
# Your solution may use string & file functions.
# Hint: see https://www.techiedelight.com/remove-punctuations-string-python/
def word_frequencies(filename):
    d = {}
    f=open(filename,'r')
    h=f.read()
    print(type(h))
    h=h.replace('-',' ')
    h=h.replace('(','')
    h=h.replace(')','')
    h=h.replace(',','')
    h=h.replace("'","")
    h=h.replace('.','')
    
    
    h=h.split()
    for a in h:
      if a.isdigit():
        h.remove(a)

    #print(h) 
    

    for k in h:
      k=k.lower()
      if k not in d.keys():
        d[k]=1
      else:
        d[k] +=1
    return d

def print_map_by_value(map):
    for k, v in sorted(map.items(), key=itemgetter(1), reverse=True):
        print("%6d %s" % (v, k) )


def main():
    #files = ["pytest", "turing", "austen"]
    # files = ["pytest", "turing"]
    #files = ["pytest"] # once this works, try the others!
    files = ["turing"]
    for f in files:
        print("=" * 10, f, "=" * 10)
        print_map_by_value(word_frequencies("files/"+f+".txt"))

# Don't run main on import
if __name__ == "__main__":
    main()