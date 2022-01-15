# Mark Hibbing CIS 345 Tues/Thurs 12:00 - 1:15pm Project GUI Submission

# This back-end GUI is kept simple to fulfill the needs of the university project. In the original vision of this
# project, before it was chosen for this project, a GUI was not intended to be added. The key feature of this
# project lies more in its capability to translate URLs into played audio in a Discord server voice channel

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

# Functions To Do
# Refresh button using get methods to save urls and time stamps
# Print button to save given urls and time stamps into a .txt file

# Without finding a way to pull out track information, the above functions are impossible


def close():
    window.destroy()


window = tk.Tk()
window.title('Developer Logger')
window.geometry('550x600')
window.config(bg='LightSkyBlue4')

# Adds music bot logo to dev panel
logo = Image.open('Sunset Concept.png')
img = logo.resize((220, 208))
img.save('Sunset Concept.png')
logo = ImageTk.PhotoImage(img)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=2, row=0, pady=10, padx=10)

welcome_lbl = Label(window, text='Sounds of Sunset \nCommunity Project', bg='LightSkyBlue4', font=('Arial', 14))
welcome_lbl.grid(columnspan=3, column=2, row=1)

# Logger box that will display each url called along with the time
logger_box = Listbox(window, width=50, height=30, bg='LightSkyBlue4', bd=5, relief=SUNKEN)
logger_box.grid(row=0, column=0, columnspan=2)

# Spacers
Label(window, text='', bg='LightSkyBlue4').grid(row=1, columnspan=4)
Label(window, text='', bg='LightSkyBlue4').grid(row=2, columnspan=4)

# Updates the list of songs called
refresh_button = Button(window, text='Refresh', relief=RAISED)
refresh_button.grid(row=4, column=2, sticky=W, padx=10)

# Saves the history of urls called during the session to a text document
save_button = Button(window, text='Save', relief=RAISED)
save_button.grid(row=4, column=3, sticky=N, padx=10)

# Exits the program
exit_button = Button(window, command=close, text='Exit', relief=RAISED)
exit_button.grid(row=4, column=4, sticky=E, padx=10)

# Move mainloop to main.py
window.mainloop()
