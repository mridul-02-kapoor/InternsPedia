### INTERNSPEDIA PYTHON INTERN ###  ### SEPTEMBER 2022- OCTOBER 2022 ###
### MRIDUL KAPOOR ####      ### mridul.kapoor2002@gmail.com ###
### PYTHON PROJECT 2 ###    ### TEXT BASED ADVENTURE ###

print("\n             ###       DEVBRATHA BIRTH     ###         \n")


print("\nHELLO! WELCOME TO THIS TEXT BASED GAME")
print("\nThis game is based upon Indian Mythology, having background in the Mahabharat Era. \nYou're supposed to get the explanation why the queen was doing all of this, which you'll get at the end, when it was supposed to happen. You have to reach to the end of the incidence, which is possible only when you'll answer correctly according to the real story.")
print("\nYou are required to answer only in ''YES'' or ''NO'' format, other formats are not accepted")

### answers should be from below list only ###
ans_yes= ["YES", "Yes","yes","Y", "y"]
ans_no= ["NO", "No","no","N", "n"]

### story starts from here ###
print("\nSTORY")
print("\nYou're King Shantanu, the Great Warrior King of Hastinapur Kingdom. \nYou are wandering at a river bank and come across a beautiful maiden woman, arising from the river and moving towards the river bank. You're dumbstruck by her beauty and get the feeling of love at first sight. You desparately want to marry her.")

### First Question ###
print("\nSo would you ask her for marriage?")

###answer required from user ###
ans1=input("yes or no?\n")

### main code containing loops of story ###
if ans1 in ans_yes:
    print("\nThe woman is surprised and she accepted your marriage proposal. But she laid some conditions for same: \nFirstly, you can never ask who's she and where she's from. \nSecondly, you cannot ask any questions or any explanations for her actions, be it of any kind")
    print("If in any case the any of the conditions are broken, she'll leave at once")
    print("\nNow, Would you like to marry her even now?")

    ans2 = input("yes or no?\n")
    if ans2 in ans_yes:
        print("\nYou both got married and spent beautiful time together. \nAfter a year, queen is expecting a child and one day, she's in labor and she gave birth to a son. King rushes to the labor room and is surprised to see that the queen picked up the son in a shawl and is moving out of the room." )
        print("\nWould you like to ask queen where she's going with your son?")

        ans3= input("yes or no?\n")
        if ans3 in ans_no:
            print("\nYou are following her and see her going to the river bank where you first met. \nYou're astonished to see that see the queen is drowning your child")
            print("\nDo you want to shout and stop your queen to do this?")

            ans4= input("yes or no?\n")
            if ans4 in ans_no:
                print("\nQueen drowned your baby and you couldn't do anything.")
                print("\nAfter a year, you almost forgot this trauma and queen is again expecting a baby")
                print("This time as well, queen took the baby and is about to drown the baby again into the river.")
                print("\nDo you want to shout and stop your queen and ask her not to do this?")

                ans5 = input("yes or no?\n")
                if ans5 in ans_no:
                    print("\nQueen again drowned your baby and you couldn't do anything.")
                    print("\nYear after a year, this cycle continues. You almost forget about past trauma and queen is expecting a baby, queen takes the baby and drown the baby into the river.")
                    print("This occurs 7 times and everytime, you couldn't do anything because of the promises you made to marry the queen")

                    print("\nThis is the 8th time and again queen is trying to drown your baby")
                    print("\nDo you want to stop her?")

                    ans6 = input("yes or no?\n")
                    if ans6 in ans_yes:
                        print("\nQueen stopped at once. You yelled at her, asking her why she was doing all this.")
                        print("\nQueen explained: \nShe's Ganga,River Goddess and all your 8 sons, including your this son, are the human incarnation of 8 Vasus of heaven.")
                        print("The story is that once all 8 Vasus visited Rishi Vashisth's Ashram. They were provoked by their wife and they stole Rishi Vashisth's Cow- Nandini")
                        print("Rishi Vashishth got infurated and cursed the Vasus that they'll suffer just like humans do-they have to go through all the human sufferings, birth and death")
                        print("Vasus got scared and asked for forgiveness. But the 8th Vasu, Prabhasha, who was mainly responsible for stealing the cow, stood defined.")
                        print("Though Rishi Vashishth calmed down, but the curse couldnt be taken back. So he told them, though you'll born as humans but you all will be short lived, except the 8th vasu,Prabhasa, who'll live a long life and will face every human emotion.")
                        print("She was assigned the task of releiving the cursed Vasus and the 7 sons were the 7 Vasus; 8th son which was saved was the 8th Vasu-Prabhasa. Now he'll live a long life")
                        print("Ganga went away and she even took the 8th son, and promising that one day she'll reappear and handover the son, making him a great warrior and very learned person, to the king. \nThereafter few yew years King Shantanu got his son.")
                        print("\nThis story was the Birth Of Bhishma, who was named as Devbhrata, and was later named as Bhishma, due to '' Bhishm'' nature")

                    else:
                        print("This isnt supposed to happen in the real story. \nTRY AGAIN")
                else:
                    print("This isnt supposed to happen in the real story. \nTRY AGAIN")
            else:
                print("This isnt supposed to happen in the real story. \nTRY AGAIN")
        else:
            print("This isnt supposed to happen in the real story. \nTRY AGAIN")
    else:
        print("This isnt supposed to happen in the real story. \nTRY AGAIN")
else:
    print("This isnt supposed to happen in the real story. \nTRY AGAIN")