"""Parent regeneration of PA19 A2 skeleton lists and their independent-generator bijections.
One child process at a time; existing research venv is read-only (-B). Every output directory is fresh.
No CNFs, proofs or solvers. Includes independent atlas-extension check of the486 balanced graphs.
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INP = HERE / 'inputs'
SRC = INP / 'src'
PY = '/Users/jinleic/.local/state/research-explorer/venv/bin/python'
OUT = HERE / 'generators-v1'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def invoke(label, argv):
    with open(OUT / (label + '.stdout'), 'xb') as so, open(OUT / (label + '.stderr'), 'xb') as se:
        r = subprocess.run(argv, cwd=SRC, stdout=so, stderr=se, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    if r.returncode:
        raise ValueError('Generator replay failed: %s rc%d' % (label, r.returncode))


def main():
    OUT.mkdir(exist_ok=False)
    da, db = OUT / 'a', OUT / 'b'
    da.mkdir(); db.mkdir()
    rec = {'started': now(), 'python': PY, 'rows': [], 'driver_sha256': sha(Path(__file__))}
    v = subprocess.run([PY, '-B', '-c', 'import sys,networkx;print(sys.version);print(networkx.__version__)'],
                       capture_output=True, text=True)
    if v.returncode:
        raise ValueError('Existing venv unavailable')
    rec['versions'] = v.stdout.strip()
    # The helper independently extends every atlas7 graph by an eighth vertex and matches all486 classes.
    atlasout = OUT / 'balanced-atlas.json'
    invoke('balanced-atlas', [PY, '-B', str(SRC / 'graphs_check.py'),
                             str(INP / 'data/quadgraphs-8v-13to16e-D4.g6'), str(atlasout)])
    atlas = json.loads(atlasout.read_text())
    rec['balanced_atlas'] = atlas
    if not atlas['bijection'] or atlas['atlas_classes'] != 486:
        raise ValueError('Independent balanced graph enumeration failed')
    for mi in range(1, 10):
        astr = 'skeletons-ms%02d.json' % mi
        bstr = 'skeletons-b-ms%02d.json' % mi
        invoke('a-ms%02d' % mi, [PY, '-B', str(SRC / 'gen_skel.py'), str(mi), str(da)])
        invoke('b-ms%02d' % mi, [PY, '-B', str(SRC / 'gen_skel_b.py'), str(mi), str(db)])
        comp = OUT / ('compare-map-ms%02d.json' % mi)
        invoke('compare-ms%02d' % mi, [PY, '-B', str(SRC / 'compare_skel.py'), str(mi), str(da), str(db), str(comp)])
        olda = INP / 'skeletons' / astr
        oldb = INP / 'cycle2/skel-b' / bstr
        oldmap = INP / ('cycle2/skel-b/compare-map-ms%02d.json' % mi)
        J = json.loads(comp.read_text())
        row = {'multiset': mi, 'count_a': J['count_a'], 'count_b': J['count_b'], 'bijection': J['bijection'],
               'a_sha256': sha(da / astr), 'pinned_a_sha256': sha(olda),
               'b_sha256': sha(db / bstr), 'pinned_b_sha256': sha(oldb),
               'mapping_sha256': sha(comp), 'pinned_mapping_sha256': sha(oldmap)}
        row['a_equal'] = row['a_sha256'] == row['pinned_a_sha256']
        row['b_equal'] = row['b_sha256'] == row['pinned_b_sha256']
        row['mapping_equal'] = row['mapping_sha256'] == row['pinned_mapping_sha256']
        row['verdict'] = 'PASS' if row['bijection'] and row['a_equal'] and row['b_equal'] and row['mapping_equal'] else 'FAIL'
        rec['rows'].append(row)
        with open(OUT / ('row-ms%02d.json' % mi), 'x') as f:
            json.dump(row, f, indent=1)
            f.write('\n')
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if all(r['verdict'] == 'PASS' for r in rec['rows']) and len(rec['rows']) == 9 else 'FAIL'
    with open(HERE / 'generator-replay-result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({'verdict': rec['verdict'], 'started': rec['started'], 'ended': rec['ended'],
                      'rows': [{k: r[k] for k in ('multiset', 'count_a', 'count_b', 'a_equal', 'b_equal', 'mapping_equal', 'verdict')}
                               for r in rec['rows']]}))
    sys.exit(0 if rec['verdict'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
