#!/usr/bin/env python3
"""Independently verify full 9-variable truth tables by direct character sums."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def parse_hex_seeds(path):
    result = []
    for line_number, raw in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError(f"line {line_number}: expected exactly 128 hexadecimal digits")
        result.append("".join(f"{int(c, 16):04b}" for c in line))
    if not result:
        raise ValueError("no truth tables in seed file")
    return result


def parse_candidate(path):
    payload = json.loads(path.read_text(encoding="utf-8"))
    bits = payload.get("bits")
    if not isinstance(bits, str) or len(bits) != N or set(bits) - {"0", "1"}:
        raise ValueError("candidate bits must be exactly 512 binary digits")
    return bits


def audit(bits, label):
    signs = [1 - 2 * int(bit) for bit in bits]
    direct = [
        sum(s * (1 - 2 * ((a & x).bit_count() & 1)) for x, s in enumerate(signs))
        for a in range(N)
    ]
    transform = signs.copy()
    stride = 1
    while stride < N:
        for start in range(0, N, 2 * stride):
            for index in range(start, start + stride):
                u, v = transform[index], transform[index + stride]
                transform[index], transform[index + stride] = u + v, u - v
        stride *= 2
    if direct != transform:
        raise RuntimeError(f"{label}: direct character sums disagree with FWHT")
    inverse = transform.copy()
    stride = 1
    while stride < N:
        for start in range(0, N, 2 * stride):
            for index in range(start, start + stride):
                u, v = inverse[index], inverse[index + stride]
                inverse[index], inverse[index + stride] = u + v, u - v
        stride *= 2
    if inverse != [N * s for s in signs]:
        raise RuntimeError(f"{label}: exact Boolean inverse mismatch")
    if sum(w * w for w in direct) != N * N:
        raise RuntimeError(f"{label}: Parseval identity mismatch")
    weight = bits.count("1")
    if direct[0] != N - 2 * weight:
        raise RuntimeError(f"{label}: W(0) and truth-table weight disagree")
    peak = max(abs(w) for w in direct)
    if peak % 2:
        raise RuntimeError(f"{label}: impossible odd Walsh coefficient")
    spectrum_bytes = (",".join(map(str, direct)) + "\n").encode("ascii")
    return {
        "label": label,
        "truth_sha256": hashlib.sha256(bits.encode("ascii")).hexdigest(),
        "weight": weight,
        "balanced": weight == N // 2,
        "walsh_zero": direct[0],
        "peak_abs_walsh": peak,
        "nonlinearity": N // 2 - peak // 2,
        "target_met": weight == N // 2 and peak <= 28,
        "zero_frequency_indices": [a for a, w in enumerate(direct) if w == 0],
        "absolute_walsh_histogram": dict(sorted(collections.Counter(map(abs, direct)).items())),
        "spectrum_sha256": hashlib.sha256(spectrum_bytes).hexdigest(),
        "walsh_values": direct,
        "independent_methods": ["direct-512-by-512-character-sums", "iterative-fwht"],
        "checked": ["full transform equality", "full exact inverse", "parseval", "weight vs W(0)"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--seed-file", type=Path)
    group.add_argument("--candidate", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.seed_file:
        tables = parse_hex_seeds(args.seed_file)
        reports = [audit(bits, f"published-seed-{i + 1}") for i, bits in enumerate(tables)]
        source = args.seed_file
    else:
        reports = [audit(parse_candidate(args.candidate), "candidate")]
        source = args.candidate
    result = {"input": str(source), "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "reports": reports}
    with args.output.open("x", encoding="utf-8") as output:
        json.dump(result, output, indent=2)
        output.write("\n")
    for report in reports:
        print(f"{report['label']}: weight={report['weight']} W0={report['walsh_zero']} "
              f"peak={report['peak_abs_walsh']} NL={report['nonlinearity']} "
              f"zeros={len(report['zero_frequency_indices'])} target={report['target_met']}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()
