#!/usr/bin/env python3
"""WRITTEN ONLY: exact-data maker, no search; run only after its own GO. Stdlib, one process, no subprocess/date.
Outputs seven raw files + manifest.json + result.json. Reimplements Singer57 from its published recipe:
B=(1,6,7,9,19,38,42,49), columns B[u+a*v] over GF8, v!=0, plus zero column.
All positives are directly DM-checked. Candidate f is the deleted row translated to f[0]=0.
Zn6/Zn12 base rows are0 and identity. Their unrestricted extension is impossible by the elementary sum parity proof.
Zn12 control fixes the near-complete-mapping prefix f[i]=2*i mod11 fori1..9, leaving2 columns free.
DM21/Singer57 planted controls fix n-3 columns, leaving exactly2 free columns, so at most n^2 completions.
These planted controls do not calibrate the target's full tree. No third-party code is executed/imported.
"""
import os, sys, json, hashlib, time, math, stat
RAW_CAP=1<<20
NAMES=('neg6.raw','neg12.raw','dm21_base5.raw','dm21_deleted.raw','singer57_base7.raw','singer57_deleted.raw','bad6.raw')

def put(name,data):
    fd=os.open(name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
    try:
        v=memoryview(data)
        while v:
            k=os.write(fd,v)
            if k<=0:raise OSError('zero write')
            v=v[k:]
    finally:os.close(fd)

def anchored_parent(path):
    """Open every absolute parent component without following symlinks; return retained parent fd + name."""
    if type(path) is not str or not path.startswith("/") or "\x00" in path:
        raise OSError("absolute normalized file path required")
    components = path.split("/")[1:]
    if not components or any(c in ("", ".", "..") for c in components):
        raise OSError("non-normalized file path")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in components[:-1]:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd, components[-1]
    except BaseException:
        os.close(fd)
        raise


def anchored_file_fd(path, cap):
    """No raw-byte preflight read: anchor parents, open NONBLOCK, verify actual regular one-link descriptor."""
    parent, name = anchored_parent(path)
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
    finally:
        os.close(parent)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > cap:
            raise OSError("input kind/link/cap")
        return fd
    except BaseException:
        os.close(fd)
        raise


def anchored_read_bytes(path, cap, check=None):
    if check is not None:
        check()
    fd = anchored_file_fd(path, cap)
    try:
        blocks, total = [], 0
        while True:
            if check is not None:
                check()
            block = os.read(fd, min(65536, cap + 1 - total))
            if check is not None:
                check()
            if not block:
                break
            total += len(block)
            if total > cap:
                raise OSError("input grew beyond cap")
            blocks.append(block)
        if os.fstat(fd).st_nlink != 1:
            raise OSError("input link count changed")
        return b"".join(blocks)
    finally:
        os.close(fd)


def main(argv):
    start=time.monotonic();status,reason='OK',None;files=[];manifest_sha=None
    try:
        if len(argv)!=6 or argv[0]!='--dm21' or argv[2]!='--dm21-sha256' or argv[4]!='--budget-s':raise ValueError('arguments')
        path,pin=argv[1],argv[3];budget=float(argv[5])
        if not math.isfinite(budget) or not 0<budget<=280:raise ValueError('budget')
        def tick():
            if time.monotonic()-start>budget:raise TimeoutError('budget')
        raw=anchored_read_bytes(path,RAW_CAP,tick)
        if len(raw)>RAW_CAP or hashlib.sha256(raw).hexdigest()!=pin:raise ValueError('input pin/cap')
        lines=raw.split(b'\n')
        if lines[-1]==b'':lines.pop()
        dm=[]
        for line in lines:
            ts=line.split()
            if not ts:raise ValueError('G1 blank')
            for t in ts:
                z=t[1:] if t[:1] in (b'+',b'-') else t
                if not z.isdigit():raise ValueError('G1 token')
            dm.append([int(t)%21 for t in ts])
        if len(dm)!=6 or any(len(r)!=21 for r in dm):raise ValueError('DM21 shape')
        def isdm(rows,n):
            return all(len({(rows[x][c]-rows[y][c])%n for c in range(n)})==n for x in range(len(rows)) for y in range(x+1,len(rows)))
        if not isdm(dm,21):raise ValueError('DM21 notDM')
        def mul(a,b):
            r=0
            for i in range(3):
                if (b>>i)&1:r^=a<<i
            for i in (4,3):
                if (r>>i)&1:r^=0b1011<<(i-3)
            return r
        B=(1,6,7,9,19,38,42,49)
        cols=[[B[u^mul(a,v)] for a in range(8)] for u in range(8) for v in range(1,8)]+[[0]*8]
        sg=[[c[a] for c in cols] for a in range(8)]
        if not isdm(sg,57):raise ValueError('Singer57 notDM')
        neg6=[[0]*6,list(range(6))];neg12=[[0]*12,list(range(12))]
        datasets={'neg6.raw':neg6,'neg12.raw':neg12,'dm21_base5.raw':dm[:5],
                  'dm21_deleted.raw':[[(v-dm[5][0])%21 for v in dm[5]]],
                  'singer57_base7.raw':sg[:7],
                  'singer57_deleted.raw':[[(v-sg[7][0])%57 for v in sg[7]]],
                  'bad6.raw':[[0]*6,[0]*6]}
        tick()
        blobs={name:('\n'.join(' '.join(map(str,r)) for r in datasets[name])+'\n').encode('ascii') for name in NAMES}
        tick()
        def chunk(vals,n,m):
            idx=0
            for c in range(1,m+1):idx=idx*n+vals[c]
            return idx
        known21=datasets['dm21_deleted.raw'][0];known57=datasets['singer57_deleted.raw'][0]
        pref12=[(2*i)%11 for i in range(12)]
        controls=[{'name':'N6','raw':'neg6.raw','n':6,'k':2,'m':0,'lo':0,'hi':1,'expected':'COMPLETE_ZERO','known':None},
                  {'name':'N12','raw':'neg12.raw','n':12,'k':2,'m':9,'lo':chunk(pref12,12,9),'hi':chunk(pref12,12,9)+1,'expected':'COMPLETE_ZERO','known':None},
                  {'name':'P21','raw':'dm21_base5.raw','n':21,'k':5,'m':18,'lo':chunk(known21,21,18),'hi':chunk(known21,21,18)+1,'expected':'COMPLETE_CONTAINS','known':'dm21_deleted.raw'},
                  {'name':'P57','raw':'singer57_base7.raw','n':57,'k':7,'m':54,'lo':chunk(known57,57,54),'hi':chunk(known57,57,54)+1,'expected':'COMPLETE_CONTAINS','known':'singer57_deleted.raw'},
                  {'name':'BAD_DM','raw':'bad6.raw','n':6,'k':2,'m':0,'lo':0,'hi':1,'expected':'NOT_DM','known':None},
                  {'name':'BAD_PIN','raw':'neg6.raw','n':6,'k':2,'m':0,'lo':0,'hi':1,'expected':'INPUT_PIN_MISMATCH','known':None}]
        if not isdm(dm[:5]+[known21],21) or not isdm(sg[:7]+[known57],57):raise ValueError('deleted-row recovery')
        manifest={'format':'ext-search-controls-v1','dm21_input_sha256':pin,
                  'files':{name:{'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)} for name,data in blobs.items()},'controls':controls}
        tick()
        mb=(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
        tick()
        for name,data in blobs.items():tick();put(name,data);files.append(name);tick()
        tick();put('manifest.json',mb);tick();manifest_sha=hashlib.sha256(mb).hexdigest()
        tick()
    except TimeoutError:status,reason='BUDGET_EXCEEDED','budget'
    except OSError as e:status,reason='IO_ERROR',type(e).__name__
    except Exception as e:status,reason='ERROR',str(e)
    def expired():
        return ('budget' in locals_context and math.isfinite(locals_context['budget']) and
                0<locals_context['budget']<=280 and time.monotonic()-start>locals_context['budget'])
    locals_context={'budget':budget} if 'budget' in locals() else {}
    if expired():status,reason='BUDGET_EXCEEDED','before result serialization'
    result={'status':status,'reason':reason,'files':files,'manifest_sha256':manifest_sha,'wall_s':round(time.monotonic()-start,3)}
    data=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    if expired():
        result.update(status='BUDGET_EXCEEDED',reason='before result publication')
        data=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    try:put('result.json',data)
    except OSError:return 2
    # Retained report is immutable. Late completion returns5, no rewrite or second line.
    late=expired()
    try:print(data.decode('ascii'),end='',flush=True)
    except OSError:return 2
    if late or expired():return 5
    return 0 if result['status']=='OK' else (5 if result['status']=='BUDGET_EXCEEDED' else 2)

if __name__=='__main__':sys.exit(main(sys.argv[1:]))
