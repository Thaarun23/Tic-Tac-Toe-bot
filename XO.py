import cv2
import numpy as np
import cv2 as cv
from ttt.board import Board
from pymycobot import MyCobot
from ttt.player import Player
import time

from ttt.one_layer_bot import OneLayerBot
from ttt.Human_player import  HumanPlayer

def pump_on():
    mc.set_basic_output(5, 0)
    time.sleep(0.05)

# Stop suction pump
def pump_off():
    mc.set_basic_output(5, 1)
    time.sleep(0.05)
    mc.set_basic_output(2, 0)
    time.sleep(1)
    mc.set_basic_output(2, 1)
    time.sleep(0.05)
def Detect_O():

    if bluefil[cgrid1[1], cgrid1[0]] != 0 and Cgrid_empty[0]:
        GridNum = 1
    if bluefil[cgrid2[1], cgrid2[0]] != 0 and Cgrid_empty[1]:
        GridNum = 2
    if bluefil[cgrid3[1], cgrid3[0]] != 0 and Cgrid_empty[2]:
        GridNum = 3
    if bluefil[cgrid4[1], cgrid4[0]] != 0 and Cgrid_empty[3]:
        GridNum = 4
    if bluefil[cgrid5[1], cgrid5[0]] != 0 and Cgrid_empty[4]:
        GridNum = 5
    if bluefil[cgrid6[1], cgrid6[0]] != 0 and Cgrid_empty[5]:
        GridNum = 6
    if bluefil[cgrid7[1], cgrid7[0]] != 0 and Cgrid_empty[6]:
        GridNum = 7
    if bluefil[cgrid8[1], cgrid8[0]] != 0 and Cgrid_empty[7]:
        GridNum = 8
    if bluefil[cgrid9[1], cgrid9[0]] != 0 and Cgrid_empty[8]:
        GridNum = 9

    return GridNum

def Gridmove(choice):
    #grid1
    if choice[0] == 0 and choice[1] == 0:
        mc.send_coords(pick_pos ,30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos,30)
        time.sleep(3)
        mc.send_coords(pick_x_pos,10)
        time.sleep(3)
        print("pump_on")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos,30)
        time.sleep(3)
        mc.send_coords(grid1coord,20)
        time.sleep(3)
        print("pump off")
        time.sleep(1)
        mc.send_coords(pick_pos ,20)
        time.sleep(2)
        mc.send_coords(home_pos,20)
    #grid2
    if choice[0] == 0 and choice[1] == 1:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid2coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)
    #grid3
    if choice[0] == 0 and choice[1] == 2:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid3coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)
    #grid4
    if choice[0] == 1 and choice[1] == 0:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid4coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)
    #grid5

    if choice[0] == 1 and choice[1] == 1:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid5coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)
    #grid6
    if choice[0] == 1 and choice[1] == 2:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid6coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)
    #grid7
    if choice[0] == 2 and choice[1] == 0:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid7coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)
    #grid8
    if choice[0] == 2 and choice[1] == 1:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid8coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)
    #grid9
    if choice[0] == 2 and choice[1] == 2:
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_x_pos, 10)
        time.sleep(3)
        print("pump_on()")
        time.sleep(1)
        mc.send_coords(pick_xab_pos, 30)
        time.sleep(3)
        mc.send_coords(pick_pos, 30)
        time.sleep(3)
        mc.send_coords(grid9coord, 20)
        time.sleep(3)
        print("pump_off()")
        time.sleep(1)
        mc.send_coords(pick_pos, 20)
        time.sleep(2)
        mc.send_coords(home_pos, 20)




print_game = True
cap = cv.VideoCapture(0)
mc = MyCobot("COM11" , 115200)
red_lower = np.array([0,175,20])
red_upper = np.array([10, 255,255])
red_lower2 = np.array([170,175,20])
red_upper2 = np.array([180,255,255])
grid_bool = False

xbot = OneLayerBot(Player.x)
obot = HumanPlayer(Player.o)

grid1 = [0,0]
grid2 = [0,1]
grid3 = [0,2]
grid4 = [1,0]
grid5 = [1,1]
grid6 = [1,2]
grid7 = [2,0]
grid8 = [2,1]
grid9 = [2,2]

grid1coord=[232.8, 57.4, 102.6, 177.58, 0.08, -48.15]
grid2coord=[236.1, -4.6, 111.8, 173.4, -3.16, -64.9]
grid3coord=[224.3, -55.3, 119.0, 179.83, -7.99, -76.97]
grid4coord=[179.3, 57.6, 107.8, 177.88, 1.62, -32.39]
grid5coord=[181.4, -0.9, 102.7, 175.26, -2.35, -48.12]
grid6coord=[194.0, -60.1, 115.0, 173.45, -6.13, -69.3]
grid7coord=[134.9, 55.4, 108.4, 174.76, 5.85, -27.05]
grid8coord=[137.3, -13.1, 107.4, 176.18, 5.53, -62.87]
grid9coord=[135.5, -49.7, 105.5, 167.0, -9.61, -67.98]

home_pos = [65.3, -59.9, 252.4, -176.27, 0.81, -74.45]
pick_pos = [184.0, -32.0, 243.3, -178.13, 1.11, -67.81]

pick_x_pos = [176.6, -171.0, 110.9, 170.99, -6.77, -101.84]
pick_xab_pos = [156.9, -162.0, 209.3, -173.65, -6.72, -101.32]


cgrid1 =[446,349]
cgrid2 =[324,348]
cgrid3 =[186,354]
cgrid4 =[452,227]
cgrid5 = [321,225]
cgrid6 =[179,224]
cgrid7 =[440,114]
cgrid8 =[334, 113]
cgrid9 =[188,112]


Cgrid1_empty = True
Cgrid2_empty = True
Cgrid3_empty = True
Cgrid4_empty = True
Cgrid4_empty = True
Cgrid5_empty = True
Cgrid6_empty = True
Cgrid7_empty = True
Cgrid8_empty = True
Cgrid9_empty = True

Cgrid_empty = [True , True , True , True, True, True ,True ,True ,True]
lower_blue = np.array([80, 150, 0])
upper_blue = np.array([140, 255, 255])

mc.send_coords(home_pos,20)

board = Board()
current_turn = Player.o
winner = None

for i in range(9):

        choice = []
        if (current_turn == xbot.player):

            choice = xbot.select_move(board)
            Gridmove(choice)
        else:
            if not cap.isOpened():
                print("Cannot open camera")
                exit()
            while True:
                # Capture frame-by-frame
                ret, frame = cap.read()
                # if frame is read correctly ret is True
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                # Our operations on the frame come here
                c2h = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                maskb = cv2.inRange(c2h, lower_blue, upper_blue)
                bluefili = cv2.bitwise_and(frame, frame, mask=maskb)
                Grayfil = cv2.cvtColor(bluefili ,cv.COLOR_BGR2GRAY)
                bluefil = cv2.inRange(Grayfil ,100 ,255)




                cv.imshow('Grayscale', Grayfil)
                cv.imshow('bluefil', bluefil)






                #Grid1
                cv.rectangle(frame ,(391,303),(500,409),(255,0,255),2 )
                cv.circle(bluefil, [446,349], 5, (255,0 ,0), 1)
                #Grid2
                cv.rectangle(frame, (264,312),(360,410),(255,0,0),2)
                cv.circle(frame, cgrid2, 2, (255, 0, 0), 1)
                #Grid3
                cv.rectangle(frame, (138, 303), (238, 412), (255, 0, 0), 2)
                cv.circle(frame, cgrid3, 2, (255, 0, 0), 1)
                #Grid4
                cv.rectangle(frame, (390,183), (496, 284), (255, 0, 0), 2)
                cv.circle(frame, cgrid4, 2, (255, 0, 0), 1)
                #Grid5
                cv.rectangle(frame, (263, 185), (367, 280), (255, 0, 0), 2)
                cv.circle(frame, cgrid5, 2, (255, 0, 0), 1)
                #Grid6
                cv.rectangle(frame, (134, 185), (239, 278), (255, 0, 0), 2)
                cv.circle(frame, cgrid6, 2, (255, 0, 0), 1)
                #Grid7
                cv.rectangle(frame, (401, 44), (501, 144), (255, 0, 0), 2)
                cv.circle(frame, cgrid7, 2, (255, 0, 0), 1)
                #Grid8
                cv.rectangle(frame, (277, 43), (376, 152), (255, 0, 0), 2)
                cv.circle(frame, cgrid8, 2, (255, 0, 0), 1)
                #Grid9
                cv.rectangle(frame, (140, 46), (248, 162), (255, 0, 0), 2)
                cv.circle(frame, cgrid9, 2, (255, 0, 0), 1)
                cv.imshow('bluefil', bluefil)
                # Display the resulting frame
                cv.imshow('frame', frame)
                if cv.waitKey(1) == ord('o'):


                    GridNum2 = Detect_O()
                    Cgrid_empty[GridNum2-1] = False
                    choice = obot.select_move(board, GridNum2)

                    break
            # When everything done, release the capture



        board.make_move(choice[0], choice[1], current_turn)

        winner = board.has_winner()

        if print_game:
            board.print()
        if (winner != None):
            print ("Congrats " + str(winner))
            break
        elif (i == 8):
            print ("It's a tie!")
            break
        current_turn = current_turn.other



# When everything done, release the capture

cap.release()
cv.destroyAllWindows()