# The Vacuum's Alibi: one excuse a robot vacuum gives for missing a spot, written to entry.txt.
import os
from pathlib import Path

output_dir = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
output_dir.mkdir(parents=True, exist_ok=True)

text = "My cliff sensors mistook your Persian rug fringe for the Grand Canyon and frankly, I value my gyroscopic stability too much."
(output_dir / 'entry.txt').write_text(text, encoding='utf-8')
