import random
import time
import string
import sys

print(f"Welcome to hangman! You start off with 8 guesses in order to guess a word :)")
time.sleep(2)

def chooseword(): #Chooses word
  with open('words.txt', 'r') as f: 
    lines = f.readlines() 
  chosenword = random.choice(lines)

  return chosenword

def getAvailableLetters(lettersGuessed): #Gets letters  
    ans =list(string.ascii_lowercase)
    for i in lettersGuessed:
      ans.remove(i)
    letters = ', '.join(ans)
    print(letters)

def underscore(chosenword, lettersGuessed):
  s=[]
  for i in chosenword:
      if i in lettersGuessed:
          s.append(i)
  underscore =''
  for i in chosenword:
      if i in s:
          underscore +=(f"{i} ")
      else:
          underscore +='_ '
  return underscore

def gotword(lettersGuessed, chosenword):
  count = 0
  for i in lettersGuessed:
    if i in chosenword:
      count += 1
  if len(chosenword) == count:
    time.sleep(1)
    print("\nGG! You got the word.")
    time.sleep(1)
    sys.exit()
  else:
    return False

global lettersGuessed
lettersGuessed=[] 
chosenword = chooseword()
chosenword = list(chosenword)
del chosenword[-1]
wordlength = len(chosenword)

print(f"Word found. It it {wordlength} letters long.")
time.sleep(1)
mistakes = 0
guessleft = 8 - mistakes 
while True: 
  if 8 - mistakes > 0:
    guess = input(f"""\nYou have {8 - mistakes} guesses left. Enter 'AW' to see all the remaining characters you can use, else only the first character you enter will be accepted.\n\nYour current word is: {underscore(chosenword, lettersGuessed)} -> """)

    guess = guess.lower()
    try:
      if guess == 'aw':
        getAvailableLetters(lettersGuessed)
      elif guess is not None:#Smth there
        if guess in lettersGuessed: #Guessed b4
          print(f"Letter already guessed: {guess}.")
          time.sleep(1)
        elif guess in chosenword and guess not in lettersGuessed: #Correct letter
          lettersGuessed.append(guess)
          print(f"Good guess: {guess}")
          gotword(lettersGuessed, chosenword)
        else: #Wrong
          guess = guess[0]
          lettersGuessed.append(guess)
          #print(guess)
          print(chosenword)
          print(f"Letter {guess} is wrong.")
          mistakes += 1

    except IndexError:
      print('Nothing was entered..\n')
  elif 8 - mistakes == 0:
    answer = ' '.join(chosenword)
    print("--------------------\n")
    print(f"Game over! the word was: {answer}.")
    time.sleep(1)
    break
