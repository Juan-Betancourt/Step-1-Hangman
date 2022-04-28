#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

user_word_selection = input("Guess a letter associated with the mystery word \n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

def find_number():
    letter_char = []
    
    for char in chosen_word:
      if char == user_word_selection:
        print("Right")
        # letter_char.append(char)
      else:
        print("Wrong")
    # print(letter_char)

find_number()