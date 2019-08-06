import curses
import time
import sys
from DoubleLinked_CircularList import*
#Structures
listaC = CircularList()

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
                        if current_row_idx == 2:
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
                        if current_row_idx == 4:
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
               userN = cadena[0]
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
        current_row_idx = 0
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