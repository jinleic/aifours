#!/usr/bin/env python3
"""Reviewer-authored (f91) RUP checker for ASCII DRUP traces. Standard library only.

Semantics: every non-deletion line must be a clause C such that unit
propagation on (current database) + (negation of C) yields a conflict.
Deletion lines are counted but NOT applied (sound for a refutation: every
lemma remains implied by the original formula).  The last line must be the
empty clause and must itself pass RUP.  No author checker code is imported.
"""
import hashlib, json, pathlib, sys

def parse_cnf(b):
    hdr = None; F = []
    for line in b.decode('ascii').splitlines():
        z = line.split()
        if not z or z[0] == 'c': continue
        if z[0] == 'p':
            if hdr is not None or len(z) != 4 or z[1] != 'cnf': raise ValueError('header')
            hdr = (int(z[2]), int(z[3])); continue
        if hdr is None: raise ValueError('clause before header')
        q = list(map(int, z))
        if not q or q[-1] != 0 or 0 in q[:-1] or any(abs(l) > hdr[0] for l in q[:-1]): raise ValueError('bad clause')
        if len(q) == 1: raise ValueError('empty clause in input')
        F.append(q[:-1])
    if hdr is None or len(F) != hdr[1]: raise ValueError('clause count')
    return hdr[0], F

def parse_proof(b, n):
    if not b or not b.endswith(b'\n'): raise ValueError('proof not newline-terminated')
    steps = []
    for line in b.decode('ascii').splitlines():
        z = line.split()
        if not z: raise ValueError('blank proof line')
        d = z[0] == 'd'
        q = list(map(int, z[1:] if d else z))
        if not q or q[-1] != 0 or 0 in q[:-1] or any(abs(l) > n for l in q[:-1]): raise ValueError('bad proof line')
        steps.append((d, q[:-1]))
    if steps[-1] != (False, []): raise ValueError('final line is not the empty clause')
    return steps

class DB:
    def __init__(self, n, F):
        self.n = n; self.C = []; self.occ = {}; self.units = []
        for c in F: self.add(c)
    def add(self, c):
        i = len(self.C); self.C.append(c)
        for l in c: self.occ.setdefault(l, []).append(i)
        if len(c) == 1: self.units.append(c[0])
    def rup(self, lemma):
        val = [0] * (self.n + 1); trail = []
        def assign(l):
            v = abs(l); s = 1 if l > 0 else -1
            if val[v] == -s: return False
            if val[v] == 0: val[v] = s; trail.append(l)
            return True
        for l in lemma:
            if not assign(-l): return True          # tautological lemma: trivially implied
        for l in self.units:
            if not assign(l): return True
        i = 0
        while i < len(trail):
            f = -trail[i]; i += 1                    # literal f just became false
            for ci in self.occ.get(f, ()):
                c = self.C[ci]; un = None; sat = False; cnt = 0
                for l in c:
                    s = val[abs(l)]
                    if s == 0: cnt += 1; un = l
                    elif (s > 0) == (l > 0): sat = True; break
                if sat: continue
                if cnt == 0: return True             # conflict
                if cnt == 1 and not assign(un): return True
        return False

def verify(cnf_bytes, proof_bytes):
    n, F = parse_cnf(cnf_bytes); steps = parse_proof(proof_bytes, n); db = DB(n, F)
    added = deleted = 0
    for k, (d, c) in enumerate(steps, 1):
        if d: deleted += 1; continue
        if not db.rup(c): raise ValueError('step %d is not RUP: %r' % (k, c))
        added += 1
        if c: db.add(c)
    return {'variables': n, 'input_clauses': len(F), 'proof_lines': len(steps), 'rup_additions': added, 'deletions_ignored': deleted}

if __name__ == '__main__':
    cnf, proof = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    C, P = cnf.read_bytes(), proof.read_bytes()
    res = {'cnf': str(cnf), 'cnf_sha256': hashlib.sha256(C).hexdigest(), 'cnf_bytes': len(C),
           'proof': str(proof), 'proof_sha256': hashlib.sha256(P).hexdigest(), 'proof_bytes': len(P)}
    try:
        res['counts'] = verify(C, P); res['result'] = 'PASS_ALL_ADDITIONS_RUP_FINAL_EMPTY'
    except (ValueError, UnicodeError) as e:
        res['result'] = 'REJECT'; res['reason'] = str(e)
    res['checker_sha256'] = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(res, indent=1))
    sys.exit(0 if res['result'].startswith('PASS') else 1)
