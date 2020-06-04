import os
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.filename = filedialog.asksaveasfilename(initialdir="~/", title="Save as", filetypes=[("text file", "*.txt")])
print(root.filename)
with open(root.filename, 'w') as f:
    f.write("test")
