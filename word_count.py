#!/usr/bin/env python

import collections
import string
import csv
import sys

def count_words(input, output):

    with open(input, 'r') as input_file:
        text = input_file.read()
    wordstring = text.translate(None, string.punctuation)
    wordlist = wordstring.split()
    counts = collections.Counter(wordlist)
    ordered = counts.most_common()
    with open(output, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(ordered)


if __name__ == '__main__':

    try:
        if len(sys.argv) == 3:
            input, output = sys.argv[1:3]
            count_words(input, output)
        else:
            print "Usage: %s INPUT_FILE.txt OUTPUT_FILE.csv" % sys.argv[0]
            sys.exit(1)
    except IOError:
        print "No such file or directory: %s" % sys.argv[1]
        sys.exit(1)
