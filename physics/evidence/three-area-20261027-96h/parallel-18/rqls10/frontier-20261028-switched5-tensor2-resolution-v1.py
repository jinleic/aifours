#!/usr/bin/env python3
"""Exact finite CSP for a new order10 resolution from a 5x5 switched QLS.
A SAT output is only a candidate until separately checked from original vectors.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import z3
P=Path(__file__).resolve().parent
M=[[0,1,2,3,4],[1,0,3,4,2],[2,3,4,0,1],[3,4,1,2,0],[4,2,0,1,3]]
# 2x2 intercalate on rows/cols 0,1 is rotated by rational (3/5,4/5).
def basis(i):return tuple(5*int(i==j)for j in range(5))
U=(3,4,0,0,0);V=(-4,3,0,0,0)
Q=[[basis(M[r][c])for c in range(5)]for r in range(5)]
Q[0][0]=Q[1][1]=U;Q[0][1]=Q[1][0]=V
assert all(sum(x*y for x,y in zip(z,z))==25 for row in Q for z in row)
for a,b in itertools.combinations(range(5),2):
 assert all(sum(x*y for x,y in zip(Q[r][a],Q[r][b]))==0 for r in range(5))
 assert all(sum(x*y for x,y in zip(Q[a][c],Q[b][c]))==0 for c in range(5))
VTX=list(itertools.product(range(5),range(2),range(5),range(2)))
L={x:z3.Int('L%d%d%d%d'%x)for x in VTX};S=z3.Solver();S.set(timeout=60000,random_seed=13)
for x in VTX:S.add(L[x]>=0,L[x]<10)
for r,u in itertools.product(range(5),range(2)):S.add(z3.Distinct([L[r,u,c,v]for c,v in itertools.product(range(5),range(2))]))
for c,v in itertools.product(range(5),range(2)):S.add(z3.Distinct([L[r,u,c,v]for r,u in itertools.product(range(5),range(2))]))
for x,y in itertools.combinations(VTX,2):
 r,u,c,v=x;s,w,d,z=y
 if (u+v)%2==(w+z)%2 and sum(a*b for a,b in zip(Q[r][c],Q[s][d]))!=0:S.add(L[x]!=L[y])
for c,v in itertools.product(range(5),range(2)):S.add(L[0,0,c,v]==2*c+v)
begin=time.monotonic();status=S.check();sec=time.monotonic()-begin
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'solver':'Z3 '+z3.get_version_string(),'timeout_ms':60000,'elapsed_seconds':round(sec,6),'status':str(status),
 'unknown_reason':S.reason_unknown()if status==z3.unknown else None,'source_Latin':M,'rotation_numerators':[3,4,5],
 'boundary':'SAT must be independently reconstructed and checked from original 10-dimensional vectors; UNSAT is solver-scoped, not a general no-go.'}
if status==z3.sat:
 mod=S.model();rows=[[int(mod.eval(L[r,u,c,v]).as_long())for c,v in itertools.product(range(5),range(2))]for r,u in itertools.product(range(5),range(2))]
 obj.update(resolution=rows,ray_count=14)
(P/'frontier-20261028-switched5-tensor2-resolution-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
