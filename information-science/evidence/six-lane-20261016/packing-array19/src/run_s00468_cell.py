#!/usr/bin/env python3
"""Parent-approved exact six-unit cover of ms06_s00468 (zero-based cell row8,column6). The pinned encode_skel
CNF is unchanged except its DIMACS clause count is increased by one and exactly one unit x[8,6,s] is appended,
s=0..5. Base SHA 137407b6532fea61a682467507462e146cef6dd546b9a496a6bd18ad0ceba994. Each base is regenerated under
the token, byte-compared to the pinned file (variable mapping bound), then the pinned clause body is used verbatim.
No solver/helper/resource/acceptance change: stream_check13.kissat_staged, 300s solve/1200s check, unchanged caps.
Every symbol subcase must be checked before the original case counts; a miss leaves it UNKNOWN; no deeper split.
Outputs cycle2/cell-cover/ms06_s00468/r08_c06/s00.json..s05.json, never overwritten. A SAT candidate is preserved and
verified by run_hard13.handle_sat and stops the run. Production stop file STOP-hard12, normal COUNT<=2 tokens.
"""
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel
import run_hard13
import stream_check13 as S

LANE = os.path.dirname(HERE)
TAG = 'ms06_s00468'
ROW, COL = 8, 6
BASE_SHA = '137407b6532fea61a682467507462e146cef6dd546b9a496a6bd18ad0ceba994'
OUT = os.path.join(LANE, 'cycle2', 'cell-cover', TAG, 'r08_c06')


def main():
    S.install_sigterm_handler()
    S.set_stop_files([os.path.join(LANE, 'cycle2', 'STOP-hard12')])
    spec = json.load(open(os.path.join(LANE, 'cases19skel', 'specs', TAG + '.json')))
    p1 = json.load(open(os.path.join(LANE, 'cases19skel', 'results', TAG + '.json')))
    assert p1['cnf_sha256'] == BASE_SHA and spec['N'] == 19 and spec['k'] == 8 and spec['q'] == 6
    os.makedirs(OUT, exist_ok=True)
    outcomes = []
    for symbol in range(6):
        dest = os.path.join(OUT, 's%02d.json' % symbol)
        if os.path.exists(dest):
            r = json.load(open(dest))
        else:
            hold = {}

            def build():
                pinned = open(os.path.join(LANE, p1['cnf']), 'rb').read()
                assert hashlib.sha256(pinned).hexdigest() == BASE_SHA
                F, X, _ = encode_skel.build(spec)
                regenerated = S.cnf_bytes_of(F)
                assert regenerated == pinned  # binds the cell variable mapping to the exact pinned bytes
                head, sep, body = pinned.partition(b'\n')
                assert sep and pinned.endswith(b'\n')
                p, cnf, nv, nc = head.split()
                assert (p, cnf) == (b'p', b'cnf')
                literal = X[ROW][COL][symbol]
                assert literal == 1 + (ROW * 8 + COL) * 6 + symbol
                unit = ('%d 0\n' % literal).encode()
                sub = ('p cnf %d %d\n' % (int(nv), int(nc) + 1)).encode() + body + unit
                hold.update({'X': X, 'literal': literal, 'body_sha256': hashlib.sha256(body).hexdigest(),
                             'base_bytes': len(pinned), 'base_header': head.decode(), 'unit_clause': unit.decode(),
                             'base_byte_identical': True, 'exact_one_unit_append': True})
                return sub

            try:
                r = S.kissat_staged(build, os.path.join(LANE, 'scratch', 'fifo', 'cell_s00468_s%02d' % symbol), 300, 1200)
            except (S.AdmissionDenied, SystemExit) as exc:
                S.write_json(os.path.join(OUT, 'deferred-s%02d-%d.json' % (symbol, time.time_ns())),
                             {'tag': TAG, 'symbol': symbol, 'status': 'UNKNOWN', 'reason': repr(exc), 'base_cnf_sha256': BASE_SHA})
                return
            r.update({'tag': TAG, 'row': ROW, 'column': COL, 'symbol': symbol, 'base_cnf_sha256': BASE_SHA,
                      'unit_literal': hold['literal'], 'base_body_sha256': hold['body_sha256'], 'base_bytes': hold['base_bytes'],
                      'base_header': hold['base_header'], 'unit_clause': hold['unit_clause'],
                      'base_byte_identical': hold['base_byte_identical'], 'exact_one_unit_append': hold['exact_one_unit_append'],
                      'encoder': 'encode_skel.py + exactly one cell unit', 'runner': 'run_s00468_cell.py'})
            if r.get('status') == 'SAT':
                run_hard13.handle_sat('cell_s00468_s%02d' % symbol, r, hold['X'], spec)
                if r.get('model_file'):
                    r['model_sha256'] = hashlib.sha256(open(os.path.join(LANE, r['model_file']), 'rb').read()).hexdigest()
            r['solver_out'] = ''
            S.write_json(dest, r)
        outcomes.append({'symbol': symbol, 'status': r.get('status'), 'checked': r.get('checked')})
        print(json.dumps({k: r.get(k) for k in ('tag', 'symbol', 'unit_literal', 'status', 'checked', 'solve_seconds',
                                               'check_seconds', 'proof_cap_hit', 'cnf_sha256', 'model_sha256')}), flush=True)
        if r.get('status') == 'SAT' or S.ABORT[0]:
            return
    summary = {'tag': TAG, 'row': ROW, 'column': COL, 'base_cnf_sha256': BASE_SHA, 'subcases': outcomes,
               'all_six_checked': len(outcomes) == 6 and all(r['status'] == 'UNSAT' and r['checked'] for r in outcomes)}
    path = os.path.join(OUT, 'summary-%d.json' % time.time_ns())
    S.write_json(path, summary)
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
