import numpy as np

map = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
tableau = np.array(map)
def verif_win():
    if tableau[0][0] == tableau[0][1] and tableau[0][1] == tableau[0][2]:
        print("ligne")
        return True
    elif tableau[1][0] == tableau[1][1] and tableau[1][1] == tableau[1][2]:
        print("ligne")
        return True
    elif tableau[2][0] == tableau[2][1] and tableau[2][1] == tableau[2][2]:
        print("ligne")
        return True
    
    
    elif tableau[0][0] == tableau[1][0] and tableau[1][0] == tableau[2][0]:
        print("colonne")
        return True
    elif tableau[0][1] == tableau[1][1] and tableau[1][1] == tableau[2][1]:
        print("colonne")
        return True
    elif tableau[0][2] == tableau[1][2] and tableau[1][2] == tableau[2][2]:
        print("colonne")
        return True
    

    elif tableau[0][0] == tableau[1][1] and tableau[1][1] == tableau[2][2]:
        print("diagonal")
        return True
    elif tableau[0][2] == tableau[1][1] and tableau[1][1] == tableau[2][0]:
        print("diagonal")
        return True

def ajoute_joueur1():

    x = input("JOUEUR1 ==>")
    indice = np.where(tableau == x)
    tableau[indice] = "X"
    draw_map()
    
def ajoute_joueur2():
    y = input("JOUEUR2 ==>")
    indice = np.where(tableau == y)
    tableau[indice] = "O"
    draw_map()

def draw_map():
    print(tableau)


    
g = True
draw_map()
compteur = 0     
while g:
    ajoute_joueur1()
    c = verif_win()
    if c is True:
        print("JOUEUR1 A GAGNER")
        g = False
        break

    ajoute_joueur2()
    verif_win()
    c = verif_win()
    if c is True:
        print("JOUEUR2 A GAGNER")
        g = False
        break
    compteur += 1
    if compteur > 4:
        print("égalité on recommence")
        map = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
        tableau = np.array(map)
        draw_map()

