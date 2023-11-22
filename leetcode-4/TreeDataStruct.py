class Node:
    
    # we initialize node and childs of it
    # by default none
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # insert method for adding new nodes
    # simplw recursive method
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data) 
                else: 
                    self.left.insert(data) 
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
         # we checked if self.data exhists
         # we did it in line 13(cursed number btw)
         # if we don't have data node we just insert node as data
        else:
            self.data = data
            
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
            
            
            
root = Node(30)
root.insert(15)
root.insert(40)
root.insert(35)
root.insert(12)
root.insert(20)
root.print_tree()



# P.S I'm coding it on my phone on geography lesson at school
