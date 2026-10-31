#!/usr/bin/env python3
"""Reviewer-authored text extraction of the pinned BBGT arXiv HTML (2307.13976v2).

Math elements are replaced by their LaTeX `alttext`; block elements and table
rows/cells become line breaks / ` | ` separators.  Each output line is prefixed
with the 1-based physical source line where its first character originated, so
every quoted row can be traced back to the pinned HTML.  The input SHA-256 is
checked before extraction.  Output is written with exclusive create.
"""
import hashlib
import html
import os
import sys
from html.parser import HTMLParser

SRC = ("/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/"
       "parallel-18/sun-coset8/frontier-20261029-bbgt-2307.13976v2-source.html")
SHA = "6cf5530f8386133e7208e6e0b77b1b44de78d8546549f2c3faf5144d403f9bfc"
WAVE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(WAVE, "reviewer-bbgt-extracted-text-v1.txt")

BLOCK = {"p", "div", "li", "tr", "br", "h1", "h2", "h3", "h4", "h5", "h6",
         "figcaption", "figure", "table", "section", "ul", "ol", "blockquote"}
SKIP = {"script", "style", "head"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines = []          # list of (src_line, text)
        self.cur = []
        self.cur_line = None
        self.math_depth = 0
        self.skip_depth = 0

    def emit(self, text):
        if not text:
            return
        if self.cur_line is None:
            self.cur_line = self.getpos()[0]
        self.cur.append(text)

    def flush(self):
        text = "".join(self.cur)
        text = " ".join(text.split())
        if text:
            self.lines.append((self.cur_line, text))
        self.cur = []
        self.cur_line = None

    def handle_starttag(self, tag, attrs):
        if self.skip_depth:
            if tag in SKIP:
                self.skip_depth += 1
            return
        if tag in SKIP:
            self.skip_depth = 1
            return
        if self.math_depth:
            if tag == "math":
                self.math_depth += 1
            return
        if tag == "math":
            alt = dict(attrs).get("alttext")
            self.emit(" $" + (alt if alt is not None else "?") + "$ ")
            self.math_depth = 1
            return
        if tag in ("td", "th"):
            self.emit(" | ")
            return
        if tag in BLOCK:
            self.flush()

    def handle_endtag(self, tag):
        if self.skip_depth:
            if tag in SKIP:
                self.skip_depth -= 1
            return
        if self.math_depth:
            if tag == "math":
                self.math_depth -= 1
            return
        if tag in BLOCK:
            self.flush()

    def handle_startendtag(self, tag, attrs):
        if tag == "br" and not self.math_depth and not self.skip_depth:
            self.flush()

    def handle_data(self, data):
        if self.skip_depth or self.math_depth:
            return
        self.emit(data)


def main() -> int:
    raw = open(SRC, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != SHA:
        print("SHA MISMATCH", sha)
        return 2
    p = Extractor()
    p.feed(raw.decode("utf-8"))
    p.close()
    p.flush()
    with open(OUT, "x", encoding="utf-8") as fh:
        fh.write(f"# extracted from {SRC}\n# sha256 {sha}\n")
        for ln, text in p.lines:
            fh.write(f"[L{ln}] {text}\n")
    print("lines", len(p.lines), "bytes_in", len(raw))
    return 0


if __name__ == "__main__":
    sys.exit(main())
