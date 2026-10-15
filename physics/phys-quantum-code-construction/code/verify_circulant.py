#!/usr/bin/env python3
"""Independent full-graph clique replay plus exact Hilbert-space anchor checks.

Does not import the search implementation. Set-valued graph neighborhoods and
NetworkX maximal cliques replace its bitset recursion. The constructed anchor
is additionally checked using integer computational-basis amplitudes.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from itertools import combinations, product
from pathlib import Path
import json
import numpy as np
import networkx as nx

ROOT=Path(__file__).resolve().parents[1]
N=11


def errors(weight):
    for support in combinations(range(N),weight):
        for local in product('XYZ',repeat=weight):
            yield {j:p for j,p in zip(support,local)}


def syndrome(err,neighborhoods):
    support=set()
    x_support=set()
    for j,p in err.items():
        if p in ('X','Y'):
            support.symmetric_difference_update(neighborhoods[j])
            x_support.add(j)
        if p in ('Z','Y'):
            support.symmetric_difference_update({j})
    return sum(2**j for j in support),x_support


def cws_detects(err,words,neighborhoods):
    induced,x_support=syndrome(err,neighborhoods)
    if induced:
        return not any((a^b)==induced for a,b in combinations(words,2))
    values={sum((word>>j)&1 for j in x_support)%2 for word in words}
    return len(values)<=1


def direct_anchor(words,neighborhoods):
    """All amplitudes are integers divided by sqrt(2048); no floating arithmetic."""
    size=2**N
    indices=np.arange(size,dtype=np.int64)
    parity=np.array([i.bit_count()%2 for i in range(size)],dtype=np.int64)
    edges=[(i,j) for i in range(N) for j in neighborhoods[i] if i<j]
    exponents=np.array([sum(((s>>i)&1)*((s>>j)&1) for i,j in edges)%2 for s in range(size)],dtype=np.int64)
    V=np.column_stack([1-2*((exponents+parity[indices&word])%2) for word in words])
    assert np.array_equal(V.T@V,size*np.eye(len(words),dtype=np.int64))
    def compress(err):
        x=sum(2**j for j,p in err.items() if p in ('X','Y'))
        z=sum(2**j for j,p in err.items() if p in ('Z','Y'))
        signs=1-2*parity[indices&z]
        return V[indices^x].T@(signs[:,None]*V)
    def scalar(matrix):
        return np.array_equal(matrix,int(matrix[0,0])*np.eye(len(words),dtype=np.int64))
    count=0
    for weight in range(4):
        for err in errors(weight):
            assert scalar(compress(err)),err
            count+=1
    witness=None
    for err in errors(4):
        if not cws_detects(err,words,neighborhoods):
            witness=err
            break
    assert witness is not None
    matrix=compress(witness)
    assert not scalar(matrix)
    return {'integer_gram_diagonal':size,'paulis_below_distance_checked':count,'distance':4,
            'weight_four_witness':''.join(witness.get(j,'I') for j in range(N)),
            'unnormalized_witness_compression':matrix.tolist()}


def run():
    data=json.loads((ROOT/'results/circulant-11-5-4.json').read_text())
    assert (data['n'],data['distance'],data['target_K'],data['graph_frames'])==(11,4,5,32)
    assert len(data['records'])==32
    assert [r['connection_mask'] for r in data['records']]==list(range(32))
    low_errors=[err for w in range(1,4) for err in errors(w)]
    assert len(low_errors)==4983
    maxima=[]
    first_anchor=None
    for mask,record in enumerate(data['records']):
        offsets={j+1 for j in range(5) if mask//(2**j)%2}
        neighborhoods=[{(i+delta)%N for j in offsets for delta in (j,-j)} for i in range(N)]
        assert record['offsets']==sorted(offsets)
        assert record['adjacency_rows']==[sum(2**j for j in nbrs) for nbrs in neighborhoods]
        prohibited=set()
        zero_x=[]
        for err in low_errors:
            induced,x_support=syndrome(err,neighborhoods)
            if induced:
                prohibited.add(induced)
            else:
                zero_x.append(x_support)
        valid=[c for c in range(1,2**N) if c not in prohibited and
               all(sum((c>>j)&1 for j in supp)%2==0 for supp in zero_x)]
        assert valid==record['allowed_words']
        graph=nx.Graph()
        graph.add_nodes_from(valid)
        graph.add_edges_from((a,b) for a,b in combinations(valid,2) if a^b not in prohibited)
        max_clique=max((len(clique) for clique in nx.find_cliques(graph)),default=0)
        assert max_clique<=3
        assert record['target_five_words'] is None
        maxima.append(max_clique)
        words=record['control_four_words']
        if words is not None:
            assert len(words)==len(set(words))==4 and 0 in words
            assert all(cws_detects(err,words,neighborhoods) for err in low_errors)
            if first_anchor is None:
                first_anchor=(record,neighborhoods)
    assert first_anchor is not None
    record,neighborhoods=first_anchor
    words=record['control_four_words']
    assert not cws_detects({0:'Z'},[0,1],neighborhoods)
    direct=direct_anchor(words,neighborhoods)
    witness={'n':11,'K':4,'distance':4,'graph_edges':[[i,j] for i in range(N) for j in neighborhoods[i] if i<j],
             'word_labels':words,'bit_order':'Qubit j is integer bit j.',
             'state_formula':'|c> = 2^(-11/2) sum_s (-1)^(sum_{edges ij} s_i*s_j + sum_j c_j*s_j) |s>',
             'origin':'First positive control in the fixed circulant-family assay; no improvement over the known K=4 baseline.',
             'distance_witness':direct['weight_four_witness']}
    (ROOT/'results/circulant-11-4-4-anchor.json').write_text(json.dumps(witness,indent=2)+'\n')
    report={'graph_frames':32,'all_word_sets_covered':True,'K5_frames':0,
            'K4_frames':sum(m==3 for m in maxima),'maximum_nonzero_clique_sizes':maxima,
            'independent_clique_implementation':'networkx.find_cliques (not search bitset recursion)',
            'anchor_cws_minimum_distance':4,'anchor_direct_integer_check':direct,
            'negative_controls_rejected':1,'scope':'Only circulant graph-state frames; vertex-transitive extension is an analytic group-theoretic argument.'}
    assert report['K4_frames']==data['control_hits']==20 and data['target_hits']==0
    (ROOT/'results/circulant-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: all 32 circulant frames independently reconstructed; no K=5, and 20 K=4 frames.')
    print('PASS: ((11,4,4)) control by CWS checks and 4984 integer state-vector compressions plus weight-4 witness.')
    return report


if __name__=='__main__':
    run()
