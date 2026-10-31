#!/usr/bin/env python3
"""Two independent exhaustive transversal enumerators on two explicit 2-MOLS nets."""
import argparse,hashlib,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
P=[('frontier-20261028-source-wanless-max2-first-pair-v1.txt','710f00cc7ad78afa54987d1b57938b9d0e9ae3ba30589383b82ee652d0102dfd',2),
   ('frontier-20261028-source-wanless-nonmax2-first-pair-v1.txt','2c32f66b0c4be0d995ff8db895e0b942034889ccd8523212f451bbab818a53a4',2),
   ('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',3)]
V=range(8)
def matrices(file,pin,k):
 b=(H/file).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('source hash')
 L=[s.strip() for s in b.decode('ascii').splitlines() if s.strip()]
 if L[0].split()[:2]!=['8','8'] or len(L)<1+8*k:raise ValueError('layout')
 out=[[[ord(c)-97 for c in L[1+8*j+i]] for i in V] for j in range(k)]
 for M in out:
  if any(set(row)!=set(V) for row in M) or any({M[i][j] for i in V}!=set(V) for j in V):raise ValueError('not Latin')
 for a,b in itertools.combinations(range(k),2):
  if len({(out[a][i][j],out[b][i][j]) for i in V for j in V})!=64:raise ValueError('not orthogonal')
 return out

def brute(T):
 out=[];l1=l2=0
 for p in itertools.permutations(V):
  a=len({T[0][i][p[i]] for i in V})==8;b=len({T[1][i][p[i]] for i in V})==8
  l1+=a;l2+=b
  if a and b:out.append(p)
 return out,l1,l2

def dfs(T):
 result=[];nodes=0
 def rec(i,C,A,B,p):
  nonlocal nodes
  nodes+=1
  if i==8:result.append(tuple(p));return
  for j in V:
   c=1<<j;a=1<<T[0][i][j];b=1<<T[1][i][j]
   if not(C&c or A&a or B&b):rec(i+1,C|c,A|a,B|b,p+[j])
 rec(0,0,0,0,[])
 return result,nodes

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 first=matrices(*P[0]);second=matrices(*P[1]);triple=matrices(*P[2])
 if triple[:2]!=second:raise ValueError('nonmax source pair does not equal the first explicit triple')
 cases=[]
 for name,T in [('maximal-source-first',first),('nonmaximal-source-first',second)]:
  a1,l1,l2=brute(T);a2,nodes=dfs(T)
  if a1!=a2:raise ValueError('independent enumeration mismatch')
  cases.append({'label':name,'permutations_scanned':40320,'common_transversals':len(a1),
                'all_common_transversals':[list(x) for x in a1],'first_square_only':l1,'second_square_only':l2,'dfs_nodes':nodes})
 if cases[0]['common_transversals']!=0 or cases[1]['common_transversals']!=16:raise ValueError('unexpected counts')
 # A real third MOLS supplies 8 explicit disjoint common transversals.
 classes=[]
 for k in V:
  p=tuple(next(j for j in V if triple[2][i][j]==k) for i in V)
  if p not in [tuple(z) for z in cases[1]['all_common_transversals']]:raise ValueError('extension class not transversal')
  classes.append(list(p))
 if len({(i,classes[k][i]) for i in V for k in V})!=64:raise ValueError('classes do not partition board')
 invalid=list(classes[0]);invalid[1]=invalid[0]
 if len(set(invalid))==8:raise ValueError('duplicate-column mutation accepted')
 out={'result':'PASS_ZERO_VS_SIXTEEN_COMMON_TRANSVERSALS',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'source_pins':{name:pin for name,pin,k in P},'cases':cases,
      'explicit_third_MOLS_symbol_classes':classes,'triple_pairwise_orthogonal':True,
      'duplicate_column_control':'rejected','elapsed_seconds':time.monotonic()-start,
      'limits':'Exact two-net finite checks; no external maximality/classification or quantum-family claim.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('cases','explicit_third_MOLS_symbol_classes')},indent=2))
 print('cases',[(x['label'],x['common_transversals'],x['first_square_only'],x['second_square_only'],x['dfs_nodes']) for x in cases])
if __name__=='__main__':main()
