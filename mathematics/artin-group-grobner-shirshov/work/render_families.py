"""Render an extracted family spec (work/specs_*.json) as a Markdown table.
Usage: python3 work/render_families.py work/specs_D4.json > evidence/certify/D4_families.md
"""
import json
import sys


def fmt(parts):
    out = []
    for w, p in parts:
        if p is None:
            out.append(w.replace("1", "Δ"))
        else:
            out.append(f"{w}^{{{p}}}")
    return " ".join(out) if out else "1"


def main():
    d = json.load(open(sys.argv[1]))
    typ = d["type"]
    print(f"# Reduced GS basis, type {typ[0]}{typ[1] or ''}, order {d['order']} (letters a<b<c<... in this order)")
    print()
    print(f"Delta = `{d['delta_word']}`, phi = {d['phi']}. All parameters k_i range over integers >= 0.")
    print("Plus the twist rules x Δ^{±1} -> Δ^{±1} φ(x) and the cancellations ΔΔ^{-1} -> 1, Δ^{-1}Δ -> 1.")
    print()
    print("| # | leading word | right side |")
    print("|---|---|---|")
    for f in d["families"]:
        print(f"| {f['name']} | `{fmt(f['lhs'])}` | `{fmt(f['rhs'])}` |")


if __name__ == "__main__":
    main()
