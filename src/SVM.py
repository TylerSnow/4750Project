import sklearn
import pickle
import os
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import datasets
from sklearn import cross_validation
from sklearn.model_selection import cross_val_score;
import pprint as pp
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline


pkl_filename="SVM_TrainedModel.pkl"

def trainSVM(trainPath,testPath):
    trainFiles=sklearn.datasets.load_files(trainPath, shuffle=True)
    testFiles=sklearn.datasets.load_files(testPath, shuffle=True)
    model=CountVectorizer(analyzer='word',stop_words=["the","is","an","and"])
    X_train=model.fit_transform(trainFiles.data)
    X_test=model.transform(testFiles.data)
    clf = sklearn.svm.LinearSVC()
    clf.fit(X_train,trainFiles.target)
    predicted= clf.predict(X_test)
    score=clf.score(X_test,testFiles.target)
    #plt.scatter(predicted,c='r')
    #plt.show()
    print(score)
    
    #test_classifier(X, files.target, clf, test_size=0.2, y_names=files.target_names, confusion=False)

def test_classifier(X, y, clf, test_size=0.3, y_names=None, confusion=False):
    #train-test split
    X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(X, y, test_size=test_size)
    clf.fit(X_train, y_train)
    y_predicted = clf.predict(X_test)
    #print(X_train[:,0].todense(),X_train[:,1].todense())
    #plt.scatter(X_test[:,0].todense(),X_test[:,1].todense(),c='b')
    print(y_test)
    print(y_predicted)
    #plt.scatter(y_predicted/X_test,c='r')
    plt.show()

def pkl_model(model):
    with open(pkl_filename,'wb') as file:
        pickle.dump(model,file)

def unpkl_to_model():
    with open(pkl_filename, 'rb') as file:  
        pickle_model = pickle.load(file)
    return pickle_model

def graphData():
    tf_transformer = TfidfTransformer()
    #X = tf_transformer.fit_transform(X_train)
    pipeline=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),])
    print(pipeline)
    X = pipeline.fit_transform(trainFiles.data).todense()
    pca=PCA(n_components=2).fit(X)
    data=pca.transform(X)
    #plots input data
    #plt.scatter(data[:,0],data[:,1],c=trainFiles.target)
    #plt.show()

def main():
    root_path=os.path.dirname(os.path.abspath(__file__))
    parent_path=os.path.dirname(os.path.abspath(root_path))
    train_dir=os.path.join(parent_path,"Datasets/debugSets/train/")
    test_dir=os.path.join(parent_path,"Datasets/debugSets/test/")
    
    model=trainSVM(train_dir,test_dir)
    pkl_model(model)


if __name__ == "__main__":
    main()
