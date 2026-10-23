"""Approved exploratory H3 experiment (HALL3_PATTERN_NECESSITY.r1.md).
No CNF/proof is retained: even the base alone exceeds the100MB retention gate.
Checks fixed support patterns, runs H3-only negative control, then runs the
parent's AG(2,8) positive configuration against F+H3 with EXACTLY5 P4-ALO and7
Q1-SB2 units removed. Checks the returned SAT model against every clause.
Only after those controls pass: ONE proof-free CaDiCaL -t600 on the unchanged
K5 hard leaf's21units, appended to F+H3. No retry/full pass/certificate cutover.
"""
from __future__ import annotations

import hashlib
import io
import itertools
import json
import os
import re
import shutil
import signal
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT/'evidence/gram_dev_v1/GA5L_K5_sb2.cnf'
MAP = ROOT/'evidence/gram_dev_v1/GA5L_K5_sb2.map.json'
BIND = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-encoder-binding-v1/K5.bind.json')
LEDGER = ROOT/'evidence/k5_split_v1/ledger/LEDGER.v008.json'
OUT = ROOT/'evidence/h3_pilot_v1'
BASE_SHA = '6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b'
MAP_SHA = '7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197'
RSS_CAP = 6*2**30
FLOOR = 12_000_000_000
R3 = list(itertools.combinations(range(8),3))
NOT_C2 = [tuple(k for k in range(8) if k not in C) for C in itertools.combinations(range(8),2)]


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def emit_json(path, obj):
    with path.open('x') as f:
        json.dump(obj,f,indent=1)


def raw_matrix_clauses(M):
    for transpose in (False,True):
        for R in R3:
            for Cc in NOT_C2:
                yield [M[c][r] if transpose else M[r][c] for r in R for c in Cc]


def simplify(cl):
    if any(l is True for l in cl):
        return None
    out = [l for l in cl if l is not False]
    if not out:
        raise RuntimeError('H3 emitted an empty clause')
    return out


def cnf_line(cl):
    return (' '.join(map(str,cl))+' 0\n').encode()


def rss_bytes(pids):
    q=subprocess.run(['ps','-o','rss=','-p',','.join(map(str,pids))],capture_output=True,text=True)
    return sum(int(x) for x in q.stdout.split())*1024


def run(tag,nv,nc,parts,limit,extra=None):
    free=shutil.disk_usage(ROOT).free
    h=hashlib.sha256(); total=0
    for b in parts:
        h.update(b); total+=len(b)
    solver=Path(shutil.which('cadical')).resolve()
    fifo=OUT/(tag+'.cnf.fifo')
    meta={'start':stamp(),'nv':nv,'clauses':nc,'cnf_sha256':h.hexdigest(),'cnf_bytes':total,
          'solver_binary':str(solver),'solver_sha256':sha(solver.read_bytes()),
          'solver_version':subprocess.run([str(solver),'--version'],capture_output=True,text=True).stdout.strip(),
          'argv':[str(solver),'-q','-t',str(limit),str(fifo)],'native_limit':limit,
          'rss_cap':RSS_CAP,'free_before_launch':free,'proof':'none; EXPLORATORY',
          'cnf_storage':'streamed only; no duplicate CNF file','extra':extra}
    if free<FLOOR:
        meta['deferred']='shared free floor'; emit_json(OUT/(tag+'.deferred.json'),meta)
        raise RuntimeError('free floor before '+tag)
    emit_json(OUT/(tag+'.input.json'),meta)
    os.mkfifo(fifo)
    feed_errors=[]; feed_h=hashlib.sha256(); feed_count=[0]
    t0=time.monotonic()
    with (OUT/(tag+'.solver.log')).open('x') as log:
        p=subprocess.Popen(meta['argv'],stdout=log,stderr=subprocess.STDOUT)
        def feed():
            try:
                with fifo.open('wb') as f:
                    for b in parts:
                        n=f.write(b)
                        if n!=len(b):
                            raise RuntimeError('short FIFO write')
                        feed_h.update(b); feed_count[0]+=n
            except Exception as e:
                feed_errors.append(repr(e))
        th=threading.Thread(target=feed); th.start()
        peak=0; guard=None
        while p.poll() is None:
            used=rss_bytes([os.getpid(),p.pid]); peak=max(peak,used)
            free=shutil.disk_usage(ROOT).free
            if used>RSS_CAP or free<FLOOR:
                guard={'rss':used,'free':free,'time':stamp()}; p.send_signal(signal.SIGTERM)
                try:
                    p.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    pass
                break
            time.sleep(2)
        rc=p.poll()
        th.join(timeout=30)
    text=(OUT/(tag+'.solver.log')).read_text(errors='replace')
    status='UNSAT' if re.search(r'^s UNSATISFIABLE\s*$',text,re.M) else (
           'SAT' if re.search(r'^s SATISFIABLE\s*$',text,re.M) else 'UNKNOWN')
    complete=(not th.is_alive() and not feed_errors and feed_count[0]==total and feed_h.hexdigest()==h.hexdigest())
    if guard or not complete or rc not in (10,20):
        status='UNKNOWN'
    result={'tag':tag,'status':status,'returncode':rc,'seconds':time.monotonic()-t0,
            'rss_peak_bytes':peak,'guard':guard,'feed_errors':feed_errors,'feed_complete_hash_matched':complete,
            'cnf_sha256':h.hexdigest(),'cnf_bytes':total,'end':stamp(),
            'claim':'EXPLORATORY timing signal only; no proof retained or checked'}
    emit_json(OUT/(tag+'.result.json'),result)
    print(json.dumps(result),flush=True)
    return result,text


def main():
    OUT.mkdir(exist_ok=False)
    raw=BASE.read_bytes()
    if sha(raw)!=BASE_SHA:
        raise RuntimeError('base pin mismatch')
    header,body=raw.split(b'\n',1); del raw
    _,_,nv,nc=header.split(); nv=int(nv); nc=int(nc)
    mr=MAP.read_bytes()
    if sha(mr)!=MAP_SHA:
        raise RuntimeError('map pin mismatch')
    mapping=json.loads(mr)['vars']; gm={}
    for key,v in mapping.items():
        nm=json.loads(key)
        if nm[0]=='g':
            gm[(nm[1],tuple(nm[2]),tuple(nm[3]))]=v
    if len(gm)!=7840 or len(set(gm.values()))!=7840:
        raise RuntimeError('g map not injective/complete')
    def G(s,p,q):
        if p==q:
            return True
        if p[0]==q[0] or p[1]==q[1]:
            return False
        p,q=sorted((p,q))
        return gm[(s,p,q)]
    lines=[[(r,j) for j in range(8)] for r in range(1,8)] + [
           [(i,c) for i in range(8)] for c in range(8)]
    h3=bytearray(); raw_count=emitted=taut=0
    for s in range(1,6):
        for line in lines:
            M=[[G(s,(0,k),p) for p in line] for k in range(8)]
            for cl in raw_matrix_clauses(M):
                raw_count+=1; folded=simplify(cl)
                if folded is None:
                    taut+=1; continue
                emitted+=1; h3.extend(cnf_line(folded))
    if raw_count!=235200:
        raise RuntimeError('raw H3 count differs from frozen protocol')
    h3=bytes(h3)
    recipe={'start':stamp(),'script_sha256':sha(Path(__file__).read_bytes()),'base_sha256':BASE_SHA,
            'map_sha256':sha(mr),'raw_h3_candidates':raw_count,'emitted_h3_clauses':emitted,
            'dropped_tautologies':taut,'h3_body_sha256':sha(h3),'h3_body_bytes':len(h3),
            'new_variables':0,'new_auxiliaries':0,'streaming_reason':'base alone137664569B exceeds100MB retention gate'}
    emit_json(OUT/'RECIPE.json',recipe)
    # Fixed-pattern controls, including a pattern passing pairwise G3 but failing H3.
    bad=[[False]*8 for _ in range(8)]
    for r in range(3):
        for c in range(2): bad[r][c]=True
    for r in range(3,5):
        for c in range(2,5): bad[r][c]=True
    for i in range(5,8): bad[i][i]=True
    def g3(M):
        return (all(any(row) for row in M) and all(any(M[r][c] for r in range(8)) for c in range(8)) and
                all(sum(M[r][c] and M[t][c] for c in range(8))!=1
                    for r,t in itertools.combinations(range(8),2)) and
                all(sum(M[r][c] and M[r][d] for r in range(8))!=1
                    for c,d in itertools.combinations(range(8),2)))
    def violations(M):
        return sum(not any(cl) for cl in raw_matrix_clauses(M))
    mats={'identity':[[r==c for c in range(8)] for r in range(8)],
          'permutation_shift3':[[(r+3)%8==c for c in range(8)] for r in range(8)],
          'Fourier8_support':[[True]*8 for _ in range(8)],
          'four_Hadamard2_blocks':[[r//2==c//2 for c in range(8)] for r in range(8)]}
    fixed={'bad_pairwise_g3_passes':g3(bad),'bad_H3_violations':violations(bad),
           'positive_H3_violations':{k:violations(M) for k,M in mats.items()}}
    if not fixed['bad_pairwise_g3_passes'] or not fixed['bad_H3_violations'] or any(fixed['positive_H3_violations'].values()):
        raise RuntimeError('fixed-pattern control failure')
    emit_json(OUT/'PATTERN_CONTROLS.json',fixed)
    M=[[r*8+c+1 for c in range(8)] for r in range(8)]
    local=[cnf_line(cl) for cl in raw_matrix_clauses(M)]
    units=[cnf_line([M[r][c] if bad[r][c] else -M[r][c]]) for r in range(8) for c in range(8)]
    negparts=(b'p cnf 64 3200\n',b''.join(local),b''.join(units))
    neg,_=run('H3_ONLY_BAD_PATTERN',64,3200,negparts,30)
    if neg['status']!='UNSAT':
        raise RuntimeError('H3-only negative control not rejected')
    # Parent binding's exact classical configuration, strong relaxation only.
    br=BIND.read_bytes(); binding=json.loads(br)
    squares={int(s):rows for s,rows in binding['c12_classical_set']['squares'].items()}
    if set(squares)!=set(range(1,6)):
        raise RuntimeError('unexpected classical square labels')
    for rows in squares.values():
        if any(len(set(rows[i]))!=8 or len({rows[r][i] for r in range(8)})!=8 for i in range(8)):
            raise RuntimeError('classical positive not Latin')
    if any(len({(squares[s][r][c],squares[t][r][c]) for r in range(8) for c in range(8)})!=64
           for s,t in itertools.combinations(squares,2)):
        raise RuntimeError('classical squares not pairwise orthogonal')
    alo=set(binding['classification']['p4']['alo_clause_indices'])
    sb2={idx:(sign,nm) for idx,sign,nm in binding['classification']['sb2_unit_index'] if nm[1]==1}
    if len(alo)!=5 or len(sb2)!=7:
        raise RuntimeError('relaxation must remove exactly5 ALO plus7 Q1 SB2 units')
    drop=alo|set(sb2); kept=bytearray(); actual_count=0
    for i,line in enumerate(io.BytesIO(body)):
        actual_count+=1
        if i in alo:
            if len(line.split())!=57:
                raise RuntimeError('P4 ALO line not56 flags')
        elif i in sb2:
            sign,nm=sb2[i]; p,q=tuple(nm[2]),tuple(nm[3]); v=G(nm[1],p,q)
            if line!=cnf_line([v if sign else -v]):
                raise RuntimeError('bound SB2 index/literal mismatch')
        else:
            kept.extend(line)
    if actual_count!=nc:
        raise RuntimeError('base clause count mismatch')
    gunits=[]
    for (s,p,q),v in sorted(gm.items(),key=lambda kv:kv[1]):
        x=squares[s][p[0]][p[1]]==squares[s][q[0]][q[1]]
        gunits.append(v if x else -v)
    ctrl_tail=b''.join(cnf_line([u]) for u in gunits)
    ctrl_nc=nc-12+emitted+len(gunits)
    ctrl_head=('p cnf %d %d\n'%(nv,ctrl_nc)).encode()
    ctrlparts=(ctrl_head,bytes(kept),h3,ctrl_tail); del kept
    pos,model=run('AG8_POSITIVE',nv,ctrl_nc,ctrlparts,120,extra={
        'binding_source_sha256':sha(br),'dropped_P4_ALO_indices':sorted(alo),
        'dropped_Q1_SB2_indices':sorted(sb2),'fixed_g_variables':len(gunits),
        'classical_squares':squares})
    if pos['status']!='SAT':
        raise RuntimeError('H3-strengthened classical positive did not return SAT')
    vals=bytearray(nv+1)
    for line in model.splitlines():
        if line.startswith('v '):
            for st in line.split()[1:]:
                l=int(st)
                if l:
                    if not 1<=abs(l)<=nv: raise RuntimeError('model variable out of range')
                    v=1 if l>0 else 2
                    if vals[abs(l)] not in (0,v): raise RuntimeError('contradictory model')
                    vals[abs(l)]=v
    checked=0
    for part in ctrlparts[1:]:
        for line in io.BytesIO(part):
            cl=[int(x) for x in line.split()[:-1]]
            if not any(vals[abs(l)]==(1 if l>0 else 2) for l in cl):
                raise RuntimeError('positive SAT model violates clause%d'%checked)
            checked+=1
    if checked!=ctrl_nc:
        raise RuntimeError('model-check clause count mismatch')
    emit_json(OUT/'CONTROL_SUMMARY.json',{'pattern':fixed,'negative_status':neg['status'],
        'positive_status':pos['status'],'positive_model_clauses_checked':checked,'all_pass':True,
        'new_H3_clauses':emitted,'new_H3_bytes':len(h3),'time':stamp()})
    del ctrlparts,ctrl_tail,vals,model
    # Exactly one approved hard-leaf exploratory solve.
    lb=LEDGER.read_bytes(); ledger=json.loads(lb)
    leaf=next(x for x in ledger['leaves'] if x['id']=='c016.L2.040.L3.104')
    lits=leaf['lits']; tail=b''.join(cnf_line([l]) for l in lits)
    if len(lits)!=21:
        raise RuntimeError('wrong path-unit count')
    old=hashlib.sha256(('p cnf %d %d\n'%(nv,nc+21)).encode()); old.update(body); old.update(tail)
    if old.hexdigest()!='6d84469eed207e6f0944c52ccbfbaa0596078966dfba432743ab78541ce6aebd':
        raise RuntimeError('old leaf identity changed')
    pilot_nc=nc+emitted+21
    parts=(('p cnf %d %d\n'%(nv,pilot_nc)).encode(),body,h3,tail)
    run('K5_HARD_LEAF_PILOT',nv,pilot_nc,parts,600,extra={
        'leaf':leaf['id'],'lits':lits,'ledger_sha256':sha(lb),'old_leaf_cnf_sha256':old.hexdigest(),
        'new_H3_clauses':emitted,'recipe_sha256':sha((OUT/'RECIPE.json').read_bytes())})


if __name__=='__main__':
    main()
