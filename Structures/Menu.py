import curses
import time
import sys
import os
import subprocess
from curses import textpad
import random
from DoubleLinked_CircularList import*
from Queue import*
from Stack import*
from DoubleLinkedList import*
#from Game import*
#Structures
listaC = CircularList()
col = Queue()
stk = Stack()
dbl = DoubleList()
#
#var user,points

userA = ""
user = ""
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
                                if userA == "":
                                        curses.echo()
                                        userN = stdscr.getstr()
                                        listaC.add(userN)
                                        stk.top = None
                                        global user 
                                        user = userN
                                        curses.noecho()
                                        
                                Game(stdscr)
                        elif current_row_idx == 1:
                                #hacer que se mantenga          
                                scoreB(stdscr)
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
                        if current_row_idx == 0:
                                dbl.graphiz()
                        elif current_row_idx == 1:
                                stk.graphiz()
                        elif current_row_idx == 2:
                                col.graphiz()
                        elif current_row_idx == 3:
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
                        global userA
                        stk.top = None
                        userA = ActUsr.user.name
                        global user
                        user =  userA
                        menup(stdscr)
                        #stdscr.refresh()
                        #stdscr.getch()
                
                stdscr.refresh()

def scoreB(stdscr):
        h,w = stdscr.getmaxyx()
        score_text1 = 'NAME          SCORE\n'
        auxc = col.head
        cont = 0
        while auxc != None and cont<10:
                score_text1 += str(auxc.user)+'        '+str(auxc.points)+'\n'
                cont += 1
                auxc = auxc.next
        stdscr.clear()        
        stdscr.addstr(0, w//2 - len(score_text1)//2,score_text1)
        
        

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)  
    menup(stdscr)
    






###############################################GAME########################################3333
def food_generation(snake,box):
    food = None

    while food is None:
        food = [random.randint(box[0][0]+1,box[1][0]-1),
         random.randint(box[0][1]+1,box[1][1]-1)]

        if food in snake:
            food = None
    return food        

def print_score(stdscr,score,user,level):
    sh,sw = stdscr.getmaxyx()
    score_text = "Score: {} User: {} ---LEVEL: {}".format(score,user,level)
    stdscr.addstr(0,sw//2-len(score_text)//2,score_text)
    stdscr.refresh()

def Game(stdscr):
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
    
    type = random.randint(0,100)
    if type <= 20:
        #bocadillo bad   
        food = food_generation(snake,box)
        stdscr.addstr(food[0],food[1],'*')
    else:
        food = food_generation(snake,box)
        stdscr.addstr(food[0],food[1],'+')    
    
    score = 0
    level = "1"
    
    print_score(stdscr,score,user,level)


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
        

        if snake[0] == food and type <=20:
            type = random.randint(0,100)      
            score -=1
            stk.pop()
            if score <= 0:
                msg = "Game Over!"
                stdscr.addstr(sh//2,sw//2-len(msg)//2,msg)
                stdscr.nodelay(0)
                #add scoreboard Report
                col.enqueue(user,score)
                score = 0
                stdscr.getch()
                dbl.head = None
                dbl.end = None
                for x in range(0,len(snake)):
                    dbl.add(snake[x][0],snake[x][1])
                break  

            if score >= 15:
                stdscr.timeout(75)
                level = "2"
            else:
                stdscr.timeout(150)
                level = "1"   
                
            if type <= 20:
                #bocadillo bad
                food = food_generation(snake,box)
                stdscr.addstr(food[0],food[1],'*')
            else:
                #bocadillo good
                food = food_generation(snake,box)
                stdscr.addstr(food[0],food[1],'+')

        elif snake[0] == food and type >20:
            if score >= 15:
                stdscr.timeout(75)
                level = "2"
            else:
                stdscr.timeout(150)
                level = "1"
            stk.push(food[0],food[1])
            score +=1
            print_score(stdscr,score,user,level)
            type = random.randint(0,100)
            if type <= 20:
                #bocadillo bad
                food = food_generation(snake,box)
                stdscr.addstr(food[0],food[1],'*')
            else:
                #bocadillo good
                food = food_generation(snake,box)
                stdscr.addstr(food[0],food[1],'+') 

        else:
            stdscr.addstr(snake[-1][0],snake[-1][1],' ')    
            snake.pop()
            

        if (snake[0][0] in [box[0][0],box[1][0]] or 
            snake[0][1] in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
            msg = "Game Over!"
            stdscr.addstr(sh//2,sw//2-len(msg)//2,msg)
            stdscr.nodelay(0)
            #add scoreboard Report
            col.enqueue(user,score)
            score = 0
            dbl.head = None
            dbl.end = None
            for x in range(0,len(snake)):
                    dbl.add(snake[x][0],snake[x][1])
            break
        
    
        stdscr.refresh()   
    
    
curses.wrapper(main)