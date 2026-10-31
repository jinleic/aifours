#!/usr/bin/env python3
"""Strict second implementation for the public R-minus coefficient certificate.

No imports from the first checker. Inputs are fixed by SHA-256. The publisher
PDF is re-extracted and matched byte-for-byte to the pinned layout. Validation
uses integer-scaled sparse vectors, not Fraction vector accumulation. Synthetic
mutation controls are in memory only; the original input files remain unchanged.
"""
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parent
FILES = {
    'pdf': ('frontier-20261028-gurpinar-annexc-original.pdf', '8befddb0faba71dbae9221956939d883946649e07a261c036ff7514dfea9ec6b'),
    'text': ('frontier-20261028-gurpinar-annexc-original.txt', 'b0bd3f614397ed11edd475efdc4acb6e8f326c6722ede71d5a08760d84578b22'),
    'zip': ('frontier-20261028-gurpinar-annexc-original.zip', '09b3bcbd76be65257adba4a69ea5d26cc2cb686e2fdac7b5bb1963ef2a4e6fd0'),
    'layout': ('frontier-20261028-gurpinar-annexc-pdf-layout.txt', '6ff906bb54ddf33e46d5bfcddf50ffa0680c0315e118d6530e6f13f36adc2ca5'),
}
OUTPUT = ROOT / 'frontier-20261028-gurpinar-certificate-independent-result.json'
BASE = 'abcdefghij'
NEIGHBOURS = {
    'a':'bcdefg', 'b':'acgij', 'c':'abdhi', 'd':'acehj', 'e':'adfij',
    'f':'aeghi', 'g':'abfhj', 'h':'cdfgij', 'i':'bcefh', 'j':'bdegh',
}
GENS = ((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))


class AuditError(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


def require(condition, reason):
    if not condition:
        raise AuditError(reason)


def pin(name, data, expected):
    require(sha256(data).hexdigest() == expected, 'INPUT_HASH_MISMATCH:' + name)


def subsets(s):
    items=sorted(s)
    for n in range(len(items)+1):
        for sub in combinations(items,n):
            yield set(sub)


def vector(terms):
    result={}
    for symbols,sign in terms:
        key=tuple(sorted(symbols))
        if key:
            result[key]=result.get(key,0)+sign
    return {k:v for k,v in result.items() if v}


def canonical(v):
    return tuple(sorted((tuple(k),val) for k,val in v.items() if val))


def copy_forms():
    original=set(BASE)
    steps=[
        ({'b':"b'0"}, set('adefghij'), original),
        ({'d':"d'1",'e':"e'1"},set('abcfghi'),original),
        ({'g':"g'2"},{'a','b','c','d',"e'1",'f','h','i'},original|{"d'1","e'1"}),
        ({'f':"f'3",'g':"g'3"},set('abcdehij'),original),
        ({'h':"h'4"},{'a','b','c','d','e','f',"f'3",'i','j'},original|{"f'3","g'3"}),
    ]
    allowed=set()
    for mapping,condition,past in steps:
        require(set(mapping)<=past and set(mapping.values()).isdisjoint(past)
                and condition<=past and condition.isdisjoint(mapping), 'INVALID_COPY_PROTOCOL')
        def add(v):
            allowed.add(canonical(v)); allowed.add(canonical({k:-value for k,value in v.items()}))
        for chosen in subsets(mapping):
            if chosen:
                fresh={mapping[x] for x in chosen}
                for context in subsets(condition):
                    add(vector([(chosen|context,1),(fresh|context,-1)]))
        fresh=set(mapping.values())
        add(vector([(fresh|condition,1),(past,1),(past|fresh,-1),(condition,-1)]))
    return allowed


def group():
    edges={frozenset((u,v)) for u,ns in NEIGHBOURS.items() for v in ns}
    require(len(edges)==26 and all(v in NEIGHBOURS[u] for u,ns in NEIGHBOURS.items() for v in ns),
            'INVALID_GRAPH')
    require(frozenset('cd') in edges and frozenset('ij') not in edges,'INVALID_GRAPH')
    for p in GENS:
        require(sorted(p)==list(range(10)), 'INVALID_AUTOMORPHISM')
        image={frozenset(BASE[p[BASE.index(x)]] for x in edge) for edge in edges}
        require(image==edges,'INVALID_AUTOMORPHISM')
    result={tuple(range(10))}
    while True:
        expanded=result|{tuple(g[p[i]] for i in range(10)) for p in result for g in GENS}
        if expanded==result:
            return result
        result=expanded


def valid_ge(row):
    pos=[set(k) for k,v in row.items() if v==1]
    neg=[set(k) for k,v in row.items() if v==-1]
    if any(abs(v)!=1 for v in row.values()):
        return None
    if len(pos)==2 and len(neg) in (1,2):
        z=pos[0]&pos[1]; union=pos[0]|pos[1]
        expected={frozenset(union)} | ({frozenset(z)} if z else set())
        if {frozenset(s) for s in neg}==expected and pos[0]-z and pos[1]-z:
            return 'CMI'
    if len(pos)==1 and len(neg) in (0,1):
        z=neg[0] if neg else set()
        if z < pos[0]:
            return 'conditional_entropy'
    if len(pos)==len(neg)==1 and pos[0]<neg[0]:
        extra=neg[0]-pos[0]
        if len(extra)==1:
            vertex=next(iter(extra))
            if vertex in NEIGHBOURS and pos[0]==set(NEIGHBOURS[vertex]):
                return 'FD'
    return None


def valid_eq(row,permutations,copies):
    if canonical(row) in copies:
        return 'copy'
    pos=[set(k) for k,v in row.items() if v==1]
    neg=[set(k) for k,v in row.items() if v==-1]
    if len(row)==2 and len(pos)==len(neg)==1 and (pos[0]|neg[0])<=set(BASE):
        if any({BASE[p[BASE.index(x)]] for x in pos[0]}==neg[0] for p in permutations):
            return 'symmetry'
    return None


def parse_input(layout, text):
    textlines=text.decode('utf-8-sig').splitlines()
    require(bool(textlines) and textlines[0].strip()=='Objective Value = 1847/276','BAD_OBJECTIVE')
    textrows=[]
    for line in textlines[1:]:
        match=re.fullmatch(r'([^\s=]+)\s*=\s*([+-]?\d+(?:/\d+)?)',line.strip())
        require(match is not None,'BAD_TEXT_ROW')
        textrows.append((match.group(1),Fraction(match.group(2))))
    require(len(textrows)==1920,'ROW_COUNT')
    raw=layout.decode('utf-8').replace('\u2019',"'").replace('\f','\n')
    require(raw.startswith('A CERTIFICATE OF 1847'), 'BAD_LAYOUT_HEADER')
    start=raw.find('H{'); require(start>=0,'BAD_LAYOUT_HEADER')
    body=raw[start:]
    body=re.sub(r'(?m)^[ \t]*\d+[ \t]*$', '', body)
    pieces=re.split(r'with\s+coefficient\s*([+-]?\d+(?:\s*/\s*\d+)?)',body)
    require(len(pieces)==3841 and not pieces[-1].strip(),'PDF_ROW_COVERAGE')
    term=r'H\s*\{[^{}]+\}'
    pattern=re.compile(r'\s*(?P<expr>[+-]?\s*'+term+r'(?:\s*[+-]\s*'+term+r')*)'
                       r'\s*(?P<relation>>=|<=|=)\s*(?P<rhs>[01])\s*')
    rows=[]
    allowed=set(BASE)|{"b'0","d'1","e'1","g'2","f'3","g'3","h'4"}
    for i,(name,textcoef) in enumerate(textrows):
        match=pattern.fullmatch(pieces[2*i])
        require(match is not None,'PDF_ROW_SYNTAX:'+str(i+1))
        coefficient=Fraction(pieces[2*i+1].replace(' ',''))
        require(coefficient==textcoef,'SOURCE_COEFFICIENT_MISMATCH')
        terms=[]
        for sign,inside in re.findall(r'([+-]?)\s*H\s*\{([^{}]+)\}',match.group('expr')):
            symbols=inside.split('.')
            require(len(symbols)==len(set(symbols)) and set(symbols)<=allowed,
                    'INVALID_SYMBOLS:'+str(i+1))
            terms.append((set(symbols),-1 if sign=='-' else 1))
        rows.append({'name':name,'coefficient':coefficient,'relation':match.group('relation'),
                     'rhs':int(match.group('rhs')),'terms':vector(terms)})
    return rows


def validate(rows):
    require(len(rows)==1920,'ROW_COUNT')
    permutations=group(); copies=copy_forms()
    counts=Counter(); scale=lcm(276,*(r['coefficient'].denominator for r in rows))
    aggregate={}; total_rhs=0
    for row in rows:
        coefficient=row['coefficient']; rel=row['relation']; rhs=row['rhs']; terms=row['terms']
        require(coefficient!=0, 'ZERO_WEIGHT')
        if rel=='>=' and rhs==0:
            require(coefficient<0,'INVALID_WEIGHT_SIGN')
            kind=valid_ge(terms)
        elif rel=='<=' and rhs==1:
            require(coefficient>0,'INVALID_WEIGHT_SIGN')
            kind=('cap' if len(terms)==1 and next(iter(terms.values()))==1
                  and len(next(iter(terms)))==1 and next(iter(terms))[0] in BASE else None)
        elif rel=='=' and rhs==0:
            kind=valid_eq(terms,permutations,copies)
        else:
            raise AuditError('INVALID_ROW')
        require(kind is not None,'INVALID_ROW')
        counts[kind]+=1
        factor=coefficient.numerator*(scale//coefficient.denominator)
        total_rhs+=factor*rhs
        for k,value in terms.items():
            aggregate[k]=aggregate.get(k,0)+factor*value
    aggregate={k:v for k,v in aggregate.items() if v}
    require(aggregate=={tuple(BASE):scale},'WEIGHTED_IDENTITY')
    require(total_rhs==1847*(scale//276),'RHS_IDENTITY')
    return {'integer_scale':scale,'row_class_counts':dict(counts),'group_size':len(permutations),
            'weighted_identity_exact':True,'weighted_rhs':'1847/276'}


def main():
    data={}
    for key,(filename,expected) in FILES.items():
        data[key]=(ROOT/filename).read_bytes(); pin(key,data[key],expected)
    extract=subprocess.run(['pdftotext','-layout',str(ROOT/FILES['pdf'][0]),'-'],
                           check=True,capture_output=True,timeout=30).stdout
    require(extract==data['layout'],'PDF_EXTRACTION_MISMATCH')
    with zipfile.ZipFile(ROOT/FILES['zip'][0]) as z:
        require(set(z.namelist())=={'AnnexC.pdf','Rminus1847over276certificate.txt'},'ZIP_MEMBER_SET')
        require(z.read('AnnexC.pdf')==data['pdf'] and z.read('Rminus1847over276certificate.txt')==data['text'],
                'ZIP_CONTENT_MISMATCH')
    rows=parse_input(data['layout'],data['text'])
    verdict=validate(rows)
    controls=[]
    def rejected(label,changes,expected):
        mutated=deepcopy(rows); changes(mutated)
        try:
            validate(mutated)
        except AuditError as exc:
            require(exc.reason==expected,'CONTROL_WRONG_REASON:'+label+':'+exc.reason)
            controls.append({'mutation':label,'expected':expected,'observed':exc.reason})
            return
        raise AuditError('CONTROL_ACCEPTED:'+label)
    first_ge=next(i for i,r in enumerate(rows) if r['relation']=='>=' and valid_ge(r['terms'])=='CMI')
    first_cap=next(i for i,r in enumerate(rows) if r['relation']=='<=')
    first_fd=next(i for i,r in enumerate(rows) if r['relation']=='>=' and valid_ge(r['terms'])=='FD')
    rejected('drop_one_row',lambda r:r.pop(),'ROW_COUNT')
    rejected('flip_CMI_weight',lambda r:r[first_ge].update(coefficient=-r[first_ge]['coefficient']),
             'INVALID_WEIGHT_SIGN')
    rejected('cap_rhs_zero',lambda r:r[first_cap].update(rhs=0),'INVALID_ROW')
    def invalid_fd(r):
        row=r[first_fd]['terms']; positive=next(k for k,v in row.items() if v==1)
        value=row.pop(positive); row[positive[:-1]]=value
    rejected('drop_FD_neighbour',invalid_fd,'INVALID_ROW')
    rejected('alter_valid_CMI_weight',lambda r:r[first_ge].update(coefficient=r[first_ge]['coefficient']-1),
             'WEIGHTED_IDENTITY')
    try:
        pin('synthetic',b'different',FILES['text'][1])
    except AuditError as exc:
        require(exc.reason=='INPUT_HASH_MISMATCH:synthetic','CONTROL_WRONG_REASON:hash')
        controls.append({'mutation':'wrong_input_bytes','expected':'INPUT_HASH_MISMATCH:synthetic','observed':exc.reason})
    else:
        raise AuditError('CONTROL_ACCEPTED:hash')
    result={'source_pins':{k:v[1] for k,v in FILES.items()},
            'PDF_reextraction_exact_bytes_match':True,'ZIP_member_bytes_match':True,
            'strict_pdf_expression_coverage':len(rows),'strict_text_row_count':len(rows),
            'pdf_text_coefficients_equal_in_order':True,'verdict':verdict,
            'controls':controls,'limits':'One independently written same-harness checker plus in-memory mutations. The publisher PDF text extraction and the stated graph/copy-protocol transcription still require independent documentary and mathematical review. Not a tighter bound or novelty result.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2); stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
