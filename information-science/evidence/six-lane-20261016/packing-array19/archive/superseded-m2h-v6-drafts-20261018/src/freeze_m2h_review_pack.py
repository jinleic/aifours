#!/usr/bin/env python3
"""Creation-only M2H review pack: production v6 owner/worker/evidence/runtime/contract module UNCHANGED (all v6 pack
hashes re-verified); three new M2H files shown in full, as /dev/null diffs, and as an informative diff of the M2H
runner against the reviewed M6 v6 adapter it generalizes. Binds the frozen M2H contract. Metadata only.
"""
import argparse
import difflib
import json
import os
import time
from pathlib import Path

import m2_ms09_contract_v6 as C
import m2_supervised_runtime_v6 as R

L = C.LANE
V6 = L/'cycle2/full-k1-v6-sourcepack-20261018T075617.json'
V6_SHA = 'cb9d45ab26a7b39ee960d70f4b28ffe4483d6add3bb6900d6fcc27cdc6a74bc3'
NEW = ('src/freeze_m2h_v6.py','src/run_m2h_v6.py','src/final_m2h_inventory_v6.py')


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); args = ap.parse_args()
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+2*1024**2
        assert R.digest(V6) == V6_SHA
        pack6 = json.loads(V6.read_bytes())
        for rel,item in pack6['source_files'].items(): assert R.digest(L/rel) == item['sha256'], ('production v6 source changed',rel)
        contract = json.loads(Path(args.contract).read_bytes())
        for rel in NEW: assert contract['source_sha256'][rel] == R.digest(L/rel)
        sources = {rel:{'sha256':R.digest(L/rel),'content':(L/rel).read_text()} for rel in NEW}
        stamp = time.strftime('%Y%m%dT%H%M%S')
        pieces = []
        for rel in NEW: pieces.extend(difflib.unified_diff([],sources[rel]['content'].splitlines(True),fromfile='/dev/null',tofile='m2h/'+rel))
        exact = L/'cycle2'/('m2h-v6-new-files-delta-%s.diff' % stamp)
        with exact.open('x') as f: f.write(''.join(pieces))
        base = pack6['source_files']['src/run_m2_ms06_direct_v6.py']['content']
        informative = L/'cycle2'/('m2h-v6-runner-vs-m6-adapter-%s.diff' % stamp)
        with informative.open('x') as f:
            f.write(''.join(difflib.unified_diff(base.splitlines(True),sources['src/run_m2h_v6.py']['content'].splitlines(True),
                fromfile='v6/src/run_m2_ms06_direct_v6.py',tofile='m2h/src/run_m2h_v6.py')))
        pack = {'schema':'PA19-M2H-REVIEW-PACK-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR PARENT REVIEW; M2H native HOLD until GO','production_v6_pack':{'path':str(V6.relative_to(L)),'sha256':V6_SHA,'unchanged_reverified':True},
            'contract':{'path':str(Path(args.contract).resolve().relative_to(L)),'sha256':R.digest(args.contract),'items':len(contract['items']),
                'cases_direct':contract['cases_direct'],'cases_split':contract['cases_split'],'split_intervals':contract['split_intervals'],
                'excluded_cases':len(contract['excluded_cases']),'recorded_old_transport_service_hours':contract['recorded_old_transport_service_hours']},
            'new_sources':sources,'deltas':{'new_files_exact':{'path':str(exact.relative_to(L)),'sha256':R.digest(exact)},
                'runner_vs_m6_adapter_informative':{'path':str(informative.relative_to(L)),'sha256':R.digest(informative)}},
            'scope':'A2 ms01..ms08 historical checked-UNSAT cases; ms09 in M9; E0 excluded until reviewed encode_q0b worker mode',
            'generator_sha256':R.digest(__file__)}
        dest = L/'cycle2'/('m2h-v6-review-pack-%s.json' % stamp)
        with dest.open('x') as f: json.dump(pack,f,indent=1)
        print(dest,R.digest(dest),flush=True); print(json.dumps({'contract':pack['contract'],'deltas':pack['deltas']},indent=1),flush=True)


if __name__ == '__main__':
    main()
