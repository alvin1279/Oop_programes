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
        dict =[]
        current = self
        stack = []
        count = 0
        while True:
            if current is not None:
                stack.append([current,count])
                if len(current.Children)>count:
                    current = current.Children[count]
                    count = 0
                else:
                    current = None
            elif stack:
                current,_ = stack.pop()
                dict.append(current.Data)
                if stack:
                    current,count=stack.pop()
                    count+=1
                else:
                    current = None
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
k = Root(0)
j.addNode(k)

b.addNode(h)
b.addNode(i)
a.addNode(j)
"""
                            20(a)
                          /   |   \
                         /    |    \
                      30(b)  40(c)  11(j)
                       /  \
                   12(h)   33(i)
                             \
                              0(k)
"""
a.printTree()