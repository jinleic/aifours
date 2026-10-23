"""Stream the addition clauses of ASCII LRAT as ASCII DRAT; ignore all deletion records and hints.

This program is NOT an LRAT verifier. Its output must be independently verified by drat-trim -I -U against
THE ORIGINAL CNF. If verified, the addition sequence itself is a valid RUP proof of that CNF, independently
of LRAT hint semantics. Keeping deleted clauses cannot invalidate a RUP consequence. No converted file is stored.
CLI: LRAT_FILE MAX_CNF_VARIABLE (stdout=ASCII additions; stderr=one JSON statistics line on success).
"""
import hashlib
import json
import sys


def main():
    path, nvar = sys.argv[1], int(sys.argv[2])
    lines = additions = deletions = negative_hint_lines = comments = 0
    src_hash, out_hash = hashlib.sha256(), hashlib.sha256()
    out = sys.stdout.buffer
    with open(path, 'rb') as f:
        for raw in f:
            src_hash.update(raw)
            lines += 1
            toks = raw.split()
            if not toks:
                continue
            if toks[0] == b'c':
                comments += 1
                continue
            if int(toks[0]) <= 0:
                raise ValueError('LRAT step id must be positive')
            if len(toks) > 1 and toks[1] == b'd':
                if toks[-1] != b'0' or any(int(x) <= 0 for x in toks[2:-1]):
                    raise ValueError('Malformed LRAT deletion record')
                deletions += 1
                continue
            stop = toks.index(b'0', 1)
            lits = [int(x) for x in toks[1:stop]]
            if any(x == 0 or abs(x) > nvar for x in lits):
                raise ValueError('LRAT clause literal outside original CNF variable range')
            hints = [int(x) for x in toks[stop + 1:]]
            if not hints or hints[-1] != 0 or any(x == 0 for x in hints[:-1]):
                raise ValueError('Malformed LRAT hint suffix')
            negative_hint_lines += int(any(x < 0 for x in hints[:-1]))
            payload = b' '.join(str(x).encode() for x in lits)
            payload = payload + b' 0\n' if lits else b'0\n'
            out.write(payload)
            out_hash.update(payload)
            additions += 1
    out.flush()
    print(json.dumps({'source_sha256': src_hash.hexdigest(), 'drat_additions_sha256': out_hash.hexdigest(),
                      'lines': lines, 'additions': additions, 'deletion_records_ignored': deletions,
                      'negative_hint_lines': negative_hint_lines, 'comments': comments}), file=sys.stderr)


if __name__ == '__main__':
    main()
