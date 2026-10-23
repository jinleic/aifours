"""Remove duplicate rendered MathML and retain the supplied TeX alttext."""
from pathlib import Path
import re

src = Path("selection-inputs/literature/vorobyev-2026.reader.md").read_text()
# Each converted inline/display formula has one MathML comment, followed by
# a rendered duplicate. Retain the comment's alttext and drop its same-line
# rendering up to the next prose paragraph only when it is an entire line.
lines = []
for line in src.splitlines():
    line = re.sub(r'<!-- MathML: <math alttext="(.*?)".*?-->',
                  lambda m: " [TEX: " + m.group(1) + "] ", line)
    lines.append(line)
Path("notes/vorobyev-formulas.txt").write_text("\n".join(lines)+"\n")
