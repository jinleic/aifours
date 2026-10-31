#!/usr/bin/env python3
"""Exact OR cover for sixth-vertex nested-fork face: O25>=0 OR O45>=0."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
old=ROOT/'frontier-20261029-ph7-nested-fork-simplex-check.py';ns={'__file__':str(old)}
exec(compile(old.read_text().split("assert len(sys.argv)==2")[0],str(old),'exec'),ns)
S,u,H,weights,vertices,D=ns['S'],ns['u'],ns['H'],ns['weights'],ns['vertices'],ns['D'];polys=ns['polys'];cover,digest=ns['cover'],ns['digest']
zero=[0]*4;D5=S.Poly(S.expand(H.subs(dict(zip(weights,zero)))),*u)
for i in (2,4):
 mid=[z/2 for z in vertices[i]];polys[f'O{i}5']=S.Poly(S.expand(4*H.subs(dict(zip(weights,mid)))-D[i].as_expr()-D5.as_expr()),*u)
names=['O25','O45'];strict=[False,False];paths=cover(names,strict);assert [len(p)for p in paths]==[2406,51]
records={n:{'degrees':list(polys[n].degree_list()),'terms':len(polys[n].terms()),'sha256':digest(polys[n])}for n in names}
out=ROOT/'frontier-20261029-ph7-nested-fork-zero-face-certificate-v1.json'
out.write_text(json.dumps({'domain':'six strictly positive finite rates','axis':'path depth modulo six',
 'records':records,'covers':[{'label':'face245_OR','names':names,'strict':strict,'paths':paths}]},indent=2)+'\n')
print('PASS: zero-vertex face OR cover, exact leaves 2406/51; saved',out)
