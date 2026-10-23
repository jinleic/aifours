"""Parent raw-to-literal binding, unfolded point-cyclic 2-(100,4,1) statements and fresh kernel replay.
Never runs the worker replay driver; copies only pinned sources; refuses an existing output directory."""
import json
from pathlib import Path
import re
import shutil
import mcdsqs38_parent_kernel_replay as shared
import point_cyclic88_parent_replay as audit

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[3] / 'information-science/evidence/six-lane-20261016/point-cyclic100/lean-kernel'
OUT = HERE / 'point-cyclic100-kernel-parent-replay-v2'
MANIFEST_SHA = '18ca2e197c6561cfc88f3b6104e15f3eb1b2502e786ceedfffff97a413f8a60a'
WORKER_RECEIPT_SHA = '27ecefb1ba0bdb035410d4246312928a4ac05598a5f550a1adf2c4fd7533c813'
RAW = HERE / 'point-cyclic100-parent-inputs-v1/pc100_t2.cert'
RAW_SHA = '971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1'
MODULES = ['Target', 'Check', 'Data100', 'Cert100']
ALLOWED_OPTIONS = {'pp.explicit', 'pp.funBinderTypes', 'maxRecDepth', 'maxHeartbeats', 'linter.unusedSectionVars'}

STATEMENT = '''import PC100Kernel.Cert100

/-! Parent-authored targets using only Mathlib notions.  `Statement`: a 2-(100,4,1) design on
`Fin 100` (4-point blocks, every pair in exactly one block) with a resolution (every class a set of
blocks partitioning the points, every block in exactly one class) and a permutation of the points
that is one cycle moving every point, maps the block set onto itself and maps every class onto a
class.  `ShiftStatement` names that permutation as `PC100.shift 100`, and `shift_is_succ` proves it
is x ↦ x + 1. -/
namespace ParentPC100Audit

def Statement : Prop :=
  ∃ B : Finset (Finset (Fin 100)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 100), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∃ R : Finset (Finset (Finset (Fin 100))),
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 100, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      ∃ σ : Equiv.Perm (Fin 100),
        (σ.IsCycle ∧ σ.support = Finset.univ) ∧
        B.image (fun X => X.map σ.toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R

theorem pc100 : Statement := by
  obtain ⟨B, hB, R, hR, σ, hσ, hA⟩ := PC100.Kernel.exists_pc100
  exact ⟨B, hB, R, hR, σ, hσ, hA⟩

def ShiftStatement : Prop :=
  ((PC100.shift 100).IsCycle ∧ (PC100.shift 100).support = Finset.univ) ∧
  ∃ B : Finset (Finset (Fin 100)), ∃ R : Finset (Finset (Finset (Fin 100))),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 100), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 100, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
    B.image (fun X => X.map (PC100.shift 100).toEmbedding) = B ∧
    ∀ P ∈ R, P.image (fun X => X.map (PC100.shift 100).toEmbedding) ∈ R

theorem shift_is_succ : ∀ x : Fin 100, PC100.shift 100 x = x + 1 := fun _ => rfl

theorem pc100_shift : ShiftStatement := by
  obtain ⟨hcyc, B, R, hB, hR, hA⟩ := PC100.Kernel.exists_pc100_shift
  exact ⟨hcyc, B, R, hB, hR, hA⟩

end ParentPC100Audit

#print axioms ParentPC100Audit.pc100
#print axioms ParentPC100Audit.shift_is_succ
#print axioms ParentPC100Audit.pc100_shift
'''


def raw_classes():
    raw = RAW.read_bytes()
    audit.require(audit.sha(RAW) == RAW_SHA, 'raw pin')
    lines = raw.decode('ascii').rstrip('\n').split('\n')
    audit.require(lines[0] == 'POINT-CYCLIC-RESOLUTION 100 4 33 25', 'raw header')
    classes = [[] for _ in range(33)]
    for line in lines[1:]:
        j, *pts = map(int, line.split())
        classes[j].append(tuple(pts))
    return classes


def main():
    shared.OUT = OUT
    OUT.mkdir(exist_ok=False)
    (OUT / 'parent-logs').mkdir()
    (OUT / 'PC100Kernel').mkdir()
    result = {'status': 'FAILED', 'started_at_pt': audit.stamp(), 'steps': [],
              'driver_sha256': audit.sha(__file__), 'shared_driver_sha256': audit.sha(shared.__file__),
              'audit_helpers_sha256': audit.sha(audit.__file__)}
    try:
        audit.require(audit.sha(SRC / 'manifest.json') == MANIFEST_SHA, 'manifest pin')
        manifest = json.loads((SRC / 'manifest.json').read_text())
        audit.require(audit.sha(SRC / 'replay-worker/result.json') == WORKER_RECEIPT_SHA, 'worker receipt pin')
        result['worker_receipt_sha256'] = WORKER_RECEIPT_SHA
        copied = {}
        for rel in [f'PC100Kernel/{m}.lean' for m in MODULES] + ['lean_env.sh', 'build_module.sh']:
            audit.require(audit.sha(SRC / rel) == manifest['files'][rel], 'source pin ' + rel)
            shutil.copyfile(SRC / rel, OUT / rel)
            copied[rel] = audit.sha(OUT / rel)
        result['source_pins'] = copied
        audit.require(manifest['inputs']['cert']['sha256'] == RAW_SHA, 'manifest input pin')
        data_source = (OUT / 'PC100Kernel/Data100.lean').read_text()
        lits = shared.lean_literals(data_source)
        audit.require([[tuple(b) for b in c] for c in lits['cert100']] == raw_classes(), 'literal differs from raw certificate')
        audit.require(f'def cert100RawSha256 : String := "{RAW_SHA}"' in data_source, 'literal raw SHA string')
        result['literal_binding'] = {'raw_sha256': RAW_SHA, 'classes_equal_in_order': 33, 'blocks_per_class': 25}
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
                audit.require(dep.startswith('Mathlib.') or (dep.startswith('PC100Kernel.') and dep.split('.', 1)[1] in MODULES),
                              'unexpected import ' + dep)
        result.update(forbidden_hits=hits, set_options=options, import_graph=imports)
        order, seen = [], set()
        def visit(module):
            if module in seen:
                return
            seen.add(module)
            for dep in imports[module]:
                if dep.startswith('PC100Kernel.'):
                    visit(dep.split('.', 1)[1])
            order.append(module)
        visit('Cert100')
        (OUT / 'ParentAudit.lean').write_text(STATEMENT)
        result['parent_statement_sha256'] = audit.sha(OUT / 'ParentAudit.lean')
        result['rebuilt_modules'] = order
        for module in order:
            shared.run(['sh', 'build_module.sh', 'PC100Kernel/' + module + '.lean'], 'build-' + module, result['steps'])
        shared.run(['sh', 'build_module.sh', 'ParentAudit.lean'], 'build-ParentAudit', result['steps'])
        log = (OUT / 'logs/ParentAudit.build.log').read_text()
        axioms = {name: [a.strip() for a in value.split(',') if a.strip()]
                  for name, value in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        audit.require(set(axioms) == {'ParentPC100Audit.pc100', 'ParentPC100Audit.shift_is_succ',
                                      'ParentPC100Audit.pc100_shift'}, 'axiom reports')
        audit.require(all(set(a) <= audit.ALLOWED_AXIOMS for a in axioms.values()), 'nonstandard axioms')
        result['axioms'] = axioms
        result['superseded_attempt'] = ('point-cyclic100-kernel-parent-replay-v1 failed only because this driver expected '
                                        'shift_is_succ to use no axioms; it uses propext and Quot.sound (standard).')
        result['shift_is_succ_axioms'] = []
        shared.run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'],
                   'fresh-ParentAudit', result['steps'], timeout=3000)
        mutations = {'TriplesNotPairs': STATEMENT.replace('T.card = 2 →', 'T.card = 3 →'),
                     'BlockSizeFive': STATEMENT.replace('X.card = 4', 'X.card = 5'),
                     'ShiftByTwo': STATEMENT.replace('PC100.shift 100 x = x + 1', 'PC100.shift 100 x = x + 2'),
                     'NinetyNinePoints': STATEMENT.replace('Fin 100', 'Fin 99')}
        result['negative_controls'] = {}
        for name, changed in mutations.items():
            audit.require(changed != STATEMENT, 'control unchanged ' + name)
            (OUT / (name + '.lean')).write_text(changed)
            shared.run(['sh', 'build_module.sh', name + '.lean'], 'negative-' + name, result['steps'], expected=1)
            clog = (OUT / 'logs' / (name + '.build.log')).read_text()
            audit.require('error' in clog.lower(), 'negative control without error ' + name)
            first = next((l for l in clog.splitlines() if 'error' in l.lower()), '')
            result['negative_controls'][name] = {'build_failed': True, 'first_error_line': first[:300],
                                                 'source_sha256': audit.sha(OUT / (name + '.lean'))}
        result['status'] = 'PARENT_PC100_BINDING_REBUILD_AND_FRESH_KERNEL_PASS'
        result['limits'] = ('Existence on Fin 100 only. Lean and leanchecker share one toolchain, not an independent kernel '
                            'or Comparator. Raw-certificate binding is checked by this driver outside Lean. The structural '
                            'reduction and priority questions are separate.')
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
