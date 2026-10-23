"""Fresh disk gate before one reviewer launch: free >= 12.2e9 + projected growth, else exit 3 (no launch).
Writes desk/gate_<NAME>.json exclusively either way. Usage: python3 -B disk_gate.py NAME
"""
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent.parent
FLOOR, GROWTH = 12_200_000_000, 50_000_000   # projected growth: prompt/stdout/stderr/note/receipt, generous


def main():
    name = sys.argv[1]
    free = shutil.disk_usage(HERE).free
    ok = free >= FLOOR + GROWTH
    rec = {'name': name, 'checked_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
           'free_bytes': free, 'floor': FLOOR, 'projected_growth': GROWTH, 'pass': ok}
    with (HERE / 'desk' / f'gate_{name}.json').open('x') as fh:
        json.dump(rec, fh, indent=1)
        fh.write('\n')
    print(json.dumps(rec))
    return 0 if ok else 3


if __name__ == '__main__':
    raise SystemExit(main())
