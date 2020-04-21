import pyxel as px
from time import time
from vector import Vector2
from const import SCREEN_SIZE_HALF
from node import Node, Node2D

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

try1 = Node2D('test20', SCREEN_SIZE_HALF, Vector2(8,8),test1)

class App:
    def __init__(self):

        self.starting_time = time()
        self.last_time = 0
        px.init(256, 256, caption='RED',fps=60, scale=5)
        px.load('./assets/assetpack1.pyxres')
        px.run(self.update, self.draw)

    def update(self):
        t = time()
        _dt = t - self.last_time
        self.last_time = t
        world.update_node_and_child()


    def draw(self):
        px.cls(0)
        world.draw_node_and_child()
        # px.bltm(0,0,0,0,0,32,32)
        px.text(10 , 10, 'TEST', px.COLOR_PEACH )

App()
