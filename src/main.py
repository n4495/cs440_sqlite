#!/bin/python3
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from pygame import mixer
import uuid
import sqlite3

def callback1(*args):
    print("callback1!")
    con = sqlite3.connect('storeDB.db')
    cur = con.cursor()
    result = cur.execute('''SELECT * FROM Employees;''')
    for each in result:
        print(each)


    mixer.music.load("moan2.wav")
    mixer.music.play()

def main():
    print("main\n")
    mixer.init()
    window = tk.Tk() # Create TKinter window obj
    #window2 = tk.Tk() # Create TKinter window obj

    # Create a label widget (can do text/image)

    button = tk.Button(
        window,
        text="This is a button!",
        width=40,
        height=10,
        bg="orange",
        fg="black",
        command=callback1
    )
    button.pack()

    text = tk.Label(text="hello",
                    fg="pink",
                    bg="green",
        #            height=5,
        #            width=20
                    )
    text.pack() # Put widget into the window

    entryObj = tk.Entry(
        fg="black",
        bg="white",
        width=50,
    )
    entryObj.pack()

#    intput = entryObj.get()

    # Create a new image object using a file path
    image1 = Image.open("../images/duck.jpeg")
    # Resassign image to a PIL image
    image1 = ImageTk.PhotoImage(image1)
    tk.Label(image=image1).pack()

    textbox = tk.Text()
    textbox.pack()

    #image1.resize((100,100), Image.ANTIALIAS)
    window.mainloop()# Run the event loop

    print(input)

if __name__ == "__main__":
    main()
