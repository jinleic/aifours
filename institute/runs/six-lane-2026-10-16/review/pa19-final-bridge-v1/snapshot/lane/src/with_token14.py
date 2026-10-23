#!/usr/bin/env python3
"""[Margin variant: stream_check14 per-stage12.2e9+64MiB guard; no other auxiliary-command change.]
Run an auxiliary command (aggregation, listing) under one lane CPU token, so that it counts against COUNT like a
pipeline stage (parent CPU accounting): acquires a token via stream_check12.Token (stage 'aux'), runs the command as a
registered helper (run_helper), releases the token after the command has exited, and prints the command's output.
Stop file: cycle2/STOP-aux (admission refused if present). Usage: with_token.py CMD [ARG ...]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check14 as S  # noqa: E402


def main():
    S.install_sigterm_handler()
    S.set_stop_files([os.path.join(os.path.dirname(HERE), "cycle2", "STOP-aux")])
    with S.Token(stage="aux"):
        rc, out = S.run_helper(sys.argv[1:])
    sys.stdout.write(out)
    sys.exit(rc)


if __name__ == "__main__":
    main()
