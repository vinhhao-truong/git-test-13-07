class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def setNext(self, value=None):
        self.next = Node(value)

    def getNext(self):
        if self.next == None:
            return None
        return self.next


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = self.head
        self.length = 0 if value == None else 1

    def insertTail(self, value):
        new_node = Node(value)
        if self.head.value == self.tail.value == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.setNext(new_node)
            self.tail = new_node

    def getMin(self):
        if self.head == self.tail == None:
            return None
        min = self.head.value
        currentNode = self.head.next
        while (currentNode != None):
            if currentNode.value < min:
                min = currentNode.value
            currentNode = currentNode.next
        return min
