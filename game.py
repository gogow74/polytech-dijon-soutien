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

