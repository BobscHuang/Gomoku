from tkinter import *
from time import *
import sys
myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background= "#b69b4c")
s.pack()

#Board Size
Board_Size = 15
Frame_Gap = 35
width = 800
height = 800

#Note: all "exit" does is terminate the while loop, so it dosen't really do much...
#      to begin another round you would need to restart the program.

def create_circle(x, y, radius, fill = "", outline = "black", width = 1):
    s.create_oval(x - radius, y - radius, x + radius, y + radius, fill = fill, outline = outline, width = width)

def Value_Check_int(Value):
    try:
        Value = int(Value)
    except ValueError:
        return "string"
    else:
        return "int"

def MouseClick(event):
    global Click_Cord
    X_click = event.x
    Y_click = event.y
    Click_Cord = Piece_Location(X_click, Y_click)
    print(Click_Cord)

s.bind("<Button-1>", MouseClick)

Click_Cord = [None, None]

def Piece_Location(X_click, Y_click):    
    X = None
    Y = None
    for i in range(len(Actual_CordX1)):
        
        if X_click > Actual_CordX1[i] and X_click < Actual_CordX2[i]:
            X = Game_CordX[i]

        if Y_click > Actual_CordY1[i] and Y_click < Actual_CordY2[i]:
            Y = Game_CordY[i]

    return X, Y

def Location_Validation():

    if X == None or Y == None:
        return False
        
    elif board[Y - 1][X - 1] == 0:
        return True

def Score_Board():
    if Winner == None:
        Turn_Text = s.create_text(width / 2, height - Frame_Gap + 15, text = "Turn = " + Turn, font = "Helvetica 25 bold", fill = Turn)
        return Turn_Text
    else:
        s.create_text(width / 2, height - Frame_Gap + 15, text = Winner.upper() + " WINS!", font = "Helvetica 25 bold", fill = Winner.lower())

def winCheck(Piece_Number, Piece_Colour, board):
    if rowCheck(Piece_Number, board) or rowCheck(Piece_Number, transpose(board)) or rowCheck(Piece_Number, transposeDiagonalInc(board)) or rowCheck(Piece_Number, transposeDiagonalDec(board)):
        Winner = Piece_Colour
        return Winner

def rowCheck(Piece_Number, board):
    for i in range(len(board)):
        if board[i].count(Piece_Number) >= 5:
            
            for z in range(len(board) - 3):
                Connection = 0

                for c in range(5):
                    if board[i][z + c] == Piece_Number:
                        Connection += 1

                    else:
                        break

                    if Connection == 5:
                        return True

def getDiagonalDec(loa, digNum):
    lst=[]
    if digNum <= len(loa) - 1:
        index = len(loa) - 1
        for i in range(digNum, -1, -1):
            lst.append(loa[i][index])
            index -= 1
        return lst
    else:
        index = (len(loa) * 2 - 2) - digNum
        for i in range(len(loa) - 1, digNum - len(loa), -1):
            lst.append(loa[i][index])
            index -= 1
        return lst


def transposeDiagonalDec(loa):
    lst = []
    for i in range(len(loa) * 2 - 1):
        lst.append(getDiagonalDec(loa, i))
    return lst

def getDiagonalInc(loa, digNum):
    lst=[]
    if digNum <= len(loa) - 1:
        index = 0
        for i in range(digNum, -1, -1):
            lst.append(loa[i][index])
            index += 1
        return lst
    else:
        index =  digNum - len(loa) + 1
        for i in range(len(loa) - 1, digNum - len(loa), -1):
            lst.append(loa[i][index])
            index += 1
        return lst


def transposeDiagonalInc(loa):
    lst = []
    for i in range(len(loa) * 2 - 1):
        lst.append(getDiagonalInc(loa, i))
    return lst

def transpose(loa):
    lst = []
    for i in range(len(loa)):
        lst.append(getCol(loa, i))
    return lst
    
def getCol(loa, colNum):
    lst = []
    for i in range(len(loa)):
        lst.append(loa[i][colNum])
    return lst

def Index2D_Cord(List, Find):
    for i, x in enumerate(List):
        if Find in x:
            Colour_CordX.append(i - 1)
            Colour_CordY.append(x.index(Find) - 1)

def Exit():
    global Winner
    Winner = "Exit"
    myInterface.destroy()
    
#Board
Board_Size = Board_Size - 1
Board_X1 = width / 10
Board_Y1 = height / 10
Board_GapX = (width - Board_X1 * 2) / Board_Size
Board_GapY = (height - Board_Y1 * 2) / Board_Size

#Chess Piece
Chess_Radius = (Board_GapX * (9 / 10)) / 2

#Turn
Turn_Num = 1
Turn = "white"
Winner = None

#Cord List
Black_Cord_PickedX = []
Black_Cord_PickedY = []
White_Cord_PickedX = []
White_Cord_PickedY = []

#Click Detection Cord
Game_CordX = []
Game_CordY = []
Actual_CordX1 = []
Actual_CordY1 = []
Actual_CordX2 = []
Actual_CordY2 = []

#2D Board List
board = []

#Buttons
B = Button(myInterface, text = "EXIT", font = "Helvetica 10 bold", command = Exit, bg = "gray", fg = "black")
B.pack()
B.place(x = width / 2 * 0.5, y = height - Frame_Gap * 1.6 + 15, height = Chess_Radius * 2, width = Chess_Radius * 4)

#2D list for gameboard
for i in range(Board_Size + 1):
    board.append([0] * (Board_Size + 1))
    
Unfilled = 0
Black_Piece = 1
White_Piece = 2

#Fills Empty List
for z in range(1, Board_Size + 2):
    
    for i in range(1, Board_Size + 2):
        Game_CordX.append(z)
        Game_CordY.append(i)
        Actual_CordX1.append((z - 1) * Board_GapX + Board_X1 - Chess_Radius)
        Actual_CordY1.append((i - 1) * Board_GapY + Board_Y1 - Chess_Radius)
        Actual_CordX2.append((z - 1) * Board_GapX + Board_X1 + Chess_Radius)
        Actual_CordY2.append((i - 1) * Board_GapY + Board_Y1 + Chess_Radius)

#Create Board
s.create_rectangle(Board_X1 - Frame_Gap, Board_Y1 - Frame_Gap, Board_X1 + Frame_Gap + Board_GapX * Board_Size, Board_Y1 + Frame_Gap + Board_GapY * Board_Size, width = 3)

for f in range(Board_Size + 1):
    s.create_line(Board_X1, Board_Y1 + f * Board_GapY, Board_X1 + Board_GapX * Board_Size, Board_Y1 + f * Board_GapY)
    s.create_line(Board_X1 + f * Board_GapX, Board_Y1, Board_X1 + f * Board_GapX, Board_Y1 + Board_GapY * Board_Size)

    s.create_text(Board_X1 - Frame_Gap * 1.7, Board_Y1 + f * Board_GapY, text = f + 1, font = "Helvetica 10 bold", fill = "black")
    s.create_text(Board_X1 + f * Board_GapX, Board_Y1 - Frame_Gap * 1.7, text = f + 1, font = "Helvetica 10 bold", fill = "black")

Turn_Text = Score_Board()

#Game Code
while Winner == None:
    s.update()

    X = Click_Cord[0]
    Y = Click_Cord[1]

    Picked = Location_Validation()

    if Picked:

        s.delete(Turn_Text)
        
        create_circle(Board_X1 + Board_GapX * (X - 1), Board_Y1 + Board_GapY * (Y - 1), radius = Chess_Radius, fill = Turn)

        if Turn_Num % 2 == 1:
            White_Cord_PickedX.append(X)
            White_Cord_PickedY.append(Y)
            board[Y - 1][X - 1] = 2
            Turn = "black"

        elif Turn_Num % 2 == 0:
            Black_Cord_PickedX.append(X)
            Black_Cord_PickedY.append(Y)
            board[Y - 1][X - 1] = 1
            Turn = "white"

        Turn_Text = Score_Board()

        Turn_Num = Turn_Num + 1

        if Turn == "white":
            Colour_Check = Black_Piece
            Win_Check = "Black"

        elif Turn == "black":
            Colour_Check = White_Piece
            Win_Check = "White"

        Winner = winCheck(Colour_Check, Win_Check, board)

s.delete(Turn_Text)

if Winner != "Exit":
    Score_Board()



    
