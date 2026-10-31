#!/usr/bin/env python3
"""ReviewF179RminusExact: mechanical extraction of the Fig. 2 (printed p570) graph of the
publisher PDF from its vector drawing (pdftocairo SVG of page 18) plus label positions
(pdftohtml -xml of page 18).  Own reviewer code; reads only files rendered by the
reviewer from the hash-pinned publisher PDF.  Prints a JSON receipt.

Reading rules (stated, not inferred from any author file):
  * node = white-filled black-stroked closed path made of 4 cubic segments (TikZ circle);
    centre = mean of the 4 segment end points;
  * label = the digit text box (pdftohtml coordinates / 1.5) nearest to the node centre;
    the assignment must be a bijection (each node's nearest label is unique and mutual);
  * open black stroke path (M..L or M..C): edge between the nodes nearest its two end
    points, each end point within END_TOL of a node centre;
  * closed black polygon (M L L Z): each side is split at every node centre lying within
    SIDE_TOL of the side, consecutive nodes along the side are joined (a node drawn on
    a straight line splits it);
  * white strokes are invisible and contribute no edge (recorded separately).
"""
import hashlib
import json
import re
import sys

DIR = "/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f179-rminus-fresh-exact-certificate/"
SVG = DIR + "ReviewF179RminusExact-publisher-page18.svg"
XML = DIR + "ReviewF179RminusExact-publisher-page18-text.xml"
END_TOL = 2.6
SIDE_TOL = 0.6

HAND = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 7), (2, 9), (2, 10),
        (3, 4), (3, 8), (3, 9), (4, 5), (4, 8), (4, 10), (5, 6), (5, 9), (5, 10), (6, 7),
        (6, 8), (6, 9), (7, 8), (7, 10), (8, 9), (8, 10)]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def attr(tag, name):
    m = re.search(name + r'="([^"]*)"', tag)
    return m.group(1) if m else None


def main():
    svg = open(SVG).read()
    tags = re.findall(r"<path[^>]*>", svg)
    figT = "matrix(0.999096, 0, 0, -0.999096, 245.936549, 180.240056)"
    nodes, opens, polys, white = [], [], [], []
    for t in tags:
        if attr(t, "stroke") is None or attr(t, "transform") != figT:
            continue
        d = attr(t, "d")
        toks = re.findall(r"[MLCZ]|-?[0-9.]+(?:e-?[0-9]+)?", d)
        cmds, pts, cur = [], [], None
        i = 0
        while i < len(toks):
            c = toks[i]
            if c in "MLCZ":
                cur = c
                i += 1
                if c == "Z":
                    cmds.append(("Z", []))
                    continue
            n = {"M": 1, "L": 1, "C": 3}[cur]
            xy = [(float(toks[i + 2 * k]), float(toks[i + 2 * k + 1])) for k in range(n)]
            i += 2 * n
            cmds.append((cur, xy))
        col = attr(t, "stroke")
        fill = attr(t, "fill")
        kinds = "".join(c for c, _ in cmds)
        if fill == "rgb(100%, 100%, 100%)" and kinds.startswith("MCCCCZ"):
            ends = [xy[-1] for c, xy in cmds if c == "C"]
            nodes.append((sum(p[0] for p in ends) / 4, sum(p[1] for p in ends) / 4))
        elif col == "rgb(100%, 100%, 100%)":
            white.append(kinds)
        elif "Z" in kinds:
            polys.append([xy[-1] for c, xy in cmds if c in "ML"])
        else:
            opens.append((cmds[0][1][-1], cmds[-1][1][-1], kinds))
    # labels
    xml = open(XML).read()
    labels = []
    for m in re.finditer(r'<text top="(\d+)" left="(\d+)" width="(\d+)" height="(\d+)" font="0">(\d+)</text>', xml):
        top, left, w, h, s = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5)
        labels.append((s, ((left + w / 2) / 1.5, (top + h / 2) / 1.5)))
    fig_labels = [(s, p) for s, p in labels if s in {str(k) for k in range(1, 11)} and 80 < p[1] < 240]

    def page(p):
        return (245.936549 + 0.999096 * p[0], 180.240056 - 0.999096 * p[1])

    def d2(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    lab = {}
    for k, c in enumerate(nodes):
        pc = page(c)
        best = min(fig_labels, key=lambda sp: d2(sp[1], pc))
        back = min(range(len(nodes)), key=lambda j: d2(page(nodes[j]), best[1]))
        if back != k:
            raise SystemExit("label assignment not mutual")
        lab[k] = int(best[0])
    if sorted(lab.values()) != list(range(1, 11)):
        raise SystemExit("label bijection failed: %r" % lab)

    def near(p):
        k = min(range(len(nodes)), key=lambda j: d2(nodes[j], p))
        return k, d2(nodes[k], p) ** 0.5

    edges = set()
    for a, b, kinds in opens:
        ka, da = near(a)
        kb, db = near(b)
        if da > END_TOL or db > END_TOL or ka == kb:
            raise SystemExit("open path end not at a node: %r %r" % (a, b))
        edges.add(tuple(sorted((lab[ka], lab[kb]))))
    poly_edges = []
    for poly in polys:
        # pdftocairo closes with "Z M p0": drop vertices repeating the previous/first one
        poly = [v for i, v in enumerate(poly) if i == 0 or (v != poly[i - 1] and v != poly[0])]
        verts = poly + [poly[0]]
        for s in range(len(poly)):
            p, q = verts[s], verts[s + 1]
            on = []
            for k, c in enumerate(nodes):
                vx, vy = q[0] - p[0], q[1] - p[1]
                tpar = ((c[0] - p[0]) * vx + (c[1] - p[1]) * vy) / (vx * vx + vy * vy)
                proj = (p[0] + tpar * vx, p[1] + tpar * vy)
                if -0.02 <= tpar <= 1.02 and d2(proj, c) ** 0.5 <= SIDE_TOL:
                    on.append((tpar, k))
            on.sort()
            for (t1, k1), (t2, k2) in zip(on, on[1:]):
                e = tuple(sorted((lab[k1], lab[k2])))
                poly_edges.append(e)
                edges.add(e)
    hand = set(HAND)
    out = {
        "svg_sha256": sha(SVG),
        "xml_sha256": sha(XML),
        "nodes": {lab[k]: [round(c[0], 3), round(c[1], 3)] for k, c in enumerate(nodes)},
        "open_black_paths": len(opens),
        "closed_black_polygons": len(polys),
        "polygon_edges": sorted(poly_edges),
        "white_stroke_paths": white,
        "extracted_edges": sorted(edges),
        "extracted_edge_count": len(edges),
        "equals_hand_transcription": edges == hand,
        "missing_vs_hand": sorted(hand - edges),
        "extra_vs_hand": sorted(edges - hand),
        "edge_9_10_present": (9, 10) in edges,
        "edge_3_4_present": (3, 4) in edges,
    }
    print(json.dumps(out, sort_keys=True))
    return 0 if edges == hand else 1


if __name__ == "__main__":
    sys.exit(main())
