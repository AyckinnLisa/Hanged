# --- LETTERS HANDLING ---

import colortx as ctx
import wordmode as wd


alphabet = [
	"A", "B", "C", "D", "E",
	"F", "G", "H", "I", "J",
	"K", "L", "M", "N", "O",
	"P", "Q", "R", "S", "T",
	"U", "V", "W", "X", "Y", "Z"
]

finded_letters = []
trash = []


def display_alphabet():
    return ' '.join(alphabet)


# set - supprime toutes les lettres doublons d'un mot
def get_single_letter(word):
    return "".join(set(word))



def is_letter_in_hidden_word(letter):
    if letter in wd.hidden_word:
        return True
    else:
        return False



def delete_letter_in_alphabet(letter):
    if letter in alphabet:
        for l in range(len(alphabet)):
            if alphabet[l] == letter:
                alphabet[l] = "_"



def wrong_entry():
    return (ctx.red("\n Ni chiffres, ni symboles et qu'une seule lettre à la fois..."))


def letter_already_finded(letter):
    return (ctx.blue(f"\n La lettre [{letter}] a déjà été trouvée..."))


def letter_in_hidden_word(letter):
    return (ctx.green(f"\n La lettre [{letter}] est dans le mot caché..."))


def letter_already_selected(letter):
    return (ctx.red(f"\n La lettre [{letter}] a déjà été selectionnée..."))


def letter_not_in_hidden_word(letter):
    return (ctx.red(f"\n La lettre [{letter}] n'est pas dans le mot caché..."))
