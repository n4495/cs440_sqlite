#!/bin/python3
import tkinter as tk

def main():
    # Create a window object
    win = tk.Tk()
    # Create a frame object
    frameA = tk.Frame(relief="groove", borderwidth="4")
    frameB = tk.Frame()
    # Create label and assign the frame as its master
    labelA = tk.Label(master=frameA, text="labelA!")
    labelA.pack()

    labelB = tk.Label(master=frameB, text="LabelB")
    labelB.pack()



    # Assign the frame to our window and pack it in
    frameB.pack()
    frameA.pack()

    
    win.mainloop()

if __name__ == "__main__":
    main()
