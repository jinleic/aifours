#!/usr/bin/env python3
"""Independent row-basis exhaustive checker for a restricted affine 5-net.

No CSP code is imported. Every allowed row is built as a pair of 4D ONBs;
complete pairwise row compatibility is then enumerated with a time cap.
The result does not cover non-affine nets or non-real-flat QLS.
"""
import argparse
import hashlib
import itertools
import json
import pathlib
import time

N=8
SLOPES=(0,1,2,3)
LIMIT=30.0


def mul(a,b):
 out=0
 for _ in range(3):
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out


def raw(a):return a|((a.bit_count()&1)<<6)


def ray(label):
 value=sum(1<<(x-1) for x in range(1,8) if (label&x).bit_count()&1)
 lo=value&63
 if raw(lo)!=value:raise ValueError('Walsh parity failure')
 return lo


ORTH=[(raw(d).bit_count()==4) for d in range(64)]
REF=tuple(ray(j) for j in range(8))
LIGHT=set(REF)


def compatible(i,a,k,b):
 diff=i^k
 for j in range(N):
  for slope in SLOPES:
   if not ORTH[a[j]^b[j^mul(slope,diff)]]:return False
 return True


def row_options(i,force_heavy=False):
 domains=[]
 for j in range(N):
  forbidden={j,*(j^mul(a,i) for a in (1,2,3))}
  if len(forbidden)!=4:raise ValueError('non-MOLS incidence')
  allowed=tuple(v for v in range(64) if all(ORTH[v^REF[x]] for x in forbidden))
  if len(allowed)!=8:raise ValueError('unexpected cell-domain size')
  domains.append(allowed)
 groups={}
 for j,D in enumerate(domains):groups.setdefault(D,[]).append(j)
 if len(groups)!=2 or any(len(c)!=4 for c in groups.values()):raise ValueError('row groups invalid')
 pieces=[]
 for domain,cols in sorted(groups.items()):
  choices=[]
  for heavy in (False,True):
   rays=[v for v in domain if (v not in LIGHT)==heavy]
   if len(rays)!=4 or not all(ORTH[a^b] for a,b in itertools.combinations(rays,2)):
    raise ValueError('light/heavy 4-basis property invalid')
   for perm in itertools.permutations(rays):choices.append((cols,perm))
  pieces.append(choices)
 for p0,p1 in itertools.product(*pieces):
  result=[-1]*8
  for cols,vals in (p0,p1):
   for j,v in zip(cols,vals):result[j]=v
  if not force_heavy or result[0] not in LIGHT:yield tuple(result)


def classical_row(i):return tuple(ray(j^mul(4,i)) for j in range(8))


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic();rows={i:list(row_options(i,i==1)) for i in range(1,5)}
 if [len(rows[i]) for i in range(1,5)]!=[1152,2304,2304,2304]:raise ValueError('row option count mismatch')
 # Positive physical control is deliberately checked without the heavy anchor.
 ctrl=[REF]+[classical_row(i) for i in range(1,5)]
 if not all(compatible(i,ctrl[i],k,ctrl[k]) for i in range(5) for k in range(i+1,5)):
  raise ValueError('classical partial net positive control failed')
 if classical_row(1)[0] not in LIGHT:raise ValueError('classical anchor control unexpectedly nonclassical')
 pairs=[];pair_tests=0
 for a in rows[1]:
  if time.monotonic()-start>LIMIT:break
  for b in rows[2]:
   pair_tests+=1
   if compatible(1,a,2,b):pairs.append((a,b))
 complete_pairs=pair_tests==len(rows[1])*len(rows[2])
 triples=[];triple_tests=0
 if complete_pairs:
  for a,b in pairs:
   if time.monotonic()-start>LIMIT:break
   for c in rows[3]:
    triple_tests+=1
    if compatible(1,a,3,c) and compatible(2,b,3,c):triples.append((a,b,c))
 complete_triples=complete_pairs and triple_tests==len(pairs)*len(rows[3])
 quads=[];quad_tests=0
 if complete_triples:
  for a,b,c in triples:
   if time.monotonic()-start>LIMIT:break
   for d in rows[4]:
    quad_tests+=1
    if compatible(1,a,4,d) and compatible(2,b,4,d) and compatible(3,c,4,d):quads.append((a,b,c,d))
 complete_quads=complete_triples and quad_tests==len(triples)*len(rows[4])
 if complete_quads and quads:status='PARTIAL_FIVE_ROW_CANDIDATES_FOUND_NOT_A_FULL_WITNESS'
 elif complete_quads:status='EXHAUSTED_NO_FIVE_ROW_COMPLETION_FOR_STATED_NET_AND_ANCHOR'
 else:status='UNKNOWN_TIME_BOUND'
 report={'result':status,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'field':'GF(2)[x]/(x^3+x+1)','three_classical_slopes':[1,2,3],
         'first_row_ray_masks6':list(REF),'anchor_heavy_cell':[1,0],
         'row_option_counts':{str(i):len(rows[i]) for i in rows},
         'pair_tests':pair_tests,'compatible_row1_row2_pairs':len(pairs),
         'triple_tests':triple_tests,'compatible_row1_row2_row3_triples':len(triples),
         'quad_tests':quad_tests,'compatible_row1_through_row4_quads':len(quads),
         'all_surviving_triples':[[list(a),list(b),list(c)] for a,b,c in triples],
         'complete_pairs':complete_pairs,'complete_triples':complete_triples,'complete_quads':complete_quads,
         'classical_five_row_positive_control':True,'anchor_control_classical_rejected':True,
         'elapsed_seconds':time.monotonic()-start,
         'limits':'This enumerates only first five rows with one heavy anchor of one affine net; no unrestricted MOQLS theorem, SAT proof, or independent acceptance.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':main()
