#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 10")

#Generating a random number
secret_number = random.randint(1,10)
#Using a variable for counting the attempts
attempts = 0
#Loop until a player guesses the number correctly, hence a while loop
while True:
    guess = int(input("Enter your guess: "))
    attempts+=1
    
    #Comparing the number
    if guess < secret_number:
        print("Too Low! try again")
    elif guess> secret_number:
        print("Too High! Try again")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts!")
        break


# In[ ]:





# In[ ]:




