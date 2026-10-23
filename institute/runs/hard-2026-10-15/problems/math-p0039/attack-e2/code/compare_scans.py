#!/usr/bin/env python3
"""Compare block aggregates AND full arithmetic at shared recorded indices.

This imports only an evidence checker. Neither producing scanner is imported
or executed. Shared residues and actual factors are compared entrywise, then
recomputed independently. This still checks only recorded subsets, not every
decision in either full scan.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from check import metadata, need, read_lines, check_record, sieve_primes


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--c-prefix', default='logs/main')
    p.add_argument('--python-prefix', default='logs/python-main')
    p.add_argument('--running', action='store_true')
    p.add_argument('--c-records')
    p.add_argument('--python-records')
    p.add_argument('--output')
    args = p.parse_args()
    hc, bc, sc = metadata(args.c_prefix, allow_partial=True, running=args.running)
    hp, bp, sp = metadata(args.python_prefix, allow_partial=True, running=args.running)
    need((hc['start'], hc['step'], hc['sieve_bound']) ==
         (hp['start'], hp['step'], hp['sieve_bound']), 'different arithmetic/sieve classes')
    need(hc['block_size'] % hp['block_size'] == 0, 'incommensurate blocks')
    ratio = hc['block_size']//hp['block_size']
    common = min(len(bc), len(bp)//ratio)
    for i in range(common):
        group = bp[i*ratio:(i+1)*ratio]
        need(group[0]['start'] == bc[i]['start'] and group[-1]['end'] == bc[i]['end'], 'different block endpoints')
        for key in ('count', 'sieved', 'tested', 'hits'):
            need(sum(b[key] for b in group) == bc[i][key], 'aggregate '+key+' mismatch at C block '+str(i))
        need([n for b in group for n in b['survivors']] == bc[i]['survivors'], 'survivor disagreement')
    def records_by_index(path, limit):
        records = {}
        for row in read_lines(path, partial_lines=args.running):
            if row['index'] < limit:
                need(row['index'] not in records, 'duplicate arithmetic record')
                records[row['index']] = row
        return records
    c_records = records_by_index(args.c_records or args.c_prefix+'.records.jsonl', sc['class_count'])
    python_records = records_by_index(args.python_records or args.python_prefix+'.records.jsonl', sp['class_count'])
    shared = sorted(c_records.keys() & python_records.keys())
    need(shared, 'no shared arithmetic records')
    primes = sieve_primes(hc['sieve_bound'])
    digest = hashlib.sha256()
    factor_records = unsieved_records = 0
    for index in shared:
        c, py = c_records[index], python_records[index]
        expected_n = hc['start'] + hc['step']*index
        need(c['n'] == py['n'] == expected_n, 'shared n mismatch')
        for key in ('decision', 'factor'):
            need(c[key] == py[key], 'shared '+key+' mismatch at n='+str(expected_n))
        for key in ('p', 'residue'):
            need(int(c[key]) == int(py[key]), 'shared full '+key+' mismatch at n='+str(expected_n))
        # This recomputes the complete power and actual smallest factor with
        # a checker that imports neither scanner, not just producer agreement.
        canonical = check_record(c, hc['sieve_bound'], primes)
        digest.update(canonical.encode())
        if c['factor']:
            factor_records += 1
        else:
            unsieved_records += 1
    result = dict(compared_c_blocks=common, python_blocks_per_c_block=ratio,
                  common_start=hc['start'],
                  common_end=hc['start']+hc['step']*hc['block_size']*common,
                  c_scan_end=sc['end'], python_scan_end=sp['end'],
                  python_class_members=sp['class_count'],
                  shared_arithmetic_records=len(shared), shared_factor_records=factor_records,
                  shared_unsieved_records=unsieved_records,
                  shared_records_sha256=digest.hexdigest(),
                  shared_min_n=c_records[shared[0]]['n'], shared_max_n=c_records[shared[-1]]['n'],
                  limitation='Block totals agree as bookkeeping. Full residues and actual sieve divisors agree and were recomputed ONLY at the shared recorded indices. No independent exhaustive main-range certification.')
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(text)
    print(text, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, AssertionError, IndexError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
