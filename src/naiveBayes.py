import pickle
import os
import ourTokenizer
import sys
import math


class NaiveBayes:

    # Args:
    #     self
    #     dataPath - The path to the directory that contains sorted data
    #               This directory should have 2 directories in it
    #               one for negative named neg and one for positive named pos
    def __init__(self):
        self.model = {}
        self.wordCounts = {}
        self.wordCounts["posCounter"] = 0
        self.wordCounts["negCounter"] = 0
        self.wordCounts["words"] = {}
        self.root_path=os.path.dirname(os.path.abspath(__file__))
        self.parent_path=os.path.dirname(os.path.abspath(self.root_path))

    def train(self, TrainingPath):
        TrainingPath=os.path.join(self.parent_path,TrainingPath)
        if(os.path.isdir(TrainingPath) and os.path.exists(TrainingPath)):
            for root, dirs, files in os.walk(TrainingPath):
                for dir in dirs:
                    if(dir == 'pos'):
                        self.posPath = os.path.join(TrainingPath, dir)
                    if(dir == 'neg'):
                        self.negPath = os.path.join(TrainingPath, dir)

            # Tokenizing training files and getting word counts
            for root, dirs, files in os.walk(self.posPath):
                for file in files:
                    filename = os.path.join(root, file)
                    tokenized = ourTokenizer.tokenize_file(ourTokenizer.readFile(filename))
                    self.countWords(tokenized, "pos")

            for root, dirs, files in os.walk(self.negPath):
                for file in files:
                    filename = os.path.join(root, file)
                    tokenized = ourTokenizer.tokenize_file(ourTokenizer.readFile(filename))
                    self.countWords(tokenized, "neg")

            self.generateTrainedModel()
        else:
            print "{} is does not exist of isn't a directory".format(TrainingPath)
            sys.exit(1)

        return self.trainedModel

    # total = sum(model['the'])
    # totalCounter = negCounter + posCounter
    # prob_the_neg = model['the'][0] / float(negCounter)
    # prob_the_pos = model['the'][1] / float(posCounter)
    # prob_the = total / float(totalCounter)
    # prob_pos = posCounter / float(totalCounter)
    # prob_neg = negCounter / float(totalCounter)

    # prob_pos_the = (prob_the_pos * prob_pos) / prob_the
    # prob_neg_the = (prob_the_neg * prob_neg) / prob_the
    # print("P(pos|the) = {}".format(prob_pos_the))
    # print("P(neg|the) = {}".format(prob_neg_the))
    # model['the'][1]/model['the'][0]+model['the'][1]

    # Method to update the model for each word
    def countWords(self, words, sentiment):
        for word in words:
            if(word not in self.wordCounts["words"]):
                self.wordCounts["words"][word] = [0, 0]
            if(sentiment == "neg"):
                self.wordCounts["words"][word][0] += 1
                self.wordCounts["negCounter"] += 1
            elif(sentiment == "pos"):
                self.wordCounts["words"][word][1] += 1
                self.wordCounts["posCounter"] += 1

    # Method to generate trained model
    def generateTrainedModel(self):
        self.trainedModel = {}
        self.trainedModel["words"] = {}
        self.trainedModel["negCounter"] = self.wordCounts["negCounter"]
        self.trainedModel["posCounter"] = self.wordCounts["posCounter"]

        totalCounter = float(self.trainedModel["posCounter"] + self.trainedModel["negCounter"])
        for word in self.wordCounts["words"]:
            # The probability of the word occuring
            probOfWord = sum(self.wordCounts["words"][word]) / float(totalCounter)
            # The probability of the word occuring given a negative sentiment
            probOfWordNeg = self.wordCounts["words"][word][0] / float(self.trainedModel["negCounter"])
            # The probability of the word occuring given a positive sentiment
            probOfWordPos = self.wordCounts["words"][word][1] / float(self.trainedModel["posCounter"])

            self.trainedModel["words"][word] = [probOfWord, probOfWordNeg, probOfWordPos]
        self.pkl_model()

    # Method to test classification accuracy of the model
    #
    # Args:
    #     testPath - the path to the test data
    #                the test data should countain 2 directories
    #                one for the negative data named neg
    #                one for the positive data named pos
    def validate(self, validatePath):
        validatePath=os.path.join(self.parent_path,validatePath)
        self.trainedModel = self.pkl_to_model()
        fileCount = 0
        correctCount = 0
        for root, dirs, files in os.walk(validatePath):
            for dire in dirs:
                #print dire
                for root1, dirs1, files1 in os.walk(os.path.join(root, dire)):
                    for file in files1:
                        fileCount += 1
                        filename = os.path.join(root1, file)
                        sentiment = self.test(filename)
                        if(sentiment == dire):
                            correctCount += 1

        accuracy = correctCount / float(fileCount)
        print "Naive Bayes accuracy: {}".format(accuracy)
        return accuracy

    def test(self, filename):
        name = ""
        for root, firs, file in os.walk(name):
            name = os.path.join(root, name)

        tokenized = ourTokenizer.tokenize_file(ourTokenizer.readFile(filename))
        # p(features | neg)
        prob_words_neg = 0
        # p(features | pos)
        prob_words_pos = 0
        # p(features)
        probOfWords = 0

        totalCounter = self.trainedModel["negCounter"] + self.trainedModel["posCounter"]
        total_prob_neg = self.trainedModel["negCounter"] / float(totalCounter)
        total_prob_pos = self.trainedModel["posCounter"] / float(totalCounter)

        for word in tokenized:
            if(word in self.trainedModel["words"]):
                probOfWords += math.log(self.trainedModel["words"][word][0])
                if(self.trainedModel["words"][word][1] != 0):
                    prob_words_neg += math.log(self.trainedModel["words"][word][1])
                if(self.trainedModel["words"][word][2] != 0):
                    prob_words_pos += math.log(self.trainedModel["words"][word][2])

        # print("probOfWords", probOfWords)
        # print("prob_words_neg", prob_words_neg)
        # print("prob_words_pos", prob_words_pos)
        prob_neg = prob_words_neg + math.log(total_prob_neg) - probOfWords
        prob_pos = prob_words_pos + math.log(total_prob_pos) - probOfWords

        sentiment = ""
        if(prob_pos < prob_neg):
            sentiment = "pos"
        else:
            sentiment = "neg"

        #print "{}".format(filename)
        #print "sentiment: {}".format(sentiment)
        #print "positive: {}".format(prob_pos)
        #print "negative: {}".format(prob_neg)

        return sentiment

    def pkl_model(self):
        with open("../bin/NaiveBayes_Trained.pkl", "wb") as file:
            pickle.dump(self.trainedModel, file)

    def pkl_to_model(self):
        with open("../bin/NaiveBayes_Trained.pkl", "rb") as file:
            return pickle.load(file)
