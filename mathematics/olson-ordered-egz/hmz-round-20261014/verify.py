#!/usr/bin/env python3
"""Frozen exact finite-certificate and universal-statement acceptance checker."""
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
LEAN_CWD = Path('/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/lean-verify')
GOAL = '''(∀ (G : Type) [Group G] [Fintype G] (xs : List G),
  xs.length = 2 * Fintype.card G - 1 →
  ∃ ys : List G, ys.Sublist xs ∧ ys.length = Fintype.card G ∧ ys.prod = 1)'''


def require(condition, message):
    if not condition:
        raise ValueError(message)


def strip_comments_strings(source):
    # Nested Lean comments are handled rather than trusted to a flat regex.
    out, index, depth, string = [], 0, 0, False
    while index < len(source):
        pair = source[index:index + 2]
        if depth:
            if pair == '/-':
                depth += 1
                index += 2
            elif pair == '-/':
                depth -= 1
                index += 2
            else:
                index += 1
        elif string:
            if source[index] == '\\':
                index += 2
            elif source[index] == '"':
                string = False
                index += 1
            else:
                index += 1
        elif pair == '/-':
            depth = 1
            index += 2
        elif pair == '--':
            end = source.find('\n', index)
            index = len(source) if end < 0 else end
        elif source[index] == '"':
            string = True
            out.append(' ')
            index += 1
        else:
            out.append(source[index])
            index += 1
    require(depth == 0 and not string, 'Unclosed Lean comment or string')
    return ''.join(out)


def finite_certificate(path):
    data = json.loads(path.read_text())
    table, identity, sequence = data['table'], data['identity'], data['sequence']
    n = len(table)
    require(n > 0, 'Group is empty')
    require(type(identity) is int and 0 <= identity < n, 'Invalid identity')
    require(all(isinstance(row, list) and len(row) == n and
                all(type(x) is int and 0 <= x < n for x in row) for row in table),
            'Table not closed square integer table')
    require(all(table[identity][a] == a and table[a][identity] == a for a in range(n)),
            'Identity law failed')
    require(all(any(table[a][b] == identity and table[b][a] == identity
                    for b in range(n)) for a in range(n)), 'Inverse law failed')
    require(all(table[table[a][b]][c] == table[a][table[b][c]]
                for a, b, c in itertools.product(range(n), repeat=3)),
            'Associativity failed')
    require(len(sequence) == 2 * n - 1, 'Sequence length differs from 2|G|-1')
    require(all(type(a) is int and 0 <= a < n for a in sequence), 'Invalid sequence entry')
    subsets = math.comb(len(sequence), n)
    require(subsets <= 100_000_000, 'Raw enumeration safety cap exceeded; not accepted')
    counts = [0] * n
    for indices in itertools.combinations(range(len(sequence)), n):
        product = identity
        for index in indices:
            product = table[product][sequence[index]]
        counts[product] += 1
        require(product != identity, 'Ordered identity witness exists: ' + repr(indices))
    require(sum(counts) == subsets, 'Raw subset enumeration count mismatch')
    layers = [{identity}] + [set() for _ in range(n)]
    for a in sequence:
        for k in range(n, 0, -1):
            layers[k].update(table[g][a] for g in layers[k - 1])
    require(identity not in layers[n], 'DP found ordered identity product')
    require(layers[n] == {a for a, count in enumerate(counts) if count}, 'Raw/DP disagreement')
    return {'group_order': n, 'sequence_length': len(sequence),
            'subsets_checked': subsets, 'product_histogram': counts,
            'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    claims_path = ROOT / 'claims.json'
    require(claims_path.is_file(), 'No claims.json: no resolution submitted')
    claims = json.loads(claims_path.read_text())
    require(claims.get('full_goal_solved') is True, 'Exact full goal not claimed solved')
    route = claims.get('route')
    require(route in ('proof', 'counterexample'), 'Invalid full-resolution route')
    proof = ROOT / 'proof.md'
    require(proof.is_file() and len(proof.read_text().strip()) > 100, 'Missing written proof')
    receipt = {'route': route, 'scope_review_required': True}
    if route == 'counterexample':
        receipt['certificate'] = finite_certificate(ROOT / 'certificate.json')
    formal = ROOT / 'Formal.lean'
    require(formal.is_file(), 'Full resolution requires Formal.lean')
    source = formal.read_text()
    code = strip_comments_strings(source)
    forbidden = r'\b(?:sorry|admit|axiom|native_decide|ofReduceBool|unsafe|opaque|implemented_by|extern|run_cmd|elab|macro|initialize|addDecl|skipKernelTC|partial)\b|#eval'
    require(re.search(forbidden, code) is None, 'Forbidden proof mechanism')
    theorem = 'Olson.ordered_egz' if route == 'proof' else 'Olson.ordered_egz_false'
    statement = GOAL if route == 'proof' else '(¬ ' + GOAL + ')'
    checked = ROOT / 'FrozenScopeCheck.lean'
    checked.write_text(source + '\n\nexample : ' + statement + ' := ' + theorem + '\n#print ' + theorem + '\n#print axioms ' + theorem + '\n')
    environment = os.environ.copy()
    environment['PATH'] = str(Path.home() / '.elan/bin') + ':' + environment.get('PATH', '')
    result = subprocess.run(['lake', 'env', 'lean', str(checked)], cwd=LEAN_CWD,
                            env=environment, capture_output=True, text=True, timeout=600)
    (ROOT / 'scope-check.log').write_text(result.stdout + result.stderr)
    require(result.returncode == 0, 'Lean exact-scope check failed; see scope-check.log')
    for axiom_list in re.findall(r'depends on axioms:\s*\[([^\]]*)\]', result.stdout):
        axioms = {a.strip() for a in axiom_list.split(',') if a.strip()}
        require(axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, 'Unapproved axiom: ' + repr(axioms))
    receipt['formal_sha256'] = hashlib.sha256(formal.read_bytes()).hexdigest()
    receipt['lean_exit_code'] = result.returncode
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.TimeoutExpired) as error:
        print('NOT ACCEPTED: ' + str(error), file=sys.stderr)
        raise SystemExit(1)
