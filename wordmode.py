# -- WORDS HANDLING --

import os, random
import wordlist
import colortx as ctx
import logo as lg
import alphabet as ab
import drawing as dw


def select_word_in_list(words):
    return random.choice(words)
    
hidden_word = select_word_in_list(wordlist.words)
len_hidden_word = (len(hidden_word))



def display_hidden_word(hidden_word, finded_letters):
    for letter in hidden_word:
        if letter in finded_letters:
            print(ctx.magenta(f"{letter} "), end="")
        else:
            print(ctx.magenta("_ "), end="")



def display_board(remaining_attempts):
    os.system('clear')
    print(lg.logo())

    print("", ab.display_alphabet())
    print(dw.hangman_states(remaining_attempts))

    print(f"\n Mot à trouver ({len_hidden_word} lettres) :  ", end="")
    display_hidden_word(hidden_word, ab.finded_letters)

    print("\n")
    print(ctx.yellow(f" Essais restants : {remaining_attempts}\n"))
