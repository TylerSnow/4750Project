import ttk
import Tkinter as tk
import tkFileDialog
import naiveBayes
import SVM
import train
import os
import sys

class UI:
    def callTrainSelectionMethods(self):
        if(len(self.train_Algorithms.curselection())!=0 and len(self.trainSet.curselection())!=0):
            alg=self.selectTrainAlg()
            trainSet=self.selectTrainer()
            trainPath=""
            if(trainSet=="IMDB Movie set"):
                trainPath="Datasets/aclImdb/train"
            elif(trainSet=="IMDB Movie subset"):
                trainPath="Datasets/debugSets/train"
                
            if(alg=="Naive Bayes"):
                nb=naiveBayes.NaiveBayes()
                nb.train(trainPath)
            elif(alg=="Support Vector Machine"):
                svm=SVM.SVM()
                svm.trainSVM(trainPath)
        else:
            print("Please select an algorithm and a test set.")

    def callTestSelectionMethods(self):
        if(len(self.testSet.curselection())!=0):
            
            testSet=self.selectTest()
            testPath=""
            #get selected test sets
            if(testSet=="IMDB Movie set(25000)"):
                testPath="Datasets/aclImdb/test"
            if(testSet=="IMDB Movie subset"):
                testPath="Datasets/debugSets/test"
            if(testSet=="Stanford Movie Set(2000)"):
                testPath="Datasets/stanfordMR/test"

            #Calculate accuracy of testVars of Naive bayes and SVM
            svm=SVM.SVM()
            svm.testSVM(testPath)
            nb=naiveBayes.NaiveBayes()
            nb.validate(testPath)
        else:
            print("Please select an algorithm and a test set.")
            
    def selectTrainAlg(self):
        clist = list()
        selection = self.train_Algorithms.curselection()
        for i in selection:
            choice= self.train_Algorithms.get(i)
            clist.append(choice)
        return clist[0]
    
    def selectTestAlg(self):
        clist = list()
        selection = self.test_Algorithms.curselection()
        for i in selection:
            choice= self.test_Algorithms.get(i)
            clist.append(choice)
        return clist

    def selectTest(self):
        tlist = list()
        selection = self.testSet.curselection()
        for i in selection:
            choice= self.testSet.get(i)
            tlist.append(choice)
        return tlist[0]

    def selectTrainer(self):
        tlist = list()
        selection = self.trainSet.curselection()
        for i in selection:
            choice= self.trainSet.get(i)
            tlist.append(choice)
        return tlist[0]

    def __init__(self, master):
        self.master = master
        self.master.title('Sentiment Analysis')
        self.master.geometry('800x800')
        self.master.option_add("*Button.Background", "white")
        self.master.option_add("*Button.Foreground", "red")
        self.master.option_add("*Label.Background","white")
        self.master.option_add("*Label.Foreground","red")
        self.master.configure(background='gray')

        for rows in range(80):
            master.rowconfigure(rows, weight=1)
            master.columnconfigure(rows, weight=1)

        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=1, column=0, columnspan=80, rowspan=80, sticky="NESW")

        # Creating the test page
        self.f_Test = tk.Frame(self.notebook)
        self.f_Test.configure(background='white')
        self.test_algLabel = tk.Label(self.f_Test, text="Testing Algorithm")
        self.test_algLabel.pack()
        
        self.test_Algorithms = tk.Listbox(self.f_Test, selectmode=tk.SINGLE, height=2, exportselection=0)
        self.test_Algorithms.insert(1, "Naive Bayes")
        self.test_Algorithms.insert(2, "Support Vector Machine")
        self.test_Algorithms.pack()
        self.test_data = tk.Label(self.f_Test, text = "Testing Dataset")
        self.test_data.pack()
        #Test data listbox with scrollview
        self.testDataFrame=tk.Frame(self.f_Test)
        self.testDataFrame.pack(fill=tk.Y)
        self.test_scrollbar=tk.Scrollbar(self.testDataFrame)
        self.test_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.testSet = tk.Listbox(self.testDataFrame, selectmode=tk.MULTIPLE, height=10, exportselection=0)
        self.testSet.config(yscrollcommand=self.test_scrollbar.set)
        self.test_scrollbar.config(command=self.testSet.yview)
        self.testSet.insert(1, "IMDB Movie set(25000)")
        self.testSet.insert(2, "IMDB Movie subset")
        self.testSet.insert(3, "Stanford Movie Set(2000)")
        self.testSet.pack()
        #Test page buttons
        self.test_button = tk.Button(self.f_Test, text="Test", command=self.callTestSelectionMethods)
        self.test_button.pack()

        self.test_close_button = tk.Button(self.f_Test, text="Close", command=master.quit)
        self.test_close_button.pack()

        # Creating the train page
        self.f_Train = tk.Frame(self.notebook)
        self.f_Train.configure(background='white')
        self.train_algLabel = tk.Label(self.f_Train, text="Training Algorithm")
        self.train_algLabel.pack()
        self.train_Algorithms = tk.Listbox(self.f_Train, selectmode=tk.SINGLE, height=2, exportselection=0)
        self.train_Algorithms.insert(1, "Naive Bayes")
        self.train_Algorithms.insert(2, "Support Vector Machine")
        self.train_Algorithms.pack()

        self.train_data = tk.Label(self.f_Train, text = "Training Dataset")
        self.train_data.pack()
        self.trainSet = tk.Listbox(self.f_Train, selectmode=tk.SINGLE, height=2, exportselection=0)
        self.trainSet.insert(1, "IMDB Movie set")
        self.trainSet.insert(2, "IMDB Movie subset")
        self.trainSet.pack()
        #Train page buttons
        self.train_button = tk.Button(self.f_Train, text="Train", command=self.callTrainSelectionMethods)
        self.train_button.pack()

        self.close_button = tk.Button(self.f_Train, text="Close", command=master.quit)
        self.close_button.pack()
        
        # Adding test and train pages to notebok
        self.notebook.add(self.f_Test, text="Testing")
        self.notebook.add(self.f_Train, text="Training")


def main():
    master = tk.Tk()
    UI(master)
    master.mainloop()


if __name__ == '__main__':
    main()
