# Write your code here
import random

def play_hangman():
    tries = 8
    word_list = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = random.choice(word_list)
    
    chosen_word_letters_set = set(chosen_word)
    
    total_to_guess = len(chosen_word_letters_set)
    
    hint_string = '-' * len(chosen_word)
    hint_list = list(hint_string)
    
    wrong_letters = set()
    
    guessed_letters = set()
    
    while tries > 0:
        print()
        print(''.join(hint_list))
        player_guess = input('Input a letter: ')
        
        if len(player_guess) != 1:
            print("You should input a single letter")
            continue
        if not player_guess.islower() or not player_guess.isascii():
            print("It is not an ASCII lowercase letter")
            continue
        
        if player_guess not in chosen_word_letters_set:
            if player_guess not in guessed_letters and player_guess not in wrong_letters:
                wrong_letters.add(player_guess)
                print('No such letter in the word')
                tries -= 1
                if (tries == 0):
                    print('You are hanged!')
                    print()
            else:
                print('You already typed this letter')
            
        else:
            total_to_guess -= 1
            start_index = 0
            letter_index = chosen_word.find(player_guess, start_index)
            while letter_index > -1:
                start_index = letter_index + 1
                hint_list[letter_index] = player_guess
                letter_index = chosen_word.find(player_guess, start_index)
            chosen_word_letters_set.discard(player_guess)
            guessed_letters.add(player_guess)
            if total_to_guess == 0:
                print('You guessed the word!')
                print('You survived!')
                print()
                break

print("H A N G M A N")

while True:
    command = input('Type "play" to play the game, "exit" to quit: ')
    if command == "exit":
        break
    if command == "play":
        play_hangman()
