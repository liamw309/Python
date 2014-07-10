import random
newcards = []
playercard1 = 0
playercard2 = 0
playercard3 = 0
playercards = []
playertotal = 0
dealercard1 = 0
dealercard2 = 0
dealercards = []
dealertotal = 0
def cardshuffle():
	global newcards
	origcards = ["Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds"]
	while len(newcards) < 52:
		card = random.choice(origcards)
		origcards.remove(card)
		newcards.append(card)
	return newcards
cardshuffle()
def player():
	global playercard1, playercard2, newcards, playercards
	playercard1 = random.choice(newcards)
	newcards.remove(playercard1)
	playercard2 = random.choice(newcards)
	newcards.remove(playercard2)
	playercards.append(playercard1)
	playercards.append(playercard2)
	return playercards, playercard1, playercard2, newcards
player()
print('Player cards: ')
for item in playercards:
	print(item)
print('')
def cardcounterplayer():
	global playercard1, playercard2, playercards, playertotal
	if playercard1[0] == 'A':
		ace = raw_input("Would you like this ace to be an one or an eleven? ")
		print('')
		if ace.lower() == 'one' or ace == '1':
			playertotal += 1
		if ace.lower() == 'eleven' or ace == '11':
			playertotal += 11
	if playercard1[0] == '2':
		playertotal += 2
	if playercard1[0] == '3':
		playertotal += 3
	if playercard1[0] == '4':
		playertotal += 4
	if playercard1[0] == '5':
		playertotal += 5
	if playercard1[0] == '6':
		playertotal += 6
	if playercard1[0] == '7':
		playertotal += 7
	if playercard1[0] == '8':
		playertotal += 8
	if playercard1[0] == '9':
		playertotal += 9
	if playercard1[0] == '1' and playercard1[1] == '0':
		playertotal += 10
	if playercard1[0] == 'J':
		playertotal += 10
	if playercard1[0] == 'Q':
		playertotal += 10
	if playercard1[0] == 'K':
		playertotal += 10
	if playercard2[0] == 'A':
		ace1 = raw_input("Would you like this ace to be an one or an eleven? ")
		print('')
		if ace1.lower() == 'one' or ace1 == '1':
			playertotal += 1
		if ace1.lower() == 'eleven' or ace1 == '11':
			playertotal += 11
	if playercard2[0] == '2':
		playertotal += 2
	if playercard2[0] == '3':
		playertotal += 3
	if playercard2[0] == '4':
		playertotal += 4
	if playercard2[0] == '5':
		playertotal += 5
	if playercard2[0] == '6':
		playertotal += 6
	if playercard2[0] == '7':
		playertotal += 7
	if playercard2[0] == '8':
		playertotal += 8
	if playercard2[0] == '9':
		playertotal += 9
	if playercard2[0] == '1' and playercard2[1] == '0':
		playertotal += 10
	if playercard2[0] == 'J':
		playertotal += 10
	if playercard2[0] == 'Q':
		playertotal += 10
	if playercard2[0] == 'K':
		playertotal += 10
	return playercard1, playercard2, playercards, playertotal
cardcounterplayer()
def dealer():
	global dealercard1
	global dealercard2
	global newcards
	global dealercards
	dealercard1 = random.choice(newcards)
	newcards.remove(dealercard1)
	dealercard2 = random.choice(newcards)
	newcards.remove(dealercard2)
	dealercards.append(dealercard1)
	dealercards.append(dealercard2)
	return dealercards
	return dealercard1
	return dealercard2
	return newcards
dealer()
def cardcounterdealer():
	global dealercard1, dealercard2, dealercards, dealertotal
	if dealercard1[0] == 'A':
		if dealertotal < 10:
			dealertotal += 11
	if dealercard1[0] == '2':
		dealertotal += 2
	if dealercard1[0] == '3':
		dealertotal += 3
	if dealercard1[0] == '4':
		dealertotal += 4
	if dealercard1[0] == '5':
		dealertotal += 5
	if dealercard1[0] == '6':
		dealertotal += 6
	if dealercard1[0] == '7':
		dealertotal += 7
	if dealercard1[0] == '8':
		dealertotal += 8
	if dealercard1[0] == '9':
		dealertotal += 9
	if dealercard1[0] == '1' and dealercard1[1] == '0':
		dealertotal += 10
	if dealercard1[0] == 'J':
		dealertotal += 10
	if dealercard1[0] == 'Q':
		dealertotal += 10
	if dealercard1[0] == 'K':
		dealertotal += 10
	if dealercard2[0] == 'A':
		if dealertotal < 10:
			dealertotal += 11
	if dealercard2[0] == '2':
		dealertotal += 2
	if dealercard2[0] == '3':
		dealertotal += 3
	if dealercard2[0] == '4':
		dealertotal += 4
	if dealercard2[0] == '5':
		dealertotal += 5
	if dealercard2[0] == '6':
		dealertotal += 6
	if dealercard2[0] == '7':
		dealertotal += 7
	if dealercard2[0] == '8':
		dealertotal += 8
	if dealercard2[0] == '9':
		dealertotal += 9
	if dealercard2[0] == '1' and dealercard2[1] == '0':
		dealertotal += 10
	if dealercard2[0] == 'J':
		dealertotal += 10
	if dealercard2[0] == 'Q':
		dealertotal += 10
	if dealercard2[0] == 'K':
		dealertotal += 10
	return dealercard1, dealercard2, dealercards, dealertotal
cardcounterdealer()
print('Dealer cards: ')
print('*')
print(dealercard2)
print('')
def logic():
	global newcards, playercard1, playercard2, playercard3, playercards, playertotal, dealercard1, dealercard2, dealercards, dealertotal	
	hit = raw_input("Would you like to hit? ")
	while playertotal <= 21 and hit.lower() == 'yes':
		playercard3 = random.choice(newcards)
		newcards.remove(playercard3)
		playercards.append(playercard3)
		print(playercard3)
		print('')
		if playercard3[0] == 'A':
			ace = raw_input("Would you like this ace to be an one or an eleven? ")
			if ace.lower() == 'one' or ace == '1':
				playertotal += 1
			if ace.lower() == 'eleven' or ace == '11':
				playertotal += 11
		if playercard3[0] == '2':
			playertotal += 2
		if playercard3[0] == '3':
			playertotal += 3
		if playercard3[0] == '4':
			playertotal += 4
		if playercard3[0] == '5':
			playertotal += 5
		if playercard3[0] == '6':
			playertotal += 6
		if playercard3[0] == '7':
			playertotal += 7
		if playercard3[0] == '8':
			playertotal += 8
		if playercard3[0] == '9':				
			playertotal += 9
		if playercard3[0] == '1' and playercard1[1] == '0':
			playertotal += 10
		if playercard3[0] == 'J':	
			playertotal += 10
		if playercard3[0] == 'Q':
			playertotal += 10
		if playercard3[0] == 'K':
			playertotal += 10
		print('Player cards: ')
		for item in playercards:
			print(item)
		print('')
		if playertotal <= 21:
			hit = raw_input("Would you like to hit? ")
	if hit.lower() == 'no':
		print('Player cards: ')
		for item in playercards:
			print(item)
		print('')
		print('Dealer cards:')
		for item in dealercards:
			print(item)
		print('')
		if (21 - dealertotal) == (21 - playertotal):
			print('Tie')
		if (21 - dealertotal) < (21 - playertotal):
			print('Dealer wins')
		if (21 - dealertotal) > (21 - playertotal):
			print('Player wins')
	if playertotal > 21:
		print('Dealer cards:')
		for item in dealercards:
			print(item)
		print('')
		print('Busted')
logic()