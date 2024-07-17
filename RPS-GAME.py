import random
import math
print("------------WELCOME TO THE ROCK PAPER SCISSOR GAME--------- ")
print("--------------------",end='')
print("\U0001f600",end='')            
print("\U0001f600",end='')
print("\U0001f600",end='')
print("\U0001f600",end='')
print("--------------------")
print("----------YOU READY FOR THIS !!! ENTER YOUR CHOICE---------")
print("-----------------------------------------------------------")
print("----'R' for ROCK , 'P' for PAPER , 'S' for SCISSORS ----")    

# Function to check who wins in a round
def win(player, opponent):               
    if((player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r')):
        return True
    else:
        return False

# Function to play the game until someone wins the best of 'n' rounds
def best_of(n):
    user_win=0
    computer_win=0
    user_input=""
    computer_choice=""
    
    # Calculating the necessary wins to declare an overall winner
    necessary_win=math.ceil(n/2)
    while((user_win<necessary_win) and (computer_win<necessary_win)):
        user_input=input()
        user_input=user_input.lower()
    
        computer_choice= random.choice(['r','s','p'])
        if(user_input==computer_choice):
            print("IT`S A TIE.")
        elif win(user_input,computer_choice):
            print("YOU WON")
            user_win=user_win+1
        else:
            print("YOU LOST")
            computer_win=computer_win+1
    return(user_win,computer_win) 

# Asking the user how many times they want to play the game    
number_of_time=int(input("HOW MANY TIMES DO YOU WANNA PLAY THIS GAME : "))

# Calling the best_of function to play the game
user_win, computer_win=best_of(number_of_time)

# Declaring the overall winner
if (computer_win<user_win):
    print("YOU WON CHAMP  ;) ")
else:
    print("YOU LOST BRUHH  :( BETTER LUCK NEXT TIME ")