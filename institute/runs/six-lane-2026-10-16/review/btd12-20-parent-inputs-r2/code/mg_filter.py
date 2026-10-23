#!/usr/bin/env python3
"""mg_filter.py -- read nauty `multig -T` lines (nv ne {v1 v2 mult}) on stdin and keep the multigraphs whose vertex
degrees are all in {2, 4, 6} (README 1.3 (I2): a d-type vertex of degree delta gives two columns with delta ones, so
delta must be even and <= 6).  Writes the kept lines unchanged to stdout and a count line to stderr.  Stdlib only.
"""
import sys


def main():
    seen = kept = 0
    for line in sys.stdin:
        t = line.split()
        if not t:
            continue
        seen += 1
        nv, ne = int(t[0]), int(t[1])
        deg = [0] * nv
        tot = 0
        for q in range(ne):
            u, v, m = int(t[2 + 3 * q]), int(t[3 + 3 * q]), int(t[4 + 3 * q])
            deg[u] += m
            deg[v] += m
            tot += m
        if tot != 12:
            raise SystemExit(f"bad edge total {tot}: {line!r}")
        if all(d in (2, 4, 6) for d in deg):
            kept += 1
            sys.stdout.write(line)
    print(f"seen {seen} kept {kept}", file=sys.stderr)


if __name__ == "__main__":
    main()
