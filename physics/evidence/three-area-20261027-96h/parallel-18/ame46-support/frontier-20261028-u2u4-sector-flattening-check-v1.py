#!/usr/bin/env python3
"""Exact rank certificates for U(2)⊕U(4) sector decomposition of the 60-state."""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys


class CertificateError(ValueError):pass


def classify(tensor):
    p=[]; groups=collections.defaultdict(lambda:collections.defaultdict(dict))
    for coord,coeff in tensor.items():
        active=tuple(j for j,v in enumerate(coord) if v in (1,2))
        if len(active)==0:
            p.append(coord)
        elif len(active)==2:
            spectator=tuple(j for j in range(4) if j not in active)
            fixed=tuple(coord[j] for j in spectator)
            cell=tuple(coord[j]-1 for j in active)
            if cell in groups[active][fixed]:raise CertificateError('duplicate active cell')
            groups[active][fixed][cell]=coeff
        else:raise CertificateError('unexpected H-sector count')
    if len(p)!=12:raise CertificateError('P sector count mismatch')
    p_checks=[]
    for pair in itertools.combinations(range(4),2):
        other=tuple(j for j in range(4) if j not in pair)
        rows=[tuple(q[j] for j in pair) for q in p]
        cols=[tuple(q[j] for j in other) for q in p]
        if len(set(rows))!=12 or len(set(cols))!=12:
            raise CertificateError('P flattening not partial permutation')
        p_checks.append({'row_parties':pair,'rank':12,'nonzero_entries':12})
    e_checks=[]
    for pair in itertools.combinations(range(4),2):
        blocks=groups[pair]
        if len(blocks)!=4:raise CertificateError('E spectator block count mismatch')
        if len({v[0] for v in blocks})!=4 or len({v[1] for v in blocks})!=4:
            raise CertificateError('E spectator pairs not a matching')
        for fixed,entries in blocks.items():
            if len(entries)!=2 or len({i for i,j in entries})!=2 or len({j for i,j in entries})!=2:
                raise CertificateError('E active block not invertible partial permutation')
            if any(v not in ((1,0),(-1,0)) for v in entries.values()):
                raise CertificateError('E coefficient not nonzero signed unit')
        e_checks.append({'active_pair':pair,'spectator_pairs':sorted(blocks),
                         'invertible_2x2_blocks':4,'cross_flattening_rank':8,'source_nonzeros':8})
    return p_checks,e_checks


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('verifier',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    spec=importlib.util.spec_from_file_location('dense',a.verifier);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    tensor,sha=mod.load_table(a.table)
    ps,es=classify(tensor)
    mutant=dict(tensor);del mutant[(0,0,1,2)]
    try:classify(mutant)
    except CertificateError as exc:
        if str(exc)!='E active block not invertible partial permutation':raise
        negative=str(exc)
    else:raise CertificateError('deleted-coefficient mutation accepted')
    result={'table_sha256':sha,'P_flattenings':ps,'E_sector_flattenings':es,
            'sum_of_sector_rank_bounds':12+6*8,
            'deleted_E_coefficient_control':negative,
            'scope':'Exact support/rank certificate for the published state, not an all-state lower bound.'}
    with a.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
