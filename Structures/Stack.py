import os
import subprocess
class NodeStack:
     def __init__(self,x,y,next):
         self.x = x
         self.y = y
         self.next = None



class Stack:
    def __init__(self):
        self.top = None
    def push(self,x,y):
        nodo = NodeStack(x,y,None)

        if self.top is None:
            self.top = nodo
            print('First Score')
        else:
            nodo.next = self.top
            self.top = nodo
            print('Added Score')

    def pop(self):
        if self.top is None:
            print('Stack is Empity')
        else:
            self.top = self.top.next
            print('Pop')

    def print(self):
        if self.top is None:
            print("Stack Empty")
        else:
            temp = self.top
            while temp is not None:
                if temp.next is None:
                    print(temp.x,end='')
                    print(temp.y)
                else:
                    print(temp.x,end='')
                    print(temp.y)
                temp = temp.next

    # GRAPHIZ (Generar Graphiz)
    def graphiz(self):
        if self.top is None:
            print('Stack Empty')
        else:
            f = open('Stack.dot','w')
            f.write('digraph firsGraph{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')
            f.write('nodo0[label=\"')
            f.write('|')
            temp = self.top
            count = 0
            while(temp.next is not None):           
                f.write('<{}> {},{}'.format(count,temp.x,temp.y))
                count+=1
                if temp.next.next is not None:
                    f.write('|')

                temp = temp.next
               
            f.write('\"];')
            f.close()
            os.system('dot Stack.dot -Tpng -o Stack.png')
            os.system('Stack.png')
            #subproces no me corrio en windows Descomentar
            #subprocess.check_call(['open','LinkedList.png'])    



