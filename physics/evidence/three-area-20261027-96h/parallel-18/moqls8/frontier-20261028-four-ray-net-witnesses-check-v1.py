#!/usr/bin/env python3
"""Independent direct-OA verification of all 39 overlap-one witnesses."""
import argparse,copy,hashlib,itertools,json,pathlib
H=pathlib.Path(__file__).parent
P=[('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',114),
   ('frontier-20261028-source-wanless-nonmax3-order8-v1.txt','f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5',3)]
CERT='ef0ba2988184474cd55cbcf7c0e6b52fa11e2d168bda04df2978138cfbc1ebc9'
def readpin(name,pin):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('hash')
 return b

def load():
 nets=[]
 for name,pin,n in P:
  L=[s.strip() for s in readpin(name,pin).decode('ascii').splitlines() if s.strip()]
  if L[0].split()[:3]!=['8','8',str(n)] or len(L)!=8*n+1:raise ValueError('layout')
  S=[[[ord(ch)-97 for ch in L[1+8*k+i]] for i in range(8)] for k in range(n)]
  for a in S:
   if any(sorted(z)!=list(range(8)) for z in a):raise ValueError('row Latin')
   if any(sorted(a[i][j] for i in range(8))!=list(range(8)) for j in range(8)):raise ValueError('column Latin')
  for k in range(0,n,3):
   T=S[k:k+3]
   for a,b in itertools.combinations(range(3),2):
    if len({(T[a][i][j],T[b][i][j]) for i in range(8) for j in range(8)})!=64:raise ValueError('not orthogonal')
   nets.append([(i,j,T[0][i][j],T[1][i][j],T[2][i][j]) for i in range(8) for j in range(8)])
 return nets

def verify(net,rec):
 r,c=rec['row_class'],rec['column_class']
 if r not in range(5) or c not in range(5) or r==c:raise ValueError('orientation')
 def point(x):
  i,j=divmod(x,8)
  z=[p for p in net if p[r]==i and p[c]==j]
  if len(z)!=1:raise ValueError('not OA2')
  return z[0]
 other=[k for k in range(5) if k not in (r,c)]
 def norm(x):
  p=point(x);out=[x//8,x%8]
  for k in other:
   match=[j for j in range(8) if point(j)[k]==p[k]]
   if len(match)!=1:raise ValueError('first row normalization')
   out.append(match[0])
  return out
 x,y=rec['cells']
 if not (8<=x<64 and 8<=y<64 and x!=y):raise ValueError('cells')
 X,Y=norm(x),norm(y);k=rec['line_class'];v=rec['line_symbol']
 if k not in range(5) or X[k]!=v or Y[k]!=v:raise ValueError('different line')
 F1=set(X[1:]);F2=set(Y[1:])
 if len(F1)!=4 or len(F2)!=4:raise ValueError('forbidden labels')
 A=sorted(set(range(8))-F1);B=sorted(set(range(8))-F2);C=sorted(set(A)&set(B))
 if [A,B]!=rec['allowed_first_row_axes'] or C!=rec['intersection'] or len(C)!=1:raise ValueError('overlap-one mismatch')

def validate(nets,cert):
 W=cert['witnesses']
 if len(nets)!=39 or len(W)!=39 or [w['species_index'] for w in W]!=list(range(39)):raise ValueError('species coverage')
 for net,rec in zip(nets,W):verify(net,rec)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 nets=load();C=json.loads(readpin('frontier-20261028-four-ray-net-witnesses-v1.json',CERT));validate(nets,C)
 cases=[('missing_species',lambda z:z['witnesses'].pop()),
        ('wrong_line',lambda z:z['witnesses'][0].update({'line_symbol':8})),
        ('duplicate_cell',lambda z:z['witnesses'][0]['cells'].__setitem__(1,z['witnesses'][0]['cells'][0])),
        ('altered_allowed_axis',lambda z:z['witnesses'][1]['allowed_first_row_axes'][0].__setitem__(0,9)),
        ('invalid_orientation',lambda z:z['witnesses'][38].update({'row_class':z['witnesses'][38]['column_class']}))]
 checks={}
 for name,mutation in cases:
  z=copy.deepcopy(C);mutation(z)
  try:validate(nets,z)
  except (ValueError,IndexError,KeyError):checks[name]='rejected'
  else:raise ValueError('mutation passed '+name)
 out={'result':'PASS_ALL_39_INDEPENDENT_ONE_COORDINATE_WITNESSES',
      'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'certificate_sha256':CERT,'species':39,'orientations_01':38,'orientations_10':1,'mutation_controls':checks,
      'limits':'Finite witness check; Hcat and written forcing argument not verified by this code.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
