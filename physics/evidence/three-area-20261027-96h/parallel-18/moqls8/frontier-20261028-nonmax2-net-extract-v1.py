#!/usr/bin/env python3
"""Validate and extract each pinned nonmaximal order-8 2-MOLS pair."""
import argparse,hashlib,json,pathlib,time
H=pathlib.Path(__file__).parent
SOURCE='frontier-20261028-source-wanless-nonmax2-complete-v1.txt';PIN='9011d27cf7d1d2383d106d1b01d4dcb897e51743fa7496833fe12679faa02061'
V=range(8)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 b=(H/SOURCE).read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('source pin')
 L=[s.strip() for s in b.decode('ascii').splitlines() if s.strip()]
 if L[0].split()[:3]!=['8','8','76'] or len(L)!=609:raise ValueError('catalogue count')
 S=[[[ord(c)-97 for c in L[1+8*k+i]] for i in V] for k in range(76)]
 for M in S:
  if any(set(row)!=set(V) for row in M) or any({M[i][j] for i in V}!=set(V) for j in V):raise ValueError('Latin')
 for j in range(38):
  a0,b0=S[2*j:2*j+2]
  if len({(a0[i][k],b0[i][k]) for i in V for k in V})!=64:raise ValueError('orthogonality')
 first=(H/'frontier-20261028-source-wanless-nonmax2-first-pair-v1.txt').read_text()
 firstlines=[s.strip() for s in first.splitlines() if s.strip()]
 if L[1:17]!=firstlines[1:]:raise ValueError('first pair mismatch')
 records=[]
 for j in range(1,38):
  name=f'frontier-20261028-source-wanless-nonmax2-pair{j:02d}-v1.txt';path=H/name
  text='8 8 2 ## exact pair excerpt index %d\n'%j+'\n'.join(L[1+16*j:1+16*(j+1)])+'\n'
  with path.open('x',encoding='ascii') as h:h.write(text)
  records.append({'index':j,'file':name,'sha256':hashlib.sha256(text.encode()).hexdigest()})
 out={'result':'PASS_38_PAIR_LATIN_AND_ORTHOGONAL','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'catalogue_snapshot':SOURCE,'catalogue_sha256':PIN,'pair_count':38,'first_pair_matches_preexisting':True,
      'extracted_new_pair_count':len(records),'pairs':records,'elapsed_seconds':time.monotonic()-start,
      'limits':'Exact source rows/pairs only; no claim of original HTTP byte identity or complete source classification.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='pairs'},indent=2))
if __name__=='__main__':main()
