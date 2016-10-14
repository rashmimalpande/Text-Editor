from tkinter import *
import tkinter.filedialog

filename = None


def newFile():
    global filename
    filename = "untitled"  # The default filename is alwaya "untitled"
    text.delete(0.0, END)  # 0.0 refers to (line no, col no)

def saveFile():
    global filename
    content = text.get(0.0, END)  # Get all the content from the file
    f = open(filename, "w")  # Open the file in write mode
    f.write(content)  # write the content into the file
    f.close()  #close the file

def openFile():
    f = tkinter.filedialog.askopenfile(mode="r")
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("Text Editor")
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
text = Text(root, width=300, height=300)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()
