#!/usr/bin/env python3
"""Simple independent scan-based RUP checker; does not import the fast checker."""
import argparse,hashlib,json,pathlib,time

def parse_formula(b):
 lines=b.decode('ascii').splitlines();header=None;F=[]
 for s in lines:
  v=s.split()
  if not v or v[0]=='c':continue
  if v[0]=='p':
   if header or len(v)!=4 or v[1]!='cnf':raise ValueError('CNF header')
   header=(int(v[2]),int(v[3]));continue
  if not header:raise ValueError('missing header')
  q=[int(z) for z in v]
  if not q or q[-1]!=0 or 0 in q[:-1] or any(abs(x)>header[0] for x in q[:-1]) or len(q)==1:raise ValueError('CNF clause')
  F.append(q[:-1])
 if not header or len(F)!=header[1]:raise ValueError('CNF count')
 return header,F

def parse_trace(b,n):
 if not b.endswith(b'\n'):raise ValueError('unterminated proof')
 T=[]
 for s in b.decode('ascii').splitlines():
  v=s.split()
  if not v:raise ValueError('empty proof line')
  d=v[0]=='d';v=v[1:] if d else v
  q=[int(z) for z in v]
  if not q or q[-1]!=0 or 0 in q[:-1] or any(abs(x)>n for x in q[:-1]):raise ValueError('proof clause')
  T.append((d,q[:-1]))
 if not T or T[-1]!=(False,[]):raise ValueError('final empty absent')
 return T

def rup(F,C):
 assignment={}
 def assign(lit):
  k=abs(lit);v=lit>0
  if k in assignment:return assignment[k]==v
  assignment[k]=v;return True
 for lit in C:
  if not assign(-lit):return True
 while True:
  changed=False
  for clause in F:
   if any(abs(l) in assignment and assignment[abs(l)]==(l>0) for l in clause):continue
   unresolved=[l for l in clause if abs(l) not in assignment]
   if not unresolved:return True
   if len(unresolved)==1:
    if not assign(unresolved[0]):return True
    changed=True
  if not changed:return False

def verify(C,P):
 (n,m),F=parse_formula(C);T=parse_trace(P,n);add=delete=0
 for d,clause in T:
  if d:delete+=1;continue
  if not rup(F,clause):raise ValueError('non-RUP step '+str(add+delete+1))
  add+=1
  if clause:F.append(clause)
 return {'variables':n,'clauses':m,'steps':len(T),'additions':add,'deletions_ignored':delete}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cnf',required=True);ap.add_argument('--proof',required=True);ap.add_argument('--cnf-sha',required=True);ap.add_argument('--proof-sha',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 C=pathlib.Path(a.cnf).read_bytes();P=pathlib.Path(a.proof).read_bytes()
 if hashlib.sha256(C).hexdigest()!=a.cnf_sha or hashlib.sha256(P).hexdigest()!=a.proof_sha:raise ValueError('hash')
 counts=verify(C,P);controls={}
 for name,c,p in [('truncated',C,P.rsplit(b'\n',2)[0]+b'\n'),('SAT_empty',b'p cnf 2 1\n1 2 0\n',b'0\n'),('wrong_cnf',b'p cnf 2176 1\n1 0\n',P)]:
  try:verify(c,p)
  except (ValueError,UnicodeError):controls[name]='rejected'
  else:raise ValueError('control accepted '+name)
 out={'result':'PASS_INDEPENDENT_SCAN_RUP_FINAL_EMPTY','checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'cnf_sha256':a.cnf_sha,'proof_sha256':a.proof_sha,'counts':counts,'mutation_controls':controls,
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Exact CNF UNSAT conditional on checker soundness; no external DRAT checker or parent replay.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
