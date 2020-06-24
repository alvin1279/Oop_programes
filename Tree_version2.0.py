from collections import defaultdict


class Root:

    def __init__(self, data=None, parent=None):
        self.Children = []
        self.Data = data
        self.Parent = parent
        self.Depth = 0

    def set_depth(self):
        parent_depth = self.Parent.Depth
        for Node in self.tree_traversal():
            Node.Depth = parent_depth + Node.Depth + 1

    # This is used to add Tree as a node
    def add_node(self, Node):
        Node.Parent = self
        Node.set_depth()
        self.Children.append(Node)

    # This is used to add single unnamed nodes, by just providing the data for it
    def add_leaf(self, data):
        self.Children.append(Root(data, self))
        self.Children[-1].set_depth()

    # An iterative method to traverse the Tree
    # The traversal is mostly called by other methods such as method : build_depth_dict
    def tree_traversal(self):
        current = self
        stack = []  # Stack will consist of a Node and the index
        index = 0

        while True:

            # Adds to the stack the current Node, and whatever the current index value is , Index values determines
            # which path to go down if a path is non existent for that index it activates the next conditional
            if current is not None:
                stack.append([current, index])
                if len(current.Children) > index:
                    current = current.Children[index]  # Goes down the Node to the child at that index
                    index = 0  # index is again initialised to zero when going down
                else:
                    current = None
                    # Note that index is not initialised to zero since it will be updated in the below elif statement

            # This conditional activates when there is no more going down a path
            elif stack:
                current, _ = stack.pop()  # The Node with no more down paths are removed
                yield current
                if stack:
                    current, index = stack.pop()
                    index += 1  # The index is incremented since previous path in tree is exhausted
                else:
                    current = None
                    # When the stack is exhausted current has to be set to None or it will keep adding old current to
                    # stack and it will keep on looping
            else:
                break

    def build_depth_dict(self):
        treedict = defaultdict(list)
        for Node in self.tree_traversal():
            treedict[Node.Depth].append(Node.Data)
        return treedict

    def __str__(self):
        return f'({self.Depth},{self.Data})'


a = Root(20)

b = Root(30)
c = Root(40)
a.add_node(b)
a.add_node(c)

h = Root(12)
h.add_leaf(10)
i = Root(33)
j = Root(11)

b.add_node(h)
b.add_node(i)
a.add_node(j)

i.add_leaf(0)
"""
                            20(a)
                          /   |   \
                         /    |    \
                      30(b)  40(c)  11(j)
                       /  \
                   12(h)   33(i)
                  /           \
                10(leaf)     0(leaf)
"""
print(a.build_depth_dict())
