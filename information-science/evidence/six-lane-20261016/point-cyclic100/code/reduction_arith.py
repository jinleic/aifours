#!/usr/bin/env python3
"""reduction_arith.py -- finite arithmetic controls for REDUCTION.md (v = 100). Controls of finite lemmas only; the
combinatorial proof is the written text. (E1, the exhaustive 4-subset stabilizer check of Lemma 2, is in e1_blocks.c.)

E2 (Lemma 3 / Corollary 4): all (h, m), h | 100, 0 <= m <= 25, satisfying (a) 100/h <= 33, (b) h | 25 - m,
   (c) m >= 1 => (100/h) m = 25.
E3 (Theorem A): 20 lies in H_h = <100/h> for every admissible h except h = 4; 20 is not a short-block difference.
E4 (Theorem B(3)): the m = 0 stabilizers h with 100/h <= 8 (classes outside O_S in type T2).
E5 (same chain at v = 52 and v = 64, consistency with the known cases): admissible (h, m) tables.
"""


def table(v):
    n, r = v // 4, (v - 1) // 3
    out = []
    for h in (d for d in range(1, v + 1) if v % d == 0):
        for m in range(0, n + 1):
            a = v // h <= r
            b = (n - m) % h == 0
            c = (m == 0) or ((v // h) * m == n)
            if a and b and c:
                out.append((h, m))
    return out


def main():
    H = {0, 25, 50, 75}
    t = table(100)
    print("E2 admissible (h, m) for v=100:", t)
    mixed = [(h, m) for h, m in t if m >= 1]
    print("E2 classes with short blocks:", mixed, "== [(4,1),(20,5),(100,25)]:", mixed == [(4, 1), (20, 5), (100, 25)])
    zero = sorted({h for h, m in t if m == 0})
    print("E2 stabilizers of classes without short blocks:", zero, "== [5, 25]:", zero == [5, 25])
    hs = sorted({h for h, m in t} - {4})
    print("E3 20 in H_h = <100/h> for h in", hs, ":", all(20 % (100 // h) == 0 for h in hs),
          "; 20 in H_4:", 20 % 25 == 0, "; short-block differences", sorted(H - {0}))
    print("E4 m=0 stabilizers with 100/h <= 8:", [h for h in zero if 100 // h <= 8])
    for w in (52, 64):
        print(f"E5 v={w} admissible (h, m):", table(w))


if __name__ == "__main__":
    main()
