import tkinter as tk
print("Vítám Vás u mé maturitní práce piškvorky")
master = tk.Tk()

def velikost_pole():
	print("Zadej počet řádků: ")
	a = int(input())
	print("Zadej počet sloupců: ")
	b = int(input())
	print("Počet řádků",a ,"Počet sloupců", b)
	for x in range(a):
		for y in range(b):
			button1 = tk.Button(master, text="", height=6, width=10)
			button1.grid(row=x, column=y)

	turnLabel= tk.Label(master, text=turn, font="Helvetica 16 bold")
	turnLabel.grid(row=a, columnspan=b)

turn = "X"

def change_turn():
    global turn
    if turn == "O":
        turn = "X"
        turnLabel.config(text=turn)
    elif turn == "X":
        turn = "O"
        turnLabel.config(text=turn)

velikost_pole()
change_turn()
tk.mainloop()

