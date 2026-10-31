#!/usr/bin/env python3
"""Exact selector covers for the zero-vertex faces of the nested-fork down-closure.

Adds the all-zero weight vertex 5 to the pinned five-vertex simplex. Certifies
O52>=0 and, for the three connector faces whose two off-diagonals can both be
negative, O5c>=0 OR Oc2>=0 OR 2*O52*Dc-O5c*Oc2>=0.
"""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
old=ROOT/'frontier-20261029-ph7-nested-fork-simplex-check.py';ns={'__file__':str(old)}
exec(compile(old.read_text().split("assert len(sys.argv)==2")[0],str(old),'exec'),ns)
S,u,H,weights,vertices,D,O=ns['S'],ns['u'],ns['H'],ns['weights'],ns['vertices'],ns['D'],ns['O'];polys=ns['polys'];cover,digest=ns['cover'],ns['digest']
D5=S.Poly(S.expand(H.subs(dict(zip(weights,[0,0,0,0])))),*u);O5={}
for i in range(5):
 mid=[z/2 for z in vertices[i]];O5[i]=S.Poly(S.expand(4*H.subs(dict(zip(weights,mid)))-D[i].as_expr()-D5.as_expr()),*u);polys[f'O{i}5']=O5[i]
specs=[('O25',['O25'],[False])]
for c in (0,1,3):
 pair=tuple(sorted((c,2)));name=f'Z{c}';polys[name]=2*O5[2]*D[c]-O5[c]*O[pair]
 specs.append((f'face5{c}2',[f'O{c}5','O'+''.join(map(str,pair)),name],[False,False,False]))
used=sorted({n for _,names,_ in specs for n in names});covers=[]
for label,names,strict in specs:
 paths=cover(names,strict);covers.append({'label':label,'names':names,'strict':strict,'paths':paths});print(label,'leaves',[len(p)for p in paths],flush=True)
records={n:{'degrees':list(polys[n].degree_list()),'terms':len(polys[n].terms()),'sha256':digest(polys[n])}for n in used}
out=ROOT/'frontier-20261029-ph7-nested-fork-down-closure-certificate-v1.json'
out.write_text(json.dumps({'domain':'six strictly positive finite rates','axis':'path depth modulo six','records':records,'covers':covers},indent=2)+'\n')
print('PASS: down-closure zero-vertex selector covers; saved',out)
