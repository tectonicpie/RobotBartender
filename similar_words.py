#-------------------------------------------------------------------------------
# Name:        SimilarWords
# Purpose:      checks finds the label with phrases most similar to a
#               phrase interpreted by sst
#
# Author:      SGreenstein
#
# Created:     30/11/2013
# Copyright:   (c) SGreenstein 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import stt_google
from collections import Counter

class SimilarWords:

    def __init__(self, fname):
        """Returns an instance of SimilarWords for finding the best label for a phrase

        Keyword arguments:
        fname -- string, specifies csv file of training data
        """
        self.instances = {} #dictionary. Key: label, value: Counter of word frequencies
        self.train(fname)

    def train(self, fname):
        """Reads a file of training data and creates self.instances for future use

        Keyword arguments:
        fname -- string, filename of csv file with training data
        training data is of the following format:
            label1, hypothesis number one, hypothesis number two,
            label1, hypothesis one,
            label2, hypothesis one, et cetera
        """
        #open file
        csvfile = open(fname, 'rb')
        reader = csv.reader(csvfile)
        instances = self.instances
        #read file into correct format, counting weighted word frequencies
        for row in reader:
            label = row.pop(0)
            if(label in instances):
                word_freqs = instances[label]
            else:
                word_freqs = Counter()
            for index, phrase in enumerate(row):
                for word in phrase.split():
                    #weight by the order Google guessed it in
                    #i.e. first guesses weighted more
                    word_freqs[word] += 1 / float(index + 1)
                instances[label] = word_freqs
        csvfile.close
        #reduce weight of words common to many labels
        #find total frequencies of words
        avg_word_freqs = Counter()
        for word_freqs in instances.itervalues():
            avg_word_freqs += word_freqs
        #convert from total to average
        for word in avg_word_freqs:
            avg_word_freqs[word] /= len(instances)
        #subtract the average frequency of each word
        for label in instances:
            instances[label] -= avg_word_freqs
        self.instances = instances

    def classify(self, hypotheses):
        """Finds the best label based on word frequencies

        Keyword arguments:
        hypotheses -- result from Google stt to classify
        """
        bestSimilarity= 0
        for label, word_freqs in self.instances.iteritems():
            similarity = 0
            for index, hypothesis in enumerate(hypotheses):
                phrase = hypothesis['utterance']
                for word in phrase.split():
                    similarity += word_freqs[word] / float(index + 1)
            if similarity >= bestSimilarity:
                bestSimilarity = similarity
                bestLabel = label
            print label
            print word_freqs
            print similarity
        return bestLabel

def main():
    stt = stt_google
    sim = SimilarWords('drink_training.csv')
    print sim.classify(stt.listen_for_speech())

if __name__ == "__main__":
    main()