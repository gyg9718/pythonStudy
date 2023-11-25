import tkinter
from math import *
count = 0

def countUP():
    global count
    count +=1
    label.config(text =str(count))
window = tkinter.Tk()

window.title("hgcom")
window.geometry("640x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window,text="0")
label.pack()

button = tkinter.Button(window, text ="카운트", overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval =100)
button.pack()

def calc(event):
    label4.config(text="결과="+str(eval(entry.get())))

entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label4 = tkinter.Label(window)
label4.pack()

window.mainloop()


