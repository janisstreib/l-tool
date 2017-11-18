import lsystem
from PIL import Image
import math
import argparse
import lfractals

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='L-System tool.')
    parser.add_argument('--fill-color', nargs=4, dest='fill_color',
                        help='Color of the strokes (RGBA)', required=False)
    parser.add_argument('--start-pos', nargs=2, dest='start_pos',
                        help='Initial position on the canvas', required=False)
    parser.add_argument('--start-dir', dest='start_dir', type=int,
                        help='Initial direction degree', required=False)
    parser.add_argument('--width', dest='width', type=int,
                        help='Canvas width', required=True)
    parser.add_argument('--height', dest='height', type=int,
                        help='Canvas height', required=True)
    parser.add_argument('--out', dest='filename',
                        help='Filename to save the generated image', required=True)
    parser.add_argument('--stepsize', dest='stepsize', type=float,
                        help='Stepsize for size', required=True)
    parser.add_argument('--axiom', dest='axiom', type=str,
                        help='Axiom', required=False)
    parser.add_argument('--stroke-width', dest='stroke_width', type=int,
                        help='with of lines in pixel', required=False)
    parser.add_argument('--depth', dest='depth', type=int,
                        help='depth', required=False)
    parser.add_argument('--func', dest='func', type=str, help='Name of the fractal class', required=True)
    parser.set_defaults(stroke_width=2)
    args = parser.parse_args()
    class_ = getattr(lfractals, args.func)
    f = class_()
    pos = (int(args.start_pos[0]), args.height - int(args.start_pos[1])) if args.start_pos is not None else (
    f.default_start_pos[0], args.height - f.default_start_pos[1])
    sdir = args.start_dir if args.start_dir is not None else f.default_start_dir
    dir = (math.cos(sdir * math.pi / 180.0), math.sin(sdir * math.pi / 180.0))
    thing = Image.new('RGBA', (args.width, args.height), (255, 255, 255, 0))
    axiom = args.axiom if args.axiom is not None else f.default_axiom
    l = lsystem.LSystem(step_length=args.stepsize, start_dir=dir, start_pos=pos, axiom=axiom, variables=f.variables,
                        constants=f.constants)
    depth = args.depth if args.depth is not None else f.default_depth
    l.generate(max_depth=depth)
    fill_col = (int(args.fill_color[0]), int(args.fill_color[1]), int(args.fill_color[2]),
                     int(args.fill_color[3])) if args.fill_color is not None else (0, 0, 0, 255)
    l.render(image=thing, filename=args.filename, actions=f.actions, fill=fill_col, stroke_width=args.stroke_width)
