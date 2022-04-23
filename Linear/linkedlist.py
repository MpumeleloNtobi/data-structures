# A class for creating a linked list node object 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def remove_first(self, data):
        if self.root is None:
            pass
        else:
            self.root = self.root.next

    def remove_last(self, data):
        if self.root is None:
            pass
        else:
            current_node = self.root
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            
    def front():
        if self.root is not None:
            print(self.root.data)
        else:
            print(self.root)

    def rear():
        if self.root is None:
            print(self.root)
        else:
            current_node = self.root
            while current_node.next.next is not None:
                current_node = current_node.next
            print(current_node.next)

    def print_list(self):
        if self.root is None:
            return
        else:
            current_node = self.root
            while current_node.next is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print(current_node.data, end=" -> ")
            print(current_node.next)
