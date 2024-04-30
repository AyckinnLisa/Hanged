# --- DRAWING HANDLING ---

import colortx as ctx
import alphabet as ab
import wordmode as wd


def win_game():
    return (ctx.green('''
             √√
            √√
           √√
    √√    √√
     √√  √√     BRAVO !
      √√√√
       √√         
    '''))



def game_over():
    return (ctx.red('''
    xx      xx
     xx    xx
      xx  xx
       xxxx     PERDU !
      xx  xx
     xx    xx
    xx      xx
    '''))



def end_of_game():
    if len(ab.finded_letters) == len(ab.get_single_letter(wd.hidden_word)):
        print("\n", win_game())
    else:
        print("\n", game_over())    



def hangman_states(atmp):
    max_attempts = 6
    drawing = [
        ctx.green('''
      +-,---+
      |/    |
      |
      |
      |
      |
      |
      |
     _|________
        '''), ctx.green('''
      +-,---+
      |/    |
      |     O
      |
      |
      |
      |
      |
     _|________
            '''), ctx.yellow('''
      +-,---+
      |/    |
      |     O
      |     |
      |     |
      |
      |
      |
     _|________
        '''), ctx.yellow('''
      +-,---+
      |/    |
      |     O
      |     |
      |     |
      |    / 
      |
      |
     _|________
        '''), ctx.red('''
      +-,---+
      |/    |
      |     O
      |     |
      |     |
      |    / \\
      |
      |
     _|________
        '''), ctx.red('''
      +-,---+
      |/    |
      |     O
      |   >-|
      |     |
      |    / \\
      |
      |
     _|________
        '''), ctx.black('''
      +-,---+
      |/    |
      |     O
      |   >-|-<
      |     |
      |    / \\
      |
      |
     _|________
        ''')
    ]
    return drawing[max_attempts - atmp]
