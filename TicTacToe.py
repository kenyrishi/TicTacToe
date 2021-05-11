import pygame
from pygame.locals import *
import random
import math
moveDict = {'q':(0,0),'w':(0,1),'e':(0,2),'a':(1,0),'s':(1,1),'d':(1,2),'z':(2,0),'x':(2,1),'c':(2,2)}   
winCombos = ['qwe','asd','zxc','qaz','wsx','edc','qsc','esz']
#characters = {False:'X',True:'O'}
characters = ['X','O']
XTurn = True
grid = [['','',''],['','',''],['','','']]

'''
BLACK = pygame.Color(0, 0, 0)         # Black
WHITE = pygame.Color(255, 255, 255)   # White
GREY = pygame.Color(128, 128, 128)   # Grey
RED = pygame.Color(255, 0, 0)       # Red

boardSize = 450

pygame.init()
FPS = 30
FramePerSec = pygame.time.Clock()



screen = pygame.display.set_mode((boardSize,boardSize))
screen.fill(WHITE)
pygame.display.set_caption("tic tac toe")



def drawGrid():
    
    pygame.draw.line(screen,BLACK,(0,150),(450,150),5)
    pygame.draw.line(screen,BLACK,(0,300),(450,300),5)
    pygame.draw.line(screen,BLACK,(150,0),(150,450),5)
    pygame.draw.line(screen,BLACK,(300,0),(300,450),5)


def checkPressed():
    global XTurn
    global grid
    myFont = pygame.font.SysFont("Times New Roman", 24)
    
    mouseX,mouseY = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click != (0,0,0):
        #position = myFont.render(f'{mouseX},{mouseY}',1,BLACK)
        #screen.blit(position,(mouseX,mouseY))
        x = math.floor(mouseX/150)
        y = math.floor(mouseY/150)
        if grid[y][x] == '':
            if XTurn:
                printX(x,y)
                grid[y][x] = 'X'
            else:
                printO(x,y)
                grid[y][x] = 'O'

            XTurn = not XTurn


def printX(x,y):
    pygame.draw.line(screen,BLACK,(150*x,150*y),(150*(x+1),150*(y+1)),5)
    pygame.draw.line(screen,BLACK,(150*(x+1),150*y),(150*x,150*(y+1)),5)


def printO(x,y):
    pygame.draw.circle(screen,BLACK,(150*x+75,150*y+75),75,5)
    

'''
        
    


def start():
    a = input('\nEnter 1 for 1 player, 2 for 2 player, or 0 for instructions. ')
    if a == '0':
        instructions()
    elif a == '1':
        play1()
    elif a == '2':
        play2()
    else:
        print('That is not a valid response. Pleas try again')
        start()
    
def instructions():
    print('Enter letters on the keyboard to do your moves.')
    print(' q w e \n a s d\n z x c')
    start()

def play1():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    won = False
    tie = False
    turn = True
    player = chooseSide()
    printGame(board)
    while (won == False and tie == False):
        turn = not turn
        if player == turn:
            a,b = move(characters[int(turn)],board)
            board[a][b] = characters[int(turn)]
        else:
            a,b = compMove2(characters[int(turn)],board)
            board[a][b] = characters[int(turn)]
        printGame(board)
        won = checkWon(board,turn)
        tie = checkTie(board)
    end(turn,won,tie)

def play2():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    won = False
    tie = False
    turn = True
    
    printGame(board)
    while (won == False and tie == False):
        turn = not turn
        a,b = move(characters[int(turn)],board)
        board[a][b] = characters[int(turn)]
        printGame(board)
        won = checkWon(board,turn)
        tie = checkTie(board)
        
    end(turn,won,tie)


def chooseSide():
    a = input('Would you like to be X or O').upper()
    if a in characters:
        return bool(characters.index(a))
    print('Please try again')
    chooseSide()

def printGame(game):
    print('\n')
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i<2:
            print('-+-+-')


def move(char,game):
    
    print(f'\nIt is {char}\'s turn.')
    val = input('Enter a move:  ')
    
    if val in moveDict.keys():
        pmove = moveDict[val]
        a = pmove[0]
        b = pmove[1]

        if game[a][b] == ' ':
            return a,b

        else:
            print('Choose a square that is not taken')
            move(char,game)
        
    else:
        print('Enter a valid character: q,w,e,a,s,d,z,x,c. Please try again.')
        move(char,game)

def compMove(char,game):
    empty = []
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == ' ':
                empty.append((i,j))

    move = random.choice(empty)
    return move[0],move[1]


def compMove2(char,game):#????????????????
    
    empty = []
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == ' ':
                empty.append((i,j))

    for i in empty:#?????????????
        a = game[:]
        a[i[0]][i[1]] = char
        if checkWon(a,characters.index(char)):
            return i[0],i[1]
        a[i[0]][i[1]] = ' '
 
    new = characters[characters.index(char)-1]   
    
    for i in empty:
        a = game[:]
        a[i[0]][i[1]] = new
        if checkWon(a,characters.index(new)):
            a[i[0]][i[1]] = char
            return i[0],i[1]
        a[i[0]][i[1]] = ' '

    return compMove(char,game)
    

def inList(chars):
    for i in winCombos:
        if (i[0] in chars) and (i[1] in chars) and (i[2] in chars):
            return True
    return False
                            

def checkWon(game,turn):
    chars = []
    player = characters[int(turn)]
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == player:
                a = (i,j)
                for char,index in moveDict.items():
                    if index == a:
                        chars.append(char)

    return(inList(chars))

def checkTie(game):
    empty = []
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == ' ':
                empty.append((i,j))

    return(len(empty) == 0)
    

def end(turn,won,tie):
    if (won):
        print(f'{characters[turn]} won!')
    else:
        print('It is a tie!')




start()

'''

running = True

while running:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.display.quit()
            running = False

    
    #screen.fill(WHITE)
    drawGrid()
    checkPressed()
    
    

    pygame.display.flip()
    FramePerSec.tick(FPS)
    
    
        

'''
