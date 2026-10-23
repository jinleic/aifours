#!/usr/bin/env python3
"""Write manifest.json (exclusive create) listing every file under this directory,
except manifest.json itself, with its SHA-256, size in bytes and role.

Usage: python3 -I -B make_manifest.py
"""

import datetime
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROLES = {
    'checker_b.py': 'frozen checker (route B, explicit MOLS)',
    'make_controls.py': 'control generator',
    'run_controls.py': 'control harness',
    'make_manifest.py': 'manifest writer',
    'report.md': 'report',
    'controls/expected.json': 'hand-derived control expectations',
}


def role(rel):
    if rel in ROLES:
        return ROLES[rel]
    if rel.startswith('controls/'):
        return 'control input'
    if rel.startswith('runs/'):
        return 'control-run output'
    return 'other'


def main():
    entries = []
    for root, dirs, files in os.walk(HERE):
        dirs.sort()
        for name in sorted(files):
            path = os.path.join(root, name)
            rel = os.path.relpath(path, HERE).replace(os.sep, '/')
            if rel == 'manifest.json':
                continue
            with open(path, 'rb') as fh:
                data = fh.read()
            entries.append({'path': rel, 'sha256': hashlib.sha256(data).hexdigest(),
                            'bytes': len(data), 'role': role(rel)})
    manifest = {
        'directory': HERE,
        'author': 'ContinueCFR21.CheckerRouteB',
        'created_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'note': 'every file created in this directory except manifest.json itself; '
                'all were created new and none was modified afterwards',
        'file_count': len(entries),
        'files': entries,
    }
    with open(os.path.join(HERE, 'manifest.json'), 'x', encoding='ascii') as fh:
        json.dump(manifest, fh, indent=1)
        fh.write('\n')
    for e in entries:
        print('%s  %7d  %s  [%s]' % (e['sha256'], e['bytes'], e['path'], e['role']))
    print('%d files listed in manifest.json' % len(entries))


if __name__ == '__main__':
    main()
