#!/usr/bin/env python3
"""Fresh raw ordered-product DP for D_(2p) (rotation slice, 2026-10-18).

Convention (olson/proof-dihedral-partial.md Sec. 0): (v,e)(v',e') = (v + e v', e e'),
rho_x = (x,+1), sigma_y = (y,-1).  A word is a list of (kind, value), kind in {'r','s'}.
No window / GR / GRX formula is used here: the DP multiplies prefixes of increasing index
sets letter by letter.  States: (size, e) -> bitmask of v in Z_p.

has_identity(word, p, size)  -> bool : some increasing index set of the given size has
                                       ordered product (0,+1).
witness(word, p, size)       -> list of indices or None (backtracked, then re-multiplied).
product(word, idx, p)        -> (v, e) direct ordered product of the letters at idx.
"""
import sys


def _shift(mask, s, p, full):
    s %= p
    if s == 0:
        return mask
    return ((mask << s) | (mask >> (p - s))) & full


def _layers(word, p, size):
    full = (1 << p) - 1
    # reach[c][ei]: ei = 0 for e = +1, 1 for e = -1
    reach = [[0, 0] for _ in range(size + 1)]
    reach[0][0] = 1
    layers = [[row[:] for row in reach]]
    for kind, val in word:
        val %= p
        for c in range(min(size - 1, len(layers) - 1), -1, -1):
            for ei in (0, 1):
                m = reach[c][ei]
                if not m:
                    continue
                e = 1 if ei == 0 else -1
                moved = _shift(m, e * val, p, full)
                if kind == 'r':
                    reach[c + 1][ei] |= moved
                elif kind == 's':
                    reach[c + 1][1 - ei] |= moved
                else:
                    raise ValueError(kind)
        layers.append([row[:] for row in reach])
    return layers


def has_identity(word, p, size):
    return bool(_layers(word, p, size)[-1][size][0] & 1)


def product(word, idx, p):
    v, e = 0, 1
    for i in idx:
        kind, val = word[i]
        v = (v + e * val) % p
        if kind == 's':
            e = -e
    return v, e


def witness(word, p, size):
    layers = _layers(word, p, size)
    if not (layers[-1][size][0] & 1):
        return None
    # backtrack: state (c, ei, v) reachable after processing j letters
    c, ei, v = size, 0, 0
    idx = []
    for j in range(len(word), 0, -1):
        prev = layers[j - 1]
        if (prev[c][ei] >> v) & 1:
            continue  # reachable without letter j-1
        kind, val = word[j - 1]
        val %= p
        pei = ei if kind == 'r' else 1 - ei
        e = 1 if pei == 0 else -1
        pv = (v - e * val) % p
        assert c >= 1 and (prev[c - 1][pei] >> pv) & 1
        idx.append(j - 1)
        c, ei, v = c - 1, pei, pv
    assert c == 0 and ei == 0 and v == 0
    idx.reverse()
    assert len(idx) == size and product(word, idx, p) == (0, 1)
    return idx


def parse(text):
    """'r1 s0 s0 r6 ...' -> [('r',1),('s',0),('s',0),('r',6),...]"""
    out = []
    for tok in text.split():
        out.append((tok[0], int(tok[1:])))
    return out


def fmt(word):
    return ' '.join('%s%d' % (k, v) for k, v in word)


if __name__ == '__main__':
    p = int(sys.argv[1])
    w = parse(sys.argv[2])
    wit = witness(w, p, 2 * p)
    print('len', len(w), 'identity_2p_subword', wit is not None, 'witness', wit)
