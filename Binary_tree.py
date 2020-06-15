class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self,value):
        if self.value:
            if self.value<value:
                if self.right == None:
                    self.right = node(value)
                else:
                    self.right.insert(value)
            elif self.value>value:
                if self.left == None:
                    self.left = node(value)
                else:
                    self.left.insert(value)
        else:
                self.value = value
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value,end='\t')
        if  self.right:
            self.right.print_tree()
a = [15,13,14,15,11,23,10,18,19,43]
start = node(16)
for value in a:
    start.insert(value)
start.print_tree()