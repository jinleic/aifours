#!/usr/bin/env python3
"""Exact controls for SHARPER.md; no producer imports.

The finite table is exhaustive for the cap-28 residue/canonical domain. Real odd
hyperplane halves from the pinned NL240 corpus test the transform identities at
cap 32; no cap-28 odd pair is known, so they are not theorem witnesses.
"""
import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "inputs/slice-screen.json.gz"
PIN = "200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d"
MONOMIALS = [()] + [(i,) for i in range(8)] + list(itertools.combinations(range(8), 2))


def canonical(magnitude):
    if magnitude % 4 != 2:
        raise ValueError("odd-weight magnitude expected")
    return magnitude if magnitude % 8 == 2 else -magnitude


def residue(value):
    return ((value * value - 4) // 32) % 2


def transform(values):
    return [sum(value * (-1 if (a & x).bit_count() & 1 else 1) for a, value in enumerate(values))
            for x in range(len(values))]


def polar_rank(bits):
    coefficients = [0] * 37
    rows = []
    for point in range(256):
        row = 0
        for index, monomial in enumerate(MONOMIALS):
            if all((point >> i) & 1 for i in monomial):
                row |= 1 << index
        rows.append((row, bits[point]))
    pivots = []
    for row, bit in rows:
        for pivot_row, pivot_bit, pivot in pivots:
            if (row >> pivot) & 1:
                row ^= pivot_row
                bit ^= pivot_bit
        if row == 0:
            if bit:
                raise ValueError("function is not quadratic")
            continue
        pivot = row.bit_length() - 1
        pivots = [(r ^ row, b ^ bit, p) if (r >> pivot) & 1 else (r, b, p) for r, b, p in pivots]
        pivots.append((row, bit, pivot))
    for row, bit, pivot in pivots:
        coefficients[pivot] = bit
    matrix = [[0] * 8 for _ in range(8)]
    for index, monomial in enumerate(MONOMIALS):
        if len(monomial) == 2 and coefficients[index]:
            i, j = monomial
            matrix[i][j] = matrix[j][i] = 1
    rank, rows = 0, [sum(bit << col for col, bit in enumerate(row)) for row in matrix]
    for col in range(8):
        pivot = next((i for i in range(rank, 8) if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(8):
            if i != rank and (rows[i] >> col) & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def split(bits, normal):
    pivot = (normal & -normal).bit_length() - 1
    others = [i for i in range(9) if i != pivot]
    kernel = []
    for y in range(256):
        x = sum(((y >> j) & 1) << coordinate for j, coordinate in enumerate(others))
        if (x & normal).bit_count() & 1:
            x |= 1 << pivot
        kernel.append(x)
    return [bits[x] for x in kernel], [bits[x ^ (1 << pivot)] for x in kernel]


def spectrum(table):
    return transform([1 - 2 * bit for bit in table])


def phase_canonical(H):
    choices = []
    for sign in (1, -1):
        for shift in range(256):
            values = [sign * (-1 if (a & shift).bit_count() & 1 else 1) * h for a, h in enumerate(H)]
            if all(value % 8 == 2 for value in values):
                choices.append(values)
    if len(choices) != 1:
        raise ValueError("canonical phase is not unique")
    return choices[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corrupt-r-bound", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    rows = []
    for m, n in itertools.product(range(2, 27, 4), repeat=2):
        if m + n > 28:
            continue
        kg, kh = canonical(m), canonical(n)
        d = residue(kg) ^ residue(kh)
        s, r = kg + kh, kg - kh
        t = -s if d else s
        if s % 16 != (4 + 8 * d) % 16 or r % 16 != (8 * d) % 16:
            raise ValueError("residue congruence failed")
        if t not in (-28, -12, 4, 20) or t * t + 8 * t > 560:
            raise ValueError("signed sum majorant failed")
        r_bound = 255 if args.corrupt_r_bound else 256
        if r * r > r_bound + 320 * d:
            raise ValueError(f"difference majorant failed at {(m, n)}")
        rows.append({"m": m, "n": n, "D": d, "S": s, "R": r, "T": t})
    allowed = []
    for rank in range(0, 9, 2):
        r = rank // 2
        if rank == 0:
            weights = {0, 128, 256}
        elif rank == 8:
            # A nondegenerate form has no radical, hence no balanced radical-linear case.
            weights = {128 - (1 << (7 - r)), 128 + (1 << (7 - r))}
        else:
            weights = {128 - (1 << (7 - r)), 128, 128 + (1 << (7 - r))}
        for weight in sorted(weights):
            if 40 * weight >= 6656 - 512 * (1 << r):
                allowed.append([rank, weight])
    expected = [[0, 256], [2, 192], [4, 128], [4, 160], [6, 112], [6, 128], [6, 144], [8, 120], [8, 136]]
    if allowed != expected:
        raise ValueError(f"allowed type table mismatch: {allowed}")
    raw = INPUT.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PIN:
        raise ValueError("input pin mismatch")
    corpus = json.loads(gzip.decompress(raw))
    controls = []
    for source_index in (0, 37, 96, 123):
        source = corpus["sources"][source_index]
        bits = [int(c) for c in source["bits"]]
        normal = next(v for v in range(511, 0, -1) if (v & source["support_xor"]).bit_count() & 1)
        g, h = split(bits, normal)
        if sum(g) % 2 != 1 or sum(h) % 2 != 1:
            raise ValueError("control halves are not odd")
        G, H = spectrum(g), spectrum(h)
        Kg, Kh = phase_canonical(G), phase_canonical(H)
        if [abs(x) for x in Kg] != [abs(x) for x in G] or [abs(x) for x in Kh] != [abs(x) for x in H]:
            raise ValueError("canonical magnitude mismatch")
        D = [residue(a) ^ residue(b) for a, b in zip(Kg, Kh)]
        S = [a + b for a, b in zip(Kg, Kh)]
        R = [a - b for a, b in zip(Kg, Kh)]
        Shat, Rhat = transform(S), transform(R)
        if any(x not in (-512, 0, 512) for x in Shat + Rhat) or any((x == 0) == (y == 0) for x, y in zip(Shat, Rhat)):
            raise ValueError("canonical transform partition failed")
        if sum(x * x for x in S) + sum(x * x for x in R) != 262144:
            raise ValueError("parallelogram identity failed")
        signed = [1 - 2 * bit for bit in D]
        C = sum(a * b for a, b in zip(signed, S))
        walsh_D = transform(signed)
        if 256 * C != sum(a * b for a, b in zip(Shat, walsh_D)):
            raise ValueError("correlation identity failed")
        rank = polar_rank(D)
        l1 = sum(abs(x) for x in walsh_D)
        if l1 != 1 << (8 + rank // 2) or abs(C) > 2 * l1:
            raise ValueError("quadratic L1 bound failed")
        controls.append({"source": source_index, "normal": normal, "cap": max(abs(a) + abs(b) for a, b in zip(G, H)),
                         "rank": rank, "weight": sum(D), "C": C, "walsh_L1": l1})
    result = {"status": "PASS", "pair_rows": len(rows), "allowed_rank_weight": allowed,
              "real_cap32_identity_controls": controls, "input_sha256": PIN,
              "seconds": round(time.monotonic() - started, 3),
              "scope": "Exhaustive cap-28 pointwise domain and normal-form arithmetic, plus real odd-half identity controls. Universal theorem relies on SHARPER.md; no NL242 existence/nonexistence claim."}
    Path(__file__).with_name("sharper-audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
