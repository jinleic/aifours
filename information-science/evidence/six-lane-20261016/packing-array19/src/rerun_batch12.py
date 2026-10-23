#!/usr/bin/env python3
"""Re-run one M1 A3'' batch that remains UNKNOWN, using the unchanged batch CNF and the frozen standard-checker
pipeline with the alternate solver: CaDiCaL binary DRAT, staged through stream_check12.cadical_staged (COUNT<=2,
full predicate, existing caps). Results <batch>_r3.json (the established aggregator rerun suffix), never overwrite.
CNF construction occurs under the stage token and its SHA must equal the original record's CNF SHA. A SAT candidate
is preserved and verified with run_hard12.handle_sat (registered helpers under a token).
Usage: rerun_batch12.py TAG BATCH_STEM SOLVE_LIMIT CHECK_BUDGET
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_partbatch
import run_hard12
import stream_check12 as S

LANE = os.path.dirname(HERE)


def main():
    tag, stem, limit, budget = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
    S.install_sigterm_handler()
    S.set_stop_files([os.path.join(LANE, 'cycle2', 'STOP-hard12')])
    base = os.path.join(LANE, 'cycle2', 'part', tag)
    out = os.path.join(base, stem + '_r3.json')
    if os.path.exists(out):
        print('exists', out)
        return
    original = json.load(open(os.path.join(base, stem + '.json')))
    spec = json.load(open(os.path.join(LANE, 'cases19skel', 'specs', tag + '.json')))
    ext = json.load(open(os.path.join(base, 'ext.json')))
    hold = {}

    def build():
        F, X, _ = encode_partbatch.build(spec, [ext['full'][i] for i in original['indices']])
        hold['X'] = X
        return S.cnf_bytes_of(F)

    r = S.cadical_staged(build, os.path.join(LANE, 'scratch', 'fifo', 'r12_' + tag + '_' + stem), limit, budget)
    r.update({'tag': tag, 'index': stem, 'indices': original['indices'], 'kind': 'partbatch',
              'encoder': 'encode_partbatch.py', 'runner': 'rerun_batch12.py',
              'cnf_matches_original_sha': r['cnf_sha256'] == original['cnf_sha256']})
    if not r['cnf_matches_original_sha']:
        r['checked'] = False
    if r.get('status') == 'SAT':
        run_hard12.handle_sat('rerun12_' + tag + '_' + stem, r, hold['X'], spec)
    r['solver_out'] = ''
    S.write_json(out, r)
    print(json.dumps({k: r.get(k) for k in ('tag', 'index', 'status', 'checked', 'solve_seconds', 'check_seconds',
                                           'cnf_matches_original_sha', 'reader_ok', 'replay_ok')}))


if __name__ == '__main__':
    main()
