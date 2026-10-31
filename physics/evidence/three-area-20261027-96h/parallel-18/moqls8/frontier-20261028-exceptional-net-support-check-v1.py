#!/usr/bin/env python3
"""Independently verify both forcing trees and support clashes, with tamper controls."""
import argparse,copy,hashlib,itertools,json,pathlib
H=pathlib.Path(__file__).parent
P={'max':'95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',
   'screen':'121fe7b1b4fafd47593c042ade5f8b18c1d9a6be43d69ea605884f12f1b1b68c',
   'certificate':'3b0d3e0cda916f6f7f313b5bd147ed9e4961584afee87c3baedb88eae393b14e'}
def fetch(path,sha):
 b=(H/path).read_bytes()
 if hashlib.sha256(b).hexdigest()!=sha:raise ValueError('input hash')
 return b

def make_net():
 raw=fetch('frontier-20261028-source-wanless-max3-order8-v1.txt',P['max']).decode('ascii')
 words=[z for z in raw.splitlines() if z.strip()]
 if words[0].split()[:3]!=['8','8','114'] or len(words)!=913:raise ValueError('catalogue layout')
 blocks=[]
 for n in range(66,69):
  block=[[ord(c)-ord('a') for c in words[1+8*n+i].strip()] for i in range(8)]
  if any(sorted(row)!=list(range(8)) for row in block):raise ValueError('row not Latin')
  if any(sorted(block[i][j] for i in range(8))!=list(range(8)) for j in range(8)):raise ValueError('column not Latin')
  blocks.append(block)
 for a,b in itertools.combinations(range(3),2):
  if len({(blocks[a][i][j],blocks[b][i][j]) for i in range(8) for j in range(8)})!=64:raise ValueError('pair not orthogonal')
 mates=[]
 for b in blocks:
  inv=[b[0].index(k) for k in range(8)]
  mates.append([[inv[b[i][j]] for j in range(8)] for i in range(8)])
 labels={8*i+j:(i,j,*(m[i][j] for m in mates)) for i in range(8) for j in range(8)}
 return mates,labels

def eligible(labels,f):
 if sorted(f)!=list(range(8)):raise ValueError('not a geometry bijection')
 return {x for x,z in labels.items() if x>=8 and f[z[1]]^f[z[2]]^f[z[3]]^f[z[4]]==0}

def full_core(E,labels):
 active=E.copy()
 while True:
  bad=set()
  for a in range(5):
   for v in range(8):
    line={x for x in active if labels[x][a]==v}
    if len(line)<4:bad.update(line)
  if not bad:return active
  active-=bad

def validate(cert,screen,mates,labels):
 if cert['normalized_classical_mates']!=mates or cert['species_index']!=22:raise ValueError('net mismatch')
 orient=screen['records'][22]['orientations'][0]
 if (orient['row_class'],orient['column_class'])!=(0,1):raise ValueError('wrong orientation')
 geoms=screen['geometry_representatives']
 cores=[]
 for f in geoms:
  E=eligible(labels,f);cores.append(len(full_core(E,labels)))
 if cores!=orient['core_counts_by_geometry'] or [(i,c) for i,c in enumerate(cores) if c]!=[(2,32),(5,32)]:raise ValueError('30-geometry core check')
 if [c['geometry_index'] for c in cert['cases']]!=[2,5]:raise ValueError('case coverage')
 for c in cert['cases']:
  if c['geometry_map']!=geoms[c['geometry_index']]:raise ValueError('geometry mismatch')
  E=eligible(labels,c['geometry_map'])
  if sorted(E)!=c['eligible_cells'] or len(E)!=32:raise ValueError('eligible mismatch')
  classes=[[{x for x in E if labels[x][a]==v} for v in range(8)] for a in range(5)]
  counts=[[len(line) for line in C] for C in classes]
  if counts!=c['line_count_matrix'] or counts[0]!=[0,8,4,4,4,4,4,4] or any(r!=[4]*8 for r in counts[1:]):raise ValueError('line count mismatch')
  seen={c['tree_root']}
  if not seen<=E or len(c['forcing_tree'])!=31:raise ValueError('tree size/root')
  for edge in c['forcing_tree']:
   p,q,k,v=edge['parent'],edge['child'],edge['class'],edge['symbol']
   if k not in range(5) or v not in range(8) or p not in seen or q in seen or len(classes[k][v])!=4 or not {p,q}<=classes[k][v]:raise ValueError('invalid forcing edge')
   seen.add(q)
  if seen!=E:raise ValueError('tree not spanning')
  row2=classes[0][2]
  if sorted(row2)!=c['row2_four_heavy_cells'] or len(row2)!=4:raise ValueError('row2 mismatch')
  x,y=c['mismatch_cells']
  if x==y or not {x,y}<=row2:raise ValueError('support witnesses not distinct row cells')
  forb=[sorted(labels[q][1:]) for q in (x,y)]
  if any(len(set(z))!=4 for z in forb) or forb[0]==forb[1] or forb!=c['forbidden_labels']:raise ValueError('forbidden mismatch')
  supports=[sorted(set(range(8))-set(z)) for z in forb]
  if supports!=c['support_labels'] or supports[0]==supports[1]:raise ValueError('support not distinct')
 return True

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 cert=json.loads(fetch('frontier-20261028-exceptional-net-support-certificate-v1.json',P['certificate']))
 screen=json.loads(fetch('frontier-20261028-wanless-q1-xor-core-receipt-v1.json',P['screen']))
 mates,labels=make_net();validate(cert,screen,mates,labels)
 mutations={}
 for name,mut in [('missing_tree_edge',lambda x:x['cases'][0]['forcing_tree'].pop()),
                  ('wrong_tree_line',lambda x:x['cases'][0]['forcing_tree'][0].update({'class':9})),
                  ('same_support_witness',lambda x:x['cases'][1]['mismatch_cells'].__setitem__(1,x['cases'][1]['mismatch_cells'][0])),
                  ('missing_geometry',lambda x:x['cases'].pop()),
                  ('altered_net_label',lambda x:x['normalized_classical_mates'][0][1].__setitem__(0,99))]:
  bad=copy.deepcopy(cert);mut(bad)
  try:validate(bad,screen,mates,labels)
  except (ValueError,IndexError,KeyError):mutations[name]='rejected'
  else:raise ValueError(name+' tamper passed')
 result={'result':'PASS_BOTH_EXCEPTIONAL_SUPPORT_OBSTRUCTIONS',
         'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'certificate_sha256':P['certificate'],'source_snapshot_sha256':P['max'],
         'geometries_checked':30,'surviving':[2,5],'eligible_sizes':[32,32],
         'forcing_tree_edges':[31,31],'unequal_support_witnesses_verified':2,
         'mutation_controls':mutations,
         'limits':'Verifies finite incidence/labels, not written mathematical inference or catalogue completeness.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(result,h,indent=2);h.write('\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
