#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

WORDS = ["python", "pavan", "developer", "challenge", "keyboard", "computer", "Artificial", "hangman"]

word = random.choice(WORDS)
guessed_letters = []
attempts=7

print("Welcome to hangman!")
print("Guess the word - You have",attempts,"lives.\n")

display_word = ["_"] * len(word)

while attempts>0 and "_" in display_word:
    print("Word: "," ".join(display_word))
    print("Guessed letters: ", ", ".join(guessed_letters))
    print(f"Lives left: {attempts}")
    
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter omly one letter. \n")
        continue
    if guess in guessed_letters:
        print("You have already guesed that letter.\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print("Good guess.\n")
        for i, letter in enumerate(word):
            if letter==guess:
                display_word[i] = guess
    else:
        print("Wromg guess")
        attempts -=1 
if "_" not in display_word:
    print("Congratulations! You guessed the word: ", word)
else:
    print("Game over! The word was: ", word)


# In[ ]:




