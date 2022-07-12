import sys
from tkinter import *
from threading import *
import time
import pyautogui

appClose = False

def appOnClose():
    global appClose
    appClose = True
    root.destroy()

def actionButtonCallback(actionB: Button):
    global amHere
    amHere = not amHere

    if (amHere):
        actionB.config(text="Stop",bg="#fa1e1e")
        for child in frequencyLF.winfo_children():
            child.configure(state='disable')
    else:
        actionB.config(text="Start",bg="#1ed21e")
        for child in frequencyLF.winfo_children():
            child.configure(state='active')

def beingHere():
    global appClose
    global amHere
    global frequency

    while not appClose:
        if (amHere):
            frequencySec = frequency.get() * 60
            pyautogui.moveRel(1, 0, 0.1)
            pyautogui.moveRel(-1, 0, 0.1)
            time.sleep(frequencySec)
        else:
            time.sleep(3)

root = Tk()
root.resizable(False, False) 
root.wm_title("I'm Here")
root.protocol("WM_DELETE_WINDOW", appOnClose)
root.grid_columnconfigure((0,1,2), weight=1)

frequency = IntVar(value=1)
frequencyLF = LabelFrame(root, text="Frequency")
freq1RB = Radiobutton(frequencyLF, text="Every 1 minute", variable=frequency, value=1)
freq5RB = Radiobutton(frequencyLF, text="Every 5 minutes", variable=frequency, value=5)
freq10RB = Radiobutton(frequencyLF, text="Every 10 minutes", variable=frequency, value=10)
frequencyLF.grid(row=0, column=0, columnspan=3, sticky=W, padx=(10,10), pady=(5,5))
freq1RB.grid(row=0, column=0)
freq5RB.grid(row=0, column=1)
freq10RB.grid(row=0, column=2)

actionB = Button(root, text='Start', bg='#1ed21e', command=lambda: actionButtonCallback(actionB))
actionB.grid(row=1, column=1, sticky=W+E, padx=(10,10), pady=(10,10)) 

amHere = False
Thread(target=beingHere).start()

try:
    root.mainloop()
except (KeyboardInterrupt, SystemExit):
    appOnClose()
    sys.exit()