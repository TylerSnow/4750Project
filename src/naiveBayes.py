import pickle

posCounter = 0
negCounter = 0
model = {}


# Args:
# TrainingFiles: This list of marked and tokenized training files
#                   [tokenized_revies, sentiment]
def naiveBayes(TrainingFiles):
    # Reads in unique words and updates their positive/negative counters
    for trainingSet in TrainingFiles:
        for review in trainingSet:
            for word in review[0]:
                trainModel(word, review[1])
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
def trainModel(word, sentiment):
    global posCounter
    global negCounter
    # try:
    if(word not in model):
        model[word] = [0, 0]
    if(sentiment == "neg"):
        model[word][0] += 1
        negCounter += 1
    elif(sentiment == "pos"):
        model[word][1] += 1
        posCounter += 1
    # print word, model[word]
    # except KeyError as e:
    #   if(posOrNeg==("pos")):
    #       model[word]=(0,1)
    #       posCounter += 1
    #   elif(posOrNeg==("neg")):
    #       model[word]=(1,0)
    #       negCounter += 1


# Method to generate trained model
def generateTrainedModel():
    trainedModel = {}
    trainedModel["words"] = {}
    totalCounter = float(posCounter + negCounter)
    for word in model:
        probOfWord = sum(model[word]) / totalCounter
        probOfWordNeg = model[word][0] / totalCounter
        probOfWordPos = model[word][1] / totalCounter
        trainedModel["words"][word] = (probOfWord, probOfWordNeg, probOfWordPos)

    return trainedModel


def main():
    naiveBayes("test")


if __name__ == '__main__':
    main()
