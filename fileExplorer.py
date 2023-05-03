import tkinter
from tkinter import filedialog

# Function to open file explorer
def theFileExplorer(info):
    root = tkinter.Tk()
    root.withdraw()

    filePath = filedialog.askopenfilename()
    info = filePath
    return info