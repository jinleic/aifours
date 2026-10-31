#!/usr/bin/env python3
"""Independent forward RUP checker for ASCII proofs; deletions may be retained.

Each added clause must individually pass reverse unit propagation. RAT-only
proofs are rejected. Input/proof are byte-hashed and parsed in full.
"""
import argparse,hashlib,json,pathlib,time

def parse_cnf(data):
 lines=data.decode('ascii').splitlines();header=None;clauses=[]
 for line in lines:
  v=line.split()
  if not v or v[0]=='c':continue
  if v[0]=='p':
   if header is not None or len(v)!=4 or v[1]!='cnf':raise ValueError('bad header')
   header=(int(v[2]),int(v[3]));continue
  if header is None:raise ValueError('header missing')
  z=list(map(int,v))
  if not z or z[-1]!=0 or 0 in z[:-1] or any(abs(k)>header[0] for k in z[:-1]):raise ValueError('bad CNF clause')
  if len(z)==1:raise ValueError('input contains empty clause')
  clauses.append(tuple(z[:-1]))
 if header is None or len(clauses)!=header[1]:raise ValueError('wrong CNF clause count')
 return header,clauses

def parse_proof(data,n):
 if not data.endswith(b'\n'):raise ValueError('unterminated proof')
 steps=[]
 for line in data.decode('ascii').splitlines():
  v=line.split()
  if not v:raise ValueError('blank proof line')
  deleted=(v[0]=='d');v=v[1:] if deleted else v
  z=list(map(int,v))
  if not z or z[-1]!=0 or 0 in z[:-1] or any(abs(k)>n for k in z[:-1]):raise ValueError('bad proof clause')
  steps.append((deleted,tuple(z[:-1])))
 if not steps or steps[-1]!=(False,()):raise ValueError('final empty clause missing')
 return steps

class Checker:
 def __init__(self,n,clauses):
  self.n=n;self.clauses=[];self.occ={};self.unit=[]
  for c in clauses:self.add(c)
 def add(self,c):
  i=len(self.clauses);self.clauses.append(c)
  for lit in c:self.occ.setdefault(lit,[]).append(i)
  if len(c)==1:self.unit.append(c[0])
 def rup(self,c):
  values=[0]*(self.n+1);remaining=[len(z) for z in self.clauses];satisfied=[0]*len(self.clauses);queue=[]
  def assign(lit):
   i=abs(lit);v=1 if lit>0 else -1
   if values[i]==-v:return False
   if values[i]==0:values[i]=v;queue.append(lit)
   return True
  for lit in self.unit:
   if not assign(lit):return True
  for lit in c:
   if not assign(-lit):return True
  pos=0
  while pos<len(queue):
   lit=queue[pos];pos+=1
   for i in self.occ.get(lit,()):satisfied[i]+=1
   for i in self.occ.get(-lit,()):
    remaining[i]-=1
    if satisfied[i]:continue
    if remaining[i]<=1:
     # Values may include assignments queued but not yet processed.  Check
     # the whole clause before declaring a conflict or propagating a unit.
     if any(values[abs(z)]==(1 if z>0 else -1) for z in self.clauses[i]):continue
     cand=[z for z in self.clauses[i] if values[abs(z)]==0]
     if not cand:return True
     if len(cand)==1 and not assign(cand[0]):return True
  return False

def verify(cnf,proof):
 (n,m),clauses=parse_cnf(cnf);steps=parse_proof(proof,n);ck=Checker(n,clauses);added=deleted=0
 for is_del,c in steps:
  if is_del:deleted+=1;continue  # retaining clauses preserves RUP soundness
  if not ck.rup(c):raise ValueError('non-RUP addition at step '+str(added+deleted+1))
  added+=1
  if c:ck.add(c)
 return {'variables':n,'original_clauses':m,'proof_steps':len(steps),'rup_additions':added,'ignored_deletions':deleted}

def main():
 p=argparse.ArgumentParser();p.add_argument('--cnf',required=True);p.add_argument('--proof',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--proof-sha',required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 C=pathlib.Path(a.cnf).read_bytes();P=pathlib.Path(a.proof).read_bytes()
 if hashlib.sha256(C).hexdigest()!=a.cnf_sha or hashlib.sha256(P).hexdigest()!=a.proof_sha:raise ValueError('input hash mismatch')
 counts=verify(C,P)
 controls={}
 for name,c,pf in [('truncated_proof',C,P.rsplit(b'\n',2)[0]+b'\n'),
                   ('sat_formula_empty_proof',b'p cnf 2 1\n1 2 0\n',b'0\n'),
                   ('wrong_formula',b'p cnf 2176 1\n1 0\n',P)]:
  try:verify(c,pf)
  except (ValueError,UnicodeError):controls[name]='rejected'
  else:raise ValueError('control passed '+name)
 report={'result':'PASS_EVERY_STEP_RUP_INCLUDING_FINAL_EMPTY',
         'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'cnf_sha256':a.cnf_sha,'proof_sha256':a.proof_sha,'cnf_bytes':len(C),'proof_bytes':len(P),
         'counts':counts,'mutation_controls':controls,'elapsed_seconds':time.monotonic()-start,
         'limits':'Exact CNF UNSAT only, conditional on checker correctness; CNF-to-physics reduction and Hcat are separate. No external drat-trim parent replay.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
