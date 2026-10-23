#!/usr/bin/env python3
"""Fast structural replay of the final recorded computational claim.

This verifier checks gap-free coverage, all per-block counts, the survivor table,
the declared audit subset, and provenance. It does NOT recompute every main-range
modular power. Use check.py records for all recorded arithmetic samples, or
replay.py for a slow complete independent range reexecution.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

# The checker is a separate arbitrary-precision implementation, not producing C.
from check import metadata, need, schema_validate


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result', default='evidence/result.json')
    args = parser.parse_args()
    result = json.loads(Path(args.result).read_text())
    header, blocks, summary = metadata('logs/main', expected_start=200000000000,
                                       expected_step=24, allow_partial=True)
    need(header['start'] % 24 == 8 and summary['end'] % 24 == 8, 'wrong congruence class')
    need(summary['end'] == result['end'], 'claimed endpoint mismatch')
    need(result['headline_resolved'] is False and result['outcome'] == 'partial', 'overstated outcome')
    need(result['conditional_on_imported_premises'] is True, 'premises not declared')
    for key in ('start', 'end', 'step', 'class_count', 'block_count', 'sieved', 'tested', 'survivors'):
        need(summary[key] == result['production'][key], 'production summary mismatch: '+key)
    need(header['sieve_bound'] == 1000000, 'unexpected sieve bound')
    need(header['threads'] <= 4 and header['cap_seconds'] <= 9000, 'resource/cap mismatch')
    need(summary['seconds'] <= header['cap_seconds'] + max(b['seconds'] for b in blocks) + 5,
         'wall time beyond cap plus final in-flight blocks')
    audit = json.loads(Path('evidence/main.audit.json').read_text())
    for key in ('start', 'end', 'step', 'class_count', 'block_count', 'sieved', 'tested', 'survivors'):
        need(audit[key] == summary[key], 'audit summary mismatch: '+key)
    need(result['recorded_arithmetic_audit_count'] == audit['audit_records'], 'arithmetic audit subset count')
    need(result['recorded_arithmetic_audit_sha256'] == audit['audit_sha256'], 'arithmetic audit digest')
    # Re-hash exactly the stored canonical records. Their arithmetic is rechecked
    # separately by check.py records, not silently assumed to cover all n.
    records = [json.loads(s) for s in Path('logs/main.records.jsonl').read_text().splitlines()]
    records.sort(key=lambda r: r['index'])
    digest = hashlib.sha256()
    for r in records:
        digest.update(('%d\t%s\t%d\t%d\n' %
                       (r['n'], r['decision'], r['factor'], int(r['residue']))).encode())
    need(len(records) == audit['audit_records'] and digest.hexdigest() == audit['audit_sha256'],
         'stored audit record integrity')
    build = json.loads(Path('evidence/build.json').read_text())
    need(sha('code/scan.c') == build['source_sha256'], 'production source changed')
    need(sha('code/scan') == build['binary_sha256'], 'production binary changed')
    need(sha('selection-inputs/literature/thas-zagier-2008.reader.md') == build['reader_sha256'],
         'staged premise text changed')
    independent_plan = json.loads(Path('evidence/independent-plan.json').read_text())
    need(sha('code/independent_scan.py') == independent_plan['source_sha256'], 'independent source changed')
    _, _, independent = metadata('logs/python-main', expected_start=200000000000,
                                  expected_step=24, allow_partial=True)
    need(independent == result['independent_contiguous_python_prefix'], 'independent prefix summary changed')
    need(not independent['survivors'] and independent['end'] < summary['end'], 'independent prefix scope')
    subprocess.run([sys.executable, 'code/compare_scans.py'], check=True)
    subprocess.run([sys.executable, 'code/check_survivors.py'], check=True)
    schema_validate(json.loads(Path('claims.json').read_text()), json.loads(Path('claims.schema.json').read_text()))
    print(json.dumps(dict(verified_structural_interval=[summary['start'], summary['end']],
                          class_count=summary['class_count'], audited_records=audit['audit_records'],
                          conclusion='One recorded production computation with declared subset checks; no independent exhaustive main-range certification and no all-orders solution.'), indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, AssertionError, IndexError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
