#!/usr/bin/env python3
"""Exact census of normalized 3-bit translation 5-nets; no QLS solver."""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time

V=tuple(range(8))


def compose(a,b):return tuple(a[b[x]] for x in V)


def plus(a,b):return tuple(a[x]^b[x] for x in V)


def isperm(a):return len(set(a))==8


def additive(a):return all(a[x^y]==(a[x]^a[y]) for x in V for y in V)


def linear_map(a,b,c):
 return tuple((a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0) for x in V)


def actual_net_check(A,B):
 maps=(V,A,B)
 arrays=[[[j^f[i] for j in V] for i in V] for f in maps]
 for square in arrays:
  if any(set(row)!=set(V) for row in square):return False
  if any({square[i][j] for i in V}!=set(V) for j in V):return False
 for x,y in itertools.combinations(range(3),2):
  if len({(arrays[x][i][j],arrays[y][i][j]) for i in V for j in V})!=64:return False
 return True


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic()
 normalized=[(0,)+p for p in itertools.permutations(range(1,8))]
 complete=[f for f in normalized if isperm(plus(f,V))]
 if len(complete)!=48 or not all(additive(f) for f in complete):
  raise ValueError('normalized complete-mapping lemma control failed')
 linear=[]
 for a,b,c in itertools.product(range(1,8),repeat=3):
  m=linear_map(a,b,c)
  if isperm(m):linear.append(m)
 if len(linear)!=168 or len(set(linear))!=168:raise ValueError('GL(3,2) enumeration failed')
 hist=collections.Counter();n=commuting=0;noncommuting_example=None;zero_D_checks=0
 for A in linear:
  if not isperm(plus(A,V)):continue
  for B in linear:
   if not isperm(plus(B,V)) or not isperm(plus(A,B)):continue
   n+=1
   if not actual_net_check(A,B):raise ValueError('actual 3-MOLS physical symbol-pair check failed')
   D=plus(plus(V,A),B);images=len(set(D))
   rank={1:0,2:1,4:2,8:3}.get(images)
   if rank is None:raise ValueError('nonlinear D image')
   hist[rank]+=1
   if compose(A,B)==compose(B,A):commuting+=1
   elif noncommuting_example is None:noncommuting_example=[list(A),list(B)]
   if rank==0:
    zero_D_checks+=1
    p=V
    for step in range(1,8):
     p=compose(A,p)
     if step<7 and p==V:raise ValueError('zero-D A has shorter order')
    if p!=V:raise ValueError('zero-D A does not have order7')
 if n!=576 or dict(hist)!={0:48,2:336,3:192}:raise ValueError('net histogram unexpected')
 # Invalid controls target different failure modes.
 if actual_net_check(V,V):raise ValueError('duplicate-square negative control not rejected')
 bad=(0,1,2,3,4,5,6,6)
 if isperm(bad):raise ValueError('nonpermutation negative control not rejected')
 report={'result':'PASS_EXACT_TRANSLATION_NET_CENSUS_NOT_FULL_NET_CLASSIFICATION',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'all_normalized_permutations':len(normalized),'normalized_complete_mappings':len(complete),
         'all_complete_mappings_additive':True,'invertible_linear_maps':len(linear),
         'actual_normalized_ordered_three_mols_nets':n,
         'D_rank_histogram':{str(k):v for k,v in sorted(hist.items())},
         'zero_D_operators_all_order7':zero_D_checks,
         'commuting_AB':commuting,'noncommuting_AB':n-commuting,
         'one_noncommuting_example':noncommuting_example,
         'all_576_actual_latin_and_pair_orthogonality_checked':True,
         'duplicate_square_control_rejected':True,'nonpermutation_control_rejected':True,
         'elapsed_seconds':time.monotonic()-start,
         'limits':'Translation-form nets only; q1 flat-Q obstruction and zero-D rank certificate require separately reviewed proofs.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':main()
