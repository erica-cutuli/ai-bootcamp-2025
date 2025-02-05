class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0
    def __len__(self):
        return self.lenght
    def add_node(self, data):
        new_node = Node(data)
        new_node.next = [None if self.lenght == 0]
        self.head = [new_node if self.lenght == 0]
        self.lenght += 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    @property
    def next(self):
        next_item = None
        if

