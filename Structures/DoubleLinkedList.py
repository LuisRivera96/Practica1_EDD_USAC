import os
import subprocess

class NodeDouble:
    def __init__(self,x,y,next,previous):
        self.x = x
        self.y= y
        self.next = None
        self.previous = None

class DoubleList:
    def __init__(self):
        self.head = None
        self.end = None
    def add(self,x,y):
        nodp = NodeDouble(x,y,None,None)

        if self.head is None:
            self.head = nodp
            self.end = nodp
            self.head.next = None
            self.head.previous = None
            print('First Coordinate')
        else:
            self.end.next = nodp
            nodp.previous = self.end
            nodp.next = None
            self.end = nodp
            print('Coordinate added')

    
    def printList(self):
        if self.head is None:
            print("List Empty")
        else:
            temp = self.head
            while temp.next is not self.head:
                print(temp.x,end='')
                print(temp.y,end='')
                print('->',end='')
                temp = temp.next
            print(temp.x,end='')
            print(temp.y,end='')
            print('->',end='')
            temp = temp.next
            print(temp.x)
            print(temp.y)
            #previous
            temp = self.end
            while temp.previous is not self.end:
                print(temp.x,end='')
                print(temp.y,end='')
                print('<-',end='')
                temp = temp.previous
            print(temp.x,end='')
            print(temp.y,end='')
            print('<-',end='')
            temp = temp.previous
            print(temp.x,end='')
            print(temp.y,end='')


    def graphiz(self):
        if self.head is None:
            print("List Empty")
        else:
            f = open('DoubleLinkedList.dot','w')
            f.write('digraph firsGraph{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')        
            temp = self.head
            count = 0
            while temp.next is not self.head:
                f.write('node{} [label=\"{},{}\"];\n'.format(count,temp.x,temp.y))
                count+=1    
                f.write('node{} -> node{};\n'.format(count-1,count))
                f.write('node{} -> node{};\n'.format(count,count-1))        
                temp = temp.next
        f.write('node{} [label=\"{},{}\"];\n'.format(count,temp.x,temp.y))     
        f.write('}')
        f.close()
        os.system('dot DoubleLinkedList.dot -Tpng -o DoubleLinkedList.png')
        os.system('DoubleLinkedList.png')
        #subproces no me corrio en windows Descomentar
        #subprocess.check_call(['open','DoubleLinkedList.png']) 