class Fractal(object):
    constants = None
    variables = None
    actions = None
    default_start_dir = 0
    default_start_pos = (0,0)
    default_axiom = None
    default_depth = 0

# Stolen from https://en.wikipedia.org/wiki/L-system
class FractalPlant(Fractal):
    default_start_dir = -50
    default_axiom = 'X'
    default_depth = 6
    default_start_pos = (10,10)
    variables = {'X': lambda: 'F[-X][X]F[-X]+FX', 'F': lambda: 'FF'}
    constants = ['+', '-', '[', ']']
    actions = {'F': lambda l, draw, fill, stroke_width: l.draw_forward(draw, fill=fill, stroke_width=stroke_width),
               '[': lambda l, draw, fill, stroke_width: l.store(),
               ']': lambda l, draw, fill, stroke_width: l.restore(),
               'X': lambda l, draw, fill, stroke_width: (l.pos, l.direction),
               '-': lambda l, draw, fill, stroke_width: l.rotate(-25),
               '+': lambda l, draw, fill, stroke_width: l.rotate(25)}

class DragonCurve(Fractal):
    default_start_dir = 0
    default_axiom = 'FX'
    default_depth = 10
    variables = {'X': lambda: 'X+YF+', 'Y': lambda: '-FX-Y'}
    constants = ['F', '+', '-']
    actions = {'F': lambda l, draw, fill, stroke_width: l.draw_forward(draw, fill=fill, stroke_width=stroke_width),
               '-': lambda l, draw, fill, stroke_width: l.rotate(90),
               '+': lambda l, draw, fill, stroke_width: l.rotate(-90),
               'X': lambda l, draw, fill, stroke_width: (l.pos, l.direction),
               'Y': lambda l, draw, fill, stroke_width: (l.pos, l.direction),
               }

class SierpinskiTriangle(Fractal):
    default_start_dir = 0
    default_axiom = 'F-G-G'
    default_depth = 4
    variables = {'F': lambda: 'F-G+F+G-F', 'G': lambda: 'GG'}
    constants = ['+', '-']
    actions = {'F': lambda l, draw, fill, stroke_width: l.draw_forward(draw, fill=fill, stroke_width=stroke_width),
               'G': lambda l, draw, fill, stroke_width: l.draw_forward(draw, fill=fill, stroke_width=stroke_width),
               '+': lambda l, draw, fill, stroke_width: l.rotate(-120),
               '-': lambda l, draw, fill, stroke_width: l.rotate(+120)}

class KochCurve(Fractal):
    default_start_dir = 0
    default_axiom = 'F'
    default_depth = 4
    variables = {'F': lambda: 'F+F-F-F+F'}
    constants = ['+', '-']
    actions = {'F': lambda l, draw, fill, stroke_width: l.draw_forward(draw, fill=fill, stroke_width=stroke_width),
               '+': lambda l, draw, fill, stroke_width: l.rotate(-90),
               '-': lambda l, draw, fill, stroke_width: l.rotate(+90)}
