#!/usr/bin/env python3
"""Cross-check all USED d=4 site diagram maps against literal matrix indices.

The only author code executed is the AST-extracted pure functions implementing
row rules and diagram loop counting. No author verifier, correction solve,
certificate pickling globals, or construction code is executed. The independent
reference enumerates actual basis coordinates of the finite local operators.
"""
import ast
import collections
import hashlib
import importlib.util
import itertools
import json
import lzma
import io
import tarfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / 'frontier-20261028-tomar-release-ep3-v3.tar.gz'
OUT = ROOT / 'frontier-20261028-independent-d4-localmaps-check-results.json'
BASE = ROOT / 'frontier-20261028-independent-d4-base-check.py'
EXPECTED_ARCHIVE_SHA = '2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3'
EXPECTED_MEMBER_SHA = '0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
D = 4


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_data_and_functions():
    data = ARCHIVE.read_bytes()
    if sha(data) != EXPECTED_ARCHIVE_SHA:
        raise ValueError('archive digest mismatch')
    spec = importlib.util.spec_from_file_location('independent_base', BASE)
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as tf:
        raw = tf.extractfile('release_ep3/certs/ep3_perd_d4.pkl.xz').read()
        source = tf.extractfile('release_ep3/ep3core.py').read()
    if sha(raw) != EXPECTED_MEMBER_SHA:
        raise ValueError('certificate member digest mismatch')
    obj = base.DataOnlyUnpickler(io.BytesIO(lzma.decompress(raw, memlimit=256*1024*1024))).load()
    if (obj['d'],obj['k']) != (4,3):
        raise ValueError('wrong target')
    tree = ast.parse(source, filename='ep3core.py')
    needed = {'parse_pattern','entry_rule','op_edges','gram_monomial'}
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in needed]
    if {node.name for node in nodes} != needed:
        raise ValueError('required author pure functions missing')
    code = ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[]))
    env = {'FAMILY_LETTERS': {'31':'aaab','22':'aabb','13':'bbba'}}
    exec(compile(code,'author-extracted-pure-functions','exec'),env)
    return obj, env, sha(source)


def explicit_vector(key, n):
    """Construct one actual four-slot diagram as a sparse vector in (R^n)^4."""
    pairs, top, bottom = key
    result = collections.Counter()
    for choices in itertools.product(range(n), repeat=len(pairs)):
        a = [None]*4
        for (i,j), value in zip(pairs,choices):
            if a[i] is not None or a[j] is not None:
                raise ValueError('overlapping diagram positions')
            a[i]=value
            a[j]=value
        for i,value in top:
            if a[i] is not None or not 0 <= value < n:
                raise ValueError('invalid top slot')
            a[i]=value
        for i,value in bottom:
            value = n + value
            if a[i] is not None or not 0 <= value < n:
                raise ValueError('invalid bottom slot')
            a[i]=value
        if any(x is None for x in a):
            raise ValueError('diagram has unspecified position')
        result[tuple(a)] += 1
    return result


def literal_index_entry(row, col, p, kpos, lpos):
    """Exact source permutation entry V_p at literally rearranged row/column indices."""
    def choose(pos):
        side, index = pos
        return row[index] if side == 'i' else col[index]
    ket = tuple(choose(pos) for pos in kpos)
    bra = tuple(choose(pos) for pos in lpos)
    return int(all(ket[p[i]] == bra[i] for i in range(4)))


def verify_row_rearrangement(row1, row2, family, kpos, lpos):
    """Compare multisets of literal vector factors, not author matching choices."""
    a,b = row1.split(),row2.split()
    if len(a)!=4 or len(b)!=4:
        return False
    if any(x not in ('a','b','a*','b*') for x in a+b):
        return False
    unc,conj = [],[]
    for j,(left,right) in enumerate(zip(a,b)):
        if left.endswith('*') != right.endswith('*'):
            return False
        if left.endswith('*'):
            unc.append((right[0],('j',j)))
            conj.append((left[0],('i',j)))
        else:
            unc.append((left[0],('i',j)))
            conj.append((right[0],('j',j)))
    letters={'31':'aaab','22':'aabb','13':'bbba'}[family]
    assigned_u=[(letters[i],kpos[i]) for i in range(4)]
    assigned_c=[(letters[i],lpos[i]) for i in range(4)]
    return collections.Counter(unc)==collections.Counter(assigned_u) and collections.Counter(conj)==collections.Counter(assigned_c)


def main():
    start=time.monotonic()
    pkg, author, source_sha=load_data_and_functions()
    patterns=set()
    for t in pkg['types']:
        for a in t['rows']:
            for b in t['rows']:
                for mod in t['modules'][:3]:
                    _,cut,lab=mod.split('|')
                    ct=tuple(int(x) for x in cut.split(',')) if cut else ()
                    f,l,r=lab.split('_')
                    label=(int(f[1:]),() if l=='e' else tuple(map(int,l)),() if r=='e' else tuple(map(int,r)))
                    patterns.add((ct,a,b,label))
    perms=list(itertools.permutations(range(4)))
    vec_cache={}
    tested=0
    row_rules={}
    failures=[]
    collision_rules=0
    for cut, row1, row2, label in sorted(patterns,key=str):
        p1=author['parse_pattern'](row1)
        p2=author['parse_pattern'](row2)
        fam,kpos,lpos=author['entry_rule'](p1,p2)
        pair=(cut,row1,row2)
        if pair not in row_rules:
            row_rules[pair]=verify_row_rearrangement(row1,row2,fam,kpos,lpos)
            if not row_rules[pair]:
                failures.append({'kind':'row_rearrangement','pattern':str(pair)})
        keys,_=pkg['diagrams'][(4,cut)][label]
        vectors=[]
        for key in keys:
            frozen=tuple(tuple(tuple(z) for z in part) for part in key)
            if frozen not in vec_cache:
                vec_cache[frozen]=explicit_vector(key,D)
            vectors.append(vec_cache[frozen])
        for p in perms:
            edges=author['op_edges'](p,kpos,lpos)
            for ia,(ka,va) in enumerate(zip(keys,vectors)):
                for ib,(kb,vb) in enumerate(zip(keys,vectors)):
                    eps,cycles=author['gram_monomial'](ka,kb,edges,4)
                    predicted=eps*D**cycles
                    actual=sum(mul_a*mul_b*literal_index_entry(a,b,p,kpos,lpos)
                               for a,mul_a in va.items() for b,mul_b in vb.items())
                    tested+=1
                    if predicted!=actual:
                        failures.append({'kind':'diagram_value','cut':list(cut),'rows':[row1,row2],
                                         'label':str(label),'permutation':list(p),'key_indices':[ia,ib],
                                         'expected_explicit':actual,'got_loop_count':predicted})
                        if len(failures)>20:
                            raise RuntimeError('more than 20 mismatches; stopping')
                    ef,cf=author['gram_monomial'](ka,kb,edges,4,nfix=D)
                    if ef*D**cf!=actual:
                        failures.append({'kind':'fixed_dimension_formula','pattern':str((cut,row1,row2,label,p,ia,ib))})
                    collision_rules+=1
    result={'kind':'independent_all_used_d4_site_diagram_literal_index_comparison',
            'archive_sha256':EXPECTED_ARCHIVE_SHA,'certificate_member_sha256':EXPECTED_MEMBER_SHA,
            'author_ep3core_sha256':source_sha,'dimension':D,'copies':3,
            'used_cut_rowpair_label_combinations':len(patterns),'distinct_rowpair_cuts':len(row_rules),
            'row_rearrangement_failures':sum(not x for x in row_rules.values()),
            'distinct_sparse_diagram_keys':len(vec_cache),'permutations_per_combination':len(perms),
            'raw_diagram_pair_permutation_comparisons':tested,'exact_nfix_comparisons':collision_rules,
            'failure_count':len(failures),'failures':failures,
            'reference':'Explicit actual n=4 basis-coordinate sparse contractions of each used uncompressed diagram; author row-rule and loop-count pure functions isolated via AST. Integer compression C then follows by bilinearity.',
            'scope':'Actual site-local maps for all row-pair/cut/module combinations used by the uncorrected d4 package only. Does NOT check aux equality maps, all-orbit identity, exact correction, corrected PSD, or EP3.',
            'elapsed_seconds':round(time.monotonic()-start,3),
            'verdict':'PASS' if not failures else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2))
    return 0 if not failures else 1


if __name__=='__main__':
    raise SystemExit(main())
