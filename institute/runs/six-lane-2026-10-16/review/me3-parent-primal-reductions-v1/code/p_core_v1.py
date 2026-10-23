"""ME3 parent desk (ME3ParentPrimal), library v1: exact coverage + strict ball evaluator for primal chart P.

Parent-authored from the definitions. Imports nothing from the worker lane; uses only python-flint (Arb) balls and
Python Fractions. FORMAT DEPENDENCY (read from producer source cert_primal_v3.py, sha b541a8c5...f213, and the frozen
spec): leaf line "<cell> <path|-> <OUTCOME>\\n", cells numbered r-major then w then phi, path bits 0 = lower half of
the split dimension, split dimension = argmax width*weight (ties -> lowest index), exact rational midpoint,
depth-first order with child 0 first.

Mathematics (derived in AUDIT-v1.md section P; every formula below was re-derived by the parent):
  D2 extreme ray (real pole 1, pair -(1+delta) +- i w, r = delta/w, tau = phi/w):
     f(t) = e^{-t} h(t),  h(t) = 1 - e^{-delta(t-tau)} (cos w(t-tau) + r sin w(t-tau)).
  cos x + r sin x = Re[(1 - i r) e^{i x}]  =>  h(t) = 1 - Re[c e^{-(delta - i w) t}],  c = (1 - i r) e^{(r - i) phi}.
  m_k = int_0^inf t^k f dt = k! (1 - Re[c zeta^{k+1}]),  zeta = 1/(1 + r w - i w)   (Re(1 + delta - i w) > 0).
  a_k := m_k/k! = 1 - Re P_k,  P_k := c zeta^{k+1};   1 + S = m0 m2/m1^2 = 2 a0 a2/a1^2.
  G := 2 a0 a2 - (1+T) a1^2;  if a1 != 0 then S > T <=> G > 0.
  d_r log c = phi + (r - i)/(1 + r^2), d_w log c = 0, d_phi log c = r - i;
  d_r log zeta = -w zeta, d_w log zeta = -(r - i) zeta, d_phi log zeta = 0.
  With L_k := phi + (r - i)/(1 + r^2) - (k+1) w zeta and Lam_{k,x} := d_x log P_k:
     Lam_{k,r} = L_k,  Lam_{k,w} = -(k+1)(r - i) zeta,  Lam_{k,phi} = r - i,   d_x a_k = -Re(P_k Lam_{k,x}).
  a_k' := d_r a_k = -Re(P_k L_k).  D := a0' a1 a2 + a0 a1 a2' - 2 a0 a1' a2 = a0 a1 a2 * d_r log(1 + S).
  d_x a_k' = -Re(P_k [Lam_{k,x} L_k + d_x L_k]),  d_r L_k = (1 - i r)^{-2} + (k+1) w^2 zeta^2,
     d_w L_k = -(k+1) zeta^2,  d_phi L_k = 1.
  Mean-value form on a box B with exact centre m and half-widths h:  F(B) is enclosed by
     F(m) + sum_j dF_j(B) * [-h_j, h_j],  valid for C^1 F because F(x) - F(m) = int_0^1 grad F(m + s(x-m)).(x-m) ds.
  INFEAS rule (domain phi_lo > pi, r_lo > 0): g_{r_lo}(phi_lo) = e^{r_lo phi_lo}(cos phi_lo - r_lo sin phi_lo) > 1.
"""
from fractions import Fraction
import flint
from flint import arb, acb, fmpq


def qa(x):
    """Ball containing the exact rational x (outward rounding by Arb)."""
    return arb(fmpq(x.numerator, x.denominator))


def ivb(lo, hi):
    """Ball containing the exact rational interval [lo, hi]."""
    return qa(lo).union(qa(hi))


def symb(h):
    """Ball containing [-h, h] for an exact rational h >= 0."""
    a = qa(h)
    return (-a).union(a)


def parse_q(s):
    s = str(s).strip()
    if "/" in s:
        a, b = s.split("/")
        return Fraction(int(a), int(b))
    return Fraction(int(s))


class Geometry:
    """Exact cell boxes, split rule and DFS-order complete-prefix-code coverage check."""

    def __init__(self, spec):
        names = ("r", "w", "phi")
        self.region = [(parse_q(spec["region"][k][0]), parse_q(spec["region"][k][1])) for k in names]
        self.nsplit = [int(spec["initial_split"][k]) for k in names]
        self.weights = [parse_q(x) for x in spec["split_weights"]]
        self.max_depth = int(spec["max_depth"])
        self.ncells = self.nsplit[0] * self.nsplit[1] * self.nsplit[2]
        self.cur = -1
        self.stack = []
        self.cells_seen = 0
        self.bad_cell = False

    def cell_box(self, ci):
        n0, n1, n2 = self.nsplit
        i, rem = divmod(ci, n1 * n2)
        j, k = divmod(rem, n2)
        idx = (i, j, k)
        out = []
        for d in range(3):
            lo, hi = self.region[d]
            n = self.nsplit[d]
            out.append((lo + (hi - lo) * Fraction(idx[d], n), lo + (hi - lo) * Fraction(idx[d] + 1, n)))
        return tuple(out)

    def split(self, box):
        sc = [(box[d][1] - box[d][0]) * self.weights[d] for d in range(3)]
        best = 0
        for d in (1, 2):
            if sc[d] > sc[best]:
                best = d
        lo, hi = box[best]
        mid = (lo + hi) / 2
        b0 = list(box)
        b1 = list(box)
        b0[best] = (lo, mid)
        b1[best] = (mid, hi)
        return tuple(b0), tuple(b1)

    def feed(self, ci, path):
        """Consume one leaf (cell index, path string; '' = root).
        Returns (box or None, list of error strings). A box is returned only when the leaf itself is a correct next
        leaf of its cell; errors about the previously closed cell can accompany a valid box."""
        errs = []
        if ci != self.cur:
            if self.cur >= 0 and self.stack and not self.bad_cell:
                errs.append(f"COVER:INCOMPLETE_CELL cell {self.cur} open {len(self.stack)} next {self.stack[-1][0]!r}")
            order_ok = (ci == self.cur + 1)
            if not order_ok:
                errs.append(f"COVER:CELL_ORDER prev {self.cur} got {ci}")
            self.cur = ci
            self.cells_seen += 1
            self.stack = []
            self.bad_cell = False
            if not order_ok or ci >= self.ncells:
                if ci >= self.ncells:
                    errs.append(f"COVER:CELL_RANGE {ci}")
                self.bad_cell = True
                return None, errs
            self.stack = [("", self.cell_box(ci))]
        if self.bad_cell:
            errs.append(f"COVER:SKIPPED_AFTER_ERROR cell {ci}")
            return None, errs
        box, err = self._descend(ci, path)
        if err:
            errs.append(err)
        return box, errs

    def _descend(self, ci, path):
        if len(path) > self.max_depth:
            self.bad_cell = True
            return None, f"COVER:DEPTH cell {ci} path len {len(path)}"
        while self.stack:
            e, box = self.stack.pop()
            if e == path:
                return box, None
            if len(e) < len(path) and path.startswith(e):
                b0, b1 = self.split(box)
                self.stack.append((e + "1", b1))
                self.stack.append((e + "0", b0))
                continue
            self.bad_cell = True
            return None, f"COVER:PATH_MISMATCH cell {ci} expected {e!r} got {path!r}"
        self.bad_cell = True
        return None, f"COVER:EXTRA_LEAF cell {ci} path {path!r}"

    def finish(self):
        errs = []
        if self.stack and not self.bad_cell:
            errs.append(f"COVER:INCOMPLETE_CELL cell {self.cur} open {len(self.stack)}")
        if self.cur != self.ncells - 1 or self.cells_seen != self.ncells:
            errs.append(f"COVER:CELLS last {self.cur} seen {self.cells_seen} expected {self.ncells}")
        return errs


class Evaluator:
    """Strict ball evaluator. dsign = -1 is the mutation control 'altered derivative sign' (a_k' -> -a_k')."""

    def __init__(self, T, prec, dsign=1):
        flint.ctx.prec = prec
        self.prec = prec
        self.T = T
        self.onepT = qa(1 + T)
        self.PI = arb.pi()
        self.dsign = dsign

    # ---- core quantities on balls -------------------------------------------------------------------------------
    def base(self, r, w, p):
        """Returns (P0, P1, P2, zeta) for real balls r, w, p."""
        E = acb(r * p, -p).exp()            # e^{(r - i) phi}
        c = acb(1, -r) * E                  # (1 - i r) e^{(r - i) phi}
        zeta = 1 / acb(1 + r * w, -w)       # 1/(1 + r w - i w)
        P0 = c * zeta
        P1 = P0 * zeta
        P2 = P1 * zeta
        return P0, P1, P2, zeta

    def G_of(self, a0, a1, a2):
        return 2 * a0 * a2 - self.onepT * (a1 * a1)

    def point(self, m):
        return qa(m[0]), qa(m[1]), qa(m[2])

    @staticmethod
    def mid_half(box):
        m = tuple((lo + hi) / 2 for lo, hi in box)
        h = tuple((hi - lo) / 2 for lo, hi in box)
        return m, h

    def balls(self, box):
        return tuple(ivb(lo, hi) for lo, hi in box)

    # ---- first derivatives of a_k on balls ------------------------------------------------------------------------
    def grad_a(self, r, w, p, P, zeta):
        """d_x a_k for x in (r, w, phi), k = 0, 1, 2, plus L_k."""
        rmi = acb(r, -1)                    # r - i
        K = rmi / (1 + r * r)               # (r - i)/(1 + r^2)
        pK = K + p
        wz = w * zeta
        rz = rmi * zeta
        out = []
        Ls = []
        for k in range(3):
            kk = k + 1
            L = pK - kk * wz
            Ls.append(L)
            dr = -(P[k] * L).real
            dw = kk * (P[k] * rz).real      # -Re(P_k * (-(k+1)(r - i) zeta))
            dp = -(P[k] * rmi).real
            out.append((dr, dw, dp))
        return out, Ls, rmi, rz

    # ---- SGE ------------------------------------------------------------------------------------------------------
    def G_naive(self, box):
        """Naive ball enclosures over the box: returns (balls, P, zeta, a, G)."""
        r, w, p = self.balls(box)
        P0, P1, P2, z = self.base(r, w, p)
        a = (1 - P0.real, 1 - P1.real, 1 - P2.real)
        return (r, w, p), (P0, P1, P2), z, a, self.G_of(*a)

    def grad_G(self, balls, P, z, a):
        """(dG/dr, dG/dw, dG/dphi) and d a_k on the given balls."""
        r, w, p = balls
        da, _, _, _ = self.grad_a(r, w, p, P, z)
        dG = [2 * (da[0][j] * a[2] + a[0] * da[2][j]) - 2 * self.onepT * a[1] * da[1][j] for j in range(3)]
        return dG, da

    def G_mvf(self, box, balls, P, z, a):
        """Mean-value-form enclosures of G and a1 over the box (gradient balls on the box, exact centre)."""
        m, h = self.mid_half(box)
        Q0, Q1, Q2, _ = self.base(*self.point(m))
        b = (1 - Q0.real, 1 - Q1.real, 1 - Q2.real)
        Gm = self.G_of(*b)
        dG, da = self.grad_G(balls, P, z, a)
        hb = [symb(x) for x in h]
        Gmvf = Gm + dG[0] * hb[0] + dG[1] * hb[1] + dG[2] * hb[2]
        a1mvf = b[1] + da[1][0] * hb[0] + da[1][1] * hb[1] + da[1][2] * hb[2]
        return Gmvf, a1mvf

    def check_SGE(self, box):
        """'naive'/'mvf' iff certified a1 > 0 and G > 0 on the whole box, else None."""
        balls, P, z, a, G = self.G_naive(box)
        a1pos = a[1] > 0
        if a1pos and G > 0:
            return "naive"
        Gmvf, a1mvf = self.G_mvf(box, balls, P, z, a)
        if not a1pos:
            a1pos = a1mvf > 0
        if a1pos and Gmvf > 0:
            return "mvf"
        return None

    # ---- DPOS -----------------------------------------------------------------------------------------------------
    def D_val(self, r, w, p):
        P0, P1, P2, z = self.base(r, w, p)
        P = (P0, P1, P2)
        a = [1 - x.real for x in P]
        rmi = acb(r, -1)
        pK = rmi / (1 + r * r) + p
        wz = w * z
        d = [self.dsign * (-(P[k] * (pK - (k + 1) * wz)).real) for k in range(3)]
        D = d[0] * a[1] * a[2] + a[0] * a[1] * d[2] - 2 * a[0] * d[1] * a[2]
        return a, d, D, P, z

    def D_naive(self, box):
        r, w, p = self.balls(box)
        a, d, D, P, z = self.D_val(r, w, p)
        return (r, w, p), a, d, D, P, z

    def grad_D(self, balls, a, d, P, z):
        """(dD/dr, dD/dw, dD/dphi), d_x a_k' and d_x a_k on the given balls."""
        r, w, p = balls
        da, Ls, rmi, rz = self.grad_a(r, w, p, P, z)
        omr = acb(1, -r)
        inv2 = 1 / (omr * omr)              # (1 - i r)^{-2}
        z2 = z * z
        wz2 = (w * z) * (w * z)
        dd = []                             # dd[k][j] = d_x a_k'
        for k in range(3):
            kk = k + 1
            L = Ls[k]
            lam = (L, -kk * rz, rmi)
            dL = (inv2 + kk * wz2, -kk * z2, acb(1))
            dd.append(tuple(self.dsign * (-(P[k] * (lam[j] * L + dL[j])).real) for j in range(3)))
        dD = []
        for j in range(3):
            t = (dd[0][j] * a[1] * a[2] + d[0] * da[1][j] * a[2] + d[0] * a[1] * da[2][j]
                 + da[0][j] * a[1] * d[2] + a[0] * da[1][j] * d[2] + a[0] * a[1] * dd[2][j]
                 - 2 * (da[0][j] * d[1] * a[2] + a[0] * dd[1][j] * a[2] + a[0] * d[1] * da[2][j]))
            dD.append(t)
        return dD, dd, da

    def D_mvf(self, box, balls, a, d, P, z):
        """Mean-value-form enclosures of D and of a0, a1, a2 over the box."""
        m, h = self.mid_half(box)
        am, dm, Dm, _, _ = self.D_val(*self.point(m))
        dD, dd, da = self.grad_D(balls, a, d, P, z)
        hb = [symb(x) for x in h]
        Dmvf = Dm + dD[0] * hb[0] + dD[1] * hb[1] + dD[2] * hb[2]
        amvf = [am[k] + da[k][0] * hb[0] + da[k][1] * hb[1] + da[k][2] * hb[2] for k in range(3)]
        return Dmvf, amvf

    def check_DPOS(self, box):
        """'naive'/'mvf' iff certified a0, a1, a2 > 0 and D > 0 on the whole box, else None."""
        balls, a, d, D, P, z = self.D_naive(box)
        apos = [x > 0 for x in a]
        if all(apos) and D > 0:
            return "naive"
        Dmvf, amvf = self.D_mvf(box, balls, a, d, P, z)
        apos = [apos[k] or (amvf[k] > 0) for k in range(3)]
        if all(apos) and Dmvf > 0:
            return "mvf"
        return None

    # ---- INFEAS ---------------------------------------------------------------------------------------------------
    def check_INFEAS(self, box):
        """Returns (ok, reason). Rule: r_lo > 0, phi_lo > pi, g_{r_lo}(phi_lo) > 1 (ball at the exact corner)."""
        (rl, rh), (wl, wh), (pl, ph) = box
        if not (rl > 0):
            return False, "INFEAS:DOMAIN_R_LO"
        plb = qa(pl)
        if not (plb > self.PI):
            return False, "INFEAS:DOMAIN_PHI_LO"
        rlb = qa(rl)
        g = (rlb * plb).exp() * (plb.cos() - rlb * plb.sin())
        if not (g > 1):
            return False, "INFEAS:G_NOT_GT_1"
        return True, "corner"

    # ---- dispatch -------------------------------------------------------------------------------------------------
    def verify(self, box, outcome):
        """Returns (ok, method_or_reason)."""
        if outcome == "SGE":
            m = self.check_SGE(box)
            return (True, m) if m else (False, "SGE:G_GT_0_NOT_CERTIFIED")
        if outcome == "DPOS":
            m = self.check_DPOS(box)
            return (True, m) if m else (False, "DPOS:D_GT_0_NOT_CERTIFIED")
        if outcome == "INFEAS":
            return self.check_INFEAS(box)
        return False, f"OUTCOME:{outcome}"

    def verify_subdiv(self, box, outcome, geom, extra_depth):
        """Recorded extra subdivision (same claimed outcome on every sub-box, split rule of `geom`).
        Returns (ok, n_subboxes, deepest, first_failure)."""
        stack = [(box, 0)]
        n = 0
        deepest = 0
        while stack:
            b, dep = stack.pop()
            ok, why = self.verify(b, outcome)
            if ok:
                n += 1
                deepest = max(deepest, dep)
                continue
            if dep >= extra_depth or outcome == "INFEAS":
                return False, n, deepest, {"box": [[str(x) for x in iv] for iv in b], "depth": dep, "reason": why}
            b0, b1 = geom.split(b)
            stack.append((b1, dep + 1))
            stack.append((b0, dep + 1))
        return True, n, deepest, None
