#!/usr/bin/env python3
"""Append the justified p2222 symmetry break for two t14 witness profiles.

At every party degrees are643333 or553333 (the same chosen profile at all4).
P occurrence counts are6-d. The four common symbols2,3,4,5 each occur3 times.
The remaining symbols contribute only2 P occurrences per party: (0,2) or(1,1).
At most8 of the14 P words therefore use any noncommon symbol, so some P word
uses common symbols at all4 parties. Independent local permutations within
{2,3,4,5} preserve the degree profile and map that word to2222. Thus p2222 may
be imposed without excluding every representation of an admissible tensor.
This is a search symmetry only; no existence or exclusion claim.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    ap=argparse.ArgumentParser();ap.add_argument('cnf',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    meta_path=Path(str(a.cnf)+'.meta.json');meta=json.loads(meta_path.read_text())
    if meta['T']!=14 or len(meta['profiles'])!=4 or any(tuple(d) not in ((6,4,3,3,3,3),(5,5,3,3,3,3)) for d in meta['profiles']):
        raise ValueError('not a qualifying degree profile')
    if any(sum(6-d for d in profile[:2])!=2 for profile in meta['profiles']):raise ValueError('rare occurrence bound')
    var=1297+216*2+36*2+6*2+2
    h=hashlib.sha256()
    with a.cnf.open('rb') as src,a.out.open('xb') as dst:
        header=src.readline().decode().split()
        if header[:2]!=['p','cnf'] or len(header)!=4:raise ValueError('bad header')
        new=f'p cnf {header[2]} {int(header[3])+1}\n'.encode();dst.write(new);h.update(new)
        for chunk in iter(lambda:src.read(1024*1024),b''):dst.write(chunk);h.update(chunk)
        unit=f'{var} 0\n'.encode();dst.write(unit);h.update(unit)
    receipt={'input_sha256':hashlib.sha256(a.cnf.read_bytes()).hexdigest(),'output_sha256':h.hexdigest(),
      'added_unit':var,'word':[2,2,2,2],'maximal_words':14,'noncommon_symbol_P_incidences_bound':8,
      'common_only_P_words_lower_bound':6,'scope':'Sound local-permutation symmetry break for the two stated search profiles, not a theorem about all AME supports.'}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
