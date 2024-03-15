import random

word_list=['watermelon','mandarin','mango','apple','grape']
word=random.choice(word_list)

guess=str(input('Choose a letter : '))
if len(guess)== 1 and guess.isalnum:
    print('good guess')
else:
    print('Oops that is not a valid input')