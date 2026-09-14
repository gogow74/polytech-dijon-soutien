#verif entre le code et le guess et renvoi le nbr de bons et le nbr de mal placés
import config

def score(guess, code):
    bon = 0
    mal_place = 0

    guess_copy = guess.copy()
    code_copy = code.copy()

    for i in range(config.code_length - 1, -1, -1):
        if guess_copy[i] == code_copy[i] :
            bon += 1
            del guess_copy[i]
            del code_copy[i]

    for j in guess_copy:
        if j in code_copy:
            mal_place += 1
            code_copy.remove(j)

    return bon, mal_place

#print(scoring(['R','V','B','J'],['R','R','R','R']))