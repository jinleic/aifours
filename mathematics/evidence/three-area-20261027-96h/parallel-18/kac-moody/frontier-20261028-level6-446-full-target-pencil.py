#!/usr/bin/env python3
"""Reconstruct EVERY nonzero target word row of the level-six 446 pencil.

Independent tree-Jacobi is evaluated once per source Lyndon word, then the
actual 162 lowest source coefficients are assembled.  This is not itself an
injectivity or positive-form assertion.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    raw=(ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    P=json.loads(raw);words=P['source_words'];k=len(P['horizontal_kernel_coefficients'])
    assert len(words)==1116 and k==162 and tuple(words)==ind.lyndon_words((4,4,6))
    out=ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json'
    if out.exists():raise FileExistsError(out)
    incidence=[[] for _ in words]
    for j,c in enumerate(P['horizontal_kernel_coefficients']):
        for i,q in c.items():incidence[int(i)].append((j,Q(q)))
    rows={}
    for idx,w in enumerate(words):
        if not incidence[idx]:continue
        e=ind.tree_d3(w,0,0);rx=ind.tree_d3(w,1,0);sy=ind.tree_d3(w,0,1)
        for target in set(e)|set(rx)|set(sy):
            a=Q(e.get(target,0));b=Q(rx.get(target,0));c=Q(sy.get(target,0));lv=b+c-2*a;kv=b-c
            if not (a or lv or kv):continue
            area=rows.setdefault(target,{})
            for j,scale in incidence[idx]:
                entry=area.setdefault(j,[Q(0),Q(0),Q(0)])
                entry[0]+=scale*lv;entry[1]+=scale*kv;entry[2]+=scale*a
    records=[]
    for w,area in sorted(rows.items()):
        entries=[{'column':j,'L':str(v[0]),'K':str(v[1]),'E':str(v[2])} for j,v in sorted(area.items()) if any(v)]
        if entries:records.append({'word':w,'entries':entries})
    assert len({row['word'] for row in records})==len(records)
    result={'degree':[4,4,6],'source_data_sha256':digest,'source_dim':1116,'whole_lowest_dim':k,
            'formal_coefficients':'D=tL+dK+E, r=t+d,s=t-d',
            'target_row_count':len(records),'nonzero_triple_count':sum(len(row['entries']) for row in records),
            'rows':records,'status':'ALL_NONZERO_TREE_JACOBI_TARGET_ROWS_RECONSTRUCTED',
            'scope':'current free-Levi source; source/ideal and rank proof separate; no global claim'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE full446 target rows',len(records),'source columns',k,'nonzero triples',result['nonzero_triple_count'],out.name,flush=True)

if __name__=='__main__':main()
