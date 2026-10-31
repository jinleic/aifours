#!/usr/bin/env python3
"""Exact six-axis/three-disjoint-support size and pairing coverage audit."""
import argparse,collections,hashlib,itertools,json,pathlib,time

def partitions(xs):
 if not xs:yield ();return
 x=xs[0]
 for j in range(1,len(xs)):
  for rest in partitions(xs[1:j]+xs[j+1:]):yield ((x,xs[j]),)+rest

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 axes=(2,3,4,5,6,7);hist=collections.Counter();words=0
 for z in itertools.product(range(4),repeat=6):
  sizes=tuple(sorted(z.count(k) for k in (1,2,3)))
  if 0 in sizes:continue
  hist[sizes]+=1;words+=1
 expected={(1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,2,2),(1,2,3),(2,2,2)}
 if set(hist)!=expected:raise ValueError('size coverage')
 pp=list(partitions(axes))
 if len(pp)!=15 or len(set(pp))!=15:raise ValueError('pairing coverage')
 # Each member-labelled pairing maps to one unordered partition, exactly 3! times.
 labelled=[x for p0 in pp for x in itertools.permutations(p0)]
 if len(labelled)!=90 or len(set(labelled))!=90:raise ValueError('S3 orbit')
 if sum(hist.values())!=words:raise ValueError('histogram mismatch')
 out={'result':'PASS_SIX_AXIS_Q3_SUPPORT_SIZE_AND_PAIRING_COVERAGE',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'all_coordinate_assignments_checked':4**6,'nonempty_disjoint_labelled_assignments':words,
      'unordered_size_histogram':{str(k):v for k,v in sorted(hist.items())},
      'unordered_saturated_pairings':[[list(x) for x in z] for z in pp],
      'labelled_saturated_pairings':len(labelled),'elapsed_seconds':time.monotonic()-start,
      'limits':'Finite local combinatorics only; no claim of realizable QLS supports, global family or excluded stratum.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='unordered_saturated_pairings'},indent=2))
if __name__=='__main__':main()
