from random import randint
x=randint(0,9)
y=input("saisir la réponse")
if int(y)==int(x):
	print("bravo, vous avez gagné")
else:
	print("Désolé, vous avez raté")