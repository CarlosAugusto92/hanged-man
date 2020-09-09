#This code is a game called hanged
import random


IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''', '''


''']


WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

WORDS2 = [
     'contraposicion',
     'rocamadour',
     'tomorrow',
     'mecanica',
     'astrofisica',
     'biotecnologia',
     'mecatronica',
     'engineering'
]

WORDS3 = [
    'parangaricutiro',
    'esternomastoideo',
    'desoxirribonucleico',
    'eucariota',
    'fotosintesis',
    'prometeo',
    'nabucodonosor',
    'antropologia'
]

def Menu_Options():
    print("Select a level of difficulty")
    print("Level 1.")
    print("Level 2.")
    print("Level 3.")

        


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def random_word_leveltwo():
    idx = random.randint(0, len(WORDS2) - 1)
    return WORDS2[idx]


def random_word_levelthree():
    idx = random.randint(0, len(WORDS3) - 1)
    return WORDS3[idx]
        



def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def run():

    option_selected = input()

    if option_selected == '1':
        word = random_word()

    elif option_selected == '2':
        word = random_word_leveltwo()
        
    elif option_selected  == '3':
        word = random_word_levelthree()

    
    #word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Select a letter: '))

        letter_indexes = []

        for idx in range (len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print ('')
                print('G A M E  O V E R!  T H E  C O R R E C T  W O R D  W A S  {}'.format(word))
               
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print ('')
            print ('F I N I S H, Y O U  W I N!,  T H E  W O R D  I S : {}'. format(word))
            break
                
        


if __name__ == '__main__':

    print('W E L C O M E  T O  T H E  H A N G E D  G A M E!')
    Menu_Options()
    run()






