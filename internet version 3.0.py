# tic tac toe game --- player vs player
import sys


class Game:
    def __init__(self):

        self.board = [[0, 0, 0] for i in range(0, 3)]
        self.coord = [0, 0]
        self.player_one = True
        self.player_two = False
        self.check_index = 0
        self.turn = 0
        print(" --- There is a co-ordinate system to place an O or X ---")
        print(" ----- enter co-ordinates like this: 1,2 or 2,1 etc -----\n")
        self.print_board()

    def update(self):

        if (self.turn == 9):
            print("No one has won!")
            sys.exit()
        elif self.player_one:
            print("Enter coordinates to place X: ")
        elif not self.player_one:
            print("Enter coordinates to place O: ")

        while True:
            try:
                user_input = input()
                self.coord[0], self.coord[1] = user_input.split(',')
                self.check_index = self.board[int(self.coord[0]) - 1][int(self.coord[1]) - 1]
            except ValueError:
                print("You've entered the co-ordinates wrong!")
                continue
            except IndexError:
                print("You've entered co-ordinates that are out of range!")
            else:
                break

        self.coord[0], self.coord[1] = int(self.coord[0]) - 1, int(self.coord[1]) - 1

        # switches player based on user input
        if (self.player_one and self.board[self.coord[0]][self.coord[1]] == 0):
            self.board[self.coord[0]][self.coord[1]] = 1
            self.player_one = False
            self.player_two = True
            self.print_board()
            self.turn += 1
        elif (self.player_two and self.board[self.coord[0]][self.coord[1]] == 0):
            self.board[self.coord[0]][self.coord[1]] = 2
            self.player_one = True
            self.player_two = False
            self.print_board()
            self.turn += 1
        else:
            print("A value is already in place there!")

        # checks if an end goal is achieved and decides winner
        if self.check(1):
            print("X WINS")
            sys.exit()
        elif self.check(2):
            print("O WINS")
            sys.exit()

    def print_board(self):

        # prints board
        for y in range(0, 3):
            for x in range(0, 3):
                letter_to_print = self.board[x][y]
                if (letter_to_print == 1):
                    print(" X ", end='')
                elif (letter_to_print == 2):
                    print(" O ", end='')
                else:
                    print(" - ", end='')
            print("\n")

    def check(self, num):

        # check horizontal
        for i in range(0, 3):
            if (self.board[0][i] == num and self.board[1][i] == num and self.board[2][i] == num):
                return True

        # check vertical
        for i in range(0, 3):
            if (self.board[i][0] == num and self.board[i][1] == num and self.board[i][2] == num):
                return True

        # check diagonal
        if (self.board[0][0] == num and self.board[1][1] == num and self.board[2][2] == num):
            return True
        if (self.board[2][0] == num and self.board[1][1] == num and self.board[0][2] == num):
            return True


if __name__ == "__main__":
    main = Game()
    while True:
        main.update()