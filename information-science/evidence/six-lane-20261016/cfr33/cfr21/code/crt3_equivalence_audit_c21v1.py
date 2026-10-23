#!/usr/bin/env python3
"""Audit explicit DM-validity-preserving beta equivalences and DRAT anchors.
Usage: crt3_equivalence_audit_c21v1.py MANIFEST.json OUTDIR [SECONDS=300]
Does not import the producer, its parameter/group-action formula, or the Gaussian
solver. Checks literal7x21 tables, row/column permutations, Z21 unit and row
normalization. Regenerates only the small selected anchor CNFs with the pinned
independent direct-CNF encoder, hashes their retained proofs/receipts, and checks
existing DRAT output. It does NOT rerun completed SAT/proof-checker processes.
An actual DM lift would transform by row permutation, subtraction of one row
columnwise, common column permutation, row translations and unit multiplication;
all preserve every row-pair difference permutation in cyclic Z21. Hence an
explicit mod7 identity maps ANY hypothetical source lift to an anchor lift.
No claim about CFR row-isotopy or unrestricted CFR6,21 is made.
"""
import copy
import hashlib
import importlib.util
import json
from math import gcd
import os
from pathlib import Path
import signal
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
ENC = ROOT / 'code/crt3_direct_sat_check_c21v3.py'
ENC_SHA = '29f06c10df113eee989f2419d8e84995f570ada13ae711e0b6905670f237de74'
CHECK_SHA = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'
STOP = False


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def term(signum, frame):
    global STOP
    STOP = True


def coefficients(index):
    if type(index) is not int or not 0 <= index < 2401:
        raise ValueError('bad pattern index')
    return [(index // 343) % 7, (index // 49) % 7, (index // 7) % 7, index % 7]


def table(index):
    u1, v1, u2, v2 = coefficients(index)
    answer = []
    for i in range(7):
        row = []
        for block, (u, v) in enumerate(((0, 0), (u1, v1), (u2, v2))):
            offset = i * (i - 1) * (u + v * (i + 1))
            row.extend((i * c + offset) % 7 for c in range(7))
        answer.append(row)
    return answer


def permutation(p, length, label):
    if not isinstance(p, list) or any(type(x) is not int for x in p) or sorted(p) != list(range(length)):
        raise ValueError(label + ' is not a permutation')


def table_identity(cert):
    si, ti = cert['source_index'], cert['target_index']
    src, dst = table(si), table(ti)
    if cert['source_coefficients'] != coefficients(si) or cert['target_coefficients'] != coefficients(ti):
        raise ValueError('coefficient/index mismatch')
    rp, cp = cert['row_permutation'], cert['column_permutation']
    permutation(rp, 7, 'row permutation')
    permutation(cp, 21, 'column permutation')
    multiplier, constants = cert['unit_mod21'], cert['row_constants_mod7']
    if type(multiplier) is not int or not 0 < multiplier < 21 or gcd(multiplier, 21) != 1 or multiplier % 3 != 1:
        raise ValueError('entry multiplier is not the specified Z21 unit')
    if not isinstance(constants, list) or len(constants) != 7 or any(type(x) is not int or not 0 <= x < 7 for x in constants):
        raise ValueError('bad row constants')
    for i in range(7):
        expected = multiplier * (src[rp[i]][cp[0]] - src[rp[0]][cp[0]]) % 7
        if constants[i] != expected:
            raise ValueError('row-constant normalization fails')
        for c in range(21):
            actual = (multiplier * (src[rp[i]][cp[c]] - src[rp[0]][cp[c]]) - constants[i]) % 7
            if actual != dst[i][c]:
                raise ValueError('beta identity fails at row%d,column%d' % (i, c))
    if cert['anchor']['index'] != ti or cert['anchor']['coefficients'] != coefficients(ti):
        raise ValueError('anchor/index mismatch')


def audit_anchor(anchor, out, encoder):
    index = anchor['index']
    case = (ROOT / anchor['case_dir']).resolve()
    if ROOT not in case.parents:
        raise ValueError('anchor path outside lane')
    recpath = case / 'receipt.json'
    if sha(recpath) != anchor['receipt_sha256']:
        raise ValueError('anchor receipt checksum mismatch')
    rec = json.loads(recpath.read_text())
    if rec['status'] != 'DRAT-VERIFIED-UNSAT' or rec['planted_control'] or (rec['n'], rec['k'], rec['q']) != (21, 7, 7):
        raise ValueError('anchor is not an unplanted target-size DRAT UNSAT')
    if rec['solver']['rc'] != 20 or rec['checker']['rc'] != 0:
        raise ValueError('anchor native return codes disagree')
    for field, filename in (('cnf_sha256', 'model.cnf'), ('proof_sha256', 'proof.drat')):
        if sha(case / filename) != anchor[field] or rec[field] != anchor[field]:
            raise ValueError('anchor ' + field + ' checksum mismatch')
    if sha(case / 'checker.out') != rec['checker']['stdout_sha256'] or rec['checker']['stdout_sha256'] != anchor['checker_output_sha256']:
        raise ValueError('anchor checker-output checksum mismatch')
    if not any(line.strip() == 's VERIFIED' for line in (case / 'checker.out').read_text().splitlines()):
        raise ValueError('anchor lacks exact stripped s VERIFIED')
    if sha(rec['checker']['command'][0]) != CHECK_SHA:
        raise ValueError('anchor checker binary pin mismatch')
    st = os.statvfs(ROOT)
    if st.f_bavail * st.f_frsize < 12_000_000_000 + 64 * 1024 ** 2:
        raise ValueError('shared disk-floor margin reached')
    newcnf = out / ('anchor-%04d-regenerated.cnf' % index)
    regenerated, _, _ = encoder.encode(7, table(index), newcnf)
    if regenerated['cnf_sha256'] != anchor['cnf_sha256']:
        raise ValueError('anchor CNF does not encode the stated beta pattern')
    return {'index': index, 'case_dir': anchor['case_dir'], 'receipt_sha256': anchor['receipt_sha256'],
            'cnf_sha256': anchor['cnf_sha256'], 'proof_sha256': anchor['proof_sha256'],
            'checker_output_sha256': anchor['checker_output_sha256'],
            'proof_bytes': (case / 'proof.drat').stat().st_size, 'regenerated_cnf_sha256': regenerated['cnf_sha256']}


def main():
    manifest_path, out = Path(sys.argv[1]), Path(sys.argv[2])
    seconds = float(sys.argv[3]) if len(sys.argv) > 3 else 300.0
    if not 0 < seconds <= 300:
        raise ValueError('audit bound must be0..300s')
    os.mkdir(out)
    signal.signal(signal.SIGTERM, term)
    signal.signal(signal.SIGINT, term)
    begin = time.monotonic()
    manifest = json.loads(manifest_path.read_text())
    if manifest['status'] != 'READY-FOR-INDEPENDENT-TABLE-AUDIT' or manifest['missing_indices']:
        raise ValueError('producer is incomplete')
    for rec in manifest['input_logs']:
        if sha(ROOT / rec['path']) != rec['sha256']:
            raise ValueError('frozen input-log checksum mismatch')
    if sha(ROOT / 'code/crt3_equivalence_cert_c21v1.py') != manifest['producer_sha256']:
        raise ValueError('producer source pin mismatch')
    if sha(ENC) != ENC_SHA:
        raise ValueError('direct encoder source pin mismatch')
    spec = importlib.util.spec_from_file_location('pinned_direct_encoder_for_anchor_audit', ENC)
    encoder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(encoder)
    certs = manifest['certificates']
    if sorted(c['source_index'] for c in certs) != list(range(2401)):
        raise ValueError('certificate sources do not cover2401 exactly once')
    anchors = {}
    for cert in certs:
        if STOP or time.monotonic() - begin >= seconds:
            raise ValueError('audit incomplete under native preparation bound/SIGTERM')
        table_identity(cert)
        index = cert['target_index']
        if index not in anchors:
            anchors[index] = audit_anchor(cert['anchor'], out, encoder)
        elif cert['anchor']['cnf_sha256'] != anchors[index]['cnf_sha256'] or cert['anchor']['proof_sha256'] != anchors[index]['proof_sha256']:
            raise ValueError('conflicting duplicate anchor metadata')
    # This is a valid permutation but deliberately NOT a valid table map.
    # Swapping two nonzero-column images leaves cp[0] and normalization intact.
    corrupt = copy.deepcopy(certs[0])
    corrupt['column_permutation'][1], corrupt['column_permutation'][2] = corrupt['column_permutation'][2], corrupt['column_permutation'][1]
    with open(out / 'invalid-column-map-control.json', 'x') as f:
        json.dump(corrupt, f, indent=1)
    try:
        table_identity(corrupt)
    except ValueError as error:
        if not str(error).startswith('beta identity fails'):
            raise AssertionError('control rejected for an unintended reason: ' + str(error))
        control = {'rejected': True, 'reason': str(error), 'still_a_column_permutation': True,
                   'scope': 'only this table-equivalence verifier control; not another checker mutation suite'}
    else:
        raise AssertionError('invalid column-map control was accepted')
    rec = {'clock': stamp(), 'status': 'VERIFIED-RESTRICTED-FAMILY-BY-DRAT-ANCHORS-AND-EXPLICIT-DM-EQUIVALENCES',
           'scope': 'only2401 common-slope polynomial23 CRT beta patterns, NOT unrestricted CFR6,21',
           'family_patterns': 2401, 'explicit_table_equalities': 2401 * 7 * 21,
           'anchors': list(anchors.values()), 'anchor_count': len(anchors), 'control': control,
           'manifest_sha256': sha(manifest_path), 'audit_source_sha256': sha(__file__),
           'encoder_source_sha256': ENC_SHA, 'checker_sha256': CHECK_SHA,
           'proofs_rechecked_natively_in_this_audit': 0,
           'proof_route': 'previous native DRAT acceptance receipts, hash-pinned proofs/output, exact anchor CNF regeneration; not Lean/kernel verification',
           'wall_s': time.monotonic() - begin}
    with open(out / 'record.json', 'x') as f:
        json.dump(rec, f, indent=1)
    print(json.dumps({k: v for k, v in rec.items() if k != 'anchors'}), flush=True)


if __name__ == '__main__':
    main()
