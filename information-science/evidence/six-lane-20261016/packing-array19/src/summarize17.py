#!/usr/bin/env python3
"""New metadata presentation only: aggregate17 exact structural row + unchanged completed six-unit M1 cover.
The six-unit predicate is reused directly from immutable summarize16.cell_cover; no solver/guard/source changes.
"""
import contextlib
import io
import json
import os

import aggregate17 as A
import summarize16 as CELL


def main():
    with contextlib.redirect_stdout(io.StringIO()):
        A.main()
    with open(os.path.join(A.LANE, 'STATUS17_BASE.json')) as f:
        out = json.load(f)
    cover = CELL.cell_cover(out['sat_results'])
    out['cell_cover_s00468'] = cover
    if cover['all_six_checked'] and CELL.TAG in out['M1_open_tags']:
        out['M1_open_tags'].remove(CELL.TAG)
        out['M1_open'] = len(out['M1_open_tags'])
        p = out['per_multiset']['ms06']
        p['M1_certified'] += 1
        p['M1_how']['cell-six-unit'] = 1
        if CELL.TAG not in out['M2_open_tags']:
            p['both'] += 1
    with open(os.path.join(A.LANE, 'STATUS17.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k:v for k,v in out.items() if not k.endswith('_tags') and k != 'uncertified_list'}, indent=1))


if __name__ == '__main__':
    main()
