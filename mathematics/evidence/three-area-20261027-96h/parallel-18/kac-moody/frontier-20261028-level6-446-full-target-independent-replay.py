#!/usr/bin/env python3
"""Independently replay ALL 446 target rows via tensor-suffix lowering.

The producer uses independent matrix-unit bracket trees. This replay uses
Levi producer's tensor-word suffix lowering, assembled per Lyndon column.
Source horizontal completeness is a separate already pinned stage.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('levi',ROOT/'frontier-20261028-levi-lie-engine.py')
levi=importlib.util.module_from_spec(spec);spec.loader.exec_module(levi)


def main():
    a=(ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json').read_bytes()
    b=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    assert hashlib.sha256(a).hexdigest()=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    assert hashlib.sha256(b).hexdigest()=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(a);F=json.loads(b);words=P['source_words'];coeff=P['horizontal_kernel_coefficients'];k=len(coeff)
    source=levi.lie_basis((4,4,6));assert [''.join(map(str,w)) for w,_ in source]==words and len(words)==1116 and k==162
    incidence=[[] for _ in words]
    for j,c in enumerate(coeff):
        for i,q in c.items():incidence[int(i)].append((j,Q(q)))
    actual={}
    for i,(word,v) in enumerate(source):
        if not incidence[i]:continue
        E=levi.lower3(v,0,0);R=levi.lower3(v,1,0);S=levi.lower3(v,0,1)
        for w in set(E)|set(R)|set(S):
            e,r,s=Q(E.get(w,0)),Q(R.get(w,0)),Q(S.get(w,0));l=r+s-2*e;z=r-s
            if not (e or l or z):continue
            wstr=''.join(map(str,w));area=actual.setdefault(wstr,{})
            for j,c in incidence[i]:
                q=area.setdefault(j,[Q(0),Q(0),Q(0)]);q[0]+=c*l;q[1]+=c*z;q[2]+=c*e
    actual={w:{j:v for j,v in rows.items() if any(v)} for w,rows in actual.items()}
    actual={w:rows for w,rows in actual.items() if rows}
    expected={row['word']:{e['column']:[Q(e['L']),Q(e['K']),Q(e['E'])] for e in row['entries']} for row in F['rows']}
    assert actual==expected and len(actual)==F['target_row_count']==1780
    triples=sum(len(row) for row in actual.values());assert triples==F['nonzero_triple_count']==263594
    out=ROOT/'frontier-20261028-level6-446-full-target-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degree':[4,4,6],'source_words':len(words),'lowest_source_vectors':k,
                               'target_rows':len(actual),'nonzero_L_K_E_triples':triples,
                               'all_full_target_entries_match':True,'producer':'tree-Jacobi','replay':'tensor-suffix Jacobi',
                               'status':'PASS_FULL_TARGET_TREE_VERSUS_SUFFIX',
                               'scope':'conditional on recorded source basis and full Cartan/PBW; no positivity or full-map kernel claim'},indent=2)+'\n')
    print('PASS full446 target: 1780 rows/162 columns/263594 nonzero L-K-E triples tree vs suffix;',out.name,flush=True)

if __name__=='__main__':main()
