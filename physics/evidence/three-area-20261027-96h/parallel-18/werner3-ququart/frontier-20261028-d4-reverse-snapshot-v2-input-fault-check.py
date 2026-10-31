#!/usr/bin/env python3
"""Exercise v2 snapshot guards using in-memory byte alterations only."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
V2=ROOT/'frontier-20261028-d4-reverse-snapshot-crt-v2.py'
PIN='425e5d827f1f4a9592732a124b5f791ebef90148c114084696131c81b9d7f971'
OUT=ROOT/'frontier-20261028-d4-reverse-snapshot-v2-input-fault-check-results.json'
if hashlib.sha256(V2.read_bytes()).hexdigest()!=PIN:raise ValueError('v2 source mismatch')
spec=importlib.util.spec_from_file_location('snapshot_v2_fault_controls',V2)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
original=Path.read_bytes

def reject_modified_bytes(target,call,reason):
    def patched(self):
        raw=original(self)
        return raw+b'\x00' if self==target else raw
    Path.read_bytes=patched
    try:
        try:call()
        except ValueError as e:return reason in str(e)
        return False
    finally:Path.read_bytes=original

# First verify both helpers can load from their actual checked snapshots.
loader=m.load('snapshot_test_loader',m.G);base=m.load('snapshot_test_base',m.BASE)
checks={
  'base_helper_tamper_rejected':reject_modified_bytes(m.BASE,lambda:m.load('tampered_base',m.BASE),'snapshot hash mismatch'),
  'global_helper_tamper_rejected':reject_modified_bytes(m.G,lambda:m.load('tampered_global',m.G),'snapshot hash mismatch'),
  'prime_receipt_tamper_rejected':reject_modified_bytes(m.R,lambda:m.snapshot(m.R),'snapshot hash mismatch'),
  'source_archive_tamper_rejected':reject_modified_bytes(loader.ARCHIVE,lambda:m.load_data_snapshot(loader,base),'archive snapshot mismatch'),
  'corrected_data_tamper_rejected':reject_modified_bytes(loader.CORRECTED,lambda:m.load_data_snapshot(loader,base),'corrected snapshot mismatch'),
}
if Path.read_bytes is not original:raise ValueError('read method not restored')
if any(hashlib.sha256(original(k)).hexdigest()!=v for k,v in m.PINS.items()):raise ValueError('actual helper bytes changed')
r={'kind':'snapshot_crt_v2_in_memory_input_tamper_guards','successor_sha256':PIN,
   'controls':checks,'actual_helper_hashes_unchanged':True,
   'method':'Override Path.read_bytes in this process only to append one byte to each target in turn; require the corresponding source snapshot guard to reject before using those bytes. Restore the method each time and verify actual helper hashes.',
   'scope':'Input-binding guard sensitivity only; not the 424-prime identity, physical theorem, no-runtime-trust proof, model-family or formal review. No real file is modified.',
   'verdict':'PASS' if all(checks.values()) else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
