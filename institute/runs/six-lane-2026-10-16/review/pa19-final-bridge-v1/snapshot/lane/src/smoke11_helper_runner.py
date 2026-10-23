#!/usr/bin/env python3
"""Test runner for smoke_stream11 test L (helper memory + watchdog2 trip): installs the revision-11 SIGTERM
handler, acquires one CPU token and runs a helper that touches 400 MiB and sleeps, via stream_check11.run_helper.
Writes a JSON log (times of token acquisition, helper return, token release; helper rc) to argv[1].
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check11 as S  # noqa: E402

HELPER = ("b = bytearray(400 * 1024 * 1024)\n"
          "for i in range(0, len(b), 4096):\n"
          "    b[i] = 1\n"
          "import time\n"
          "time.sleep(90)\n")


def main():
    S.install_sigterm_handler()
    log = {"pid": os.getpid()}
    try:
        with S.Token(stage="helper-mem-test") as tok:
            log["token"], log["token_acquired"] = tok.name, time.time()
            rc, out = S.run_helper([sys.executable, "-c", HELPER])
            log["helper_rc"], log["helper_returned"] = rc, time.time()
        log["token_released"] = time.time()
    except SystemExit as e:
        log["system_exit"] = repr(e)
        log["token_released_or_exit"] = time.time()
    log["abort_flag"] = S.ABORT[0]
    with open(sys.argv[1], "w") as f:
        json.dump(log, f, indent=1)


if __name__ == "__main__":
    main()
