import os
from tkinter import *
root = Tk()
root.geometry('600x100')

def runit():
	os.startfile('link.bat')

def downloady():
	with open('link.bat', 'w')as down_load:
		down_load.write(f'youtube-dl{link.get()}')
		down_load.close()

	runit()

f= Frame(root)
f.grid()

Label(f,text='~~~~~~~~~~~~~~~~YOUTUBE VIDEO DOWNLOADER~~~~~~~~~~~~~~~~~~~~~', font = 20, padx=5).pack()

f1= Frame(root)
f1.grid()
Label(f1,text = 'Enter Link Here: ', font=5).grid(row=1)

link = StringVar()

Entry(f1,font=5, textvariable=link).grid(row=1,column=1, pady=5, padx=10)

button = Button(f1,text='Download',padx=50,relief=RAISED, font=10, borderwidth=5,command=downloady)
# mylabel = Button.grid(column=1, pady =5)
button.grid(row=2, column=1)
root.mainloop()