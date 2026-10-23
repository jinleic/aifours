#!/usr/bin/env python3
"""Derive the trusted Comparator challenge modules from the statement-level sources.

The challenge copies are byte-identical to the solution sources except that `import
KSatUpper.X` lines become `import KSatChallenge.X`; declarations and namespaces are unchanged, so
constant names coincide. `--check` verifies that property for existing copies.
The target statements themselves live in hand-written KSatChallenge/{Endpoints,General}.lean.
"""
import pathlib, re, sys, hashlib, json

ROOT = pathlib.Path(__file__).resolve().parents[1] / 'lean'
COPIES = ['Local', 'Model', 'Series', 'TrialSpec', 'Criterion']

def derive(text):
    return re.sub(r'^import KSatUpper\.', 'import KSatChallenge.', text, flags=re.M)

def main(check):
    out = {}
    for name in COPIES:
        src = (ROOT / 'KSatUpper' / f'{name}.lean').read_text()
        dst = ROOT / 'KSatChallenge' / f'{name}.lean'
        want = derive(src)
        if check:
            if dst.read_text() != want:
                raise SystemExit(f'challenge copy differs beyond import renaming: {dst}')
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(want)
        imports = [l for l in want.splitlines() if l.startswith('import KSatUpper')]
        if imports:
            raise SystemExit(f'challenge copy still imports solution modules: {dst}')
        out[name] = {'source_sha256': hashlib.sha256(src.encode()).hexdigest(),
                     'challenge_sha256': hashlib.sha256(want.encode()).hexdigest()}
    print(json.dumps({'checked' if check else 'written': out}, indent=1))

if __name__ == '__main__':
    main('--check' in sys.argv)
