
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

    def graphic(self):
        dot = ""
        aux = self.head.next
        grap = open("grafic.dot","w")
        grap.write("digraph USERS\n{\n")
        grap.write("compound=true;\n")
        grap.write("node [shape = \"Mrecord\"];\n")
        grap.write("rankdir=\"LR\";\n")
        grap.write("color=green;\n")
        while aux.next is not self.head:
            grap.write("\"")
            grap.write(str(aux.user.name))
            grap.write("\"")

            grap.write("->")
            aux = aux.next
        grap.write("\"")
        grap.write(str(aux.user.name))
        grap.write("\"")
        grap.write("->")
        aux = aux.next
        grap.write("\"")
        grap.write(str(aux.user.name))
        grap.write("\"")
        grap.write("}\n")
        grap.close()

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

























