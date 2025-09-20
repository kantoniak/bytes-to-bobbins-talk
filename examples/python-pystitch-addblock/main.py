from pathlib import Path
from pystitch import EmbPattern
from typing import List, Tuple
from utils import parse_args, UNITS_PER_MM

args = parse_args(default_filename = f'out/{Path(__file__).parent.name}.jef')

# Create and encode pattern
STITCH_UNITS = 2 * UNITS_PER_MM
CENTERED_SQUARE_COORDS = [(-1/2, -1/2), (1/2, -1/2), (1/2, 1/2), (-1/2, 1/2), (-1/2, -1/2)]

def scale_pattern(coords: List[Tuple[float, float]], scale: float):
    return list((scale*x, scale*y) for (x, y) in coords)

pattern = EmbPattern()
pattern.add_block(scale_pattern(CENTERED_SQUARE_COORDS, 1*STITCH_UNITS), "red") # 2 mm stitch
pattern.add_block(scale_pattern(CENTERED_SQUARE_COORDS, 2*STITCH_UNITS), "orange") # 4 mm stitch
pattern.add_block(scale_pattern(CENTERED_SQUARE_COORDS, 3*STITCH_UNITS), "yellow") # 6 mm stitch
pattern.write(args.output)