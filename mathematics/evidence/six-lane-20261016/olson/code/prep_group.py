#!/usr/bin/env python3
"""Build table + Aut-orbit file for a named group into evidence/groups/NAME.*"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, 'evidence', 'groups')


def prep(name):
    os.makedirs(OUT, exist_ok=True)
    tab = os.path.join(OUT, name + '.tab')
    aut = os.path.join(OUT, name + '.aut.json')
    orb = os.path.join(OUT, name + '.orbits')
    subprocess.run([sys.executable, os.path.join(HERE, 'groups.py'), name, tab], check=True)
    subprocess.run([sys.executable, os.path.join(HERE, 'autorbits.py'), tab, aut], check=True)
    d = json.load(open(aut))
    with open(orb, 'w') as f:
        f.write(f"{d['n']}\n")
        f.write(' '.join(map(str, d['orbit_of'])) + '\n')
        f.write(' '.join(map(str, d['inverse'])) + '\n')
    return tab, orb


if __name__ == '__main__':
    for nm in sys.argv[1:]:
        print(prep(nm))
