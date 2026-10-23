#!/usr/bin/env python3
"""Compare aggregate decisions in every completely overlapping pair of scans.

This imports only an evidence checker. Neither producing scanner is imported
or executed. Equal aggregate counts are additional controls, not per-n hashes.
"""
import argparse
import json
from pathlib import Path

from check import metadata, need


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--c-prefix', default='logs/main')
    p.add_argument('--python-prefix', default='logs/python-main')
    p.add_argument('--running', action='store_true')
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
    result = dict(compared_c_blocks=common, python_blocks_per_c_block=ratio,
                  common_start=hc['start'],
                  common_end=hc['start']+hc['step']*hc['block_size']*common,
                  c_scan_end=sc['end'], python_scan_end=sp['end'],
                  python_class_members=sp['class_count'],
                  limitation='Whole-block aggregate agreement only. The separate Python computation repeats only its stated contiguous prefix, not the entire C range.')
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
