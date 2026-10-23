#!/usr/bin/env python3
"""Classify every KSatUpper module against the pinned upstream SatUpper sources.

verbatim: identical to upstream after the single substitution SatUpper -> KSatUpper.
derived:  generalized rewrite of the upstream module of the same path (diff stats reported).
new:      no upstream counterpart.
Upstream pin: yamelton/sat-upper-4268 commit 87fb64825b24159418aa0cdca830a76a9d85ff84.
"""
import difflib, hashlib, json, pathlib, subprocess, sys

FORMAL = pathlib.Path(__file__).resolve().parents[1]
UP = FORMAL / 'upstream' / 'sat-upper-4268'
OURS = FORMAL / 'lean' / 'KSatUpper'
PIN = '87fb64825b24159418aa0cdca830a76a9d85ff84'

def upstream_text(rel):
    p = subprocess.run(['git', '-C', str(UP), 'show', f'{PIN}:lean/SatUpper/{rel}'],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None

def main():
    head = subprocess.run(['git', '-C', str(UP), 'rev-parse', 'HEAD'], capture_output=True,
                          text=True).stdout.strip()
    rows = {}
    for p in sorted(OURS.rglob('*.lean')):
        rel = str(p.relative_to(OURS))
        ours = p.read_text()
        up = upstream_text(rel)
        sha = hashlib.sha256(ours.encode()).hexdigest()
        if up is None:
            rows[rel] = {'class': 'new', 'sha256': sha}
        elif up.replace('SatUpper', 'KSatUpper') == ours:
            rows[rel] = {'class': 'verbatim', 'sha256': sha}
        else:
            d = list(difflib.unified_diff(up.splitlines(), ours.splitlines(), lineterm='', n=0))
            rows[rel] = {'class': 'derived', 'sha256': sha,
                         'lines_removed': sum(1 for l in d if l.startswith('-') and not l.startswith('---')),
                         'lines_added': sum(1 for l in d if l.startswith('+') and not l.startswith('+++'))}
    counts = {c: sum(1 for r in rows.values() if r['class'] == c) for c in ['verbatim', 'derived', 'new']}
    print(json.dumps({'upstream_pin': PIN, 'upstream_checkout_head': head, 'counts': counts,
                      'modules': rows}, indent=1))
    return 0 if head == PIN else 1

if __name__ == '__main__':
    sys.exit(main())
