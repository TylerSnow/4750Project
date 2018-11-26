import Tkinter as tk
import naiveBayes
import SVM
import train
import os
import sys

class sentimentAnalysisGUI:
    def callSelectionMethods(self):
        if(len(self.algorithms.curselection())!=0 and len(self.testSet.curselection())!=0):
            self.selectAlg()
            self.selectTest()
        else:
            print("Please select an algorithm and a test set.")
            
    def selectAlg(self):
        clist = list()
        selection = self.algorithms.curselection()
        for i in selection:
            choice= self.algorithms.get(i)
            clist.append(choice)
        for val in clist:
            print(val)

    def selectTest(self):
        tlist = list()
        selection = self.testSet.curselection()
        for i in selection:
            choice= self.testSet.get(i)
            tlist.append(choice)
        for val in tlist:
            print(val)

    def showFrame(self,frame):
        self.viewFrame=self.frames[frame]
        self.viewFrame.pack(fill=tk.BOTH,expand=1)

    def hideFrame(self):
        self.master.withdraw()
            
    def __init__(self, master):
        self.master = master
        master.title("Sentiment Analysis")
        master.geometry("800x500")
        master.option_add("*Button.Background", "white")
        master.option_add("*Button.Foreground", "red")
        master.option_add("*Label.Background","white")
        master.option_add("*Label.Foreground","red")
        master.configure(background='white')
        f_Test= tk.Frame(master)
        f_Train= tk.Frame(master)
        f_displayData = tk.Frame(master)
        self.viewFrame=tk.Frame(master)
        self.viewFrame=f_Test
        self.frames=[f_Test,f_Train,f_displayData]
        
        #Testing Frame
        self.algLabel = tk.Label(f_Test, text="Algorithm")
        self.algLabel.pack()

        self.algorithms = tk.Listbox(f_Test,selectmode=tk.SINGLE,height=2,exportselection=0)
        self.algorithms.insert(1,"Naive Bayes")
        self.algorithms.insert(2,"Support Vector Machine")
        alg=self.algorithms.curselection()
        self.algorithms.pack()

        self.testLabel = tk.Label(f_Test, text="Test Set")
        self.testLabel.pack()
        self.testSet = tk.Listbox(f_Test,selectmode=tk.SINGLE,height=1,exportselection=0)
        self.testSet.insert(1,"IMDB Movie test set")
        self.testSet.pack()
        
        self.test_button = tk.Button(f_Test, text="Test", command=self.callSelectionMethods)
        self.test_button.pack()

        self.close_button = tk.Button(f_Test, text="Close", command=master.quit)
        self.close_button.pack()

        self.train_frame_button=tk.Button(f_Test, text="Training", command=self.showFrame(1))
        self.train_frame_button.pack()

        #Training Frame
        self.train_label= tk.Label(f_Train,text="Algorithm to Train")
        self.train_label.pack()
def main():
    root = tk.Tk()
    gui = sentimentAnalysisGUI(root)
    root.mainloop()

    #Retrieving and processing the training data
    neg_fnames, pos_fnames = get_training_filepaths()
    neg_reviews, pos_reviews = process_files(neg_fnames, pos_fnames)
    print("done processing files")

    reviews = [neg_reviews, pos_reviews]

    naiveBayes.naiveBayes(reviews)



if __name__ == '__main__':
    main()
