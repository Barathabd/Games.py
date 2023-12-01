
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print('''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/            ''')
from hangman_words import word_list
guess=random.choice(word_list)
display=[]
lives=7
for i in (guess):
    display+='_'
print(display)
end_of_game=False
while  not end_of_game:
    choice=input(("Enter a letter: ").lower())
    if choice in display:
        print(f"you have already guessed the letter {choice}")

    for i in range(len(guess)):
        if guess[i]==choice:
            display[i]=choice
    if choice not in guess:
        lives-=1
        
        print(stages[lives])
        print(f"")
        print(f"Remaining lives left is :{lives}")
        
    if lives==0:
            end_of_game=True
            print("you loose")
    
    print(display)
    
    if ('_' not in  display):
        end_of_game=True
        print("you win")
    