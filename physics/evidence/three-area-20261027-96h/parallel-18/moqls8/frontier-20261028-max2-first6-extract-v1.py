#!/usr/bin/env python3
"""Extract six explicit maximal-source pairs and exact transversal counts."""
import argparse,hashlib,importlib.util,json,pathlib,time
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-source-wanless-max2-first6-v1.txt';PIN='533948f849d4e1972c7d0fdd136d1f4ea91f94d882152ee3134d355e2d3f6145'
MOD='frontier-20261028-two-nets-transversal-census-v1.py';MP='035a11d4f02fa708a1d3a9e5693800b3d8af22ba68b3f8627bc6f334e7464990'
if hashlib.sha256((H/MOD).read_bytes()).hexdigest()!=MP:raise ValueError('counter pin')
s=importlib.util.spec_from_file_location('transversal',H/MOD);tr=importlib.util.module_from_spec(s);s.loader.exec_module(tr)
V=range(8)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 b=(H/SRC).read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('source pin')
 L=[z.strip() for z in b.decode('ascii').splitlines() if z.strip()]
 if L[0].split()[:3]!=['8','8','4254'] or len(L)!=97:raise ValueError('six-pair extraction')
 S=[[[ord(c)-97 for c in L[1+8*k+i]] for i in V] for k in range(12)]
 for M in S:
  if any(set(row)!=set(V) for row in M) or any({M[i][j] for i in V}!=set(V) for j in V):raise ValueError('Latin')
 records=[]
 for j in range(6):
  T=S[2*j:2*j+2]
  if len({(T[0][i][k],T[1][i][k]) for i in V for k in V})!=64:raise ValueError('MOLS')
  a1,c1,c2=tr.brute(T);a2,nodes=tr.dfs(T)
  if a1!=a2:raise ValueError('transversal enumeration mismatch')
  if j==0:
   first=[s.strip() for s in (H/'frontier-20261028-source-wanless-max2-first-pair-v1.txt').read_text().splitlines() if s.strip()]
   if L[1:17]!=first[1:]:raise ValueError('first sample mismatch')
   name='frontier-20261028-source-wanless-max2-first-pair-v1.txt';h=hashlib.sha256((H/name).read_bytes()).hexdigest()
  else:
   name=f'frontier-20261028-source-wanless-max2-pair{j:02d}-v1.txt';text='8 8 2 ## exact maximal-source pair excerpt index %d\n'%j+'\n'.join(L[1+16*j:1+16*(j+1)])+'\n'
   with (H/name).open('x',encoding='ascii') as f:f.write(text)
   h=hashlib.sha256(text.encode()).hexdigest()
  records.append({'index':j,'file':name,'sha256':h,'common_transversals':len(a1),'first_only':c1,'second_only':c2,'dfs_nodes':nodes})
 out={'result':'PASS_SIX_MAXIMAL_SOURCE_PAIRS_VALIDATED','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'reader_snapshot_sha256':PIN,'transversal_counter_sha256':MP,'records':records,'elapsed_seconds':time.monotonic()-start,
      'limits':'First six source pairs only; source maximality/completeness and all other pairs not proved.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
