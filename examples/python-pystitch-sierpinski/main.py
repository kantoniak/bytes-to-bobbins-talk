from pathlib import Path
from pystitch import EmbPattern, CONTINGENCY_TIE_ON_THREE_SMALL, CONTINGENCY_TIE_OFF_THREE_SMALL, CONTINGENCY_LONG_STITCH_SEW_TO
from typing import List, Tuple
from utils import parse_args, UNITS_PER_MM
import math
import pystitch

args = parse_args(default_filename = f'out/{Path(__file__).parent.name}.jef')

# Create and encode pattern
SIDE_WIDTH = args.side_width * UNITS_PER_MM
CURVE_ORDER = args.curve_order
print(f'Curve order: {CURVE_ORDER}')


def build_arrowhead_curve(order: int, segment_length: float) -> List[Tuple[float, float]]:
  path = [(0.0, 0.0)]
  angle = 60 if order % 2 == 1 else 0

  def expand(symbol: str, depth: int):
    if depth == 0:
      return symbol
    result = ''
    for char in symbol:
      if char == 'A':
        result += 'B-A-B'
      elif char == 'B':
        result += 'A+B+A'
      else:
        result += char
    return expand(result, depth - 1)


  instructions = expand('A', order)
  for cmd in instructions:
    if cmd in 'AB':
      x, y = path[-1]
      dx = segment_length * math.cos(math.radians(angle))
      dy = segment_length * math.sin(math.radians(angle))
      path.append((x + dx, y - dy))
    elif cmd == '+':
      angle += 60
    elif cmd == '-':
      angle -= 60
  return path


segment_length = SIDE_WIDTH / pow(2, CURVE_ORDER)
print(f'Stitch length: {segment_length / UNITS_PER_MM}')
if (segment_length > 6 * UNITS_PER_MM) or (1 * UNITS_PER_MM > segment_length):
  print(f'Computed stitch length of {segment_length / UNITS_PER_MM} mm is out of recommended range 1-6 mm.')

pattern = EmbPattern()
pattern.add_block(build_arrowhead_curve(CURVE_ORDER, segment_length), "red")
pattern.move_center_to_origin()
pystitch.write(pattern, args.output, settings = {
    'max_stitch': segment_length + 1, # Forces acceptable stitch length, the value might be outside of range supported by the machine,
    'long_stitch_contingency': CONTINGENCY_LONG_STITCH_SEW_TO,
    'tie_on': CONTINGENCY_TIE_ON_THREE_SMALL, # Tie-on stitches before the pattern
    'tie_off': CONTINGENCY_TIE_OFF_THREE_SMALL, # Tie-off stitches after the pattern
  })