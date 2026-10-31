#!/usr/bin/env python3
"""Probe: status and floating objective of the mixed-block functional LP for given colorings.

Usage: python3 script.py COLORS [COLORS ...]  (10-character strings over {-,0,1,2}).
Calls solve(col, 900.0) of frontier-20261028-plane-functional-v2-lp.py and prints one
JSON line per coloring: status, objective, whether a dual support was returned.
Byte-identical in logic to the scratch copy /tmp/class48-probe.py run at 08:21 PDT
on 2026-10-29 (that scratch file lies outside the write root and is not evidence).
"""
import json,sys
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('fl',ROOT/'frontier-20261028-plane-functional-v2-lp.py');fl=module_from_spec(s);s.loader.exec_module(fl)
for text in sys.argv[1:]:
    col=tuple(None if ch=='-' else int(ch) for ch in text)
    r=fl.solve(col,900.0)
    print(json.dumps({'colors':text,'status':r['status'],'objective':r.get('objective'),'has_dual_support':'dual_support' in r,'keys':sorted(r.keys())}),flush=True)
