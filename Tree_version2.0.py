from collections import defaultdict


# This is the Root class, the Root and only the Root of a tree is initialised with Root class
class Root:

    # The root contains by default Depth = 0 and Parent as None
    # Root and Nodes in common contains the list of Children and Data of the entity
    def __init__(self, data=None):
        self.Children = []
        self.Data = data
        self.Depth = 0
        self.Parent = None

    # To later independently add new attribute or change value of any attribute
    def set_attribute(self, attribute, data):
        self.__dict__[attribute] = data

    # Adds end nodes or leafs which is not a named entity
    def add_leaf(self, data):
        self.Children.append(Node(data, self))

    # To add whole another Tree to This Instance(Which is a node of another Tree)
    # The characteristics of the Root of the added tree is changed to behave as a node, but it is still a Root Entity
    # The Parent of the root is changed from None to this Instance
    # The depth is initialised to 1 then modified to depend on parent depth
    def add_tree(self, Tree):
        Tree.Parent = self
        Tree.Depth = 1
        Tree.set_depth()
        self.Children.append(Tree)

    # Method to set or update the depth of a leaf/Node/Tree and its children if any exists
    def set_depth(self):
        # The node depth is just parent depth + 1
        self.Depth = self.Parent.Depth + 1
        # The depth of the child nodes are also updated if children exists
        if self.Children:
            for child in self.Children:
                child.set_depth()

    # An iterative method to traverse the Tree
    # The traversal is mostly called by other methods such as method : build_depth_dict
    def tree_traversal(self):
        current = self  # Initial current value is of the Root or the node for which tree traversal  is called
        stack = []  # Stack will consist of a Node and the index
        index = 0  # index value determines which child from list is taken, initialised to zero

        while True:

            if current is not None:
                # Adds to the stack the current Node, and whatever the current index value is
                stack.append([current, index])
                if len(current.Children) > index:
                    current = current.Children[index]  # Goes down the Node to the child at that index
                    index = 0  # index is again initialised to zero when going down
                else:
                    current = None
                    # Note that index is not initialised to zero since it will be updated in the below elif statement

            # This conditional activates when the current stack top has no children or index goes out of bound for it
            elif stack:
                current, _ = stack.pop()  # The stack top is popped out, index is not needed
                yield current.Data, current.Depth  # yields the value to whatever function that called tree traversal
                if stack:
                    current, index = stack.pop()  # The stack is popped again
                    index += 1  # The index is updates
                    # Updated index and current Node will be added to stack in above if statement
                else:
                    current = None
                    # This will only activate when tree is exhausted
            else:
                break

    # A function to make a dictionary with depth and list with all Node data at that depth
    def build_depth_dict(self):
        treedict = defaultdict(list)
        for (node, depth) in self.tree_traversal():
            treedict[depth].append(node)
        return treedict

    def __str__(self):
        return f'({self.Depth},{self.Data})'


# Node class is use to make nodes, it inherits the the methods of root but the instance initialisation is changed
# Node has a Parent, The depth is found using the set_depth method
class Node(Root):
    def __init__(self, data, parent):
        super().__init__(data)
        self.Parent = parent
        self.set_depth()


a = Root(20)

b = Root(30)
c = Root(40)
a.add_tree(b)
a.add_tree(c)

h = Root(12)
i = Root(33)
j = Root(11)

b.add_tree(h)
b.add_tree(i)
a.add_tree(j)

k = Root(0)
i.add_tree(k)
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
