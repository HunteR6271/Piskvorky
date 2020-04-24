from tkinter import *
print("Vítám Vás u mé maturitní práce piškvorky")
master = Tk()
master.title("Piškvorky")
seznam_tlacitek = []

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
			button = Button(master, text="", height=6, width=10, font="Helvetica 15 bold", bg='grey', fg='white')
			button.config(command = create_functions(button))
			button.grid(row=x, column=y)
			seznam_tlacitek.append(button)
	 
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
	vyhodnoceni()
	 

#Funkce, která vytváří další funkce.
def create_functions(tlacitko_funkce):
	#Funkce měnící text v tlačítku.
	def zmena_pole():
		tlacitko_funkce.config(text=turn)
		change_turn()
	return zmena_pole
#Funkce vyhodnocení kdo vyhrál.
def vyhodnoceni():
	#Vyhrává řádek
	for i in range(a):
		for
			if seznam_tlacitek[b*i] ['text'] == seznam_tlacitek[b*i+1] ['text'] == seznam_tlacitek[b*i+2] ['text'] != "":
				print (f"Vyhrál hráč {seznam_tlacitek[b*i] ['text']}")
	#Vyhrává sloupec
	for z in range(b):
		if seznam_tlacitek[z] ['text'] == seznam_tlacitek[z+b] ['text'] == seznam_tlacitek[z+2*b] ['text'] != "":
			print (f"Vyhrál hráč {seznam_tlacitek[z] ['text']}")
	#Vyhráva diagonála z leva do prava
	for p in range(a-b+1):
		if seznam_tlacitek[p*3] ['text'] == seznam_tlacitek[p*3+4] ['text'] == seznam_tlacitek[p*3+8] ['text'] != "":
			print (f"Vyhrál hráč {seznam_tlacitek[p*3] ['text']}")

velikost_pole(a,b)   
master.mainloop()



