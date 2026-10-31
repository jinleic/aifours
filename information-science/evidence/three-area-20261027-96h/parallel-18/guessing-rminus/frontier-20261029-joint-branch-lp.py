#!/usr/bin/env python3
"""Add a joint (cross-branch) copy system to the current LP and re-optimize.

Usage: python3 script.py OUT.json JOINT PRELOAD.json PRELOAD_SHA [EXTRA.json]
JOINT=j12: variables a..j, b'0, d'1, e'1, g'2 built by the SEQUENTIAL copy lemma:
  b'0 copies b over a,d,e,f,g,h,i,j (independent of the originals given that set);
  (d'1,e'1) copies (d,e) over a,b,c,f,g,h,i, independent of originals and b'0 given it;
  g'2 copies g over a,b,c,d,e'1,f,h,i, independent of every earlier variable given it.
JOINT=j13: a..j, b'0, f'3, g'3, h'4 analogously with the publisher's third branch.
Every elemental Shannon inequality of the 14-variable set is added (these include
cross-branch rows omitted by the publisher). Sequential copy construction makes
each joint system valid. The rest of the model is the v3 symmetric publisher LP,
preloaded DFZ cuts and optional extra single copies. Cold IPM with crossover.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time

ROOT=Path(__file__).resolve().parent
def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3','frontier-20261029-dfz-cutting-plane-v3.py');v5=load('cp5','frontier-20261029-dfz-cutting-plane-v5.py');v6=load('cp6','frontier-20261029-copy-cutting-plane-v6.py')
L=list('abcdefghij')
SPECS={'j12':[(["b'0"],['b'],list('adefghij')),(["d'1","e'1"],['d','e'],list('abcfghi')),(["g'2"],['g'],['a','b','c','d',"e'1",'f','h','i'])],
       'j13':[(["b'0"],['b'],list('adefghij')),(["f'3","g'3"],['f','g'],list('abcdehij')),(["h'4"],['h'],['a','b','c','d','e','f',"f'3",'i','j'])]}

def add_joint(M,tag):
    steps=SPECS[tag];names=L+[x for st in steps for x in st[0]];pos={x:i for i,x in enumerate(names)}
    def keyf(m):
        if m==0:return None
        return ('o',m) if m<1024 else (tag,m)
    def mk(s):return sum(1<<pos[x] for x in s)
    cp.add_shannon(M,names,keyf);existing=list(L)
    for new,old,over in steps:
        Y=mk(over)
        for q in range(1,1<<len(new)):
            nm=sum(1<<pos[new[k]] for k in range(len(new)) if q>>k&1);om=sum(1<<pos[old[k]] for k in range(len(new)) if q>>k&1)
            U=Y
            while True:
                M.add([(keyf(U|nm),1),(keyf(U|om),-1)],0,0,('jcopy',tag,tuple(new),q,U))
                if not U:break
                U=(U-1)&Y
        E=mk(existing);Nn=mk(new)
        M.add([(keyf(E|Nn),1),(keyf(Y),1),(keyf(E),-1),(keyf(Y|Nn),-1)],0,0,('jindependence',tag,tuple(new)))
        existing+=new

def main():
    out=ROOT/sys.argv[1];tags=sys.argv[2].split(',');raw=(ROOT/sys.argv[3]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[4]:raise ValueError('PRELOAD_HASH')
    extra=json.loads((ROOT/sys.argv[5]).read_text())['branches'] if len(sys.argv)>5 else []
    t0=time.monotonic();keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym')
    for k,(S,T) in enumerate(extra):v6.add_single_copy(M,k,S[0],T)
    seen=set();cuts=[]
    for c in json.loads(raw)['cuts']:
        tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z']);cuts.append(dict(c,tag=tag))
    for tag in tags:add_joint(M,tag)
    print('columns',len(M.col),'rows',len(M.rows),flush=True)
    h,status,obj,x,dt=cp.solve(M)
    res={'branches':'gurpinar-sym','joint':tags,'extra_single_copies':extra,'cuts':cuts,'status':status,'objective':obj,'rows':len(M.rows),'columns':len(M.col),'solve_s':dt,
         'final_original_profile_float':[float(v) for v in v5.profile(M,x,'o')[1:]],'limits':'Floating proposal; exact certificate required.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')
    print(status,obj,round(time.monotonic()-t0,1))

if __name__=='__main__':main()
