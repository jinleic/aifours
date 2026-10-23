#!/usr/bin/env python3
"""Run Comparator configs and write one JSON receipt per config.

Acceptance requires exit code 0 and both markers 'Solution valid.' and 'Your solution is okay!'.
Expected-rejection controls must exit nonzero with the listed message fragment.
Environment: FORMAL points at the owned formal/ directory (toolchain, comparator, shims).
"""
import json, os, pathlib, subprocess, sys, time

FORMAL = pathlib.Path(os.environ.get('FORMAL', pathlib.Path(__file__).resolve().parents[1]))
ENV = FORMAL / 'env'
LEAN_DIR = FORMAL / 'lean'
COMPARATOR = ENV / 'comparator' / '.lake' / 'build' / 'bin' / 'comparator'
EXPECT = {
    'endpoints': ('accept', None),
    'general': ('accept', None),
    'control-Match': ('accept', None),
    'control-Statement': ('reject', 'do not match'),
    'control-Sorry': ('reject', "Illegal axiom detected: 'sorryAx'"),
    'control-Axiom': ('reject', "Illegal axiom detected: 'KSatControl.helper'"),
    'control-Definition': ('reject', 'not match'),
    'control-WrongDensity': ('reject', 'do not match'),
    'control-AlteredModel': ('reject', 'not match'),
    'control-EndpointsWrongDensityL4': ('reject', 'do not match'),
    'control-EndpointsWrongDensityL5': ('reject', 'do not match'),
    'control-EndpointsWrongDensityK3a': ('reject', 'do not match'),
    'control-EndpointsWrongDensityK3b': ('reject', 'do not match'),
    'endpoints-k3': ('accept', None),
}

def run(name):
    cfg = FORMAL / 'comparator' / f'{name}.json'
    env = dict(os.environ)
    env['PATH'] = f"{ENV/'bin'}:{ENV/'toolchains'/'lean-4.24.0-darwin_aarch64'/'bin'}:{env['PATH']}"
    env['LEAN_NUM_THREADS'] = env.get('LEAN_NUM_THREADS', '4')
    t0 = time.time()
    p = subprocess.run(['lake', 'env', str(COMPARATOR), str(cfg)], cwd=LEAN_DIR, env=env,
                       capture_output=True, text=True)
    out = p.stdout + p.stderr
    kind, frag = EXPECT[name]
    accepted = p.returncode == 0 and 'Solution valid.' in out and 'Your solution is okay!' in out
    ok = accepted if kind == 'accept' else (p.returncode != 0 and frag in out)
    receipt = {'config': name, 'expected': kind, 'expected_fragment': frag,
               'exit_code': p.returncode, 'accepted': accepted, 'as_expected': ok,
               'seconds': round(time.time() - t0, 1),
               'fake_landrun': 'THIS IS NOT REAL LANDRUN' in out,
               'markers': [m for m in ['Solution valid.', 'Your solution is okay!'] if m in out],
               'log_tail': out.splitlines()[-12:]}
    (FORMAL / 'comparator' / 'receipts').mkdir(exist_ok=True)
    (FORMAL / 'comparator' / 'receipts' / f'{name}.json').write_text(json.dumps(receipt, indent=1))
    (FORMAL / 'comparator' / 'receipts' / f'{name}.log').write_text(out[-200000:])
    print(json.dumps({k: receipt[k] for k in ['config', 'exit_code', 'accepted', 'as_expected', 'seconds']}))
    return ok

if __name__ == '__main__':
    names = sys.argv[1:] or list(EXPECT)
    results = [run(n) for n in names]
    sys.exit(0 if all(results) else 1)
