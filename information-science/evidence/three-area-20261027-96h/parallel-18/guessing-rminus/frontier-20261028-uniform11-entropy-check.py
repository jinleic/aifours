#!/usr/bin/env python3
"""Exact integer comparisons used in the uniform support <=11 obstruction."""
from hashlib import sha256
from math import prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
GRAPH=('frontier-20261028-sparse-coloring-independent-result.json','5994e7fbec78f4fa864e713438e28d9676a107bf4a5e66df9044fe3103863eb4')
OUT=ROOT/'frontier-20261028-uniform11-entropy-check-result.json'


def ge(m,terms):
    if any(sum(block)!=m or c<=0 for c,block in terms):raise ValueError('PARTITION')
    total=sum(c for c,_ in terms)
    if 2*total<3:raise ValueError('EXPONENT')
    left=m**((2*total-3)*m)
    right=prod(prod(x**x for x in block if x)**(2*c) for c,block in terms)
    return left>=right,left>right


def main():
    raw=(ROOT/GRAPH[0]).read_bytes()
    if sha256(raw).hexdigest()!=GRAPH[1]:raise ValueError('GRAPH_HASH')
    graph=json.loads(raw)
    if not graph['all_checked'] or any(len(s)<6 for s in graph['noncolorable_vertex_sets']):raise ValueError('K4_FREE')
    results=[]
    def check(name,m,terms):
        ok,strict=ge(m,terms)
        if not ok:raise ValueError(('INEQUALITY',name))
        results.append({'name':name,'support_size':m,'terms':[{'coefficient':c,'block_sizes':list(b)} for c,b in terms],
                        'at_least_three_halves_joint_entropy':ok,'strict':strict})
    for m in range(2,10):check('ten_nonconstant',m,[(10,(1,m-1))])
    m=10;h=lambda k:(k,m-k)
    check('m10_two_exceptions',m,[(8,h(1)),(2,h(2))])
    check('m10_one_separator',m,[(9,h(1)),(1,h(3))])
    m=11;h=lambda k:(k,m-k)
    check('m11_four_exceptions',m,[(6,h(1)),(4,h(2))])
    check('m11_three_one_separator',m,[(7,h(1)),(2,h(2)),(1,h(3))])
    check('m11_two_two_separators',m,[(8,h(1)),(2,h(3))])
    check('m11_one_three_block_separator',m,[(9,h(1)),(1,(5,3,3))])
    check('m11_two_one_three_block_separator',m,[(8,h(1)),(1,h(2)),(1,(5,3,3))])
    mi={str(m):m**m>16*(m-1)**(m-1) for m in (10,11)}
    if not all(mi.values()):raise ValueError('MI_BLOCK2')
    if ge(10,[(10,(1,9))])[0]:raise ValueError('CONTROL_ACCEPTED')
    out={'graph_receipt_sha256':GRAPH[1],'exact_entropy_comparisons':results,'indicator_block2_strict_mi_obstruction':mi,
         'all_checked':True,'controls':{'m10_ten_minimum_entropy_alone':'rejected'},
         'limits':'Exact entropy comparisons and pinned K4-free graph check; partition/FD argument is separate written mathematics.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'entropy_comparison_count':len(results),'indicator_block2':mi,'all_checked':True,'controls':out['controls']},indent=2))


if __name__=='__main__':main()
