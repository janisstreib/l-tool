# l-tool
Playing around with Lindenmayer Systems (L-Systems)

## Setup
`l-tool` requires pillow, a PIL implementation.

## Usage
Example: 
  
    python3 l_tool.py --func FractalPlant --width 1250 --height 990 --out plant.png --stepsize=8 --stroke-width=3

![Image of a fractal plant](https://janis-streib.de/l-tool/fractal_plant_6.png)

For advanced options, consult `python3 l_tool.py -h`.

## Add a fractal
The reproduction rules are defined in `lfractals.py`.
