from tkinter import *
print("Vítám Vás u mé maturitní práce piškvorky")
master = Tk()
master.title("Piškvorky")

print("Zadej počet řádků: ")
a = int(input())
print("Zadej počet sloupců: ")
b = int(input())

#Vykreslení pole
def velikost_pole(a,b):
	print("Počet řádků",a ,"Počet sloupců", b)
	for x in range(a):
		for y in range(b):
			button1 = Button(master, text="",command=zmena_pole , height=6, width=10)
			button1.grid(row=x, column=y)
	 
turn = "X"	
turnLabel= Label(master, text=turn, font="Helvetica 16 bold")
turnLabel.grid(row=a, columnspan=b)

#Zobrazení kdo je na tahu.
def change_turn():
    global turn
    if turn == "O":
        turn = "X"
        turnLabel.config(text=turn)
    elif turn == "X":
        turn = "O"
        turnLabel.config(text=turn)

#Změna pole na křížek nebo kolečko po kliknutí.
def zmena_pole():
	global text
	print ("x")
	change_turn()

velikost_pole(a,b)   
master.mainloop()


