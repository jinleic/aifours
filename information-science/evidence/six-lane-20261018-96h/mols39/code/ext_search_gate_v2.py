#!/usr/bin/env python3
"""WRITTEN ONLY. Prefix/artifact gate for ext-search-plan-v1.json. Single process, stdlib, no date/subprocess.
Only control qualification is possible. No target nonexistence claim is emitted by this gate.
Reads actual result/raw artifacts and parent audits, strict canonical JSON, typed fields, rechecks every solution.
Agrees only when independent COMPLETE sets match and controls meet their frozen mathematical premises.
Prior gates are included in the audited prefix. Every job and gate needs its own GO; never autochains.
"""
import os, sys, stat, json, hashlib, math, time
KEYS={'status','reason','program','n','q','k','m','chunk_lo','chunk_hi','mode','chunks','solutions','solutions_sha256','input_sha256','program_sha256','extra','wall_s'}
MFILES=('neg6.raw','neg12.raw','dm21_base5.raw','dm21_deleted.raw','singer57_base7.raw','singer57_deleted.raw','bad6.raw')
CODE={'COMPLETE':0,'ESTIMATE':0,'STOPPED_AT_SOLUTIONS':1,'INCOMPLETE_BUDGET':5,'INCOMPLETE_OUTPUT':6,'BAD_INPUT':2,'INPUT_PIN_MISMATCH':2,'IO_ERROR':2,'NOT_DM':3,'INTERNAL_ERROR':4}
GKEYS={'status','reason','self','plan_sha256','prefix','all_as_expected','qualified','target_claim','items','wall_s'}
AKEYS={'format','item','plan_sha256','verdict','settled','exit_code','declared_output_sha256','receipt_sha256','auditor','at','notes'}
CAP=16<<20

class Failure(Exception):pass

def digest(b):return hashlib.sha256(b).hexdigest()
def exact(a,b):
    if type(a) is not type(b):return False
    if type(a) is dict:return set(a)==set(b) and all(exact(a[k],b[k]) for k in a)
    if type(a) is list:return len(a)==len(b) and all(exact(x,y) for x,y in zip(a,b))
    return a==b
def parse(b):
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise Failure('duplicate JSON key')
            d[k]=v
        return d
    def bad(v):raise Failure('nonfinite JSON')
    def fl(v):
        x=float(v)
        if not math.isfinite(x):raise Failure('nonfinite JSON')
        return x
    try:return json.loads(b.decode('utf8'),object_pairs_hook=pairs,parse_constant=bad,parse_float=fl)
    except (ValueError,UnicodeError,RecursionError):raise Failure('JSON grammar') from None

def canonical(b,keys):
    d=parse(b)
    if type(d) is not dict or set(d)!=set(keys):raise Failure('object keys')
    if (json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')!=b:raise Failure('canonical bytes')
    return d

def dirfd(path):
    if not path.startswith('/') or any(p in ('','.','..') for p in path.split('/')[1:]):raise Failure('absolute real path required')
    fd=os.open('/',os.O_RDONLY|os.O_DIRECTORY)
    try:
        for p in path.split('/')[1:]:
            nxt=os.open(p,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd);os.close(fd);fd=nxt
    except BaseException:os.close(fd);raise
    return fd

def readat(fd,name):
    if '/' in name or name in ('','.','..'):raise Failure('plain name required')
    f=os.open(name,os.O_RDONLY|os.O_NOFOLLOW,dir_fd=fd)
    try:
        st=os.fstat(f)
        if not stat.S_ISREG(st.st_mode) or st.st_nlink!=1 or st.st_size>CAP:raise Failure('artifact kind/link/cap')
        bs=[];total=0
        while True:
            b=os.read(f,1048576)
            if not b:break
            total+=len(b)
            if total>CAP:raise Failure('artifact cap')
            bs.append(b)
        return b''.join(bs)
    finally:os.close(f)

def rawrows(b):
    ls=b.split(b'\n')
    if ls[-1]==b'':ls.pop()
    ans=[]
    for ln in ls:
        ts=ln.split()
        if not ts:raise Failure('G1 blank row')
        for t in ts:
            z=t[1:] if t[:1] in (b'+',b'-') else t
            if not z.isdigit():raise Failure('G1 token')
        ans.append([int(t) for t in ts])
    return ans


def validate_result(b,job,raw,control):
    d=canonical(b,KEYS)
    if d['program']!=job['program_name'] or d['status']!=job['status']:raise Failure('program/status mismatch')
    if type(d['wall_s']) is not float or not math.isfinite(d['wall_s']) or d['wall_s']<0:raise Failure('wall field')
    if d['input_sha256']!=digest(raw):raise Failure('actual raw hash mismatch')
    if type(d['program_sha256']) is not str or len(d['program_sha256'])!=64:raise Failure('informational program hash shape')
    if type(d['extra']) is not dict or any(type(v) is not int for v in d['extra'].values()):raise Failure('extra schema')
    if type(d['solutions']) is not list or type(d['chunks']) is not list:raise Failure('result lists')
    sols=d['solutions']
    if digest(json.dumps(sols,separators=(',',':')).encode('ascii'))!=d['solutions_sha256']:raise Failure('actual solution digest')
    if d['status'] in ('NOT_DM','INPUT_PIN_MISMATCH'):
        if type(d['reason']) is not str or not d['reason']:raise Failure('intended-error reason missing')
        if sols:raise Failure('error result contains solutions')
        return d
    D=rawrows(raw);n=len(D[0]);k=len(D)
    for key,val in (('n',n),('q',n//3),('k',k),('m',control['m']),('chunk_lo',control['lo']),('chunk_hi',control['hi']),('mode','search')):
        if not exact(d[key],val):raise Failure('result '+key)
    if d['reason'] is not None:raise Failure('COMPLETE reason must be null')
    if sols!=sorted(sols) or len({tuple(f) for f in sols})!=len(sols):raise Failure('solution order/duplicates')
    counts={}
    for f in sols:
        if type(f) is not list or len(f)!=n or any(type(v) is not int or not 0<=v<n for v in f) or f[0]!=0:raise Failure('solution vector')
        idx=0
        for c in range(1,control['m']+1):idx=idx*n+f[c]
        if not control['lo']<=idx<control['hi']:raise Failure('solution outside chunk')
        if any(len({(row[c]-f[c])%n for c in range(n)})!=n for row in D):raise Failure('direct extension failure')
        counts[idx]=counts.get(idx,0)+1
    if len(d['chunks'])!=control['hi']-control['lo']:raise Failure('chunk coverage')
    for idx,e in zip(range(control['lo'],control['hi']),d['chunks']):
        if type(e) is not dict or set(e)!={'chunk','status','nodes','solutions'}:raise Failure('chunk schema')
        if not exact(e['chunk'],idx) or e['status']!='COMPLETE' or type(e['nodes']) is not int or e['nodes']<0 or not exact(e['solutions'],counts.get(idx,0)):raise Failure('chunk contents')
    return d


def main(argv):
    t0=time.monotonic();out={'status':'ERROR','reason':None,'self':None,'plan_sha256':None,'prefix':[],
        'all_as_expected':False,'qualified':False,'target_claim':'UNEVALUATED','items':[],'wall_s':0.0}
    rc=2;opened=[]
    try:
        if len(argv)!=8 or argv[0]!='--plan' or argv[2]!='--plan-sha256' or argv[4]!='--self' or argv[6]!='--budget-s':raise Failure('arguments')
        path,pin,selfname,S=argv[1],argv[3],argv[5],float(argv[7])
        if not math.isfinite(S) or not 0<S<=280:raise Failure('budget')
        def tick():
            if time.monotonic()-t0>S:raise TimeoutError('budget')
        pb=open(path,'rb').read(CAP+1)
        if len(pb)>CAP or digest(pb)!=pin:raise Failure('plan pin')
        plan=parse(pb);jobs={j['item']:j for j in plan['jobs']};order=plan['order']
        if selfname not in jobs or jobs[selfname]['kind']!='gate' or order!=[j['item'] for j in plan['jobs']]:raise Failure('self/order')
        prefix=order[:order.index(selfname)];out.update(self=selfname,plan_sha256=pin,prefix=prefix)
        base=dirfd(plan['base_dir']);audit=dirfd(plan['audit_dir']);opened += [base,audit]
        mine=os.open(selfname,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=base)
        opened.append(mine)
        a,b=os.stat('.'),os.fstat(mine)
        if (a.st_dev,a.st_ino)!=(b.st_dev,b.st_ino):raise Failure('wrong working root')
        for p in plan['pins']:
            tick();data=open(p['path'],'rb').read(CAP+1)
            if len(data)>CAP or digest(data)!=p['sha256']:raise Failure('source/input pin '+p['path'])
        states={};ok={};controls=None;datafiles=None
        for item in prefix:
            tick();j=jobs[item];rec={'item':item,'problems':[],'artifacts':{}}
            try:
                fd=os.open(item,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=base)
                try:files={nm:readat(fd,nm) for nm in j['outputs']}
                finally:os.close(fd)
                hashes={nm:digest(bs) for nm,bs in files.items()};rec['artifacts']=hashes
                aud=parse(readat(audit,item+'.audit.json'))
                if type(aud) is not dict or set(aud)!=AKEYS:raise Failure('audit keys')
                wanted={'format':'ext-search-job-audit-v1','item':item,'plan_sha256':pin,'verdict':'AUDITED_PASS','settled':True,'exit_code':j['exit']}
                for key,val in wanted.items():
                    if not exact(aud[key],val):raise Failure('audit '+key)
                if not exact(aud['declared_output_sha256'],hashes):raise Failure('actual artifact/audit hashes')
                if any(type(aud[k]) is not str for k in ('receipt_sha256','auditor','at','notes')):raise Failure('audit string fields')
                if j['kind']=='data':
                    maker=canonical(files['result.json'],('status','reason','files','manifest_sha256','wall_s'))
                    if type(maker['wall_s']) is not float or not math.isfinite(maker['wall_s']) or maker['wall_s']<0:raise Failure('maker wall field')
                    if maker['status']!='OK' or maker['reason'] is not None or maker['files']!=list(MFILES) or maker['manifest_sha256']!=digest(files['manifest.json']):raise Failure('maker result')
                    man=canonical(files['manifest.json'],('format','dm21_input_sha256','files','controls'))
                    if man['format']!='ext-search-controls-v1' or set(man['files'])!=set(MFILES):raise Failure('control manifest')
                    if man['dm21_input_sha256']!=plan['dm21_sha256']:raise Failure('DM21 provenance pin')
                    for nm in MFILES:
                        if not exact(man['files'][nm],{'sha256':digest(files[nm]),'bytes':len(files[nm])}):raise Failure('control data hash')
                    if [c['name'] for c in man['controls']]!=['N6','N12','P21','P57','BAD_DM','BAD_PIN']:raise Failure('control names')
                    controls={c['name']:c for c in man['controls']};datafiles=files
                elif j['kind']=='search':
                    if not ok.get('DATA') or controls is None:raise Failure('unaudited DATA dependency')
                    ctl=controls[j['control']];raw=datafiles[ctl['raw']]
                    res=validate_result(files['result.json'],j,raw,ctl)
                    if ctl['expected']=='COMPLETE_ZERO' and res['solutions']:raise Failure('parity control notzero')
                    if ctl['expected']=='COMPLETE_CONTAINS':
                        known=rawrows(datafiles[ctl['known']])[0]
                        if known not in res['solutions']:raise Failure('known deleted row missing')
                    states[item]=res
                    peer=j.get('compare_to')
                    if peer is not None:
                        if not ok.get(peer) or states[peer]['solutions']!=res['solutions'] or states[peer]['solutions_sha256']!=res['solutions_sha256']:raise Failure('independent COMPLETE sets disagree')
                elif j['kind']=='gate':
                    g=canonical(files['result.json'],GKEYS)
                    if g['status']!='OK' or g['reason'] is not None or g['self']!=item or g['plan_sha256']!=pin or g['prefix']!=order[:order.index(item)] or g['all_as_expected'] is not True or g['qualified'] is not False or g['target_claim']!='UNEVALUATED':raise Failure('prior gate artifact')
                else:raise Failure('unknown jobkind')
            except (Failure,OSError,ValueError,KeyError,TypeError,IndexError) as e:rec['problems'].append(str(e))
            ok[item]=not rec['problems'];out['items'].append(rec)
        tick();good=all(ok.values())
        out.update(status='OK',all_as_expected=good,qualified=(good and selfname==plan['final_gate']))
        rc=0 if good else 1
    except TimeoutError:out.update(status='BUDGET_EXCEEDED',reason='budget');rc=5
    except Exception as e:out.update(status='ERROR',reason=str(e));rc=2
    finally:
        for f in reversed(opened):os.close(f)
    out['wall_s']=round(time.monotonic()-t0,3)
    data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    try:
        f=os.open('result.json',os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
        try:
            v=memoryview(data)
            while v:
                k=os.write(f,v)
                if k<=0:raise OSError('zero write')
                v=v[k:]
        finally:os.close(f)
    except OSError:return 2
    print(data.decode('ascii'),end='',flush=True);return rc

if __name__=='__main__':sys.exit(main(sys.argv[1:]))
