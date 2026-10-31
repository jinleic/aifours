#!/usr/bin/env python3
"""Strict independent checker for textual LRAT with positive RUP hints only.

No solver is called. The complete CNF and proof are read once and hashed. Every
added clause must follow by reverse unit propagation in the supplied positive
hint order. RAT (negative hint IDs) is unsupported and REJECTED, not skipped.
Deletion timestamps may equal the last addition ID (standard LRAT).
All lines are parsed through EOF; a verified derived empty clause is mandatory.
This deliberately does not use the upstream lrat-check binary.
"""
import argparse
import hashlib
import json
from pathlib import Path


class CertificateError(ValueError):pass


def cnf_parse(raw):
    header=None;pending=[];clauses={}
    try:text=raw.decode('ascii')
    except UnicodeDecodeError as exc:raise CertificateError('CNF not ASCII') from exc
    for line in text.splitlines():
        if not line.strip() or line.startswith('c'):continue
        if line.startswith('p '):
            if header is not None or pending or clauses:raise CertificateError('CNF misplaced header')
            parts=line.split()
            if len(parts)!=4 or parts[:2]!=['p','cnf']:raise CertificateError('CNF invalid header')
            try:header=(int(parts[2]),int(parts[3]))
            except ValueError as exc:raise CertificateError('CNF invalid counts') from exc
            if min(header)<0:raise CertificateError('CNF negative counts')
            continue
        if header is None:raise CertificateError('CNF missing header')
        try:vals=list(map(int,line.split()))
        except ValueError as exc:raise CertificateError('CNF invalid literal') from exc
        for v in vals:
            if v==0:clauses[len(clauses)+1]=tuple(dict.fromkeys(pending));pending=[]
            else:
                if abs(v)>header[0]:raise CertificateError('CNF literal out of range')
                pending.append(v)
    if header is None:raise CertificateError('CNF missing header')
    if pending:raise CertificateError('CNF unterminated clause')
    if len(clauses)!=header[1]:raise CertificateError('CNF clause count mismatch')
    return header,clauses


def rup(clause,hints,db):
    assign={};contradict=False
    for lit in clause:
        v=abs(lit);val=(lit<0) # negate the proposed clause literal
        if v in assign and assign[v]!=val:contradict=True
        assign[v]=val
    # Still require every serialized hint to refer to an existing clause.
    for h in hints:
        if h<=0:raise CertificateError('unsupported nonpositive RUP hint')
        if h not in db:raise CertificateError('unknown or deleted hint clause')
    if contradict:return len(hints)
    work=0
    for h in hints:
        row=db[h];unit=None;unassigned=0;satisfied=False
        for lit in row:
            v=abs(lit)
            if v not in assign:unit=lit;unassigned+=1
            elif assign[v]==(lit>0):satisfied=True;break
        work+=1
        if satisfied:raise CertificateError('RUP hint already satisfied')
        if unassigned==0:return work
        if unassigned!=1:raise CertificateError('RUP hint not unit or conflicting')
        assign[abs(unit)]=(unit>0)
    raise CertificateError('RUP hints ended without conflict')


def verify(cnf_bytes,proof_bytes):
    (nv,nc),db=cnf_parse(cnf_bytes);last=nc;added=deleted=steps=0;empty=[]
    try:text=proof_bytes.decode('ascii')
    except UnicodeDecodeError as exc:raise CertificateError('proof not ASCII') from exc
    for lineno,line in enumerate(text.splitlines(),1):
        if not line.strip() or line.startswith('c'):continue
        parts=line.split()
        try:ident=int(parts[0])
        except (ValueError,IndexError) as exc:raise CertificateError('proof invalid clause ID') from exc
        is_delete=len(parts)>1 and parts[1]=='d'
        if ident<last or (ident==last and not is_delete):raise CertificateError('proof addition IDs not increasing')
        last=ident
        if is_delete:
            try:items=list(map(int,parts[2:]))
            except ValueError as exc:raise CertificateError('invalid deletion IDs') from exc
            if not items or items[-1]!=0 or any(x<=0 for x in items[:-1]):raise CertificateError('invalid deletion terminator')
            for x in items[:-1]:
                if x not in db:raise CertificateError('delete unknown clause')
                del db[x];deleted+=1
            continue
        try:items=list(map(int,parts[1:]));split=items.index(0)
        except ValueError as exc:raise CertificateError('proof addition missing clause terminator') from exc
        lits=items[:split];hints=items[split+1:]
        if not hints or hints[-1]!=0 or any(x==0 for x in hints[:-1]):raise CertificateError('invalid hint terminator')
        if any(abs(x)>nv for x in lits):raise CertificateError('proof literal out of range')
        row=tuple(dict.fromkeys(lits));steps+=rup(row,hints[:-1],db)
        db[ident]=row;added+=1
        if not row:empty.append(ident)
    if not empty:raise CertificateError('no verified empty clause')
    return {'input_variables':nv,'input_clauses':nc,'added_clauses':added,'deleted_clauses':deleted,
            'RUP_hint_steps_until_conflict':steps,'verified_empty_clause_IDs':empty,'all_lines_parsed':True}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('cnf',type=Path);ap.add_argument('proof',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    C=a.cnf.read_bytes();P=a.proof.read_bytes();result=verify(C,P)
    result.update({'status':'VERIFIED_TEXT_LRAT_RUP','cnf_sha256':hashlib.sha256(C).hexdigest(),
      'cnf_bytes':len(C),'proof_sha256':hashlib.sha256(P).hexdigest(),'proof_bytes':len(P),
      'scope':'Exactly the pinned CNF follows UNSAT from positive-hint RUP; no encoder or mathematical normal-form correctness claim.'})
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    try:main()
    except CertificateError as exc:raise SystemExit('INVALID: '+str(exc))
