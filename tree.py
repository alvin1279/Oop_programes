class Node:
    def __init__(self,value):
        self.Value = value
        self.Children = []
        self.Children_number=0
    def add(self,value):
        self.Children.append(Node(value))
        self.Children_number+=1
    def print_tree(self):
        print(self.Value,end='\t')
        print(self.Children_number)
        if self.Children:
            print()
            for child in self.Children:
                child.print_tree()
            print()
    def add_node(self,node):
        self.Children.append(node)
        self.Children_number+=1
n= Node(10)
n.add(20)
n.add(30)
n.add(40)
p = Node(50)
p.add_node(n)
p.add_node(n)
n.print_tree()
p.print_tree()

print(p.Children_number)