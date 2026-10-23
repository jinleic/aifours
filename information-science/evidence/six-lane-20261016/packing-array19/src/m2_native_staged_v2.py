#!/usr/bin/env python3
"""Supervised per-item native core. NO token/bigmem ownership or /bin/ps helper inside this group.
Owner holds capacity and the reviewed supervise_r3 controls the entire process group on every exceptional exit.
Same B constructor, Kissat/CaDiCaL limits, staged binary DRAT zstd1/raw1200MiB/compressed500MiB as the old protocol;
new successful-write/close measurements for BOTH CNF feeds, exact completed collectors, and persistent INVALID class.
No regular-file CNF/proof retention. Native stdout is hashed; only bounded solver text/status lines are retained.
"""
import errno
import hashlib
import json
import os
import subprocess
import sys
import threading
import time
from compression import zstd
from pathlib import Path

import encode_skel_b as ENC
import m2_supervised_runtime_v2 as R

L = Path(__file__).resolve().parent.parent
CHUNK = 1 << 20
MAX_RAW = 1200*1024**2
MAX_ZBUF = 500*1024**2
KISSAT,CADICAL,DT = '/opt/homebrew/bin/kissat','/opt/homebrew/bin/cadical',str(L/'tools/drat-trim/drat-trim')
P0 = [4,3,3,3,3,3]


class BoundedUnknown(Exception):
    pass


def status_lines(raw):
    return [v.decode('ascii','backslashreplace') for v in raw.replace(b'\r',b'').split(b'\n') if v.startswith(b's ')]


def collector(stream,record,retain=False):
    h,n,line,out = hashlib.sha256(),0,bytearray(),bytearray()
    lines,error,eof,overline = [],None,False,False
    def endline():
        nonlocal overline
        if line.startswith(b's '):
            if overline: raise ValueError('overlong native status line')
            if len(lines) >= 16: raise ValueError('bounded native status-line count exceeded')
            lines.append(bytes(line).decode('ascii','backslashreplace'))
        line.clear()
        overline = False
    try:
        while True:
            b = stream.read(65536)
            if not b:
                eof = True
                break
            h.update(b)
            n += len(b)
            if retain:
                if len(out)+len(b) > 2*1024**2: raise ValueError('bounded solver stdout capture exceeded')
                out.extend(b)
            parts = b.replace(b'\r',b'').split(b'\n')
            for k,part in enumerate(parts):
                if len(line)+len(part) > 4096:
                    overline = True
                line.extend(part[:max(0,4096-len(line))])
                if k != len(parts)-1: endline()
        if line: endline()
    except BaseException as exc:
        error = repr(exc)
    finally:
        try: stream.close()
        except BaseException as exc: error = error or repr(exc)
        record.update(bytes_read=n,sha256=h.hexdigest(),status_lines=lines,error=error,complete=bool(eof and error is None))
        if retain: record['text'] = bytes(out).decode('utf-8','replace')


def feed_cnf(path,data,record,stop,deadline):
    """Derived from reviewed M7 feed pattern; count/hash ONLY writes that succeeded, and require close success."""
    fd,h,n,error,closed = None,hashlib.sha256(),0,None,False
    try:
        while fd is None:
            if stop.is_set() or time.monotonic() > deadline: raise TimeoutError('CNF FIFO open cancelled/deadline')
            try: fd = os.open(path,os.O_WRONLY|os.O_NONBLOCK)
            except OSError as exc:
                if exc.errno != errno.ENXIO: raise
                time.sleep(0.01)
        view = memoryview(data)
        while n < len(view):
            if stop.is_set() or time.monotonic() > deadline: raise TimeoutError('CNF write cancelled/deadline')
            try: wrote = os.write(fd,view[n:n+CHUNK])
            except BlockingIOError:
                time.sleep(0.01)
                continue
            if wrote <= 0: raise OSError('zero/negative CNF write')
            h.update(view[n:n+wrote])
            n += wrote
    except BaseException as exc:
        error = repr(exc)
    finally:
        if fd is not None:
            try:
                os.close(fd)
                closed = True
            except BaseException as exc: error = error or repr(exc)
        record.update(bytes=n,sha256=h.hexdigest(),error=error,close_ok=closed,
                      complete=bool(n == len(data) and closed and error is None))


def proof_reader(path,state,stop):
    h,n,zparts,zbytes,error,eof = hashlib.sha256(),0,[],0,None,False
    cap = None
    zc = zstd.ZstdCompressor(level=1)
    try:
        with open(path,'rb',buffering=0) as f:
            while True:
                b = f.read(CHUNK)
                if not b:
                    eof = True
                    break
                if cap: continue
                h.update(b)
                n += len(b)
                z = zc.compress(b)
                if z: zparts.append(z); zbytes += len(z)
                if n > MAX_RAW or zbytes > MAX_ZBUF:
                    cap = 'raw' if n > MAX_RAW else 'zbuf'
                    state['proof_cap_hit'] = cap
                    state.update(raw_bytes=n,raw_sha256=h.hexdigest(),compressed_bytes=zbytes,
                                 count_scope='hashed retained prefix through cap; later drained bytes not counted')
                    stop.set()
            if not cap:
                tail = zc.flush()
                if zbytes+len(tail) > MAX_ZBUF:
                    cap = 'zbuf-tail'
                    state['proof_cap_hit'] = cap
                    state.update(raw_bytes=n,raw_sha256=h.hexdigest(),compressed_bytes=zbytes,
                                 count_scope='complete raw stream; rejected compressed-frame tail not retained')
                    stop.set()
                else:
                    zparts.append(tail)
                    zbytes += len(tail)
    except BaseException as exc:
        error = repr(exc)
        state.update(raw_bytes=n,raw_sha256=h.hexdigest(),compressed_bytes=zbytes,reader_error=error,reader_complete=False)
        stop.set()
    state.update(raw_bytes=n,raw_sha256=h.hexdigest(),compressed_bytes=zbytes,chunks=zparts,
                 reader_error=error,reader_complete=bool(eof and error is None and cap is None))


def replay(parts,stream,record):
    h,n,error,complete,closed = hashlib.sha256(),0,None,False,False
    zd = zstd.ZstdDecompressor()
    try:
        for part in parts:
            raw = zd.decompress(part)
            view,offset = memoryview(raw),0
            while offset < len(view):
                wrote = stream.write(view[offset:offset+CHUNK])
                if wrote is None or wrote <= 0: raise OSError('incomplete proof pipe write')
                h.update(view[offset:offset+wrote])
                offset += wrote
                n += wrote
        if not zd.eof or zd.unused_data:
            raise ValueError('incomplete/extra zstd frame')
        complete = True
    except BaseException as exc:
        error = repr(exc)
    finally:
        try: stream.close(); closed = True
        except BaseException as exc: error = error or repr(exc)
        record.update(bytes=n,sha256=h.hexdigest(),error=error,close_ok=closed,complete=bool(complete and closed and error is None))


def start_native(command,collect,retain,stdin=False,start_hook=None):
    p = subprocess.Popen(command,stdin=subprocess.PIPE if stdin else subprocess.DEVNULL,stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,bufsize=0)
    if start_hook is not None: start_hook(p)  # control harness only; production never supplies it
    t = threading.Thread(target=collector,args=(p.stdout,collect,retain),daemon=True)
    t.start()
    return p,t


def await_native(p,seconds,stop):
    end = time.monotonic()+seconds+60
    while p.poll() is None:
        if stop.is_set(): raise BoundedUnknown('declared proof cap/reader stop')
        if time.monotonic() > end: raise BoundedUnknown('native wall/grace bound')
        time.sleep(0.02)
    return p.returncode


def outcome(result):
    """INVALID is persistent; bounded timeout/cap/resource UNKNOWN is different and never qualifies."""
    if result.get('solver_rc') == 10 or result.get('solver_collector',{}).get('status_lines') == ['s SATISFIABLE']:
        return 'SAT',True  # preserve an UNVERIFIED candidate even when later feed/lifecycle cleanup fails
    dc = result.get('checker_collector',{})
    if any('NOT VERIFIED' in str(v) for v in dc.get('status_lines',[])):
        return 'INVALID',True
    if dc.get('complete') and dc.get('status_lines') not in (['s VERIFIED'],['s TIMEOUT']):
        return 'INVALID',True
    if result.get('lifecycle_error'):
        return 'UNKNOWN',True
    if result.get('resource_refusal') or result.get('proof_cap_hit'):
        return 'UNKNOWN',bool(result.get('resource_refusal'))
    if result.get('proof_integrity_error') or result.get('input_integrity_error'):
        return 'INVALID',True
    if result.get('bounded_unknown'):
        return ('INVALID',True) if result.get('proof_stream',{}).get('reader_error') else ('UNKNOWN',False)
    sc,dc = result.get('solver_collector',{}),result.get('checker_collector',{})
    if sc.get('error') or not sc.get('complete'):
        return 'INVALID',True
    s,rc = sc.get('status_lines'),result.get('solver_rc')
    if rc == 10 and s == ['s SATISFIABLE']:
        return 'SAT',True
    expected_bytes,expected_sha = result['cnf_bytes'],result['cnf_sha256']
    sf = result.get('cnf_feeds',{}).get('solver',{})
    if sf.get('error') or not sf.get('complete') or not sf.get('close_ok') or sf.get('bytes') != expected_bytes or sf.get('sha256') != expected_sha:
        return 'INVALID',True
    if rc == 0 and s in ([],['s UNKNOWN']):
        return 'UNKNOWN',False
    if rc != 20 or s != ['s UNSATISFIABLE']:
        return 'INVALID',True
    if dc.get('complete') and dc.get('error') is None and dc.get('status_lines') == ['s TIMEOUT']:
        return 'UNKNOWN',False
    if set(result.get('cnf_feeds',{})) != {'solver','checker'}:
        return 'INVALID',True
    for feed in result['cnf_feeds'].values():
        if feed.get('error') or not feed.get('complete') or not feed.get('close_ok') or feed.get('bytes') != expected_bytes or feed.get('sha256') != expected_sha:
            return 'INVALID',True
    if result.get('checker_rc') != 0 or not dc.get('complete') or dc.get('error') or dc.get('status_lines') != ['s VERIFIED']:
        return 'INVALID',True
    p,r = result['proof_stream'],result['proof_delivery']
    if not p.get('reader_complete') or p.get('reader_error') or not r.get('complete') or r.get('error') or not r.get('close_ok'):
        return 'INVALID',True
    if r.get('bytes') != p.get('raw_bytes') or r.get('sha256') != p.get('raw_sha256'):
        return 'INVALID',True
    return 'UNSAT',False


def pipeline(raw,job,commands=None,start_hook=None):
    """commands/start_hook are library-only controlled fixtures; the production CLI supplies neither."""
    result = {'schema':'PA19-NATIVE-RESULT-v2','cnf_sha256':hashlib.sha256(raw).hexdigest(),'cnf_bytes':len(raw),
              'cnf_feeds':{'solver':{},'checker':{}},'solver_collector':{},'checker_collector':{},
              'proof_stream':{},'proof_delivery':{},'gates':[],'no_regular_cnf_or_proof':True}
    result['tier'] = job['lease']['tier']
    folder = Path(job['workdir'])
    assert folder.resolve().is_relative_to(L.resolve()), 'native I/O escapes owned lane'
    folder.mkdir(parents=True,exist_ok=False)
    paths = {k:str(folder/k) for k in ('solver-cnf.fifo','checker-cnf.fifo','proof.fifo')}
    for p in paths.values(): os.mkfifo(p,0o600)
    stop,threads = threading.Event(),[]
    s = job['solver_seconds']
    native = [KISSAT,'-q','-f','--seed=1','--time=%d' % s] if job['solver'] == 'kissat' else [CADICAL,'-q','-t',str(s)]
    solver_command = native+[paths['solver-cnf.fifo'],paths['proof.fifo']]
    checker_command = [DT,paths['checker-cnf.fifo'],'-i','-t',str(job['checker_seconds'])]
    if commands is not None: solver_command,checker_command = commands(paths)
    result.update(solver_command=solver_command,checker_command=checker_command)
    try:
        sf = threading.Thread(target=feed_cnf,args=(paths['solver-cnf.fifo'],raw,result['cnf_feeds']['solver'],stop,job['lease']['item_deadline_monotonic']),daemon=True)
        pr = threading.Thread(target=proof_reader,args=(paths['proof.fifo'],result['proof_stream'],stop),daemon=True)
        sf.start(); threads.append(sf)
        pr.start(); threads.append(pr)
        t0 = time.monotonic()
        gate = R.full_gate(job['lease'],'solver')
        result['gates'].append(gate)
        if not gate['admitted']: result['resource_refusal'] = gate['errors']; return result
        sp,st = start_native(solver_command,result['solver_collector'],True,start_hook=start_hook)
        threads.append(st)
        result['solver_rc'] = await_native(sp,s,stop)
        result['solver_stop'] = 'self'
        result['solve_seconds'] = time.monotonic()-t0
        for t in (sf,pr,st): t.join(60)
        if any(t.is_alive() for t in (sf,pr,st)): raise RuntimeError('solver feed/proof/collector thread incomplete')
        if result['proof_stream'].get('proof_cap_hit'):
            result['proof_cap_hit'] = result['proof_stream']['proof_cap_hit']
            return result
        sc = result['solver_collector']
        if result['solver_rc'] != 20 or sc.get('status_lines') != ['s UNSATISFIABLE'] or not sc.get('complete') or sc.get('error'):
            return result
        if result['cnf_feeds']['solver'].get('bytes') != len(raw) or not result['cnf_feeds']['solver'].get('complete'):
            result['input_integrity_error'] = 'solver CNF delivery incomplete'
            return result
        if not result['proof_stream'].get('reader_complete') or result['proof_stream'].get('reader_error'):
            result['proof_integrity_error'] = 'solver proof stream incomplete/failed'
            return result
        cf = threading.Thread(target=feed_cnf,args=(paths['checker-cnf.fifo'],raw,result['cnf_feeds']['checker'],stop,job['lease']['item_deadline_monotonic']),daemon=True)
        t1 = time.monotonic()
        gate = R.full_gate(job['lease'],'checker')
        result['gates'].append(gate)
        if not gate['admitted']: result['resource_refusal'] = gate['errors']; return result
        dp,dt = start_native(checker_command,result['checker_collector'],False,stdin=True,start_hook=start_hook)
        threads.append(dt)
        cf.start(); threads.append(cf)
        rp = threading.Thread(target=replay,args=(result['proof_stream']['chunks'],dp.stdin,result['proof_delivery']),daemon=True)
        rp.start(); threads.append(rp)
        result['checker_rc'] = await_native(dp,job['checker_seconds'],threading.Event())
        result['checker_stop'] = 'self'
        result['check_seconds'] = time.monotonic()-t1
        for t in (cf,rp,dt): t.join(60)
        if any(t.is_alive() for t in (cf,rp,dt)): raise RuntimeError('checker feed/replay/collector thread incomplete')
    except BoundedUnknown as exc:
        result['bounded_unknown'] = str(exc)
        result['proof_cap_hit'] = result['proof_stream'].get('proof_cap_hit')
    except BaseException as exc:
        result['lifecycle_error'] = repr(exc)
    finally:
        stop.set()
        # Freeze public metrics away from any daemon that is still unwinding after a failure.
        result['proof_stream'] = {k:v for k,v in result['proof_stream'].items() if k != 'chunks'}
        result['solver_collector'] = dict(result['solver_collector'])
        result['checker_collector'] = dict(result['checker_collector'])
        result['cnf_feeds'] = {k:dict(v) for k,v in result['cnf_feeds'].items()}
        result['proof_delivery'] = dict(result['proof_delivery'])
        result['status'],result['halt_production'] = outcome(result)
        if result['status'] not in ('SAT','INVALID'):
            result['solver_collector'].pop('text',None)  # statuses/hash/completion retained; no redundant progress transcript
        if result['status'] == 'UNSAT' and len((json.dumps(result,indent=1)+'\n').encode()) > 32768:
            result.update(status='UNKNOWN',halt_production=True,metadata_bound_error='ordinary worker receipt exceeds32KiB')
    return result


def recipe_cnf(job):
    recipe = job['recipe']
    sp = L/recipe['skeleton_path']
    assert R.digest(sp) == recipe['skeleton_sha256'] and R.digest(L/'src'/'encode_skel_b.py') == recipe['encoder_sha256']
    D = json.loads(sp.read_bytes())
    sk = D['skeletons'][recipe['b_index']]
    special = [p for p in D['profiles'] if list(p) != P0]
    if recipe['mode'] == 'direct':
        nv,cl = ENC.build_v2(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special)
    elif recipe['mode'] == 'partbatch':
        ep = L/recipe['list_path']
        assert R.digest(ep) == recipe['list_sha256']
        ed = json.loads(ep.read_bytes())
        assert ed['num_placements'] == len(ed['placements']) == recipe['complete_denominator'] > 0
        lo,hi = recipe['indices']
        nv,cl = ENC.build_partbatch(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special,[ed['placements'][i] for i in range(lo,hi+1)])
    else: raise ValueError('unknown production recipe')
    raw = ENC.cnf_bytes(nv,cl)
    assert len(raw) == job['cnf_bytes'] and hashlib.sha256(raw).hexdigest() == job['cnf_sha256'],'owner/worker construction differs'
    return raw


def main():
    path,h = Path(sys.argv[1]),sys.argv[2]
    assert R.digest(path) == h
    job = json.loads(path.read_bytes())
    assert job['schema'] == 'PA19-NATIVE-JOB-v2' and job['solver'] in ('kissat','cadical')
    assert job['checker_seconds'] == 1200 and job['solver_seconds'] in (300,600)
    assert os.getppid() == job['lease']['owner_pid'] == int(os.environ['K3_SUPERVISOR_PID'])
    assert os.environ['K3_SUPERVISOR_SCRIPT'] == str(R.SUP_PATH) and R.digest(R.SUP_PATH) == R.SUP_SHA
    assert R.digest(KISSAT if job['solver'] == 'kissat' else CADICAL) == job['solver_binary_sha256'] and R.digest(DT) == job['checker_binary_sha256']
    assert Path(job['result_path']).parent.resolve().is_relative_to(L.resolve())
    for rel,expected in job['source_sha256'].items():
        assert not Path(rel).is_absolute() and (L/rel).resolve().is_relative_to(L.resolve())
        assert R.digest(L/rel) == expected, 'worker source changed: '+rel
    try:
        raw = recipe_cnf(job)
        result = pipeline(raw,job)
    except BaseException as exc:
        result = {'schema':'PA19-NATIVE-RESULT-v2','status':'INVALID','halt_production':True,'construction_error':repr(exc)}
    result['tier'] = job['lease']['tier']
    payload = (json.dumps(result,indent=1)+'\n').encode()
    assert len(payload) <= 16*1024**2, 'halting worker diagnostic bound'
    temporary = job['result_path']+'.writing'
    with open(temporary,'xb') as f:
        f.write(payload)
    os.link(temporary,job['result_path'])  # no partial scientific JSON if a sole-RSS stop interrupts publication
    print(json.dumps({k:result.get(k) for k in ('status','halt_production','solve_seconds','check_seconds','bounded_unknown','lifecycle_error')}),flush=True)


if __name__ == '__main__':
    main()
