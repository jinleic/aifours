"""Parent raw-to-literal binding, unfolded point-cyclic statements for v in {112,136,160,196}, rebuild and fresh
kernel replay of the combined table package. Never runs worker replay drivers; copies only pinned sources;
refuses an existing output directory. Lean and leanchecker share one toolchain.
Usage: python3 -B point_cyclic_table_parent_kernel_replay.py
"""
import json
from pathlib import Path
import re
import shutil
import mcdsqs38_parent_kernel_replay as shared
import point_cyclic88_parent_replay as audit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / 'information-science/evidence/six-lane-20261016/point-cyclic-table200/lean-kernel'
V100 = ROOT / 'information-science/evidence/six-lane-20261016/point-cyclic100/lean-kernel'
OUT = HERE / 'point-cyclic-table-kernel-parent-replay-v1'
MANIFEST_SHA = '1f15f540625ed8e83ccda8cf8d2698d61e47e50c5864b99bd4e3f8a62d156897'
ORDERS = {112: ('pc112_t1', 37, 28), 136: ('pc136_t3', 45, 34), 160: ('pc160_t3', 53, 40), 196: ('pc196_t2', 65, 49)}
ALLOWED_OPTIONS = {'pp.explicit', 'pp.funBinderTypes', 'maxRecDepth', 'maxHeartbeats', 'linter.unusedSectionVars'}


def statement_block(v):
    return f'''
def Statement{v} : Prop :=
  ∃ B : Finset (Finset (Fin {v})),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin {v}), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∃ R : Finset (Finset (Finset (Fin {v}))),
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin {v}, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      ∃ σ : Equiv.Perm (Fin {v}),
        (σ.IsCycle ∧ σ.support = Finset.univ) ∧
        B.image (fun X => X.map σ.toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R

theorem pc{v} : Statement{v} := by
  obtain ⟨B, hB, R, hR, σ, hσ, hA⟩ := PC100.Kernel.exists_pc{v}
  exact ⟨B, hB, R, hR, σ, hσ, hA⟩

def ShiftStatement{v} : Prop :=
  ((PC100.shift {v}).IsCycle ∧ (PC100.shift {v}).support = Finset.univ) ∧
  ∃ B : Finset (Finset (Fin {v})), ∃ R : Finset (Finset (Finset (Fin {v}))),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin {v}), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin {v}, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
    B.image (fun X => X.map (PC100.shift {v}).toEmbedding) = B ∧
    ∀ P ∈ R, P.image (fun X => X.map (PC100.shift {v}).toEmbedding) ∈ R

theorem shift{v}_is_succ : ∀ x : Fin {v}, PC100.shift {v} x = x + 1 := fun _ => rfl

theorem pc{v}_shift : ShiftStatement{v} := by
  obtain ⟨hcyc, B, R, hB, hR, hA⟩ := PC100.Kernel.exists_pc{v}_shift
  exact ⟨hcyc, B, R, hB, hR, hA⟩
'''


STATEMENT = ''.join(f'import PCTableKernelR2.Cert{v}\n' for v in ORDERS) + '''
/-! Parent-authored targets using only Mathlib notions.  For each listed v, `Statement` asserts a 2-(v,4,1)
design on `Fin v` with a resolution and a single-cycle point permutation preserving the blocks and mapping every
class onto a class; `ShiftStatement` names that permutation as `PC100.shift v`, which is x ↦ x + 1. -/
namespace ParentPCTableAudit
''' + ''.join(statement_block(v) for v in ORDERS) + '''
end ParentPCTableAudit
''' + ''.join(f'''
#print axioms ParentPCTableAudit.pc{v}
#print axioms ParentPCTableAudit.shift{v}_is_succ
#print axioms ParentPCTableAudit.pc{v}_shift''' for v in ORDERS) + '\n'


def raw_classes(v, stem, classes, per_class):
    pin = HERE / f'point-cyclic{v}-parent-inputs-v1'
    receipt = json.loads((pin / 'pin-receipt.json').read_text())
    raw_sha = receipt['files'][stem + '.cert']['sha256']
    audit.require(audit.sha(pin / (stem + '.cert')) == raw_sha, f'raw pin {v}')
    lines = (pin / (stem + '.cert')).read_text().rstrip('\n').split('\n')
    audit.require(lines[0] == f'POINT-CYCLIC-RESOLUTION {v} 4 {classes} {per_class}', f'raw header {v}')
    out = [[] for _ in range(classes)]
    for line in lines[1:]:
        j, *pts = map(int, line.split())
        out[j].append(tuple(pts))
    return out, raw_sha


def main():
    shared.OUT = OUT
    OUT.mkdir(exist_ok=False)
    (OUT / 'parent-logs').mkdir()
    (OUT / 'PC100Kernel').mkdir()
    (OUT / 'PCTableKernelR2').mkdir()
    result = {'status': 'FAILED', 'started_at_pt': audit.stamp(), 'steps': [], 'driver_sha256': audit.sha(__file__),
              'shared_driver_sha256': audit.sha(shared.__file__), 'audit_helpers_sha256': audit.sha(audit.__file__)}
    try:
        audit.require(audit.sha(SRC / 'manifest.json') == MANIFEST_SHA, 'manifest pin')
        manifest = json.loads((SRC / 'manifest.json').read_text())
        receipt_sha = audit.sha(SRC / 'replay-worker/result.json')
        audit.require(receipt_sha.startswith('7afaf1fd') and receipt_sha.endswith('595c'), 'worker receipt pin')
        result['worker_receipt_sha256'] = receipt_sha
        v100 = json.loads((V100 / 'manifest.json').read_text())
        modules = ['PC100Kernel/Target', 'PC100Kernel/Check'] + [f'PCTableKernelR2/{kind}{v}' for v in ORDERS for kind in ('Data', 'Cert')]
        copied = {}
        for rel in [m + '.lean' for m in modules] + ['lean_env.sh', 'build_module.sh']:
            audit.require(audit.sha(SRC / rel) == manifest['files'][rel], 'source pin ' + rel)
            shutil.copyfile(SRC / rel, OUT / rel)
            copied[rel] = audit.sha(OUT / rel)
        for rel in ['PC100Kernel/Target.lean', 'PC100Kernel/Check.lean']:
            audit.require(copied[rel] == v100['files'][rel], 'generic module differs from accepted v100 package: ' + rel)
        result['source_pins'] = copied
        result['generic_modules_equal_accepted_v100'] = True
        bindings = {}
        for v, (stem, classes, per_class) in ORDERS.items():
            raw, raw_sha = raw_classes(v, stem, classes, per_class)
            audit.require(manifest['inputs'][str(v)]['cert']['sha256'] == raw_sha, f'manifest input pin {v}')
            source = (OUT / f'PCTableKernelR2/Data{v}.lean').read_text()
            lits = shared.lean_literals(source)
            audit.require([[tuple(b) for b in c] for c in lits[f'cert{v}']] == raw, f'literal differs from raw certificate {v}')
            audit.require(f'def cert{v}RawSha256 : String := "{raw_sha}"' in source, f'literal raw SHA string {v}')
            bindings[v] = {'raw_sha256': raw_sha, 'classes_equal_in_order': classes, 'blocks_per_class': per_class}
        result['literal_binding'] = bindings
        hits, options, imports = [], {}, {}
        for rel in copied:
            if not rel.endswith('.lean'):
                continue
            text = audit.without_comments((OUT / rel).read_text())
            for pattern in audit.FORBIDDEN:
                if re.search(pattern, text, re.M):
                    hits.append({'file': rel, 'pattern': pattern})
            options[rel] = sorted(set(re.findall(r'set_option\s+(\S+)', text)))
            imports[rel[:-5]] = re.findall(r'^import\s+(\S+)', text, re.M)
        audit.require(not hits, 'forbidden construct')
        audit.require(all(set(v) <= ALLOWED_OPTIONS for v in options.values()), 'unexpected options')
        for module, deps in imports.items():
            for dep in deps:
                audit.require(dep.startswith('Mathlib.') or dep.replace('.', '/') in modules, 'unexpected import ' + dep)
        result.update(forbidden_hits=hits, set_options=options, import_graph=imports)
        order, seen = [], set()

        def visit(module):
            if module in seen:
                return
            seen.add(module)
            for dep in imports[module]:
                if not dep.startswith('Mathlib.'):
                    visit(dep.replace('.', '/'))
            order.append(module)
        for v in ORDERS:
            visit(f'PCTableKernelR2/Cert{v}')
        (OUT / 'ParentAudit.lean').write_text(STATEMENT)
        result['parent_statement_sha256'] = audit.sha(OUT / 'ParentAudit.lean')
        result['rebuilt_modules'] = order
        for module in order:
            shared.run(['sh', 'build_module.sh', module + '.lean'], 'build-' + module.replace('/', '-'), result['steps'], timeout=3000)
        shared.run(['sh', 'build_module.sh', 'ParentAudit.lean'], 'build-ParentAudit', result['steps'], timeout=3000)
        log = (OUT / 'logs/ParentAudit.build.log').read_text()
        axioms = {name: [a.strip() for a in value.split(',') if a.strip()]
                  for name, value in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        expected = {f'ParentPCTableAudit.{n}' for v in ORDERS for n in (f'pc{v}', f'pc{v}_shift')}
        audit.require(expected <= set(axioms), 'axiom reports')
        audit.require(all(set(a) <= audit.ALLOWED_AXIOMS for a in axioms.values()), 'nonstandard axioms')
        result['axioms'] = axioms
        shared.run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'],
                   'fresh-ParentAudit', result['steps'], timeout=6000)
        mutations = {'TriplesNotPairs196': STATEMENT.replace('T : Finset (Fin 196), T.card = 2', 'T : Finset (Fin 196), T.card = 3'),
                     'BlockSizeFive112': STATEMENT.replace('∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 112)', '∀ X ∈ B, X.card = 5) ∧ ∀ T : Finset (Fin 112)'),
                     'ShiftByTwo136': STATEMENT.replace('PC100.shift 136 x = x + 1', 'PC100.shift 136 x = x + 2'),
                     'WrongOrder160': STATEMENT.replace('Statement160 : Prop :=\n  ∃ B : Finset (Finset (Fin 160))', 'Statement160 : Prop :=\n  ∃ B : Finset (Finset (Fin 159))')}
        result['negative_controls'] = {}
        for name, changed in mutations.items():
            audit.require(changed != STATEMENT, 'control unchanged ' + name)
            (OUT / (name + '.lean')).write_text(changed)
            shared.run(['sh', 'build_module.sh', name + '.lean'], 'negative-' + name, result['steps'], expected=1, timeout=3000)
            clog = (OUT / 'logs' / (name + '.build.log')).read_text()
            audit.require('error' in clog.lower(), 'negative control without error ' + name)
            first = next((l for l in clog.splitlines() if 'error' in l.lower()), '')
            result['negative_controls'][name] = {'build_failed': True, 'first_error_line': first[:300],
                                                 'source_sha256': audit.sha(OUT / (name + '.lean'))}
        result['status'] = 'PARENT_PC_TABLE_BINDING_REBUILD_AND_FRESH_KERNEL_PASS'
        result['limits'] = ('Existence for the four listed orders only. Lean and leanchecker share one toolchain, not an independent '
                            'kernel or Comparator. Raw-certificate binding is checked outside Lean by this driver. Nonexistence entries '
                            '(124/172 published, 184 written 8p corollary) and the cited 148 entry are not kernel-checked here.')
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
