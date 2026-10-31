#!/usr/bin/env python3
"""Bounded DIMACS search for four real-flat MOQLS(8), restricted first row.

CNF uses 6-bit even-parity sign rays and gated XOR forbidden-pattern clauses.
A SAT assignment is checked from original 8-dimensional sign vectors. UNKNOWN
or UNSAT is not a global result, and no unchecked proof is promoted.
"""
import argparse
import hashlib
import itertools
import json
import pathlib
import resource
import subprocess
import time

N=8;M=4


def gf8mul(a,b):
 out=0
 for _ in range(3):
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out


def raw_walsh(label):
 return sum(1<<(x-1) for x in range(1,8) if (label&x).bit_count()&1)


def encode6(raw):
 low=raw&63
 if (raw>>6)&1 != low.bit_count()%2:raise ValueError('reference ray has odd parity')
 return low


def decode7(v):return v|((v.bit_count()%2)<<6)


def isorth6(a,b):return (a^b).bit_count() in (3,4)


def gram8(a,b):return 8-2*(decode7(a)^decode7(b)).bit_count()


def direct_check(arr):
 err={'row_gram_errors':0,'column_gram_errors':0,'pair_product_gram_errors':0}
 for a in range(M):
  for i in range(N):
   for j in range(N):
    for k in range(N):
     want=8 if j==k else 0
     err['row_gram_errors']+=gram8(arr[a][i][j],arr[a][i][k])!=want
     err['column_gram_errors']+=gram8(arr[a][j][i],arr[a][k][i])!=want
 for a in range(M):
  for b in range(a+1,M):
   for x in range(N*N):
    i,j=divmod(x,N)
    for y in range(N*N):
     k,l=divmod(y,N);want=64 if x==y else 0
     err['pair_product_gram_errors']+=gram8(arr[a][i][j],arr[a][k][l])*gram8(arr[b][i][j],arr[b][k][l])!=want
 return err


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prefix',required=True);args=ap.parse_args()
 prefix=pathlib.Path(args.prefix)
 if not prefix.name.startswith('frontier-20261028-'):raise ValueError('invalid output prefix')
 start=time.monotonic()
 base=[[[encode6(raw_walsh(gf8mul(a+1,i)^j)) for j in range(N)] for i in range(N)] for a in range(M)]
 bad=[[row[:] for row in square] for square in base];bad[1]=[row[:] for row in bad[0]]
 good_check=direct_check(base);bad_check=direct_check(bad)
 if any(good_check.values()) or bad_check['row_gram_errors'] or bad_check['column_gram_errors'] or not bad_check['pair_product_gram_errors']:
  raise ValueError('physical Gram controls failed')
 clauses=[];varcount=0
 base_value=[False];bad_value=[False]
 good_failed=bad_failed=target_failed=0
 def var(v1,v2):
  nonlocal varcount
  varcount+=1;base_value.append(bool(v1));bad_value.append(bool(v2));return varcount
 def clause(items,category='base'):
  nonlocal good_failed,bad_failed,target_failed
  lits=tuple(items)
  if not lits:raise ValueError('unexpected empty clause')
  if not any(base_value[abs(v)] == (v>0) for v in lits):
   if category=='target':target_failed+=1
   else:good_failed+=1
  if category!='target' and not any(bad_value[abs(v)] == (v>0) for v in lits):bad_failed+=1
  clauses.append(' '.join(map(str,lits))+' 0\n')
 q=[[[[0]*6 for _ in range(N)] for _ in range(N)] for _ in range(M)]
 for a in range(M):
  for i in range(N):
   for j in range(N):
    for k in range(6):q[a][i][j][k]=var((base[a][i][j]>>k)&1,(bad[a][i][j]>>k)&1)
 for a in range(M):
  for j in range(N):
   val=encode6(raw_walsh(j))
   for k in range(6):clause([q[a][0][j][k] if (val>>k)&1 else -q[a][0][j][k]])
 def xorvars(a,x,y):
  i,j=divmod(x,N);k,l=divmod(y,N);out=[]
  for bit in range(6):
   u=q[a][i][j][bit];v=q[a][k][l][bit]
   z=var(base_value[u]^base_value[v],bad_value[u]^bad_value[v]);out.append(z)
   clause([-u,-v,-z]);clause([u,v,-z]);clause([u,-v,z]);clause([-u,v,z])
  return out
 def forbid(z,patterns,gate=None,category='base'):
  for pattern in patterns:
   term=[] if gate is None else [-gate]
   term += [-z[k] if (pattern>>k)&1 else z[k] for k in range(6)]
   clause(term,category)
 nonorth=[p for p in range(64) if p.bit_count() not in (3,4)]
 line_count=0
 for a in range(M):
  for line in range(N):
   for j in range(N):
    for k in range(j+1,N):
     forbid(xorvars(a,line*N+j,line*N+k),nonorth)
     forbid(xorvars(a,j*N+line,k*N+line),nonorth)
     line_count+=2
 pair_count=0
 for x in range(N*N):
  i,j=divmod(x,N)
  for y in range(x+1,N*N):
   k,l=divmod(y,N)
   if i==k or j==l:continue
   gates=[]
   for a in range(M):
    z=xorvars(a,x,y)
    g=var(isorth6(base[a][i][j],base[a][k][l]),isorth6(bad[a][i][j],bad[a][k][l]));gates.append(g)
    forbid(z,nonorth,gate=g)
   for a,b in itertools.combinations(range(M),2):clause([gates[a],gates[b]])
   pair_count+=1
 target=xorvars(0,0,9)
 forbid(target,[p for p in range(64) if p.bit_count() not in (1,2,5,6)],category='target')
 if good_failed!=0 or bad_failed==0 or target_failed==0:raise ValueError(f'CNF encoded controls failed {good_failed,bad_failed,target_failed}')
 cnf=prefix.with_name(prefix.name+'-input.cnf')
 with cnf.open('x',encoding='ascii') as h:
  h.write(f'p cnf {varcount} {len(clauses)}\n');h.writelines(clauses)
 # Leave the original input/artifacts in place; do not clean or overwrite.
 def cap():
  limit=1536*1024*1024
  resource.setrlimit(resource.RLIMIT_AS,(limit,limit))
 cmd=['kissat','--sat','--time=15','--conflicts=100000','--seed=20261028',str(cnf)]
 try:
  proc=subprocess.run(cmd,capture_output=True,text=True,check=False,timeout=25,preexec_fn=cap)
  stdout,stderr,rc=proc.stdout,proc.stderr,proc.returncode;outer_timeout=False
 except subprocess.TimeoutExpired as exc:
  stdout=exc.stdout.decode() if isinstance(exc.stdout,bytes) else (exc.stdout or '')
  stderr=exc.stderr.decode() if isinstance(exc.stderr,bytes) else (exc.stderr or '')
  rc=None;outer_timeout=True
 out=prefix.with_name(prefix.name+'-kissat-stdout.txt');err=prefix.with_name(prefix.name+'-kissat-stderr.txt')
 with out.open('x',encoding='utf-8') as h:h.write(stdout)
 with err.open('x',encoding='utf-8') as h:h.write(stderr)
 status='INCOMPLETE';candidate_sha=None;model_errors=None;target_w=None
 if 's SATISFIABLE' in stdout:
  signs={}
  for line in stdout.splitlines():
   if line.startswith('v '):
    for text in line.split()[1:]:
     lit=int(text)
     if lit:signs[abs(lit)]=lit>0
  if all(q[a][i][j][k] in signs for a in range(M) for i in range(N) for j in range(N) for k in range(6)):
   arr=[[[sum((1<<k) for k in range(6) if signs[q[a][i][j][k]]) for j in range(N)] for i in range(N)] for a in range(M)]
   model_errors=direct_check(arr);target_w=(arr[0][0][0]^arr[0][1][1]).bit_count()
   if not any(model_errors.values()) and target_w in (1,2,5,6):
    cp=prefix.with_name(prefix.name+'-candidate.json')
    with cp.open('x',encoding='utf-8') as h:
     json.dump({'ray_masks6':arr,'decode':'bits1..6 + parity bit7, first sign+','physical_errors':model_errors,'target_weight6':target_w},h,indent=2);h.write('\n')
    candidate_sha=hashlib.sha256(cp.read_bytes()).hexdigest();status='SAT_EXACT_FULL_GRAM_CHECKED_REQUIRES_INDEPENDENT_WITNESS_REVIEW'
   else:status='SAT_MODEL_REJECTED_BY_DIRECT_PHYSICAL_CHECKER'
  else:status='SAT_ASSIGNMENT_INCOMPLETE'
 elif 's UNSATISFIABLE' in stdout:status='UNSAT_RESTRICTED_CNF_SOLVER_RESULT_PROOF_NOT_CHECKED'
 elif 's UNKNOWN' in stdout or outer_timeout:status='UNKNOWN_OR_TIMEOUT_RESTRICTED_CNF'
 report={'result':status,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'cnf_sha256':hashlib.sha256(cnf.read_bytes()).hexdigest(),'solver_argv':cmd,'solver_exit':rc,
         'solver_stdout_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'solver_stderr_sha256':hashlib.sha256(err.read_bytes()).hexdigest(),
         'outer_timeout':outer_timeout,'address_space_limit_bytes':1536*1024*1024,
         'variables':varcount,'clauses':len(clauses),'line_pairs':line_count,'off_line_cell_pairs':pair_count,
         'baseline_cnf_base_failures':good_failed,'duplicate_square_cnf_base_failures':bad_failed,
         'baseline_target_failures_expected':target_failed,'baseline_physical_check':good_check,'duplicate_square_physical_check':bad_check,
         'candidate_sha256':candidate_sha,'candidate_physical_errors':model_errors,'target_sixbit_weight':target_w,
         'elapsed_seconds':time.monotonic()-start,
         'limits':'Restricted real-flat sign rays, fixed Walsh first rows, selected target cell; no global result. SAT needs independently written triple verification; UNSAT needs proof replay.'}
 rp=prefix.with_name(prefix.name+'-receipt.json')
 with rp.open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':main()
