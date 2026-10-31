#!/usr/bin/env python3
"""In-memory source-compression scaling controls for stdlib local maxima."""
import copy
import hashlib
import importlib.util
import io
import json
import lzma
import tarfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
HELP=ROOT/'frontier-20261028-d4-reverse-stdlib-local-maxima-check.py'
PIN='02c358a3d92a52fa290bcb58fadc05a0618a78f3e40586cb372f7a60b37efa69'
OUT=ROOT/'frontier-20261028-d4-reverse-stdlib-local-maxima-fault-check-results.json'
if hashlib.sha256(HELP.read_bytes()).hexdigest()!=PIN:raise ValueError('helper mismatch')
spec=importlib.util.spec_from_file_location('standalone_maps',HELP)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
if m.sha(m.ARCH)!=m.PIN_ARCH:raise ValueError('archive mismatch')
with tarfile.open(m.ARCH,mode='r:gz') as tf:raw=tf.extractfile(m.MEMBER).read()
if hashlib.sha256(raw).hexdigest()!=m.PIN_MEMBER:raise ValueError('member mismatch')
pkg=m.SafeData(io.BytesIO(lzma.decompress(raw,memlimit=256*1024*1024))).load()
site=None
for t in pkg['types']:
    for a in t['rows']:
        for b in t['rows']:
            _,kp,lp=m.reverse_rule(a,b)
            for mod in t['modules'][:3]:
                v=max(map(abs,m.site_values(pkg,mod,kp,lp)),default=0)
                if v:site=(mod,kp,lp,v);break
            if site:break
        if site:break
    if site:break
if site is None:raise ValueError('no nonzero actual site map')
mod,kp,lp,baseline=site;_,cut,_=mod.split('|');cut=tuple(map(int,cut.split(','))) if cut else ()
fault_site=copy.deepcopy(pkg);key=(4,cut);lab=m.label(mod);keys,C=fault_site['diagrams'][key][lab]
fault_site['diagrams'][key][lab]=(keys,[[257*x for x in row] for row in C])
site_fault=max(map(abs,m.site_values(fault_site,mod,kp,lp)))
eq=None
for group in pkg['eq_groups'].values():
    for part in group['parts']:
        for s in part['local']:
            if s[0]!='S':continue
            for mk in s[4]:
                v=max(map(abs,m.equality_values(pkg,s,mk)),default=0)
                if v:eq=(s,mk,v);break
            if eq:break
        if eq:break
    if eq:break
if eq is None:raise ValueError('no nonzero actual equality map')
s,mk,eqbaseline=eq;fault_eq=copy.deepcopy(pkg);lab=m.label(mk);keys,C=fault_eq['diagrams'][(3,())][lab]
fault_eq['diagrams'][(3,())][lab]=(keys,[[25*x for x in row] for row in C])
eq_fault=max(map(abs,m.equality_values(fault_eq,s,mk)))
ok=site_fault>256 and eq_fault>24
r={'kind':'stdlib_local_maxima_in_memory_compression_fault_controls',
   'helper_sha256':PIN,'site_original_max':baseline,'site_scaled_max':site_fault,'site_guard_256_rejected':site_fault>256,
   'equality_original_max':eqbaseline,'equality_scaled_max':eq_fault,'equality_guard_24_rejected':eq_fault>24,
   'method':'Scale two actual source compression matrices in separate in-memory package copies and re-enumerate their literal maps. No archive/data bytes are changed.',
   'scope':'Source-map scanner sensitivity only; no original physical state, q3 counterexample, full identity, formal kernel or model-family review.',
   'verdict':'PASS' if ok else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if ok else 1)
