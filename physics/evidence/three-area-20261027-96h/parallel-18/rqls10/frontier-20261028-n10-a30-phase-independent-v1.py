#!/usr/bin/env python3
"""A.30 all 252 halves, independent literal matrix and Q(i,sqrt3) arithmetic."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
S=[
 ['1','1','1','1','1','1','1','1','1','1'],
 ['1','1','-i','i','i','-i','w4','w4','w8','w8'],
 ['1','1','i','-1','-1','i','w11','w11','w7','w7'],
 ['1','i','w8','w10','w7','w11','a','-a','w4','w4'],
 ['1','i','w4','w2','w11','w7','w8','w8','b','-b'],
 ['1','-i','w8','w4','w7','w5','ai','-ai','w1','w1'],
 ['1','-i','w4','w8','w11','w1','w5','w5','bi','-bi'],
 ['1','-1','1','-1','1','-1','aw11','-aw11','bw7','-bw7'],
 ['1','-1','-i','-i','i','i','aw7','-aw7','bw11','-bw11'],
 ['1','-1','i','1','-1','-i','-a','a','-b','b']]
def parse(s):
 e=0;p=q=0
 if s.startswith('-'):e+=6;s=s[1:]
 if s.startswith('a'):p=1;s=s[1:]
 elif s.startswith('b'):q=1;s=s[1:]
 if s=='i':e+=3
 elif s.startswith('w'):e+=int(s[1:])
 elif s not in ('','1'):raise ValueError(s)
 return (e%12,p,q)
K=[[parse(x)for x in row]for row in S]
Z=(0,0,0,0);ONE=(1,0,0,0)
# 2*zeta12^k, in integral basis 1,i,sqrt3,i sqrt3.
roots=[(2,0,0,0),(0,1,1,0),(1,0,0,1),(0,2,0,0),(-1,0,0,1),(0,1,-1,0),(-2,0,0,0),(0,-1,-1,0),(-1,0,0,-1),(0,-2,0,0),(1,0,0,-1),(0,-1,1,0)]
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def neg(x):return tuple(-a for a in x)
def mul(x,y):
 out=[0]*4
 for i,a in enumerate(x):
  for j,b in enumerate(y):
   r=i//2+j//2;s=i%2+j%2;out[(r%2)*2+s%2]+=a*b*(3 if r>=2 else 1)*(-1 if s>=2 else 1)
 return tuple(out)
def conj(x):return (x[0],-x[1],x[2],-x[3])
def poly(pairs):
 out={}
 for x,y in pairs:
  e,a,b=x;f,c,d=y;k=(c-a,d-b);out[k]=add(out.get(k,Z),roots[(f-e)%12])
 return {k:v for k,v in out.items()if v!=Z}
for i,j in itertools.combinations(range(10),2):
 assert not poly((K[t][i],K[t][j])for t in range(10))
 assert not poly((K[i][t],K[j][t])for t in range(10))
def classify(p):
 if not p:return 'free'
 if len(p)==1:return 'impossible'
 if len(p)>2:return 'multi'
 a,b=p.values();return 'binary' if mul(a,conj(a))==mul(b,conj(b)) else 'impossible'
def eq(poly0):
 (a,x),(b,y)=sorted(poly0.items());d=(b[0]-a[0],b[1]-a[1]);num=neg(x);den=y
 if d[0]<0 or d[0]==0 and d[1]<0:d=(-d[0],-d[1]);num,den=den,num
 return d,num,den
def pw(x,n):
 out=ONE
 for _ in range(n):out=mul(out,x)
 return out
def substitute(p,var,n,d):
 lo=min(k[var]for k in p);hi=max(k[var]for k in p);out={}
 for k,v in p.items():
  w=mul(v,mul(pw(n,k[var]-lo),pw(d,hi-k[var])));j=k[1-var];out[j]=add(out.get(j,Z),w)
 return {k:v for k,v in out.items()if v!=Z}
def pairs(vertices):
 if not vertices:yield ();return
 a=vertices[0]
 for i,b in enumerate(vertices[1:],1):
  for m in pairs(vertices[1:i]+vertices[i+1:]):yield ((a,b),)+m
ALL=list(pairs(list(range(10))));assert len(ALL)==945
counts=collections.Counter();eligible_halves=0;total_match=0;out=P/'frontier-20261028-n10-a30-phase-independent-v1.jsonl'
with out.open('w') as fp:
 for E in itertools.combinations(range(10),5):
  polys={(i,j):poly((K[t][i],K[t][j])for t in E)for i,j in itertools.combinations(range(10),2)};typ={e:classify(p)for e,p in polys.items()};nm=0
  for match in ALL:
   if any(typ[e]=='impossible' for e in match):continue
   nm+=1;total_match+=1;seen={};bad=False;multi=[]
   for edge in match:
    if typ[edge]=='multi':multi.append(edge)
    if typ[edge]=='binary':
     x,n,d=eq(polys[edge])
     if x in seen and mul(n,seen[x][1])!=mul(seen[x][0],d):bad=True
     seen[x]=(n,d)
   if bad:status='inconsistent_binomials'
   elif (1,0) in seen and (0,1) in seen:status='both_parameters_in_field_direct'
   elif len(seen)==1 and len(multi)==1:
    x,(n,d)=next(iter(seen.items()));assert x in [(1,0),(0,1)];var=0 if x==(1,0) else 1;red=substitute(polys[multi[0]],var,n,d)
    assert len(red)==2 and max(red)-min(red)==1;status='both_parameters_in_field_substitution'
   else:status='UNRESOLVED'
   counts[status]+=1;fp.write(json.dumps({'E':E,'matching':match,'status':status},separators=(',',':'))+'\n')
  eligible_halves+=bool(nm)
# Generic source row/column pair 5+5 multiplicity, a,b treated as independent.
rowpairs=[];colpairs=[]
for i,j in itertools.combinations(range(10),2):
 def ratios(aa):
  return collections.Counter(((y[0]-x[0])%12,y[1]-x[1],y[2]-x[2])for x,y in aa)
 if sorted(ratios((K[i][t],K[j][t])for t in range(10)).values())==[5,5]:rowpairs.append((i,j))
 if sorted(ratios((K[t][i],K[t][j])for t in range(10)).values())==[5,5]:colpairs.append((i,j))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'symbolic_row_and_column_gram_pairs':90,'halves':252,'eligible_halves':eligible_halves,
 'possible_matchings':total_match,'counts':dict(counts),'generic_row_ratio_5plus5':rowpairs,'generic_column_ratio_5plus5':colpairs,'status':'PASS' if not counts['UNRESOLVED'] else 'UNRESOLVED'}
(P/'frontier-20261028-n10-a30-phase-independent-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
