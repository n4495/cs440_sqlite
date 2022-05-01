import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3 as sq

def mgr_setup(in_frame):
	H = 200
	W = 300
	sale_info_frame = tk.Frame(in_frame,bg="orange",width=W, height=H)
	sale_info_frame.grid(row=1,column=0)

	salary_info = tk.Frame(in_frame,bg="purple", width=W, height=H)
	salary_info.grid(row=1,column=1)

	dept_info = tk.Frame(in_frame,bg="green", width=W, height=H)
	dept_info.grid(row=1,column=2)

	frame4 = tk.Frame(in_frame,bg="pink", width=W, height=H)
	frame4.grid(row=2,column=0)

	frame5 = tk.Frame(in_frame,bg="blue", width=W, height=H)
	frame5.grid(row=2,column=1)

	frame6 = tk.Frame(in_frame,bg="grey", width=W, height=H)
	frame6.grid(row=2,column=2)

	# Print output here
	txt_out = tk.Text(in_frame,bg="black", fg="white")
	txt_out.grid(row=3,column=0,columnspan=3)

	new_lbl = tk.Label(sale_info_frame, text="hi")
	new_lbl = tk.Label(salary_info, text="hi")


	#output = tk.Text(in_frame,width=100,height=50)
	#output.grid(row=9,column=0, columnspan=3)
	return in_frame
