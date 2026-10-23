"""Parent raw-to-literal binding, unfolded RDSQS(52) statement and fresh Lean-kernel replay.
Never runs the worker replay driver; copies only pinned sources; refuses an existing output directory."""
import ast
import json
from pathlib import Path
import re
import shutil
import subprocess
import time
import point_cyclic88_parent_replay as audit

HERE = Path(__file__).resolve().parent
SRC = HERE / 'rdsqs-kernel-worker-v1'
OUT = HERE / 'rdsqs-kernel-parent-replay-v1'
MANIFEST_SHA = '18d865aaf11b6e203c9abc81a1156e3382aff42b7529ae9bdfeecd6361865e1f'
WORKER_RECEIPT_SHA = '4a79572ae61b095332f9fa84d9035b3eca0891ca3eaa876d6c85a7fd7519cc97'
RAW_REL = 'review/rdsqs52-parent-inputs-v1/rdsqs52_z52_m23.txt'
RAW_SHA = '7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6'
MODULES = ['Target', 'Generic', 'Check', 'Counts', 'Data52', 'Cert52']
ALLOWED_OPTIONS = {'pp.explicit', 'pp.funBinderTypes', 'maxRecDepth', 'maxHeartbeats', 'linter.unusedSectionVars'}

STATEMENT = '''import RdsqsKernel.Cert52

/-! Parent-authored target.  Only Mathlib notions appear in `Statement`: an SQS(52) on `Fin 52`
(every block has 4 points, every 3-subset lies in exactly one block) whose derived design at EVERY
point `x` (blocks `X.erase x` for the blocks `X` through `x`) has a resolution `R`: a set of
parallel classes, each consisting of derived blocks and partitioning the points other than `x`,
such that every derived block lies in exactly one class. -/
namespace ParentRdsqsAudit

def Statement : Prop :=
  ∃ B : Finset (Finset (Fin 52)),
    (∀ X ∈ B, X.card = 4) ∧
    (∀ T : Finset (Fin 52), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∀ x : Fin 52, ∃ R : Finset (Finset (Finset (Fin 52))),
      (∀ P ∈ R, (∀ T ∈ P, ∃ X ∈ B, x ∈ X ∧ T = X.erase x) ∧
        ∀ y : Fin 52, y ≠ x → ∃! T, T ∈ P ∧ y ∈ T) ∧
      (∀ X ∈ B, x ∈ X → ∃! P, P ∈ R ∧ X.erase x ∈ P)

theorem rdsqs52 : Statement := by
  obtain ⟨B, ⟨hcard, hcover⟩, hres⟩ := Rdsqs.Kernel.exists_rdsqs52
  refine ⟨B, hcard, hcover, fun x => ?_⟩
  obtain ⟨R, hclasses, hunique⟩ := hres x
  refine ⟨R, fun P hP => ?_, fun X hX hxX => hunique _ ?_⟩
  · obtain ⟨hsub, hpart⟩ := hclasses P hP
    refine ⟨fun T hT => ?_, hpart⟩
    obtain ⟨X, hXf, hXT⟩ := Finset.mem_image.mp (hsub hT)
    exact ⟨X, (Finset.mem_filter.mp hXf).1, (Finset.mem_filter.mp hXf).2, hXT.symm⟩
  · exact Finset.mem_image.mpr ⟨X, Finset.mem_filter.mpr ⟨hX, hxX⟩, rfl⟩

end ParentRdsqsAudit

#print axioms ParentRdsqsAudit.rdsqs52
'''


def run(command, name, steps, expected=0, timeout=1800):
    t = time.monotonic()
    p = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=timeout)
    (OUT / 'parent-logs' / (name + '.stdout')).write_text(p.stdout)
    (OUT / 'parent-logs' / (name + '.stderr')).write_text(p.stderr)
    row = {'name': name, 'command': command, 'exit_code': p.returncode,
           'wall_seconds': round(time.monotonic() - t, 3)}
    steps.append(row)
    print(json.dumps(row), flush=True)
    if (expected == 0 and p.returncode != 0) or (expected != 0 and p.returncode == 0):
        raise ValueError('unexpected exit ' + name)
    return p


def raw_point0(raw_path):
    lines = raw_path.read_text().split('\n')
    start = lines.index('POINT 0')
    classes, i = [], start + 1
    while i < len(lines) and not lines[i].startswith('POINT'):
        line = lines[i]
        if line.startswith('CLASS'):
            audit.require(line == f'CLASS {len(classes)}', 'raw class order')
            classes.append([])
        elif line and not line.startswith('#'):
            classes[-1].append(tuple(map(int, line.split())))
        i += 1
    return classes


def lean_literal(source):
    body = re.search(r'def data52 : List \(List RawTriple\) := (\[.*?\n\])\n', source, re.S)
    audit.require(body is not None, 'data52 literal not found')
    text = re.sub(r'--[^\n]*', '', body.group(1))
    return ast.literal_eval(text)


def main():
    OUT.mkdir(exist_ok=False)
    (OUT / 'parent-logs').mkdir()
    (OUT / 'RdsqsKernel').mkdir()
    result = {'status': 'FAILED', 'started_at_pt': audit.stamp(), 'steps': [],
              'driver_sha256': audit.sha(__file__), 'audit_helpers_sha256': audit.sha(audit.__file__)}
    try:
        audit.require(audit.sha(SRC / 'manifest.json') == MANIFEST_SHA, 'manifest pin')
        manifest = json.loads((SRC / 'manifest.json').read_text())
        audit.require(audit.sha(SRC / 'replay-52-worker/result.json') == WORKER_RECEIPT_SHA, 'worker receipt pin')
        result['worker_receipt_sha256'] = WORKER_RECEIPT_SHA
        copied = {}
        for rel in [f'RdsqsKernel/{m}.lean' for m in MODULES] + ['lean_env.sh', 'build_module.sh']:
            audit.require(audit.sha(SRC / rel) == manifest['files'][rel], 'source pin ' + rel)
            shutil.copyfile(SRC / rel, OUT / rel)
            copied[rel] = audit.sha(OUT / rel)
        result['source_pins'] = copied
        raw = HERE.parent / RAW_REL
        audit.require(audit.sha(raw) == RAW_SHA == manifest['inputs']['52']['raw']['sha256'], 'raw pin')
        data_source = (OUT / 'RdsqsKernel/Data52.lean').read_text()
        literal = lean_literal(data_source)
        point0 = raw_point0(raw)
        audit.require(len(point0) == 25 and all(len(c) == 17 for c in point0), 'raw POINT 0 shape')
        audit.require([list(c) for c in point0] == [list(map(tuple, c)) for c in literal], 'literal differs from raw POINT 0')
        audit.require(f'def data52RawSha256 : String := "{RAW_SHA}"' in data_source, 'literal raw SHA string')
        mults = re.search(r'def mults52 : List \(ℕ × ℕ\) := (\[.*?\])\n', data_source)
        powers = [pow(23, i, 52) for i in range(6)]
        expected_mults = [(m, pow(m, -1, 52)) for m in powers]
        audit.require(mults is not None and ast.literal_eval(mults.group(1)) == expected_mults, 'multiplier list')
        audit.require(pow(23, 6, 52) == 1 and len(set(powers)) == 6, 'multiplier order')
        result['literal_binding'] = {'raw_sha256': RAW_SHA, 'point0_classes': 25, 'triples_per_class': 17,
                                     'literal_equals_raw_point0_in_order': True, 'mults52': expected_mults}
        hits, options, imports = [], {}, {}
        for rel in copied:
            if not rel.endswith('.lean'):
                continue
            text = audit.without_comments((OUT / rel).read_text())
            for pattern in audit.FORBIDDEN:
                if re.search(pattern, text, re.M):
                    hits.append({'file': rel, 'pattern': pattern})
            options[rel] = sorted(set(re.findall(r'set_option\s+(\S+)', text)))
            imports[Path(rel).stem] = re.findall(r'^import\s+(\S+)', text, re.M)
        audit.require(not hits, 'forbidden construct')
        audit.require(all(set(v) <= ALLOWED_OPTIONS for v in options.values()), 'unexpected options')
        for module, deps in imports.items():
            for dep in deps:
                audit.require(dep.startswith('Mathlib.') or (dep.startswith('RdsqsKernel.') and dep.split('.', 1)[1] in MODULES),
                              'unexpected import ' + dep)
        result.update(forbidden_hits=hits, set_options=options, import_graph=imports)
        order, seen = [], set()
        def visit(module):
            if module in seen:
                return
            seen.add(module)
            for dep in imports[module]:
                if dep.startswith('RdsqsKernel.'):
                    visit(dep.split('.', 1)[1])
            order.append(module)
        visit('Cert52')
        (OUT / 'ParentAudit.lean').write_text(STATEMENT)
        result['parent_statement_sha256'] = audit.sha(OUT / 'ParentAudit.lean')
        result['rebuilt_modules'] = order
        for module in order:
            run(['sh', 'build_module.sh', 'RdsqsKernel/' + module + '.lean'], 'build-' + module, result['steps'])
        run(['sh', 'build_module.sh', 'ParentAudit.lean'], 'build-ParentAudit', result['steps'])
        log = (OUT / 'logs/ParentAudit.build.log').read_text()
        axioms = {name: [a.strip() for a in value.split(',') if a.strip()]
                  for name, value in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        audit.require(set(axioms) == {'ParentRdsqsAudit.rdsqs52'}, 'axiom report')
        audit.require(all(set(a) <= audit.ALLOWED_AXIOMS for a in axioms.values()), 'nonstandard axioms')
        result['axioms'] = axioms
        run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'],
            'fresh-ParentAudit', result['steps'], timeout=3000)
        mutations = {'WrongBlockSize': STATEMENT.replace('X.card = 4', 'X.card = 5'),
                     'PairsInsteadOfTriples': STATEMENT.replace('T.card = 3 →', 'T.card = 2 →'),
                     'FiftyThreePoints': STATEMENT.replace('Fin 52', 'Fin 53')}
        result['negative_controls'] = {}
        for name, changed in mutations.items():
            audit.require(changed != STATEMENT, 'control unchanged ' + name)
            (OUT / (name + '.lean')).write_text(changed)
            run(['sh', 'build_module.sh', name + '.lean'], 'negative-' + name, result['steps'], expected=1)
            clog = (OUT / 'logs' / (name + '.build.log')).read_text()
            audit.require('error' in clog.lower(), 'negative control without error ' + name)
            first = next((l for l in clog.splitlines() if 'error' in l.lower()), '')
            result['negative_controls'][name] = {'build_failed': True, 'first_error_line': first[:300],
                                                 'source_sha256': audit.sha(OUT / (name + '.lean'))}
        result['status'] = 'PARENT_RDSQS52_BINDING_REBUILD_AND_FRESH_KERNEL_PASS'
        result['limits'] = ('RDSQS(52) only; the exploratory 76 root is not replayed here. Lean and leanchecker share one '
                            'toolchain, not an independent kernel or Comparator. The statement is existence on Fin 52; '
                            'the raw-certificate binding is checked by this driver, not inside Lean.')
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = audit.stamp()
        with (OUT / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
        print(json.dumps({k: result.get(k) for k in ['status', 'error', 'axioms', 'negative_controls']}, indent=2))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
