#!/usr/bin/env python3
"""Bind the written 16-term inequality to the independent entropy identity."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parent
PROOF=('frontier-20261028-universal-gluing-inequality-v1.md','a017351d672c37c170b5dff4cf6ce76467f5d2460fa04ce81d922de660b48dce')
RECEIPT=('frontier-20261028-cross-pair-farkas-independent-check-result.json','199a7471622c6c3085a669e2b43e7235676e680ee7e8cb3fa8f636449a1aff45')
OUTPUT=ROOT/'frontier-20261028-universal-gluing-term-map-check-result.json'
SYMBOLS=tuple('abcdefghij')+('D','F')


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return raw


def parse(text):
    begin=text.index('L={}')
    end=text.index(r'\end{aligned}',begin)
    body=re.sub(r'[\s&\\]+','',text[begin:end])
    found=re.findall(r'([+-]?)(\d*)H\(([^()]*)\)',body)
    if len(found)!=16:raise ValueError(('TERM_COUNT',len(found)))
    out=Counter()
    for sign,number,labels in found:
        if any(x not in SYMBOLS for x in labels) or len(set(labels))!=len(labels):raise ValueError(('LABELS',labels))
        mask=sum(1<<SYMBOLS.index(x) for x in labels)
        if mask&3072==3072:raise ValueError('MIXED_TERM')
        coeff=int(number) if number else 1
        out[mask]+=(-coeff if sign=='-' else coeff)
    return {m:c for m,c in out.items() if c}


def main():
    raw=pin(PROOF);rec=json.loads(pin(RECEIPT));proof=raw.decode('utf-8')
    if not rec['all_checked'] or rec['exact_identity']['known_constant']!='-12637/1725000':raise ValueError('IDENTITY_RECEIPT')
    expected={m:int(Fraction(c)) for m,c in rec['exact_identity']['known_terms']}
    if any(Fraction(c).denominator!=1 for _,c in rec['exact_identity']['known_terms']):raise ValueError('NONINTEGER_COEFFICIENT')
    actual=parse(proof)
    if actual!=expected:raise ValueError(('TERM_MAP_MISMATCH',actual,expected))
    controls={}
    for tag,needle,replacement in (
        ('flipped_term_sign','-H(abcefgij)','+H(abcefgij)'),
        ('removed_term','-H(abdefgij)',''),
        ('changed_auxiliary','+H(abcefgijD)','+H(abcefgijF)')):
        if proof.count(needle)!=1:raise ValueError(('CONTROL_NEEDLE',tag))
        try:
            if parse(proof.replace(needle,replacement,1))!=expected:raise ValueError('MISMATCH')
        except ValueError:controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    out={'proof_sha256':PROOF[1],'independent_identity_receipt_sha256':RECEIPT[1],
         'term_count':16,'mixed_auxiliary_terms':0,'exact_map_matches_written_proof':True,
         'term_map':[{'mask':m,'labels':[SYMBOLS[i] for i in range(12) if m&(1<<i)],'coefficient':c}
                     for m,c in sorted(actual.items())],
         'mutation_controls':controls,
         'limits':'Checks text-to-identity binding and controls; the conditional product gluing proof is written mathematics and has not been formally or independently reviewed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
