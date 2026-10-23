#!/usr/bin/env python3
"""Requested exact original M2 LEGACY5 counts/total-CNF-bytes, metadata ONLY, one existing token inline.
No helper/solver/checker child. Original flags are screened by the explicit historical gate; parent formula binding
is reported separately as required, not fabricated. The output is NOT a final global acceptance inventory.
"""
import hashlib
import json
import re
import time
from collections import Counter
from pathlib import Path

import m2_legacy5_evidence as LEGACY
import stream_check15 as TOKEN

L = Path(__file__).resolve().parent.parent


def main():
    TOKEN.install_sigterm_handler()
    TOKEN.set_stop_files([str(L/'cycle2'/'STOP-aux')])
    if TOKEN.token_count() not in (1,2):
        raise SystemExit('one existing COUNT<=2 metadata token required')
    with TOKEN.Token(stage='legacy5-count-metadata-no-children'):
        assert TOKEN.token_count() in (1,2)
        files = set((L/'cycle2'/'m2skel_drat').glob('ms*_b*.json'))
        files.update((L/'cycle2'/'m2part_drat').glob('ms*_b*/batch_*.json'))
        files.update((L/'m2q0c'/'results').glob('g*.json'))
        rows,hist,groups,issues,sats = [],Counter(),{},[],[]
        for p in sorted(files):
            raw = p.read_bytes()
            r = json.loads(raw)
            assert isinstance(r,dict), ('nonobject result',str(p))
            rev = r.get('stream_check_revision')
            hist[str(rev)] += 1
            if type(rev) is not int or rev != 5:
                continue
            rel = str(p.relative_to(L))
            ident = {}
            if p.parent.name == 'results' and p.parent.parent.name == 'm2q0c':
                index = int(p.stem[1:])
                group,case = 'm2q0c_E0','E0:g%03d' % index
                ident = {'graph_index':index,'encoder':'encode_q0b.py'}
            else:
                m = re.fullmatch(r'ms(\d{2})_b(\d{5})',p.stem if p.parent.name == 'm2skel_drat' else p.parent.name)
                assert m, ('unexpected legacy record name',rel)
                mi,bi = map(int,m.groups())
                group,case = 'ms%02d' % mi,'ms%02d:b%05d' % (mi,bi)
                ident = {'multiset':mi,'b_index':bi}
                if p.parent.name != 'm2skel_drat':
                    bm = re.fullmatch(r'batch_(\d+)_(\d+)(?:_exact|_r3)?\.json',p.name)
                    assert bm, ('untyped legacy batch name',rel)
                    ident['indices'] = [int(bm.group(1)),int(bm.group(2))]
            errors = LEGACY.gate_errors(r,ident)
            n = r.get('cnf_bytes')
            if type(n) is not int or n <= 0:
                issues.append({'record':rel,'error':'missing/invalid CNF byte count'})
                continue
            if r.get('status') == 'SAT': sats.append({'record':rel,'sha256':hashlib.sha256(raw).hexdigest()})
            g = groups.setdefault(group,{'records':0,'original_gate_pass_records':0,'cnf_bytes_all':0,'cnf_bytes_original_gate_pass':0,
                                        'cases_all':set(),'cases_original_gate_pass':set()})
            g['records'] += 1; g['cnf_bytes_all'] += n; g['cases_all'].add(case)
            if not errors:
                g['original_gate_pass_records'] += 1; g['cnf_bytes_original_gate_pass'] += n; g['cases_original_gate_pass'].add(case)
            rows.append({'record':rel,'record_sha256':hashlib.sha256(raw).hexdigest(),'case':case,'class':group,
                         'cnf_sha256':r['cnf_sha256'],'cnf_bytes':n,'original_gate_pass':not errors,'errors':errors,
                         'not_retained':LEGACY.NOT_RETAINED,'parent_formula_binding':'REQUIRED, separate parent method=M2 BYTE_EQUAL manifest'})
        for g in groups.values():
            g['unique_cases_all'] = len(g.pop('cases_all'))
            g['unique_cases_original_gate_pass'] = len(g.pop('cases_original_gate_pass'))
        def total(names):
            return {k:sum(groups.get(n,{}).get(k,0) for n in names) for k in ('records','original_gate_pass_records','cnf_bytes_all','cnf_bytes_original_gate_pass')}
        out = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'schema':'PA19-M2-LEGACY5-COUNTS-v1','scope':'original independent M2 receipts only; M1 replay/exposure is separate; no final acceptance',
               'by_class':groups,'ms01':total(['ms01']),'other_ms':total(['ms%02d' % n for n in range(2,10)]),
               'm2q0c_E0':total(['m2q0c_E0']),'all_legacy5':total(list(groups)), 'all_scanned_revision_histogram':dict(hist),
               'issues':issues,'SAT_veto':sats,'records':rows,'weaker_than_guard15':True,'original_records_unchanged':True}
        assert not TOKEN.ACTIVE, 'metadata counter must never own a native child'
        dest = L/'cycle2'/('legacy5-counts-'+time.strftime('%Y%m%dT%H%M%S')+'.json')
        with dest.open('x') as f: json.dump(out,f,indent=1)
        print(dest)
        print(json.dumps({k:out[k] for k in ('by_class','ms01','other_ms','m2q0c_E0','all_legacy5','all_scanned_revision_histogram','issues','SAT_veto')},indent=1))


if __name__ == '__main__':
    main()
