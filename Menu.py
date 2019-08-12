import curses
import time
import sys
import os
import subprocess
from curses import textpad
import random
from DoubleLinked_CircularList import*
from Game import*
#Structures
listaC = CircularList()
game = Game()
#
#var user,points
userA = ""
pointsA = 0

#


menu = ['Play', 'Scoreboard','User Selection','Reports','Bulk Loading','Exit']

def print_menu(stdscr,selected_row_idx):
    h,w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)
    stdscr.refresh()

menuR = ['Snake Report','Score Report','ScoreBoard Report','Users Report','Return']
def print_menuR(stdscr,selected_row_idx):
    h,w = stdscr.getmaxyx()

    for idx, row in enumerate(menuR):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)
    stdscr.refresh()


def menup(stdscr):
               
        current_row_idx = 0
        print_menu(stdscr,current_row_idx)
        while 1:
                key = stdscr.getch()
                stdscr.clear()
                if key == curses.KEY_UP and current_row_idx > 0:
                        current_row_idx -= 1

                elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
                        current_row_idx += 1
                elif key == curses.KEY_ENTER or key in [10,13]:
                         #stdscr.addstr(0,0,"You pressed enter {}".format(menu[current_row_idx]))
                        if current_row_idx == 0:
                                game.Game()
                        elif current_row_idx == 2:
                                listUsers(stdscr)
                        elif current_row_idx == 3:
                                menuRe(stdscr)
                        elif current_row_idx == 4:
                                curses.echo()
                                bulkL(stdscr)
                                curses.noecho()
                        elif current_row_idx == 5:
                                sys.exit()   
                                    
                        #stdscr.refresh()
                        #stdscr.getch()
                print_menu(stdscr, current_row_idx)
                stdscr.refresh()


def menuRe(stdscr):
        current_row_idx = 0
        print_menuR(stdscr,current_row_idx)
        while 1:
                key = stdscr.getch()
                stdscr.clear()
                if key == curses.KEY_UP and current_row_idx > 0:
                        current_row_idx -= 1

                elif key == curses.KEY_DOWN and current_row_idx < len(menuR)-1:
                        current_row_idx += 1
                elif key == curses.KEY_ENTER or key in [10,13]:
                        #stdscr.addstr(0,0,"You pressed enter {}".format(menuR[current_row_idx]))
                        if current_row_idx == 3:
                                listaC.graphiz()
                        elif current_row_idx == 4:
                                menup(stdscr)
                        #stdscr.refresh()
                        #stdscr.getch()
                print_menuR(stdscr, current_row_idx)
                stdscr.refresh()

def bulkL(stdscr):

        
       name = stdscr.getstr()
       users = open(name,"r")
       for line in users.readlines():
               div = ","
               cadena = line.split(div)
               userN = cadena[0].rstrip('\n')
               if "\"Usuario\"" in userN:
                       print('')
               else:
                       listaC.add(userN)
                      
       users.close()  

def listUsers(stdscr):
        h,w = stdscr.getmaxyx()
        ActUsr = listaC.head
        #Tusr = "<---------------------------"+ActUsr.user.name+"----------------------------->"
        user_Text = "User: {}".format(ActUsr.user.name)
        stdscr.addstr(0, w//2 - len(ActUsr.user.name)//2, ActUsr.user.name)
        current_row_idx = 1
        while 1:
                key = stdscr.getch()
                stdscr.clear()
                if key == curses.KEY_UP and current_row_idx > 0:
                        current_row_idx -= 1

                elif key == curses.KEY_DOWN and current_row_idx < len(1)-1:
                        current_row_idx += 1
                elif key == curses.KEY_LEFT:
                        ActUsr = ActUsr.previous
                        #Tusr = "<---------------------------"+ActUsr.user.name+"----------------------------->"
                        user_Text = "User: {}".format(ActUsr.user.name)
                        stdscr.addstr(0, w//2 - len(ActUsr.user.name)//2, ActUsr.user.name)
                        stdscr.refresh()
                elif key == curses.KEY_RIGHT:
                        ActUsr = ActUsr.next
                        #Tusr = "<---------------------------"+ActUsr.user.name+"----------------------------->"
                        user_Text = "User: {}".format(ActUsr.user.name)
                        stdscr.addstr(0, w//2 - len(ActUsr.user.name)//2, ActUsr.user.name)
                        stdscr.refresh()
                elif key == curses.KEY_ENTER or key in [10,13]:
                        #stdscr.addstr(0,0,"You pressed enter {}".format(menuR[current_row_idx]))
                        userA = ActUsr.user.name
                        menup(stdscr)
                        #stdscr.refresh()
                        #stdscr.getch()
                
                stdscr.refresh()



def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)  
    menup(stdscr)
    


curses.wrapper(main)



###############################################GAME########################################3333
def food_generation(snake,box):
        food = None
    
        while food is None:
            food = [random.randint(box[0][0]+1,box[1][0]-1),
             random.randint(box[0][1]+1,box[1][1]-1)]
    
            if food in snake:
                food = None
        return food        
    
def print_score(stdscr,score):
        sh,sw = stdscr.getmaxyx()
        score_text = "Score: {}".format(score)
        stdscr.addstr(0,sw//2-len(score_text)//2,score_text)
        stdscr.refresh()
    
def GameS(stdscr):
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(150)
        sh ,sw = stdscr.getmaxyx()
        box = [[3,3],[sh-3, sw-3]]
        textpad.rectangle(stdscr,box[0][0],box[0][1],box[1][0],box[1][1])
        
        snake = [[sh//2,sw//2+1],[sh//2,sw//2],[sh//2,sw//2-1]]
        direction = curses.KEY_RIGHT
    
        for y,x in snake:
            stdscr.addstr(y,x,'#')
        
    
        food = food_generation(snake,box)
        stdscr.addstr(food[0],food[1],'*')
        
        score = 0
        print_score(stdscr,score)
    
    
        while 1:
            key = stdscr.getch()
            
            if key in [curses.KEY_RIGHT,curses.KEY_LEFT,curses.KEY_UP,curses.KEY_DOWN]:
                direction = key
    
            head = snake[0]
            if direction == curses.KEY_RIGHT:
                new_head = [head[0],head[1]+1]
            elif direction == curses.KEY_LEFT:
                new_head = [head[0],head[1]-1]
            elif direction == curses.KEY_UP:
                new_head = [head[0]-1,head[1]]
            elif direction == curses.KEY_DOWN:
                new_head = [head[0]+1,head[1]]       
    
            snake.insert(0, new_head)
            stdscr.addstr(new_head[0], new_head[1],'#')
    
            if snake[0] == food:
                food = food_generation(snake,box)
                stdscr.addstr(food[0],food[1],'*')
                score +=1
                print_score(stdscr,score) 
            else:
                stdscr.addstr(snake[-1][0],snake[-1][1],' ')    
                snake.pop()
    
            if (snake[0][0] in [box[0][0],box[1][0]] or 
                snake[0][1] in [box[0][1], box[1][1]] or
                snake[0] in snake[1:]):
                msg = "Game Over!"
                stdscr.addstr(sh//2,sw//2-len(msg)//2,msg)
                stdscr.nodelay(0)
                stdscr.getch()
                break
        
            stdscr.refresh()   
        
#curses.wrapper(GameS) 

