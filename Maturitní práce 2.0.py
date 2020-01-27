import tkinter as tk

master = tk.Tk()

def velikost_pole():
	print("Počet řádků")
	a = int(input())
	print("Počet sloupců")
	b = int(input())
	print("Počet řádků",a,"Počet sloupců", b)
	for x in range(a):
		for y in range(b):
			button1 = tk.Button(master, text="", height=6, width=10)
			button1.grid(row=x, column=y)

velikost_pole()
tk.mainloop()




