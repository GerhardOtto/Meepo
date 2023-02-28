import tkinter
from tkinter import filedialog

def theFileExplorer(info):
    root = tkinter.Tk()
    root.withdraw()

    filePath = filedialog.askopenfilename()
    info = filePath
    return info