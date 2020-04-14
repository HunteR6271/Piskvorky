from tkinter import *
print("Vítám Vás u mé maturitní práce piškvorky")
master = Tk()
master.title("Piškvorky")

#Zadání hodnot pro velikost pole.
print("Zadej počet řádků: ")
a = int(input())
print("Zadej počet sloupců: ")
b = int(input())

#Funkce vykreslení pole
def velikost_pole(a,b):
	print("Počet řádků",a ,"Počet sloupců", b)
	for x in range(a):
		for y in range(b):
			button = Button(master, text="", height=6, width=10, font="Helvetica 12 bold")
			button.config(command = create_functions(button))
			button.grid(row=x, column=y)
	 
turn = "X"	
turnLabel= Label(master, text=turn, font="Helvetica 20 bold")
turnLabel.grid(row=a, columnspan=b)

#Funkce zobrazení kdo je na tahu.
def change_turn():
    global turn
    if turn == "O":
        turn = "X"
        turnLabel.config(text=turn)
    elif turn == "X":
        turn = "O"
        turnLabel.config(text=turn)

#Funkce, která vytváří další funkce.
def create_functions(tlacitko_funkce):
	#Funkce měnící text v tlačítku.
	def zmena_pole():
		tlacitko_funkce.config(text=turn)
		change_turn()
	return zmena_pole

velikost_pole(a,b)   
master.mainloop()



