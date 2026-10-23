#!/usr/bin/env python3
"""Build explicit beta-pattern implications to existing DRAT-certified anchors.
Usage: crt3_equivalence_cert_c21v1.py OUTDIR [SECONDS=300]
Never runs a SAT solver, imports the Gaussian program, or claims unrestricted
nonexistence. See frozen README ADD-13 for the DM-validity-preserving operations.
The chosen row/column permutations, Z21 unit multiplier, and mod7 row constants
are the certificate; the affine parameter formula is producer-only convenience.
A separate table-level program must verify them and the actual proof anchors.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
STOP = False
LOGS = ('runs/crt3-direct-prefix-v2/cases.jsonl', 'runs/crt3-direct-rest-v2/cases.jsonl',
        'runs/crt3-direct-tail-v2/cases.jsonl', 'runs/crt3-direct-retry-v3/cases/cases.jsonl')


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def term(signum, frame):
    global STOP
    STOP = True


def quad(index):
    out = [0] * 4
    for k in range(3, -1, -1):
        index, out[k] = divmod(index, 7)
    if index:
        raise ValueError('index out of range')
    return out


def number(cs):
    z = 0
    for x in cs:
        z = 7 * z + x
    return z


def beta(cs):
    u1, v1, u2, v2 = cs
    U, V = (0, u1, u2), (0, v1, v2)
    return [[(i * c + U[t] * (i * i - i) + V[t] * (i ** 3 - i)) % 7
             for t in range(3) for c in range(7)] for i in range(7)]


def load():
    base, anchors, logmeta = {}, {}, []
    for j, rel in enumerate(LOGS):
        path = ROOT / rel
        logmeta.append({'path': rel, 'sha256': sha(path)})
        seen = set()
        for line in path.read_text().splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            index = rec['index']
            if index in seen or not 0 <= index < 2401 or rec['coefficients'] != quad(index):
                raise AssertionError('duplicate/index/coefficient mismatch')
            seen.add(index)
            if j < 3:
                if index in base:
                    raise AssertionError('overlapping original ranges')
                base[index] = rec
            elif index not in base or base[index]['status'] == 'DRAT-VERIFIED-UNSAT' or rec['cnf_sha256'] != base[index]['cnf_sha256']:
                raise AssertionError('retry was not an unchanged unresolved original')
            if rec['status'] == 'DRAT-VERIFIED-UNSAT':
                if rec['planted_control'] or (rec['n'], rec['k'], rec['q']) != (21, 7, 7) or rec['checker']['rc'] != 0:
                    raise AssertionError('invalid anchor metadata')
                case = path.parent / ('case-%04d' % index)
                anchors[index] = {'index': index, 'coefficients': quad(index),
                                  'case_dir': str(case.relative_to(ROOT)),
                                  'cnf_sha256': rec['cnf_sha256'], 'proof_sha256': rec['proof_sha256'],
                                  'proof_bytes': rec['proof_bytes'],
                                  'receipt_sha256': sha(case / 'receipt.json'),
                                  'checker_output_sha256': rec['checker']['stdout_sha256']}
    if set(base) != set(range(2401)):
        raise AssertionError('original case logs do not cover2401 exactly once')
    return base, anchors, logmeta


def select_anchors(anchors):
    """Small existing proof subset; correctness does not rely on orbit labels."""
    remaining, selected, partition = set(range(2401)), {}, []
    for seed in range(2401):
        if seed not in remaining:
            continue
        u1, v1, u2, v2 = quad(seed)
        U, V, orbit = (0, u1, u2), (0, v1, v2), set()
        for s in itertools.permutations(range(3)):
            du = [(U[s[t]] - U[s[0]]) % 7 for t in (1, 2)]
            dv = [(V[s[t]] - V[s[0]]) % 7 for t in (1, 2)]
            for a in range(1, 7):
                for b in range(7):
                    for l in range(1, 7):
                        cs = [l * a * a * (du[t] + 3 * b * dv[t]) % 7 if f == 0
                              else l * a ** 3 * dv[t] % 7 for t in (0, 1) for f in (0, 1)]
                        orbit.add(number(cs))
        if not orbit <= remaining:
            raise AssertionError('producer orbit partition overlaps')
        available = orbit & anchors.keys()
        best = min(available, key=lambda i: (anchors[i]['proof_bytes'], i)) if available else None
        if best is not None:
            selected[best] = anchors[best]
        partition.append({'seed': seed, 'size': len(orbit), 'anchor_index': best})
        remaining.difference_update(orbit)
    if remaining:
        raise AssertionError('producer orbit partition incomplete')
    return selected, partition


def find(index, anchors):
    u1, v1, u2, v2 = quad(index)
    U, V = (0, u1, u2), (0, v1, v2)
    src = beta(quad(index))
    for s in itertools.permutations(range(3)):
        dU = [(U[s[t]] - U[s[0]]) % 7 for t in range(3)]
        dV = [(V[s[t]] - V[s[0]]) % 7 for t in range(3)]
        for a in range(1, 7):
            for b in range(7):
                for l in range(1, 7):
                    cs = [l * a * a * (dU[t] + 3 * b * dV[t]) % 7 if f == 0
                          else l * a ** 3 * dV[t] % 7 for t in (1, 2) for f in (0, 1)]
                    target = number(cs)
                    if target not in anchors:
                        continue
                    L = next(x for x in range(1, 21) if x % 7 == l and x % 3 == 1)
                    rp = [(a * i + b) % 7 for i in range(7)]
                    scale = l * a % 7
                    qU = l * (2 * a * b - a + a * a) % 7
                    qV = l * (3 * a * b * b - a + 3 * a * a * b + a ** 3) % 7
                    cp = [7 * s[t] + (pow(scale, -1, 7) * (c - qU * dU[t] - qV * dV[t])) % 7
                          for t in range(3) for c in range(7)]
                    constants = [L * (src[rp[i]][cp[0]] - src[rp[0]][cp[0]]) % 7 for i in range(7)]
                    return {'source_index': index, 'target_index': target,
                            'source_coefficients': quad(index), 'target_coefficients': cs,
                            'row_permutation': rp, 'column_permutation': cp, 'unit_mod21': L,
                            'row_constants_mod7': constants,
                            'full_DM_operation': 'Dprime[i,c]=L*(D[rp[i],cp[c]]-D[rp[0],cp[c]]-D[rp[i],cp[0]]+D[rp[0],cp[0]]) mod21',
                            'producer_parameters': {'a': a, 'b': b, 'l': l, 'blocks': list(s)},
                            'anchor': anchors[target]}
    return None


def main():
    out = Path(sys.argv[1])
    seconds = float(sys.argv[2]) if len(sys.argv) > 2 else 300.0
    if not 0 < seconds <= 300:
        raise ValueError('preparation bound must be0..300s')
    os.mkdir(out)
    signal.signal(signal.SIGTERM, term)
    signal.signal(signal.SIGINT, term)
    begin = time.monotonic()
    base, anchors, logmeta = load()
    unresolved = sorted(set(base) - set(anchors))
    selected, partition = select_anchors(anchors)
    certificates, missing = [], []
    for index in range(2401):
        if STOP or time.monotonic() - begin >= seconds:
            missing.extend(range(index, 2401))
            break
        rec = find(index, selected)
        if rec is None:
            missing.append(index)
        else:
            certificates.append(rec)
    manifest = {'clock': stamp(), 'producer_sha256': sha(__file__), 'input_logs': logmeta,
                'family': 'all2401 common-slope polynomial23 beta patterns, not all CFR6,21',
                'direct_certified_count': len(anchors), 'direct_certified_indices': sorted(anchors),
                'selected_anchor_count': len(selected), 'producer_orbit_partition': partition,
                'residual_count': len(unresolved), 'certificates': certificates, 'missing_indices': missing,
                'wall_s': time.monotonic() - begin,
                'status': 'READY-FOR-INDEPENDENT-TABLE-AUDIT' if not missing else 'UNKNOWN-INCOMPLETE',
                'signal': STOP}
    with open(out / 'manifest.json', 'x') as f:
        json.dump(manifest, f, indent=1)
    print(json.dumps({k: v for k, v in manifest.items() if k not in ('certificates', 'direct_certified_indices')}), flush=True)


if __name__ == '__main__':
    main()
