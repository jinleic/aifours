#!/usr/bin/env python3
"""Versioned compatibility re-encoding for a certificate whose strict parent checker requires ASCII comments.
Nothing outside full hash-comment lines may change. Only U+222A is changed to the ASCII word 'union'; any
other non-ASCII character is an error. Source SHA is mandatory. Both old bytes and new output are retained.
Usage: ascii_comment_projection.py INPUT EXPECTED_SOURCE_SHA NEW_OUTPUT
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
from lane_guard import xopen  # noqa: E402
import hashlib
import json


def main():
    src, expected, out = sys.argv[1:4]
    raw = open(src, 'rb').read()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('source SHA does not match the pinned input')
    original = raw.decode('utf-8').splitlines(keepends=True)
    projected, changed = [], []
    for n, line in enumerate(original, 1):
        new = line.replace('\u222a', 'union') if line.lstrip().startswith('#') else line
        new.encode('ascii')  # fail, rather than dropping any remaining non-ASCII character
        if new != line:
            changed.append(n)
        projected.append(new)
    old_body = ''.join(line for line in original if not line.lstrip().startswith('#'))
    new_body = ''.join(line for line in projected if not line.lstrip().startswith('#'))
    if old_body != new_body:
        raise ValueError('noncomment bytes changed')
    data = ''.join(projected).encode('ascii')
    with xopen(out, 'xb') as fh:
        fh.write(data)
    print(json.dumps({'source':src, 'source_sha256':expected, 'output':out,
                      'sha256':hashlib.sha256(data).hexdigest(), 'changed_comment_lines':changed,
                      'noncomment_bytes_identical':True, 'bytes':len(data)}))


if __name__ == '__main__':
    main()
