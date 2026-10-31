#!/usr/bin/env python3
"""Bind and summarize the twelve completed projective F7 diagnostics."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('output',type=Path);args=ap.parse_args()
    root=args.root;items=[];total=0
    for C in range(4):
        for B in range(4):
            if C==B:continue
            name=('frontier-20261028-mixed-product-rank-search-f7-v1.json' if (C,B)==(0,1)
                  else f'frontier-20261028-mixed-product-rank-search-f7-c{C}b{B}-v1.json')
            path=root/name;record=json.loads(path.read_text())
            if (record['C'],record['B'],record['field'],record['sqrt2'],record['projective_vectors'],
                record['mixed_C_vectors_examined'],record['pairs_examined'],record['rank_at_most_one_found']) != (
                C,B,7,3,19608,19200,376473600,False):raise ValueError(f'bad receipt {name}')
            total+=record['pairs_examined'];items.append({'C':C,'B':B,'path':name,'sha256':digest(path)})
    if len(items)!=12 or total!=4517683200:raise ValueError('incomplete orientation coverage')
    result={'field':7,'sqrt2':3,'orientations':len(items),'total_projective_pairs':total,
            'rank_at_most_one_found':False,'orientation_receipts':items,
            'input_table_sha256_at_aggregation':digest(root/'frontier-20261028-pandya-table-v1.txt'),
            'search_cpp_sha256_at_aggregation':digest(root/'frontier-20261028-mixed-product-rank-search-v1.cpp'),
            'rank_control_receipt_sha256':digest(root/'frontier-20261028-mixed-rank-search-controls-v1.json'),
            'scope':'Finite F7 diagnostic only; no implication over C. Hashes at aggregation, not execution-time attestations.'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='orientation_receipts'},indent=2))


if __name__=='__main__':main()
