from vector import Vector2

Vector2.ZERO = Vector2(0, 0)


class Node:
    def __init__(self, name, parent=None, children=None):
        """name is arbitrary for now, parent is a single node, children should be in a list"""
        self.name = name
        self.parent = parent if parent is None else self.set_parent(parent)
        self.children = []
        self.children_lenght = 0
        if children != None:
            self.set_children(children)
    
    def update_children_lenght(self):
        self.children_lenght = len(self.children)

    def set_children(self, children):
        """Set yourself as the parent of given node(s), children should be put in a list"""
        for node in children:
            node.parent = self
        self.children.extend(children)
        self.update_children_lenght()

    def get_children(self):
        return self.children

    def get_children_lenght(self):
        return self.children_lenght

    def append_children(self, node):
        if type(node) == list:
            self.children.extend(node)
        else:
            self.children.append(node)
        self.update_children_lenght()

    def set_parent(self, node):
        """Set yourself as the child of given node"""
        self.parent = node
        node.append_children(self)

    def get_parent(self):
        return self.parent

    def get_children_name(self):
        name_list = []
        for node_position_index, node in enumerate(self.children):
            name_list.append("%s at position %d" %
                             (node.name, node_position_index))
        return name_list

    def get_children_by_name(self, name):
        for node in self.children:
            if node.name == name:
                return node

    def update(self):
        print(self.name)
        if self.children_lenght > 0:
            for node in self.children:
                node.update()

    def draw(self):
        for node in self.children:
            node.draw()
