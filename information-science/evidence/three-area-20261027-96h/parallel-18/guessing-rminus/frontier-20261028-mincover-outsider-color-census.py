#!/usr/bin/env python3
"""Exact three-group color census for every four-cover single-outsider trade."""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations,product
from pathlib import Path
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
HELPER=('frontier-20261028-four-factor-cover-mip.py','e1308e6a85572dd52028ff4ef344ebff51b3fd112b94449ddbe4e5d8466c5fd1')
COVERS=('frontier-20261028-syndrome-cover-check-result.json','e1bf3ece1f9204a8f0f779bf98a236d689946df2bef5d2a50408b30bc9f3418d')
OUT=ROOT/'frontier-20261028-mincover-outsider-color-census-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return raw


def helper():
    pin(HELPER);spec=spec_from_file_location('mixed',ROOT/HELPER[0]);m=module_from_spec(spec);spec.loader.exec_module(m);return m


def colors():
    values=np.array([(0,)+x for x in product(range(3),repeat=9)],dtype=np.uint8);masks=np.zeros((3,len(values)),np.uint16)
    for v in range(10):
        for c in range(3):masks[c]|=(values[:,v]==c).astype(np.uint16)<<v
    return values,masks


def main():
    mod=helper();coverdoc=json.loads(pin(COVERS));covers=coverdoc['exact_checks']['minimum_covers']
    if len(covers)!=19:raise ValueError('COVERS')
    cs,cm=colors();records=[]
    for cover in covers:
        Ts,pos=mod.model_geometry(cover);seed=set(mod.xor_seed(Ts,pos));vmap=[];bad=[]
        for d in range(4096):
            mask=sum(1<<(v-1) for v in range(1,11) if any(d>>j&1 for j in pos[v]));vmap.append(mask)
            bad.append(any(not(mask&sum(1<<(u-1) for u in mod.N[v])) for v in range(1,11) if mask>>(v-1)&1))
        for sy in range(1,16):
            outsider=0
            for t,T in enumerate(Ts):
                if sy>>t&1:
                    v=T[0];slot=pos[v][[j for j,U in enumerate(Ts) if v in U].index(t)];outsider|=1<<slot
            removed={x for x in seed if bad[x^outsider]};W=sorted((seed-removed)|{outsider})
            mod.verify(W,pos)
            diffs={vmap[a^b] for a,b in combinations(W,2)};mins=[]
            for D in sorted(diffs,key=lambda x:(x.bit_count(),x)):
                if not any(M&D==M for M in mins):mins.append(D)
            valid=np.ones(len(cs),dtype=bool)
            for D in mins:
                valid &= np.all((cm&D)!=D,axis=0)
                if not np.any(valid):raise ValueError(('NO_COLOR',cover,sy))
            idx=int(np.flatnonzero(valid)[0]);records.append({'factors':cover,'syndrome':sy,'outside_word':outsider,
                 'removed_conflicts':len(removed),'support_size':len(W),'vertex_colors':cs[idx].tolist()})
    if len(records)!=285:raise ValueError('COUNT')
    out={'helper_sha256':HELPER[1],'cover_receipt_sha256':COVERS[1],'cover_count':len(covers),
         'syndromes_per_cover':15,'cases':records,'all_checked':True,
         'limits':'Exact finite 3-color witnesses for canonical single-outsider mixed supports; entropy/translation implications are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'cover_count':len(covers),'cases':len(records),'all_checked':True},indent=2))


if __name__=='__main__':main()
