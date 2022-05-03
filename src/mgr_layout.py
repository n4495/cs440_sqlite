import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3 as sq

from mgr_callbacks import *

def mgr_setup(in_frame):
	H = 200
	W = 300
	upt_dept_frame = tk.Frame(in_frame,bg="orange",width=W, height=H)
	upt_dept_frame.grid(row=1,column=0)

	upt_dept_lbl= tk.Label(upt_dept_frame,
						text="Update department name")
	upt_dept_lbl.grid(row=0,column=0)

	upt_dept_in = tk.Entry(upt_dept_frame)
	upt_dept_in.grid(row=1,column=1)

	upt_dept_in2 = tk.Entry(upt_dept_frame)
	upt_dept_in2.grid(row=1,column=2)

	upt_dept_btn = tk.Button(upt_dept_frame, text="Go!",
					command=lambda:update_department_name(txt_out,
					upt_dept_in.get(), upt_dept_in2.get()))
	upt_dept_btn.grid(row=1,column=0)





	# Print output here
	txt_out = tk.Text(in_frame,bg="black", fg="white")
	txt_out.grid(row=3,column=0,columnspan=3)



	#output = tk.Text(in_frame,width=100,height=50)
	#output.grid(row=9,column=0, columnspan=3)
	return in_frame
