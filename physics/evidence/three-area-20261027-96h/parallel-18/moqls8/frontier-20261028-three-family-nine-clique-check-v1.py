#!/usr/bin/env python3
"""Exact per-edge verification of a 9-vector obstruction to any fourth mate."""
import argparse,copy,hashlib,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-three-family-mixed8-witness-v1.json';PIN='a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413'
CELLS=[0,1,2,9,17,18,19,26,37]
class BadClique(ValueError):pass
class MissingEdge(ValueError):pass
def check(w,cells):
 if len(cells)!=9 or len(set(cells))!=9 or any(x not in range(64) for x in cells):raise BadClique('nine distinct board cells required')
 Q=w['quantum_square_numerators'];M=w['classical_mates']
 if len(Q)!=64 or len(M)!=2:raise ValueError('shape')
 out=[]
 for x,y in itertools.combinations(cells,2):
  i,j=divmod(x,8);k,l=divmod(y,8);d=sum(a*b for a,b in zip(Q[x],Q[y]));why=[]
  if i==k:why.append('same_row')
  if j==l:why.append('same_column')
  if M[0][i][j]==M[0][k][l]:why.append('same_A_symbol')
  if M[1][i][j]==M[1][k][l]:why.append('same_B_symbol')
  if d!=0:why.append('nonzero_Q_overlap')
  if not why:raise MissingEdge(f'{x},{y}')
  out.append({'cells':[x,y],'reasons':why,'Q_integer_dot':d})
 return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic();raw=(H/FILE).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=PIN:raise ValueError('witness hash')
 w=json.loads(raw);edges=check(w,CELLS)
 if len(edges)!=36:raise ValueError('edge count')
 controls={}
 try:check(w,CELLS[:-1])
 except BadClique:controls['missing_vertex']='BadClique'
 else:raise ValueError('missing vertex accepted')
 bad=copy.deepcopy(w);bad['quantum_square_numerators'][18]=[0,0,1,0,0,0,0,0]
 try:check(bad,CELLS)
 except MissingEdge as e:
  if str(e)!='0,18':raise ValueError('quantum mutation wrong missing edge '+str(e))
  controls['remove_unique_quantum_edge']='MissingEdge:0,18'
 else:raise ValueError('quantum mutation accepted')
 bad=copy.deepcopy(w);bad['classical_mates'][1][2][1]=2
 try:check(bad,CELLS)
 except MissingEdge as e:
  if str(e)!='0,17':raise ValueError('mate mutation wrong missing edge '+str(e))
  controls['remove_unique_classical_edge']='MissingEdge:0,17'
 else:raise ValueError('mate mutation accepted')
 out={'result':'PASS_NINE_CELLS_ALL_36_FORCED_ORTHOGONALITY_EDGES',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'witness_sha256':PIN,
      'cells':CELLS,'edges':edges,'forced_vectors':9,'output_dimension':8,'mutation_controls':controls,
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Given the pinned three-family, any ordinary fourth QLS would require these 9 orthogonal 8D rays. Independent written and witness reviews remain separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='edges'},indent=2))
if __name__=='__main__':main()
