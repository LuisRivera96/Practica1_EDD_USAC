import os
import subprocess
class User:

    def __init__(self,name,points):
        self.name = name
        self.points = points

class NodeCircular:
    def __init__(self,User,next,previous):
        self.user = User
        self.next = None
        self.previous = None

class CircularList:
    def __init__(self):
        self.head = None
        self.end = None
    def add(self,user):
        usr = User(user,0)
        nodp = NodeCircular(usr,None,None)

        if self.head is None:
            self.head = nodp
            self.end = nodp
            self.head.next = self.head
            self.head.previous = self.head
            print('First User')
        else:
            self.end.next = nodp
            self.head.previous = nodp
            nodp.previous = self.end
            nodp.next = self.head
            self.end = nodp
            print('User added')

    
    def printList(self):
        if self.head is None:
            print("List Empty")
        else:
            temp = self.head
            while temp.next is not self.head:
                print(temp.user.name,end='')
                print('->',end='')
                temp = temp.next
            print(temp.user.name,end='')
            print('->',end='')
            temp = temp.next
            print(temp.user.name)
            #previous
            temp = self.end
            while temp.previous is not self.end:
                print(temp.user.name,end='')
                print('<-',end='')
                temp = temp.previous
            print(temp.user.name,end='')
            print('<-',end='')
            temp = temp.previous
            print(temp.user.name)


    def graphiz(self):
        if self.head is None:
            print("List Empty")
        else:
            f = open('CircularList.dot','w')
            f.write('digraph firsGraph{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')        
            temp = self.head
            count = 0
            while temp.next is not self.head:
                f.write('node{} [label=\"{}\"];\n'.format(count,temp.user.name))
                count+=1    
                f.write('node{} -> node{};\n'.format(count-1,count))
                f.write('node{} -> node{};\n'.format(count,count-1))        
                temp = temp.next
        f.write('node{} [label=\"{}\"];\n'.format(count,temp.user.name))
        f.write('node{} -> node{};\n'.format(0,count))
        f.write('node{} -> node{};\n'.format(count,0))      
        f.write('}')
        f.close()
        os.system('dot CircularList.dot -Tpng -o CircularList.png')
        os.system('CircularList.png')
        #subproces no me corrio en windows Descomentar
        #subprocess.check_call(['open','CircularList.png']) 
        
           

























