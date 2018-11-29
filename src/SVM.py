import sklearn
import pickle
import os
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import datasets
from sklearn.pipeline import Pipeline

class SVM:
    def __init__(self):
        self.pipeline_filename="../bin/SVM_TrainedPipeline.pkl"
        self.root_path=os.path.dirname(os.path.abspath(__file__))
        self.parent_path=os.path.dirname(os.path.abspath(self.root_path))
        
    def trainSVM(self,trainPath):
        trainPath=os.path.join(self.parent_path,trainPath)
        trainFiles=sklearn.datasets.load_files(trainPath, shuffle=True)
        pipeline=Pipeline([('vect',CountVectorizer(analyzer='word',stop_words=["the","is","an","and"])),('clf',sklearn.svm.LinearSVC()),])
        pipeline.fit(trainFiles.data,trainFiles.target)
        self.pkl_model(pipeline)
       
    def testSVM(self,testPath):
        testPath=os.path.join(self.parent_path,testPath)
        print(testPath)
        pipeline=self.unpkl_to_model()
        #self.graphData(pipeline)
        testFiles=sklearn.datasets.load_files(testPath, shuffle=True)
        predicted= pipeline.predict(testFiles)
        score=pipeline.score(testFiles.data,testFiles.target)
        print "SVM accuracy: {}".format(score)
        return score

    def pkl_model(self,pipeline):
        with open(self.pipeline_filename,'wb') as file:
            pickle.dump(pipeline,file)

    def unpkl_to_model(self):
        with open(self.pipeline_filename, 'rb') as file:  
            pipeline=(pickle.load(file))
        return pipeline

    def graphData(self,pipeline):
        data=pipeline.get_params()
        print(data['clf'].densify())
        #plots input data
        plt.scatter(data['clf'].densify,range(0,len(data['clf'].densify())))
        plt.show()


def main():
    svm=SVM()
    root_path=os.path.dirname(os.path.abspath(__file__))
    parent_path=os.path.dirname(os.path.abspath(root_path))
    train_dir=os.path.join(parent_path,"Datasets/debugSets/train/")
    test_dir=os.path.join(parent_path,"Datasets/debugSets/test/")
        
    #svm.trainSVM(train_dir)
    #svm.testSVM(test_dir)


if __name__ == "__main__":
    main()
