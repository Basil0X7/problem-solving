class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def new_next(self, data):
        new_node = Node(data)
        if not self.head:
            self.current = self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.back = self.tail
            self.tail = new_node
            self.current.back = self.current
            self.current = new_node

    def add_back(self, string):
        if self.current:
            self.current = self.current.back
            self.current.data += string

    def add_next(self, string):
        if self.current:
            self.current.data += string
            self.current = self.current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x = list(s)
        node_counter = 0
        basil = DoublyLinkedList()
        for i in range(numRows):
            basil.new_next(x[i])
            node_counter += 1
        j = node_counter

        while j < len(x):
            if node_counter == numRows:
                while node_counter > 0 and j < len(x):
                    basil.add_back(x[j])
                    node_counter -= 1
                    j += 1
            else:
                while node_counter < numRows and j < len(x):
                    basil.add_next(x[j])
                    node_counter += 1
                    j += 1

        basil.display()

        # for h in range(len(x)):








