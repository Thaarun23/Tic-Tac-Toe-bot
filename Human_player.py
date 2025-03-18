import random
import cv2
class HumanPlayer():
    def __init__(self, player):
        self.player = player

    def select_move(self, board,GridNum):

        if GridNum == 1:
            choice = [0,0]
        if GridNum == 2:
            choice = [0,1]
        if GridNum == 3:
            choice = [0,2]
        if GridNum == 4:
            choice = [1,0]
        if GridNum == 5:
            choice = [1,1]
        if GridNum == 6:
            choice = [1,2]
        if GridNum == 7:
            choice = [2,0]
        if GridNum == 8:
            choice = [2,1]
        if GridNum == 9:
            choice = [2,2]

        return choice
