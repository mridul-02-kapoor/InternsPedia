### INTERNSPEDIA PYTHON INTERN ###  ### SEPTEMBER 2022- OCTOBER 2022 ###
### MRIDUL KAPOOR ####      ### mridul.kapoor2002@gmail.com ###
### PYTHON PROJECT 2 ###    ### TEXT BASED ADVENTURE ###

#function to ask play again or not
def lets_play_again():
    print("\nDo you want to play again? (y or n)")

    #convert player's input to lower case
    answer = input(">").lower()

    #loop function
    if answer == "y":
        start()
    else:
        exit()



#game_over function accepts an argument called "reason"
def game_over(reason):
    #reason for loosing at snake_room
    if reason == 1:
        print("You want eggs not the treasure!! That's why snake killed you. \nGame Over!")
        lets_play_again()
    
    #reason for loosing at monster_room
    if reason == 2:
        print("The monster was hungry, he/it ate you. \nGame Over!")
        lets_play_again()



#Treasure room
def treasure_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do?   (1 or 2)")
    print("1). Take some diamonds  and go through the door.")
    print("2). Just go through the door.")
    
    #convert player's input to lower case
    treasure_answer = input(">")

    #loop function
    if treasure_answer == "2":
        print("Congratulations! You Won!!!")
        lets_play_again()
    else:
        print("You showed greediness. \nGame Over")
        lets_play_again()



#monster room
def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping. \nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")

    #convert player's input to lower case
    monster_answer = input(">")

    #loop function
    if monster_answer == "1":
        treasure_room()
    else:
        game_over(2)



#snake room
def snake_room():
    print("\nThere is a snake here.")
    print("Behind the Snake is another door.")
    print("The snake is having eggs!")
    print("What would you do?   (1 or 2)")
    print("1). Take the eggs.")
    print("2). Taunt the snake.")

    #convert player's input to lower case
    snake_answer = input(">")

    #loop function
    if snake_answer == "2":
        treasure_room()
    else:
        game_over(1)


   
#function to start
def start():
    print("You are standing in a dark room.")
    print("There is a door to your left and to your right, which one do you take?   (l or r)")
    
    #convert player's input to lower case
    answer = input(">").lower()

    #loop function
    if answer == "l":
        snake_room()
    else:
        monster_room()

#start the game
start()


###     CODE ENDS   ###