"""Parent sweep driver for cover_exhaust (no timeouts, no signals, refuses overwrite).
Usage: python3 -B run_sweep.py OUTDIR
Runs, in order: (12,3) for every L = 1..36, then Chee-Etzion-Ta-Vu Table I exact-value calibrations
(9,3) 1..12, (10,3) 1..16, (11,3) 1..22, (9,2) 1..20, (10,2) 1..38. Each job writes OUTDIR/n{n}r{R}L{L}.json
and .hits; a summary line per job is appended to OUTDIR/sweep.jsonl.
"""
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
BIN = HERE / 'cover_exhaust'
JOBS = [(12, 3, 36), (9, 3, 12), (10, 3, 16), (11, 3, 22), (9, 2, 20), (10, 2, 38)]


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds')


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(exist_ok=False)
    log = (out / 'sweep.jsonl').open('x')
    log.write(json.dumps({'event': 'start', 'at_pt': stamp(), 'jobs': JOBS}) + '\n')
    log.flush()
    for n, r, top in JOBS:
        for length in range(1, top + 1):
            base = out / f'n{n}r{r}L{length}'
            started = stamp()
            t0 = time.monotonic()
            proc = subprocess.run([str(BIN), str(n), str(r), str(length), '4', str(base) + '.json', str(base) + '.hits'],
                                  capture_output=True, text=True)
            rec = {'n': n, 'R': r, 'L': length, 'exit': proc.returncode, 'started_pt': started, 'finished_pt': stamp(),
                   'seconds': round(time.monotonic() - t0, 3), 'stdout': proc.stdout.strip(), 'stderr': proc.stderr.strip()}
            if proc.returncode == 0:
                rec['result'] = json.loads((base.parent / (base.name + '.json')).read_text())
            log.write(json.dumps(rec) + '\n')
            log.flush()
            if proc.returncode != 0:
                log.write(json.dumps({'event': 'abort', 'at_pt': stamp()}) + '\n')
                return 1
    log.write(json.dumps({'event': 'done', 'at_pt': stamp()}) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
