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

#Zadání hodnoty pro výběr modu hry.
print("Nakolik vítězných políček chceš hrát? Pokud na tři napiš 3, pokud na pět napiš 5.")
r = int(input())

#Funkce vykreslení pole
def velikost_pole(a,b):
	print("Hraješ hru",a,"x",b,"na",r,"vítězných polí." )
	for x in range(a):
		for y in range(b):
			button = Button(master, text="", height=2, width=5, font="Helvetica 15 bold", bg='grey', fg='white')
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
	if r == 5:
		vyhodnoceni_5()
	elif r == 3:
		vyhodnoceni_3()
	else:
		print("Špatně zadaná hodnota pro počet vítězných políček")
		exit()

#Funkce, která vytváří další funkce.
def create_functions(tlacitko_funkce):
	#Funkce měnící text v tlačítku.
	def zmena_pole():
		tlacitko_funkce.config(text=turn)
		change_turn()
	return zmena_pole

#Funkce vyhodnocení kdo vyhrál na 3 políčka za sebou.
def vyhodnoceni_3():
	#Vyhrává řádek
	for z in range(b-2):
		for i in range(a):
			if seznam_tlacitek[b*i+z] ['text'] == seznam_tlacitek[b*i+1+z] ['text'] == seznam_tlacitek[b*i+2+z] ['text'] != "":
				print (f"Vyhrál hráč {seznam_tlacitek[b*i+z] ['text']}")
	#Vyhrává sloupec
	for i in range(a-2):
		for z in range(b):
			if seznam_tlacitek[z+b*i] ['text'] == seznam_tlacitek[z+b+b*i] ['text'] == seznam_tlacitek[z+2*b+b*i] ['text'] != "":
				print (f"Vyhrál hráč s {seznam_tlacitek[z+b*i] ['text']}")
	#Vyhráva diagonála z leva do prava
	for d in range(b-2):
		for p in range(a-2):
			if seznam_tlacitek[p*b+d] ['text'] == seznam_tlacitek[p*b+b+1+d] ['text'] == seznam_tlacitek[p*b+2*b+2+d] ['text'] != "":
				print (f"Vyhrál hráč s {seznam_tlacitek[p*b+d] ['text']}")
	#Vyhrává diagonála z prava do leva
	for d in range(b-2): 
		for k in range(a-2):
			if seznam_tlacitek[k*b+2+d] ['text'] == seznam_tlacitek[k*b+2+b-1+d] ['text'] == seznam_tlacitek[k*b+2+2*b-2+d] ['text'] != "":
				print (f"Vyhrál hráč s {seznam_tlacitek[k*b+2+d] ['text']}")
	#Remíza
	kontrola = True
	for button in seznam_tlacitek:
		if button ['text'] == "":
			kontrola = False
	if kontrola:
		print("Remíza")

#Funkce vyhodnocení kdo vyhrál na 5 políček za sebou. 
def vyhodnoceni_5():
	#Vyhrává řádek
	for z in range(b-4):
		for i in range(a):
			if seznam_tlacitek[b*i+z] ['text'] == seznam_tlacitek[b*i+1+z] ['text'] == seznam_tlacitek[b*i+2+z] ['text'] == seznam_tlacitek[b*i+3+z] ['text'] == seznam_tlacitek[b*i+4+z] ['text'] != "":
				print (f"Vyhrál hráč s {seznam_tlacitek[b*i+z] ['text']}")
	#Vyhrává sloupec
	for i in range(a-4):
		for z in range(b):
			if seznam_tlacitek[z+b*i] ['text'] == seznam_tlacitek[z+b+b*i] ['text'] == seznam_tlacitek[z+2*b+b*i] ['text'] == seznam_tlacitek[z+3*b+b*i] ['text'] == seznam_tlacitek[z+4*b+b*i] ['text'] != "":
				print (f"Vyhrál hráč s {seznam_tlacitek[z+b*i] ['text']}")
	#Vyhráva diagonála z leva do prava
	for d in range(b-4):
		for p in range(a-4):
			if seznam_tlacitek[p*b+d] ['text'] == seznam_tlacitek[p*b+b+1+d] ['text'] == seznam_tlacitek[p*b+2*b+2+d] ['text'] == seznam_tlacitek[p*b+3*b+3+d] ['text'] == seznam_tlacitek[p*b+4*b+4+d] ['text'] != "":
				print (f"Vyhrál hráč s {seznam_tlacitek[p*b+d] ['text']}")
	#Vyhrává diagonála z prava do leva
	for d in range(b-4): 
		for k in range(a-4):
			if seznam_tlacitek[k*b+2+d] ['text'] == seznam_tlacitek[k*b+2+b-1+d] ['text'] == seznam_tlacitek[k*b+2+2*b-2+d] ['text'] == seznam_tlacitek[k*b+2+3*b-3+d] ['text'] == seznam_tlacitek[k*b+2+4*b-4+d] ['text'] != "":
				print (f"Vyhrál hráč s {seznam_tlacitek[k*b+2+d] ['text']}")
	#Remíza
	kontrola = True
	for button in seznam_tlacitek:
		if button ['text'] == "":
			kontrola = False
	if kontrola:
		print("Remíza")

velikost_pole(a,b)   
master.mainloop()



