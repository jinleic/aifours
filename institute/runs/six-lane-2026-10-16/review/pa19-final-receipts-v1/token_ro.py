"""Read-only lane CPU token for PA19FinalReceiptAudit metadata readers.

Opens an EXISTING token file t<i> (i < current COUNT) with O_RDONLY and takes an exclusive flock; never creates,
truncates or writes token files. Tries each admitted token once without blocking, then waits with ONE blocking
flock on t0 (no polling loop). After acquisition the index is re-checked against COUNT; if COUNT dropped, the lock
is released and TokenRefused is raised. The lock is released on context exit (or process exit).
"""
import fcntl
import os
import time

TOK = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/tokens"


class TokenRefused(RuntimeError):
    pass


def count():
    with open(os.path.join(TOK, "COUNT")) as f:
        return max(0, int(f.read().split()[0]))


class ReadOnlyToken:
    def __init__(self):
        self.fd, self.name, self.acquired_at, self.waited_s = None, None, None, None

    def _fd(self, i):
        p = os.path.join(TOK, "t%d" % i)
        if not os.path.isfile(p):
            raise TokenRefused("token file missing: %s" % p)
        return os.open(p, os.O_RDONLY)

    def __enter__(self):
        t0 = time.time()
        n = count()
        if n < 1:
            raise TokenRefused("COUNT=%d: no token admitted" % n)
        for i in range(n):
            fd = self._fd(i)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                os.close(fd)
                continue
            self.fd, self.name = fd, "t%d" % i
            break
        if self.fd is None:  # one blocking wait, no polling
            fd = self._fd(0)
            fcntl.flock(fd, fcntl.LOCK_EX)
            self.fd, self.name = fd, "t0"
        if int(self.name[1:]) >= count():
            self.__exit__()
            raise TokenRefused("COUNT dropped below held token index")
        self.acquired_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        self.waited_s = round(time.time() - t0, 1)
        return self

    def __exit__(self, *a):
        if self.fd is not None:
            fcntl.flock(self.fd, fcntl.LOCK_UN)
            os.close(self.fd)
            self.fd = None
        return False
