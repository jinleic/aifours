#!/usr/bin/env python3
"""Independent, standard-library-only checks of preserved production evidence.

No producing source, executable, or Python module is imported or executed.
Stored block counts check structural coverage, NOT all individual decisions.
Every supplied arithmetic record is recomputed with Python's arbitrary-precision
pow, and its sieve decision is independently checked by trial division.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time

EXPECTED = [2, 8, 24, 90, 512, 134217728, 297474474]


def need(condition, message):
    if not condition:
        raise ValueError(message)


def read_lines(path, partial_lines=False):
    with open(path) as stream:
        rows = []
        for line in stream:
            if partial_lines and not line.endswith('\n'):
                break
            if line.strip():
                rows.append(json.loads(line))
        return rows


def sieve_primes(bound):
    composite = bytearray(bound + 1)
    for q in range(2, math.isqrt(bound) + 1):
        if not composite[q]:
            composite[q*q:bound+1:q] = b'\1' * ((bound - q*q) // q + 1)
    return [q for q in range(2, bound + 1) if not composite[q]]


def smallest_factor(n, bound, primes):
    p = n*n + n + 1
    for q in primes:
        if q > bound or q*q > p:
            break
        if p % q == 0:
            need(1 < q < p, 'factor is not proper')
            return q
    return 0


def metadata(prefix, expected_start=None, expected_stop=None, expected_step=None,
             expected_hits=None, allow_partial=False, running=False, max_blocks=None):
    lines = read_lines(str(prefix) + '.blocks.jsonl', partial_lines=running)
    need(lines and lines[0]['kind'] == 'header', 'missing header')
    header = lines[0]
    if running:
        # A snapshot is explicitly NOT a production completion footer. No
        # synthetic footer is written to disk. Only the unbroken observed
        # prefix is admitted, optionally frozen at a requested block count.
        observed = [b for b in lines[1:] if b['kind'] == 'block']
        observed.sort(key=lambda b: b['id'])
        need(len(observed) == len({b['id'] for b in observed}), 'duplicate observed block')
        blocks = []
        for i, b in enumerate(observed):
            if b['id'] != i:
                break
            blocks.append(b)
        if max_blocks is not None:
            need(0 < max_blocks <= len(blocks), 'requested snapshot boundary not complete')
            blocks = blocks[:max_blocks]
        footer = dict(kind='in-memory-snapshot', assigned_blocks=len(blocks),
                      planned_blocks=header['blocks'], seconds=None,
                      completed_plan=len(blocks) == header['blocks'])
        allow_partial = True
    else:
        need(max_blocks is None, 'max-blocks requires --running')
        need(lines[-1]['kind'] == 'footer', 'missing footer')
        footer = lines[-1]
        blocks = lines[1:-1]
    need(all(b['kind'] == 'block' for b in blocks), 'unexpected block kind')
    blocks.sort(key=lambda b: b['id'])
    a, z, step = header['start'], header['stop'], header['step']
    need(a >= 2 and z > a and step > 0, 'invalid progression')
    if expected_start is not None:
        need(a == expected_start, 'start differs from expected')
    if expected_stop is not None:
        need(z == expected_stop, 'planned stop differs from expected')
    if expected_step is not None:
        need(step == expected_step, 'step differs from expected')
    count = len(range(a, z, step))
    need(header['total'] == count, 'header count mismatch')
    size = header['block_size']
    need(size > 0, 'invalid block size')
    need(header['blocks'] == (count + size - 1) // size, 'planned block count')
    need(footer['planned_blocks'] == header['blocks'], 'footer planned blocks')
    need(footer['assigned_blocks'] == len(blocks), 'footer assigned blocks')
    need(footer['completed_plan'] == (len(blocks) == header['blocks']), 'completion flag')
    if not allow_partial:
        need(footer['completed_plan'], 'run stopped before its planned endpoint')
    previous_end = a
    hits = []
    sieved = tested = covered = 0
    for number, b in enumerate(blocks):
        need(b['id'] == number, 'missing or repeated block ID')
        index = number * size
        length = min(size, count - index)
        need(b['index'] == index and b['count'] == length, 'block arithmetic-class count')
        need(b['start'] == previous_end == a + step*index, 'gap or overlap')
        need(b['end'] == b['start'] + step*length, 'block endpoint')
        need(b['sieved'] >= 0 and b['tested'] >= 0, 'negative counts')
        need(b['sieved'] + b['tested'] == length, 'sieved+tested!=class count')
        if header['sieve_bound'] == 0:
            need(b['sieved'] == 0, 'sieving occurred in unsieved control')
        values = b['survivors']
        need(values == sorted(set(values)), 'survivor order/duplicates')
        need(len(values) == b['hits'] <= b['tested'], 'survivor count')
        for n in values:
            need(b['start'] <= n < b['end'] and (n-a) % step == 0, 'survivor outside block')
            need(pow(2, n+1, n*n+n+1) == 1, 'claimed survivor fails exact power')
        hits.extend(values)
        previous_end = b['end']
        sieved += b['sieved']; tested += b['tested']; covered += length
    if expected_hits is not None:
        need(hits == expected_hits, 'survivors differ from expected list')
    need(covered == len(range(a, previous_end, step)), 'overall count mismatch')
    summary = dict(start=a, end=previous_end, step=step, class_count=covered,
                   block_count=len(blocks), sieved=sieved, tested=tested,
                   survivors=hits, seconds=footer['seconds'],
                   completed_plan=footer['completed_plan'],
                   limitation='Coverage counts are checked structurally; individual decisions outside audit subsets are not independently recomputed.')
    if running:
        summary['snapshot_only'] = True
    return header, blocks, summary


def check_record(record, bound, primes):
    n = record['n']
    p = n*n + n + 1
    need(int(record['p']) == p, 'modulus mismatch at n=%d' % n)
    expected_residue = pow(2, n+1, p)
    need(int(record['residue']) == expected_residue,
         'full residue mismatch at n=%d: stored=%s expected=%d' % (n, record['residue'], expected_residue))
    q = smallest_factor(n, bound, primes)
    need(record['factor'] == q, 'actual smallest sieve factor mismatch at n=%d' % n)
    decision = 'factor' if q else ('survivor' if expected_residue == 1 else 'base2-fail')
    need(record['decision'] == decision, 'decision mismatch at n=%d' % n)
    return '%d\t%s\t%d\t%d\n' % (n, decision, q, expected_residue)


def check_records(prefix, records_path=None, allow_partial=False, running=False, max_blocks=None):
    started = time.monotonic()
    header, blocks, summary = metadata(prefix, allow_partial=allow_partial,
                                       running=running, max_blocks=max_blocks)
    path = records_path or str(prefix) + '.records.jsonl'
    records = read_lines(path, partial_lines=running)
    if running:
        records = [r for r in records if r['index'] < summary['class_count']]
    records.sort(key=lambda r: r['index'])
    by_index = {}
    for r in records:
        need(r['index'] not in by_index, 'duplicate audit record index')
        by_index[r['index']] = r
    primes = sieve_primes(header['sieve_bound'])
    # q=2 (and q=2 mod 3) cannot divide n^2+n+1; retaining them makes this
    # trial-division checker independent of the producer's cube-root sieve.
    all_hash = hashlib.sha256()
    windows = []
    expected_indices = set()
    for b in blocks:
        base, length = b['index'], b['count']
        edges = {base+j for j in (0, 1, length-2, length-1) if 0 <= j < length}
        has_window = header['window_every'] and (
            b['id'] % header['window_every'] == 0 or b['id']+1 == header['blocks'])
        window_indices = set(range(base, base + min(length, header['window_len']))) if has_window else set()
        hit_indices = {(n-header['start']) // header['step'] for n in b['survivors']}
        expected_indices.update(edges | window_indices | hit_indices)
        if window_indices:
            windows.append(dict(block=b['id'], first_index=base, count=len(window_indices),
                                start=b['start'], end=b['start']+header['step']*len(window_indices)))
    need(set(by_index) == expected_indices, 'missing or extra audit records')
    window_hashes = {w['block']: hashlib.sha256() for w in windows}
    factor_count = tested_count = 0
    for r in records:
        i = r['index']
        need(r['n'] == header['start'] + header['step'] * i, 'record progression')
        need(r['block'] == i // header['block_size'], 'record block ID')
        b = blocks[r['block']]
        local = i-b['index']
        is_window = bool(header['window_every'] and
                         (b['id'] % header['window_every'] == 0 or b['id']+1 == header['blocks'])
                         and local < header['window_len'])
        is_edge = local < 2 or local+2 >= b['count']
        need(r['window'] == is_window and r['edge'] == is_edge, 'audit selection flags')
        canonical = check_record(r, header['sieve_bound'], primes).encode()
        all_hash.update(canonical)
        if is_window:
            window_hashes[r['block']].update(canonical)
        if r['factor']:
            factor_count += 1
        else:
            tested_count += 1
    for w in windows:
        w['sha256_every_n_decision_factor_full_residue'] = window_hashes[w['block']].hexdigest()
    summary.update(audit_records=len(records), audit_factor_records=factor_count,
                   audit_unsieved_records=tested_count,
                   audit_sha256=all_hash.hexdigest(), contiguous_audit_windows=windows,
                   audit_seconds=time.monotonic()-started,
                   independent_arithmetic='Python int pow and independent trial division, all records in stated subsets only.')
    return summary


def schema_validate(value, schema, location='$'):
    kinds = {'object': dict, 'array': list, 'string': str}
    kind = schema.get('type')
    if kind:
        need(isinstance(value, kinds[kind]), location+' has wrong JSON type')
    if 'enum' in schema:
        need(value in schema['enum'], location+' invalid enum')
    if kind == 'object':
        need(all(k in value for k in schema.get('required', [])), location+' missing required key')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            need(set(value) <= set(props), location+' additional properties')
        for k, v in value.items():
            if k in props:
                schema_validate(v, props[k], location+'.'+k)
    if kind == 'array':
        for i, item in enumerate(value):
            schema_validate(item, schema['items'], location+'[%d]' % i)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for cmd in ('metadata', 'records'):
        p = sub.add_parser(cmd)
        p.add_argument('prefix')
        p.add_argument('--allow-partial', action='store_true')
        p.add_argument('--running', action='store_true', help='Audit only an observed complete prefix; not a production completion claim.')
        p.add_argument('--max-blocks', type=int, help='Freeze a running-prefix audit at this exact number of blocks.')
        p.add_argument('--output')
        if cmd == 'metadata':
            p.add_argument('--start', type=int)
            p.add_argument('--stop', type=int)
            p.add_argument('--end', type=int, help='Expected actually completed boundary, including cap-stopped runs.')
            p.add_argument('--step', type=int)
            p.add_argument('--published-controls', action='store_true')
        else:
            p.add_argument('--records-path')
    p = sub.add_parser('single')
    p.add_argument('record')
    p.add_argument('--bound', type=int, default=1000000)
    sub.add_parser('schema')
    args = parser.parse_args()
    if args.command == 'metadata':
        result = metadata(args.prefix, args.start, args.stop, args.step,
                          EXPECTED if args.published_controls else None,
                          args.allow_partial, args.running, args.max_blocks)[2]
        if args.end is not None:
            need(result['end'] == args.end, 'completed endpoint differs from expected')
    elif args.command == 'records':
        result = check_records(args.prefix, args.records_path, args.allow_partial,
                               args.running, args.max_blocks)
    elif args.command == 'single':
        r = json.loads(Path(args.record).read_text())
        check_record(r, args.bound, sieve_primes(args.bound))
        result = dict(valid=True, n=r['n'])
    else:
        schema_validate(json.loads(Path('claims.json').read_text()), json.loads(Path('claims.schema.json').read_text()))
        result = dict(valid=True, schema='claims.schema.json')
    text = json.dumps(result, indent=2) + '\n'
    if getattr(args, 'output', None):
        Path(args.output).write_text(text)
    print(text, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, AssertionError, KeyError, IndexError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
