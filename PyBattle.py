# THIS IS A WORK IN PROGRESS
# EVERYTHING IS SUBJECT TO CHANGE
# GitHub: https://github.com/estaciohugoDev

# PyBattle is a rather simple but fun little text-based RPG that i made back in 2017
# for practice purposes, i intend to implement a lot of things in it like an inventory system,
# Equipment, XP Gain and much more, im using this project to further my knowledge in python, its really fun.
# Feel free to snatch the code and do whatever you feel like it, also feel free to message me with whatever
# fun ideas you may have had for it, im eager to know.

import random
import time

enemyList = ["Slime","Skeleton","Thief","Orc","Zombie"]
randomEnemy = random.choice(enemyList)

enemy_hp = 10
player_hp = 10

player_damage = 0;

def playerWeapon(player_damage):
	weapons = ['sword','staff','axe','claw']
	print("Choose a weapon:\n1 - Sword\n2 - Staff\n3 - Axe\n4 - Claw\n")
	weapChoice = input("Weapon: ")
	if weapChoice == 1:
		print("You chose Sword! Attack +2")
		weapons.sword(player_damage + 2)
		pass
	if weapChoice == 2:
		print("You chose Staff! Attack +1")
		weapons.staff(player_damage + 1)
		pass
	if weapChoice == 3:
		print("You chose Axe! Attack +3")
		weapons.axe(player_damage + 3)
		pass
	if weapChoice == 4:
		print("You chose Claw! Attack +4")
		weapons.claw(player_damage + 4)
		pass

print("==================PYBATTLE====================")
print("Welcome to PyBattle, input your character name...")
name = input("Character name: ")
playerWeapon(player_damage)

for i in range(1,3):
	print('.\n')
	time.sleep(1)
	pass

print("{} finds a {} BATTLE TIME!".format(name,randomEnemy))


#Battle Loop
while (enemy_hp > 0 or player_hp > 0):

	enemy_damage = random.randint(0,5)
	player_damage = random.randint(0,5)
	enemy_hp = enemy_hp - player_damage

	print("{0} hits {1} for {2} damage!\n{3} has {4} HP left!".format(name,randomEnemy,player_damage,randomEnemy,enemy_hp))
	
	if enemy_hp <= 0:
		print("{} WON THE BATTLE!".format(name))
		break

	for i in range(1,3):
		print('.\n')
		time.sleep(1)
		pass

	player_hp = player_hp - enemy_damage
	print("{0} hits {1} for {2} damage!\n{3} has {4} HP left!".format(randomEnemy,name,enemy_damage,name,player_hp))

	if player_hp <= 0:
		print("{} WON THE BATTLE!".format(randomEnemy))
		break

	for i in range(1,3):
		print('.\n')
		time.sleep(1)
		pass
	pass
#Battle loop end 