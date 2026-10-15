import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[name]='1'
import collections,json,math,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from witness_search import CASES,access

ROOT=Path(__file__).resolve().parent
TARGETS=[(1,5),(2,6),(3,5),(4,6),(5,6),(5,7)]


def distribution(case,m,colors,full=True):
    _,qs,fs,_=access(CASES[case-1]);parsed=[]
    for name in ('white','black'):
        c=[(tuple(p['orbit']),Fraction(p['probability'])) for p in colors[name]]
        assert c and all(len(a)==m and tuple(sorted(a))==a and all(0<=x<32 for x in a) and p>0 for a,p in c)
        assert sum(p for _,p in c)==1;parsed.append(c)
    for q in qs:
        assert min(sum(bool(x&q) for x in a) for a,_ in parsed[1])>=max(sum(bool(x&q) for x in a) for a,_ in parsed[0])+1
    violations=[]
    for f in fs:
        dist=[];expected=[]
        for color in parsed:
            d=collections.Counter();e=collections.Counter()
            for a,p in color:
                d[tuple(sorted(x&f for x in a))]+=p
                for x in a:e[x&f]+=p
            dist.append(d);expected.append(e)
        assert expected[0]==expected[1]
        if full:assert dist[0]==dist[1]
        elif dist[0]!=dist[1]:violations.append(f)
    return {'all_forbidden':len(fs),'all_qualified':len(qs),'support_sizes':list(map(len,parsed)),'full_security_violations':violations}


def arc(arrays,weights,fs,iw,ib):
    trace=[]
    while len(iw) and len(ib):
        keep=[np.ones(len(iw),dtype=bool),np.ones(len(ib),dtype=bool)];counts=[]
        for f in fs:
            buckets=[collections.defaultdict(list),collections.defaultdict(list)]
            for c,ids in enumerate((iw,ib)):
                for local,global_id in enumerate(ids):buckets[c][tuple(sorted(int(x)&f for x in arrays[c][global_id]))].append(local)
            match=[np.zeros(len(iw),dtype=bool),np.zeros(len(ib),dtype=bool)]
            for key,wl in buckets[0].items():
                bl=buckets[1].get(key,[])
                if not bl:continue
                for start in range(0,len(wl),64):
                    ws=np.array(wl[start:start+64]);bs=np.array(bl)
                    relation=np.all(weights[1][ib[bs]][None,:,:]>weights[0][iw[ws]][:,None,:],axis=2)
                    match[0][ws]|=relation.any(axis=1);match[1][bs]|=relation.any(axis=0)
            keep[0]&=match[0];keep[1]&=match[1]
            counts.append([int(a.sum()) for a in match])
        nw,nb=iw[keep[0]],ib[keep[1]]
        trace.append({'before':[len(iw),len(ib)],'matched_per_forbidden':counts,'after':[len(nw),len(nb)]})
        if len(nw)==len(iw) and len(nb)==len(ib):return nw,nb,trace
        iw,ib=nw,nb
    return iw,ib,trace


def check_full(case,m):
    _,qs,_,fs=access(CASES[case-1])
    arrays=[np.fromfile(ROOT/f'case{case}_m{m}_{c}.bin',dtype=np.uint8).reshape((-1,m)) for c in ('white','black')]
    weights=[np.stack([(a&q!=0).sum(axis=1) for q in qs],axis=1) for a in arrays]
    enum=json.loads((ROOT/f'case{case}_m{m}_enumeration.json').read_text())
    assert enum['black_enumerated']==math.comb(m+31,m)
    assert enum['white_with_zero']==math.comb(m+30,m-1)
    assert enum['black_surviving']==len(arrays[1]) and enum['white_projection_filtered']==len(arrays[0])
    assert all(np.all(a[:,:-1]<=a[:,1:]) for a in arrays)
    assert np.all(arrays[0][:,0]==0)
    for q in qs:
        for f in fs:
            assert np.all(np.any((arrays[1]&q!=0)&(arrays[1]&(q&f)==0),axis=1))
    savedarc=json.loads((ROOT/f'case{case}_m{m}_arc.json').read_text())
    iw,ib,trace=arc(arrays,weights,fs,np.arange(len(arrays[0])),np.arange(len(arrays[1])))
    assert trace==savedarc['arc_trace'] and [len(iw),len(ib)]==savedarc['surviving']
    doc=json.loads((ROOT/f'case{case}_m{m}_decision.json').read_text());seen={};terms=0
    def walk(nid,iw,ib):
        nonlocal terms
        if nid in seen:
            assert tuple(map(tuple,(iw,ib)))==seen[nid];return
        seen[nid]=tuple(map(tuple,(iw,ib)));node=doc['nodes'][nid]
        assert node['before']==[len(iw),len(ib)]
        iw,ib,tr=arc(arrays,weights,fs,iw,ib)
        assert tr==node['arc_trace'] and node['after']==[len(iw),len(ib)]
        if node['kind']=='empty':assert not len(iw) or not len(ib);return
        if node['kind']=='separating_functional':
            cert=node['certificate'];table={}
            for term in cert['terms']:
                f=term['forbidden'];p=tuple(term['projection']);v=term['coefficient']
                assert f in fs and len(p)==m and tuple(sorted(p))==p and all(x&f==x for x in p) and isinstance(v,int)
                key=(f,p);assert key not in table;table[key]=v
            scores=[]
            for c,ids in enumerate((iw,ib)):
                scores.append([cert['constant']+sum(table.get((f,tuple(sorted(int(x)&f for x in arrays[c][ix]))),0) for f in fs) for ix in ids])
            assert min(scores[0])==cert['white_min']>=1 and max(scores[1])==cert['black_max']<=0
            terms+=len(table);return
        assert node['kind']=='threshold_split';k=qs.index(node['qualified']);children={c['threshold']:c['node'] for c in node['children']}
        for t in range(1,m+1):
            w=iw[weights[0][iw,k]<t];b=ib[weights[1][ib,k]>=t]
            assert node['threshold_cases'][t-1]=={'threshold':t,'candidate_counts':[len(w),len(b)]}
            if len(w) and len(b):assert t in children;walk(children[t],w,b)
        assert set(children)<=set(range(1,m+1))
    walk(doc['root'],iw,ib)
    assert doc['verdict']=='NO' and len(seen)==len(doc['nodes'])
    return {'case':case,'m':m,'verdict':'NO','checked_nodes':len(seen),'checked_separator_terms':terms,'no_lp_solver_used':True}


def check_relaxed(case,m):
    doc=json.loads((ROOT/f'case{case}_m{m}_relaxed_exact.json').read_text())
    if doc['verdict']=='YES':
        witnesses=[n['witness'] for n in doc['nodes'] if n['kind']=='witness'];assert witnesses
        verified=distribution(case,m,witnesses[0],False)
        return {'case':case,'m':m,'verdict':'YES','witness':verified,'no_lp_solver_used':True}
    _,qs,_,fs=access(CASES[case-1])
    arrays=[np.fromfile(ROOT/f'case0_m{m}_{c}.bin',dtype=np.uint8).reshape((-1,m)) for c in ('white','black')]
    assert [len(a) for a in arrays]==[math.comb(m+30,m-1),math.comb(m+31,m)]
    weights=[]
    for a in arrays:
        w=np.empty((len(a),len(qs)),dtype=np.int8)
        for k,q in enumerate(qs):w[:,k]=(a&q!=0).sum(axis=1)
        weights.append(w)
    seen=set()
    def walk(nid,iw,ib):
        node=doc['nodes'][nid]
        # Threshold conditions determine a unique pair of candidate universes.
        assert node['candidates']==[len(iw),len(ib)]
        if nid in seen:return
        seen.add(nid)
        if node['kind']=='empty':assert not len(iw) or not len(ib);return
        if node['kind']=='separator':
            c=node['certificate'];g=[]
            for term in c['expected_projection_terms']:assert term['forbidden'] in fs and term['projected_column']&term['forbidden']==term['projected_column']
            for term in c['contrast_terms']:assert term['qualified'] in qs and term['coefficient']<=0
            for column in range(32):
                g.append(sum(t['coefficient'] for t in c['expected_projection_terms'] if column&t['forbidden']==t['projected_column'])+sum(t['coefficient'] for t in c['contrast_terms'] if column&t['qualified']))
            assert g==c['column_costs'] and m*max(abs(v) for v in g)<2**62
            g=np.array(g,dtype=np.int64);bounds=[]
            for color,ids in enumerate((iw,ib)):
                bound=None
                for start in range(0,len(ids),200000):
                    values=g[arrays[color][ids[start:start+200000]]].sum(axis=1)
                    v=int(values.max() if color==0 else values.min())
                    bound=v if bound is None else (max(bound,v) if color==0 else min(bound,v))
                bounds.append(bound)
            zsum=sum(t['coefficient'] for t in c['contrast_terms'])
            assert bounds==[c['white_max'],c['black_min']] and zsum==c['contrast_sum']
            assert bounds[1]-bounds[0]-zsum==c['margin']>0;return
        assert node['kind']=='threshold_split';k=qs.index(node['qualified']);children={c['threshold']:c['node'] for c in node['children']}
        for t in range(1,m+1):
            w=iw[weights[0][iw,k]<t];b=ib[weights[1][ib,k]>=t]
            assert node['threshold_cases'][t-1]=={'threshold':t,'candidates':[len(w),len(b)]}
            if len(w) and len(b):assert t in children;walk(children[t],w,b)
    walk(doc['root'],np.arange(len(arrays[0])),np.arange(len(arrays[1])))
    assert len(seen)==len(doc['nodes'])
    return {'case':case,'m':m,'verdict':'NO','checked_nodes':len(seen),'no_lp_solver_used':True}


def run():
    started=time.monotonic();full=[check_full(c,m) for c,m in TARGETS]
    controls=[]
    for witness in json.loads((ROOT/'basis_controls.json').read_text()):
        colors={name:[{'orbit':witness[name],'probability':'1'}] for name in ('white','black')}
        controls.append({'case':witness['case'],'m':witness['m'],**distribution(witness['case'],witness['m'],colors)})
    relaxed_doc=json.loads((ROOT/'expected_count_control.json').read_text())
    checked=distribution(relaxed_doc['case'],relaxed_doc['m'],relaxed_doc['witness'],False)
    assert checked['full_security_violations']
    relaxed={'case':relaxed_doc['case'],'m':relaxed_doc['m'],'verdict':'YES','verification':checked,'no_lp_solver_used':True}
    result={'full_model':full,'positive_controls':controls,'expected_count_control':relaxed,'seconds':time.monotonic()-started}
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    run()
