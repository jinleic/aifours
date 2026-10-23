"""Metadata-only free-space monitor. Reads statvfs of the repo volume every INTERVAL seconds and, every 300 s,
the local APFS snapshot names via tmutil. Writes one JSON line per observation to a NEW file. Never modifies,
signals or deletes anything; no cleanup, no thinning, no configuration change. Stops itself at END_EPOCH.
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime

VOLUME = '/Users/jinleic/repos/aifours'
INTERVAL = 10
SNAP_EVERY = 300
END_EPOCH = float(sys.argv[2])
OUT = sys.argv[1]
last_snap = 0.0
with open(OUT, 'x') as out:
    out.write(json.dumps({'event': 'start', 'at': datetime.now().astimezone().isoformat(), 'interval': INTERVAL,
                          'end_epoch': END_EPOCH, 'pid': os.getpid()}) + '\n')
    out.flush()
    while time.time() < END_EPOCH:
        now = time.time()
        st = os.statvfs(VOLUME)
        rec = {'t': datetime.fromtimestamp(now).astimezone().isoformat(timespec='seconds'),
               'free': st.f_bavail * st.f_frsize}
        if now - last_snap >= SNAP_EVERY:
            last_snap = now
            try:
                p = subprocess.Popen(['/usr/bin/tmutil', 'listlocalsnapshots', '/'], stdout=subprocess.PIPE,
                                     stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, text=True)
                text = p.communicate()[0]
                rec['snapshots'] = [x for x in text.split() if x.startswith('com.apple.TimeMachine.')][-4:]
            except Exception as e:  # recorded, never hidden
                rec['snapshots_error'] = repr(e)
        out.write(json.dumps(rec) + '\n')
        out.flush()
        time.sleep(INTERVAL)
    out.write(json.dumps({'event': 'end', 'at': datetime.now().astimezone().isoformat()}) + '\n')
