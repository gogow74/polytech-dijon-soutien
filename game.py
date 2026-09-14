import config
import random

def code_creation():
    code = []

    for _ in range(config.code_length):
        x = random.randint(0, len(config.colors)-1)
        code.append(config.colors[x][0])

    return code

def afficher_couleurs():
    for i in range(len(config.colors)):
        print(config.colors[i][0], ":", config.colors[i][1])

def saisie_code():
    lettres_valides = []
    for i in range(len(config.colors)):
        lettres_valides.append(config.colors[i][0])

    saisie = []
    for i in range(config.code_length):
        saisieInvalide = True
        while saisieInvalide:
            #enelve les espaces et met tt en maj
            x = input(f"Choix de la couleur {i+1} : ").strip().upper()
            if x in lettres_valides :
                saisieInvalide = False
            else:
                print("Saisie invalide")
        saisie.append(x)
    return saisie
