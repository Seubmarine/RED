import pyxel as px
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
        pass

    def draw(self):
        pass

    def update_node_and_child(self):
        self.update()
        if self.children_lenght > 0:
            for node in self.children:
                node.update_node_and_child()

    def draw_node_and_child(self):
        self.draw()
        if self.children_lenght > 0:
            for node in self.children:
                node.draw_node_and_child()


class Node2D(Node):
    def __init__(self, name, position: Vector2, size: Vector2, parent=None, children=None):
        super().__init__(name, parent, children)
        self.original_position = position 
        self.position = position
        self.size = size
        self.velocity = Vector2.ZERO
        self.speed = 2
        self.direction = Vector2.ZERO
        # self.aabb = self.get_collision_box()
        self.x = self.position.x
        self.y = self.position.y + 4
        self.l = self.y + self.size.y
        self.w = self.x + self.size.x

    def get_collision_box(self):
        pass
    def update(self):
        # if self.position.x > 0 and self.position.y > 0:
        #     test = px.tilemap(0).get(self.position.x/8,self.position.y/8)
        #     print("Bounds :", test)
        # else:
        #     print('Out of bounds')
        self.direction = Vector2.ZERO
        if px.btn(px.KEY_UP):
            self.direction += Vector2.UP
        if px.btn(px.KEY_RIGHT):
            self.direction += Vector2.RIGHT
        if px.btn(px.KEY_DOWN):
            self.direction += Vector2.DOWN
        if px.btn(px.KEY_LEFT):
            self.direction += Vector2.LEFT
        # self.direction = Vector2.LEFT
        self.velocity = self.direction.normalize() * self.speed
        self.position += self.velocity
        self.position = self.position.floor()
        print(self.position)
        # print(self.position, 'pos')
    def draw(self):
        px.bltm(-self.position.x + self.original_position.x,-self.position.y + self.original_position.y,0,0,0,255,255)
        px.blt(self.original_position.x, self.original_position.y, 0, 8, 8, 8, 8, colkey=1)
        px.pset(self.x, self.y, px.COLOR_PINK)
        # blt(self.position.x, self.position.y, 0, 8, 8, 8, 8)
