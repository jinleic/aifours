#!/usr/bin/env python3
"""Summarize the 12 complete projective F5 72-state searches."""
import argparse
import hashlib
import json
from pathlib import Path


def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    records=[];total=0
    for C in range(4):
        for B in range(4):
            if C==B:continue
            path=a.root/f'frontier-20261028-72state-rank-search-f5-c{C}b{B}-v1.json';r=json.loads(path.read_text())
            if (r['C'],r['B'],r['field'],r['i'],r['mode'],r['projective_vectors'],r['C_vectors_examined'],r['pairs_examined'],r['rank_at_most_one_found']) != (C,B,5,2,'all',3906,3906,15256836,False):raise ValueError(f'bad receipt {path}')
            total+=r['pairs_examined'];records.append({'C':C,'B':B,'path':path.name,'sha256':h(path)})
    if len(records)!=12 or total!=183082032:raise ValueError('incomplete search')
    result={'field':5,'i':2,'orientations':12,'total_projective_pairs':total,'rank_at_most_one_found':False,
      'receipts':records,'source_sha256_at_aggregation':h(a.root/'frontier-20261028-pandya-table-v1.txt'),
      'search_cpp_sha256_at_aggregation':h(a.root/'frontier-20261028-72state-rank-search-f5-v1.cpp'),
      'rank_control_receipt_sha256':h(a.root/'frontier-20261028-72state-rank-control-v1.json'),
      'scope':'One exact 72-state diagnostic over F5, not a complex proof; hashes observed at aggregation.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='receipts'},indent=2))


if __name__=='__main__':main()
