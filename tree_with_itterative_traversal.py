from collections import defaultdict


class Root:
    def __init__(self, data=None):
        self.Children = []
        self.Data = data
        self.Depth = 0

    def set_attribute(self, attribute, data):
        self.__dict__[attribute] = data

    def find_depth(self, initial):
        self.Depth = initial + 1

    def add_node(self, Node):
        self.Children.append(Node)
        Node.find_depth(self.Depth)

    def tree_traversal(self):
        current = self
        stack = []
        count = 0
        while True:
            if current is not None:
                stack.append([current, count])
                if len(current.Children) > count:
                    current = current.Children[count]
                    count = 0
                else:
                    current = None
            elif stack:
                current, _ = stack.pop()
                yield current.Data, current.Depth
                if stack:
                    current, count = stack.pop()
                    count += 1
                else:
                    current = None
            else:
                break

    def build_depth_dict(self):
        treedict = defaultdict(list)
        for (node, depth) in self.tree_traversal():
            treedict[depth].append(node)
        return treedict


a = Root(20)

b = Root(30)
c = Root(40)
a.add_node(b)
a.add_node(c)

h = Root(12)
i = Root(33)
j = Root(11)

b.add_node(h)
b.add_node(i)
a.add_node(j)

k = Root(0)
i.add_node(k)
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
print(a.build_depth_dict())
