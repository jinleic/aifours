#!/usr/bin/env python3
"""Build positive and mutation control fixtures from the explicit families of
Abel-Costa-Finizio, Discrete Appl. Math. 143 (2004) 43-53, Section 3 (transcribed from
sources/acf2004-section3-excerpt.txt). Writes certificates in the strict verify_cdf.py format.

Positive fixtures:  controls/positive/acf2004_<v>.txt
Negative fixtures:  controls/negative/<v>_<mutation>.txt      (verifier must REJECT)
Preserving:         controls/preserving/<v>_<mutation>.txt    (verifier must ACCEPT)
Manifest:           controls/manifest.json (expected verdict and intended failing check per fixture)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "controls")

# --- Section 3.1, Type 1 (no multipliers). "(0:12;33;74;78)" in the reader text for 161 is read as (0,12,33,74,78).
TYPE1 = {
    81: [(0, 1, 5, 12, 26), (0, 2, 10, 40, 64), (0, 3, 18, 47, 53), (0, 9, 32, 48, 68)],
    121: [(0, 14, 26, 51, 60), (0, 15, 31, 55, 59), (0, 10, 23, 52, 58), (0, 3, 36, 56, 57), (0, 7, 18, 45, 50),
          (0, 8, 30, 47, 49)],
    141: [(0, 33, 60, 92, 97), (0, 3, 45, 88, 110), (0, 18, 39, 68, 139), (0, 12, 67, 75, 113), (0, 1, 15, 84, 94),
          (0, 7, 11, 24, 30), (0, 36, 90, 116, 125)],
    161: [(0, 19, 34, 73, 80), (0, 16, 44, 71, 79), (0, 12, 33, 74, 78), (0, 13, 30, 72, 77), (0, 11, 36, 67, 76),
          (0, 18, 32, 69, 75), (0, 10, 48, 68, 70), (0, 3, 29, 52, 53)],
    201: [(0, 1, 45, 98, 100), (0, 3, 32, 65, 89), (0, 4, 54, 70, 75), (0, 6, 49, 69, 91), (0, 7, 58, 81, 95),
          (0, 8, 34, 72, 90), (0, 9, 36, 77, 96), (0, 10, 35, 83, 94), (0, 12, 40, 79, 92), (0, 15, 46, 76, 93)],
    221: [(0, 1, 24, 61, 116), (0, 3, 46, 65, 113), (0, 4, 73, 89, 130), (0, 6, 39, 50, 118), (0, 7, 66, 81, 94),
          (0, 8, 38, 64, 139), (0, 9, 29, 80, 107), (0, 10, 35, 93, 135), (0, 12, 34, 52, 88), (0, 14, 31, 63, 84),
          (0, 5, 77, 122, 124)],
}

# --- Section 3.2, Type 2 (v = q^2): blocks times m^i, 0 <= i < (q-1)/2; "limited" blocks only times m^0..m^(lim-1).
TYPE2 = {
    361: dict(m=54, t=9, orbit=[(0, 1, 3, 19, 147), (0, 10, 75, 104, 236)], limited=[]),
    841: dict(m=14, t=14, orbit=[(0, 1, 17, 50, 85), (0, 43, 120, 354, 786), (0, 5, 66, 206, 588)], limited=[]),
    961: dict(m=235, t=15, orbit=[(0, 1, 7, 19, 45), (0, 24, 60, 230, 664), (0, 8, 47, 113, 867)],
              limited=[((1, 531, 388, 374, 628), 3)]),
}

# --- Section 3.3, Type 3: invariant blocks once; other blocks times m^y, 0 <= y < t.
TYPE3 = {
    341: dict(m=4, t=5, inv=[(1, 4, 16, 64, 256), (3, 12, 48, 192, 86)],
              orbit=[(0, 1, 18, 91, 157), (0, 26, 51, 169, 285), (0, 5, 40, 170, 284)]),
    781: dict(m=5, t=5, inv=[(1, 5, 25, 125, 625), (3, 15, 75, 375, 313), (8, 40, 200, 219, 314),
                             (23, 115, 575, 532, 317)],
              orbit=[(0, 1, 7, 10, 145), (0, 38, 134, 489, 628), (0, 11, 52, 217, 429), (0, 21, 49, 133, 534),
                     (0, 17, 65, 295, 649), (0, 22, 129, 288, 357), (0, 8, 26, 203, 399)]),
    261: dict(m=28, t=2, inv=[(0, 9, 45, 72, 162), (9, 63, 144, 29, 232), (9, 252, 58, 174, 145)],
              orbit=[(0, 1, 6, 22, 149), (0, 3, 26, 184, 208), (0, 17, 64, 178, 219), (0, 7, 57, 130, 249),
                     (0, 15, 52, 185, 228)]),
    561: dict(m=307, t=2, inv=[(0, 33, 77, 187, 385), (88, 253, 517, 51, 510), (11, 22, 253, 255, 306),
                               (297, 154, 209, 102, 459), (44, 264, 539, 153, 408), (22, 44, 143, 204, 357)],
              orbit=[(0, 205, 20, 60, 503), (0, 224, 225, 234, 309), (0, 81, 203, 208, 526),
                     (0, 368, 393, 464, 523), (0, 19, 211, 370, 433), (0, 216, 290, 410, 548),
                     (0, 56, 371, 398, 527), (0, 172, 285, 361, 532), (0, 83, 106, 426, 494),
                     (0, 152, 316, 453, 533), (0, 117, 166, 149, 553)]),
    381: dict(m=19, t=3, inv=[(0, 127, 1, 19, 361)],
              orbit=[(0, 2, 5, 79, 245), (0, 4, 26, 101, 199), (0, 25, 52, 137, 200), (0, 36, 66, 187, 331),
                     (0, 65, 114, 198, 285), (0, 8, 41, 130, 258)]),
    441: dict(m=67, t=3, inv=[(0, 147, 1, 67, 79)],
              orbit=[(0, 2, 5, 30, 113), (0, 6, 14, 141, 241), (0, 9, 59, 164, 266), (0, 10, 23, 87, 409),
                     (0, 18, 75, 262, 303), (0, 4, 49, 143, 252), (0, 22, 137, 297, 401)]),
    481: dict(m=211, t=3, inv=[],
              orbit=[(0, 1, 5, 40, 145), (0, 2, 22, 101, 203), (0, 10, 130, 309, 448), (0, 6, 15, 60, 222),
                     (0, 11, 88, 106, 237), (0, 19, 65, 136, 371), (0, 8, 49, 124, 160), (0, 14, 72, 209, 330)]),
    741: dict(m=178, t=3, inv=[(0, 247, 1, 178, 562)],
              orbit=[(0, 21, 51, 129, 188), (0, 111, 220, 435, 491), (0, 2, 89, 151, 688), (0, 4, 26, 102, 201),
                     (0, 125, 260, 416, 601), (0, 31, 65, 114, 236), (0, 58, 68, 139, 299),
                     (0, 105, 337, 360, 680), (0, 15, 163, 473, 646), (0, 48, 141, 264, 367),
                     (0, 90, 284, 519, 535), (0, 6, 19, 150, 244)]),
    921: dict(m=289, t=3, inv=[(0, 307, 1, 289, 631)],
              orbit=[(0, 145, 521, 713, 843), (0, 73, 233, 711, 879), (0, 21, 75, 131, 314),
                     (0, 256, 457, 595, 869), (0, 2, 195, 349, 677), (0, 152, 372, 463, 687),
                     (0, 10, 49, 252, 618), (0, 15, 65, 213, 456), (0, 5, 126, 539, 765), (0, 6, 302, 506, 547),
                     (0, 7, 278, 444, 868), (0, 19, 162, 186, 910), (0, 27, 859, 202, 434),
                     (0, 48, 84, 360, 833), (0, 64, 240, 398, 851)]),
    981: dict(m=499, t=3, inv=[(0, 327, 1, 499, 808)],
              orbit=[(0, 143, 546, 785, 878), (0, 66, 316, 746, 845), (0, 187, 263, 449, 667),
                     (0, 176, 220, 635, 929), (0, 3, 120, 451, 648), (0, 25, 75, 102, 206),
                     (0, 20, 49, 127, 507), (0, 33, 69, 122, 223), (0, 55, 168, 527, 765), (0, 7, 310, 525, 570),
                     (0, 9, 119, 362, 604), (0, 10, 193, 219, 291), (0, 11, 290, 423, 583),
                     (0, 15, 57, 364, 708), (0, 30, 231, 289, 542), (0, 18, 593, 773, 908)]),
}

# --- Theorem 12: (20t+3,5,1) OOC over Z_w missing +-x  ->  (7w,5,1) DF over Z_7 x Z_w ~ Z_7w (gcd(7,w)=1).
OOC = {
    23: dict(x=5, blocks=[(0, 1, 7, 9, 20)]),
    43: dict(x=21, blocks=[(0, 1, 5, 13, 15), (0, 3, 9, 20, 27)]),
    83: dict(x=34, blocks=[(0, 1, 3, 20, 75), (0, 4, 10, 37, 52), (0, 13, 18, 39, 71), (0, 14, 36, 43, 59)]),
    103: dict(x=49, blocks=[(0, 1, 3, 14, 20), (0, 5, 21, 29, 60), (0, 18, 46, 53, 91), (0, 23, 33, 67, 94),
                            (0, 15, 40, 62, 66)]),
    143: dict(x=38, blocks=[(0, 1, 3, 77, 119), (0, 6, 26, 34, 99), (0, 15, 45, 63, 102), (0, 4, 9, 55, 62),
                            (0, 12, 22, 35, 106), (0, 16, 47, 107, 126), (0, 14, 43, 54, 75)]),
}


def mult(block, m, v):
    return tuple((m * b) % v for b in block)


def expand_type2(v, d):
    out = []
    for blk in d["orbit"]:
        for i in range(d["t"]):
            out.append(mult(blk, pow(d["m"], i, v), v))
    for blk, lim in d["limited"]:
        for i in range(lim):
            out.append(mult(blk, pow(d["m"], i, v), v))
    return out


def expand_type3(v, d):
    out = list(d["inv"])
    for blk in d["orbit"]:
        for i in range(d["t"]):
            out.append(mult(blk, pow(d["m"], i, v), v))
    return out


def theorem12(w, d):
    v = 7 * w

    def crt(a7, aw):
        # unique z in Z_v with z = a7 (mod 7), z = aw (mod w)
        for z in range(aw % w, v, w):
            if z % 7 == a7 % 7:
                return z
        raise AssertionError("CRT failed")

    out = []
    for blk in d["blocks"]:
        a, b, c, dd, e = blk
        for z in range(1, 7):
            out.append(tuple(crt(i * z, val) for i, val in enumerate((a, b, c, dd, e))))
        out.append(tuple(crt(0, 2 * val) for val in blk))
    x = d["x"]
    out.append((crt(0, x), crt(0, -x), crt(1, 0), crt(2, 0), crt(4, 0)))
    return v, out


def render(v, k, blocks, header=None):
    head = header if header is not None else "CDF %d %d" % (v, k)
    return head + "\n" + "".join(" ".join(str(x) for x in blk) + "\n" for blk in blocks)


def mutations(v, blocks):
    """Yield (name, text, expected_verdict, intended_check)."""
    k = len(blocks[0])
    b = [list(x) for x in blocks]

    def changed():
        c = [list(x) for x in b]
        for delta in range(1, v):
            y = (c[0][2] + delta) % v
            if y not in c[0]:
                c[0][2] = y
                return c
        raise AssertionError

    def swapped():
        c = [list(x) for x in b]
        for i in range(1, k):
            for j in range(1, k):
                x, y = c[0][i], c[1][j]
                if x != y and y not in c[0] and x not in c[1]:
                    c[0][i], c[1][j] = y, x
                    return c
        raise AssertionError

    def dup_difference():
        c = [list(x) for x in b]
        c[1] = [(x + 1) % v for x in c[0]]
        return c

    yield "changed_element", render(v, k, changed()), "REJECT", "DPC"
    yield "swapped_elements", render(v, k, swapped()), "REJECT", "DPC"
    yield "duplicated_difference", render(v, k, dup_difference()), "REJECT", "DPC"
    yield "wrong_v_plus20", render(v, k, b, header="CDF %d %d" % (v + 20, k)), "REJECT", "F"
    yield "wrong_v_not1mod20", render(v, k, b, header="CDF %d %d" % (v - 1, k)), "REJECT", "F"
    c = [list(x) for x in b]
    c[0][1] = c[0][0]
    yield "duplicate_element", render(v, k, c), "REJECT", "F"
    c = [list(x) for x in b]
    c[0][1] = v
    yield "out_of_range", render(v, k, c), "REJECT", "F"
    yield "missing_block", render(v, k, b[:-1]), "REJECT", "F"
    yield "extra_block", render(v, k, b + [b[0]]), "REJECT", "F"
    yield "bad_header", render(v, k, b, header="CDF %d" % v), "REJECT", "F"
    yield "trailing_space", render(v, k, b).replace("\n", " \n", 2).replace(" \n", "\n", 1), "REJECT", "F"
    yield "crlf", render(v, k, b).replace("\n", "\r\n"), "REJECT", "F"
    base = render(v, k, b)
    lz = base.replace("\n0 ", "\n00 ", 1) if "\n0 " in base else base.replace("\n", "\n0", 1)
    yield "leading_zero", lz, "REJECT", "F"


def preserving(v, blocks):
    k = len(blocks[0])
    b = [list(x) for x in blocks]
    c = [list(x) for x in b]
    c[0] = [(x + 7) % v for x in c[0]]
    yield "translate_block", render(v, k, c), "ACCEPT", None
    c = [list(x) for x in b]
    c[1] = [(-x) % v for x in c[1]]
    yield "negate_block", render(v, k, c), "ACCEPT", None
    yield "reverse_block_order", render(v, k, b[::-1]), "ACCEPT", None
    yield "reverse_within_blocks", render(v, k, [x[::-1] for x in b]), "ACCEPT", None


def main():
    os.makedirs(os.path.join(OUT, "positive"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "negative"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "preserving"), exist_ok=True)
    families = {}
    for v, blks in TYPE1.items():
        families[v] = ("ACF2004 Sec3.1 Type 1", blks)
    for v, d in TYPE2.items():
        families[v] = ("ACF2004 Sec3.2 Type 2 m=%d" % d["m"], expand_type2(v, d))
    for v, d in TYPE3.items():
        families[v] = ("ACF2004 Sec3.3 order-%d multiplier m=%d" % (d["t"], d["m"]), expand_type3(v, d))
    for w, d in OOC.items():
        v, blks = theorem12(w, d)
        if v in families:
            families["%d_thm12" % v] = ("ACF2004 Thm12 from (%d,5,1) OOC, x=%d" % (w, d["x"]), blks)
        else:
            families[v] = ("ACF2004 Thm12 from (%d,5,1) OOC, x=%d" % (w, d["x"]), blks)
    manifest = []
    for key in sorted(families, key=lambda z: (int(str(z).split("_")[0]), str(z))):
        origin, blks = families[key]
        v = int(str(key).split("_")[0])
        name = "acf2004_%s.txt" % key
        path = os.path.join(OUT, "positive", name)
        with open(path, "w", newline="") as fh:
            fh.write(render(v, 5, blks))
        manifest.append(dict(file="positive/" + name, v=v, origin=origin, expect="ACCEPT", check=None))
    mutate_from = [81, 121, 141, 161, 201, 221, 261, 341, 381]
    for v in mutate_from:
        blks = families[v][1]
        for mname, text, expect, check in mutations(v, blks):
            name = "%d_%s.txt" % (v, mname)
            with open(os.path.join(OUT, "negative", name), "w", newline="") as fh:
                fh.write(text)
            manifest.append(dict(file="negative/" + name, v=v, origin="mutation of positive/acf2004_%d.txt" % v,
                                 expect=expect, check=check))
        for mname, text, expect, check in preserving(v, blks):
            name = "%d_%s.txt" % (v, mname)
            with open(os.path.join(OUT, "preserving", name), "w", newline="") as fh:
                fh.write(text)
            manifest.append(dict(file="preserving/" + name, v=v, origin="mutation of positive/acf2004_%d.txt" % v,
                                 expect=expect, check=check))
    with open(os.path.join(OUT, "manifest.json"), "w") as fh:
        json.dump(manifest, fh, indent=1)
    print("wrote %d fixtures" % len(manifest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
