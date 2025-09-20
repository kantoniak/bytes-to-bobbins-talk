from pathlib import Path
from pystitch import EmbPattern, STITCH, TRIM, END
from utils import parse_args, UNITS_PER_MM

args = parse_args(default_filename = f'out/{Path(__file__).parent.name}.jef')

# Create and encode pattern
STITCH_UNITS = 3 * UNITS_PER_MM

pattern = EmbPattern()
pattern.add_stitch_absolute(STITCH, x=-STITCH_UNITS/2, y=-STITCH_UNITS/2)
pattern.add_stitch_relative(STITCH, dx=STITCH_UNITS, dy=0)
pattern.add_stitch_relative(STITCH, dx=0, dy=STITCH_UNITS)
pattern.add_stitch_relative(STITCH, dx=-STITCH_UNITS, dy=0)
pattern.add_stitch_relative(STITCH, dx=0, dy=-STITCH_UNITS)
pattern.add_command(TRIM)
pattern.add_command(END)
pattern.write(args.output)