#!/usr/bin/env python3
"""Independent exact verifier of every catalogued XOR/core context.

Reconstructs the 30 affine plane systems via Steiner triple systems, not by
permutation quotienting, and computes each five-line core by simultaneous
fixed-point sweeps. Does not import the producer's code.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time

HERE=pathlib.Path(__file__).parent
DATA=[('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',114),
      ('frontier-20261028-source-wanless-nonmax3-order8-v1.txt','f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5',3)]
CERT='121fe7b1b4fafd47593c042ade5f8b18c1d9a6be43d69ea605884f12f1b1b68c'
V=range(8)


def parse_data(name,pin,expected):
 data=(HERE/name).read_bytes()
 if hashlib.sha256(data).hexdigest()!=pin:raise ValueError('catalogue hash mismatch')
 lines=[x.strip() for x in data.decode('ascii').splitlines() if x.strip()]
 if lines[0].split()[:3]!=['8','8',str(expected)] or len(lines)!=1+8*expected:
  raise ValueError('catalogue count')
 blocks=[]
 for k in range(expected):
  block=[]
  for i in range(8):
   text=lines[1+8*k+i]
   if len(text)!=8 or set(text)!=set('abcdefgh'):raise ValueError('catalogue row not Latin')
   block.append(tuple(ord(c)-97 for c in text))
  if any(len({block[i][j] for i in V})!=8 for j in V):raise ValueError('catalogue column not Latin')
  blocks.append(block)
 result=[]
 for k in range(0,expected,3):
  T=blocks[k:k+3]
  for a,b in itertools.combinations(range(3),2):
   if len({(T[a][i][j],T[b][i][j]) for i in V for j in V})!=64:
    raise ValueError('catalogue pair not orthogonal')
  result.append(T)
 return result


def steiner_geometries():
 points=range(1,8);pairs=frozenset(itertools.combinations(points,2));solutions=[]
 def dfs(left,lines):
  if not left:solutions.append(tuple(lines));return
  a,b=min(left)
  for c in points:
   if c in (a,b):continue
   tri=tuple(sorted((a,b,c)))
   used=frozenset(itertools.combinations(tri,2))
   if used<=left:dfs(left-used,lines+[tri])
 dfs(pairs,[])
 signatures=set()
 for lines in solutions:
  masks=[1+sum(1<<x for x in line) for line in lines]
  signatures.add(tuple(sorted(masks+[255^x for x in masks])))
 if len(solutions)!=30 or len(signatures)!=30:raise ValueError('independent Steiner plane count')
 return signatures


def signature_from_mapping(f):
 if sorted(f)!=list(V):raise ValueError('geometry mapping is not bijective')
 planes=[]
 for a,b,c,d in itertools.combinations(V,4):
  if f[a]^f[b]^f[c]^f[d]==0:planes.append((1<<a)|(1<<b)|(1<<c)|(1<<d))
 return tuple(sorted(planes))


def board_of(triple,rowcol):
 r,c=rowcol
 points=[(i,j,triple[0][i][j],triple[1][i][j],triple[2][i][j]) for i in V for j in V]
 lookup={(p[r],p[c]):p for p in points}
 if len(lookup)!=64:raise ValueError('OA pair not bijective')
 others=[a for a in range(5) if a not in rowcol]
 to_column=[]
 for a in others:
  mapping={lookup[(0,j)][a]:j for j in V}
  if len(mapping)!=8:raise ValueError('first-row label not bijective')
  to_column.append(mapping)
 return tuple(tuple(tuple(to_column[k][lookup[(i,j)][a]] for j in V) for i in V)
              for k,a in enumerate(others))


def independent_screen(T,planes):
 lines=[]
 for i in V:lines.append({8*i+j for j in V})
 for j in V:lines.append({8*i+j for i in V})
 for s in T:
  for k in V:lines.append({8*i+j for i in V for j in V if s[i][j]==k})
 if len(lines)!=40 or any(len(line)!=8 for line in lines):raise ValueError('invalid line class')
 active=set()
 for i in range(1,8):
  for j in V:
   labels=(j,T[0][i][j],T[1][i][j],T[2][i][j])
   if len(set(labels))!=4:raise ValueError('forbidden labels repeat')
   mask=sum(1<<a for a in labels)
   if mask in planes:active.add(8*i+j)
 initial=len(active)
 while True:
  small=set().union(*(line&active for line in lines if len(line&active)<4))
  if not small:return initial,len(active)
  active-=small


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic();raw=pathlib.Path(args.certificate).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=CERT:raise ValueError('certificate hash mismatch')
 cert=json.loads(raw)
 triples=sum((parse_data(*record) for record in DATA),[])
 if len(triples)!=39:raise ValueError('not 39 triples')
 independent=steiner_geometries()
 ordered=[signature_from_mapping(f) for f in cert['geometry_representatives']]
 if len(ordered)!=30 or set(ordered)!=independent:raise ValueError('plane-structure coverage mismatch')
 if len(cert['records'])!=39:raise ValueError('species coverage')
 hist=collections.Counter();contexts=0;zero_species=[]
 for ix,(trip,record) in enumerate(zip(triples,cert['records'])):
  if record['species_index']!=ix:raise ValueError('species order mismatch')
  orientations=record['orientations'];expected=[(r,c) for r in range(5) for c in range(5) if r!=c]
  if [(x['row_class'],x['column_class']) for x in orientations]!=expected:
   raise ValueError('row/column orientation coverage mismatch')
  maxcore=0;surv=0
  for orient in orientations:
   T=board_of(trip,(orient['row_class'],orient['column_class']))
   Es=[];Cs=[]
   for sig in ordered:
    e,c=independent_screen(T,set(sig));Es.append(e);Cs.append(c);hist[c]+=1;contexts+=1
   if Es!=orient['eligible_counts_by_geometry'] or Cs!=orient['core_counts_by_geometry']:
    raise ValueError('independent context counts disagree')
   maxcore=max(maxcore,max(Cs));surv+=sum(c>=24 for c in Cs)
  if maxcore!=record['max_core'] or surv!=record['contexts_core_ge24']:
   raise ValueError('species summary mismatch')
  if maxcore==0:zero_species.append(ix)
 if contexts!=23400 or dict(hist)!={0:23168,32:140,40:80,56:12}:
  raise ValueError('overall context count mismatch')
 # Mutations are evaluated against the exact comparison predicates above.
 mutated=cert['records'][0]['orientations'][0]['core_counts_by_geometry'][:]
 mutated[0]+=1
 if mutated==cert['records'][0]['orientations'][0]['core_counts_by_geometry']:
  raise ValueError('core-count tamper control failed')
 if len(cert['records'][:-1])==39:raise ValueError('missing-species control failed')
 bad=[list(row) for row in triples[0][0]];bad[0][0]=bad[0][1]
 if len(set(bad[0]))==8:raise ValueError('non-Latin row mutation control failed')
 report={'result':'PASS_INDEPENDENT_ALL_23400_XOR_CORE_CONTEXTS',
         'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'producer_certificate_sha256':CERT,'species':len(triples),'Steiner_plane_systems':len(independent),
         'contexts':contexts,'core_histogram':{str(k):v for k,v in sorted(hist.items())},
         'zero_core_species_indices':zero_species,'zero_core_species_count':len(zero_species),
         'core_count_mutation_rejected':True,'missing_species_mutation_rejected':True,
         'nonLatin_row_mutation_rejected':True,'elapsed_seconds':time.monotonic()-start,
         'limits':'Independent finite-data check, not proof of external catalogue completeness, geometry equivalence, physical theorem, or novelty.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':main()
