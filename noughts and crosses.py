#modules

import random
import sys

#global variables
boxes = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

#board
def convert_numb_to_text(numb):
    if (numb == 0):
        return("_")
    if (numb == 1):
        return("X")
    if (numb == 2):
        return("o")

def print_board(boxes):
    print_noughts_and_crosses()

    print('|'+convert_numb_to_text(boxes[0][0])+'|'+convert_numb_to_text(boxes[0][1])+'|'+convert_numb_to_text(boxes[0][2])+'|')
    print('|'+convert_numb_to_text(boxes[1][0])+'|'+convert_numb_to_text(boxes[1][1])+'|'+convert_numb_to_text(boxes[1][2])+'|')
    print('|'+convert_numb_to_text(boxes[2][0])+'|'+convert_numb_to_text(boxes[2][1])+'|'+convert_numb_to_text(boxes[2][2])+'|')

#check for victory

def check_for_victory(boxes):
    #selects in order the possible squares
    for i in range(0, 2):
        for n in range(0, 2):
            #looks to see if blank
            if boxes[i][n] == 0:
                continue
            #horizontal
            if boxes[i][0] == boxes[i][1] == boxes [i][2]:
                return boxes[i][n]
            #vertical
            if (boxes[0][n]) == (boxes[1][n]) == (boxes[2][n]):
                return boxes[i][n]
        #diaginal
        if (boxes[0][0]) == (boxes[1][1]) == (boxes[2][2]):
            return boxes[1][1]
        if (boxes[2][0]) == (boxes[1][1]) == (boxes[0][2]):
            return boxes[1][1]
    return False

#player move input
def player_move_input():
    player_move = input(print("to make your move enter a co-ordinate starting from top right: \n "))
    if player_move != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        player_move_input()
    else:
        return(player_move)

#determine who start first
def who_start_first():
    who_starts = random.randint(1,2)
    if who_starts == 1:
        return("player_1")

    else:
        return("The computer")


#print noughts and crosses
def print_noughts_and_crosses():
    for i in range (0,30):
        print("\n")
    print('  _   _                   _     _                         _')
    print('| \ | |                 | |   | |                       | |')
    print('|  \| | ___  _   _  __ _| |__ | |_ ___    __ _ _ __   __| |   ___ _ __ ___  ___ ___  ___ ___')
    print("| . ` |/ _ \| | | |/ _` | '_ \| __/ __|  / _` | '_ \ / _` |  / __| '__/ _ \/ __/ __|/ _ / __|")
    print("| |\  | (_) | |_| | (_| | | | | |_\__ \ | (_| | | | | (_| | | (__| | | (_) \__ \__ |  __\__ \ ")
    print("|_| \_|\___/ \__,_|\__, |_| |_|\__|___/  \__,_|_| |_|\__,_|  \___|_|  \___/|___|___/\___|___/")
    print('                    __/ | ')
    print('                    |___/')

#computer

#main
print_noughts_and_crosses()
who_start_first = who_start_first()
print(who_start_first + "starts first")

if who_start_first == ("player 1"):
    player_move_input()
if who_start_first == ("The computer"):
    #computer
    print("computer")

while check_for_victory(boxes) == False:




