import pickle

posCounter=0
negCounter=0
model={}

def naiveBayes(TrainingFiles): #TrainingFiles is a list of tuples (filename, posOrNeg) 
	#Reads in unique words and updates their positive/negative counters 
	for fileNum in (range(len(TrainingFiles))):
		currentFile=open(TrainingFiles[fileNum][0],'r')
		for line in currentFile:
			for word in line:
				trainModel(word,TrainingFiles[fileNum][1])
	tModel=generateTrainedModel()
	naiveBayesFile=open("../bin/naiveBayesTrainedModel.bin",'w')
	pickle.dump(tModel,naiveBayesFile)
	naiveBayesFile.close()

#Method to update the model for each word
def trainModel(word,posOrNeg):
	try:
		if(posOrNeg==("pos")):
			model[word][1]+=1
			posCounter+=1
		elif(posOrNeg==("neg")):
			model[word][0]+=1
			negCounter+=1
	except KeyError as e:
		if(posOrNeg==("pos")):
			model[word]=(0,1)
			posCounter+=1
		elif(posOrNeg==("neg")):
			model[word]=(1,0)
			negCounter+=1

#Method to generate trained model
def GenerateTrainedModel():
	trainedModel={}
	for word in model:
		probNegative=model[word][0]/(model[word][0]+modelword[1])
		probPositive=model[word][1]/(model[word][0]+modelword[1])
		probOfWord=(model[word][0]+modelword[1])/(posCounter+negCounter)
		trainedModel[word]=(probOfWord,probNegative,probPositive)
	return trainedModel

