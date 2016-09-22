## FILENAME: project2Chanlatte.py
## AUTHOR: Ryan Chanlatte
## LAST MODIFIED: 06/07/2016 @ 3:22 P.M.
##
## DESCRIPTION: Create a game of rock, paper, scissors. Include both one-player
##              and two-player.
##
##              Program should include a Main Menu:
##                  1.) See the Rules
##                  2.) Play against the computer
##                  3.) Play a two-player game
##                  4.) Quit
##
##              Weapon Menu for both one-player and two-player game to choose:
##                  1.) Rock
##                  2.) Paper
##                  3.) Scissors
##                  4.) Return to Main Menu
##
##              * The one-player game should include a randomly generated
##                choice between (1-3) by the computer.
##
##              * The two-player game should calculate and display scores
##                for the two-players each time they play a game.
##
##              * The user(s) should be allowed to play as many times as
##                he/she wishes until a choice is made to quit.
##
##              Input Validation:
##
##                  * The user must choose 1 - 4 from the game menu.
##                  * The user must choose 1 - 4 from the weapon menu.
##
###################################################################################

import sys
import time
import random
from getpass import getpass

###################################################################################


"""

TODO: FIX THE INPUT AND MAKE SURE THE PLAYER ONE OR TWO CANNOT GO PAST
      UNLESS THEIR INPUT IS ACCEPTABLE

"""

def Game_Loop():
    
    userAns = ""
    mainMenu_txt = "-----Main Menu-----"
    mainMenu_options = "\n1.) See the Rules\n2.) Play against the computer\n3.) Play a two-player game\n4.) Clear Screen\n5.) Quit\n"

    while True:

        print("---------------------------------------------------------------"
              + "-----------------\n")
        print("{:^80}".format(mainMenu_txt))
        print(mainMenu_options)
        print("---------------------------------------------------------------"
              + "-----------------\n")

        userAns = input("What is your selection? ")
        userAns = userAns.lower()

        if (userAns == "1"):
            Rules()
        elif (userAns == "2"):
            Single_Player(0, 0, 0)
        elif (userAns == "3"):
            Multiplayer()
        elif (userAns == "4" or userAns == "clear" or userAns == "clear screen"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        elif (userAns == "5" or userAns == "quit" or userAns == "exit"):
            print("\n\nExitting the game...\n\n")
            time.sleep(1.0)
            sys.exit()
        else:
            print("Sorry, I couldn't understand that (use only number 1-5).\n")

###################################################################################

def Rules():

    rulesMenu_txt = "Here are the rules to the game:"

    print("\n")
    print("{:^80}".format(rulesMenu_txt))
    
    # explain the game's mechanics to the player
    print("\nMuch like traditional \"Rock, Paper, Scissors\", you must "
          + "best your opponent\nduring a battle of wits! In order to "
          + "do so, you must select the correct\nweapon combination:\n")
    print("Paper Covers Rock")
    print("Rock Smashes Scissors")
    print("Scissors Cut Paper")

    # pause before returning to the Main Menu
    userAns = input("\n\nPress \"Enter\" to return to the main menu...")
    print("Returning to the main menu...\n")
    time.sleep(1.0)
    Game_Loop()

###################################################################################

def Main_Game(playerOneChoice, playerTwoChoice):

    # so, in the form of numeric values, we shall evaluate the win condition
    Move_LIST = ["NULL", "Rock", "Paper", "Scissors"]
    playerOne_Move = Move_LIST[playerOneChoice]
    playerTwo_Move = "NULL"
    isComputer = False

    # '4' will be my value to initialize the computer's moveset, otherwise,
    # I'll just throw an actual value to the function, bypassing this with
    # the else-statement
    if (playerTwoChoice == 4):
        playerTwo_Move = Move_LIST[random.randint(1, 3)]
        isComputer = True
    else:
        playerTwo_Move = Move_LIST[playerTwoChoice]

    # here are the main game conditionals
    if (isComputer == True):

        # basic code to create a concatonated computer names
        # I think it provides a bit more personality to the game
        computerName_LIST = ["Noah", "Emma", "Mason", "Sherry", "James", "Isabella", "Benjamin", "Mia", "Jamal", "Aaliyah", "Akio", "Sakiya"]
        computerName = "Computer " + computerName_LIST[random.randint(0, 11)]

        # intro your opponent, give good luck
        print("\nYou will be facing " + computerName + "...")
        print("May the best player win!")

        if (playerOne_Move == playerTwo_Move):

            # make it seem like the computer is thinking
            time.sleep(0.5)
            print("\n" + computerName + " is coming up with an answer.", end = "")
            time.sleep(0.65)
            print(".", end = "")
            time.sleep(0.75)
            print(".", end = "")
            time.sleep(0.85)
            print(".", end = "")
            time.sleep(1.0)
            print("\n")

            print("Player 1 picked:", playerOne_Move, "\n" + computerName + " picked:", playerTwo_Move)
            return 0

        elif (playerOne_Move == "Rock" and playerTwo_Move == "Scissors" or
              playerOne_Move == "Paper" and playerTwo_Move == "Rock" or
              playerOne_Move == "Scissors" and playerTwo_Move == "Paper"):

            time.sleep(0.5)
            print("\n" + computerName + " is coming up with an answer.", end = "")
            time.sleep(0.65)
            print(".", end = "")
            time.sleep(0.75)
            print(".", end = "")
            time.sleep(0.85)
            print(".", end = "")
            time.sleep(1.0)
            print("\n")

            print("Player 1 picked:", playerOne_Move, "\n" + computerName + " picked:", playerTwo_Move)
            return 1

        elif (playerTwo_Move == "Rock" and playerOne_Move == "Scissors" or
              playerTwo_Move == "Paper" and playerOne_Move == "Rock" or
              playerTwo_Move == "Scissors" and playerOne_Move == "Paper"):

            time.sleep(0.5)
            print("\n" + computerName + " is coming up with an answer.", end = "")
            time.sleep(0.65)
            print(".", end = "")
            time.sleep(0.75)
            print(".", end = "")
            time.sleep(0.85)
            print(".", end = "")
            time.sleep(1.0)
            print("\n")

            print("Player 1 picked:", playerOne_Move, "\n" + computerName + " picked:", playerTwo_Move)
            return 2

    elif (playerOne_Move == playerTwo_Move):
        print("Player 1 picked:", playerOne_Move, "\nPlayer 2 picked:", playerTwo_Move)
        return 0

    elif (playerOne_Move == "Rock" and playerTwo_Move == "Scissors" or
        playerOne_Move == "Paper" and playerTwo_Move == "Rock" or
        playerOne_Move == "Scissors" and playerTwo_Move == "Paper"):
        print("Player 1 picked:", playerOne_Move, "\nPlayer 2 picked:", playerTwo_Move)
        return 1

    elif (playerTwo_Move == "Rock" and playerOne_Move == "Scissors" or
        playerTwo_Move == "Paper" and playerOne_Move == "Rock" or
        playerTwo_Move == "Scissors" and playerOne_Move == "Paper"):
        print("Player 1 picked:", playerOne_Move, "\nPlayer 2 picked:", playerTwo_Move)
        return 2

###################################################################################

def Single_Player(PlayerScore, ComputerScore, DrawScore):

    singleMenu_txt = "Welcome to the single-player game!\n"
    PlayerScore = 0
    ComputerScore = 0
    Draws = 0

    # intro the function
    print("\n")
    print("---------------------------------------------------------------"
          + "-----------------\n")
    print("{:^80}".format(singleMenu_txt))
    print("---------------------------------------------------------------"
          + "-----------------\n")

    while True:

        # some variables
        userAns = ""

        # gives the computer some words to say after a win/loss/draw
        # provides more personality
        computerWinAns_LIST = ["\"Yes! I won!","Nice!\"","\"This game is easy!\"","\"Haha, I'm the game master!\"","\"I'm the best!\""]
        computerLossAns_LIST = ["\"Darn it!\"","\"This game sucks...\"","\"How did you beat me?!\"","\"This isn't fair...\"","\"Dang! No Way!\""]
        computerDrawAns_LIST = ["\"Huh, it's a draw.\"","\"A draw?!\"","\"No way! I thought for sure I had won.\"","\"It's a tie.\"","\"Deadlocked!\""]
        computerWin_Response = computerWinAns_LIST[random.randint(0,4)]
        computerLoss_Response = computerLossAns_LIST[random.randint(0,4)]
        computerDraw_Response = computerDrawAns_LIST[random.randint(0,4)]

        # this numeric value will determine who won
        # -1 = unitialized value, done in case I need to debug
        # 0 = draw
        # 1 = player one won
        # 2 = player two won
        whoWon = -1

        print("---------------------------------------------------------------"
              + "-----------------")

        # show what moves are possible
        print("\nMove choice:\n\n"
               + "1.) Rock\n"
               + "2.) Paper\n"
               + "3.) Scissors\n"
               + "4.) Return to Main menu\n")
        
        # make sure the user isn't trying to exit the game or input illegal
        # values
        try:
            userAns = input("What is your move? ")
        except ValueError:
            print("Please input a string.")

        userAns = userAns.lower()

        if (userAns == "1" or userAns == "2" or userAns == "3"):
            # converting so the function can take it as an argument
            userAns = int(userAns)
            # assign "who won" to the return value of the function
            whoWon = Main_Game(userAns, 4)
        elif (userAns == "4"):
            print("Exiting the single-player game...")
            time.sleep(1.0)
            Game_Loop()
        else:
            print("\nI'm sorry, I couldn't understand that...")

        # evaluating the win condition
        if (whoWon == 0):
            print("\nIT'S A DRAW!\n")
            print("The computer said: " + computerDraw_Response)
            Draws += 1
            print(input("\nPress \"Enter\" to get the scoreboard and to continue..."))
            print("The tally is:\n" + "---------------------------------------------"
                  + "\n|  Wins:", PlayerScore, "\tDraws:", Draws, "\tLosses:", ComputerScore,
                  "  |\n---------------------------------------------")
            
        elif (whoWon == 1):
            print("\nPLAYER ONE WON!\n")
            print("The computer groaned: " + computerLoss_Response)
            PlayerScore += 1
            print(input("\nPress \"Enter\" to get the scoreboard and to continue..."))
            print("The tally is:\n" + "---------------------------------------------"
                  + "\n|  Wins:", PlayerScore, "\tDraws:", Draws, "\tLosses:", ComputerScore,
                  "  |\n---------------------------------------------")

        elif (whoWon == 2):
            print("\nTHE COMPUTER WON!\n")
            print("The computer exclaimed: " + computerWin_Response)
            ComputerScore += 1
            print(input("\nPress \"Enter\" to get the scoreboard and to continue..."))
            print("The tally is:\n" + "---------------------------------------------"
                  + "\n|  Wins:", PlayerScore, "\tDraws:", Draws, "\tLosses:", ComputerScore,
                  "  |\n---------------------------------------------")

        if (whoWon > -1 or whoWon == 0):

            # small while-loop to keep iterating program
            while True:

                print("\nScreen too cluttered? Use \"clear\" to clear the screen.\nUse \"quit\" to exit the game.")
                userAns = input("\nWould you like to continue (yes)? Or would you like to return to the\nmain menu (no)? ")
                userAns = userAns.lower()

                if (userAns == "yes" or userAns == "y" ):
                    break
                elif (userAns == "no" or userAns == "n" ):
                    print("\nReturning to the main menu...\n")
                    time.sleep(1.5)
                    Game_Loop()
                elif ( userAns == "clear"):
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                elif (userAns == "quit"):
                    print("\nExiting the game...\n")
                    time.sleep(1.0)
                    sys.exit()
                else:
                    print("Invalid input. Either \"Yes\" or \"No\".")
                
###################################################################################

def Multiplayer():

    multipleMenu_txt = "Welcome to a two-player game!\n"
    PlayerOneScore = 0
    PlayerTwoScore = 0
    Draws = 0

    # intro the function
    print("\n")
    print("---------------------------------------------------------------"
          + "-----------------\n")
    print("{:^80}".format(multipleMenu_txt))
    print("---------------------------------------------------------------"
          + "-----------------\n")

    while True:
        
        PlayerOne = -1
        PlayerTwo = -1
        whoWon = -1

        while PlayerOne < 0 or PlayerOne > 4:
        
            print("---------------------------------------------------------------"
                  + "-----------------")

            print("\nMove choice:\n\n"
                   + "1.) Rock\n"
                   + "2.) Paper\n"
                   + "3.) Scissors\n"
                   + "4.) Return to Main menu\n")

            # when playing this with myself to test it, I realized the game wouldn't truly
            # work in the way it typically does. That is, you can see what the previous player
            # input before being handed the keyboard. This obviously gives the second player
            # an advantage. So, I've utilized the "getpass" module which hides the input, but
            # it will ONLY DO SO in the commandline and NOT in the typical IDLE GUI interface.
            # just something to keep in mind.
            try:
                PlayerOne = int(getpass("What is your move, Player one? "))
                if(PlayerOne == 4):
                    print("Exiting the multiplayer-player game...")
                    time.sleep(2.0)
                    Game_Loop()
                elif(PlayerOne > 4):
                    print("\n***ERROR*** Please input a value between 1 - 4.\n")
                    
            except ValueError:
                print("\n***ERROR*** Please input a value between 1 - 4.\n")

        while PlayerTwo < 0 or PlayerTwo > 4:

                print("\nMove choice:\n\n"
                       + "1.) Rock\n"
                       + "2.) Paper\n"
                       + "3.) Scissors\n"
                       + "4.) Return to Main menu\n")
                
                try:
                    PlayerTwo = int(getpass("What is your move, Player two? "))
                    if(PlayerTwo == 4):
                        print("Exiting the multiplayer-player game...")
                        time.sleep(2.0)
                        Game_Loop()
                    elif(PlayerTwo > 4):
                        print("\n***ERROR*** Please input a value between 1 - 4.\n")
                except ValueError:
                    print("\n***ERROR*** Please input a value between 1 - 4.\n")
                
        
        if (PlayerOne == 1 or PlayerOne == 2 or PlayerOne == 3):
            # assign "who won" to the return value of the function
            whoWon = Main_Game(PlayerOne, PlayerTwo)
        else:
            print("\nI'm sorry, I couldn't understand that...")

        # evaluating the win condition
        if (whoWon == 0):
            print("\nIT'S A DRAW!\n")
            Draws += 1
            print(input("\nPress \"Enter\" to get the scoreboard and to continue..."))
            print("The tally is:\n" + "---------------------------------------------------------"
                  + "\n|  Player One:", PlayerOneScore, "\t Draws:", Draws, "\tPlayer Two:", PlayerTwoScore,
                  "  |\n---------------------------------------------------------")
            
        elif (whoWon == 1):
            print("\nPLAYER ONE WON!\n")
            PlayerOneScore += 1
            print(input("\nPress \"Enter\" to get the scoreboard and to continue..."))
            print("The tally is:\n" + "---------------------------------------------------------"
                  + "\n|  Player One:", PlayerOneScore, "\t Draws:", Draws, "\tPlayer Two:", PlayerTwoScore,
                  "  |\n---------------------------------------------------------")

        elif (whoWon == 2):
            print("\nPLAYER TWO WON!\n")
            PlayerTwoScore += 1
            print(input("\nPress \"Enter\" to get the scoreboard and to continue..."))
            print("The tally is:\n" + "---------------------------------------------------------"
                  + "\n|  Player One:", PlayerOneScore, "\t Draws:", Draws, "\tPlayer Two:", PlayerTwoScore,
                  "  |\n---------------------------------------------------------")

        if (whoWon > -1 or whoWon == 0):
            # small while-loop to keep iterating program
            while True:

                print("\nScreen too cluttered? Use \"clear\" to clear the screen.\nUse \"quit\" to exit the game.")
                userAns = input("\nWould you like to continue (yes)? Or would you like to return to the\nmain menu (no)? ")
                userAns = userAns.lower()

                if (userAns == "yes" or userAns == "y" ):
                    break
                elif (userAns == "no" or userAns == "n" ):
                    print("\nReturning to the main menu...\n")
                    time.sleep(1.5)
                    Game_Loop()
                elif ( userAns == "clear"):
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                elif (userAns == "quit"):
                    print("\nExiting the game...\n")
                    time.sleep(1.0)
                    sys.exit()
                else:
                    print("Invalid input. Either \"Yes\" or \"No\".")
        


###################################################################################

def main():

    # intro the program
    print("\nWelcome to the ROCK, PAPER, SCISSORS GAME!!!\n")

    # call main game loop
    Game_Loop()

###################################################################################

main()
