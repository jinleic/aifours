#!/usr/bin/env python3
"""Exact independent replay: Fraction LP, Pauli algebra, integer amplitudes, CWS.

No numerical optimization is trusted. A passing LP witness is explicitly not
promoted to a code. The graph-atlas assay is redundant with the analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import copy
import hashlib
import json
import platform
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
N = 7


def load(name):
    return json.loads((ROOT/'results'/name).read_text())


def transform_column(i):
    """Coefficients of (x+3y)^(7-i)(x-y)^i by polynomial multiplication."""
    coeff = [1]
    for slope in [3]*(N-i)+[-1]*i:
        nxt = [0]*(len(coeff)+1)
        for j, value in enumerate(coeff):
            nxt[j] += value
            nxt[j+1] += slope*value
        coeff = nxt
    return coeff


def transforms(a, K):
    coeffs = [transform_column(i) for i in range(N+1)]
    b = [F(K,2**N)*sum(coeffs[i][j]*a[i] for i in range(N+1)) for j in range(N+1)]
    s = [F(1,2**N)*sum((-1)**i*coeffs[i][j]*a[i] for i in range(N+1)) for j in range(N+1)]
    return b,s


def primal_ok(a, K=3):
    b,s=transforms(a,K)
    return (a[0]==1 and min(a)>=0 and min(s)>=0 and
            all(b[j]==a[j] for j in range(3)) and
            all(b[j]>=a[j] for j in range(3,N+1)))


def farkas_ok(cert):
    assert (cert['n'],cert['K'],cert['d']) == (7,4,3)
    cols=[transform_column(i) for i in range(N+1)]
    rows={}
    for j in range(N+1):
        rows[f'a_{j}']=[F(int(i==j)) for i in range(N+1)]
        rows[f'KB_{j}-A_{j}']=[F(4*cols[i][j]-128*int(i==j)) for i in range(N+1)]
        rows[f'shadow_{j}']=[F((-1)**i*cols[i][j]) for i in range(N+1)]
    total=[F(0)]*(N+1)
    for label,value in cert['nonnegative_multipliers'].items():
        value=F(value)
        if value<0 or (label.startswith('KB_') and int(label.split('_')[1].split('-')[0])<3):
            return False
        for i in range(N+1):
            total[i]+=value*rows[label][i]
    constant=F(0)
    for label,value in cert['equality_multipliers'].items():
        value=F(value)
        if label=='a_0=1':
            constant+=value
            total[0]+=value
        else:
            label=label.removesuffix('=0')
            if label not in [f'KB_{j}-A_{j}' for j in range(3)]:
                return False
            for i in range(N+1):
                total[i]+=value*rows[label][i]
    return not any(total) and constant==1


def verify_lp():
    cert=load('lp-feasible-7-3-3.json')
    assert (cert['n'],cert['K'],cert['d']) == (7,3,3)
    a=list(map(F,cert['a']))
    assert len(a)==8 and primal_ok(a)
    b,s=transforms(a,3)
    dual=load('lp-infeasible-7-4-3.json')
    assert farkas_ok(dual)
    broken=a.copy()
    broken[4]+=1
    assert not primal_ok(broken)
    broken_dual=copy.deepcopy(dual)
    broken_dual['nonnegative_multipliers']['a_1']='5'
    assert not farkas_ok(broken_dual)
    return {'K3_a':list(map(str,a)), 'K3_b':list(map(str,b)), 'K3_shadow':list(map(str,s)),
            'K4_farkas_identity':'0 >= 1', 'negative_controls_rejected':2}


def as_masks(word):
    return (sum(1<<j for j,p in enumerate(word) if p in 'XY'),
            sum(1<<j for j,p in enumerate(word) if p in 'ZY'))


def symplectic_distance(code):
    generators=[as_masks(word) for word in code['stabilizer_generators']]
    assert all(((x&v).bit_count()+(z&u).bit_count())%2==0
               for x,z in generators for u,v in generators)
    span={(0,0)}
    for x,z in generators:
        span |= {(u^x,v^z) for u,v in list(span)}
    assert len(span)==64
    assert code['K']==2**N//len(span)
    minimum=N+1
    distribution=[0]*(N+1)
    for x in range(2**N):
        for z in range(2**N):
            if (x,z) not in span and all(((x&v).bit_count()+(z&u).bit_count())%2==0 for u,v in generators):
                w=(x|z).bit_count()
                distribution[w]+=1
                minimum=min(minimum,w)
    assert minimum==code['distance']==3
    return {'paulis_enumerated':4**N,'stabilizer_size':len(span),
            'normalizer_minus_stabilizer_weight_counts':distribution,'distance':minimum}


def act(word, state):
    """Integer signed permutation, Y represented by XZ (global phase omitted)."""
    out=[0]*(2**N)
    for basis,amplitude in enumerate(state):
        if not amplitude:
            continue
        target=basis
        sign=1
        for j,pauli in enumerate(word):
            bit=(basis>>j)&1
            if pauli in ('Z','Y') and bit:
                sign=-sign
            if pauli in ('X','Y'):
                target ^= 1<<j
        out[target]+=sign*amplitude
    return out


def compression(word, states):
    return [[sum(a*b for a,b in zip(left,act(word,right)))
             for right in states] for left in states]


def scalar_matrix(matrix):
    return all(matrix[i][j]==(matrix[0][0] if i==j else 0)
               for i in range(len(matrix)) for j in range(len(matrix)))


def words_of_weight(w):
    for support in combinations(range(N),w):
        for labels in product('XYZ',repeat=w):
            word=['I']*N
            for j,label in zip(support,labels):
                word[j]=label
            yield ''.join(word)


def vector_distance(code):
    states=[[int(i in supp) for i in range(2**N)] for supp in code['basis_supports']]
    assert len(states)==2
    gram=[[sum(x*y for x,y in zip(a,b)) for b in states] for a in states]
    assert gram==[[8,0],[0,8]]
    for generator,eigenvalue in zip(code['stabilizer_generators'],code['generator_eigenvalues']):
        for state in states:
            assert act(generator,state)==[eigenvalue*x for x in state]
    tested=0
    for w in range(3):
        for word in words_of_weight(w):
            assert scalar_matrix(compression(word,states)), word
            tested+=1
    witness=code['weight_three_logical_witness']
    assert sum(c!='I' for c in witness)==3
    m=compression(witness,states)
    assert not scalar_matrix(m)
    # Negative control: orthogonal computational basis vectors fail at weight one.
    bad=[[int(i==0) for i in range(128)],[int(i==1) for i in range(128)]]
    assert not scalar_matrix(compression('ZIIIIII',bad))
    return {'integer_gram':gram,'low_weight_paulis_checked':tested,
            'weight_three_witness':witness,'unnormalized_witness_compression':m,
            'distance':3,'negative_controls_rejected':1}


def graph_assay():
    errors=[]
    for w in (1,2):
        for word in words_of_weight(w):
            errors.append(as_masks(word))
    graphs=[g for g in nx.graph_atlas_g() if len(g)==N]
    assert len(graphs)==1044
    histogram={}
    degenerate_graphs=0
    graph_digest=hashlib.sha256()
    for g in graphs:
        neighbors=[sum(1<<j for j in g.neighbors(i)) for i in range(N)]
        graph_digest.update(bytes(neighbors))
        forbidden=set()
        zero_x=[]
        for x,z in errors:
            induced=z
            for j in range(N):
                if x>>j&1:
                    induced ^= neighbors[j]
            if induced:
                forbidden.add(induced)
            else:
                zero_x.append(x)
        if zero_x:
            degenerate_graphs+=1
        allowed={c for c in range(1,128) if c not in forbidden and
                 all((c&x).bit_count()%2==0 for x in zero_x)}
        histogram[len(allowed)]=histogram.get(len(allowed),0)+1
        # With 0 translated into the code, a third word needs a,b,a XOR b allowed.
        assert all(a^b not in allowed for a,b in combinations(sorted(allowed),2))
    return {'graphs':len(graphs),'graphs_with_weight_below_three_graph_stabilizers':degenerate_graphs,
            'allowed_nonzero_word_histogram':histogram,'graphs_admitting_three_words':0,
            'atlas_adjacency_sha256':graph_digest.hexdigest(),
            'scope':'CWS graph-basis codes only; atlas completeness is not needed by the analytic proof'}


def verify_sources():
    manifest=json.loads((ROOT/'source/manifest.json').read_text())
    for entry in manifest:
        data=(ROOT/'source'/entry['file']).read_bytes()
        assert len(data)==entry['bytes']
        assert hashlib.sha256(data).hexdigest()==entry['sha256']
    return len(manifest)


def main():
    report={'python':platform.python_version(),'networkx':nx.__version__,
            'lp':verify_lp()}
    code=load('steane-7-1-3.json')
    report['steane_symplectic']=symplectic_distance(code)
    report['steane_state_vectors']=vector_distance(code)
    report['cws']=graph_assay()
    report['source_snapshots_hash_verified']=verify_sources()
    report['verdict']='PARTIAL: known subclass exclusions certified; general ((7,3,3)) remains open'
    (ROOT/'results/verification.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print('PASS: K=3 enhanced LP feasible over rationals; K=4 Farkas contradiction 0 >= 1.')
    print('PASS: Steane distance 3 by 16384-Pauli enumeration and 211 exact state-vector compressions plus a weight-3 witness.')
    print('PASS: 1044 seven-vertex graph representatives; zero CWS dimension-3 candidates (including degeneracy constraints).')
    print('PASS: 3 negative controls rejected; source snapshot hashes matched.')
    print('FULL INSTANCE: OPEN. No general rank-3 projector or nonexistence certificate is claimed.')


if __name__=='__main__':
    main()
