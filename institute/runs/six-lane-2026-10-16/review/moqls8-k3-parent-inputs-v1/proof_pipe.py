"""Feed regenerated DIMACS and compressed binary DRAT to the parent checker using anonymous pipes only.
The CNF is opened by drat-trim through its inherited /dev/fd descriptor; no CNF or named FIFO is written.
"""
import hashlib
import os
import subprocess
import threading
import time
from collections import deque


def check(cnf_bytes, proof, drat_trim, seconds=60):
    t0 = time.monotonic()
    rfd, wfd = os.pipe()
    z = subprocess.Popen(['/opt/homebrew/bin/zstd', '-q', '-dc', str(proof)], stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL)
    try:
        d = subprocess.Popen([str(drat_trim), '/dev/fd/%d' % rfd, '-i', '-t', str(seconds)],
                             pass_fds=(rfd,), stdin=z.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    finally:
        os.close(rfd)
        z.stdout.close()
    feed = {'complete': False, 'error': None}

    def writer():
        try:
            with os.fdopen(wfd, 'wb') as f:
                f.write(cnf_bytes)
            feed['complete'] = True
        except (BrokenPipeError, OSError) as e:
            feed['error'] = str(e)
    th = threading.Thread(target=writer)
    th.start()
    h, statuses, tail, lines = hashlib.sha256(), [], deque(maxlen=4), 0
    for raw in d.stdout:
        h.update(raw)
        lines += 1
        s = raw.decode('utf-8', 'replace').strip()
        tail.append(s)
        if s.startswith('s '):
            statuses.append(s)
    drc, zrc = d.wait(), z.wait()
    th.join()
    return {'drat_rc': drc, 'zstd_rc': zrc, 'feed': feed, 'statuses': statuses,
            'output_sha256': h.hexdigest(), 'output_lines': lines, 'tail': list(tail),
            'wall_s': round(time.monotonic() - t0, 3),
            'verified': drc == 0 and zrc == 0 and feed['complete'] and statuses == ['s VERIFIED']}
