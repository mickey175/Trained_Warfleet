from random import randint
from termcolor import cprint

class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.enemy_board = []
        self.agent_board = []

        self.reset_board(board_size)

    def reset_board(self, board_size):
        for x in range(board_size):
            self.enemy_board.append([" "] * board_size)
            self.agent_board.append([" "] * board_size)

    def draw_board(self):
        # Clear Screen: screen wird nur verschoben aber reicht auch zur übersicht
        print('\n' * 40)
        print("Gegnerisches Spielfeld")
        x = 0
        print("  "+" 0 1 2 3 4 5 6 7 8 9") # Obere leiste
        for row in self.enemy_board:
            string = str(x)+"  "+" ".join(row)
            cprint('\x1b[2;31;44m'+string, 'red', 'on_blue')
            x += 1
        print("Dein Spielfeld")
        x = 0
        print("  "+" 0 1 2 3 4 5 6 7 8 9") # Obere leiste
        for row in self.agent_board:
            string = str(x) + "  " + " ".join(row)
            cprint('\x1b[3;30;44m'+string, 'white', 'on_blue')
            x += 1

    def place_enemy_ship(self, orientation, start, end, column):

        # tauschen der zahlen bei falscher eingabe
        if start >= end:
            temp = end
            end = start
            start = temp

        if orientation == 0:
            for row in range(start, end + 1):
                self.enemy_board[column][row] = "x"

        if orientation == 1:
            for row in range(start, end + 1):
                self.enemy_board[row][column] = "x"

    def place_agent_ship(self):
        orientation = int(input("Waagrecht(0) oder Senkrecht(1)? : "))
        # minus 1 weil der array immer bei 0 anfängt
        column = int(input("Welche Reihe/Spalte: "))
        start = int(input("Anfang Shiff: "))
        end = int(input("Ende Shiff: "))

        # tauschen der zahlen bei falscher eingabe
        if start >= end:
            temp = end
            end = start
            start = temp

        #waagrecht
        if orientation == 0:
            for row in range(start, end + 1):
                self.agent_board[column][row] = "x"

        #senkrecht
        if orientation == 1:
            for row in range(start, end + 1):
                self.agent_board[row][column] = "x"

    def place_hit(self, x, y, selected_board):
        selected_board[y][x] = "O"

    def check_sunken_ships(self, shiplist):
        if shiplist is []:
            pass

    def check_hit(self, action_space):
        pass

    def get_enemy_board(self):
        return self.enemy_board

    def get_agent_board(self):
        return self.agent_board

