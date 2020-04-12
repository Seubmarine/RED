import pyxel as px
from time import time
from vector import Vector2
from node import Node

world = Node('world')
test1 = Node('test1')
test2 = Node('test2')
test3 = Node('test3')
test4 = Node('test4')
test6 = Node('test6')
test5 = Node('test5', None, [test6])

test3.set_parent(test1)
test1.set_parent(world)
test2.set_parent(world)
test4.set_parent(test1)
test5.set_parent(test2)

class App:
    def __init__(self):

        self.starting_time = time()
        self.last_time = 0
        px.init(160, 120, fps=60)
        px.run(self.update, self.draw)

    def update(self):
        t = time()
        _dt = t - self.last_time
        self.last_time = t

        world.update()

    def draw(self):
        px.cls(0)


App()
