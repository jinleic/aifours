#!/usr/bin/env python3
"""Bounded exact screening of catalogue 3-MOLS via real-flat necessary conditions.

Checks input Latin/orthogonal-array consistency, all ordered row/column class
choices, and all 30 affine-plane structures on the first-row labels. The
catalogue's external species completeness is a separate, unproved import.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time

HERE=pathlib.Path(__file__).parent
PINS={'max':('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',114),
      'nonmax':('frontier-20261028-source-wanless-nonmax3-order8-v1.txt','f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5',3)}
V=range(8); COMBS=list(itertools.combinations(V,4));LIMIT=40.0


def read_catalogue(filename,pin,n_squares):
 data=(HERE/filename).read_bytes()
 if hashlib.sha256(data).hexdigest()!=pin:raise ValueError('source snapshot hash mismatch')
 lines=[line.strip() for line in data.decode('ascii').splitlines() if line.strip()]
 h=lines.pop(0).split()
 if h[:3]!=['8','8',str(n_squares)] or len(lines)!=8*n_squares:raise ValueError('source header/row count')
 if any(len(row)!=8 or any(ch not in 'abcdefgh' for ch in row) for row in lines):raise ValueError('source row alphabet')
 squares=[[[ord(lines[8*k+i][j])-97 for j in V] for i in V] for k in range(n_squares)]
 if len(squares)%3:raise ValueError('source square grouping')
 out=[]
 for pos in range(0,len(squares),3):
  trip=squares[pos:pos+3]
  for s in trip:
   if any(set(s[i])!=set(V) for i in V) or any({s[i][j] for i in V}!=set(V) for j in V):
    raise ValueError('catalogue Latin condition')
  for a,b in itertools.combinations(range(3),2):
   if len({(trip[a][i][j],trip[b][i][j]) for i in V for j in V})!=64:
    raise ValueError('catalogue pairwise orthogonality')
  out.append(trip)
 return out


def plane_structures():
 systems={}
 for p in itertools.permutations(range(1,8)):
  f=(0,)+p
  sig=tuple(sorted(sum(1<<j for j in C) for C in COMBS if f[C[0]]^f[C[1]]^f[C[2]]^f[C[3]]==0))
  if len(sig)!=14:raise ValueError('affine plane count')
  systems.setdefault(sig,f)
 if len(systems)!=30:raise ValueError('affine-label structure count')
 return [(set(sig),list(f)) for sig,f in sorted(systems.items())]


def relabel_oa(trip,r,c):
 points=[(i,j,*(trip[k][i][j] for k in range(3))) for i in V for j in V]
 board=[[None]*8 for _ in V]
 for point in points:
  i,j=point[r],point[c]
  if board[i][j] is not None:raise ValueError('OA strength-two duplicate')
  board[i][j]=point
 if any(board[i][j] is None for i in V for j in V):raise ValueError('OA strength-two omission')
 others=[d for d in range(5) if d not in (r,c)]
 inv=[]
 for d in others:
  first=[board[0][j][d] for j in V]
  if len(set(first))!=8:raise ValueError('first-row symbol permutation')
  rev={symbol:j for j,symbol in enumerate(first)};inv.append(rev)
 return [[[inv[a][board[i][j][d]] for j in V] for i in V] for a,d in enumerate(others)]


def core(eligible,mates):
 # Each of five actual net lines through a heavy cell must have >=4 heavy cells.
 lines=[[] for _ in range(40)];memberships=[]
 for x in range(64):
  i,j=divmod(x,8);ids=(i,8+j,16+mates[0][i][j],24+mates[1][i][j],32+mates[2][i][j])
  memberships.append(ids)
  for line in ids:lines[line].append(x)
 active=set(eligible);counts=[sum(x in active for x in line) for line in lines]
 queue=collections.deque(x for x in active if any(counts[d]<4 for d in memberships[x]))
 while queue:
  x=queue.popleft()
  if x not in active or all(counts[d]>=4 for d in memberships[x]):continue
  active.remove(x)
  for d in memberships[x]:
   counts[d]-=1
   if counts[d]==3:
    for y in lines[d]:
     if y in active:queue.append(y)
 return len(active)


def eligible_for(mates,planes):
 out=[]
 for i in range(1,8):
  for j in V:
   labels=(j,*(mates[k][i][j] for k in range(3)))
   if len(set(labels))!=4:raise ValueError('actual forbidden labels not distinct')
   mask=sum(1<<v for v in labels)
   if mask in planes:out.append(8*i+j)
 return out


def mul(a,b):
 z=0
 for _ in range(3):
  if b&1:z^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return z


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic()
 triples=read_catalogue(*PINS['max'])+read_catalogue(*PINS['nonmax'])
 if len(triples)!=39:raise ValueError('catalogue triple count')
 geometries=plane_structures()
 standard=next(planes for planes,mapping in geometries if mapping==list(V))
 aff=lambda slopes:[[[j^mul(a,i) for j in V] for i in V] for a in slopes]
 pos=eligible_for(aff((1,2,3)),standard)
 neg=eligible_for(aff((1,2,4)),standard)
 if len(pos)!=56 or core(pos,aff((1,2,3)))!=56 or len(neg)!=0:
  raise ValueError('analytic affine zero-sum/nonzero-sum controls failed')
 records=[];eligible_hist=collections.Counter();core_hist=collections.Counter();complete=True
 species_summary=[]
 for index,trip in enumerate(triples):
  if time.monotonic()-start>LIMIT:complete=False;break
  species_eligible=species_core=species_surv=0
  orient_summary=[]
  for r in range(5):
   for c in range(5):
    if r==c:continue
    mates=relabel_oa(trip,r,c)
    Es=[];Cs=[]
    for planes,mapping in geometries:
     E=eligible_for(mates,planes);k=core(E,mates)
     Es.append(len(E));Cs.append(k);eligible_hist[len(E)]+=1;core_hist[k]+=1
     if k>=24:species_surv+=1
    species_eligible=max(species_eligible,max(Es));species_core=max(species_core,max(Cs))
    orient_summary.append({'row_class':r,'column_class':c,'eligible_counts_by_geometry':Es,'core_counts_by_geometry':Cs})
  records.append({'species_index':index,'catalogue':'maximal' if index<38 else 'nonmaximal',
                  'max_eligible':species_eligible,'max_core':species_core,
                  'contexts_core_ge24':species_surv,'orientations':orient_summary})
  species_summary.append({'species_index':index,'max_core':species_core,'contexts_core_ge24':species_surv})
 if complete and len(records)!=39:raise ValueError('incomplete species census')
 report={'result':'COMPLETE_RELAXATION_SCREEN' if complete else 'PARTIAL_TIME_BOUND',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'catalogue_snapshot_pins':{k:v[1] for k,v in PINS.items()},
         'catalogue_origin':'https://users.monash.edu.au/~iwanless/data/MOLS/; maximal snapshot reader-paged/normalized whitespace',
         'species_completed':len(records),'ordered_row_column_choices_per_species':20,
         'affine_plane_structures_per_orientation':len(geometries),
         'contexts_checked':sum(core_hist.values()),'eligible_histogram':dict(sorted(eligible_hist.items())),
         'core_histogram':dict(sorted(core_hist.items())),
         'contexts_core_ge24':sum(v for k,v in core_hist.items() if k>=24),
         'species_summary':species_summary,'geometry_representatives':[m for _,m in geometries],
         'records':records,'complete':complete,
         'affine_zero_sum_control_eligible_core':[len(pos),core(pos,aff((1,2,3)))],
         'affine_nonzero_sum_control_eligible':len(neg),'elapsed_seconds':time.monotonic()-start,
         'limits':'Necessary XOR-plane/5-line min4 core only. Any global statement is conditional on external catalogue species completeness and independently checked symmetry/real-flat theorem.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ('records','geometry_representatives')},indent=2))

if __name__=='__main__':main()
