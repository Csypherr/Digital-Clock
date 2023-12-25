#=========================================================================================
#   Author: Mela Bamiji.
#   Date:   25th December, 2023.
#   
#   This is a simple GUI clock program that displays the current day, date, and time. 
#   The code is meant for tutorial documentation only. So you are free to copy and 
#   modify this code to suit your purposes.
#=========================================================================================

from tkinter import *
from time import *

def update():
    """Update the values for date and the day of the week. 
    Time is recursively updated every second."""

    # time update
    time_string = strftime("%H:%M:%S %p")
    time_label.config(text=time_string)

    # day update
    day_string = strftime("%A")
    day_label.config(text=day_string)

    # date update
    date_string = strftime("%B %d, %Y.")
    date_label.config(text=date_string)

    # update every one thousand milliseconds
    time_label.after(1000, update)

# instantiate a GUI window: make window with fixed size
window = Tk()
window.resizable(width=False, height=False)

# create a label for the current time 
time_label = Label(window, font=("Arial", 50), fg="green", bg="black")
time_label.pack()

# create a label for day of the week
day_label = Label(window, font=("Ink Free", 25)) 
day_label.pack()

# create a label for the current date
date_label = Label(window, font=("Ink Free", 30))
date_label.pack()

# update the window
window.after(1000, update) 


# program's main loop
window.mainloop()

# EOF 