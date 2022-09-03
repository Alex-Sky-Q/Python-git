# Challenge 1 - Create a method to draw a square
# Challenge 2 - Create a direction attr and a forward method to move scribe in that direction
# Challenge 3 - Create a data structure that defines some scribes with instructions for each of them
# and then create a function that takes in all of that data and makes the whole thing go.
# You can include the canvas definition in your data structure.
# Remember to include the starting direction for each scribe and maybe give them some names.

import os
import time
from termcolor import colored
import math as m


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))


class TerminalScribe:
    def __init__(self, canvas, direction=90):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]
        # Solution to Challenge 2
        self.direction = direction
        self.dist_x_rel = m.cos(m.radians(self.direction))
        self.dist_y_rel = m.sin(m.radians(self.direction))
        self.dist_x = round(self.dist_x_rel * self.canvas._x)
        self.dist_y = round(self.dist_y_rel * self.canvas._y)

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

# Solution to Challenge 2
    def forward(self):
        # 0 < degree <= 90 (sin for y, cos for x)
        if self.dist_x >= 0 and self.dist_y >= 0:
            for s in range(self.dist_x):
                self.right()
            for s in range(self.dist_y):
                self.up()
        # 90 < degree <= 180
        elif self.dist_x <= 0 <= self.dist_y:
            for s in range(abs(self.dist_x)):
                self.left()
            for s in range(self.dist_y):
                self.up()
        # 180 < degree <= 270
        elif self.dist_x <= 0 and self.dist_y <= 0:
            for s in range(abs(self.dist_x)):
                self.left()
            for s in range(abs(self.dist_y)):
                self.down()
        else:
            # for s in range(self.dist_x):
            #     self.right()
            # for s in range(abs(self.dist_y)):
            #     self.down()
            # A shorter way from A to B
            for x, y in zip(range(self.dist_x), range(abs(self.dist_y))):
                self.draw([round(x), round(y)])

# Solution to Challenge 1
    def drawSquare(self, size):
        for s in range(size):
            self.right()
        for s in range(size):
            self.down()
        for s in range(size):
            self.left()
        for s in range(size):
            self.up()


# Solution to Challenge 3
scribes_canvas = [{'canvas': (5, 5)},
                  {'name': 'Tess', 'direction': 300, 'move': 'forward'},
                  {'name': 'Man', 'direction': 315, 'move': 'forward'},
                  {'name': 'Cat', 'direction': 333, 'move': 'right'}]


def create_canvas(data_list):
    w, h = data_list[0]['canvas']
    return Canvas(w, h)


def create_scribes(data_list, canvas):
    temp_list = []
    for s in data_list[1:]:
        # temp_list.append([item for item in s.values()])
        temp_list.append([s['name'], TerminalScribe(canvas, s['direction']), s['move']])
    # print(temp_list)
    # move_scribe(temp_list)
    return temp_list


def move_scribe(s_list):
    for s in s_list:
        if s[2] == 'forward':
            s[1].forward()
        elif s[2] == 'right':
            s[1].right()
        # The same logic goes on


canvas_from_list = create_canvas(scribes_canvas)
scribe_1, scribe_2, scribe_3 = [s[1] for s in create_scribes(scribes_canvas, canvas_from_list)]

move_scribe(create_scribes(scribes_canvas, canvas_from_list))

# scribe_1.forward()
# scribe_2.forward()
# scribe_3.forward()

# canvas = Canvas(5, 5)
# scribe = TerminalScribe(canvas, 315)

# scribe.drawSquare(5)
# scribe.forward()

# scribe.right()
# scribe.right()
# scribe.right()
# scribe.down()
# scribe.down()
# scribe.down()
# scribe.left()
# scribe.left()
# scribe.left()
# scribe.up()
# scribe.up()
# scribe.up()
