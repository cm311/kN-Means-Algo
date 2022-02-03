# Import Module
from tkinter import *
import kNMeans
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

if __name__ == '__main__':

    # create root window
    root = Tk()

    # root window title and dimension
    root.title("kN_Means with Pokemon")
    # Set geometry (widthxheight)
    root.geometry('800x600')


    options = kNMeans.all_features

    # datatype of menu text
    clicked1 = StringVar()
    clicked2 = StringVar()
    menu = StringVar(root, "1")
    drop1 = OptionMenu(root, clicked1, *options)
    drop2 = OptionMenu(root, clicked2, *options)
    drop1.grid(column=0, row=0)
    drop2.grid(column=0, row=1)

    def show():
        pass

    def scatter():
        selected_features = [clicked1.get(), clicked2.get()]
        print(selected_features)
        X = kNMeans.df[selected_features]


        fig = Figure(figsize = (5, 5), dpi = 100)
        plot1 = fig.add_subplot(111)


        plot1.set_xlabel(selected_features[0])
        plot1.set_ylabel(selected_features[1])
        plot1.scatter(X[selected_features[0]], X[selected_features[1]], s=3, color='r')


        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = root)
        canvas.draw()
        canvas.get_tk_widget().grid(column=3, row=3)


    button = Button( root , text = "click Me" , command = show )

    showPlot = Button(root, text="Show Scatter Plot", command=scatter)
    showPlot.grid(column=1, row=2)

    # Execute Tkinter
    root.mainloop()
