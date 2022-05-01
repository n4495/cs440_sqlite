import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3 as sq

def get_sale_info(txt_out):
	# Why does this want a float!?!?
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	results = cur.execute('''SELECT * FROM Employees;''')
	txt_out.delete(0.0, tk.END)

	for each in results:
		txt_out.insert(tk.END, str(each) + "\n")

	con.close()
	return
