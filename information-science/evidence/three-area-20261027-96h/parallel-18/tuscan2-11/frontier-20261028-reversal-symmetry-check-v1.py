#!/usr/bin/env python3
"""Exact candidate-level check of all symbol/reversal automorphisms.

A symbol permutation mapping one entire source row to a chosen target row is
uniquely determined. Therefore n possible images of that row enumerate every
symbol automorphism, and likewise every symbol-plus-global-reversal map.
"""
import hashlib
import json
import sys
from pathlib import Path


def inspect(path):
    raw=path.read_bytes(); rows=json.loads(raw)['rows']; n=len(rows)
    if n<2 or any(len(r)!=n or sorted(r)!=list(range(n)) for r in rows):
        raise ValueError('invalid permutation array')
    events=[(r[i],r[i+1]) for r in rows for i in range(n-1)]
    if len(set(events))!=n*(n-1):
        raise ValueError('input lacks complete directed adjacency')
    rowset={tuple(r) for r in rows}
    if len(rowset)!=n:
        raise AssertionError('repeated row')
    def maps(reverse):
        trial=list(reversed(rows[0])) if reverse else rows[0]
        matches=[]
        for target in rows:
            relabel={trial[i]:target[i] for i in range(n)}
            transformed={tuple(relabel[v] for v in (reversed(row) if reverse else row)) for row in rows}
            if transformed==rowset:
                matches.append([relabel[v] for v in range(n)])
        return matches
    symbols,reverse=maps(False),maps(True)
    return {'source':str(path),'source_sha256':hashlib.sha256(raw).hexdigest(),
            'n':n,'candidate_maps_tested_per_kind':n,
            'symbol_automorphisms':symbols,'symbol_plus_reversal_automorphisms':reverse}


def main(argv):
    if len(argv)<3:
        raise ValueError('usage: SCRIPT OUTPUT.json INPUT.json [INPUT.json ...]')
    output=Path(argv[1]); checks=[inspect(Path(arg)) for arg in argv[2:]]
    result={'method':'map one full row to each possible target row, then check whole row set',
            'checks':checks,'scope':'The named finite inputs only; universal proof is written separately.'}
    with output.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main(sys.argv)
