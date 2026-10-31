#!/usr/bin/env python3
"""Independent explicit-Kronecker verifier for three real QLS; stdlib only."""
import argparse,copy,hashlib,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-three-family-mixed8-witness-v1.json';PIN='a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413'
class ShapeError(ValueError):pass
class NormError(ValueError):pass
class RowGramError(ValueError):pass
class ColumnGramError(ValueError):pass
class PairGramError(ValueError):pass
class HashError(ValueError):pass

def parse(raw,pin):
 if hashlib.sha256(raw).hexdigest()!=pin:raise HashError('witness hash mismatch')
 def uniq(pairs):
  z={}
  for k,v in pairs:
   if k in z:raise ShapeError('duplicate JSON key')
   z[k]=v
  return z
 w=json.loads(raw,object_pairs_hook=uniq)
 needed={'kind','source_triple_index','source_square_index','quantum_square_numerators','quantum_square_denominator_squared','classical_mates','trade_cells','normalization','limits'}
 if set(w)!=needed:raise ShapeError('unexpected JSON keys')
 return w

def verify(w,n):
 Q=w['quantum_square_numerators'];D=w['quantum_square_denominator_squared'];M=w['classical_mates']
 if len(Q)!=n*n or len(D)!=n*n or len(M)!=2 or any(len(row)!=n for row in Q):raise ShapeError('Q dimensions')
 for row,d in zip(Q,D):
  if type(d)!=int or d not in (1,2) or any(type(v)!=int or v not in (-1,0,1) for v in row) or sum(v*v for v in row)!=d:raise NormError('invalid ray norm')
 if any(len(L)!=n or any(len(row)!=n or any(type(v)!=int or v not in range(n) for v in row) for row in L) for L in M):raise ShapeError('mate dimensions/labels')
 # Three numerator-vector arrays; each physical vector is raw/sqrt(den^2).
 raw=[Q,[],[]];den=[D,[1]*(n*n),[1]*(n*n)]
 for idx,L in enumerate(M,1):
  raw[idx].extend([[int(k==L[i][j]) for k in range(n)] for i in range(n) for j in range(n)])
 def dot(a,b):return sum(x*y for x,y in zip(a,b))
 for q in range(3):
  for i in range(n):
   for j in range(n):
    for k in range(n):
     x=n*i+j;y=n*i+k
     if dot(raw[q][x],raw[q][y])!=(den[q][x] if j==k else 0):raise RowGramError('row ONB')
     x=n*j+i;y=n*k+i
     if dot(raw[q][x],raw[q][y])!=(den[q][x] if j==k else 0):raise ColumnGramError('column ONB')
 # Explicit n^2-dimensional Kronecker vectors, not product-of-Gram shortcut.
 pairs=0
 for q in range(3):
  for r in range(q+1,3):
   T=[[a*b for a in raw[q][x] for b in raw[r][x]] for x in range(n*n)]
   for x in range(n*n):
    for y in range(n*n):
     if dot(T[x],T[y])!=(den[q][x]*den[r][x] if x==y else 0):raise PairGramError('pair-product ONB')
     pairs+=1
 if any(D[j]!=1 or Q[j]!=[int(k==j) for k in range(n)] for j in range(n)):raise ShapeError('first row not standard')
 mixed=[x for x,row in enumerate(Q) if sum(v!=0 for v in row)>1]
 return {'n':n,'row_gram_entries':3*n*n*n,'column_gram_entries':3*n*n*n,'tensor_gram_entries':pairs,'mixed_cells':mixed}

def small_four():
 # Three classical MOLS over GF(4), independently built as standard vectors.
 def mult(a,b):
  out=0
  for _ in range(2):
   if b&1:out^=a
   b>>=1;a<<=1
   if a&4:a^=7
  return out
 S=[[[j^mult(t,i) for j in range(4)] for i in range(4)] for t in (1,2,3)]
 # Relabel first square's first row, already 0..3.
 return {'quantum_square_numerators':[[int(k==S[0][i][j]) for k in range(4)] for i in range(4) for j in range(4)],
         'quantum_square_denominator_squared':[1]*16,'classical_mates':S[1:]}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic();raw=(H/FILE).read_bytes()
 w=parse(raw,PIN);result=verify(w,8)
 if result['mixed_cells']!=[18,19,26,27,36,37,44,45] or len(result['mixed_cells'])!=8:raise ShapeError('mixed set')
 small=verify(small_four(),4)
 controls={}
 def require(name,mut,expected):
  z=copy.deepcopy(w);mut(z)
  try:verify(z,8)
  except expected:controls[name]=expected.__name__
  except Exception as e:raise ValueError(name+' wrong failure '+repr(e))
  else:raise ValueError(name+' accepted')
 require('duplicate_quantum_same_row',lambda z:(z['quantum_square_numerators'].__setitem__(19,z['quantum_square_numerators'][18][:]),z['quantum_square_denominator_squared'].__setitem__(19,z['quantum_square_denominator_squared'][18])),RowGramError)
 require('duplicate_classical_mate',lambda z:z['classical_mates'].__setitem__(1,copy.deepcopy(z['classical_mates'][0])),PairGramError)
 require('drop_quantum_cell',lambda z:z['quantum_square_numerators'].pop(),ShapeError)
 require('wrong_quantum_norm',lambda z:z['quantum_square_denominator_squared'].__setitem__(18,1),NormError)
 require('out_of_range_mate',lambda z:z['classical_mates'][0][0].__setitem__(0,8),ShapeError)
 try:parse(raw,'0'*64)
 except HashError:controls['wrong_expected_hash']='HashError'
 else:raise ValueError('hash mutation accepted')
 out={'result':'PASS_EXPLICIT_TENSOR_THREE_FAMILY_GRAMS','checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'witness_sha256':PIN,'actual':result,'gf4_positive':small,'intended_reason_controls':controls,
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Owner-local third implementation, not separately owned/cross-model witness acceptance or novelty clearance. No fourth mate shown.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
