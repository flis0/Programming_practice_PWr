import numpy as np
import random as rng
import os
import time
import keyboard

class LifeBoard:
    def __init__(self, speed=1, size=(15,15), alive_marker='#', dead_marker='.'):
        self.speed = speed
        self.size = size
        self.alive_marker = alive_marker
        self.dead_marker = dead_marker
        self.__board = np.random.rand(*size) > 0.5

    def run(self):
        while True:
            os.system('cls')
            self.display()
            self.tick()
            time.sleep(self.speed)
            
    def tick(self):
        new_board = np.zeros_like(self.__board)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                slice = self.__board[np.clip(i-1, 0, self.size[0]):np.clip(i+2, 0, self.size[0]), np.clip(j-1, 0, self.size[1]):np.clip(j+2, 0, self.size[1])]
                alive_nb_count = np.sum(slice) - self.__board[i,j]
                
                if self.__board[i,j]:
                    new_board[i,j] = alive_nb_count == 2 or alive_nb_count == 3
                else:
                    new_board[i,j] = alive_nb_count == 3

        self.__board = new_board

    def display(self):
        for row in self.__board:
            print(' '.join([self.alive_marker if cell else self.dead_marker for cell in row]))
    

if __name__ == "__main__":
    speed = abs(float(input("Time of iteration [s]: ")))
    nrows = abs(int(input("Number of rows: ")))
    ncols = abs(int(input("Number of columns: ")))
    alive_m = input("Alive marker: ")
    dead_m = input("Dead marker: ")
    LF = LifeBoard(speed=speed, size=(nrows, ncols), alive_marker=alive_m, dead_marker=dead_m)
    LF.run()
