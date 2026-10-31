#!/usr/bin/env python3
"""Bounded exact CSP for one affine 5-net and a real-flat quantum square.

A solution is directly checked against all original row/column and pair-product
ONBs. An exhaustive no-solution result is conditional on this finite class and
requires separate checker review; a timeout means UNKNOWN.
"""
import argparse
import collections
import hashlib
import json
import pathlib
import time

N=8
SLOPES=(1,2,3)  # 1 xor 2 xor 3 = 0 in the chosen GF(8) encoding.
LIMIT_SECONDS=18.0


def mul(a,b):
 out=0
 for _ in range(3):
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out


def raw7(a):return a|((a.bit_count()%2)<<6)


def gram8(a,b):return 8-2*(raw7(a)^raw7(b)).bit_count()


def walsh6(label):
 raw=sum(1<<(x-1) for x in range(1,8) if (label&x).bit_count()&1)
 lo=raw&63
 if raw7(lo)!=raw:raise ValueError('Walsh encoding invalid')
 return lo


def support(a):
 return [j for j in range(N) if gram8(a,walsh6(j))!=0]


def classes(x):
 i,j=divmod(x,N)
 return (i,j,*(j^mul(a,i) for a in SLOPES))


def full_check(Q):
 labels=[[[j^mul(a,i) for j in range(N)] for i in range(N)] for a in SLOPES]
 rowerr=colerr=pairerr=0
 for i in range(N):
  for j in range(N):
   for k in range(N):
    want=8 if j==k else 0
    rowerr+=gram8(Q[8*i+j],Q[8*i+k])!=want
    colerr+=gram8(Q[8*j+i],Q[8*k+i])!=want
 for L in labels:
  for i in range(N):
   for j in range(N):
    for k in range(N):
     rowerr+=(L[i][j]==L[i][k])!=(j==k)
     colerr+=(L[j][i]==L[k][i])!=(j==k)
 squares=4
 for a in range(squares):
  for b in range(a+1,squares):
   for x in range(64):
    i,j=divmod(x,8)
    for y in range(64):
     k,l=divmod(y,8);want=8 if x==y else 0
     if a==0:
      actual=gram8(Q[x],Q[y])*(labels[b-1][i][j]==labels[b-1][k][l])
     else:
      actual=8*(labels[a-1][i][j]==labels[a-1][k][l])*(labels[b-1][i][j]==labels[b-1][k][l])
     pairerr+=actual!=want
 return {'row_gram_errors':int(rowerr),'column_gram_errors':int(colerr),
         'pair_product_gram_errors':int(pairerr)}


def members(mask):
 while mask:
  b=mask&-mask;yield b.bit_length()-1;mask-=b


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prefix',required=True);args=ap.parse_args()
 prefix=pathlib.Path(args.prefix)
 if not prefix.name.startswith('frontier-20261028-'):raise ValueError('invalid output prefix')
 start=time.monotonic()
 ref=[walsh6(j) for j in range(N)]
 qsupport=[support(a) for a in range(64)]
 if sorted(len(z) for z in qsupport)!=[1]*8+[4]*56:raise ValueError('ray alphabet classification failed')
 orth=[]
 for a in range(64):
  mask=0
  for b in range(64):
   if gram8(a,b)==0:mask|=1<<b
  orth.append(mask)
 facts=[classes(x) for x in range(64)]
 neighbors=[tuple(y for y in range(64) if y!=x and any(facts[x][c]==facts[y][c] for c in range(5))) for x in range(64)]
 if any(len(z)!=35 for z in neighbors):raise ValueError('incidence is not five independent classes')
 allmask=(1<<64)-1
 domains=[allmask for _ in range(64)]
 for j in range(8):domains[j]=1<<ref[j]
 # Normalize one hypothesized nonclassical cell to (1,0). Restricted if the
 # net automorphism/flat-frame action is not separately reviewed.
 anchor=8
 heavy=sum(1<<a for a in range(64) if len(qsupport[a])==4)
 domains[anchor]&=heavy
 for x in range(8,64):
  forbidden=[facts[x][c] for c in (1,2,3,4)]
  if len(set(forbidden))!=4:raise ValueError('classical mate labels collided')
  for k in forbidden:domains[x]&=orth[ref[k]]
  if domains[x].bit_count()!= (4 if x==anchor else 8):raise ValueError('initial domain count mismatch')
 # Positive classical control: L(i,j)=j+4i is orthogonal to all three mates.
 classic=[walsh6(j^mul(4,i)) for i in range(8) for j in range(8)]
 good=full_check(classic)
 if any(good.values()):raise ValueError('classical four-family physical positive control failed')
 bad=classic[:];bad[9]=bad[8]
 negative=full_check(bad)
 if not negative['row_gram_errors']:raise ValueError('duplicate-cell physical negative control failed')
 stats={'nodes':0,'arc_revisions':0,'domain_values_removed':0,'failures':0,'max_depth':0,'timed_out':False}
 def propagate(D,queue):
  while queue:
   x,y=queue.popleft();stats['arc_revisions']+=1
   if stats['arc_revisions']%2048==0 and time.monotonic()-start>LIMIT_SECONDS:
    stats['timed_out']=True;return False
   old=D[x];new=0
   for r in members(old):
    if orth[r]&D[y]:new|=1<<r
   if new!=old:
    stats['domain_values_removed']+=old.bit_count()-new.bit_count();D[x]=new
    if new==0:stats['failures']+=1;return False
    for z in neighbors[x]:
     if z!=y:queue.append((z,x))
  return True
 def search(D,depth):
  stats['nodes']+=1;stats['max_depth']=max(stats['max_depth'],depth)
  if time.monotonic()-start>LIMIT_SECONDS:stats['timed_out']=True;return None
  branch=[x for x in range(64) if D[x].bit_count()>1]
  if not branch:return D
  x=min(branch,key=lambda z:(D[z].bit_count(),-sum(D[y].bit_count()>1 for y in neighbors[z])))
  for r in members(D[x]):
   child=D.copy();child[x]=1<<r
   if propagate(child,collections.deque((y,x) for y in neighbors[x])):
    ans=search(child,depth+1)
    if ans is not None:return ans
   if stats['timed_out']:return None
  return None
 initial=domains.copy()
 root_ok=propagate(initial,collections.deque((x,y) for x in range(64) for y in neighbors[x]))
 solution=search(initial,0) if root_ok and not stats['timed_out'] else None
 candidate_sha=None;verified=None
 if solution is not None:
  rays=[next(members(d)) for d in solution];verified=full_check(rays)
  if any(verified.values()) or len(qsupport[rays[anchor]])!=4:raise ValueError('CSP solution failed full physical verification')
  candidate={'Q_sign_masks6':rays,'three_classical_mate_slopes':list(SLOPES),
             'field':'GF(2)[x]/(x^3+x+1)','first_row':ref,'physical_errors':verified,
             'nonclassical_anchor_cell':[1,0],'anchor_support':qsupport[rays[anchor]],
             'limits':'Exact actual candidate from one affine 5-net; independent witness review still required.'}
  cp=prefix.with_name(prefix.name+'-candidate.json')
  with cp.open('x',encoding='utf-8') as h:json.dump(candidate,h,indent=2);h.write('\n')
  candidate_sha=hashlib.sha256(cp.read_bytes()).hexdigest();outcome='SAT_EXACT_PHYSICAL_FULL_GRAM_NEEDS_INDEPENDENT_REVIEW'
 elif stats['timed_out']:outcome='UNKNOWN_TIME_BOUND'
 else:outcome='EXHAUSTED_NO_SOLUTION_FOR_RESTRICTED_ANCHOR_INTERNAL_CHECK_ONLY'
 report={'result':outcome,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'field':'GF(2)[x]/(x^3+x+1)','slopes':list(SLOPES),'one_nonclassical_anchor':[1,0],
         'initial_anchor_domain_size':domains[anchor].bit_count(),
         'initial_domain_histogram':dict(collections.Counter(d.bit_count() for d in domains)),
         'root_propagation_succeeded':root_ok,'search_statistics':stats,
         'positive_classical_control':good,'duplicate_cell_negative_control':negative,
         'candidate_full_physical_errors':verified,'candidate_sha256':candidate_sha,
         'elapsed_seconds':time.monotonic()-start,
         'limits':'One affine 5-net, one anchor, real-flat rays. Timeout is UNKNOWN; any exhaustiveness claim requires independently reviewed solver.'}
 rp=prefix.with_name(prefix.name+'-receipt.json')
 with rp.open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':main()
