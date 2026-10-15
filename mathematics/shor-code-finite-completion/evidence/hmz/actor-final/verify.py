#!/usr/bin/env python3
"""Frozen acceptance gate: an actual witness or an exact Lean noncompletion proof."""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
LEAN_CWD = Path('/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/lean-verify')
STATEMENT_SHA = '26ed6f00f550e5007e36cba58ce957121a11b28e029eaaec2bd48058a39cb4b3'
PAIRS = [(0,j) for j in (0,1,7,13,14)] + [(i,j) for i in (3,8) for j in (0,2,4,6)] + [(11,j) for j in (0,1,2)]
ORIGINAL = {'a'*i + 'b' + 'a'*j for i,j in PAIRS}


def ud(words):
    """Sardinas–Patterson; equality of a residual set terminates the exact assay."""
    if '' in words:
        return False
    residual = {v[len(u):] for u in words for v in words if u != v and v.startswith(u)}
    seen = set()
    while residual:
        if '' in residual:
            return False
        frozen = frozenset(residual)
        if frozen in seen:
            return True
        seen.add(frozen)
        residual = ({v[len(u):] for u in words for v in residual if v.startswith(u)} |
                    {v[len(u):] for u in residual for v in words if v.startswith(u)})
    return True


def kraft(words):
    return sum((Fraction(1, 2**len(w)) for w in words), Fraction())


def check_witness(raw):
    if not isinstance(raw, list) or not all(isinstance(w, str) for w in raw):
        raise ValueError('witness must be a list of strings')
    words = set(raw)
    if len(words) != len(raw) or any(not w or set(w) - {'a','b'} for w in words):
        raise ValueError('duplicate, empty or non-binary word')
    if not ORIGINAL <= words:
        raise ValueError('missing original codeword')
    if not ud(words):
        raise ValueError('not uniquely decipherable')
    if kraft(words) != 1:
        raise ValueError('not complete: Kraft sum differs from one')
    return words


def main():
    statement = ROOT / 'Statement.lean'
    if hashlib.sha256(statement.read_bytes()).hexdigest() != STATEMENT_SHA:
        raise ValueError('frozen exact statement changed')
    # Actual false-proposition controls, not missing typeclass synthesis.
    assert ud({'a','b'}) and kraft({'a','b'}) == 1
    assert not ud({'a','aa','b'})
    assert ud(ORIGINAL) and kraft(ORIGINAL) < 1
    if (ROOT / 'witness.json').is_file():
        words = check_witness(json.loads((ROOT / 'witness.json').read_text()))
        removed = words - {next(iter(ORIGINAL))}
        try:
            check_witness(sorted(removed))
        except ValueError:
            pass
        else:
            raise AssertionError('containment mutation accepted')
        assert not ud(words | {'bb'})  # b.b = bb, since b belongs to ORIGINAL.
        assert kraft(removed) < 1
        print(json.dumps({'verdict':'EXACT_POSITIVE_CERTIFICATE', 'words':len(words), 'kraft':'1', 'controls':'passed'}))
        return 0
    solution = ROOT / 'Solution.lean'
    if solution.is_file():
        text = solution.read_text()
        if re.search(r'\b(sorry|admit|axiom|native_decide|ofReduceBool|unsafe|opaque|import|implemented_by|extern)\b', text):
            raise ValueError('disallowed Lean proof escape or import')
        combined = ROOT / 'CombinedVerification.lean'
        combined.write_text(statement.read_text() + '\n' + text + '\nexample : ¬ ShorCompletion.HasFiniteCompletion := ShorCompletion.noncompletion\n#print ShorCompletion.noncompletion\n#print axioms ShorCompletion.noncompletion\n')
        env = os.environ.copy()
        env['PATH'] = str(Path.home()/'.elan/bin') + ':' + env.get('PATH','')
        run = subprocess.run(['lake','env','lean',str(combined)],cwd=LEAN_CWD,env=env,capture_output=True,text=True,timeout=180)
        (ROOT/'lean-verification.log').write_text(run.stdout+run.stderr)
        if run.returncode:
            print(run.stdout+run.stderr)
            return run.returncode
        if 'sorryAx' in run.stdout or 'sorryAx' in run.stderr:
            raise ValueError('proof depends on sorryAx')
        print(json.dumps({'verdict':'EXACT_NEGATIVE_LEAN_ROOT', 'log':'lean-verification.log', 'semantic_review':'still required'}))
        return 0
    print(json.dumps({'verdict':'UNRESOLVED', 'reason':'No finite complete witness or exact universal Lean proof; partial arguments do not pass.'}))
    return 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, AssertionError, subprocess.TimeoutExpired) as error:
        print(json.dumps({'verdict':'REJECTED', 'reason':str(error)}))
        sys.exit(1)
