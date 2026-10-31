#!/usr/bin/env python3
"""Independent full-subset packing audit, tied to 8!-exhaustive counts."""
import argparse,collections,copy,csv,hashlib,io,json,pathlib,time
H=pathlib.Path(__file__).parent
P={'frontier-20261028-source-wanless-max2-complete-v1.txt':'6786f29c22c354673df942485faeed7d462ebaf4e3916b7a649cc0ff6a303154',
   'frontier-20261028-max2-transversal-exhaust-v1.csv':'379d3843d889cc1937e476788b5f57265cc95ece15f6e15cd276b224d585079d',
   'frontier-20261028-max2-transversal-packing-receipt-v1.json':'0090a1762bfd8299b14da8d5c60e99ba104dd2cc55076b0bd5daed731d8d16ba',
   'frontier-20261028-two-nets-transversal-census-receipt-v1.json':'651620bd2cfe0845648bcff0eb1bed952b433e179c1632461101acece6ca49b5'}
def pin(name):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=P[name]:raise ValueError('input hash '+name)
 return b

def maxpack(trans):
 masks=[sum(1<<(8*i+j) for i,j in enumerate(p)) for p in trans];n=len(masks)
 if n>19:raise ValueError('unsupported case size')
 adj=[sum(1<<j for j in range(n) if i!=j and not masks[i]&masks[j]) for i in range(n)]
 good=bytearray(1<<n);good[0]=1;best=0
 for subset in range(1,1<<n):
  bit=subset&-subset;i=bit.bit_length()-1;rest=subset^bit
  if good[rest] and rest&~adj[i]==0:
   good[subset]=1;best=max(best,subset.bit_count())
 return best

def validate_record(rec,T,expected):
 trans=rec['transversals']
 if len(trans)!=expected or len({tuple(p) for p in trans})!=expected:raise ValueError('transversal coverage')
 for p in trans:
  if sorted(p)!=list(range(8)) or any(len({T[k][i][p[i]] for i in range(8)})!=8 for k in range(2)):raise ValueError('invalid transversal')
 best=maxpack(trans);w=rec['packing_witness_indices']
 if best!=rec['maximum_disjoint'] or len(w)!=best or len(set(w))!=best or any(i not in range(len(trans)) for i in w):raise ValueError('packing maximum/witness')
 for i,j in __import__('itertools').combinations(w,2):
  if any(trans[i][r]==trans[j][r] for r in range(8)):raise ValueError('packing not disjoint')
 return best

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 rows=[s.strip() for s in pin('frontier-20261028-source-wanless-max2-complete-v1.txt').decode('ascii').splitlines() if s.strip()]
 if len(rows)!=34033 or rows[0].split()[:3]!=['8','8','4254']:raise ValueError('source layout')
 counts=list(csv.DictReader(io.StringIO(pin('frontier-20261028-max2-transversal-exhaust-v1.csv').decode('ascii'))))
 if len(counts)!=2127 or [int(r['index']) for r in counts]!=list(range(2127)) or any(int(r['permutations_tested'])!=40320 for r in counts):raise ValueError('count coverage')
 R=json.loads(pin('frontier-20261028-max2-transversal-packing-receipt-v1.json'));records=R['cases'];indices=[int(r['index']) for r in counts if int(r['common_transversals'])>0]
 if [r['index'] for r in records]!=indices or len(indices)!=147:raise ValueError('positive coverage')
 hist=collections.Counter();sample=None
 for rec in records:
  k=rec['index'];T=[[[ord(c)-97 for c in rows[1+16*k+8*j+i]] for i in range(8)] for j in range(2)]
  best=validate_record(rec,T,int(counts[k]['common_transversals']));hist[best]+=1
  if sample is None:sample=(rec,T,int(counts[k]['common_transversals']))
 if dict(hist)!={1:34,2:79,4:34}:raise ValueError('histogram')
 control=json.loads(pin('frontier-20261028-two-nets-transversal-census-receipt-v1.json'))['cases'][1]['all_common_transversals']
 if len(control)!=16 or maxpack(control)!=8:raise ValueError('extendible control')
 checks={}
 for name,mutation in [('claimed_maximum',lambda r:r.update({'maximum_disjoint':r['maximum_disjoint']+1})),
                       ('missing_transversal',lambda r:r['transversals'].pop()),
                       ('invalid_witness',lambda r:r['packing_witness_indices'].__setitem__(0,999))]:
  r=copy.deepcopy(sample[0]);mutation(r)
  try:validate_record(r,sample[1],sample[2])
  except (ValueError,IndexError):checks[name]='rejected'
  else:raise ValueError('mutation passed '+name)
 out={'result':'PASS_INDEPENDENT_ALL_147_FULL_SUBSET_PACKINGS',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'input_pins':P,
      'positive_pairs':len(records),'zero_pairs':2127-len(records),'maximum_packing_histogram':dict(sorted(hist.items())),
      'extendible_control_maximum':8,'mutation_controls':checks,'elapsed_seconds':time.monotonic()-start,
      'limits':'Exact finite data for pinned local 2-MOLS pairs; source classification and quantum claims are separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
