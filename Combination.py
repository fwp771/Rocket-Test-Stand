import time
import sys
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import *

EMULATE_HX711=False
valarr=[0]
referenceUnit = 1
r = tk.Tk()
r.geometry("300x300")
r.title('Counting Seconds')
array=[1,2,3,4,5,6,7,8,9,10],[2,4,6,8,10,12,14,16,18,20]

def HX711():
	#HX771 Example Code
	print("Started")
	EMULATE_HX711=False
	valarr=[0]
	referenceUnit = 1

	if not EMULATE_HX711:
		import RPi.GPIO as GPIO
		from hx711 import HX711
	else:
		from emulated_hx711 import HX711

	def cleanAndExit():
		print("Cleaning...")

		if not EMULATE_HX711:
			GPIO.cleanup()
			
		print("Bye!")
		sys.exit()

	hx = HX711(5, 6)
	hx.set_reading_format("MSB", "MSB")
	hx.set_reference_unit(referenceUnit)
	hx.reset()
	hx.tare()
	print("Tare done! Add weight now...")
	while True:
		try:
			val = hx.get_weight(5)
			print(val)
			valarr.append(val)
			hx.power_down()
			hx.power_up()
			time.sleep(0.01)

		except (KeyboardInterrupt, SystemExit):
			cleanAndExit()
        
#Start the Gui
w = Canvas(r, width=40, height=60)
w.pack()

canvas_height=5000
canvas_width=500
y = int(canvas_height / 2)

#w.create_line(0, y, canvas_width, y)
def Graph_Generator():   

    # get random dta to visualize normal distribution data
    normal_dev=np.random.normal(200000,25000,2000)
    # Create a histogram plot
    plt.hist(normal_dev,200)
    plt.title("Normal distribution")
    plt.show()


def Data_Graph():
    print(array[0])
    print(array[1])
    #Makes the graph based on the 
    plt.plot(array[0],array[1])
    plt.show()

#Transfer Data too an exel worksheet
def Create_Exel():
    #Make two arrays into x-y
    df = pd.DataFrame(array).T
    with pd.ExcelWriter(r'C:/Users/mmwes/Desktop/test.xlsx') as writer: df.to_excel(writer,sheet_name ='df', index=False)
    print('Data Saved')
    
#Graph generation Button
graph_button=Button(r,text="Generate graph",command=Graph_Generator)
graph_button.pack(pady=30)

#Stop All button / Kill switch 
stopbutton = tk.Button(r, text='Stop All', width=25, command=r.destroy) 
stopbutton.pack()

#Load Cell Start 
startbutton = tk.Button(r, text='Load Cell Start', width=25, command=HX711)#Add the ignition stage here
startbutton.pack()

#Save as exel File button
Data_Graphbutton = tk.Button(r, text='Graph Data', width=25, command=Data_Graph)
Data_Graphbutton.pack()

#Save as exel File button
create_exel = tk.Button(r, text='Save Data', width=25, command=Create_Exel)
create_exel.pack()


r.mainloop()
