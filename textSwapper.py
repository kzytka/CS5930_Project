#import the csv file to be used assuming that the file has 4 columns
#with the word in English and then Arabic, then the changed words
#T. Zerrouki‏, Pyarabic, An Arabic language library for Python,
#  https://pypi.python.org/pypi/pyarabic/, 2010
# import he bidi algorithm so that the Arabic can be displayed

import csv
import arabic_reshaper
from bidi.algorithm import get_display

# -*- coding: utf-8 -*-

text = 'آدرسة'
reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
bidi_text = get_display(reshaped_text)
print(bidi_text)

import tkinter as tk #GUI
import subprocess #to handle copy/paste, clip.exe for windows systems, pbcopy for macOS
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    leftText.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        leftText.insert(tk.END, text)
    window.title(f"TEXT SCRAMBLER - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = rightText.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"TEXT SCRAMBLER - {filepath}")

def copy():
    text = rightText.get("1.0", tk.END)
    window.clipboard_clear()
    window.clipboard_append(text)

def paste():
    text = window.clipboard_get()
    leftText.insert(tk.END, text)

def scramble(leftText, rightText):
    print("Select All / Copy button pressed!")
    #open the file that has the censored words and the changes
    with open('iranCensorship.csv', newline='', encoding='utf-8') as csvfile:

        #create a dictionary reader
        reader = csv.DictReader(csvfile) #this is a dictionary

        #iterate through censored word in dictionary
        for i in reader:

            #check if the word from the dictionary is in the file
            if i['censoredWord'] in leftText.get('1.0','end'):
                
                #replace the word
                leftText = leftText.insert(tk.END, text.replace(i['censoredWord'],
                                                                 i['replacementWord']))

        rightText.insert("1.0", leftText)


#generate windows
window = tk.Tk()
window.title("TEXT SCRAMBLER - Now with support for Arabic!")

#left side of window
leftFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="LightBlue3")
leftFrame.pack() #.pack(side=tk.LEFT) for side-by-side frames
leftLabel = tk.Label(master=leftFrame, text="Original Text")
leftLabel.pack()
leftText = tk.Text(master=leftFrame)
leftText.pack()

leftPasteBtn = tk.Button(master=leftFrame, text="Paste Text", width=10, height=1, bg="gray88", fg="black", command=paste, activebackground="gray88")
leftPasteBtn.pack(side=tk.LEFT)

leftOpenBtn = tk.Button(master=leftFrame, text="Open File", width=10, height=1, bg="gray88", fg="black", command=open_file, activebackground="gray88")
leftOpenBtn.pack(side=tk.LEFT)

leftScrambleBtn = tk.Button(master=leftFrame, text="SCRAMBLE", width=10, height=1, bg="gray88", fg="black", command=lambda: scramble(leftText, rightText), activebackground="gray88")
leftScrambleBtn.pack(side=tk.RIGHT)


#right side of window
rightFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="LightBlue3")
rightFrame.pack() #.pack(side=tk.RIGHT) for side-by-side frames
rightLabel = tk.Label(master=rightFrame, text="SCRAMBLED Text")
rightLabel.pack()
rightText = tk.Text(master=rightFrame)
rightText.pack()

rightCopyBtn = tk.Button(master=rightFrame, text="Select All & Copy", width=15, height=1, bg="gray88", fg="black", command=copy, activebackground="gray88")
rightCopyBtn.pack(side=tk.LEFT)

rightSaveBtn = tk.Button(master=rightFrame, text="Save Text as File", width=15, height=1, bg="gray88", fg="black", command=save_file, activebackground="gray88")
rightSaveBtn.pack(side=tk.LEFT)

window.mainloop() #<- always needs to be last line of code, runs event handler

    #add scramble code here
    #add scramble code here
    #add scramble code here   

#generate window
window = tk.Tk()
window.title("TEXT SCRAMBLER - Now with support for Arabic!")

#left side of window
leftFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="LightBlue3")
leftFrame.pack() #.pack(side=tk.LEFT) for side-by-side frames
leftLabel = tk.Label(master=leftFrame, text="Original Text")
leftLabel.pack()
leftText = tk.Text(master=leftFrame)
leftText.pack()

leftPasteBtn = tk.Button(master=leftFrame, text="Paste Text", width=10, height=1, bg="gray88", fg="black", command=paste, activebackground="gray88")
leftPasteBtn.pack(side=tk.LEFT)

leftOpenBtn = tk.Button(master=leftFrame, text="Open File", width=10, height=1, bg="gray88", fg="black", command=open_file, activebackground="gray88")
leftOpenBtn.pack(side=tk.LEFT)

leftScrambleBtn = tk.Button(master=leftFrame, text="SCRAMBLE", width=10, height=1, bg="gray88", fg="black", command=lambda: scramble(leftText, rightText), activebackground="gray88")
leftScrambleBtn.pack(side=tk.RIGHT)


#right side of window
rightFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="LightBlue3")
rightFrame.pack() #.pack(side=tk.RIGHT) for side-by-side frames
rightLabel = tk.Label(master=rightFrame, text="SCRAMBLED Text")
rightLabel.pack()
rightText = tk.Text(master=rightFrame)
rightText.pack()

rightCopyBtn = tk.Button(master=rightFrame, text="Select All & Copy", width=15, height=1, bg="gray88", fg="black", command=copy, activebackground="gray88")
rightCopyBtn.pack(side=tk.LEFT)

rightSaveBtn = tk.Button(master=rightFrame, text="Save Text as File", width=15, height=1, bg="gray88", fg="black", command=save_file, activebackground="gray88")
rightSaveBtn.pack(side=tk.LEFT)

window.mainloop() #<- always needs to be last line of code, runs event handler
