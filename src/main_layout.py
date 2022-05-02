import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3 as sq

from main_callbacks import *

def main_setup(in_frame):
    H = 200
    W = 300

    # Print output here
    txt_out = tk.Text(in_frame,bg="black", fg="white")
    txt_out.grid(row=3,column=0,columnspan=3)

    emp_info_frame = tk.Frame(in_frame,bg="orange",width=W,height=H)
    emp_info_frame.grid(row=1,column=0)

    emp_info_lbl = tk.Label(emp_info_frame, text="Get list of employees!")
    emp_info_lbl.grid(row=0,column=0)

    select_btn = tk.Button(emp_info_frame, text="Go!",
                           command=lambda:get_emp_info(txt_out))
    select_btn.grid(row=1,column=0)


    sale_info_frame = tk.Frame(in_frame,bg="purple", width=W, height=H)
    sale_info_frame.grid(row=1,column=1)

    sale_info_lbl = tk.Label(sale_info_frame, text="Find All Sales Greater than")
    sale_info_lbl.grid(row=0, column=0, columnspan=2)

    sale_info_in = tk.Entry(sale_info_frame)
    sale_info_in.grid(row=1,column=1)

    sale_info_btn = tk.Button(sale_info_frame, bg="purple", fg="orange",
                                text="Go!", 
                              command=lambda:get_sale_info(txt_out,
                                                           sale_info_in.get()))
    sale_info_btn.grid(row=1,column=0)

    dept_info = tk.Frame(in_frame,bg="green", width=W, height=H)
    dept_info.grid(row=1,column=2)

    frame4 = tk.Frame(in_frame,bg="pink", width=W, height=H)
    frame4.grid(row=2,column=0)

    frame5 = tk.Frame(in_frame,bg="blue", width=W, height=H)
    frame5.grid(row=2,column=1)

    frame6 = tk.Frame(in_frame,bg="grey", width=W, height=H)
    frame6.grid(row=2,column=2)


    #new_lbl = tk.Label(emp_info_frame, text="hi")
    new_lbl = tk.Label(sale_info_frame, text="hi")


    #output = tk.Text(in_frame,width=100,height=50)
    #output.grid(row=9,column=0, columnspan=3)
    return in_frame
