import sklearn
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

def trainSVM(path):
    files=sklearn.datasets.load_files(path, shuffle=True)
    #print(files)
    model=CountVectorizer(analyzer='word',stop_words=["the","is","an","and"])
    X_train=model.fit_transform(files.data)
    #print(X_train.toarray())
    tf_transformer = TfidfTransformer()
    #X = tf_transformer.fit_transform(X_train)
    pipeline=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),])
    print(pipeline)
    X = pipeline.fit_transform(files.data).todense()
    pca=PCA(n_components=2).fit(X)
    data=pca.transform(X)
    #plots input data
    plt.scatter(data[:,0],data[:,1],c=files.target)
    plt.show()
    clf = sklearn.svm.LinearSVC()
    test_classifier(X, files.target, clf, test_size=0.2, y_names=files.target_names, confusion=False)

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

def main():
    root_path=os.path.dirname(os.path.abspath(__file__))
    parent_path=os.path.dirname(os.path.abspath(root_path))
    pos_dir=os.path.join(parent_path,"Datasets/testSets")
    trainSVM(pos_dir)

if __name__ == "__main__":
    main()
