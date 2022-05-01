import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

import main_layout
import mgr_layout

def main():
	HEIGHT = 1000 # This is still bad, but less so
	WIDTH = 900

	root = tk.Tk()
	root.geometry("900x1000")
	root.attributes('-type', 'dialog')

	headerImg = ImageTk.PhotoImage(Image.open("../images/bobs_bolts_header.png"))
	headerLbl = tk.Label(root, image=headerImg).pack()

	# Create our main menu tab widget
	tabs = ttk.Notebook(root)
	tabs.pack() #Place it onto the root window


	# Set up frames which will be contained in our tabs
	main_frame = tk.Frame(tabs, bg="red", width=WIDTH, height=WIDTH)
	# Pass frame object for setup and get it back
	main_frame = main_layout.main_setup(main_frame)

	manager_frame = tk.Frame(tabs, bg="blue", width=HEIGHT, height=HEIGHT)
	manager_frame = mgr_layout.mgr_setup(manager_frame)

	main_frame.pack(fill="both", expand=True)
	manager_frame.pack(fill="both", expand=True)

	tabs.add(main_frame, text="Main Menu")
	tabs.add(manager_frame, text="Manager Menu")

	root.mainloop()
	return


if (__name__ == "__main__"):
	main()

