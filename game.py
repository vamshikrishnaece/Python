import random
def welcome():
	for i in range(1,9):
		print("*\t",end="")
	print()
	print("*",end="")
	for i in range(1,8):
		print("\t",end="")
	print("*")
	print("*",end="")
	for i in range(1,4):
		print("\t",end="")
	print("welcome",end="")
	for i in range(1,5):
		print("\t",end="")
	print("*")
	print("*",end="")
	for i in range(1,6):
		print("\t",end="")
	print("BY VAMSHI",end="")
	print("\t*")
	for i in range(1,9):
		print("*\t",end="")
	print()
	input("enter any key: ")


def game():
	print("\n******select any game******\n	1.Rock Paper Scissors \n	2.Cows and Bulls \n	3.Exit")
	v=int(input("choose a game: "))
	for i in range(0,41):
		print("=",end="")
	if v==3 :
		return
	elif v==1 :
		rock();
	elif v==2:
		cows()
	else:
		print("\ninvalid choics!")
		game()


def rock():
	print("\nlets start the game")
	print("1.play \n2.rules \n3.Return to main menu")
	ch=int(input("\nselect any one from above\n"))
	for i in range(0,41):
		print("=",end="")
	if ch==1:
		rockplay()
	elif ch==2:
		rockrules()
	else:
		print("Thank You\n")
def rockrules():
	print("RULES:\n Enter only the mentioned numbers to play without errors \n After entering a number press enter\n")
	input("\nPress any key to start the game")
	for i in range(0,41):
		print("=",end="")
	rockplay()
def rockplay():
	print("\nYou need to score 5 points to win the match ")
	print("To put Rock press 0 \nTo put Paper press 1 \nTo put Scissors press 2 \n")
	for i in range(0,41):
		print("=",end="")
	#k=int(input("choose :"))
	usr=0
	pc=0
	cout=0
	
	#p=["Rock","Paper","Scissors"]ry:

	while usr<5 and pc<5:
		p=["Rock","Paper","Scissors"]
		k=int(input("\nchoose: "))
		if k in range(0,3):
			pass
		else:
			print("enter choice from 0,1,2 only")
			continue

		s=random.choice([0,1,2])
		if (k==0) and (s==1):
			pc+=1
		elif (k==0) and (s==2):
			usr+=1
		elif (k==1) and (s==0):
			usr+=1
		elif (k==1) and (s==2):
			pc+=1
		elif (k==2) and (s==0):
			pc+=1
		elif (k==2) and (s==1):
			usr+=1
		elif (k==s):
			print("no points draw")
		print("You:",p[k],"PC:",p[s])
		
		cout+=1
		print("score:")
		print("\n you :",usr,"computer :",pc)
		
			#except:
			#	print("enter choice from 0,1,2 only")
	if usr>pc:
		for i in range(0,41):
			print("=",end="")
		print("\n* * * * * congratulations You won!!* * * * * * *\n")
		for i in range(0,41):
			print("=",end="")
	else:
		for i in range(0,41):
			print("=",end="")
		print("\n * * * * *sorry better luck next time* * * * * * *")
		for i in range(0,41):
			print("=",end="")#game()
	game()
def cowsrules():
	print("RULES:\n Enter only the mentioned numbers to play without errors \n After entering a number press enter\n")
	print("cows --> it shows nuber of char in the word you guessed match with the computer word")
	print("\nbulls --> it shows no of positions match in the words\n you neeed to Enter only 4 char words only \n")
	input("\nPress any key to start the game")
	for i in range(0,41):
		print("=",end="")
	cowsplay()
def cowsplay():
	words=["rate","pass","fail","cake","tear","calm","time","face"]
	n=random.randrange(0,7)
	word=words[n]
	cnt=0
	print("\nlets start the cows and bulls game \n you get 10 chances to gess the same word which computer guess\n")
	while(cnt<10):
		y=input("Enter a word:")
		if y=="-1":
			print("invalid input! enter a word")
			for i in range(0,41):
				print("=",end="")
			continue
		cows=0
		bulls=0
		char=0
		for a in y:
			if a in word:
				char+=1
		for i in range(0,4):
			if y[i]==word[i]:
				bulls+=1
		cows=char-bulls
		print("Cows:",cows,"\tBulls:",bulls)
		if bulls==4:
			for i in range(0,41):
				print("=",end="")
			print("Congragulations!You win!")
			for i in range(0,41):
				print("=",end="")
			game()
		cnt+=1
	for i in range(0,41):
				print("=",end="")
	print("Oops!Maximum guess limit reached!\n")
	for i in range(0,41):
				print("=",end="")
	input("Press any key to return")
	mainmenu()


def cows():
	print("\nlets start the game")
	print("1.play \n2.rules \n3.Return to main menu")
	ch=int(input("\nselect any one from above"))
	for i in range(0,41):
		print("=",end="")
	if ch==1:
		cowsplay()
	elif ch==2:
		cowsrules()
	else:
		for i in range(0,41):
				print("=",end="")
		print("Thank You")
		for i in range(0,41):
				print("=",end="")




welcome()
print("\n"*100)
game();