                        ### INTERNSPEDIA PYTHON INTERN ###  ### SEPTEMBER 2022- OCTOBER 2022 ###
                        ### MRIDUL KAPOOR ####      ### mridul.kapoor2002@gmail.com ###
                        ### PYTHON PROJECT 1 ###    ### GUESS THE NUMBER ###


#importing modules
import random

#Taking inputs from user
upper= int(input("Enter upper value of range: "))
lower= int(input("Enter lower value of range: "))

###generating random number
random_num_generated = random.randint(lower,upper)

#Taking the number we'll guess as none
#showing that we haven't guessed any number 
guessed_num = None

#Main code (Getting guesses)
while guessed_num!= random_num_generated:
    guessed_num = int(input("Guess a number within your range prescribed: "))

    ###working code
    if guessed_num == random_num_generated:
        print("CONGRATULATIONS!!! \nYou guessed the number")
        break
    elif guessed_num < random_num_generated:
        print("Wrong guess! Guess is smaller than random number generated! \n TRY AGAIN!")
    else:
        print("Wrong guess! Guess is larger than random number generated! \n TRY AGAIN!")

###CODE ENDS###