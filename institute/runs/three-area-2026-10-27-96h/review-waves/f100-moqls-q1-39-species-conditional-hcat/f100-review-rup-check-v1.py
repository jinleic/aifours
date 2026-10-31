#!/usr/bin/env python3
"""f100 review: reviewer-authored DRUP (RUP-addition / deletion) proof checker, standard library only.

Semantics: a proof line "l1 ... lk 0" is accepted only if unit propagation on the current clause
database together with the negation of {l1..lk} yields a conflict (reverse unit propagation).  A
line "d l1 ... lk 0" deletes one matching clause.  The proof is VERIFIED only if an empty clause is
accepted; trailing lines after that are counted and reported.  Strict parsing: DIMACS header counts
must match; every literal must be nonzero with |lit| <= declared variables; proof lines must be
integer sequences terminated by 0.  Two-watched-literal propagation with a fresh assignment per check
(with every variable unassigned, any watch pair satisfies the watch invariant, so watches persist).
No author code is imported or consulted at run time.
"""
import argparse, hashlib, json, pathlib, sys, time


class CheckError(Exception):
    pass


def parse_cnf(data):
    text = data.decode('ascii')
    lines = text.split('\n')
    if lines[-1] != '':
        raise CheckError('cnf: no trailing newline')
    hdr = lines[0].split()
    if len(hdr) != 4 or hdr[:2] != ['p', 'cnf']:
        raise CheckError('cnf: header')
    nv, nc = int(hdr[2]), int(hdr[3])
    clauses = []
    for l in lines[1:-1]:
        toks = l.split()
        if not toks or toks[-1] != '0':
            raise CheckError('cnf: clause line')
        lits = [int(t) for t in toks[:-1]]
        if any(v == 0 or abs(v) > nv for v in lits):
            raise CheckError('cnf: literal range')
        clauses.append(lits)
    if len(clauses) != nc:
        raise CheckError('cnf: clause count %d != header %d' % (len(clauses), nc))
    return nv, clauses


def parse_proof(data, nv):
    text = data.decode('ascii')
    lines = text.split('\n')
    if lines[-1] != '':
        raise CheckError('proof: no trailing newline')
    steps = []
    for l in lines[:-1]:
        toks = l.split()
        if not toks:
            raise CheckError('proof: blank line')
        delete = False
        if toks[0] == 'd':
            delete = True
            toks = toks[1:]
        if not toks or toks[-1] != '0':
            raise CheckError('proof: line not 0-terminated: %r' % l)
        lits = [int(t) for t in toks[:-1]]
        if any(v == 0 or abs(v) > nv for v in lits):
            raise CheckError('proof: literal range in %r' % l)
        steps.append((delete, lits))
    return steps


class Checker:
    def __init__(self, nv):
        self.nv = nv
        self.val = [0] * (2 * nv + 2)        # per literal index: 1 true, -1 false, 0 unassigned
        self.watches = [[] for _ in range(2 * nv + 2)]
        self.clauses = []                     # clause id -> list of literal indices (or None if deleted)
        self.units = {}                       # literal index -> count of active unit clauses
        self.empty = 0

    @staticmethod
    def idx(lit):
        return 2 * abs(lit) + (1 if lit < 0 else 0)

    def add(self, lits):
        li = []
        seen = set()
        for v in lits:
            i = self.idx(v)
            if i not in seen:
                seen.add(i); li.append(i)
        cid = len(self.clauses)
        self.clauses.append(li)
        if len(li) == 0:
            self.empty += 1
        elif len(li) == 1:
            self.units[li[0]] = self.units.get(li[0], 0) + 1
        else:
            self.watches[li[0]].append(cid)
            self.watches[li[1]].append(cid)
        return cid

    def delete(self, lits):
        key = frozenset(self.idx(v) for v in lits)
        for cid in range(len(self.clauses) - 1, -1, -1):
            cl = self.clauses[cid]
            if cl is not None and frozenset(cl) == key:
                self.clauses[cid] = None
                if len(cl) == 1:
                    self.units[cl[0]] -= 1
                    if self.units[cl[0]] == 0:
                        del self.units[cl[0]]
                elif len(cl) == 0:
                    self.empty -= 1
                return True
        return False

    def rup(self, lits):
        """Return True iff unit propagation from (units + negation of lits) conflicts."""
        val = self.val; watches = self.watches; clauses = self.clauses
        trail = []
        conflict = False
        if self.empty:
            return True
        assumptions = list(self.units.keys()) + [self.idx(v) ^ 1 for v in lits]
        for i in assumptions:
            if val[i] == 1:
                continue
            if val[i] == -1:
                conflict = True; break
            val[i] = 1; val[i ^ 1] = -1; trail.append(i)
        qi = 0
        while not conflict and qi < len(trail):
            fl = trail[qi] ^ 1          # literal that became false
            qi += 1
            wl = watches[fl]
            keep = []
            n = len(wl)
            k = 0
            while k < n:
                cid = wl[k]; k += 1
                cl = clauses[cid]
                if cl is None:
                    continue              # deleted clause: drop watch
                if cl[0] == fl:
                    cl[0], cl[1] = cl[1], cl[0]
                other = cl[0]
                if val[other] == 1:
                    keep.append(cid); continue
                moved = False
                for m in range(2, len(cl)):
                    if val[cl[m]] != -1:
                        cl[1], cl[m] = cl[m], cl[1]
                        watches[cl[1]].append(cid)
                        moved = True
                        break
                if moved:
                    continue
                keep.append(cid)
                if val[other] == -1:
                    conflict = True
                    keep.extend(wl[k:])
                    break
                val[other] = 1; val[other ^ 1] = -1; trail.append(other)
            watches[fl] = keep
        for i in trail:
            val[i] = 0; val[i ^ 1] = 0
        return conflict


def check(cnf_bytes, proof_bytes):
    nv, clauses = parse_cnf(cnf_bytes)
    steps = parse_proof(proof_bytes, nv)
    ck = Checker(nv)
    for cl in clauses:
        ck.add(cl)
    res = {'variables': nv, 'formula_clauses': len(clauses), 'proof_lines': len(steps), 'additions': 0, 'deletions': 0,
           'deletion_misses': 0, 'rup_verified': 0, 'first_failure': None, 'empty_clause_verified': False,
           'lines_after_empty': 0, 'max_lemma_len': 0}
    for n, (delete, lits) in enumerate(steps, 1):
        if res['empty_clause_verified']:
            res['lines_after_empty'] += 1
            continue
        if delete:
            res['deletions'] += 1
            if not ck.delete(lits):
                res['deletion_misses'] += 1
            continue
        res['additions'] += 1
        res['max_lemma_len'] = max(res['max_lemma_len'], len(lits))
        if ck.rup(lits):
            res['rup_verified'] += 1
            ck.add(lits)
            if not lits:
                res['empty_clause_verified'] = True
        else:
            res['first_failure'] = {'line': n, 'lemma': lits}
            break
    res['verdict'] = 'VERIFIED' if (res['empty_clause_verified'] and res['first_failure'] is None) else 'NOT_VERIFIED'
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cnf', required=True)
    ap.add_argument('--proof', required=True)
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    out = pathlib.Path(a.output)
    if out.exists():
        raise SystemExit('refusing to overwrite ' + str(out))
    cb = pathlib.Path(a.cnf).read_bytes(); pb = pathlib.Path(a.proof).read_bytes()
    t0 = time.monotonic()
    try:
        res = check(cb, pb)
    except CheckError as e:
        res = {'verdict': 'NOT_VERIFIED', 'parse_error': str(e)}
    res.update({'cnf': a.cnf, 'cnf_sha256': hashlib.sha256(cb).hexdigest(), 'cnf_bytes': len(cb), 'proof': a.proof,
                'proof_sha256': hashlib.sha256(pb).hexdigest(), 'proof_bytes': len(pb), 'elapsed_seconds': time.monotonic() - t0,
                'checker_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()})
    with out.open('x', encoding='utf-8') as h:
        json.dump(res, h, indent=1); h.write('\n')
    print(json.dumps(res))


if __name__ == '__main__':
    main()
