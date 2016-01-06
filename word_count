import collections
import string
import csv

class WordCounter:

    def __init__(self, filename):
        self.f = open(filename, 'r')
        self.text = self.f.readlines()        # Stores file content in a list
        self.f.close()

    def removepunctuation(self):
        self.text = "".join(self.text)        # Converts list to string
        self.words = ""
        self.punct = set(string.punctuation)  # Creates a set of all punctuations
        for character in self.text:
            if(character not in self.punct):
                self.words += character
        self.words = self.words.split()       # Converts string into list without punctuations

    def findcount(self):
        self.countdict = {}
        self.countdict = collections.Counter(self.words) # Creates a dictionary with all words and counts

    def writecountfile(self,csvfilename):
        writer = csv.writer(open(csvfilename, 'wb'))
        self.sorted_names = sorted(self.countdict, key=lambda k: (-self.countdict[k], k)) # Sorts dictionary by values in descending order
        for k in self.sorted_names:
            writer.writerow([k, self.countdict[k]])


a = WordCounter('resume.txt')
a.removepunctuation()
a.findcount()
a.writecountfile('resume.csv')
