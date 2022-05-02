import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3 as sq

def get_emp_info(txt_out):
	# Why does this want a float!?!?
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	results = cur.execute('''SELECT * FROM Employees;''')
	txt_out.delete(0.0, tk.END)

	for each in results:
		txt_out.insert(tk.END, str(each) + "\n")

	con.close()
def get_sale_info(txt_out, num):
	# Run SQL query to get all sales with a dollar amount greater than num
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	num = int(num)
	results = cur.execute('''
						SELECT Sales.date, Sales.dollar_amount,
						Sales.last_four_card
						FROM sales
						WHERE sales.dollar_amount > {:d}
					   '''.format(num))
	txt_out.delete(0.0, tk.END)

	txt_out.insert(tk.END,"Date | Dollar Amount | Last four of card\n")
	for each in results:
		txt_out.insert(tk.END, str(each) + "\n")
	con.close()



def get_uuid_info(txt_out, num):
	# Run SQL query to get all sales with a dollar amount greater than num
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	num = int(num)
	results = cur.execute('''
		SELECT merchandise.product_name, merchandise.quantity,merchandise.price
		FROM  merchandise
		WHERE merchandise.UPC = {:d}
					   '''.format(num))
	txt_out.delete(0.0, tk.END)

	txt_out.insert(tk.END,"Name | Quant | Price\n")
	for each in results:
		txt_out.insert(tk.END, str(each) + "\n")
	con.close()
	return
