from argparse import ArgumentParser
import os

UNITS_PER_MM = 10

def parse_args(default_filename: str = 'out/out.jef'):
  ALLOWED_EXTENSIONS = [
    '.dst',  # Tajima Embroidery Format
    '.exp',  # Melco Expanded Embroidery Format
    '.gcode',  # gcode Format, Text File
    '.jef',  # Janome Embroidery Format
    '.pec',  # Brother Embroidery Format
    '.pes',  # Brother Embroidery Format
    '.tbf',  # Tajima Embroidery Format
    '.u01',  # Barudan Embroidery Format
    '.vp3',  # Pfaff Embroidery Format
    '.xxx'   # Singer Embroidery Format
  ]

  parser = ArgumentParser(description="Generate an embroidery design.")
  parser.add_argument('-o', '--output', type=str, default=default_filename, help=f"Output file path. {default_filename} by default")
  args = parser.parse_args()

  _, ext = os.path.splitext(args.output)
  if ext.lower() not in ALLOWED_EXTENSIONS:
    raise ValueError(f"Invalid file extension '{ext}'. Allowed extensions: {ALLOWED_EXTENSIONS}")

  return args