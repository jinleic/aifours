#!/usr/bin/env python3
"""Exact independent audit of the public R-minus Annex C certificate.

Reads the downloaded publisher-linked PDF's pdftotext layout and independently
cross-checks the separate original text and ZIP bytes. Each weighted row is
classified against elemental entropy, graph FDs, graph symmetry, or an explicit
conditional-copy protocol. Rational accumulation is exact; no LP status is used.
"""
from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent
TXT = ROOT / 'frontier-20261028-gurpinar-annexc-original.txt'
PDF = ROOT / 'frontier-20261028-gurpinar-annexc-original.pdf'
ZIP = ROOT / 'frontier-20261028-gurpinar-annexc-original.zip'
LAYOUT = ROOT / 'frontier-20261028-gurpinar-annexc-pdf-layout.txt'
OUTPUT = ROOT / 'frontier-20261028-gurpinar-certificate-audit-result.json'
BASE = tuple('abcdefghij')
NEIGHBOURS = {
    'a':set('bcdefg'), 'b':set('acgij'), 'c':set('abdhi'),
    'd':set('acehj'), 'e':set('adfij'), 'f':set('aeg hi'.replace(' ','')),
    'g':set('abfhj'), 'h':set('cdfgij'), 'i':set('bc efh'.replace(' ','')),
    'j':set('bdegh'),
}
GENERATORS = ((7,9,6,5,8,2,3,0,1,4), (0,4,5,6,1,2,3,7,8,9))
# (old copied tuple, fresh tuple, conditioning base, all variables existing
# before this copy) as transcribed from the publisher's Theorem 5.2.
COPY_STEPS = (
    (('b',), ("b'0",), set('adefghij'), set(BASE)),
    (('d','e'), ("d'1","e'1"), set('abcfghi'), set(BASE)),
    (('g',), ("g'2",), set(('a','b','c','d',"e'1",'f','h','i')),
     set(BASE) | {"d'1","e'1"}),
    (('f','g'), ("f'3","g'3"), set('abcdehij'), set(BASE)),
    (('h',), ("h'4",), set(('a','b','c','d','e','f',"f'3",'i','j')),
     set(BASE) | {"f'3","g'3"}),
)


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def powerset(values):
    values = tuple(values)
    for size in range(len(values)+1):
        for subset in combinations(values,size):
            yield frozenset(subset)


def row_key(terms):
    acc = Counter()
    for subset,value in terms:
        subset = frozenset(subset)
        if subset:
            acc[subset] += value
    return tuple(sorted((tuple(sorted(s)),c) for s,c in acc.items() if c))


def both_signs(key):
    return (key, tuple((s,-c) for s,c in key))


def automorphisms():
    assert all(u in NEIGHBOURS[v] for u,ns in NEIGHBOURS.items() for v in ns)
    edges = {frozenset((u,v)) for u,ns in NEIGHBOURS.items() for v in ns}
    assert len(edges)==26 and frozenset(('c','d')) in edges and frozenset(('i','j')) not in edges
    for p in GENERATORS:
        assert sorted(p)==list(range(10))
        assert {frozenset(BASE[p[BASE.index(x)]] for x in edge) for edge in edges} == edges
    identity=tuple(range(10)); group={identity}; queue=deque([identity])
    while queue:
        p=queue.popleft()
        for g in GENERATORS:
            q=tuple(g[p[i]] for i in range(10))
            if q not in group:
                group.add(q); queue.append(q)
    return group


def copy_equality_set():
    allowed = set()
    for old,new,conditioning,past in COPY_STEPS:
        assert len(old)==len(new) and not set(old)&conditioning and not set(new)&past
        assert conditioning <= past and set(old) <= past
        for subset in powerset(range(len(old))):
            if not subset:
                continue
            os = {old[i] for i in subset}; ns = {new[i] for i in subset}
            for cond in powerset(sorted(conditioning)):
                key=row_key(((os | set(cond),1),(ns | set(cond),-1)))
                allowed.update(both_signs(key))
        key=row_key(((set(new)|conditioning,1),(past,1),
                     (past|set(new),-1),(conditioning,-1)))
        allowed.update(both_signs(key))
    return allowed


def classify_ge(terms):
    positives=[s for s,c in terms if c==1]
    negatives=[s for s,c in terms if c==-1]
    if any(abs(c)!=1 for _,c in terms):
        return None
    # CMI, including empty conditioning set (the H(empty) term is omitted).
    if len(positives)==2 and len(negatives) in (1,2):
        p,q=map(set,positives); inter=p&q; union=p|q
        negative_sets={frozenset(s) for s in negatives}
        expected={frozenset(union)} | ({frozenset(inter)} if inter else set())
        if negative_sets==expected and p-inter and q-inter:
            return 'CMI_nonnegative'
    # Conditional entropy H(S union T)-H(S), including H(S) with S empty.
    if len(positives)==1 and len(negatives) in (0,1):
        p=set(positives[0]); q=set(negatives[0]) if negatives else set()
        if q < p:
            return 'conditional_entropy_nonnegative'
    # The reverse conditional entropy is zero specifically by an original FD.
    if len(positives)==len(negatives)==1:
        p,n=map(set,(positives[0],negatives[0])); extra=n-p
        if p < n and len(extra)==1:
            v=next(iter(extra))
            if v in NEIGHBOURS and p==NEIGHBOURS[v]:
                return 'original_FD_zero_as_ge'
    return None


def classify_equal(terms,group,copy_allowed):
    key=tuple(terms)
    if key in copy_allowed:
        return 'conditional_copy_equality'
    positives=[set(s) for s,c in terms if c==1]
    negatives=[set(s) for s,c in terms if c==-1]
    if len(positives)==len(negatives)==1 and all(x in BASE for s,_ in terms for x in s):
        lhs,rhs=positives[0],negatives[0]
        for p in group:
            if {BASE[p[BASE.index(x)]] for x in lhs} == rhs:
                return 'graph_automorphism_equality'
    return None


def main():
    text_bytes=TXT.read_bytes(); pdf_bytes=PDF.read_bytes(); zip_bytes=ZIP.read_bytes()
    layout=LAYOUT.read_text(encoding='utf-8')
    with zipfile.ZipFile(ZIP) as z:
        names=sorted(z.namelist())
        zip_match = (set(names)=={'AnnexC.pdf','Rminus1847over276certificate.txt'}
                     and z.read('AnnexC.pdf')==pdf_bytes
                     and z.read('Rminus1847over276certificate.txt')==text_bytes)
    assert zip_match, names
    lines=text_bytes.decode('utf-8-sig').splitlines()
    assert lines[0].strip()=='Objective Value = 1847/276'
    txt_rows=[]
    for line in lines[1:]:
        name,coefficient=line.split(' = ',1)
        txt_rows.append((name,Fraction(coefficient.strip())))
    assert len(txt_rows)==1920

    # Remove only standalone PDF page numbers; preserve all row text.
    layout=re.sub(r'(?m)^\s*\d+\s*$', ' ', layout).replace('\u2019',"'")
    entropy=r'H\s*\{[^{}]*\}'
    pattern=re.compile(r'(?P<expr>[+-]?\s*'+entropy+r'(?:\s*[+-]\s*'+entropy+r')*)'
                       r'\s*(?P<rel>>=|<=|=)\s*(?P<rhs>[01])'
                       r'\s*with\s+coefficient\s*(?P<coef>[+-]?\d+(?:\s*/\s*\d+)?)')
    matches=list(pattern.finditer(layout))
    assert len(matches)==1920, f'parsed {len(matches)} PDF expressions, expected 1920'
    allowed_symbols=set(BASE)|{"b'0","d'1","e'1","g'2","f'3","g'3","h'4"}
    group=automorphisms(); copy_allowed=copy_equality_set()
    accumulator={}; rhs_total=Fraction(0)
    categories=Counter(); bad=[]; coefficient_mismatches=[]
    for index,(match,(name,txt_coefficient)) in enumerate(zip(matches,txt_rows),start=1):
        coefficient=Fraction(match.group('coef').replace(' ',''))
        if coefficient != txt_coefficient:
            coefficient_mismatches.append({'row':index,'name':name,
                'pdf_coefficient':str(coefficient),'txt_coefficient':str(txt_coefficient)})
        raw_terms=[]
        for sign,inside in re.findall(r'([+-]?)\s*H\s*\{([^{}]*)\}',match.group('expr')):
            tokens=[x.strip() for x in inside.split('.') if x.strip()]
            assert len(tokens)==len(set(tokens)) and set(tokens)<=allowed_symbols, (index,tokens)
            raw_terms.append((set(tokens), -1 if sign=='-' else 1))
        terms=row_key(raw_terms)
        rel,rhs=match.group('rel'),int(match.group('rhs'))
        if rel=='>=' and rhs==0 and coefficient < 0:
            kind=classify_ge(terms)
        elif rel=='<=' and rhs==1 and coefficient > 0:
            kind=('original_singleton_cap' if len(terms)==1 and terms[0][1]==1
                  and len(terms[0][0])==1 and terms[0][0][0] in BASE else None)
        elif rel=='=' and rhs==0 and coefficient:
            kind=classify_equal(terms,group,copy_allowed)
        else:
            kind=None
        categories[kind or 'UNRECOGNIZED']+=1
        if kind is None:
            bad.append({'row':index,'name':name,'relation':rel,'rhs':rhs,
                        'coefficient':str(coefficient),'terms':terms})
        for subset,c in terms:
            accumulator[subset]=accumulator.get(subset,Fraction(0))+coefficient*c
        rhs_total += coefficient*rhs
    residual={'.'.join(s):str(c) for s,c in sorted(accumulator.items()) if c}
    expected={'.'.join(BASE):'1'}
    result={'txt_sha256':sha(TXT),'pdf_sha256':sha(PDF),'zip_sha256':sha(ZIP),
            'layout_sha256':sha(LAYOUT),'zip_members':names,'zip_member_bytes_match_separate_originals':zip_match,
            'txt_nonzero_rows':len(txt_rows),'pdf_parsed_rows':len(matches),
            'coefficient_mismatch_count':len(coefficient_mismatches),
            'coefficient_mismatches':coefficient_mismatches[:20],
            'group_size':len(group),'independently_checked_automorphism_generators':GENERATORS,
            'allowed_copy_equality_forms':len(copy_allowed),
            'row_class_counts':dict(categories),'unrecognized_count':len(bad),
            'unrecognized_rows':bad[:30],
            'exact_weighted_lhs_residual':residual,
            'exact_weighted_rhs':str(rhs_total),
            'exact_target_lhs_identity':residual==expected,
            'exact_target_rhs_identity':rhs_total==Fraction(1847,276),
            'all_individual_rows_classified':len(bad)==0,
            'all_pdf_txt_coefficients_match':len(coefficient_mismatches)==0,
            'limits':'Classification is relative to the explicitly encoded publisher copy protocol, graph and entropy rules; matching those transcriptions to publisher figures and mathematical review of the conditional-copy construction remain separate. No novelty or tighter upper bound is claimed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2); stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
