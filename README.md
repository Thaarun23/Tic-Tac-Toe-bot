# Tic-Tac-Toe-bot
Tic Tac Toe robot using a Mycobot 280M5

**1.	INTRODUCTION** 

A Cobot 280M5 is used as the actuator for the game of tic tac toe using opencv and pymycobot as package installs. The program utilized an engine designed for two robots to play tic tac toe , converting one of them to human and making the Bot control the Cobot as a way to visualize the tic tac toe game in real life by placing blocks. The project uses a camera to recognize the color blue as O which is designated for the player and the X for the robot. the robot uses the color red to represent X but any color can be used as the X isn’t dependent on the robot. the program has a grid drawn on the video so as to show the player where to place the blocks and the correct way to place it so the camera detects the color.

**2.	METHOD** 

2.1 Tic Tac Toe engine
The tic tac toe engine uses a program called onelayerbot to specify how the robot should play. Due to the nature of the game , tic tac toe can be made so that the robot always wins or ties with the player, to give some leeway to the human player the robot only places blocks it knows it can win with, the robot, if it see no winning move will immediately select a random place to place the block instead of placing a block to block the players winning move. The human player on the other hand uses blue blocks to place on the grid , these blue blocks represent O. the grids are all numbered and when placed on the grid, the game prints O in that place. This is basically how the tic tac toe engine works , however this program can be used to make the bot completely unwinnable.


2.2 OpenCV
OpenCV is used to do operations on the video taken by the camera , there are 3 different frames generated so as to clean the inputs more . the camera is positioned above the playable environment and is inverted causing all the grids to be upside down, however the game is played purely on the board and the visual grid represented on the video is a reference to keep the block in the right place. On the frame displayed to the person , there are 9 grids drawn on the program with each individual grid having its center point marked, this center point denotes the place at which the cube must at least be shown, the robot then utilizes this information to know which grid has been occupied and which grid has not.


![image](https://github.com/user-attachments/assets/6bb6dba7-abb8-4aee-bfd5-6648fa0e7ef4) 


Fig 2.1 Grid System in tic tac toe


![image](https://github.com/user-attachments/assets/9c6d766e-a0ee-4c6b-8a78-11bf65f67f5c)

Fig 2.2 Blue Color mask , thresholded 

2.3 Cobot controls

the Cobot is controlled using the pymycobot package , a suction pump is attached for the pneumatic gripper so that the blocks are picked up easily without much need for accuracy. the robot is assigned the color red and the X in the tic tac toe engine. The function for suction pumps is also added into the code for ease of use. The cobot is then dragged along each of the grids of to set the coordinates of the points in the variables grid_coordinates numbered 1 to 9. A home position , a pick position and a two coordinates indicating the picking and placing of the X or red block is assigned and a function Gridmove running between them is written in the program. The robot is then made to run through these positions as a test since the cobot sometimes would not be able to reach the point.


2.4 Cobot and Engine Integration

The code consists of a board object which generates the grid which is to be played on and 2 players assigned to X or O. the player turns and the win checking condition are placed in an if else statement that switches between the player turns if there is no winner on that turn, the entire tic tac toe playing program is placed in a for loop that loops 9 times . using opencv the camera function is placed inside the if else statement at the else part where the camera waits for the user input to detect the blocks existing in one of the grids, once a block is recognized the user presses O to confirm their move and the board updates the move in the grid, the board then uses this information to make the X robot decide its next move, the robot also disables the use of that grid to prevent it from detecting that grid again. On the X robots turn the program simply makes a choice and according to the choice arrays values the robot selects which set of blocks to run and runs the code block that places the blocks on the playable area after which the code updates with the move you have selected the, robot technically checks if there are any winning moves before deciding to make a choice. Once the robot or the player makes a winning move the robot or the player wins and the code is stopped. 
