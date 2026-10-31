#!/usr/bin/env python3
"""Exact one-common-coordinate witnesses in all 39 pinned order-8 3-MOLS nets."""
import argparse,hashlib,itertools,json,pathlib
H=pathlib.Path(__file__).parent
PINS=[('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',114),
      ('frontier-20261028-source-wanless-nonmax3-order8-v1.txt','f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5',3)]
V=range(8)
def catalogue(name,sha,n):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=sha:raise ValueError('snapshot hash')
 L=[s.strip() for s in b.decode('ascii').splitlines() if s.strip()]
 if L[0].split()[:3]!=['8','8',str(n)] or len(L)!=8*n+1:raise ValueError('snapshot layout')
 squares=[[[ord(c)-97 for c in L[1+8*k+i]] for i in V] for k in range(n)]
 for Q in squares:
  if any(set(Q[i])!=set(V) for i in V) or any({Q[i][j] for i in V}!=set(V) for j in V):raise ValueError('not Latin')
 result=[]
 for k in range(0,n,3):
  T=squares[k:k+3]
  if any(len({(T[a][i][j],T[b][i][j]) for i in V for j in V})!=64 for a,b in itertools.combinations(range(3),2)):raise ValueError('not MOLS')
  result.append(T)
 return result

def orient(T,r,c):
 pts=[(i,j,*(T[k][i][j] for k in range(3))) for i in V for j in V]
 board={(p[r],p[c]):p for p in pts}
 if len(board)!=64:raise ValueError('OA not strength two')
 other=[k for k in range(5) if k not in (r,c)]
 inv=[{board[0,j][k]:j for j in V} for k in other]
 if any(len(x)!=8 for x in inv):raise ValueError('firstrow')
 return [[[inv[a][board[i,j][k]] for j in V] for i in V] for a,k in enumerate(other)]

def witness(T):
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(8,64)}
 allowed={x:set(V)-set(f[1:]) for x,f in facts.items()}
 if any(len(S)!=4 for S in allowed.values()):raise ValueError('bad forbidden labels')
 for a in range(5):
  for v in V:
   line=[x for x in facts if facts[x][a]==v]
   for x,y in itertools.combinations(line,2):
    intersection=sorted(allowed[x]&allowed[y])
    if len(intersection)==1:return {'line_class':a,'line_symbol':v,'cells':[x,y],
      'allowed_first_row_axes':[sorted(allowed[x]),sorted(allowed[y])],'intersection':intersection}
 return None

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 triples=sum((catalogue(*p) for p in PINS),[])
 if len(triples)!=39:raise ValueError('species count')
 output=[]
 for i,T in enumerate(triples):
  found=None
  for r,c in itertools.permutations(range(5),2):
   w=witness(orient(T,r,c))
   if w is not None:found={'species_index':i,'row_class':r,'column_class':c,**w};break
  if found is None:raise ValueError('no witness in species '+str(i))
  output.append(found)
 result={'result':'ALL_39_SPECIES_HAVE_OVERLAP_ONE_WITNESS','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'snapshots':{p[0]:p[1] for p in PINS},'witnesses':output,
         'limits':'Exact incidence witnesses only; catalogue completeness and mathematical forcing proof are separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(result,h,indent=2);h.write('\n')
 print(json.dumps({'result':result['result'],'source_sha256':result['source_sha256'],'species':len(output),
                   'orientations':{str(x):sum((w['row_class'],w['column_class'])==x for w in output) for x in {(w['row_class'],w['column_class']) for w in output}},
                   'first_witness':output[0],'last_witness':output[-1]},indent=2))
if __name__=='__main__':main()
