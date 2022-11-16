import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import *


r = tk.Tk()
r.geometry("300x300")
r.title('Counting Seconds')


w = Canvas(r, width=40, height=60)
w.pack()

canvas_height=5000
canvas_width=500
y = int(canvas_height / 2)

#w.create_line(0, y, canvas_width, y)
def Graph_Generator():   
    plt.clear()

    # get random dta to visualize normal distribution data
    normal_dev=np.random.normal(200000,25000,2000)
    # Create a histogram plot
    plt.hist(normal_dev,200)
    plt.title("Normal distribution")
    plt.show()

array=[1,2,3,4,5,6,7,8,9,10],[2,4,6,8,10,12,14,16,18,20]

def Data_Graph():
    print(array[0])
    print(array[1])
    #Makes the graph based on the 
    plt.plot(array[0],array[1])
    plt.show()

#Transfer Data too an exel worksheet
def Create_Exel():
    #Make two arrays into a
    df = pd.DataFrame(array).T
    df.to_excel(excel_writer = "C:/Users/mmwes/Desktop/test.xlsx")
    
#Graph generation Button
graph_button=Button(r,text="Generate graph",command=Graph_Generator)
graph_button.pack(pady=30)

#Stop All button / Kill switch 
stopbutton = tk.Button(r, text='Stop All', width=25, command=r.destroy) 
stopbutton.pack()

#Ignition Button 
startbutton = tk.Button(r, text='Start', width=25, command=print("Started"))#Add the ignition stage here
startbutton.pack()

#Save as exel File button
Data_Graphbutton = tk.Button(r, text='Graph Data', width=25, command=Data_Graph)
Data_Graphbutton.pack()

#Save as exel File button
create_exel = tk.Button(r, text='Save Data', width=25, command=Create_Exel)
create_exel.pack()


r.mainloop()
