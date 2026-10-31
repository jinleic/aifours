#!/usr/bin/env python3
"""Check the frozen nine-degree gcd-coloring certificate by integer arithmetic."""
import hashlib
import json
import math
import sys
from itertools import combinations

CERT_SHA256 = "e43fedc2b3662b72313e8c5294bc9befa2a9529bb0e5b938fa2a6fec674ad3cc"


def check_certificate(data):
    if set(data) != {"format", "rows"} or data["format"] != "small-alternating-index-gcd-coloring-v1":
        raise ValueError("format")
    rows = data["rows"]
    if len(rows) != 9 or [r["degree"] for r in rows] != list(range(5, 14)):
        raise ValueError("degree coverage")
    total_pairs = 0
    for row in rows:
        if set(row) != {"degree", "order", "classes"}:
            raise ValueError("row format")
        n, order, classes = row["degree"], row["order"], row["classes"]
        if type(order) is not int or order != math.factorial(n) // 2:
            raise ValueError("group order")
        if not 1 <= len(classes) <= 7 or any(not c for c in classes):
            raise ValueError("color count")
        expected = set()
        for d in range(1, math.isqrt(order) + 1):
            if order % d == 0:
                if d >= n:
                    expected.add(d)
                if order // d >= n:
                    expected.add(order // d)
        values = [v for c in classes for v in c]
        if any(type(v) is not int for v in values):
            raise ValueError("integer values")
        if len(set(values)) != len(values):
            raise ValueError("duplicate index")
        if set(values) != expected:
            raise ValueError("divisor coverage")
        pairs = 0
        for color in classes:
            for x, y in combinations(color, 2):
                pairs += 1
                if 2 <= math.gcd(x, y) <= 7:
                    raise ValueError("same-color gcd collision")
        total_pairs += pairs
        print(f"n={n} order={order} vertices={len(values)} colors={len(classes)} sizes={[len(c) for c in classes]} same_color_pairs={pairs}")
    print(f"PASS nine degrees; {total_pairs} same-color pairs")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: checker CERTIFICATE.json")
    with open(sys.argv[1], "rb") as f:
        raw = f.read()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != CERT_SHA256:
        raise SystemExit(f"SHA256 mismatch: {digest}")
    check_certificate(json.loads(raw))
    print(f"certificate SHA256={digest}")


if __name__ == "__main__":
    main()
