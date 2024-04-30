#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import colortx as ctx
import alphabet as ab
import wordmode as wd
import drawing as dw


remaining_attempts = 6

while remaining_attempts > 0 and len(ab.finded_letters) < len(ab.get_single_letter(wd.hidden_word)):
    wd.display_board(remaining_attempts)

    letter = input("\n Entrer une lettre : ").upper()

    if "!Q" in letter:
            print(ctx.red("\n Fin de jeu... A bientot :)"))
            exit(0)


    if len(letter) > 1 or not letter.isalpha():
        print(ab.wrong_entry())
        
    elif ab.is_letter_in_hidden_word(letter):
        if letter in ab.finded_letters:
            print(ab.letter_already_finded(letter))
        else:
            print(ab.letter_in_hidden_word(letter))
            ab.finded_letters.append(letter)
    else:
        if letter in ab.trash:
            print(ab.letter_already_selected(letter))
        else:    
            print(ab.letter_not_in_hidden_word(letter))
            ab.trash.append(letter)
        remaining_attempts -= 1
    
    time.sleep(1)
    ab.delete_letter_in_alphabet(letter)


wd.display_board(remaining_attempts)
dw.end_of_game()
