import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3 as sq

def get_aisles(txt_out, txt_in):
	# Why does this want a float!?!?
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	txt_in = str(txt_in)
	results = cur.execute('''
				SELECT department.aisles
				FROM department
				WHERE department.dept_name == '{name1}'
					   '''.format(name1=txt_in))
	txt_out.delete(0.0, tk.END)

	txt_out.insert(tk.END,"Aisle Number\n")
	for each in results:
		txt_out.insert(tk.END, str(each) + "\n")

	con.close()

def get_emp_info(txt_out):
	# Why does this want a float!?!?
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	results = cur.execute('''SELECT * FROM Employees;''')
	txt_out.delete(0.0, tk.END)

	for each in results:
		txt_out.insert(tk.END, str(each) + "\n")

	con.close()


def get_date_sale(txt_out, num):
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	num = int(num)
	results = cur.execute('''
					SELECT Sales.Date, COUNT(Sales.date)
					FROM Sales
					WHERE Sales.Dollar_amount >{:d} 
					GROUP BY Sales.Date;
					   '''.format(num))
	txt_out.delete(0.0, tk.END)
	txt_out.insert(tk.END,"Date | Count\n")

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
def update_department_name(txt_in, txt_in2):
	# Takes the old name and desired name as input
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	txt_in = str(txt_in)
	txt_in = str(txt_in2)
	results = cur.execute('''
				UPDATE department
				SET dept_name == '{name1}'
				
				WHERE 
				department.dept_name == '{name2}'
					   '''.format(name1=txt_in, name2=txt_in2))
	con.close()
def update_salary(txt_in,num):
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	txt_in = str(txt_in)
	num = int(num)
	results = cur.execute('''
				UPDATE Employees
				SET salary == '{salary1}'
				
				WHERE 
				Employees.given_name == '{name1}'
					   '''.format(salary1=num, name1=txt_in))
	con.close()

	

