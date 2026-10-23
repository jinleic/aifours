"""Parent raw-to-literal binding, unfolded optimality statements and fresh CPCW kernel replay."""
import ast
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import time
import point_cyclic88_parent_replay as audit

HERE = Path(__file__).resolve().parent
SRC = HERE / 'cpcw-kernel-worker-v1'
OUT = HERE / 'cpcw-kernel-parent-replay-v1'
CASES = [(122, 6, 4), (123, 6, 4), (124, 6, 4), (143, 5, 7),
         (144, 5, 7), (146, 5, 7), (162, 5, 8), (167, 5, 8)]


def run(command, name, steps, expected=0, timeout=1800):
    t = time.monotonic()
    p = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=timeout)
    (OUT / 'parent-logs' / (name + '.stdout')).write_text(p.stdout)
    (OUT / 'parent-logs' / (name + '.stderr')).write_text(p.stderr)
    row = {'name': name, 'command': command, 'exit_code': p.returncode,
           'wall_seconds': round(time.monotonic() - t, 3)}
    steps.append(row)
    print(json.dumps(row), flush=True)
    if p.returncode != expected:
        raise ValueError('unexpected exit ' + name)
    return p


def parent_source():
    text = '''import CpcwKernel.Bridge

/-! Parent-authored target. The family condition spells out all differences and counts;
no worker predicate appears in the statement. In addition to existence at the stated floor,
the theorem quantifies over EVERY other family and proves the upper bound. -/
namespace ParentCpcwAudit

def Family {v k n : Nat} (B : Fin n → Fin k → Fin v) : Prop :=
  (∀ i : Fin n, ∀ j l : Fin k, B i j = B i l → j = l) ∧
  (∀ d : Fin v, d.val ≠ 0 →
    (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
      fun t => B t.1 t.2.1 - B t.1 t.2.2).count d ≤ 1) ∧
  (∀ d : Fin v, d.val = 0 →
    (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
      fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)

def Statement (v k n : Nat) : Prop :=
  (∃ B : Fin n → Fin k → Fin v, Family B) ∧
  n = (v - 1) / (k * (k - 1)) ∧
  (∀ m : Nat, ∀ B : Fin m → Fin k → Fin v, Family B → m ≤ (v - 1) / (k * (k - 1)))

'''
    for v, k, n in CASES:
        tag = str(v) + 'k' + str(k)
        text += f'''theorem optimal{tag} : Statement {v} {k} {n} := by
  obtain ⟨B, hB, hsize⟩ := Cpcw.Kernel.exists_cpcw{tag}
  exact ⟨⟨B, hB⟩, hsize, fun _ _ h => Cpcw.IsCPCW.le_bound (by decide) h⟩

'''
    text += 'end ParentCpcwAudit\n\n'
    for v, k, _ in CASES:
        text += f'#print axioms ParentCpcwAudit.optimal{v}k{k}\n'
    return text


def main():
    OUT.mkdir(exist_ok=False)
    (OUT / 'parent-logs').mkdir()
    (OUT / 'CpcwKernel').mkdir()
    result = {'status': 'FAILED', 'started_at_pt': audit.stamp(), 'steps': [],
              'driver_sha256': audit.sha(__file__), 'audit_helpers_sha256': audit.sha(audit.__file__)}
    try:
        audit.require(audit.sha(SRC / 'manifest.json') == '2bcba717395adfdac125473266cc2e4ebffa76d56e34dc728cd6ef22f0fb2494', 'manifest pin')
        manifest = json.loads((SRC / 'manifest.json').read_text())
        audit.require(audit.sha(SRC / 'replay-worker/result.json') == '044e74904301803dc18ec3134bac89e4ebbfad782c376f63d4927383666ae50b', 'worker receipt pin')
        result['worker_receipt_sha256'] = audit.sha(SRC / 'replay-worker/result.json')
        copied = {}
        for rel, digest in manifest['files'].items():
            if rel.endswith('.lean') or rel in ['lean_env.sh', 'build_module.sh']:
                audit.require(audit.sha(SRC / rel) == digest, 'source pin ' + rel)
                shutil.copyfile(SRC / rel, OUT / rel)
                copied[rel] = audit.sha(OUT / rel)
        result['source_pins'] = copied
        bindings = []
        for v, k, n in CASES:
            tag = str(v) + 'k' + str(k)
            raw_rel = f'review/cpcw{v}-parent-inputs-v1/cpcw_{v}_{k}.txt'
            raw = HERE.parent / raw_rel
            digest = audit.sha(raw)
            audit.require(digest == manifest['raw_inputs'][raw_rel], 'raw pin')
            lines = raw.read_text().splitlines()
            audit.require(lines[0] == f'CPCW {v} {k}', 'raw header')
            rows = [list(map(int, line.split())) for line in lines[1:]]
            source = (OUT / 'CpcwKernel' / ('Data' + tag + '.lean')).read_text()
            literal = re.search(r'def data' + tag + r' : List \(List Nat\) := (\[.*?\n\])', source, re.S)
            header = re.search(r'def data' + tag + r'Header : Nat × Nat := \((\d+), (\d+)\)', source)
            sha_literal = re.search(r'def data' + tag + r'RawSha256 : String := "([a-f0-9]{64})"', source)
            audit.require(literal and ast.literal_eval(literal.group(1)) == rows, 'literal row binding ' + tag)
            audit.require(header and tuple(map(int, header.groups())) == (v, k), 'literal header ' + tag)
            audit.require(sha_literal and sha_literal.group(1) == digest, 'literal SHA ' + tag)
            audit.require(len(rows) == n == (v - 1) // (k * (k - 1)) and all(len(r) == k for r in rows), 'shape/floor ' + tag)
            bindings.append({'v': v, 'k': k, 'n': n, 'sha256': digest, 'literal_rows_equal': True})
        result['literal_binding'] = bindings
        hits, options = [], {}
        for rel in copied:
            if not rel.endswith('.lean'):
                continue
            text = audit.without_comments((OUT / rel).read_text())
            for pattern in audit.FORBIDDEN:
                if re.search(pattern, text, re.M):
                    hits.append({'file': rel, 'pattern': pattern})
            options[rel] = sorted(set(re.findall(r'set_option\s+(\S+)', text)))
            module = Path(rel).stem
            imports = re.findall(r'^import\s+(\S+)', text, re.M)
            audit.require(imports == manifest['import_graph'][module], 'import graph ' + module)
        audit.require(not hits, 'forbidden construct')
        audit.require(all(set(v) <= {'pp.explicit', 'pp.funBinderTypes', 'maxRecDepth', 'maxHeartbeats'} for v in options.values()), 'unexpected options')
        result.update(forbidden_hits=hits, set_options=options)
        order, seen = [], set()
        def visit(module):
            if module in seen:
                return
            seen.add(module)
            for dep in manifest['import_graph'][module]:
                if dep.startswith('CpcwKernel.'):
                    visit(dep.split('.', 1)[1])
            order.append(module)
        visit('Bridge')
        (OUT / 'ParentAudit.lean').write_text(parent_source())
        result['parent_statement_sha256'] = audit.sha(OUT / 'ParentAudit.lean')
        result['rebuilt_modules'] = order
        for module in order:
            run(['sh', 'build_module.sh', 'CpcwKernel/' + module + '.lean'], 'build-' + module, result['steps'])
        run(['sh', 'build_module.sh', 'ParentAudit.lean'], 'build-ParentAudit', result['steps'])
        log = (OUT / 'logs/ParentAudit.build.log').read_text()
        axioms = {name: [a.strip() for a in value.split(',') if a.strip()]
                  for name, value in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        audit.require(set(axioms) == {f'ParentCpcwAudit.optimal{v}k{k}' for v, k, _ in CASES}, 'eight axiom reports')
        audit.require(all(set(a) <= audit.ALLOWED_AXIOMS for a in axioms.values()), 'nonstandard axioms')
        result['axioms'] = axioms
        run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'],
            'fresh-ParentAudit', result['steps'], timeout=3000)
        source = (OUT / 'ParentAudit.lean').read_text()
        mutations = {'FullDifferenceFamily': source.replace('.count d ≤ 1', '.count d = 1'),
                     'WrongNumberOfWords': source.replace('Statement 122 6 4', 'Statement 122 6 5')}
        result['negative_controls'] = {}
        for name, changed in mutations.items():
            audit.require(changed != source, 'control unchanged')
            (OUT / (name + '.lean')).write_text(changed)
            run(['sh', 'build_module.sh', name + '.lean'], 'negative-' + name, result['steps'], expected=1)
            log = (OUT / 'logs' / (name + '.build.log')).read_text()
            audit.require('error:' in log.lower() and 'type mismatch' in log.lower(), 'unintended control error')
            result['negative_controls'][name] = {'expected_type_error': True, 'source_sha256': audit.sha(OUT / (name + '.lean'))}
        result['status'] = 'PARENT_EIGHT_OPTIMALITY_ROOTS_REBUILD_AND_FRESH_KERNEL_PASS'
        result['limits'] = 'Eight frozen cases only; the separate163 addendum is not formalized here. Lean and leanchecker share a toolchain, not an independent kernel/Comparator. Parent statement uses the source-equivalent difference form and includes the universal upper bound.'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = audit.stamp()
        with (OUT / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
        print(json.dumps({k: result.get(k) for k in ['status', 'error', 'axioms']}, indent=2))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
