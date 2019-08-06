import curses
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

prueba = Stack()
prueba.push(0,0)
prueba.push(1,1)
prueba.push(2,2)
prueba.push(3,3)
prueba.print()
prueba.pop()
prueba.print()
prueba.pop()
prueba.print()
