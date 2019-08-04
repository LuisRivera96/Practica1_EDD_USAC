
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





prueba = Queue()
prueba.enqueue("asda",0)
prueba.enqueue("hola",1)
prueba.enqueue("co",3)
prueba.enqueue("la",4)
prueba.print()
prueba.dequeue()
prueba.print()
prueba.dequeue()
prueba.print()
