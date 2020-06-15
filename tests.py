class Root:

    def __init__(self,Data=None):
        self.Children = []
        self.Data = Data
        self.Depth = 0
    def setAttribute(self,attribute,data):
        self.__dict__[attribute] = data
    def findDepth(self, initial):
        self.Depth = initial + 1
    def addNode(self,Node):
        self.Children.append(Node)
        Node.findDepth(self.Depth)
    def printTree(self):
        dict ={}
        current = self
        stack = []
        count = 0
        while True:
            if current is not None:
                stack.append([current,count])
                try:
                    current = current.Children[count]
                except:
                    current = None
            elif stack:
                current,_= stack.pop()
                try:
                    dict[current.Depth] += [current.Data]
                except:
                    dict[current.Depth] = [current.Data]
                try:
                    current.Children[count]
                except:
                    current = None
                if stack:
                    stack[-1][-1] += 1
                    count = stack[-1][-1]

            else:
                break
        print(dict)


a = Root(20)

b = Root(30)
c = Root(40)
a.addNode(b)
a.addNode(c)

h = Root(12)
i = Root(33)
j = Root(11)
b.addNode(h)
b.addNode(i)
a.addNode(j)
"""
                            20
                          /  |  \
                         /   |   \
                       30    40   12
                      /  \
                    12   33

"""
a.printTree()