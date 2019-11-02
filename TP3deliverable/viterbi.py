
#logic for this function derived from reading the texts https://medium.com/syncedreview/applying-multinomial-naive-bayes-to-nlp-problems-a-practical-explanation-4f5271768ebf,https://www.slideshare.net/timruffles1/naturallanguage-processing-with-naive-bayes and https://web.stanford.edu/class/cs124/lec/naivebayes.pdf
from probabilitieCal import*
import math
import os

class ViterbiDecode:

    def __init__(self):
        self.emissionProbability = {}
        self.transitionProbability = {}
        self.tagsForWord = {}
        self.word_tag_viterbi_probability = {}
        self.index_tag_key = None
        self.firstTimeTag = set()
        self.bigramTagCount = None

    def recursive_probability_cal_sequence(self, word_sequence, index, word_tag_i):
        if index == 1: #base
            return 0.0

        if (index, word_tag_i) in self.word_tag_viterbi_probability: #memoisation
            return self.word_tag_viterbi_probability[index, word_tag_i][0]

        if word_sequence[index - 1] in self.tagsForWord:
            word_tags_i_1 = self.tagsForWord[word_sequence[index - 1]]
        else:
            word_tags_i_1 = self.firstTimeTag

        if word_sequence[index - 2] in self.tagsForWord:
            word_tags_i_2 = self.tagsForWord[word_sequence[index - 2]]
        else:
            word_tags_i_2 = self.firstTimeTag

        max_viterbi_prob = -1 #prob cant be negative anyway

        back_pointer_tag = "*"
        for word_tag_i_1 in word_tags_i_1:
            for word_tag_i_2 in word_tags_i_2:
                viterbi_prob = 0.0

                if (word_tag_i_2, word_tag_i_1, word_tag_i) in self.transitionProbability:
                    transition_prob = self.transitionProbability[(word_tag_i_2, word_tag_i_1, word_tag_i)]
                else:
                    if (word_tag_i_2, word_tag_i_1) in self.bigramTagCount:
                        transition_prob = (1.0 / float(self.bigramTagCount[(word_tag_i_2, word_tag_i_1)] + len(self.firstTimeTag)))
                    else:
                        transition_prob = (1.0 / float(len(self.firstTimeTag)))

                if (word_sequence[index], word_tag_i) not in self.emissionProbability:
                    transition_prob = 0.0
                    viterbi_prob = self.recursive_probability_cal_sequence(word_sequence, index - 1, word_tag_i_1) + \
                                   transition_prob
                else:
                    """Viterbi probability for any sequence is Viterbi Probability from previous words +
                     Emission probability for given word-tag sequence +
                     Transition probability for tag(i),tag(i-1),tag(i-2) formula from  https://web.stanford.edu/class/cs124/lec/naivebayes.pdf"""
                    viterbi_prob = self.recursive_probability_cal_sequence(word_sequence, index - 1, word_tag_i_1) + \
                                   self.emissionProbability[(word_sequence[index], word_tag_i)] + transition_prob
                if max_viterbi_prob < viterbi_prob: #checking the seq with max prob
                    max_viterbi_prob = viterbi_prob
                    back_pointer_tag = word_tag_i_1

        self.word_tag_viterbi_probability[index, word_tag_i] = (max_viterbi_prob, (index - 1, back_pointer_tag))
        return max_viterbi_prob

    def load(self):
        prob = calcProbabilities()
        prob.run('/users/anoushkatiwari/TP3deliverable/train.txt')
        self.transitionProbability =prob.transitionProbability
        self.emissionProbability =prob.emissionProbability
        self.tagsForWord = prob.tagsForWord
        self.firstTimeTag = prob.firstTimeTag
        self.bigramTagCount = prob.bigramTagCount

    def viterbi_algorithm(self,sentence):
       

        max_viterbi_prob = -1
        self.word_tag_viterbi_probability = {}
        # length of the current sentence
        sentence=sentence.split()
        len_sentence = len(sentence)
        if sentence[len_sentence - 1] in self.tagsForWord:
            word_tags_i = self.tagsForWord[sentence[len_sentence - 1]]
        else:
            word_tags_i = self.firstTimeTag

        for word_tag_i in word_tags_i:
            viterbi_prob = self.recursive_probability_cal_sequence(sentence, len_sentence - 1, word_tag_i)
        
            if max_viterbi_prob < viterbi_prob:
                max_viterbi_prob = viterbi_prob
                self.index_tag_key = (len_sentence - 1, word_tag_i)

        tagged_sentence = []
        while self.index_tag_key[0] >=2:
            tagged_sentence.insert(0, sentence[self.index_tag_key[0]] + "/" + self.index_tag_key[1])
            self.index_tag_key = self.word_tag_viterbi_probability[self.index_tag_key][1] 
        output=(" ".join(tagged_sentence) + "\n")
        return output
viterbi = ViterbiDecode()

    