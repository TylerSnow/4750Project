import ttk
import Tkinter as tk
import tkFileDialog


class UI:

    def __init__(self, master):
        self.master = master
        self.master.title('Sentiment Analysis')
        self.master.geometry('800x800')

        for rows in range(80):
            master.rowconfigure(rows, weight=1)
            master.columnconfigure(rows, weight=1)

        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=1, column=0, columnspan=80, rowspan=80, sticky="NESW")

        # Creating the test page
        self.f_Test = tk.Frame(self.notebook)
        self.testSet = tk.Listbox(self.f_Train, selectmode=tk.SINGLE, height=1, exportselection=0)
        self.testSet.insert(1, "IMDB Movie test set")
        self.testSet.pack()

        # Creating the train page
        self.f_Train = tk.Frame(self.notebook)
        self.algorithms = tk.Listbox(self.f_Train, selectmode=tk.SINGLE, height=2, exportselection=0)
        self.algorithms
        self.algorithms.insert(1, "Naive Bayes")
        self.algorithms.insert(2, "Support Vector Machine")
        self.algorithms.pack()
        # Adding test and train pages to notebok
        self.notebook.add(self.f_Test, text="Testing")
        self.notebook.add(self.f_Train, text="Training")


def main():
    master = tk.Tk()
    UI(master)
    master.mainloop()


if __name__ == '__main__':
    main()
