import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list= word_list
        self.num_lives=num_lives
        self.word=random.choice(word_list)
        self.word_guessed=['_'] * len(self.word)
        self.num_letters=len(set(self.word))
        self.list_of_guesses=[]

    
    
    def check_guess(self,guess):
        guess=guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] ==guess:
                    self.word_guessed[i]=guess
            self.num_letters -=1
            print(self.word_guessed)
        else:
            self.num_lives-=1
            print('Sorry, 'f'{guess} is not in the word')
            print('You have ' f'{self.num_lives} lives left')
            
    def ask_for_input(self):
            guess=input('Guess a letter: ')
            if len(guess)!=1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives=5
    game=Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print('Game over, try again')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulatuons you've won the game")        
            print('the word was'f'{self.word}')
            break
word_list=['watermelon','mandarin','mango','apple','grape']
game=Hangman(word_list)
play_game(word_list)