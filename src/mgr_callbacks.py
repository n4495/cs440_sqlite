import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3 as sq

def update_department_name(in_frame,txt_in, txt_in2):
	# Takes the old name and desired name as input
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	txt_in = str(txt_in)
	txt_in2 = str(txt_in2)
	print("to"+txt_in)
	print("from"+txt_in2)
	results = cur.execute('''
				UPDATE department
                SET dept_name == '{name2}'
                WHERE
                department.dept_name == '{name1}';
				'''.format(name1=txt_in, name2=txt_in2))
	con.commit()
	con.close()

	#department.dept_name == '{name2}'
def update_salary(txt_in,num):
	con = sq.connect('../test_db/storeDB.db')
	cur = con.cursor()
	txt_in = str(txt_in)
	num = int(num)
	results = cur.execute('''
				UPDATE Employees
				SET salary == '{salary1}'
				WHERE
				Employees.employee == '{name1}'
				'''.format(salary1=num, name1=txt_in))
	con.close()

