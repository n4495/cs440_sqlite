#!/bin/python3
import tkinter as tk

def main():
    # Create a window object
    win = tk.Tk()
    win.columnconfigure(1, weight=1, minsize=10)
    win.rowconfigure(0, weight=1, minsize=50)

    # Create a frame object
    frameA = tk.Frame()
    frameB = tk.Frame()
    # Create label and assign the frame as its master
    labelA = tk.Label(master=frameA, text="labelA!")
    labelA.pack()

    labelB = tk.Label(master=frameB, text="LabelB")
    labelB.pack()

    enter_bt = tk.Button(master = frameA, text="Run Query!", width = 25, height=25,
                         fg='yellow',
                         bg='blue')
    enter_bt.pack()



    # Assign the frame to our window and pack it in
    frameB.grid(row=0,column=1)
    frameA.grid(row=2,column=0)

    
    win.mainloop()

if __name__ == "__main__":
    main()
