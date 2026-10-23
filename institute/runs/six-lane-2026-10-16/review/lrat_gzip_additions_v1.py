#!/usr/bin/env python3
"""Stream gzip ASCII-LRAT additions as ASCII DRAT; NOT an LRAT verifier.

Discard hints and deletions, retaining all addition clauses. Only the separate
pinned drat-trim -I -U verdict can establish UNSAT of the original CNF. Retaining
previous RUP consequences is sound. CLI: PROOF.lrat.gz MAX_CNF_VARIABLE.
"""
import gzip
import hashlib
import json
import sys


def main():
    path, maximum = sys.argv[1], int(sys.argv[2])
    additions = deletions = lines = 0
    raw_hash, addition_hash = hashlib.sha256(), hashlib.sha256()
    with gzip.open(path, "rb") as source:
        for raw in source:
            lines += 1
            raw_hash.update(raw)
            tokens = raw.split()
            if not tokens or tokens[0] == b"c":
                continue
            if int(tokens[0]) <= 0:
                raise ValueError("nonpositive step id")
            if len(tokens) > 1 and tokens[1] == b"d":
                if tokens[-1] != b"0" or any(int(v) <= 0 for v in tokens[2:-1]):
                    raise ValueError("malformed deletion record")
                deletions += 1
                continue
            stop = tokens.index(b"0", 1)
            literals = [int(v) for v in tokens[1:stop]]
            if any(v == 0 or abs(v) > maximum for v in literals):
                raise ValueError("literal outside original variable range")
            hints = [int(v) for v in tokens[stop + 1:]]
            if not hints or hints[-1] != 0 or any(v == 0 for v in hints[:-1]):
                raise ValueError("malformed hint suffix")
            row = b" ".join(str(v).encode() for v in literals)
            row = row + b" 0\n" if literals else b"0\n"
            sys.stdout.buffer.write(row)
            addition_hash.update(row)
            additions += 1
    sys.stdout.buffer.flush()
    print(json.dumps({"uncompressed_lrat_sha256": raw_hash.hexdigest(),
                      "addition_sha256": addition_hash.hexdigest(), "lines": lines,
                      "additions": additions, "deletions_discarded": deletions}), file=sys.stderr)


if __name__ == "__main__":
    main()
