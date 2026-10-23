"""Mechanics probe (not evidence): cadical reads CNF on stdin ('-'), writes binary DRAT into a named FIFO held open by
this process (reader + dummy writer, so EOF only after the solver is reaped); prints rc, stdout lines, proof bytes."""
import hashlib
import os
import select
import subprocess
import sys
import time

CAD = '/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical'
HERE = os.path.dirname(os.path.abspath(__file__))
fifo = os.path.join(HERE, 'proof.fifo')
for name in sys.argv[1:]:
    cnf = open(os.path.join(HERE, name), 'rb').read()
    rfd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    wdummy = os.open(fifo, os.O_WRONLY | os.O_NONBLOCK)
    p = subprocess.Popen([CAD, '-q', '-t', '10', '-', fifo], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, env={'PATH': '/usr/bin:/bin', 'LC_ALL': 'C'})
    p.stdin.write(cnf)
    p.stdin.close()
    buf = bytearray()
    out = p.stdout.read()
    err = p.stderr.read()
    rc = p.wait()
    os.close(wdummy)
    while True:
        r, _, _ = select.select([rfd], [], [], 1.0)
        if not r:
            break
        b = os.read(rfd, 1 << 16)
        if not b:
            break
        buf += b
    os.close(rfd)
    print(name, 'rc', rc, 'stdout', out.decode().splitlines(), 'stderr', err.decode()[:200], 'proof', len(buf),
          buf.hex(), hashlib.sha256(bytes(buf)).hexdigest()[:16])
