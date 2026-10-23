#!/usr/bin/env python3
"""PA19 v6_1 admission/ownership. Single normal3.5GiB sampled group threshold, COUNT<=2; NO automatic retries.
v6_1 = v6 with ONE change: SUP_PATH/SUP_SHA pin supervise_pa19_v4.py (the v3 adapter plus the bounded re-poll).
Every admission gate and inventory share one persistent-veto registry (old m2k1 plus new m2k3 markers).
Local supervise_pa19_v4 copies the reviewed r3 with one ownership callback only; the exact Popen remains retained
until explicit wait/reaping AND group quiescence. Native groups contain no /bin/ps/setuid helper.
Accounting amendment: immutable exact census age<=600s, refreshed at chunk start/expiry/waits>600s; reserve all
planned remaining outputs plus256MiB. Residual: the bound covers this route's writes and assumes no other lane
writer adds>256MiB within600s. statvfs, STOP/count/deadline and contract binary checks remain per-admission fresh.
Sampled RSS thresholds are NOT kernel instantaneous hard caps. Unknown measurements refuse; safety holds persist.
"""
import ctypes
import errno
import fcntl
import hashlib
import importlib.util
import json
import os
import signal
import struct
import time
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
SUP_PATH = LANE/'src'/'supervise_pa19_v4.py'
SUP_SHA = '3b5c1808813a1f0627a4ebb721f197294659ddd66fcc7ecc09213b972c4b9f17'
BASE_GATE = 12200000000
FLOOR = 12000000000
LANE_CAP = 8*1024**3
GROUP_RSS_CAP = 3584*1024**2
CONTROL_MARGIN = 128*1024**2
DATA_CAP = 10000000000
ITEM_ORDINARY_BOUND = 384*1024
ITEM_GROWTH = 64*1024**2  # per-item worst halting diagnostic retention, no CNF/proof copies
ROUTE_FAILURE_RESERVE = 2*ITEM_GROWTH  # two admitted normal pipelines may each leave one halting diagnostic
ALL_PLANNED_RETAINED_BOUND = (5009+106+1119+117)*ITEM_ORDINARY_BOUND+ROUTE_FAILURE_RESERVE
CENSUS_TTL = 600.0
OTHER_WRITER_MARGIN = 256*1024**2
# One shared registry for EVERY admission gate and inventory. Old persistent markers are never cleared or reinterpreted.
RESOURCE_STOPS = ('STOP-hard12','STOP-m2r12','STOP-K1')
SAT_VETO_FLAGS = ('m2k1-SAT.flag','m2k3-SAT.flag')
NONSAT_VETO_FLAGS = ('m2k1-INVALID.flag','m2k1-HALT.flag','m2k1-QUARANTINE.flag','m2k3-INTEGRITY.flag','m2k3-HALT.flag','m2k3-QUARANTINE.flag')
PERSISTENT_VETO_FLAGS = SAT_VETO_FLAGS+NONSAT_VETO_FLAGS
ADMISSION_MARKERS = RESOURCE_STOPS+PERSISTENT_VETO_FLAGS
CENSUS_DIR = LANE/'cycle2'/'accounting-v3'
import lane_new_data_accounting as ACCOUNT
LIBC = ctypes.CDLL(None,use_errno=True)
LIBC.sysctl.argtypes = (ctypes.POINTER(ctypes.c_int),ctypes.c_uint,ctypes.c_void_p,ctypes.POINTER(ctypes.c_size_t),ctypes.c_void_p,ctypes.c_size_t)
LIBC.sysctl.restype = ctypes.c_int
_CANCEL = [False]
_SUP = None


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def supervisor():
    global _SUP
    if _SUP is None:
        assert digest(SUP_PATH) == SUP_SHA,'reviewed supervisor changed'
        spec = importlib.util.spec_from_file_location('pa19_reviewed_supervise_r3',SUP_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _SUP = module
    return _SUP


def install_handlers():
    def cancel(signum,frame):
        _CANCEL[0] = True  # never raises through an owner holding a possibly live group
    signal.signal(signal.SIGTERM,cancel)
    signal.signal(signal.SIGINT,cancel)


def present_vetoes(lane=LANE):
    return [name for name in PERSISTENT_VETO_FLAGS if (Path(lane)/'cycle2'/name).exists()]


def present_resource_stops(lane=LANE):
    return [name for name in RESOURCE_STOPS if (Path(lane)/'cycle2'/name).exists()]


def admission_union(lane=LANE):
    """Full admission union with distinct classifications; every gate refuses on either class."""
    return {'resource_stops':present_resource_stops(lane),'persistent_vetoes':present_vetoes(lane)}


def token_count(lane=LANE):
    text = (Path(lane)/'cycle2'/'tokens'/'COUNT').read_text().strip()
    if text not in ('0','1','2'):
        raise ValueError('COUNT is not an integer in0..2')
    return int(text)


def _argmax():
    mib = (ctypes.c_int*2)(1,8)  # CTL_KERN,KERN_ARGMAX
    value,size = ctypes.c_int(),ctypes.c_size_t(ctypes.sizeof(ctypes.c_int))
    if LIBC.sysctl(mib,2,ctypes.byref(value),ctypes.byref(size),None,0) != 0 or not (0 < value.value <= 16*1024**2):
        raise OSError(ctypes.get_errno(),'KERN_ARGMAX unavailable')
    return value.value


def _argv(pid,capacity):
    mib = (ctypes.c_int*3)(1,49,pid)  # CTL_KERN,KERN_PROCARGS2
    buf,size = ctypes.create_string_buffer(capacity),ctypes.c_size_t(capacity)
    if LIBC.sysctl(mib,3,buf,ctypes.byref(size),None,0) != 0:
        raise OSError(ctypes.get_errno(),'process argv unavailable')
    raw = buf.raw[:size.value]
    if len(raw) < 5:
        raise ValueError('short argv response')
    argc = struct.unpack_from('=i',raw)[0]
    if not (0 < argc <= 100000):
        raise ValueError('invalid argc')
    pos = raw.find(b'\0',4)
    if pos < 0:
        raise ValueError('unterminated executable path')
    while pos < len(raw) and raw[pos] == 0:
        pos += 1
    args = []
    for _ in range(argc):
        end = raw.find(b'\0',pos)
        if end < 0:
            raise ValueError('truncated argv')
        args.append(raw[pos:end])
        pos = end+1
    return args


def lane_rss(lane=LANE,group=None,owner=None):
    """Known same-euid research argv processes only; group monitor separately catches any forbidden setuid member.
    Control-plane/setuid monitoring helpers are not treated as zero-RSS lane members: an explicit128MiB margin is
    reserved. Unknown argv/probes among candidate same-euid processes fail closed; exited/zombie races are skipped.
    """
    sup = supervisor()
    capacity,needle = _argmax(),os.fsencode(str(Path(lane).resolve()))
    total,current,members = 0,0,[]
    for pid in sup.list_pids(4,os.geteuid()):  # PROC_UID_ONLY: never infer ownership from a process's name
        try:
            args = _argv(pid,capacity)
        except (OSError,ValueError):
            state,_,_ = sup.probe(pid)
            if state in ('gone','zombie'):
                continue
            raise
        if not any(needle in arg for arg in args):
            continue
        state,rss,ident = sup.probe(pid)
        if state in ('gone','zombie'):
            continue
        if state != 'alive' or rss <= 0:
            raise RuntimeError('unknown RSS for candidate lane pid%d' % pid)
        total += rss
        if pid == owner or group is not None and ident.get('pgid') == group:
            current += rss
        members.append({'pid':pid,'rss_bytes':rss,'pgid':ident.get('pgid'),'start':ident.get('start')})
    return {'known':True,'rss_bytes':total,'current_group_and_owner_bytes':current,'members':members,
            'scope':'same-euid argv contains absolute lane; no environment data;128MiB control-plane margin'}


def _json_bytes(value):
    return (json.dumps(value,indent=1)+'\n').encode()


def create_census(lane=LANE):
    """An exact allocated/logical census. Unknown/error never becomes a fresh success record."""
    started = time.monotonic()
    data = ACCOUNT.account(lane)
    if data.get('known') is not True or data.get('stat_errors') or type(data.get('new_data_usage_upper_bytes')) is not int:
        raise RuntimeError('exact lane data census unknown: '+repr(data.get('stat_errors')))
    record = {'schema':'PA19-ALLOCATED-CENSUS-v3','started_monotonic':started,'finished_monotonic':time.monotonic(),
              'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'data':data,'ttl_seconds':CENSUS_TTL}
    folder = Path(lane)/'cycle2'/'accounting-v3'; folder.mkdir(parents=True,exist_ok=True)
    path = folder/('census-%d-%d.json' % (os.getpid(),time.time_ns()))
    raw = _json_bytes(record)
    with path.open('xb') as f: f.write(raw)
    return {'path':str(path.relative_to(Path(lane))),'sha256':hashlib.sha256(raw).hexdigest()}


def census_for_gate(reference,force=False,lane=LANE):
    if not isinstance(reference,dict): raise ValueError('missing chunk census authority')
    path = Path(lane)/reference['path']
    if not path.resolve().is_relative_to((Path(lane)/'cycle2/accounting-v3').resolve()): raise ValueError('census path outside owned census directory')
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != reference['sha256']: raise ValueError('census SHA differs')
    record = json.loads(raw)
    if record.get('schema') != 'PA19-ALLOCATED-CENSUS-v3' or record.get('ttl_seconds') != CENSUS_TTL: raise ValueError('unknown census schema/TTL')
    data = record.get('data') or {}
    if data.get('known') is not True or data.get('stat_errors') or type(data.get('new_data_usage_upper_bytes')) is not int: raise ValueError('unknown cached census')
    age = time.monotonic()-record['finished_monotonic']
    if age < 0: raise ValueError('future census clock')
    if force or age > CENSUS_TTL:
        return census_for_gate(create_census(lane),False,lane)
    return {'reference':reference,'age_seconds':age,'finished_monotonic':record['finished_monotonic'],
            'current_data_upper_bytes':data['new_data_usage_upper_bytes'],'record':record}


def binary_observations(authority):
    """Expected identities are supplied only by the frozen contract, NEVER promoted from these observations."""
    if not isinstance(authority,dict) or set(authority) != {'python','solver','checker'}: raise ValueError('missing binary authorities')
    observed = {}
    for kind,item in authority.items():
        p,h = item['path'],item['sha256']
        if not isinstance(h,str) or len(h) != 64 or any(c not in '0123456789abcdef' for c in h): raise ValueError('invalid frozen binary SHA')
        if kind == 'python' and p != os.path.abspath(__import__('sys').executable): raise ValueError('unexpected Python binary path')
        if kind == 'solver' and p not in ('/opt/homebrew/bin/kissat','/opt/homebrew/bin/cadical'): raise ValueError('unexpected solver path')
        if kind == 'checker' and p != str(LANE/'tools/drat-trim/drat-trim'): raise ValueError('unexpected checker path')
        actual = digest(p)
        observed[kind] = {'path':p,'expected_sha256':h,'observed_sha256':actual,'matches':actual == h}
    return observed


def full_gate(lease,phase,lane=LANE,providers=None):
    """Last operation before every admission. Expensive census refresh precedes final fresh guards/hash checks."""
    p,errors = providers or {},[]
    accounting,rss,binaries,count,free,required = None,{'known':False},{},None,None,None
    try:
        accounting = p['census']() if 'census' in p else census_for_gate(lease['census_reference'],bool(lease.get('force_census_refresh')),lane)
        lease['census_reference'] = accounting['reference']
        lease['force_census_refresh'] = False
        bound = lease['whole_plan_remaining_bound_bytes']
        if type(bound) is not int or bound < ALL_PLANNED_RETAINED_BOUND: errors.append('whole-plan bound missing/narrowed')
        if type(accounting.get('current_data_upper_bytes')) is not int or accounting['current_data_upper_bytes'] < 0: errors.append('unknown allocated-data bytes')
        elif accounting['current_data_upper_bytes']+bound+OTHER_WRITER_MARGIN > DATA_CAP: errors.append('allocated-data cap with whole-plan reservation/margin')
        if not (0 <= accounting['age_seconds'] <= CENSUS_TTL): errors.append('stale/unknown census age')
        rss = p['rss']() if 'rss' in p else lane_rss(lane,os.getpgrp() if phase != 'construct' else None,lease['owner_pid'])
        if not isinstance(rss,dict) or rss.get('known') is not True or type(rss.get('rss_bytes')) is not int or rss['rss_bytes'] < 0:
            errors.append('unknown RSS/headroom')
        else:
            if lease['group_rss_cap_bytes'] != GROUP_RSS_CAP or lease['busy_units'] != 2 or lease['lane_busy_ceiling'] != 4:
                errors.append('wrong normal resource budget')
            current = rss.get('current_group_and_owner_bytes')
            if type(current) is not int or not (0 <= current <= rss['rss_bytes']): errors.append('unknown current-group RSS')
            elif rss['rss_bytes']+max(0,GROUP_RSS_CAP-current)+CONTROL_MARGIN > LANE_CAP: errors.append('RSS headroom')
            members = rss.pop('members',None)
            if members is not None:
                rss['member_count'] = len(members)
                rss['member_set_sha256'] = hashlib.sha256(json.dumps(members,sort_keys=True).encode()).hexdigest()
        # Frozen expected identities survive every capacity wait; compare again immediately before every spawn.
        binaries = p['binaries']() if 'binaries' in p else binary_observations(lease['binary_authority'])
        if set(binaries) != {'python','solver','checker'} or any(v.get('matches') is not True for v in binaries.values()): errors.append('contract binary drift')
        count = p['count']() if 'count' in p else token_count(lane)
        if type(count) is not int or not (0 <= count <= 2): errors.append('COUNT ceiling/format')
        if count == 0 and phase != 'checker': errors.append('new admissions paused')
        if _CANCEL[0]: errors.append('owner cancelled')
        for name in ADMISSION_MARKERS:
            if (Path(lane)/'cycle2'/name).exists(): errors.append('STOP/veto '+name)
        growth = lease['projected_growth_bytes']
        if type(growth) is not int or growth < ITEM_GROWTH: errors.append('unknown/narrow projected retained growth')
        required = BASE_GATE+growth
        free = p['free']() if 'free' in p else (lambda s:s.f_bavail*s.f_frsize)(os.statvfs(lane))
        if type(free) is not int or free < required: errors.append('fresh statvfs growth/floor gate')
        now = p['clock']() if 'clock' in p else time.monotonic()
        allowance = 1450 if phase == 'checker' else 2200
        if now+allowance > lease['chunk_deadline_monotonic'] or now+allowance > lease['item_deadline_monotonic']: errors.append('deadline allowance')
        # Record the age at actual admission, not merely at cache loading before other guards.
        if 'census' not in p:
            accounting['age_seconds'] = time.monotonic()-accounting['finished_monotonic']
            if accounting['age_seconds'] > CENSUS_TTL: errors.append('census expired before admission')
    except (OSError,ValueError,KeyError,TypeError,RuntimeError,AssertionError) as exc:
        errors.append('gate measurement/authority error: '+repr(exc))
    return {'phase':phase,'at_monotonic':time.monotonic(),'count':count,'free_bytes':free,'required_free_bytes':required,
        'rss':rss,'binary_observations':binaries,'census':accounting,'whole_plan_remaining_bound_bytes':lease.get('whole_plan_remaining_bound_bytes'),
        'other_writer_margin_bytes':OTHER_WRITER_MARGIN,'additional_data_cap_bytes':DATA_CAP,'group_rss_cap_bytes':GROUP_RSS_CAP,
        'busy_units':2,'lane_busy_ceiling':4,'projected_growth_bytes':lease.get('projected_growth_bytes'),
        'chunk_deadline_monotonic':lease.get('chunk_deadline_monotonic'),'item_deadline_monotonic':lease.get('item_deadline_monotonic'),
        'next_phase_allowance_seconds':1450 if phase == 'checker' else 2200,'errors':errors,'admitted':not errors}


class Capacity:
    """One normal token. NO automatic tier2 path. Every stop requires a complete receipt/parent decision."""
    def __init__(self,deadline,lane=LANE,metadata=False,wait_allowance=2550):
        self.lane,self.deadline,self.metadata,self.wait_allowance = Path(lane),deadline,metadata,wait_allowance
        self.fds,self.safe,self.record,self.children = [],True,None,[]
        self.settlement = None

    def __enter__(self):
        started = time.monotonic()
        try:
            while not self.fds:
                if _CANCEL[0] or time.monotonic()+self.wait_allowance > self.deadline: raise RuntimeError('capacity wait deadline/cancellation')
                n = token_count(self.lane)
                if n == 0: raise RuntimeError('COUNT0; no new admission')
                for i in range(n):
                    fd = os.open(self.lane/'cycle2/tokens'/('t%d' % i),os.O_RDWR)
                    try: fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
                    except BlockingIOError:
                        os.close(fd); continue
                    self.fds.append(fd)
                    os.ftruncate(fd,0)
                    os.write(fd,('%d %.3f supervised-v3\n' % (os.getpid(),time.time())).encode())
                    break
                if not self.fds: time.sleep(0.1)
            self.wait_seconds = time.monotonic()-started
            return self
        except BaseException:
            self._release(); raise

    def supervise(self,command,name,lease,record,quarantine):
        assert not self.metadata and len(self.fds) == 1
        s = supervisor()
        lease['force_census_refresh'] = bool(lease.get('force_census_refresh') or self.wait_seconds > CENSUS_TTL)
        gate = full_gate(lease,'worker',self.lane)
        if not gate['admitted']: return None,gate
        self.safe = False
        try:
            rec = s.supervise(command,name,2400,GROUP_RSS_CAP,FLOOR,str(self.lane),str(record),str(quarantine),
                              grace=60,owner_child=self.children)
            self.record = rec
            self._settle(rec)
            return rec,gate
        except BaseException:
            if self.record is None:
                self._freeze('supervisor raised without an ownership record')
                while True: time.sleep(1)
            self._settle(self.record)
            raise

    def _freeze(self,why):
        try:
            with (self.lane/'cycle2/tokens/COUNT').open('w') as f: f.write('0\n')
        except BaseException: pass
        try:
            with (self.lane/'cycle2/m2k3-QUARANTINE.flag').open('x') as f:
                json.dump({'status':'UNKNOWN','reason':why,'owner_pid':os.getpid()},f)
        except BaseException: pass

    def _live(self,s,leader,observed):
        live = s.live_members(leader,s.probe,observed)
        for text,ident in observed.items():
            state,_,current = s.probe(int(text))
            if state == 'unknown' or state == 'alive' and (not ident.get('start') or current.get('start') == ident.get('start')):
                live.append({'pid':int(text),'state':state})
        return live

    def _settle(self,rec):
        s = supervisor()
        if rec.get('leader_pid') is None and not self.children:
            self.safe = True
            self.settlement = {'no_child_started':True,'group_quiescent':True,'leader_reaped':True}
            return
        if len(self.children) != 1 or self.children[0].pid != rec.get('leader_pid'):
            self._freeze('owned Popen handle unavailable/mismatched; do not guess reaping')
            while True: time.sleep(1)
        child,leader = self.children[0],rec['leader_pid']
        observed = dict(rec.get('observed_identities') or {})
        stop = rec.get('stop') or {}
        if rec.get('uncertain') or rec.get('quarantine_record') or rec.get('cleanup_exception') or stop.get('survivors') or stop.get('killpg_error'):
            self._freeze('nonclean group cleanup; retain token through explicit leader wait and group quiescence')
        polls = 0
        while True:
            try:
                live = self._live(s,leader,observed)
                child.poll(); polls += 1
                if not live and child.returncode is not None:
                    returncode = child.wait()  # exact retained Popen, also for leaders exiting AFTER the grace
                    after = self._live(s,leader,observed)
                    if not after:
                        self.settlement = {'group_quiescent':True,'leader_reaped':True,'owned_leader_pid':leader,
                            'leader_returncode':returncode,'explicit_owned_popen_wait':True,'poll_calls':polls,
                            'post_reap_quiescence_monotonic':time.monotonic()}
                        self.safe = True
                        return
            except BaseException: self._freeze('settlement probe/reap failed; token stays held')
            time.sleep(0.25)

    def _release(self):
        for fd in reversed(self.fds):
            fcntl.flock(fd,fcntl.LOCK_UN); os.close(fd)
        self.fds = []

    def __exit__(self,*exc):
        if not self.safe:
            self._freeze('owner exit before known quiescence/reaping')
            if self.record is None:
                while True: time.sleep(1)
            self._settle(self.record)
        self._release()
