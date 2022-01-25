import numpy as np
import random
import keyboard
from time import sleep
from os import system, name

# Définit les quatres actions possibles sur la grille :
# HAUT
def up(mat) :
	matrice = np.array(mat)
	for z in range(4) :
		for j in range(4) :
			for i in range(3) :
				if z != 2 :
					if matrice[i,j] == 0 :
						matrice[i,j] = matrice[i+1,j]
						matrice[i+1,j] = 0
				else :
					if matrice[i,j] == matrice[i+1,j] :
						matrice[i,j] = 2 * matrice[i,j]
						matrice[i+1,j] = 0
	return matrice

# BAS
def down(mat) :
	matrice = np.array(mat)
	for z in range(4) :
		for j in range(4) :
			for i in range(3) :
				if z!= 2 :
					if matrice[3-i,j] == 0 :
						matrice[3-i,j] = matrice[3-(i+1),j]
						matrice[3-(i+1),j] = 0
				else :
					if matrice[3-i,j] == matrice[3-(i+1),j] :
						matrice[3-i,j] = 2 * matrice[3-i,j]
						matrice[3-(i+1),j] = 0
	return matrice

# DROITE
def right(mat) :
	matrice = np.array(mat)
	for z in range(4) :
		for i in range(4) :
			for j in range(3) :
				if z != 2 :
					if matrice[i,3-j] == 0 :
						matrice[i,3-j] = matrice[i,3-(j+1)]
						matrice[i,3-(j+1)] = 0
				else :
					if matrice[i,3-j] == matrice[i,3-(j+1)] :
						matrice[i,3-j] = 2 * matrice[i,3-j]
						matrice[i,3-(j+1)] = 0
	return matrice

# GAUCHE
def left(mat) :
	matrice = np.array(mat)
	for i in range(4) :
		for j in range(3) :
			if matrice[i,j] == matrice[i,j+1] :
				matrice[i,j] = 2 * matrice[i,j]
				matrice[i,j+1] = 0
	for z in range(4) :
		for i in range(4) :
			for j in range(3) :
				if z != 2 :
					if matrice[i,j] == 0 :
						matrice[i,j] = matrice[i,j+1]
						matrice[i,j+1] = 0
				else :
					if matrice[i,j] == matrice[i,j+1] :
						matrice[i,j] = 2 * matrice[i,j]
						matrice[i,j+1] = 0
	return matrice
	
# Cherche les 0 dans le tableau, en prends un au hasard et le remplace par la valeur 2 ou 4
def rand(matrice) :
	w = np.where(matrice == 0)
	l = len(w[0])
	
	if l != 0 : # Evite un index out of range
		r = random.choice(range(l))
		if random.random() < 0.8 :
			matrice[w[0][r] , w[1][r]] = 2
		else :
			matrice[w[0][r] , w[1][r]] = 4
	return matrice

# Clear screen
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Draw the state of the game using the matrice
def draw(mat) :
	
	# Create the raw game board
	square = np.array([	" .-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------. ",
				"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |                                            | |                                            | |                                            | |                                            | |",
				"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
				"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |                                            | |                                            | |                                            | |                                            | |",
				"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
				"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |                                            | |                                            | |                                            | |                                            | |",
				"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
				"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |",
				"| |                                            | |                                            | |                                            | |                                            | |",
				"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
				" '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------' "])
	
	# Add number parts to the list of strings according to their placement in the matrice
	for j in range(4) :
		for i in range(4) :
			if mat[i, j] == 0 :
				square[2 + 9 * i] += "                                            | |"
				square[3 + 9 * i] += "                                            | |"
				square[4 + 9 * i] += "                                            | |"
				square[5 + 9 * i] += "                                            | |"
				square[6 + 9 * i] += "                                            | |"
				square[7 + 9 * i] += "                                            | |"
			elif mat[i, j] == 2 :
				square[2 + 9 * i] += "                    ___                     | |"
				square[3 + 9 * i] += "                   |__ \                    | |"
				square[4 + 9 * i] += "                      ) |                   | |"
				square[5 + 9 * i] += "                     / /                    | |"
				square[6 + 9 * i] += "                    / /_                    | |"
				square[7 + 9 * i] += "                   |____|                   | |"
			elif mat[i, j] == 4 :
				square[2 + 9 * i] += "                   _  _                     | |"
				square[3 + 9 * i] += "                  | || |                    | |"
				square[4 + 9 * i] += "                  | || |_                   | |"
				square[5 + 9 * i] += "                  |__   _|                  | |"
				square[6 + 9 * i] += "                     | |                    | |"
				square[7 + 9 * i] += "                     |_|                    | |"
			elif mat[i, j] == 8 :
				square[2 + 9 * i] += "                    ___                     | |"
				square[3 + 9 * i] += "                   / _ \                    | |"
				square[4 + 9 * i] += "                  | (_) |                   | |"
				square[5 + 9 * i] += "                   > _ <                    | |"
				square[6 + 9 * i] += "                  | (_) |                   | |"
				square[7 + 9 * i] += "                   \___/                    | |"
			elif mat[i, j] == 16 :
				square[2 + 9 * i] += "                 __     __                  | |"
				square[3 + 9 * i] += "                /_ |   / /                  | |"
				square[4 + 9 * i] += "                 | |  / /_                  | |"
				square[5 + 9 * i] += "                 | | | '_ \                 | |"
				square[6 + 9 * i] += "                 | | | (_) |                | |"
				square[7 + 9 * i] += "                 |_|  \___/                 | |"
			elif mat[i, j] == 32 :
				square[2 + 9 * i] += "                ____    ___                 | |"
				square[3 + 9 * i] += "               |___ \  |__ \                | |"
				square[4 + 9 * i] += "                 __) |    ) |               | |"
				square[5 + 9 * i] += "                |__ <    / /                | |"
				square[6 + 9 * i] += "                ___) |  / /_                | |"
				square[7 + 9 * i] += "               |____/  |____|               | |"
			elif mat[i, j] == 64 :
				square[2 + 9 * i] += "                 __    _  _                 | |"
				square[3 + 9 * i] += "                / /   | || |                | |"
				square[4 + 9 * i] += "               / /_   | || |_               | |"
				square[5 + 9 * i] += "              | '_ \  |__   _|              | |"
				square[6 + 9 * i] += "              | (_) |    | |                | |"
				square[7 + 9 * i] += "               \___/     |_|                | |"
			elif mat[i, j] == 128 :
				square[2 + 9 * i] += "              __   ___     ___              | |"
				square[3 + 9 * i] += "             /_ | |__ \   / _ \             | |"
				square[4 + 9 * i] += "              | |    ) | | (_) |            | |"
				square[5 + 9 * i] += "              | |   / /   > _ <             | |"
				square[6 + 9 * i] += "              | |  / /_  | (_) |            | |"
				square[7 + 9 * i] += "              |_| |____|  \___/             | |"
			elif mat[i, j] == 256 :
				square[2 + 9 * i] += "            ___    _____     __             | |"
				square[3 + 9 * i] += "           |__ \  | ____|   / /             | |"
				square[4 + 9 * i] += "              ) | | |__    / /_             | |"
				square[5 + 9 * i] += "             / /  |___ \  | '_ \            | |"
				square[6 + 9 * i] += "            / /_   ___) | | (_) |           | |"
				square[7 + 9 * i] += "           |____| |____/   \___/            | |"
			elif mat[i, j] == 512 :
				square[2 + 9 * i] += "              _____   __   ___              | |"
				square[3 + 9 * i] += "             | ____| /_ | |__ \             | |"
				square[4 + 9 * i] += "             | |__    | |    ) |            | |"
				square[5 + 9 * i] += "             |___ \   | |   / /             | |"
				square[6 + 9 * i] += "              ___) |  | |  / /_             | |"
				square[7 + 9 * i] += "             |____/   |_| |____|            | |"
			elif mat[i, j] == 1024 :
				square[2 + 9 * i] += "          __    ___    ___    _  _          | |"
				square[3 + 9 * i] += "         /_ |  / _ \  |__ \  | || |         | |"
				square[4 + 9 * i] += "          | | | | | |    ) | | || |_        | |"
				square[5 + 9 * i] += "          | | | | | |   / /  |__   _|       | |"
				square[6 + 9 * i] += "          | | | |_| |  / /_     | |         | |"
				square[7 + 9 * i] += "          |_|  \___/  |____|    |_|         | |"
			elif mat[i, j] == 2048 :
				square[2 + 9 * i] += "        ___     ___    _  _      ___        | |"
				square[3 + 9 * i] += "       |__ \   / _ \  | || |    / _ \       | |"
				square[4 + 9 * i] += "          ) | | | | | | || |_  | (_) |      | |"
				square[5 + 9 * i] += "         / /  | | | | |__   _|  > _ <       | |"
				square[6 + 9 * i] += "        / /_  | |_| |    | |   | (_) |      | |"
				square[7 + 9 * i] += "       |____|  \___/     |_|    \___/       | |"
			elif mat[i, j] == 4096 :
				square[2 + 9 * i] += "       _  _      ___     ___      __        | |"
				square[3 + 9 * i] += "      | || |    / _ \   / _ \    / /        | |"
				square[4 + 9 * i] += "      | || |_  | | | | | (_) |  / /_        | |"
				square[5 + 9 * i] += "      |__   _| | | | |  \__, | | '_ \       | |"
				square[6 + 9 * i] += "         | |   | |_| |    / /  | (_) |      | |"
				square[7 + 9 * i] += "         |_|    \___/    /_/    \___/       | |"
			elif mat[i, j] == 8192 :
				square[2 + 9 * i] += "          ___    __    ___    ___           | |"
				square[3 + 9 * i] += "         / _ \  /_ |  / _ \  |__ \          | |"
				square[4 + 9 * i] += "        | (_) |  | | | (_) |    ) |         | |"
				square[5 + 9 * i] += "         > _ <   | |  \__, |   / /          | |"
				square[6 + 9 * i] += "        | (_) |  | |    / /   / /_          | |"
				square[7 + 9 * i] += "         \___/   |_|   /_/   |____|         | |"
			elif mat[i, j] == 16384 :
				square[2 + 9 * i] += "    __     __    ____     ___    _  _       | |"
				square[3 + 9 * i] += "   /_ |   / /   |___ \   / _ \  | || |      | |"
				square[4 + 9 * i] += "    | |  / /_     __) | | (_) | | || |_     | |"
				square[5 + 9 * i] += "    | | | '_ \   |__ <   > _ <  |__   _|    | |"
				square[6 + 9 * i] += "    | | | (_) |  ___) | | (_) |    | |      | |"
				square[7 + 9 * i] += "    |_|  \___/  |____/   \___/     |_|      | |"
			elif mat[i, j] == 32768 :
				square[2 + 9 * i] += "   ____    ___    ______     __     ___     | |"
				square[3 + 9 * i] += "  |___ \  |__ \  |____  |   / /    / _ \    | |"
				square[4 + 9 * i] += "    __) |    ) |     / /   / /_   | (_) |   | |"
				square[5 + 9 * i] += "   |__ <    / /     / /   | '_ \   > _ <    | |"
				square[6 + 9 * i] += "   ___) |  / /_    / /    | (_) | | (_) |   | |"
				square[7 + 9 * i] += "  |____/  |____|  /_/      \___/   \___/    | |"
			elif mat[i, j] == 65536 :
				square[2 + 9 * i] += "     __    _____   _____   ____      __     | |"
				square[3 + 9 * i] += "    / /   | ____| | ____| |___ \    / /     | |"
				square[4 + 9 * i] += "   / /_   | |__   | |__     __) |  / /_     | |"
				square[5 + 9 * i] += "  | '_ \  |___ \  |___ \   |__ <  | '_ \    | |"
				square[6 + 9 * i] += "  | (_) |  ___) |  ___) |  ___) | | (_) |   | |"
				square[7 + 9 * i] += "   \___/  |____/  |____/  |____/   \___/    | |"
	
	# Draw the entire board by printing the list of strings
	for k in range(len(square)) :
		print(square[k])


# Initialisation des variables :
mat1 = np.array([[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]])
mat2 = np.array([[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]])
rand(mat2)
rand(mat2)

clear()

print("""




	   222222222222222         000000000            444444444       888888888     
	  2:::::::::::::::22     00:::::::::00         4::::::::4     88:::::::::88   
	  2::::::222222:::::2  00:::::::::::::00      4:::::::::4   88:::::::::::::88 
	  2222222     2:::::2 0:::::::000:::::::0    4::::44::::4  8::::::88888::::::8
	              2:::::2 0::::::0   0::::::0   4::::4 4::::4  8:::::8     8:::::8
	              2:::::2 0:::::0     0:::::0  4::::4  4::::4  8:::::8     8:::::8
	           2222::::2  0:::::0     0:::::0 4::::4   4::::4   8:::::88888:::::8 
	      22222::::::22   0:::::0 000 0:::::04::::444444::::444  8:::::::::::::8  
	    22::::::::222     0:::::0 000 0:::::04::::::::::::::::4 8:::::88888:::::8 
	   2:::::22222        0:::::0     0:::::04444444444:::::4448:::::8     8:::::8
	  2:::::2             0:::::0     0:::::0          4::::4  8:::::8     8:::::8
	  2:::::2             0::::::0   0::::::0          4::::4  8:::::8     8:::::8
	  2:::::2       2222220:::::::000:::::::0          4::::4  8::::::88888::::::8
	  2::::::2222222:::::2 00:::::::::::::00         44::::::44 88:::::::::::::88 
	  2::::::::::::::::::2   00:::::::::00           4::::::::4   88:::::::::88   
	  22222222222222222222     000000000             4444444444     888888888     
  
  
  
  
""")

sleep(3)


# Boucle du jeu
while True :
	
	sleep(0.5)
	clear()
	draw(mat2)
	mat1 = np.array(mat2)
	
	key = keyboard.read_key()
	
	if key == "up" :
		mat2 = np.array(up(mat1))
		rand(mat2)

	elif key == "down" :
		mat2 = np.array(down(mat1))
		rand(mat2)

	elif key == "right" :
		mat2 = np.array(right(mat1))
		rand(mat2)

	elif key == "left" :
		mat2 = np.array(left(mat1))
		rand(mat2)

	elif key == "esc" :
		break



# Fin du jeu
clear()
print("""
 _____   ___  ___  ___ _____   _____  _   _ ___________  
|  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \ 
| |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ / 
| | __ |  _  || |\/| ||  __|  | | | || | | |  __||    /  
| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \  
 \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_| 
""")
