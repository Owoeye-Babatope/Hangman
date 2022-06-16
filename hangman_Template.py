'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from enum import unique
import random
from textwrap import indent

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
        self.rem = 0
        randindex = random.randrange(len(word_list)) # random index to select one of the word in the given list
        self.word = word_list[randindex] # The selected word to be guessed by user
        self.word_guessed = list('_'*len(self.word)) # list of the correctly guessed words which is displayed
        self.unique = []  # initialze the list to append all unique letters
        '''

        for char in list(self.word):
            if char not in self.unique:
                self.unique.append(char)
        '''
        self.num_letters = len(self.unique)   # Declares the number of unique letters which is to be guessed by the user
        #num_letters  = self.num_letters
        
        self.num_lives = num_lives 
        self.list_letters = [] # the list of letters correctly guessed so far
        self.rem = len(self.word) - len(self.list_letters) # The number of letters remaining to be guessed 

        a = len(self.word) # word length
        print("The mystery word has {} characters".format(a)) # Hint on thenumber of letters to be guessed


    def check_letter(self, letter) -> None:       
        word_lower = self.word.lower()
        

        if (letter in list(word_lower)):
            ## check the number of times it is present
            count = 0
            indices = []
            
            for let in list(word_lower):
                if letter == let:
                    count = count + 1
            if (count > 1):
                word = list(word_lower[:])

                for cha in word:
                    if (cha == letter):
                       index = word.index(letter)
                       # self.list_letters.append(cha)
                       indices.append(index)
                       word[index] = '_'
                    #print(f"indices is {indices}")
            else:
                indices.append(list(word_lower).index(letter))
            
            for index in indices:
                self.word_guessed = list(self.word_guessed) 
                self.word_guessed[index] = letter
                self.num_letters = self.num_letters - 1
                self.list_letters.append(letter)
                
                
                self.rem = len(self.word) - len(self.list_letters)
                print('The remaining numbers of life is {}'.format(self.num_lives))
                
                #print('The lis of letters guessed is {}'.format(self.list_letters))
                print("{}".format(self.word_guessed))
                #print('The remaining numbers of letter to guess is {}'.format(self.rem))
                #print(self.unique)


        elif(letter not in self.word.lower()):
            self.num_lives = self.num_lives - 1
            print('You guessed wrong')
            if (self.num_lives > 0 and self.rem > 0):
                for cha in self.word_guessed:
                    if cha == '_':
                        index = self.word_guessed.index(cha)
                        let = list(self.word)[index]
                        self.list_letters.append(let)
                        self.word_guessed[index] = let
                        break
                print('The remaining numbers of life is {}'.format(self.num_lives))
                print("{}".format(self.word_guessed))
                self.ask_letter()
            else:
                print('The remaining numbers of life is {}'.format(self.num_lives))
                print("{}".format(self.word_guessed))
                
            

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method

        input_validated = True
        letter = ''
        while(input_validated):


            if(len(letter) == 1 and letter not in self.list_letters):
                self.check_letter(letter)
                input_validated = False
            elif (len(letter) > 1):
                letter = input('Enter a single letter you think is in the guess!')
            else:
                letter = input('Enter a letter you think is in the guess!')
def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    
    while(game.num_lives > 0 and game.rem > 0):
        game.ask_letter()
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"
    
    

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
