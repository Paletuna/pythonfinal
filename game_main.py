import sys
import time
import random

wounds = 0
food = 4
water = 4
day = 1
supplies = 2
bandages = 1
fortlevel = 1
bike = False
radio = False
daywounded = 0
sick = False
sickexpl = 0
daysrest = 0

# Code for healing over time. Unused currently because of bandages
def gradheal():
	if day >= int(daywounded) + 8 and daywounded != 0 and wounds != 0:
		wounds = wounds - 1
		daywounded = day
		time.sleep(1)
		print("After going about a week and a half without any further injuries, some of your wounds healed!")
		time.sleep(1)


#Number generators for various events
def gatheramountwk1():
	global amount
	amount = random.randint(2, 4)
#Tables for random events and the radio

def radiomessagewk1():
	if radio == True:
		print("You take a moment to fiddle with the radio")
		time.sleep(1)
		chance = random.randint(1, 100)
		if chance < 75:
			message = random.randint(1, 3)
			if message == 1:
				print("You hear some static for a second, but nothing that actually sounds like words")
				time.sleep(1)
			elif message == 2:
				print("The radio begins playing some classical music")
				time.sleep(1)
			elif message == 3:
				print("You overhear a conversation between some people about theories about the cause of the zombies")
				time.sleep(1)
		else:
			print("The radio remains silent")

def wk1event():
	global water
	global food
	global supplies
	global wounds
	global bike
	global sick
	global sickexpl
	event = random.randint(1, 12)
	if event == 1:
		time.sleep(1)
		print("While you were away, some rodents got into your food supply!")
		food = food - 2
	elif event == 2:
		if food >= 4:
			print("A man approaches you after you get back from getting resources. He wants to trade some of his supplies for 3 food")
			time.sleep(1)
			print("Enter accept/decline")
			done = 0
			while done == 0:
				option = input()
				if option == "accept":
					gatheramountwk1()
					print("'Thank you for making the trade'")
					food = food - 3
					supplies = supplies + amount
					done = 1
				elif option == "decline":
					print("'Thanks anyway'")
					done = 1
	elif event == 3:
		if supplies >= 5:
			print("A shady looking stranger approaches you and asks if you want to make a deal.")
			time.sleep(1)
			print("'I'll take 5 of your supplies in exchange for some food and water'")
			time.sleep(1)
			print("Enter accept/decline")
			option = input()
			done = 0
			while done == 0:
				if option == "accept":
					gatheramountwk1()
					print("'Thanks'")
					supplies = supplies - 5
					food = food + int(amount/2) + 2
					water = water + int(amount/2) + 2
					done = 1
				elif option == "decline":
					print("'Ah well...'")
					done = 1
	elif event == 4:
		print("While out getting resources, you turn around and find that some zombies have gotten the drop on you. If only you had a bike, you could get away quickly and without injury.")
		time.sleep(1)
		if bike == True:
			print("Luckily, you do have a bike. You manage to escape unharmed.")
			if random.randint(1, 100) > 60:
				time.sleep(1)
				print("However, your bike broke down after your escape.")
				bike = False
		elif bike == False:
			print("With a brief struggle, you manage to get away from the zombies, though you got a small wound in the process.")
			wounds = wounds + 1
	elif event == 5:
		print("A band of armed strangers approaches you while you're making your way back home")
		time.sleep(1)
		print("The one that looks like the leader takes a step forward")
		time.sleep(1)
		print("'That food you have, give it to us'")
		print("Enter accept/decline")
		done = 0
		while done == 0:
			option = input()
			if option == "accept":
				print("The armed strangers take most of your food")
				food = int(food/3)
				print("You only have " + str(food) + " food left.")
				done = 1
			elif option == "decline":
				chance = random.randint(1, 100)
				if chance < 40 and bike == True:
					time.sleep(1)
					print("You quickly hop onto your bike and try to flee. A few seconds later you hear the sound of a gunshot and feel a searing pain in your shoulder.")
					wounds = wounds + 1
					daywounded = day
					done = 1
				elif chance >= 40 and bike == True:
					time.sleep(1)
					print("Hopping on your bike, you manage to outpace them and get away without trouble")
					done = 1
				elif chance < 40 and bike == False:
					time.sleep(1)
					print("You get thrown onto the ground and hear a cracking noise. Hopefully you didn't break anything important.")
					wounds = wounds + 1
					food = int(food/1.5)
					time.sleep(1)
					print("You only have " + str(food) + " food left.")
					daywounded = day
					done = 1
				else:
					time.sleep(1)
					print("You get held against a wall, and the a few of the armed strangers take some of your food")
					food = int(food/2)
					time.sleep(1)
					print("You only have " + str(food) + " food left.")
					done = 1
	elif event == 6 and day >= 7:
		time.sleep(1)
		print("You double over and feel sick to your stomach") 
		time.sleep(1)
		print("You are now sick")
		sick = True
		if sickexpl == 0:
			print("While sick, you take more water than normal, and can get rid of it by either waiting it out, or resting for a few consecutive days.")
			sickexpl = 1
		
		

def wk1scavenge():
	global supplies
	global radio
	global bandages
	global bike
	event = random.randint(1, 4)
	if event == 1:
		time.sleep(1)
		print("You manage to salvage some supplies from the nearby shed")
		supplies = supplies + 2
		time.sleep(1)
		print("You now have " + str(supplies) + " supplies.")
	elif event == 2 and supplies > 2:
		time.sleep(1)
		print("You found a broken down bike, and can either salvage it for supplies, or repair it using 3 supplies. Enter repair/salvage")
		done = 0
		while done == 0:
			option = input()
			if bike == True:
				option = "salvage"
			if option == "repair":
				supplies = supplies - 3
				print("You used three of your supplies to repair the bike")
				bike = True
				time.sleep(1)
				print("You now have " + str(supplies) + " supplies.")
				done = 1
			elif option == "salvage":
				print("You salvaged the bike for 2 supplies")
				supplies = supplies + 2
				time.sleep(1)
				print("You now have " + str(supplies) + " supplies.")
				done = 1
	elif event == 2 and supplies < 3:
		time.sleep(1)
		print("You manage to salvage some supplies from the nearby shed")
		supplies = supplies + 2
		time.sleep(1)
	elif event == 3 and radio == True:
		time.sleep(1)
		print("You found some stuff that looked like it could be useful to you")
		supplies = supplies + 3
		time.sleep(1)
		print("You now have " + str(supplies) + " supplies.")
	elif event == 3 and radio == False:
		time.sleep(1)
		print("Although you didn't find any useful supplies, you did find a radio!")
		radio = True
		time.sleep(1)
	elif event == 4:
		time.sleep(1)
		print("You managed to find some bandages")
		bandages = bandages + 1
		
def wk1gather():
	global food
	global water
	global wounds
	global daywounded
	global day
	gatheramountwk1()
	event = random.randint(1, 9)
	if event == 1 or event == 2 or event == 3:
		time.sleep(1)
		print("You found some bottled water at a store")
		water = water + amount
		print("You now have " + str(water) + " water")
	elif event == 4 or event == 5:
		time.sleep(1)
		print("You found some food slightly past the sell-by date, but you can't afford to be picky")
		food = food + amount + 2
		print("You now have " + str(food) + " food")
	elif event == 6 or event == 7 or event == 8:
		time.sleep(1)
		print("You managed to find both food and water in an abandonded house")
		food = food + int(amount / 2) + 1
		water = water + int(amount / 2)
		print("You now have " + str(food) + " food and " + str(water) + " water")
	elif event == 9:
		time.sleep(1)
		print("Although you managed to find some food, you got injured in the process")
		food = food + amount + 2
		print("You now have " + str(food) + " food")
		daywounded = day
		wounds = wounds + 1
		
def wk1rest():
	global daysrest
	global sick
	global wounds
	global bandages
	print("You spend the day resting")
	daysrest = daysrest + 1
	time.sleep(1)
	if bandages > 0 and wounds > 0:
		wounds = wounds - 1
		bandages = bandages - 1
		print("Using some of the bandages you found, you patch up your wounds")
	print("You have rested " + str(daysrest) + " consecutive days")
	if daysrest >= 3 and sick == True:
		sick = False
		time.sleep(1)
		print("After spending time resting, you are no longer sick!")
	
	
# Intro bit to the game	

print("You have gathered some meager supplies after the zombie apocalypse happened, but it won't last you long. The place you are in at the moment isn't very fortified, but it'll do for now")
time.sleep(1)
print("You can either scavenge for supplies, or go and try to gather some more food and water. You need water every day, and food every other day. Getting a total of 5 wounds will also kill you.")
time.sleep(1)
print("If you do get wounds and you have bandages, you can rest to use a bandage to heal a wound. Resting 3 consecutive days will also help you recover from getting sick")

while 1 < 14:
	time.sleep(1)
	if food < 0:
		print("You have died from lack of food.")
		quit()
	if water < 0:
		print("You have died from lack of water.")
		quit()
	if wounds >= 5:
		print("You are too injured to continue.")
		quit()
	print("\n")
	print("Today is day " + str(day))
	time.sleep(1)
	print("You have " + str(supplies) +" supplies, " + str(food) + " food and " + str(water) + " water. You also have " + str(wounds) + " wound(s)")
	time.sleep(1)
	if bandages > 0:
		print("You also have " + str(bandages) + " bandage(s)")
	radiomessagewk1()
	time.sleep(1)
	print("Type in either 'scavenge', 'gather' or 'rest'")
	done = 0
	while done == 0:
		option = input()
		if option == "scavenge":
			wk1scavenge()
			wk1event()
			daysrest = 0
			done = 1
		elif option == "gather":
			wk1gather()
			wk1event()
			daysrest = 0
			done = 1
		elif option == "rest":
			wk1rest()
			done = 1
			
	if day & 2 == 0:
		food = food - 1
	water = water - 1	
	if sick == True:
		water = water - 1
	day = day + 1
	

	
	
	
	
