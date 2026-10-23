#!/usr/bin/env python3
"""Producer of the outer cell certificate for one facet cone Sigma_u, u = (FI, FJ)
(floating-point search only; every leaf is re-checked by cert_cells.py in arb).

Adapted from code/bnb_produce.py.  Frozen scheme unchanged (README "FROZEN: outer cell certificate
scheme"): tree of exact edge bisections from conv(n*, P_sigma/3 : sigma(FI) != FJ); leaves
  ['C']                     all 5 vertices in the box |n_k - 1/9| <= r1 (k = 00,01,10,11);
  ['D', y_hex[18], mu_hex[9][4]]   U_y(v) < L* at the 5 vertices, a_u from the rational mu0^u.
Producer heuristics (allowed to change): per-cell multiplier choice y (reuse of the parent's leaf
data, then the dual optimum at the centroid, then a minimax refinement max_lambda min_y over the
vertex weights), mu0^u = exp(theta^u) of the float inner optimum, split rule (longest edge in the
metric sum_u (dn^u)^2 / n^u_mid, or Frobenius).  Vertices are carried exactly as integers over
9 * 2^PBITS so that central decisions and replayed midpoints agree with the checker.

Usage: bnb_produce.py FI FJ R1 OUT.json [--workdir DIR] [--log LOG] [--time-limit SEC] ...
  Work is split into 2^K top-level job cells (K = --top-depth); each finished job is stored in
  DIR/job_XXX.json, an unfinished one in DIR/job_XXX.partial.json (explicit DFS stack + emitted
  preorder prefix), refreshed every --save-every seconds; rerunning the same command resumes.
  OUT.json is assembled when every job is finished.  Exit codes: 0 done, 3 time limit (resumable).
  --bfs-profile: level-by-level profiling run (no certificate), location histograms per level.
"""
import argparse
import itertools
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fastdual as fd  # noqa: E402

PBITS = 240
ONE9 = 1 << PBITS          # numerator of 1/9; a coordinate N stands for N / SCALE
SCALE = 9 * ONE9
THIRD = 3 * ONE9
LSTAR = fd.LSTAR
EDGE_PAIRS = [(i, j) for i in range(5) for j in range(i + 1, 5)]


def nine_int(p):
    n1, n2, n3, n4 = p
    return (n1, n2, THIRD - n1 - n2, n3, n4, THIRD - n3 - n4, THIRD - n1 - n3, THIRD - n2 - n4,
            n1 + n2 + n3 + n4 - THIRD)


def cell_v9(cell):
    v = np.array([[x / SCALE for x in nine_int(p)] for p in cell])
    assert (v >= 0).all()
    return v


def root_cell(fi, fj):
    perms = [s for s in itertools.permutations(range(3)) if s[fi] != fj]
    assert len(perms) == 4
    return [(ONE9,) * 4] + [tuple(THIRD * int(c) for c in (s[0] == 0, s[0] == 1, s[1] == 0, s[1] == 1))
                            for s in perms]


def midpoint(a, b):
    out = []
    for x, y in zip(a, b):
        s = x + y
        assert s & 1 == 0, 'PBITS exhausted'
        out.append(s >> 1)
    return tuple(out)


def split_cell(cell, i, j):
    m = midpoint(cell[i], cell[j])
    c1 = list(cell); c1[i] = m
    c2 = list(cell); c2[j] = m
    return c1, c2


class Producer:
    def __init__(self, args):
        self.a = args
        r1 = Fraction(args.r1)
        self.r1n, self.r1d = r1.numerator, r1.denominator
        self.safety = args.safety
        self.st = self.new_stats()

    @staticmethod
    def new_stats():
        return {'evaluated': 0, 'dual_new': 0, 'dual_reused': 0, 'central': 0, 'splits': 0,
                'maxdepth': 0, 'min_margin': None, 'minimax_calls': 0, 'minimax_wins': 0,
                'qp_split': 0, 'dual_solves': 0, 'fail_numeric': 0,
                'h_eval_r': {}, 'h_acc_r': {}, 'h_eval_n': {}, 'h_acc_n': {}, 'h_depth': {},
                'acc_min_r': None, 'acc_min_n': None, 't_eval': 0.0}

    # ---------------- geometry helpers ----------------
    def central(self, cell):
        lim = self.r1n * SCALE
        return all(abs(x - ONE9) * self.r1d <= lim for p in cell for x in p)

    def split_edge(self, V9):
        best, bi, bj = -1.0, 0, 1
        for (i, j) in EDGE_PAIRS:
            d = V9[i] - V9[j]
            if self.a.split == 'euclid':
                L = float(d @ d)
            else:
                mid = 0.5 * (V9[i] + V9[j])
                L = float(np.sum(np.where(mid > 0, d * d / np.where(mid > 0, mid, 1.0), 0.0)))
            if L > best:
                best, bi, bj = L, i, j
        return bi, bj

    @staticmethod
    def hist_add(h, key):
        k = str(key)
        h[k] = h.get(k, 0) + 1

    def loc_bins(self, V9):
        c = V9.mean(axis=0)
        r = float(np.linalg.norm(c - 1.0 / 9))
        rb = int(math.floor(math.log2(r))) if r > 0 else -99
        mn = float(c.min())
        nb = int(math.floor(math.log10(mn))) if mn > 0 else -99
        return r, mn, rb, nb

    # ---------------- per-cell work ----------------
    def leaf_from(self, y, th):
        mu = np.exp(th)
        a = fd.a_from_mu(fd.zmat(y), mu)
        return a, np.array(y, float), mu

    @staticmethod
    def hexleaf(y, mu):
        return fd.to_hex(y), [fd.to_hex(mu[u]) for u in range(9)]

    def qp_simplex(self, u, Q, lam, eps):
        """max_l u.l - 1/2 (l-lam)^T Q (l-lam) over {sum l = 1, l >= eps}; active-set enumeration."""
        best = None
        Qlam = Q @ lam
        for mask in range(1, 32):
            A = [i for i in range(5) if mask >> i & 1]
            N = [i for i in range(5) if not mask >> i & 1]
            nA = len(A)
            K = np.zeros((nA + 1, nA + 1))
            K[:nA, :nA] = Q[np.ix_(A, A)]
            K[:nA, nA] = 1.0
            K[nA, :nA] = 1.0
            rhs = np.zeros(nA + 1)
            rhs[:nA] = u[A] + Qlam[A] - (Q[np.ix_(A, N)].sum(axis=1) * eps if N else 0.0)
            rhs[nA] = 1.0 - eps * len(N)
            try:
                sol = np.linalg.solve(K, rhs)
            except np.linalg.LinAlgError:
                sol = np.linalg.lstsq(K, rhs, rcond=None)[0]
            l = np.full(5, eps)
            l[A] = sol[:nA]
            if (l < eps - 1e-13).any():
                continue
            nu = sol[nA]
            gr = u - Q @ (l - lam)
            if N and (gr[N] > nu + 1e-10 * (1 + abs(nu))).any():
                continue
            f = float(u @ l - 0.5 * (l - lam) @ Q @ (l - lam))
            if best is None or f > best[0]:
                best = (f, l)
        return best

    def evaluate(self, cell, inh, depth):
        """Returns ('C',) | ('D', yhex, muhex, margin, reused) | ('S', i, j, child_inh)."""
        st = self.st
        st['maxdepth'] = max(st['maxdepth'], depth)
        if self.central(cell):
            st['central'] += 1
            return ('C',)
        t0 = time.perf_counter()
        st['evaluated'] += 1
        V9 = cell_v9(cell)
        Ev = fd.ent(V9)
        r, mn, rb, nb = self.loc_bins(V9)
        self.hist_add(st['h_eval_r'], rb)
        self.hist_add(st['h_eval_n'], nb)
        thr = LSTAR - self.safety
        cand = inh.get('cand') if inh else None
        if cand is not None:
            U = V9 @ cand[0] + Ev
            if U.max() < thr:
                st['dual_reused'] += 1
                self.accept_stats(r, mn, rb, nb, LSTAR - U.max(), depth, t0)
                return ('D',) + self.hexleaf(cand[1], cand[2]) + (LSTAR - U.max(), True)
        y0 = inh.get('y') if inh else None
        th0 = inh.get('th') if inh else None
        lam = np.full(5, 0.2)
        best = None
        y = th = None
        for it in range(self.a.minimax_iters + 1):
            nl = lam @ V9
            try:
                D, y, gres, th, mh, R, val, nit = fd.solve_dual(nl, y0, th0)
                st['dual_solves'] += 1
                if not np.isfinite(D) or not np.all(np.isfinite(y)):
                    raise FloatingPointError
                a, yq, muq = self.leaf_from(y, th)
            except (FloatingPointError, np.linalg.LinAlgError, ValueError):
                st['fail_numeric'] += 1
                break
            U = V9 @ a + Ev
            if not np.all(np.isfinite(U)):
                st['fail_numeric'] += 1
                break
            if best is None or U.max() < best[0]:
                best = (float(U.max()), a, yq, muq)
            if U.max() < thr:
                st['dual_new'] += 1
                if it > 0:
                    st['minimax_wins'] += 1
                self.accept_stats(r, mn, rb, nb, LSTAR - U.max(), depth, t0)
                return ('D',) + self.hexleaf(yq, muq) + (LSTAR - U.max(), False)
            if it == self.a.minimax_iters:
                break
            # quadratic model of phi(lambda) = min_y sum_v lambda_v U_y(v)
            st['minimax_calls'] += 1
            u = V9 @ val + Ev
            Cm = np.einsum('uk,uke->ue', mh, fd.C)
            G = V9 @ Cm
            H = ((nl[:, None, None] * R).reshape(144) @ fd.PH).reshape(18, 18)
            try:
                Q = G @ np.linalg.solve(H + 1e-13 * np.eye(18), G.T)
            except np.linalg.LinAlgError:
                break
            Q = 0.5 * (Q + Q.T)
            res = self.qp_simplex(u, Q, lam, self.a.lam_eps)
            if res is None:
                break
            phi, lam_new = res
            if phi > thr - self.a.qp_slack * max(0.0, float(u.max()) - phi):
                st['qp_split'] += 1
                break
            lam = lam_new
            y0, th0 = y, th
        # split
        i, j = self.split_edge(V9)
        st['splits'] += 1
        st['t_eval'] += time.perf_counter() - t0
        child = {'y': y if y is not None else y0, 'th': th if th is not None else th0,
                 'cand': (best[1], best[2], best[3]) if best is not None and self.a.reuse else None}
        return ('S', i, j, child)

    def accept_stats(self, r, mn, rb, nb, margin, depth, t0):
        st = self.st
        self.hist_add(st['h_acc_r'], rb)
        self.hist_add(st['h_acc_n'], nb)
        self.hist_add(st['h_depth'], depth)
        st['min_margin'] = margin if st['min_margin'] is None else min(st['min_margin'], margin)
        st['acc_min_r'] = r if st['acc_min_r'] is None else min(st['acc_min_r'], r)
        st['acc_min_n'] = mn if st['acc_min_n'] is None else min(st['acc_min_n'], mn)
        st['t_eval'] += time.perf_counter() - t0


# ---------------- serialisation of DFS state ----------------
def inh_to_json(inh):
    if not inh:
        return None
    out = {'y': None if inh.get('y') is None else [float(v) for v in inh['y']],
           'th': None if inh.get('th') is None else np.asarray(inh['th']).tolist(), 'cand': None}
    if inh.get('cand') is not None:
        a, yq, muq = inh['cand']
        out['cand'] = [[float(v) for v in a], [float(v) for v in yq], np.asarray(muq).tolist()]
    return out


def inh_from_json(d):
    if d is None:
        return None
    inh = {'y': None if d['y'] is None else np.array(d['y']),
           'th': None if d['th'] is None else np.array(d['th']), 'cand': None}
    if d['cand'] is not None:
        inh['cand'] = (np.array(d['cand'][0]), np.array(d['cand'][1]), np.array(d['cand'][2]))
    return inh


def cell_to_json(cell):
    return [[str(x) for x in p] for p in cell]


def cell_from_json(c):
    return [tuple(int(x) for x in p) for p in c]


def atomic_dump(obj, path):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, separators=(',', ':'))
    os.replace(tmp, path)


def now():
    return time.strftime('%Y-%m-%d %H:%M:%S %Z')


class Logger:
    def __init__(self, path):
        self.f = open(path, 'a') if path else None

    def __call__(self, obj):
        line = json.dumps(obj, separators=(',', ':'))
        print(line, flush=True)
        if self.f:
            self.f.write(line + '\n')
            self.f.flush()


def summary(st):
    keys = ['evaluated', 'dual_new', 'dual_reused', 'central', 'splits', 'maxdepth', 'min_margin',
            'minimax_calls', 'minimax_wins', 'qp_split', 'dual_solves', 'fail_numeric', 'acc_min_r',
            'acc_min_n']
    out = {k: st[k] for k in keys}
    out['ms_per_eval'] = round(1e3 * st['t_eval'] / max(1, st['evaluated']), 3)
    return out


def merge_stats(tot, st):
    for k, v in st.items():
        if k.startswith('h_'):
            for kk, vv in v.items():
                tot[k][kk] = tot[k].get(kk, 0) + vv
        elif k in ('maxdepth',):
            tot[k] = max(tot[k], v)
        elif k in ('min_margin', 'acc_min_r', 'acc_min_n'):
            if v is not None:
                tot[k] = v if tot[k] is None else min(tot[k], v)
        else:
            tot[k] += v


# ---------------- BFS profiling ----------------
def bfs_profile(P, root, log, tlimit, cap):
    t0 = time.time()
    front = [(root, None)]
    depth = 0
    while front and time.time() - t0 < tlimit:
        nxt = []
        P.st = P.new_stats()
        h_open_r, h_open_n = {}, {}
        for cell, inh in front:
            res = P.evaluate(cell, inh, depth)
            if res[0] == 'S':
                c1, c2 = split_cell(cell, res[1], res[2])
                nxt.append((c1, res[3])); nxt.append((c2, res[3]))
                V9 = cell_v9(cell)
                _, _, rb, nb = P.loc_bins(V9)
                P.hist_add(h_open_r, rb); P.hist_add(h_open_n, nb)
            if time.time() - t0 > tlimit:
                break
        log({'t': now(), 'elapsed_s': round(time.time() - t0, 1), 'level': depth, 'nodes': len(front),
             **summary(P.st), 'split_r_hist': h_open_r, 'split_nmin_hist': h_open_n,
             'acc_r_hist': P.st['h_acc_r'], 'acc_nmin_hist': P.st['h_acc_n']})
        front = nxt
        depth += 1
        if len(front) > cap:
            log({'t': now(), 'stop': 'frontier cap', 'frontier': len(front)})
            break
    log({'t': now(), 'stop': 'time' if front else 'done', 'frontier': len(front), 'level': depth})


# ---------------- production (DFS jobs) ----------------
def top_jobs(P, root, K):
    """Fixed top tree of depth K: returns (top preorder split list, job cells in preorder)."""
    top, jobs = [], []

    def rec(cell, d):
        if d == K:
            top.append(['J', len(jobs)])
            jobs.append(cell)
            return
        i, j = P.split_edge(cell_v9(cell))
        top.append(['S', i, j])
        c1, c2 = split_cell(cell, i, j)
        rec(c1, d + 1)
        rec(c2, d + 1)

    rec(root, 0)
    return top, jobs


def run_job(P, idx, cell, wd, log, deadline, save_every, prog_every):
    fin = os.path.join(wd, f'job_{idx:03d}.json')
    part = os.path.join(wd, f'job_{idx:03d}.partial.json')
    if os.path.exists(part):
        s = json.load(open(part))
        nodes = s['nodes']
        stack = [(cell_from_json(c), inh_from_json(h), d) for c, h, d in s['stack']]
        P.st = s['stats']
        prev_runtime = s['runtime_s']
        log({'t': now(), 'job': idx, 'event': 'resume', 'nodes': len(nodes), 'open': len(stack)})
    else:
        nodes, stack, prev_runtime = [], [(cell, None, 0)], 0.0
        P.st = P.new_stats()
    t0 = time.time()
    t_save = t_prog = t0
    while stack:
        c, inh, d = stack.pop()
        res = P.evaluate(c, inh, d)
        if res[0] == 'C':
            nodes.append(['C'])
        elif res[0] == 'D':
            nodes.append(['D', res[1], res[2]])
        else:
            nodes.append(['S', res[1], res[2]])
            c1, c2 = split_cell(c, res[1], res[2])
            stack.append((c2, res[3], d + 1))
            stack.append((c1, res[3], d + 1))
        tn = time.time()
        if tn - t_prog > prog_every:
            t_prog = tn
            log({'t': now(), 'job': idx, 'open': len(stack), 'nodes': len(nodes),
                 'runtime_s': round(prev_runtime + tn - t0, 1), **summary(P.st),
                 'eval_r': P.st['h_eval_r'], 'acc_r': P.st['h_acc_r'], 'eval_n': P.st['h_eval_n'],
                 'acc_n': P.st['h_acc_n']})
        if stack and (tn - t_save > save_every or tn > deadline):
            t_save = tn
            atomic_dump({'job': idx, 'nodes': nodes, 'stats': P.st, 'runtime_s': prev_runtime + tn - t0,
                         'stack': [(cell_to_json(cc), inh_to_json(hh), dd) for cc, hh, dd in stack]}, part)
            if tn > deadline:
                log({'t': now(), 'job': idx, 'event': 'time limit, partial saved', 'nodes': len(nodes),
                     'open': len(stack)})
                return False
    rt = prev_runtime + time.time() - t0
    atomic_dump({'job': idx, 'nodes': nodes, 'stats': P.st, 'runtime_s': rt}, fin)
    if os.path.exists(part):
        os.replace(part, part + '.done')
    log({'t': now(), 'job': idx, 'event': 'job done', 'nodes': len(nodes), 'runtime_s': round(rt, 1),
         **summary(P.st)})
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('fi', type=int)
    ap.add_argument('fj', type=int)
    ap.add_argument('r1')
    ap.add_argument('out')
    ap.add_argument('--workdir', default=None)
    ap.add_argument('--log', default=None)
    ap.add_argument('--safety', type=float, default=5e-12)
    ap.add_argument('--split', choices=['emetric', 'euclid'], default='emetric')
    ap.add_argument('--minimax-iters', type=int, default=3)
    ap.add_argument('--lam-eps', type=float, default=1e-3)
    ap.add_argument('--qp-slack', type=float, default=0.0)
    ap.add_argument('--no-reuse', dest='reuse', action='store_false')
    ap.add_argument('--top-depth', type=int, default=5)
    ap.add_argument('--time-limit', type=float, default=1500.0)
    ap.add_argument('--save-every', type=float, default=300.0)
    ap.add_argument('--progress-every', type=float, default=30.0)
    ap.add_argument('--bfs-profile', action='store_true')
    ap.add_argument('--frontier-cap', type=int, default=400000)
    args = ap.parse_args()
    np.seterr(all='ignore')
    P = Producer(args)
    log = Logger(args.log)
    root = root_cell(args.fi, args.fj)
    cfg = {k: v for k, v in vars(args).items()}
    log({'t': now(), 'event': 'start', 'cfg': cfg, 'pid': os.getpid()})
    if args.bfs_profile:
        bfs_profile(P, root, log, args.time_limit, args.frontier_cap)
        return 0
    wd = args.workdir or (os.path.splitext(args.out)[0] + '.work')
    os.makedirs(wd, exist_ok=True)
    topf = os.path.join(wd, 'top.json')
    if os.path.exists(topf):
        T = json.load(open(topf))
        top, jobs = T['top'], [cell_from_json(c) for c in T['jobs']]
    else:
        top, jobs = top_jobs(P, root, args.top_depth)
        atomic_dump({'facet': [args.fi, args.fj], 'top_depth': args.top_depth, 'top': top,
                     'jobs': [cell_to_json(c) for c in jobs]}, topf)
    t_start = time.time()
    deadline = t_start + args.time_limit
    for idx, cell in enumerate(jobs):
        if os.path.exists(os.path.join(wd, f'job_{idx:03d}.json')):
            continue
        if time.time() > deadline:
            log({'t': now(), 'event': 'time limit before job', 'job': idx})
            return 3
        if not run_job(P, idx, cell, wd, log, deadline, args.save_every, args.progress_every):
            return 3
    # assemble
    tree, tot, rt = [], Producer.new_stats(), 0.0
    for node in top:
        if node[0] == 'S':
            tree.append(node)
        else:
            J = json.load(open(os.path.join(wd, f"job_{node[1]:03d}.json")))
            tree.extend(J['nodes'])
            merge_stats(tot, J['stats'])
            rt += J['runtime_s']
    stats = summary(tot)
    stats['top_splits'] = sum(1 for n in top if n[0] == 'S')
    stats['dual_leaves'] = sum(1 for n in tree if n[0] == 'D')
    stats['central_leaves'] = sum(1 for n in tree if n[0] == 'C')
    stats['producer_runtime_s'] = round(rt, 1)
    stats['h_acc_r'], stats['h_acc_n'], stats['h_depth'] = tot['h_acc_r'], tot['h_acc_n'], tot['h_depth']
    cert = {'facet': [args.fi, args.fj], 'r0': args.r1, 'safety': args.safety,
            'producer': {k: cfg[k] for k in ('split', 'minimax_iters', 'lam_eps', 'qp_slack', 'reuse',
                                             'top_depth')},
            'stats': stats, 'tree': tree}
    atomic_dump(cert, args.out)
    log({'t': now(), 'event': 'assembled', 'out': args.out, **{k: stats[k] for k in
         ('dual_leaves', 'central_leaves', 'producer_runtime_s', 'min_margin', 'maxdepth')}})
    return 0


if __name__ == '__main__':
    sys.exit(main())
