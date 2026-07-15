#Singly Linked List
class Node:
    self.daata = data
    self.next = None


class LinkedList:
    def __init__(self):
        self.head=None

    def print_LinkedList(self):
        if self.head is None:
            print("empty Linked List")
        else:
            n=self.head
        while n in not None:
                println(n.data,"-->",end=" ")

n1 = Node(10)
n2=Node(20)
n3=Node(30)

l=LinkedList()
l.head=n1
n1.next = n2
n2.next = n3

l.print_LinkedList()


