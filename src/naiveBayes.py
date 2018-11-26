# import pickle


# Args:
# TrainingFiles: This list of marked and tokenized training files
#                   [tokenized_revies, sentiment]
def naiveBayes(TrainingFiles):
    model = {}
    model["posCounter"] = 0
    model["negCounter"] = 0
    model["words"] = {}
    # Reads in unique words and updates their positive/negative counters
    for trainingSet in TrainingFiles:
        for review in trainingSet:
            for word in review[0]:
                trainModel(model["words"], word, review[1])
    total = sum(model['the'])
    totalCounter = model["negCounter"] + model["posCounter"]
    prob_the_neg = model["words"]['the'][0] / float(model["negCounter"])
    prob_the_pos = model["words"]['the'][1] / float(model["posCounter"])
    prob_the = total / float(totalCounter)
    prob_pos = model["posCounter"] / float(totalCounter)
    prob_neg = model["negCounter"] / float(totalCounter)

    prob_pos_the = (prob_the_pos * prob_pos) / prob_the
    prob_neg_the = (prob_the_neg * prob_neg) / prob_the
    print("P(pos|the) = {}".format(prob_pos_the))
    print("P(neg|the) = {}".format(prob_neg_the))
    # model['the'][1]/model['the'][0]+model['the'][1]


# Method to update the model for each word
def trainModel(wordDict, word, sentiment):
    # try:
    if(word not in wordDict):
        wordDict[word] = [0, 0]
    if(sentiment == "neg"):
        wordDict[word][0] += 1
        wordDict["negCounter"] += 1
    elif(sentiment == "pos"):
        wordDict[word][1] += 1
        wordDict["posCounter"] += 1
    # print word, model[word]
    # except KeyError as e:
    #   if(posOrNeg==("pos")):
    #       model[word]=(0,1)
    #       posCounter += 1
    #   elif(posOrNeg==("neg")):
    #       model[word]=(1,0)
    #       negCounter += 1


# Method to generate trained model
def generateTrainedModel(model):
    trainedModel = {}
    trainedModel["words"] = {}
    words = model["words"]
    totalCounter = float(model["posCounter"] + model["negCounter"])
    for word in words:
        # The probability of the word occuring
        probOfWord = sum(words[word]) / totalCounter
        # The probability of the word occuring given a negative sentiment
        probOfWordNeg = model[word][0] / model["negCounter"]
        # The probability of the word occuring given a positive sentiment
        probOfWordPos = model[word][1] / model["posCounter"]

        trainedModel[words][word] = (probOfWord, probOfWordNeg, probOfWordPos)
    return trainedModel


def main():
    naiveBayes("test")


if __name__ == '__main__':
    main()
