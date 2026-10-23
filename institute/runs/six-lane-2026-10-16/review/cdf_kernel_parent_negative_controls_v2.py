"""Mutation controls for the parent-authored Lean statement (v2).

v1 (cdf_kernel_parent_negative_controls.py, receipt cdf-kernel-parent-negative-controls-v1/result.json) ran the same
five controls; every wrong statement was rejected, but its receipt says FAIL because it matched the error text
'type mismatch' case-sensitively while Lean 4.34.1 prints 'Type mismatch'. v2 changes only that comparison and the
output directory. Reuses the .olean build of cdf-kernel-parent-replay-v1 (read-only) via CDF_BUILD.
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REPLAY = HERE / 'cdf-kernel-parent-replay-v1'
OUT = HERE / 'cdf-kernel-parent-negative-controls-v2'
STATEMENT = '''def S (v n : Nat) (c : Nat) : Prop :=
  ∃ B : Fin n → Fin 5 → Fin v,
    (∀ i : Fin n, ∀ j k : Fin 5, B i j = B i k → j = k) ∧
    (∀ d : Fin v, d.val ≠ 0 →
      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map
        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = c) ∧
    (∀ d : Fin v, d.val = 0 →
      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map
        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)
'''
CONTROLS = {
    'Positive': ('theorem t : S 321 16 1 := Cdf.Kernel.exists_cdf321', True),
    'WrongOrder': ('theorem t : S 322 16 1 := Cdf.Kernel.exists_cdf321', False),
    'WrongBlockCount': ('theorem t : S 321 17 1 := Cdf.Kernel.exists_cdf321', False),
    'WrongMultiplicity': ('theorem t : S 321 16 2 := Cdf.Kernel.exists_cdf321', False),
    'CrossedRoot': ('theorem t : S 901 45 1 := Cdf.Kernel.exists_cdf801', False),
}


def main():
    OUT.mkdir(exist_ok=False)
    env_script = REPLAY / 'lean_env.sh'
    results = {}
    for name, (theorem, should_pass) in CONTROLS.items():
        src = OUT / f'Control{name}.lean'
        src.write_text('import CdfKernel.Cert321\nimport CdfKernel.Cert801\nimport CdfKernel.Cert901\n\n'
                       f'namespace NegControl{name}\n\n{STATEMENT}\n{theorem}\n\nend NegControl{name}\n')
        cmd = ['sh', '-c', f'CDF_BUILD="{REPLAY}/build"; export CDF_BUILD; . "{env_script}"; exec "$LEAN" -j 1 "$1"',
               'control', str(src)]
        proc = subprocess.run(cmd, cwd=OUT, capture_output=True, text=True, timeout=600)
        output = proc.stdout + proc.stderr
        (OUT / f'Control{name}.log').write_text(output)
        passed = proc.returncode == 0
        intended = passed == should_pass and (should_pass or 'type mismatch' in output.lower())
        results[name] = {'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'expected_to_compile': should_pass,
                         'compiled': passed, 'intended': intended,
                         'first_error_line': next((l for l in output.splitlines() if 'error' in l), '')}
    status = 'NEGATIVE_CONTROLS_PASS' if all(r['intended'] for r in results.values()) else 'FAIL'
    receipt = {'status': status, 'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'controls': results,
               'scope': 'Shows the elaborator/kernel reject wrong parent statements against the worker roots; same toolchain.'}
    with (OUT / 'result.json').open('x') as stream:
        json.dump(receipt, stream, indent=2)
        stream.write('\n')
    print(json.dumps(receipt, indent=2))
    return 0 if status.endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
