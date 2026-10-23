#!/usr/bin/env python3
"""Check and report only the unbroken structural prefix of a running log.

This does NOT certify all arithmetic decisions. Use check.py after completion.
"""
import json
import datetime
from pathlib import Path
import sys


def status(prefix):
    raw = Path(prefix+'.blocks.jsonl').read_text()
    rows = []
    for line in raw.splitlines(keepends=True):
        if not line.endswith('\n'):
            break
        rows.append(json.loads(line))
    h = rows[0]
    completed = {r['id']: r for r in rows if r['kind'] == 'block'}
    i = total = sieved = tested = 0
    hits = []
    while i in completed:
        b = completed[i]
        k = min(h['block_size'], h['total']-i*h['block_size'])
        assert b['index'] == total == i*h['block_size']
        assert b['count'] == k == b['sieved']+b['tested']
        assert b['start'] == h['start']+h['step']*total
        assert b['end'] == b['start']+h['step']*k
        assert len(b['survivors']) == b['hits']
        total += k; sieved += b['sieved']; tested += b['tested']
        hits.extend(b['survivors'])
        i += 1
    result = dict(structural_start=h['start'], structural_end=h['start']+h['step']*total,
                  complete_prefix_blocks=i, class_count=total, sieved=sieved,
                  tested=tested, survivors=hits,
                  finished=rows[-1]['kind'] == 'footer',
                  log_bytes=len(raw),
                  note='Preliminary structural coverage only; full independent record audit not yet implied.')
    return result


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--both':
        result = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
        for label, prefix in [('C', 'logs/main'), ('Python', 'logs/python-main')]:
            r = status(prefix)
            result[label] = {key: r[key] for key in
                             ('structural_end', 'complete_prefix_blocks', 'survivors', 'finished')}
        print(json.dumps(result))
    else:
        prefix = sys.argv[1] if len(sys.argv) > 1 else 'logs/main'
        print(json.dumps(status(prefix)))


if __name__ == '__main__':
    main()
