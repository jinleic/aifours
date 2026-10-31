#!/usr/bin/env python3
"""Select, for each net species, an orientation with zero core for all geometries."""
import argparse,hashlib,json,pathlib
H=pathlib.Path(__file__).parent
PINS={'screen':'121fe7b1b4fafd47593c042ade5f8b18c1d9a6be43d69ea605884f12f1b1b68c',
      'audit':'f3634c36eb50f2c88c3bb8de6113ea07d015a85e003267ab4be4b7483a737be0'}
def fetch(name,pin):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('pinned input hash')
 return json.loads(b)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 x=fetch('frontier-20261028-wanless-q1-xor-core-receipt-v1.json',PINS['screen'])
 y=fetch('frontier-20261028-wanless-q1-xor-core-check-receipt-v1.json',PINS['audit'])
 if not x['complete'] or x['contexts_checked']!=23400 or y['result']!='PASS_INDEPENDENT_ALL_23400_XOR_CORE_CONTEXTS':raise ValueError('unverified inputs')
 chosen=[];exceptional=[]
 for r in x['records']:
  good=[(o['row_class'],o['column_class']) for o in r['orientations'] if len(o['core_counts_by_geometry'])==30 and max(o['core_counts_by_geometry'])==0]
  if good:chosen.append({'species_index':r['species_index'],'chosen_row_column':good[0],'zero_orientations':len(good)})
  else:exceptional.append(r['species_index'])
 if len(chosen)!=38 or exceptional!=[22]:raise ValueError('unexpected orientation reduction')
 z=x['records'][22]['orientations'][0]
 if (z['row_class'],z['column_class'])!=(0,1):raise ValueError('exceptional orientation')
 remaining=[{'geometry_index':i,'core_size':c} for i,c in enumerate(z['core_counts_by_geometry']) if c]
 if remaining!=[{'geometry_index':2,'core_size':32},{'geometry_index':5,'core_size':32}]:raise ValueError('exceptional cores')
 report={'result':'PASS_38_SPECIES_ZERO_ORIENTATION_ONE_EXCEPTION','checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 'screen_sha256':PINS['screen'],'independent_screen_audit_sha256':PINS['audit'],'species_with_zero_orientation':chosen,
 'exceptional_species':exceptional,'exceptional_row_column':[0,1], 'exceptional_nonzero_geometries':remaining,
 'limits':'Selection from checked finite records only; application needs the all-five-line ONB reorientation and named real-flat inputs; catalogue completeness is external.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
