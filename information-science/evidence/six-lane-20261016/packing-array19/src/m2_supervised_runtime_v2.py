#!/usr/bin/env python3
"""Outer ownership/admission for PA19 v2. Uses the parent-reviewed M7 supervise_r3 public API unchanged.
No /bin/ps or other helper is spawned by this module. RSS selection uses same-euid argv through Darwin sysctl and
strict libproc probes; no argv/environment contents are logged. Setuid helpers are forbidden inside native groups.
Tier1 owns one token at a3.5GiB sampled group threshold; tier2 owns ALL existing token flocks plus bigmem at7GiB.
Every owned flock is retained through exceptional/quarantine cleanup until known quiescence. These are sampled
RSS/SIGTERM guards, NOT kernel instantaneous hard caps. Fresh lane headroom/free gates and COUNT<=2 remain required.
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
import re
import time
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
SUP_PATH = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py')
SUP_SHA = '0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d'
BASE_GATE = 12334217728
FLOOR = 12000000000
LANE_CAP = 8*1024**3
GROUP_CAPS = {1:3584*1024**2,2:7*1024**3}
CONTROL_MARGIN = 128*1024**2
DATA_CAP = 10000000000
ITEM_ORDINARY_BOUND = 384*1024
ITEM_GROWTH = 64*1024**2  # per-item worst halting diagnostic retention, no CNF/proof copies
ROUTE_FAILURE_RESERVE = 2*ITEM_GROWTH  # two already admitted tier1 pipelines may diagnose concurrently
ALL_PLANNED_RETAINED_BOUND = 2*(5009+106+1119)*ITEM_ORDINARY_BOUND+ROUTE_FAILURE_RESERVE
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


def full_gate(lease,phase,lane=LANE,providers=None):
    p = providers or {}
    errors = []
    try:
        count = p['count']() if 'count' in p else token_count(lane)
        if type(count) is not int or count > 2 or count < 0:
            errors.append('COUNT ceiling/format')
        if count == 0 and phase != 'checker':
            errors.append('new item/solver admissions paused')
        if _CANCEL[0]: errors.append('owner cancelled')
        for name in ('STOP-hard12','STOP-m2r12','STOP-K1','m2k1-SAT.flag','m2k1-INVALID.flag','m2k1-HALT.flag','m2k1-QUARANTINE.flag'):
            if (Path(lane)/'cycle2'/name).exists(): errors.append('STOP/veto '+name)
        free = p['free']() if 'free' in p else (lambda s:s.f_bavail*s.f_frsize)(os.statvfs(lane))
        growth = lease['projected_growth_bytes']
        if type(growth) is not int or growth <= 0: errors.append('unknown/nonpositive projected growth')
        required = BASE_GATE+growth
        if type(free) is not int or free < required: errors.append('fresh growth/floor gate')
        accounting = lease['accounting_envelope']
        if not isinstance(accounting,dict) or accounting.get('known') is not True or type(accounting.get('upper_bytes')) is not int or not (0 <= accounting['upper_bytes'] <= DATA_CAP):
            errors.append('unknown/excess additional-data accounting')
        rss = p['rss']() if 'rss' in p else lane_rss(lane,os.getpgrp() if phase != 'item' else None,lease['owner_pid'])
        if not isinstance(rss,dict) or rss.get('known') is not True or type(rss.get('rss_bytes')) is not int or rss['rss_bytes'] < 0:
            errors.append('unknown RSS/headroom')
        else:
            assert type(lease['tier']) is int and lease['tier'] in (1,2), 'invalid tier'
            assert type(lease['group_rss_cap_bytes']) is int and lease['group_rss_cap_bytes'] == GROUP_CAPS[lease['tier']], 'wrong tier RSS threshold'
            assert lease['busy_units'] == 2 and lease['lane_busy_ceiling'] == 4, 'wrong busy budget'
            if lease['tier'] == 2:
                assert lease['exclusive_bigmem'] is True and lease['held_token_indices'] == list(range(8)), 'tier2 not exclusive'
            else:
                assert lease['exclusive_bigmem'] is False and len(lease['held_token_indices']) == 1, 'tier1 token missing'
            assert type(rss.get('current_group_and_owner_bytes')) is int and 0 <= rss['current_group_and_owner_bytes'] <= rss['rss_bytes'], 'unknown current group RSS'
            reserve = max(0,lease['group_rss_cap_bytes']-rss.get('current_group_and_owner_bytes',0))
            if rss['rss_bytes']+reserve+CONTROL_MARGIN > LANE_CAP: errors.append('RSS headroom')
            if isinstance(rss.get('members'),list):
                members = rss.pop('members')
                rss['member_count'] = len(members)
                rss['member_set_sha256'] = hashlib.sha256(json.dumps(members,sort_keys=True).encode()).hexdigest()
        now = p['clock']() if 'clock' in p else time.monotonic()
        allowance = 1450 if phase == 'checker' else 2200
        if now+allowance > lease['chunk_deadline_monotonic'] or now+allowance > lease['item_deadline_monotonic']:
            errors.append('deadline allowance')
    except (OSError,ValueError,KeyError,TypeError,RuntimeError,AssertionError) as exc:
        errors.append('gate measurement/accounting error: '+repr(exc))
        count,free,required,rss = None,None,None,{'known':False}
    return {'phase':phase,'at_monotonic':time.monotonic(),'count':count,'free_bytes':free,'required_free_bytes':required,
            'rss':rss,'projected_growth_bytes':lease.get('projected_growth_bytes'),
            'accounting_envelope':lease.get('accounting_envelope'),'group_rss_cap_bytes':lease.get('group_rss_cap_bytes'),
            'tier':lease.get('tier'),'busy_units':lease.get('busy_units'),'lane_busy_ceiling':lease.get('lane_busy_ceiling'),
            'exclusive_bigmem':lease.get('exclusive_bigmem'),'held_token_indices':lease.get('held_token_indices'),
            'chunk_deadline_monotonic':lease.get('chunk_deadline_monotonic'),'item_deadline_monotonic':lease.get('item_deadline_monotonic'),
            'next_phase_allowance_seconds':1450 if phase == 'checker' else 2200,'control_margin_bytes':CONTROL_MARGIN,
            'errors':errors,'admitted':not errors}


class Capacity:
    def __init__(self,deadline,lane=LANE,tier=1,metadata=False,wait_allowance=2550):
        assert tier in (1,2) and not (metadata and tier != 1)
        self.lane,self.deadline,self.fds,self.safe = Path(lane),deadline,[],True
        self.record,self.tier,self.metadata,self.wait_allowance = None,tier,metadata,wait_allowance
        self.token_indices = []

    def _waiting_gate(self):
        if _CANCEL[0] or time.monotonic()+self.wait_allowance > self.deadline:
            raise RuntimeError('capacity wait deadline/cancellation')
        if token_count(self.lane) == 0: raise RuntimeError('COUNT0; no new admission')

    def _hold(self,path,index=None):
        fd = os.open(path,os.O_RDWR)
        try:
            while True:
                self._waiting_gate()
                try:
                    fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
                    self.fds.append(fd)
                    if index is not None:
                        self.token_indices.append(index)
                        os.ftruncate(fd,0)
                        os.write(fd,('%d %.3f supervised-v2-tier%d\n' % (os.getpid(),time.time(),self.tier)).encode())
                    return
                except BlockingIOError: time.sleep(0.1)
        except BaseException:
            if fd not in self.fds: os.close(fd)
            raise

    def __enter__(self):
        root = self.lane/'cycle2'/'tokens'
        try:
            if self.tier == 2:
                # Same order for every exclusive owner: never hold token1 while waiting for token0.
                # All8 legacy token files are held, not merely the currently visible COUNT.
                for i in range(8): self._hold(root/('t%d' % i),i)
                self._hold(root/'bigmem')
            else:
                while not self.fds:
                    self._waiting_gate()
                    for i in range(token_count(self.lane)):
                        fd = os.open(root/('t%d' % i),os.O_RDWR)
                        try: fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
                        except BlockingIOError:
                            os.close(fd)
                            continue
                        self.fds.append(fd)
                        self.token_indices.append(i)
                        os.ftruncate(fd,0)
                        os.write(fd,('%d %.3f supervised-v2-tier1\n' % (os.getpid(),time.time())).encode())
                        break
                    if not self.fds: time.sleep(0.1)
            return self
        except BaseException:
            self._release()
            raise

    def supervise(self,command,name,lease,record,quarantine):
        assert not self.metadata and lease['tier'] == self.tier
        assert self.token_indices == lease['held_token_indices']
        assert len(self.fds) == (9 if self.tier == 2 else 1), 'incomplete tier ownership'
        sup = supervisor()
        gate = full_gate(lease,'item',self.lane)
        if not gate['admitted']: return None,gate
        self.safe = False  # every exceptional return retains ownership until known group quiescence
        try:
            rec = sup.supervise(command,name,2400,lease['group_rss_cap_bytes'],FLOOR,str(self.lane),
                                str(record),str(quarantine),grace=60)
            self.record = rec
            self._settle(rec)
            return rec,gate
        except BaseException:
            if self.record is None:
                self._freeze('supervisor raised without a returned ownership record')
                while True: time.sleep(1)
            self._settle(self.record)
            raise

    def _freeze(self,why):
        try:
            with (self.lane/'cycle2'/'tokens'/'COUNT').open('w') as f: f.write('0\n')
        except BaseException: pass
        try:
            with (self.lane/'cycle2'/'m2k1-QUARANTINE.flag').open('x') as f:
                json.dump({'status':'UNKNOWN','reason':why,'owner_pid':os.getpid(),'tier':self.tier},f)
        except BaseException: pass  # receipt I/O failure NEVER releases capacity

    def _settle(self,rec):
        sup,leader = supervisor(),rec.get('leader_pid')
        if leader is None:
            self.safe = True  # reviewed API did not reach Popen
            return
        if rec.get('uncertain') or rec.get('quarantine_record') or rec.get('cleanup_exception') or (rec.get('stop') or {}).get('survivors'):
            self._freeze('returned quarantine/uncertainty; retain capacity until known quiescent')
        observed = dict(rec.get('observed_identities') or {})
        while True:
            try:
                live = sup.live_members(leader,sup.probe,observed)
                for text,ident in observed.items():
                    pid = int(text)
                    state,_,current = sup.probe(pid)
                    if state == 'unknown': live.append({'pid':pid,'state':'unknown'})
                    elif state == 'alive' and (not ident.get('start') or current.get('start') == ident.get('start')):
                        live.append({'pid':pid,'state':'alive'})
                if not live:
                    self.safe = True
                    return
            except BaseException: self._freeze('quiescence probe failed; capacity stays held')
            time.sleep(0.25)

    def _release(self):
        for fd in reversed(self.fds):
            fcntl.flock(fd,fcntl.LOCK_UN)
            os.close(fd)
        self.fds = []

    def __exit__(self,*exc):
        if not self.safe:
            self._freeze('owner exit attempted before quiescence')
            if self.record is None:
                while True: time.sleep(1)
            self._settle(self.record)
        self._release()


def rss_only_stop(rec,tier,native=None):
    """A recorded sole-RSS stop, no uncertainty/anomaly, with known-quiescent cleanup; never a certificate."""
    if type(tier) is not int or tier not in (1,2) or not isinstance(rec,dict): return False
    match = re.fullmatch(r'aggregate RSS ([0-9]+) above ([0-9]+)(?: at completion)?',str(rec.get('trip_reason')))
    if not match or int(match[1]) <= int(match[2]) or int(match[2]) != GROUP_CAPS[tier]: return False
    if rec.get('uncertain') is not False or any(rec.get(k) for k in ('exception','cleanup_exception','quarantine_record','quarantine_write_error','record_write_error','stop_error')): return False
    stop = rec.get('stop') or {}
    if stop.get('listing_ok') is not True or stop.get('survivors') != [] or stop.get('kill_error'): return False
    if native:
        checker = native.get('checker_collector') or {}
        if native.get('status') in ('SAT','INVALID') or any('NOT VERIFIED' in str(v) for v in checker.get('status_lines',[])): return False
        if any(native.get(k) for k in ('construction_error','input_integrity_error','proof_integrity_error','resource_refusal','proof_cap_hit')): return False
    return True


def rss_only_retry(rec,tier,native=None):
    return tier == 1 and rss_only_stop(rec,tier,native)
