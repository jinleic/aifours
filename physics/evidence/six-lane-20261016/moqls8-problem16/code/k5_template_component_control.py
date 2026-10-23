"""Finite exhaustive control for K5_COLUMN0_TEMPLATE_COVER.r1.md (parent23:0x).
Enumerate all CONNECTED bicoloured graph isomorphism classes with part sizes
1..8, degrees1..3, using hash-pinned nauty genbg; independently parse graph6,
filter the necessary pair-overlap rules and H3 (union of any3 rows/columns
has size>=3), and list every passing component outside the five block types.
A degree1 vertex under the pair-overlap rules must be an isolated K11; thus
nontrivial connected candidates may be generated with min-degree2. This is a
separate necessary pruning fact, not the claimed classification. r<c covers
c<r by explicit transpose symmetry. No other classification pruning is used.

Every nonempty-row/column support matrix up to8x8 decomposes uniquely into
such components; the rules are invariant under independent row/column labels.
For H3 across different components: 1+1+1 rows give3 neighbours; 2+1 rows give
at least2+1 (two rows with a single neighbour union would violate pair overlap).
Thus filtering components and composing their EXACT labelled orbit counts is
an exhaustive symmetry-compressed enumeration of the full matrices, not a
random sample. Zero rows/columns fail the original G3 nonempty condition.
Unexpected components are recorded, never discarded; any one blocks13runs.
No graph/CNF/proof stream is retained. One genbg+one filter, <=1GiB for control.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import resource
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'evidence/k5_template_component_control_v2'
FLOOR=12_000_000_000
WANTED={'I1','K22','K33-e','K33','K44-matching'}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def dump(path,obj):
    with path.open('x') as f: json.dump(obj,f,indent=1)


def parser(r,c):
    n=r+c; L=n*(n-1)//2; pad=(-L)%6
    positions=[[(L-1-((r+j)*(r+j-1)//2+i)) for j in range(c)] for i in range(r)]
    allowed=sum(1<<p for row in positions for p in row)
    def parse(line):
        s=line.rstrip(b'\r\n')
        if len(s)!=1+(L+5)//6 or s[0]!=n+63 or any(not 63<=x<=126 for x in s[1:]):
            raise RuntimeError('graph6 format/header mismatch')
        x=0
        for b in s[1:]: x=(x<<6)|(b-63)
        if pad and x&((1<<pad)-1): raise RuntimeError('nonzero graph6 padding')
        x>>=pad
        if x&~allowed: raise RuntimeError('edge inside a colour part')
        rows=[sum((1<<j) for j,p in enumerate(row) if (x>>p)&1) for row in positions]
        cols=[sum(1<<i for i,mask in enumerate(rows) if (mask>>j)&1) for j in range(c)]
        return rows,cols
    return parse


def pairs_ok(masks):
    return all((a&b).bit_count()!=1 for a,b in itertools.combinations(masks,2))


def rank3_ok(masks):
    return all((a|b|c).bit_count()>=3 for a,b,c in itertools.combinations(masks,3))


def connected(rows,cols):
    rs={0}; cs=set(); change=True
    while change:
        old=(len(rs),len(cs))
        cs|={j for i in rs for j in range(len(cols)) if (rows[i]>>j)&1}
        rs|={i for j in cs for i in range(len(rows)) if (cols[j]>>i)&1}
        change=old!=(len(rs),len(cs))
    return len(rs)==len(rows) and len(cs)==len(cols)


def kind(r,c,rows,cols):
    E=sum(x.bit_count() for x in rows)
    if r==c==1 and E==1: return 'I1'
    if r==c==2 and E==4: return 'K22'
    if r==c==3 and E==8: return 'K33-e'
    if r==c==3 and E==9: return 'K33'
    if r==c==4 and all(x.bit_count()==3 for x in rows+cols): return 'K44-matching'
    return None


def labelled_orbit(rows,c):
    images=set(); r=len(rows)
    for rp in itertools.permutations(range(r)):
        for cp in itertools.permutations(range(c)):
            code=0
            for i,oldi in enumerate(rp):
                for j,oldj in enumerate(cp):
                    if (rows[oldi]>>oldj)&1: code|=1<<(i*c+j)
            images.add(code)
    return images


def deadline(signum,frame):
    raise TimeoutError('per-size900s control cap')


def main():
    OUT.mkdir(exist_ok=False)
    exe=Path(shutil.which('genbg')).resolve()
    meta={'start':stamp(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'genbg_binary':str(exe),'genbg_sha256':hashlib.sha256(exe.read_bytes()).hexdigest(),
          'genbg_version_from_install_path':exe.parent.parent.name,
          'method':'all connected colour-preserving graph isomorphism classes; transpose symmetry; exact labelled orbits',
          'nonempty_rows_and_columns':'required by G3; zero vertices not relevant transition patterns',
          'max_part_size':8,'max_degree':3,'per_size_wall_limit':900,'total_wall_cap':10400,'floor':FLOOR,
          'proof_note_sha256':hashlib.sha256((ROOT/'review/K5_COLUMN0_TEMPLATE_COVER.r1.md').read_bytes()).hexdigest()}
    dump(OUT/'META.json',meta)
    parts=[]; accepted=[]; labels={k:set() for k in range(1,9)}; seen=set(); t0=time.monotonic()
    journal=(OUT/'SIZES.jsonl').open('x')
    signal.signal(signal.SIGALRM,deadline)
    for r in range(1,9):
        for c in range(r,9):
            item={'rows':r,'columns':c,'generated_classes':0,'pair_overlap_pass':0,'rank3_reject':0,
                  'accepted_classes':0,'accepted':[],'transpose_also_covers':[c,r] if c!=r else None}
            if (r==1 and c!=1) or max(2*r,2*c)>min(3*r,3*c,r*c) and (r,c)!=(1,1):
                item['empty_reason']='degree1-isolated fact or minimum2/maximum3 edge-count bounds'
                parts.append(item); journal.write(json.dumps(item)+'\n'); journal.flush(); continue
            if shutil.disk_usage(ROOT).free<FLOOR:
                dump(OUT/'DEFERRED.json',{'before_size':[r,c],'free':shutil.disk_usage(ROOT).free,'time':stamp()})
                raise RuntimeError('free floor before genbg launch; enumeration incomplete')
            remaining=int(10400-(time.monotonic()-t0))
            if remaining<=0:
                dump(OUT/'DEFERRED_WALL_CAP.json',{'before_size':[r,c],'time':stamp()})
                raise RuntimeError('finite control total wall cap; incomplete')
            cmd=[str(exe),'-c','-g','-d1' if(r,c)==(1,1) else '-d2','-D3',str(r),str(c)]
            item['argv']=cmd; parse=parser(r,c); stream_h=hashlib.sha256(); start=time.monotonic()
            with (OUT/('genbg_%d_%d.stderr.txt'%(r,c))).open('x') as err:
                p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=err)
                signal.alarm(min(900,remaining))
                normal_end=False
                try:
                    for line in p.stdout:
                        if line.startswith(b'>>graph6<<'): line=line[len(b'>>graph6<<'):]
                        if not line.strip(): continue
                        stream_h.update(line); item['generated_classes']+=1
                        rows,cols=parse(line)
                        low=1 if(r,c)==(1,1) else 2
                        if any(not low<=x.bit_count()<=3 for x in rows+cols):
                            raise RuntimeError('generated degree out of range')
                        if not pairs_ok(rows) or not pairs_ok(cols): continue
                        item['pair_overlap_pass']+=1
                        if not rank3_ok(rows) or not rank3_ok(cols):
                            item['rank3_reject']+=1; continue
                        if not connected(rows,cols): raise RuntimeError('genbg connected flag not honoured')
                        ty=kind(r,c,rows,cols)
                        rec={'size':[r,c],'graph6':line.decode().strip(),'row_masks':rows,'column_masks':cols,'type':ty}
                        if ty is None:
                            dump(OUT/'OUTSIDE_COMPONENT.json',rec)
                            raise RuntimeError('component outside claimed list; listed; no template run allowed')
                        orb=labelled_orbit(rows,c)
                        if labels[r]&orb: raise RuntimeError('duplicate accepted colour-isomorphism class')
                        labels[r]|=orb; rec['labelled_orbit_size']=len(orb)
                        accepted.append(rec); seen.add(ty); item['accepted_classes']+=1; item['accepted'].append(rec)
                    normal_end=True
                finally:
                    signal.alarm(0)
                    if not normal_end and p.poll() is None:
                        p.terminate()
                    try:
                        p.wait(timeout=30)
                    except subprocess.TimeoutExpired:
                        if p.poll() is None:
                            p.terminate()
                        try: p.wait(timeout=30)
                        except subprocess.TimeoutExpired: pass
                item['exit']=p.poll()
            if item['exit']!=0: raise RuntimeError('genbg failed/interrupted; enumeration incomplete')
            item['stream_sha256']=stream_h.hexdigest(); item['seconds']=time.monotonic()-start
            parts.append(item); journal.write(json.dumps(item)+'\n'); journal.flush()
            print(json.dumps({k:item[k] for k in ('rows','columns','generated_classes','pair_overlap_pass',
                                                  'rank3_reject','accepted_classes','seconds')}),flush=True)
            rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if sys.platform!='darwin': rss*=1024
            child_rss=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
            if sys.platform!='darwin': child_rss*=1024
            item['max_self_plus_child_rss_upper_bound']=rss+child_rss
            if rss+child_rss>2**30: raise RuntimeError('control self+child RSS cap1GiB')
            if rss>2**30: raise RuntimeError('control own RSS cap1GiB')
    journal.close()
    if seen!=WANTED: raise RuntimeError('not all five positive component types observed')
    a={k:len(v) for k,v in labels.items()}
    # Unique component containing row0, with independent row/column labels.
    full=[1]
    for n in range(1,9):
        full.append(sum(math.comb(n-1,k-1)*math.comb(n,k)*a[k]*full[n-k] for k in range(1,n+1)))
    result={'complete':True,'time':stamp(),'seconds':time.monotonic()-t0,'parts':parts,'accepted_components':accepted,
            'outside_components':[],'connected_labelled_square_components_by_size':a,
            'all_labelled_square_matrices_by_size_0to8':full,
            'recurrence':'M_n=sum_k binom(n-1,k-1)*binom(n,k)*a_k*M_(n-k), M_0=1',
            'generated_isomorphism_classes_total':sum(x['generated_classes'] for x in parts),
            'rank3_rejected_components_total':sum(x['rank3_reject'] for x in parts),
            'zero_vertices':'excluded by nonempty G3; no supported unitary has a zero row/column',
            'all_pass':True,'claim':'finite symmetry-compressed support enumeration only; not a K5 exclusion'}
    dump(OUT/'RESULT.json',result)
    print(json.dumps({k:result[k] for k in ('complete','seconds','generated_isomorphism_classes_total',
                    'connected_labelled_square_components_by_size','all_labelled_square_matrices_by_size_0to8',
                    'rank3_rejected_components_total','all_pass')}),flush=True)


if __name__=='__main__':
    main()
