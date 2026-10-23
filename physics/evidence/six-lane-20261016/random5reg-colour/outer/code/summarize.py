#!/usr/bin/env python3
"""Collect per-cone producer/checker results and resource usage into outer/evidence/summary.json.
Usage (lane root): outer/code/summarize.py"""
import glob
import json
import os
import re
import time

EV = 'outer/evidence'


def parse_time(path):
    txt = open(path).read()
    m = re.search(r'([\d.]+) real\s+([\d.]+) user\s+([\d.]+) sys', txt)
    rss = re.search(r'(\d+)\s+maximum resident set size', txt)
    return {'real_s': float(m.group(1)), 'user_s': float(m.group(2)), 'sys_s': float(m.group(3)),
            'max_rss_MiB': round(int(rss.group(1)) / 2**20, 1)}


def main():
    rows, tot = [], {'dual_leaves': 0, 'central_leaves': 0, 'nodes_total': 0, 'producer_wall_s': 0.0,
                     'checker_wall_s': 0.0}
    min_margin = None
    for fi in range(3):
        for fj in range(3):
            c = f'{fi}{fj}'
            row = {'cone': [fi, fj]}
            chk = f'{EV}/cone{c}.check.json'
            if os.path.exists(chk):
                r = json.load(open(chk))
                row.update({k: r[k] for k in ('verdict', 'dual_leaves', 'central_leaves', 'splits', 'failed',
                                              'nodes_total', 'maxdepth', 'min_margin', 'min_margin_float',
                                              'runtime_s', 'cert_sha256', 'r0', 'prec_bits', 'reason')})
                tot['dual_leaves'] += r['dual_leaves']
                tot['central_leaves'] += r['central_leaves']
                tot['nodes_total'] += r['nodes_total']
                if r['min_margin_float'] is not None:
                    min_margin = r['min_margin_float'] if min_margin is None else min(min_margin, r['min_margin_float'])
            else:
                row['verdict'] = 'NOT CHECKED'
            asm = None
            if os.path.exists(f'{EV}/cone{c}.log'):
                for line in open(f'{EV}/cone{c}.log'):
                    d = json.loads(line)
                    if d.get('event') == 'assembled':
                        asm = d
            row['producer_cpu_runtime_s'] = asm['producer_runtime_s'] if asm else None
            chunks = sorted(glob.glob(f'{EV}/resources/produce_cone{c}_chunk*.time'))
            pr = [parse_time(p) for p in chunks]
            if c == '00' and not pr:
                row['producer_resources'] = 'run before resource wrapper; wall time from cone00.log'
            else:
                row['producer_resources'] = pr
                tot['producer_wall_s'] += sum(p['real_s'] for p in pr)
            ct = f'{EV}/resources/check_cone{c}.time'
            if os.path.exists(ct):
                row['checker_resources'] = parse_time(ct)
                tot['checker_wall_s'] += row['checker_resources']['real_s']
            rows.append(row)
    out = {'generated': time.strftime('%Y-%m-%d %H:%M:%S %Z'), 'cones': rows, 'totals': tot,
           'min_margin_float_all_cones': min_margin,
           'all_pass': all(r.get('verdict') == 'PASS' for r in rows)}
    json.dump(out, open(f'{EV}/summary.json', 'w'), indent=1)
    for r in rows:
        print(r['cone'], r.get('verdict'), r.get('dual_leaves'), r.get('central_leaves'), r.get('maxdepth'),
              r.get('min_margin_float'), r.get('producer_cpu_runtime_s'), r.get('runtime_s'))
    print(json.dumps({k: out[k] for k in ('totals', 'min_margin_float_all_cones', 'all_pass')}))


if __name__ == '__main__':
    main()
