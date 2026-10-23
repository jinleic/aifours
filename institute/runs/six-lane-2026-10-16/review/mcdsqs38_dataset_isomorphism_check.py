"""Parent check of the priority finding that the pinned mcDSQS(38) block set is isomorphic to
record 143 (1-based) of Kiermaier-Krcadinac-Wassermann's SQS(38) dataset, Zenodo 10.5281/zenodo.17153238,
file 3-38-4-1.des.gz. Uses the explicit point map reported by the audit; does not search for maps.
Usage: DATASET.des.gz NEW_OUTPUT_DIR
"""
from datetime import datetime
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
CERT = HERE / 'mcdsqs38-parent-inputs-v1/mcdsqs38_g342_s0.txt'
CERT_SHA = '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'
DATASET_SHA = '715ab56db350e4eade13b3f1b84df9a0108f4f2670dc41115adafcbcdda17b25'
RECORD = 143
N = 38


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def records(raw_text):
    """Split the GAP list into record bodies at each 'rec(' token, in file order (1-based)."""
    starts = [m.start() for m in re.finditer(r'rec\(', raw_text)]
    return [raw_text[s:e] for s, e in zip(starts, starts[1:] + [len(raw_text)])]


def blocks_of(record_text):
    m = re.search(r'blocks\s*:=\s*\[(.*?)\]\s*\]', record_text, re.S)
    if m is None:
        raise ValueError('blocks field not found')
    found = re.findall(r'\[\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\]', m.group(0))
    return [tuple(int(x) for x in b) for b in found]


def generators_of(record_text):
    m = re.search(r'autGroup\s*:=\s*Group\(\s*\[(.*?)\]\s*\)', record_text, re.S)
    if m is None:
        raise ValueError('autGroup field not found')
    gens = []
    for gen_text in re.split(r',\s*(?=\()', m.group(1).strip()):
        perm = list(range(N + 1))
        for cyc in re.findall(r'\(([^()]*)\)', gen_text):
            pts = [int(x) for x in cyc.replace('\n', ' ').split(',')]
            for a, b in zip(pts, pts[1:] + pts[:1]):
                perm[a] = b
        gens.append(tuple(perm[1:]))
    return gens


def closure(gens):
    ident = tuple(range(1, N + 1))
    group, frontier = {ident}, [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                gh = tuple(h[g[i] - 1] for i in range(N))
                if gh not in group:
                    group.add(gh)
                    nxt.append(gh)
        frontier = nxt
    return group


def cert_blocks():
    raw = CERT.read_bytes()
    if sha_bytes(raw) != CERT_SHA:
        raise ValueError('certificate SHA mismatch')
    lines = [l for l in raw.decode('ascii').split('\n') if l and not l.startswith('#')]
    start = lines.index('BLOCKS') + 1
    return {frozenset(map(int, l.split())) for l in lines[start:start + 2109]}


def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: DATASET.des.gz NEW_OUTPUT_DIR')
    data_path, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(exist_ok=False)
    raw_gz = data_path.read_bytes()
    result = {'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'status': 'FAILED',
              'driver_sha256': sha_bytes(Path(__file__).read_bytes()), 'dataset_sha256': sha_bytes(raw_gz),
              'dataset_doi': '10.5281/zenodo.17153238', 'record_one_based': RECORD}
    try:
        if result['dataset_sha256'] != DATASET_SHA:
            raise ValueError('dataset SHA mismatch')
        text = gzip.decompress(raw_gz).decode('latin1')
        recs = records(text)
        result['record_count'] = len(recs)
        rec = recs[RECORD - 1]
        dblocks = blocks_of(rec)
        if len(dblocks) != 2109 or len(set(map(frozenset, dblocks))) != 2109:
            raise ValueError('record does not list 2109 distinct blocks')
        triples = {}
        for b in dblocks:
            for t in itertools.combinations(sorted(b), 3):
                triples[t] = triples.get(t, 0) + 1
        result['record_is_sqs38'] = len(triples) == 8436 and set(triples.values()) == {1}
        point_map = {i: (i - 1) if i % 2 == 1 else (21 - i) % N for i in range(1, N + 1)}
        result['map_is_bijection'] = sorted(point_map.values()) == list(range(N))
        image = {frozenset(point_map[p] for p in b) for b in dblocks}
        result['mapped_record_equals_certificate_block_set'] = image == cert_blocks()
        gens = generators_of(rec)
        group = closure(gens)
        result['listed_autGroup_generators'] = len(gens)
        result['listed_autGroup_order_by_closure'] = len(group)
        dset = set(map(frozenset, dblocks))
        result['listed_generators_preserve_record'] = all(
            {frozenset(g[p - 1] for p in b) for b in dset} == dset for g in gens)
        (out / 'record143.txt').write_text(rec, encoding='latin1')
        result['extracted_record_sha256'] = sha_bytes((out / 'record143.txt').read_bytes())
        ok = (result['record_is_sqs38'] and result['map_is_bijection'] and
              result['mapped_record_equals_certificate_block_set'] and result['listed_generators_preserve_record'])
        result['status'] = 'PARENT_ISOMORPHISM_TO_PUBLISHED_RECORD_CONFIRMED' if ok else 'MISMATCH'
        result['scope'] = ('Confirms only that the published SQS(38) record maps onto the certificate block set. '
                           'The listed group order is computed from the dataset generators; that it is the full '
                           'automorphism group is the dataset authors\' claim. No colouring claim exists in the record.')
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
        with (out / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
        print(json.dumps(result, indent=2))
    return 0 if result['status'].endswith('CONFIRMED') else 1


if __name__ == '__main__':
    raise SystemExit(main())
