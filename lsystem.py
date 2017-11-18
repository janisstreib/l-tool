from PIL import Image, ImageDraw
import math
import re


class LSystem(object):
    def __init__(self, start_pos, start_dir, step_length, constants, variables, axiom):
        self.pos = start_pos
        self.direction = start_dir
        self.step_length = step_length
        self.constants = constants
        self.variables = variables
        self.axiom = axiom

    old_pos = list()
    old_dir = list()

    @staticmethod
    def normalize(v):
        l = math.sqrt(v[0] * v[0] + v[1] * v[1])
        return v[0] / l, v[1] / l

    def draw_forward(self, draw, fill, stroke_width):
        npos = (self.pos[0] + self.step_length * self.direction[0], self.pos[1] + self.step_length * self.direction[1])
        draw.line([self.pos, npos], fill=fill, width=stroke_width)
        return npos, self.direction

    def store(self):
        self.old_pos.append(self.pos)
        self.old_dir.append(self.direction)
        return self.pos, self.direction

    def restore(self):
        return self.old_pos.pop(), self.old_dir.pop()

    def rotate(self, deg):
        rad = deg * math.pi / 180.0
        return self.pos, (self.direction[0] * math.cos(rad) - self.direction[1] * math.sin(rad),
                          self.direction[0] * math.sin(rad) + self.direction[1] * math.cos(rad))

    def reproduce(self, c):
        if c in self.constants:
            return c
        return self.variables[c]()

    def generate(self, max_depth):
        depth = 0
        self.input = self.axiom
        last = None
        print(self.input)
        while not last == self.input and depth < max_depth:
            last = self.input
            rep = {re.escape(k):v() for k,v in self.variables.items()}
            pattern = re.compile('|'.join(rep.keys()))
            self.input = pattern.sub(lambda m: rep[re.escape(m.group(0))], self.input)
            print(self.input)
            depth += 1

    def render(self, actions, image, filename, fill, stroke_width):
        d = ImageDraw.Draw(image)
        for c in self.input:
            if c in actions:
                self.pos, self.direction = actions[c](self, draw=d, fill=fill, stroke_width=stroke_width)
                self.direction = self.normalize(self.direction)
            else:
                print('WARN: Missing action:', c)

        del d
        image.save(filename, 'PNG')
