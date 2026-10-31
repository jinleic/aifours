#!/usr/bin/env python3
"""Ensure equality binding detects changed module even at equal shape."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
HELP=ROOT/'frontier-20261028-d4-physical-equality-source-check.py'
EXPECT='077737ece6d3953daee00187ef4ea203046d97aab59d0dd86211b72e87f94e6f'
OUT=ROOT/'frontier-20261028-d4-equality-compression-fault-check-results.json'
if hashlib.sha256(HELP.read_bytes()).hexdigest()!=EXPECT:raise ValueError('helper changed')
spec=importlib.util.spec_from_file_location('eq_binding',HELP)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
g,pkg,corr=m.load();parts=copy.deepcopy(pkg['eq_groups']['abb']['parts'])
origkeys=list(parts[1]['local'][3][4]);old=origkeys[0]
oldmat=pkg['aux'][old];shape=(len(oldmat),len(oldmat[0]))
fault_pkg=copy.deepcopy(pkg);alt='__in_memory_same_shape_fault__'
fake=[list(row) for row in oldmat];fake[0][0]+=1
fault_pkg['aux'][alt]=fake
parts[1]['local']=[list(s) for s in parts[1]['local']]
newkeys=list(parts[1]['local'][3][4]);newkeys[0]=alt;parts[1]['local'][3][4]=newkeys
try:m.validate_group(fault_pkg,'abb',parts)
except ValueError as e:detected='different actual compression modules' in str(e);reason=str(e)
else:detected=False;reason='no error'
r={'kind':'same_shape_equality_compression_guard_fault_control',
   'original_module':old,'substituted_synthetic_module':alt,'shared_matrix_shape':list(shape),
   'detected':detected,'reported_reason':reason,
   'scope':'In-memory module-key mismatch only; same matrix shape is not sufficient to assert same compression. This guard detection is not a physical counterexample.',
   'verdict':'PASS' if detected else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if detected else 1)
