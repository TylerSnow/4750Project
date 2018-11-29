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
            elif(trainSet=="Custom Set 1"):
                trainPath="Datasets/custom1/train"
            elif(trainSet=="Custom Set 2"):
                trainPath="Datasets/custom2/train"
            elif(trainSet=="Custom Set 3"):
                trainPath="Datasets/custom3/train"
                
                
            if(alg=="Naive Bayes"):
                nb=naiveBayes.NaiveBayes()
                nb.train(trainPath)
            elif(alg=="Support Vector Machine"):
                svm=SVM.SVM()
                svm.trainSVM(trainPath)
        else:
            print("Please select an algorithm and a test set.")

    def callTestSelectionMethods(self):
        naiveTestResults=[]
        sVMTestResults=[]
        testSetName=[]
        if(len(self.testSet.curselection())!=0):
            
            testSet=self.selectTest()
            for curSet in testSet:
                testPath=""
            #get selected test sets
                if(curSet=="IMDB Movie set(25000)"):
                    testPath="Datasets/aclImdb/test"
                if(curSet=="IMDB Movie subset"):
                    testPath="Datasets/debugSets/test"
                if(curSet=="Stanford Movie Set(2000)"):
                    testPath="Datasets/stanfordMR/test"
                if(curSet=="Custom Set 1"):
                    testPath="Datasets/custom1/test"
                if(curSet=="Custom Set 2"):
                    testPath="Datasets/custom2/test"
                if(curSet=="Custom Set 3"):
                    testPath="Datasets/custom3/test"

                testSetName.append(curSet)
                #Calculate accuracy of testVars of Naive bayes and SVM
                svm=SVM.SVM()
                sVMTestResults.append(svm.testSVM(testPath))
                nb=naiveBayes.NaiveBayes()
                naiveTestResults.append(nb.validate(testPath))
        else:
            print("Please select an algorithm and a test set.")
        for k in range(1,6):
            self.f_TResults.grid_slaves(k, 0)[0].delete(0,tk.END)
            self.f_TResults.grid_slaves(k, 2)[0].delete(0,tk.END)
            self.f_TResults.grid_slaves(k, 1)[0].delete(0,tk.END)
        for i in range(1,len(testSetName)+1):
            self.f_TResults.grid_slaves(i, 0)[0].insert(0,testSetName[i-1])
            self.f_TResults.grid_slaves(i, 2)[0].insert(0,sVMTestResults[i-1])
            self.f_TResults.grid_slaves(i, 1)[0].insert(0,naiveTestResults[i-1])
            
        print(testSetName)
        print(sVMTestResults)
        print(naiveTestResults)
        self.f_Test.update()
            
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
        return tlist

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
        self.testSet.insert(2, "IMDB Movie subset(650)")
        self.testSet.insert(3, "Stanford Movie Set(2000)")
        self.testSet.insert(4, "Custom Set 1")
        self.testSet.insert(5, "Custom Set 2")
        self.testSet.insert(6, "Custom Set 3")
        self.testSet.pack()
        #Test page buttons
        self.test_button = tk.Button(self.f_Test, text="Test", command=self.callTestSelectionMethods)
        self.test_button.pack()


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
        self.trainSet = tk.Listbox(self.f_Train, selectmode=tk.SINGLE, height=5, exportselection=0)
        self.trainSet.insert(1, "IMDB Movie set(50000)")
        self.trainSet.insert(2, "IMDB Movie subset(750)")
        self.trainSet.insert(3, "Custom Set 1")
        self.trainSet.insert(4, "Custom Set 2")
        self.trainSet.insert(5, "Custom Set 3")
        self.trainSet.pack()
        #Train page buttons
        self.train_button = tk.Button(self.f_Train, text="Train", command=self.callTrainSelectionMethods)
        self.train_button.pack()

        self.close_button = tk.Button(self.f_Train, text="Close", command=master.quit)
        self.close_button.pack()

        #Test Results grid display
        tk.Label(self.f_Test,text="Test Results",pady=30).pack()
        self.f_TResults=tk.Frame(self.f_Test)
        tk.Label(self.f_TResults, text="Test Set").grid(row=0,column=0)
        tk.Label(self.f_TResults, text="Naive Bayes").grid(row=0,column=1)
        tk.Label(self.f_TResults, text="SVM").grid(row=0,column=2)
        
        #Test set names
        self.setGrid=[]
        set1 = tk.Entry(self.f_TResults)
        set1.grid(row=1,column=0)
        set2 = tk.Entry(self.f_TResults)
        set2.grid(row=2,column=0)
        set3 = tk.Entry(self.f_TResults)
        set3.grid(row=3,column=0)
        set4 = tk.Entry(self.f_TResults)
        set4.grid(row=4,column=0)
        set5 = tk.Entry(self.f_TResults)
        set5.grid(row=5,column=0)
        set6 = tk.Entry(self.f_TResults)
        set6.grid(row=6,column=0)
        #Naive Bayes results
        nb1 = tk.Entry(self.f_TResults)
        nb1.grid(row=1,column=1)
        nb2 = tk.Entry(self.f_TResults)
        nb2.grid(row=2,column=1)
        nb3 = tk.Entry(self.f_TResults)
        nb3.grid(row=3,column=1)
        nb4 = tk.Entry(self.f_TResults)
        nb4.grid(row=4,column=1)
        nb5 = tk.Entry(self.f_TResults)
        nb5.grid(row=5,column=1)
        nb6 = tk.Entry(self.f_TResults)
        nb6.grid(row=6,column=1)
    
        #SVM results
        svm1 = tk.Entry(self.f_TResults)
        svm1.grid(row=1,column=2)
        svm2 = tk.Entry(self.f_TResults)
        svm2.grid(row=2,column=2)
        svm3 = tk.Entry(self.f_TResults)
        svm3.grid(row=3,column=2)
        svm4 = tk.Entry(self.f_TResults)
        svm4.grid(row=4,column=2)
        svm5 = tk.Entry(self.f_TResults)
        svm5.grid(row=5,column=2)
        svm6 = tk.Entry(self.f_TResults)
        svm6.grid(row=6,column=2)
        

        self.f_TResults.pack()
    
        self.test_close_button = tk.Button(self.f_Test, text="Close", command=master.quit)
        self.test_close_button.pack()
        # Adding test and train pages to notebok
        self.notebook.add(self.f_Test, text="Testing")
        self.notebook.add(self.f_Train, text="Training")


def main():
    master = tk.Tk()
    UI(master)
    master.mainloop()


if __name__ == '__main__':
    main()
