import random

class Hangman:
    ''' 
    This Class is used to initialise the attributes to run our hangman game.
        
        Attributes:
            The self is used to initialize this instance of our class
            word_list(str): Used to store the list we want to guess.
            num_lives: used to count the number of lives we have left.    
            random.choice(word_list) : used to randomly select a word from our list for us to guess.    
            
            word_guessed=['_'] * len(self.word) : used to store our words to guess in a ' _ ' blank fortmat
            where the underscore denotes the letters we have yet to guess.
            num_letters=len(set(self.word)): used to store the number of letters in each word to guess,
            they are stored in a set because of their unique property.
            list_of_guesses=[]: This is used to store our guesses in a list format.
                
                '''
    def __init__(self,word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    
    
    def check_guess(self, guess):
        ''' 
        This function takes the guess from another function and checks to see if it is valid.
            Depending on the input, it will tell you if you guessed correctly or incorrectly.
        Args:
            guess(str): This is the letter we're providing to be compated against a chosen word.
        '''
        guess = guess.lower()
        ''' 
        This if statement followed by the for loop, checks the validity of our provided guess
            by matching it against our stored words, letter by letter. It does this via indexing.
            
            Returns:
                str:When succesful, it decrements each letter by 1. 
                str:Sends our current guesses to a print statement so the player has a live view of their progress.
                str:When unsuccesful, it passes to the else statement which tells you the given letter
                is not in the list and then removes one of the lives.

        '''
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -=1
            print(self.word_guessed)
        else:
            self.num_lives-= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
            
    def ask_for_input(self):
            ''' 
            This function asks the user for an input.
                It filters the user input to make sure there are no invalid or duplicate inputs.

                Returns:a
                    str: Invalid letter if letter is len of letter is more than 1 and if not alphabetical.
                    str: You already tried that if duplicate letter detected.
                    
            '''
            guess = input('Guess a letter: ')
            if len(guess)!=1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    '''
        This function brings together the rest of the code and defines the winning and losing terms.
        Args:
            word_list: our provided list of fruits to guess
        Returns:
            str: Game over when the number of lives reaches 0
            str: Congratulations when the remaining letters hits 0 
            Continues to prompt the user if these two conditions are not met.
            break statement terminates the game when the success or failure conditions are met.
        '''
    num_lives = 5
    game=Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print('Game over, try again')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations you've won the game")        
            print(f'the word was: {game.word}')
            break
if __name__ =="__main__":
    word_list = ['watermelon','mandarin','mango','apple','grape']
    play_game(word_list)
