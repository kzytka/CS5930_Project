#import the csv file to be used assuming that the file has 4 columns
#with the word in English and then Arabic, then the changed words
#T. Zerrouki‏, Pyarabic, An Arabic language library for Python,
#  https://pypi.python.org/pypi/pyarabic/, 2010
# import he bidi algorithm so that the Arabic can be displayed

import csv
import re
import arabic_reshaper
from bidi.algorithm import get_display

# -*- coding: utf-8 -*-

'''
text = 'آدرسة'
reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
bidi_text = get_display(reshaped_text)
print(bidi_text)
'''

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

def scrambleE(leftText, rightText):
    #print("Select All / Copy button pressed!")
    #open the file that has the censored words and the changes
    with open('iranCensorship.csv', newline='', encoding='utf-8') as csvfile:

        #create a dictionary reader
        reader = csv.DictReader(csvfile) #this is a dictionary
        plainText = leftText.get('1.0','end')

        #iterate through censored word in dictionary
        for i in reader:
                
            #replace the word if it was in it
            plainText = re.sub(i['censoredWord'], i['replacementWord'], plainText,
                               flags=re.IGNORECASE)

        rightText.insert('1.0', plainText)

def scrambleA(leftText, rightText):
    #print("Select All / Copy button pressed!")
    #open the file that has the censored words and the changes
    with open('iranCensorship.csv', newline='', encoding='utf-8') as csvfile:

        #create a dictionary reader
        reader = csv.DictReader(csvfile) #this is a dictionary
        plainText = leftText.get('1.0','end')

        #iterate through censored word in dictionary
        for i in reader:
                
            #replace the word if it was in it
            plainText = re.sub(i['translation'], i['translation2'], plainText,
                               flags=re.IGNORECASE)

        rightText.insert('1.0', plainText)
 

#generate windows
window = tk.Tk()
window.title("TEXT SCRAMBLER - Now with support for Arabic! | جهاز تشويش إذاعي نص - الآن مع دعم للغة العربية!")

#left side of window
leftFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="LightBlue3")
leftFrame.pack() #.pack(side=tk.LEFT) for side-by-side frames
leftLabel = tk.Label(master=leftFrame, text="Original Text | النص الأصلي")
leftLabel.pack()
leftText = tk.Text(master=leftFrame)
leftText.pack()

leftPasteBtn = tk.Button(master=leftFrame, text="Paste Text | لصق النص", width=12, height=1, bg="gray88", fg="black", command=paste, activebackground="gray88")
leftPasteBtn.pack(side=tk.LEFT)

leftOpenBtn = tk.Button(master=leftFrame, text="Open File | افتح ملف", width=12, height=1, bg="gray88", fg="black", command=open_file, activebackground="gray88")
leftOpenBtn.pack(side=tk.LEFT)

#arabic
leftScrambleBtnA = tk.Button(master=leftFrame, text="تزاحم", width=6, height=1, bg="gray88", fg="black", command=lambda: scrambleA(leftText, rightText), activebackground="gray88")
leftScrambleBtnA.pack(side=tk.RIGHT)

#english
leftScrambleBtn = tk.Button(master=leftFrame, text="SCRAMBLE", width=6, height=1, bg="gray88", fg="black", command=lambda: scrambleE(leftText, rightText), activebackground="gray88")
leftScrambleBtn.pack(side=tk.RIGHT)


#right side of window
rightFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="LightBlue3")
rightFrame.pack() #.pack(side=tk.RIGHT) for side-by-side frames
rightLabel = tk.Label(master=rightFrame, text="SCRAMBLED Text | نص مخلوط")
rightLabel.pack()
rightText = tk.Text(master=rightFrame)
rightText.pack()

#testLabel = tk.Label(master=rightFrame, text=leftText)
#testLabel.pack()

rightCopyBtn = tk.Button(master=rightFrame, text="Select All & Copy | حدد الكل ونسخ", width=20, height=1, bg="gray88", fg="black", command=copy, activebackground="gray88")
rightCopyBtn.pack(side=tk.LEFT)

rightSaveBtn = tk.Button(master=rightFrame, text="Save Text as File | حفظ النص كملف", width=20, height=1, bg="gray88", fg="black", command=save_file, activebackground="gray88")
rightSaveBtn.pack(side=tk.LEFT)

window.mainloop() #<- always needs to be last line of code, runs event handler