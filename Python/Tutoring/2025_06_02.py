import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils import Prints


Prints.PrintLine("GUI")
import tkinter as tk


# window = tk.Tk()
# window.title("My GUI")
# window.geometry("300x200")
# window.mainloop()

def Say_Hello(label):
    label.config(text="Hello, World")
    
window = tk.Tk()
window.title("인사 GUI")
window.geometry("300x200")

_label = tk.Label(window, text="여기에 인사말이 표시됨")
_label.pack()

#command에는 매개변수 없는 함수만 올 수 있다.
button = tk.Button(window, text="인사하기", command=lambda: Say_Hello(_label))

button.pack()
window.mainloop()