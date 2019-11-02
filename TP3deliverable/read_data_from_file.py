
import os
class ReadFiles:
    def __init__(self, file_name):
        self.file_name = file_name
        # list of list of tuples of sentences.
        self.all_tuples = []
                                    
        self.tagsForWord = {}                                                    
        
        self.firstTimeTag = set() 
    def word_tag_tuples(self):
        with open(self.file_name, "rt") as f:
            text=f.read()
     
        for line in text.splitlines():                                                                                                   
            list_tuples_sentence = []
            tuple_words = line.split()
            for tup in tuple_words:
                split_word = tup.split('/')
                splitWordTheWord = split_word[0]
                split_word_tag = split_word[-1]
                if split_word_tag not in self.firstTimeTag:
                    self.firstTimeTag.add(split_word_tag)
                # word-tag pair
                tuples_for_sentence = (splitWordTheWord,split_word_tag)
                list_tuples_sentence.append(tuples_for_sentence)
                if splitWordTheWord in self.tagsForWord:
                    tags_set = self.tagsForWord[splitWordTheWord]
                    tags_set.add(split_word_tag)
                else:
                    tags_set = set([split_word_tag])
                    self.tagsForWord[splitWordTheWord] = tags_set
            list_tuples_sentence.insert(0,('*','*'))  #idea for this line taken from https://medium.com/syncedreview/applying-multinomial-naive-bayes-to-nlp-problems-a-practical-explanation-4f5271768ebf 
            list_tuples_sentence.insert(0, ('*', '*'))
            self.all_tuples.append(list_tuples_sentence)
            self.tagsForWord["*"] = "*" #idea for this line taken from https://medium.com/syncedreview/applying-multinomial-naive-bayes-to-nlp-problems-a-practical-explanation-4f5271768ebf 
        return self.all_tuples

    def word_raw(self):

        all_tuples_raw = []

        with open(self.file_name, "r") as f:
            for line in f.splitlines():
               
                #tuples for a sentence
                list_tuples_sentence = []

                # splitting the sentences at space
                tuple_words = line.split()
                for tup in tuple_words:
                    list_tuples_sentence.append(tup)
                list_tuples_sentence.insert(0, ('*'))
                list_tuples_sentence.insert(0, ('*'))

                all_tuples_raw.append(list_tuples_sentence)

        return all_tuples_raw
