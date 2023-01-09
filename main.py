#import libraries for game
import random 
import os
import time

colors = "RGBY"
#create a color variable
simon = " "

for score in range(0, 10):
    #number of loops in the  game
    simon += random.choice(colors)
    #pick a random color
    for color in simon:
        print(color)
        time.sleep(1.5)
        #wait before OS system to clear
        os.system("clear")
        #clear the screen ("clear on mac")
    guess = input("Repeat: ")
    os.system("clear")

    if guess != simon:
        break
      
    
    print("Game over! Your Final Score is {score}! ")
