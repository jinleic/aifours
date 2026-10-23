"""Small independent LRAT/RUP checker; accepts positive RUP hints only.

Initial clause IDs are DIMACS line order. Deletions may remove clauses;
each added clause is checked by a fresh assignment and the exact listed
unit-propagation hints. Unsupported RAT steps fail instead of being
trusted. An empty-clause derivation is required. No solver libraries or
producer code are imported. Text proofs may be gzip-compressed.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time


def op(path):
    return gzip.open(path,'rt') if str(path).endswith('.gz') else open(path)


def check(cnfpath,proofpath):
    db={}
    nv=nc=None
    with op(cnfpath) as fh:
        for line in fh:
            if not line.strip() or line[0]=='c': continue
            if line[0]=='p':
                _,typ,v,c=line.split()
                assert typ=='cnf'
                nv,nc=int(v),int(c)
                continue
            vals=list(map(int,line.split()))
            assert vals[-1]==0 and 0 not in vals[:-1]
            assert all(1<=abs(v)<=nv for v in vals[:-1])
            db[len(db)+1]=tuple(vals[:-1])
    assert len(db)==nc
    max_id=nc
    additions=deletions=0
    empty=False
    start=time.monotonic()
    with op(proofpath) as fh:
        for lineno,line in enumerate(fh,1):
            if not line.strip() or line[0]=='c': continue
            fields=line.split()
            cid=int(fields[0])
            if fields[1]=='d':
                assert fields[-1]=='0'
                for word in fields[2:-1]:
                    old=int(word)
                    assert old in db
                    del db[old]
                    deletions+=1
                continue
            assert cid>max_id, (lineno,cid,max_id)
            vals=list(map(int,fields[1:]))
            cut=vals.index(0)
            clause=tuple(vals[:cut])
            hints=vals[cut+1:]
            assert hints and hints[-1]==0 and all(h>0 for h in hints[:-1]), ('unsupported non-RUP hint',lineno)
            assert all(1<=abs(v)<=nv for v in clause)
            assignment={}
            conflict=False
            for lit in clause:
                var=abs(lit)
                val=lit<0
                if var in assignment and assignment[var]!=val:
                    conflict=True
                    break
                assignment[var]=val
            for hint in hints[:-1]:
                if conflict: break
                assert hint in db, ('missing hint',lineno,hint)
                candidate=db[hint]
                unit=None
                unresolved=0
                satisfied=False
                for lit in candidate:
                    val=assignment.get(abs(lit))
                    if val is None:
                        unit=lit
                        unresolved+=1
                    elif val==(lit>0):
                        satisfied=True
                        break
                if satisfied:
                    continue
                assert unresolved<=1, ('hint not unit',lineno,hint,unresolved)
                if unresolved==0:
                    conflict=True
                else:
                    assignment[abs(unit)]=(unit>0)
            assert conflict, ('RUP failure',lineno,cid)
            db[cid]=clause
            max_id=cid
            additions+=1
            if not clause:
                empty=True
            if additions%250000==0:
                print('checked additions',additions,'active clauses',len(db),'seconds',round(time.monotonic()-start,2),flush=True)
    assert empty, 'No checked empty clause: partial proof is inconclusive'
    cnf_bytes=Path(cnfpath).read_bytes()
    uncompressed_cnf=gzip.decompress(cnf_bytes) if str(cnfpath).endswith('.gz') else cnf_bytes
    return {'status':'PASS','initial_clauses':nc,'variables':nv,'checked_additions':additions,'deleted_clauses':deletions,'checked_empty_clause':True,'cnf_sha256':hashlib.sha256(uncompressed_cnf).hexdigest(),'cnf_file_sha256':hashlib.sha256(cnf_bytes).hexdigest(),'proof_sha256':hashlib.sha256(Path(proofpath).read_bytes()).hexdigest()}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('cnf')
    p.add_argument('proof')
    p.add_argument('--output')
    a=p.parse_args()
    result=check(a.cnf,a.proof)
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)


if __name__=='__main__': main()
