#!/usr/bin/env python3
"""Read-only binding check of every first-column list consumed by the GPS-1|C1 and GPS-2|C1 probes against the lane's
frozen list authorities (requested by the parent 2026-10-18 ~14:2x). Metadata only: JSON reads and SHA-256; one lane
metadata token; fresh statvfs admission recorded; creation-only receipt cycle2/gps-list-binding-<stamp>.json.
Authorities:
  ms09: M9 contract cycle2/m2-ms09-k1-v6-contract-20261018T075542.json (per-case list path/sha256/n/raw/aut) whose
        phase file is cycle2/ms09-batch-denominators-v2-20261018T015110.json (complete list counts/hashes pinned
        before any remaining batch solve);
  ms06 b68/b73: cycle2/ms06-two-batch-denominators-20261018T024846.json (list sha256, exact raw/orbit denominators,
        complete-denominator pin file).
For every consumed list: on-disk SHA == probe-receipt SHA == authority SHA, n == authority n, and (ms06) the
complete-denominator pin file exists with its recorded SHA. Completeness itself is the authority's claim; this
check establishes only that the probes consumed exactly the authority-bound lists.
Usage: gps_list_binding_check_v1.py
"""
import hashlib
import json
import os
import time
from pathlib import Path

import m2_supervised_runtime_v6_3 as R

L = Path(__file__).resolve().parents[1]
PROBES = {'gps1c1':('cycle2/gps1c1-probe-20261018T140808.json','d82ddf381c34348b1c4ae8b7a6956f8a6a6f0650c6ee947dd30e24beb0cc961d'),
          'gps2c1':('cycle2/gps2c1-ms06-probe-20261018T141048.json','12b4320e3acdfd119516a505518357c9bd647f1ec5b19755196a0cf752b8bf57')}
M9 = ('cycle2/m2-ms09-k1-v6-contract-20261018T075542.json','072a6172c9cb71ab8110effb24e26eba66b5239594df4300d58c9797b1ec14a8')
PHASE9 = ('cycle2/ms09-batch-denominators-v2-20261018T015110.json','d0d0d7fa9dae6ab263b05af800c0967916adf840c7583613d98c15d41d810d33')
PHASE6 = ('cycle2/ms06-two-batch-denominators-20261018T024846.json','fc5b86191bb977f7f08fa1996a2011f9f086be6bcce954887146a3035476f83c')


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    for p,h in list(PROBES.values())+[M9,PHASE9,PHASE6]: assert digest(L/p) == h, ('pinned file changed',p)
    m9 = json.loads((L/M9[0]).read_bytes()); assert m9['phase_path'] == PHASE9[0] and m9['phase_sha256'] == PHASE9[1]
    by9 = {c['b_index']:c for c in m9['cases']}
    p6 = {int(c['job'].split(':')[1]):c for c in json.loads((L/PHASE6[0]).read_bytes())['cases']}
    rows,bad = [],[]
    c1 = json.loads((L/PROBES['gps1c1'][0]).read_bytes()); c2 = json.loads((L/PROBES['gps2c1'][0]).read_bytes())
    consumed = [('gps1c1','ms09',x) for x in c1['cases']['ms09']]+[('gps1c1','ms06',x) for x in c1['cases']['ms06']]+[('gps2c1','ms06',x) for x in c2['cases']]
    for probe,ms,x in consumed:
        disk = digest(L/x['list']); e = json.loads((L/x['list']).read_bytes())
        row = {'probe':probe,'case':'%s_b%05d' % (ms,x['b_index']),'list':x['list'],'disk_sha256':disk,'probe_sha256':x['list_sha256'],
               'n':e['num_placements'],'raw':e.get('raw_class_assignments'),'aut':e.get('automorphisms')}
        if ms == 'ms09':
            a = by9.get(x['b_index']); lst = (a or {}).get('list') or {}
            row.update(authority=M9[0],authority_sha256=lst.get('sha256'),authority_n=lst.get('n'),authority_raw=lst.get('raw'),authority_aut=lst.get('aut'),
                       ok=bool(a) and lst.get('path') == x['list'] and disk == x['list_sha256'] == lst.get('sha256') and e['num_placements'] == lst.get('n')
                          and lst.get('raw') == e.get('raw_class_assignments') and lst.get('aut') == e.get('automorphisms'))
        else:
            a = p6.get(x['b_index']) or {}; pin = a.get('complete_pin') or {}
            pin_ok = bool(pin) and (L/pin['path']).exists() and digest(L/pin['path']) == pin['sha256']
            row.update(authority=PHASE6[0],authority_sha256=a.get('list_sha256'),authority_n=a.get('exact_complete_orbit_denominator'),
                       authority_raw=a.get('exact_raw_assignment_denominator'),authority_aut=a.get('automorphisms'),complete_pin=pin,complete_pin_ok=pin_ok,
                       ok=a.get('list_path') == x['list'] and disk == x['list_sha256'] == a.get('list_sha256') and e['num_placements'] == a.get('exact_complete_orbit_denominator')
                          and a.get('exact_raw_assignment_denominator') == e.get('raw_class_assignments') and pin_ok)
        rows.append(row)
        if not row['ok']: bad.append(row['case']+' ('+probe+')')
    s = os.statvfs(L)
    out = {'schema':'PA19-GPS-LIST-BINDING-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'source_sha256':digest(__file__),'pinned':{p:h for p,h in list(PROBES.values())+[M9,PHASE9,PHASE6]},
           'consumed_lists':len(rows),'all_bound':not bad,'unbound':bad,'rows':rows,
           'admission':{'free_bytes_at_finish':s.f_bavail*s.f_frsize,'projected_growth_bytes':'<1 MiB (this receipt)'},
           'scope':'binding of consumed lists to the frozen list authorities only; list completeness is the authorities\' claim; no solver'}
    dest = L/'cycle2'/('gps-list-binding-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f: json.dump(out,f,indent=1); f.write('\n')
    print(dest,digest(dest),'consumed',len(rows),'all_bound',not bad,bad[:10],flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); free = s.f_bavail*s.f_frsize
        assert free >= R.BASE_GATE+16*1024**2, ('fresh admission refused',free)
        print('admission free',free,flush=True)
        main()
