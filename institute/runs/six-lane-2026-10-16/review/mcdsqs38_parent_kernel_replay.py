"""Parent raw-to-literal binding, unfolded mcDSQS(38) statements and fresh Lean-kernel replay.
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
SRC = HERE / 'mcdsqs-kernel-worker-v1'
OUT = HERE / 'mcdsqs38-kernel-parent-replay-v1'
MANIFEST_SHA = '1200c2c8dd48383c318f9abbeb411c8b2e0c424a37a25a0c42012c1348305a6b'
WORKER_RECEIPT_SHA = 'fe673e16fa5b04ab0708652755e9a0db109f80189d3fead07d28ff01f9e8306c'
RAW = HERE / 'mcdsqs38-parent-inputs-v1/mcdsqs38_g342_s0.txt'
RAW_SHA = '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'
MODULES = ['Target', 'Check', 'Counts', 'Data38', 'Cert38']
ALLOWED_OPTIONS = {'pp.explicit', 'pp.funBinderTypes', 'maxRecDepth', 'maxHeartbeats', 'linter.unusedSectionVars'}

STATEMENT = '''import McdKernel.Cert38

/-! Parent-authored targets using only Mathlib notions.  `ColourCounts n` is the set of numbers
of colour classes of colourings of Steiner triple systems on `Fin n`: every block is a 3-set,
every pair lies in exactly one block, and the colour classes are nonempty sets of pairwise
disjoint blocks with every block in exactly one class.  `Statement` says an SQS(38) exists whose
derived design at EVERY point has a colouring with exactly `sInf (ColourCounts 37)` classes. -/
namespace ParentMcdAudit

def ColourCounts (n : ℕ) : Set ℕ :=
  {r | ∃ S : Finset (Finset (Fin n)),
      ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin n), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
      ∃ C : Finset (Finset (Finset (Fin n))),
        ((∀ Q ∈ C, Q.Nonempty ∧ Q ⊆ S ∧ ∀ T ∈ Q, ∀ T' ∈ Q, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ S, ∃! Q, Q ∈ C ∧ T ∈ Q) ∧ C.card = r}

theorem chi37 : sInf (ColourCounts 37) = 19 := Mcd.Kernel.chiPrime_37

def Statement : Prop :=
  ∃ B : Finset (Finset (Fin 38)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 38), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∀ x : Fin 38, ∃ C : Finset (Finset (Finset (Fin 38))),
      ((∀ Q ∈ C, Q.Nonempty ∧ (∀ T ∈ Q, ∃ X ∈ B, x ∈ X ∧ T = X.erase x) ∧
          ∀ T ∈ Q, ∀ T' ∈ Q, T ≠ T' → Disjoint T T') ∧
        ∀ X ∈ B, x ∈ X → ∃! Q, Q ∈ C ∧ X.erase x ∈ Q) ∧
      C.card = sInf (ColourCounts 37)

theorem mcdsqs38 : Statement := by
  obtain ⟨B, hB, hcol⟩ := Mcd.Kernel.exists_mcdsqs38
  refine ⟨B, hB, fun x => ?_⟩
  obtain ⟨C, ⟨hppc, huniq⟩, hcard⟩ := hcol x
  refine ⟨C, ⟨fun Q hQ => ?_, fun X hX hxX => huniq _ ?_⟩, ?_⟩
  · obtain ⟨hne, hsub, hdisj⟩ := hppc Q hQ
    refine ⟨hne, fun T hT => ?_, hdisj⟩
    obtain ⟨X, hXf, hXT⟩ := Finset.mem_image.mp (hsub hT)
    exact ⟨X, (Finset.mem_filter.mp hXf).1, (Finset.mem_filter.mp hXf).2, hXT.symm⟩
  · exact Finset.mem_image.mpr ⟨X, Finset.mem_filter.mpr ⟨hX, hxX⟩, rfl⟩
  · calc C.card = Mcd.chiPrime (38 - 1) := hcard
      _ = 19 := Mcd.Kernel.chiPrime_37
      _ = sInf (ColourCounts 37) := chi37.symm

end ParentMcdAudit

#print axioms ParentMcdAudit.chi37
#print axioms ParentMcdAudit.mcdsqs38
'''


def run(command, name, steps, expected=0, timeout=1800):
    t = time.monotonic()
    p = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=timeout)
    (OUT / 'parent-logs' / (name + '.stdout')).write_text(p.stdout)
    (OUT / 'parent-logs' / (name + '.stderr')).write_text(p.stderr)
    row = {'name': name, 'command': command, 'exit_code': p.returncode, 'wall_seconds': round(time.monotonic() - t, 3)}
    steps.append(row)
    print(json.dumps(row), flush=True)
    if (expected == 0 and p.returncode != 0) or (expected != 0 and p.returncode == 0):
        raise ValueError('unexpected exit ' + name)
    return p


def lean_literals(source):
    """Return {name: python value} for every `def NAME : TYPE := [...]` literal, by bracket matching."""
    clean = re.sub(r'--[^\n]*', '', source)
    out = {}
    for m in re.finditer(r'^def (\w+) : [^\n]*:= \[', clean, re.M):
        i, depth = m.end() - 1, 0
        for j in range(i, len(clean)):
            if clean[j] == '[':
                depth += 1
            elif clean[j] == ']':
                depth -= 1
                if depth == 0:
                    out[m.group(1)] = ast.literal_eval(clean[i:j + 1])
                    break
    return out


def raw_sections():
    lines = [l for l in RAW.read_text().split('\n') if l and not l.startswith('#')]
    audit.require(lines[:3] == ['MCDSQS 38', 'COLOURS 19', 'BLOCKS'], 'raw header')
    blocks = [tuple(map(int, l.split())) for l in lines[3:3 + 2109]]
    cols, x = {}, None
    for l in lines[3 + 2109:]:
        if l.startswith('POINT'):
            x = int(l.split()[1]); cols[x] = []
        elif l.startswith('CLASS'):
            audit.require(l == f'CLASS {len(cols[x])}', 'raw class order')
            cols[x].append([])
        else:
            cols[x][-1].append(tuple(map(int, l.split())))
    audit.require(sorted(cols) == list(range(38)), 'raw POINT order')
    return blocks, cols


def main():
    OUT.mkdir(exist_ok=False)
    (OUT / 'parent-logs').mkdir()
    (OUT / 'McdKernel').mkdir()
    result = {'status': 'FAILED', 'started_at_pt': audit.stamp(), 'steps': [],
              'driver_sha256': audit.sha(__file__), 'audit_helpers_sha256': audit.sha(audit.__file__)}
    try:
        audit.require(audit.sha(SRC / 'manifest.json') == MANIFEST_SHA, 'manifest pin')
        manifest = json.loads((SRC / 'manifest.json').read_text())
        audit.require(audit.sha(SRC / 'replay-worker/result.json') == WORKER_RECEIPT_SHA, 'worker receipt pin')
        result['worker_receipt_sha256'] = WORKER_RECEIPT_SHA
        copied = {}
        for rel in [f'McdKernel/{m}.lean' for m in MODULES] + ['lean_env.sh', 'build_module.sh']:
            audit.require(audit.sha(SRC / rel) == manifest['files'][rel], 'source pin ' + rel)
            shutil.copyfile(SRC / rel, OUT / rel)
            copied[rel] = audit.sha(OUT / rel)
        result['source_pins'] = copied
        audit.require(audit.sha(RAW) == RAW_SHA == manifest['input']['sha256'], 'raw pin')
        data_source = (OUT / 'McdKernel/Data38.lean').read_text()
        lits = lean_literals(data_source)
        chunk_names = sorted((k for k in lits if re.fullmatch(r'blocks38_\d+', k)), key=lambda k: int(k.split('_')[1]))
        assembled = re.search(r'def blocks38 : List RawQuad :=\s*\n\s*(.+)\n', data_source)
        audit.require(assembled and assembled.group(1).split(' ++ ') == chunk_names, 'blocks38 assembly order')
        lean_blocks = [tuple(b) for k in chunk_names for b in lits[k]]
        colour_line = re.search(r'def colour38 : List \(List \(List RawTriple\)\) :=\s*\n\s*\[(.*)\]\n', data_source)
        audit.require(colour_line and [s.strip() for s in colour_line.group(1).split(',')] == [f'col38_{x}' for x in range(38)],
                      'colour38 assembly order')
        raw_blocks, raw_cols = raw_sections()
        audit.require(lean_blocks == raw_blocks, 'block literal differs from raw BLOCKS section')
        for x in range(38):
            audit.require([[tuple(t) for t in c] for c in lits[f'col38_{x}']] == raw_cols[x], f'colour literal differs at POINT {x}')
        audit.require(f'def data38RawSha256 : String := "{RAW_SHA}"' in data_source, 'literal raw SHA string')
        result['literal_binding'] = {'raw_sha256': RAW_SHA, 'blocks_equal_in_order': 2109, 'points_equal_in_order': 38,
                                     'block_chunks': chunk_names}
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
                audit.require(dep.startswith('Mathlib.') or (dep.startswith('McdKernel.') and dep.split('.', 1)[1] in MODULES),
                              'unexpected import ' + dep)
        result.update(forbidden_hits=hits, set_options=options, import_graph=imports)
        order, seen = [], set()
        def visit(module):
            if module in seen:
                return
            seen.add(module)
            for dep in imports[module]:
                if dep.startswith('McdKernel.'):
                    visit(dep.split('.', 1)[1])
            order.append(module)
        visit('Cert38')
        (OUT / 'ParentAudit.lean').write_text(STATEMENT)
        result['parent_statement_sha256'] = audit.sha(OUT / 'ParentAudit.lean')
        result['rebuilt_modules'] = order
        for module in order:
            run(['sh', 'build_module.sh', 'McdKernel/' + module + '.lean'], 'build-' + module, result['steps'])
        run(['sh', 'build_module.sh', 'ParentAudit.lean'], 'build-ParentAudit', result['steps'])
        log = (OUT / 'logs/ParentAudit.build.log').read_text()
        axioms = {name: [a.strip() for a in value.split(',') if a.strip()]
                  for name, value in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        audit.require(set(axioms) == {'ParentMcdAudit.chi37', 'ParentMcdAudit.mcdsqs38'}, 'axiom reports')
        audit.require(all(set(a) <= audit.ALLOWED_AXIOMS for a in axioms.values()), 'nonstandard axioms')
        result['axioms'] = axioms
        run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'],
            'fresh-ParentAudit', result['steps'], timeout=3000)
        mutations = {'ChiEighteen': STATEMENT.replace('theorem chi37 : sInf (ColourCounts 37) = 19', 'theorem chi37 : sInf (ColourCounts 37) = 18'),
                     'BlockSizeFive': STATEMENT.replace('X.card = 4', 'X.card = 5'),
                     'EighteenColours': STATEMENT.replace('      C.card = sInf (ColourCounts 37)\n', '      C.card = 18\n'),
                     'ThirtyNinePoints': STATEMENT.replace('Fin 38', 'Fin 39')}
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
        result['status'] = 'PARENT_MCDSQS38_BINDING_REBUILD_AND_FRESH_KERNEL_PASS'
        result['limits'] = ('mcDSQS(38) only. Lean and leanchecker share one toolchain, not an independent kernel or Comparator. '
                            'The raw-certificate binding is checked by this driver outside Lean. Priority and novelty are separate.')
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
