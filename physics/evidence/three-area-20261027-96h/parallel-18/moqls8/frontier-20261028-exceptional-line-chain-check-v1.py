#!/usr/bin/env python3
"""Check the exact short line chains printed in the accompanying proof."""
import argparse,hashlib,json,pathlib
H=pathlib.Path(__file__).parent
PIN='3b0d3e0cda916f6f7f313b5bd147ed9e4961584afee87c3baedb88eae393b14e'
CHAINS={2:[(1,0),(0,3),(0,5),(0,7),(2,0),(0,4),(0,6),(1,4),(0,2),(1,2),(1,3),(1,5),(1,6),(1,7)],
        5:[(1,0),(0,2),(0,4),(0,6),(2,0),(0,5),(0,7),(1,4),(0,3),(1,2),(1,3),(1,5),(1,6),(1,7)]}
def verify(c,case,chain):
 E=set(case['eligible_cells']);M=c['normalized_classical_mates'];seen={8}
 for k,s in chain:
  if k not in (0,1,2) or not 0<=s<8:raise ValueError('line label')
  def val(x):
   i,j=divmod(x,8)
   return i if k==0 else j if k==1 else M[0][i][j]
  line={x for x in E if val(x)==s}
  if len(line)!=4 or not line&seen or not line-seen:raise ValueError('invalid chain line')
  seen|=line
 if seen!=E:raise ValueError('chain misses eligible cells')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 b=(H/'frontier-20261028-exceptional-net-support-certificate-v1.json').read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('certificate hash')
 c=json.loads(b)
 for case in c['cases']:verify(c,case,CHAINS[case['geometry_index']])
 try:verify(c,c['cases'][0],CHAINS[2][:-1])
 except ValueError:omitted=True
 else:raise ValueError('omitted final line not detected')
 out={'result':'PASS_BOTH_PRINTED_14_LINE_CHAINS','checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'certificate_sha256':PIN,'geometries':[2,5],'lengths':[14,14],'omitted_last_line_rejected':omitted}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
