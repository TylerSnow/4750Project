import ttk
import Tkinter as tk
import tkFileDialog
import naiveBayes
import SVM
import train
import os
import sys

class UI:
    def callSelectionMethods(self):
        if(len(self.algorithms.curselection())!=0 and len(self.trainSet.curselection())!=0):
            self.selectAlg()
            self.selectTrainer()
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

    def selectTrainer(self):
        tlist = list()
        selection = self.trainSet.curselection()
        for i in selection:
            choice= self.trainSet.get(i)
            tlist.append(choice)
        for val in tlist:
            print(val)

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
        self.trainSet = tk.Listbox(self.f_Train, selectmode=tk.SINGLE, height=1, exportselection=0)
        self.trainSet.insert(1, "IMDB Movie test set")
        self.trainSet.pack()
        #Train page buttons
        self.train_button = tk.Button(self.f_Train, text="Train", command=self.callSelectionMethods)
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
