import os
import subprocess
class NodeQ:
     def __init__(self,user,points,next):
         self.user = user
         self.points = points
         self.next = None



class Queue:
    def __init__(self):
        self.head = None
    def enqueue(self,user,points):
        nodo = NodeQ(user,points,None)

        if self.head is None:
            self.head = nodo
            print('First Score')
        else:
            nodo.next = self.head
            self.head = nodo
            print('Added Score')

    def dequeue(self):
        if self.head is None:
            print('Queue is Empity')
        else:
            self.head = self.head.next
            print('Dequeue')

    def print(self):
        if self.head is None:
            print("Queue Empty")
        else:
            temp = self.head
            while temp is not None:
                if temp.next is None:
                    print(temp.user,end='')
                else:
                    print(temp.user,end='')
                    print('->',end='')
                temp = temp.next

    # GRAPHIZ (Generar Graphiz)
    def graphiz(self):
        if self.head is None:
            print('Queue Empty')
        else:
            f = open('Queue.dot','w')
            f.write('digraph firsGraph{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')
            temp = self.head
            count = 0
            while(temp.next is not None):
                f.write('node{} [label=\"{},{}\"];\n'.format(count,temp.user,temp.points))
                count+=1
                f.write('node{} -> node{};\n'.format(count-1,count))
                #if temp.dato is valor:
                    #print('Se encontro el elemento ',end='')
                    #print(temp.dato)
                
                temp = temp.next
            f.write('node{} [label=\"{},{}\"];\n'.format(count,temp.user,temp.points))    
            f.write('}')
            f.close()
            os.system('dot Queue.dot -Tpng -o Queue.png')
            os.system('Queue.png')
            #subproces no me corrio en windows Descomentar
            #subprocess.check_call(['open','Queue.png'])



