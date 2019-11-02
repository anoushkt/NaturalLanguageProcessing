
from read_data_from_file import *
import math
import os
class calcProbabilities:
    def __init__(self):
        self.wordTagCount = {} #occurrences of a word with a tag
        self.tagCount = {} #no of occurences of a tag
        self.trigramTagCount = {} #no of times 3 tags occuring together
        self.bigramTagCount = {} #no of times 2 tags occuring together
        self.emissionProbability = {} #prob a tag is related to a word
        self.transitionProbability = {} #prob of 3 tags occuring together
        self.tagsForWord = {}
        self.firstTimeTag = set()

    # calculate the word-tag counts
    def findTheCounts(self, filename):  #logic for this function derived from reading the texts https://medium.com/syncedreview/applying-multinomial-naive-bayes-to-nlp-problems-a-practical-explanation-4f5271768ebf,https://www.slideshare.net/timruffles1/naturallanguage-processing-with-naive-bayes and https://web.stanford.edu/class/cs124/lec/naivebayes.pdf
        read_files = ReadFiles(filename)
        all_tuples = read_files.word_tag_tuples()
        self.tagsForWord = read_files.tagsForWord
        self.firstTimeTag = read_files.firstTimeTag
        for sentence in all_tuples:
            for i in range(2, len(sentence)):
            
                if sentence[i] in self.wordTagCount:
                    self.wordTagCount[sentence[i]] += 1
                else:
                    self.wordTagCount[sentence[i]] = 1
                tag = sentence[i][1]    
                self.tagCount[tag] = self.tagCount.get(tag, 0) + 1
                words_trigram = (sentence[i-2][1],sentence[i-1][1],sentence[i][1])
                if words_trigram in self.trigramTagCount:
                    self.trigramTagCount[words_trigram] += 1
                else:
                    self.trigramTagCount[words_trigram] = 1
                words_bigram = (sentence[i-2][1], sentence[i - 1][1])
                if words_bigram in self.bigramTagCount:
                    self.bigramTagCount[words_bigram] += 1
                else:
                    self.bigramTagCount[words_bigram] = 1

  
    def run(self, filename):
        self.findTheCounts(filename)
        self.calculate_emissionProbability()
        self.calculate_transitionProbability()
    # conditional p(word/tag)
    def calculate_emissionProbability(self):
        for word_tag, wordTagCount in self.wordTagCount.items():
            self.emissionProbability[word_tag] = (float(wordTagCount)/float(self.tagCount[word_tag[1]]))
          

    # p(tag3/tag1,tag2)
    def calculate_transitionProbability(self):
        for trigram_tuple, trigram_tuple_count in self.trigramTagCount.items():
            bigram_count = self.bigramTagCount[(trigram_tuple[0],trigram_tuple[1])]
            firstTimetagCount = len(self.firstTimeTag)
            self.transitionProbability[trigram_tuple] = (float(trigram_tuple_count+1)/float(bigram_count + firstTimetagCount)) #laplace smoothing
           

if __name__ == "__main__":
    prob = calcProbabilities()
    prob.run('/users/anoushkatiwari/TP3/train.txt')