| Claim | Verdict |
|---|---|
| Lemma EDGE | **ACCEPT** |
| Extended B0S-CJ triple-prime | **ACCEPT** |
| Extended REFL-B0 | **ACCEPT**, reading SOURCE06 through SOURCE07/08 as requested |

**No new FATAL, MAJOR, or MINOR mathematical defect found.** Two inherited MINOR wording corrections in SOURCE06 remain relevant and are recorded below.

All eleven SHA256 hashes and byte counts match. This audit used only static reads and hashes within the snapshot. The accepted CJ range in **SOURCE04:L13** retains both inequalities; the extension below depends on the newly audited EDGE argument. H0, P0, the accepted RED reduction and its upstream RGR results remain scoped imports.

**The imported inequalities survive removal of the bound.** At [SOURCE01:L27–48](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-edge-r2-review-v1/snapshot/01-B0SCJx-r4.md:27), the relevant assumptions are \(R\ge4\kappa-4\), \(R\ge p\), and the standing avoider cut \(R\le2p-1\).

Window nonemptiness requires \(R\ge2\kappa+1\). For \(\kappa\ge3\), \(4\kappa-4\ge2\kappa+2\); for \(\kappa\le2\), \(R\ge p\ge5\) suffices. The cap \(p-1\) in \(g_1\) remains inactive because \(E\le2p-1\). Avoidance excludes full windows, giving unique gap representatives even for zero-mass intervals.

For C2(a), the two-small calculation is exact:
\[
\sum_i g(m_i)=R-2\kappa-\lceil T/2\rceil\ge-2
\iff m_1+m_2\ge4\kappa-4-R.
\]
The right side is nonpositive. One small gives \(R/2-1-\kappa\ge-2\); three small give \(R-3\kappa\ge-2\), using \(R\ge3\kappa-2\); none small gives a nonnegative bound. No \(2\kappa\le p-1\) enters.

For C2(b), two small pair sums sharing mass \(m_b\) give
\[
(B')=\left\lfloor\frac{3R+m_b}{2}\right\rfloor-2\kappa\ge p-2,
\]
because \(3R+m_b\ge2p+4\kappa-4\). Three small give \(2R-3\kappa\ge R+\kappa-4\ge p-2\) for \(\kappa\ge2\); \(\kappa=1\) would force \(R\le3\). With no small pair sum, integrality gives \((B')\ge R-1\). With one small sum \(s\), the imported bound is
\[
(B')\ge R-\kappa-1+\lceil s/2\rceil\ge p-2
\]
whenever \(s\ge2\Delta-1\). Thus C1, C2(c), and the \(\Delta\le0\) SIGMA-2P induction all transfer. They allow nonempty sets of run indices whose rotation mass is zero.

In the edge cells,
\[
\Delta\le(3-p)/2<0,\qquad k\in\{p+3,p+2\},\qquad
\sum x_t=p,\quad \sum\mathrm{bh}_t=2p-R\in\{2,1\}.
\]
Also \(g(R)=p-1\), so an empty singleton has gap \([1-\kappa,0]\). Genuineness excludes residue zero, forcing \(x_t<0\): every empty run is a defect. The defect bound gives
\[
c_t=r_t+\delta_t\in\{2,4,\ldots,p-1\}.
\]
Zero defect deficit is permitted; positive mass then supplies \(c_t\ge2\).

**All six conditions support K1–K3.** For [SOURCE00:L40–63](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-edge-r2-review-v1/snapshot/00-EDGE-r2.md:40), “proper” means proper in the entire run cycle. A pattern may equal \(Z\), since \(Z\subsetneq[k]\).

For K1, U2 is its lower bound on \(\Phi\), and U3 follows from \(P\subseteq Z\). U1 and L1 are respectively \(\Phi-2\delta_P\) and \(\Phi-2\rho_P\), hence at most \(2p\). Since \(m\ge1\),
\[
\text{L2 left side}=\Phi-4m\le2p-4\le2R-p-3.
\]
For L3, \(\delta_P\le2p-2-\rho_P\). At \(\rho_P=0\), the parity-adjusted upper bound is exactly \(2p-2\) in both cells; at positive mass, \(\delta_P\le2p-3\le R-1\).

For K2, nonadjacency gives \(m=2\). U1 and L1 become exactly \(\delta_P\ge1\) and \(\rho_P\ge1\). U2 is automatic, U3 assumed, L2 is \(2p-6\le2R-p-3\), and L3 follows from \(\delta_P=2p-2-\rho_P\).

For K3, \(P=\{t,y\}\) has
\[
\rho=r_y,\quad m=2,\quad \delta=p-1-\mathrm{bh}_y.
\]
U2, U3 and U1 are precisely (a), (b), (c). L1 is \(p+3-2x_y\le2p\), since nondefect status gives \(2x_y\ge r_y+1\). L2 requires \(r_y-x_y\le R-p+1\); failure would imply
\[
r_y\ge R-p+2+x_y\ge p+(r_y+1)/2,
\]
hence \(r_y\ge2p+1>R\). L3 follows from \(\mathrm{bh}_y\ge1\).

All these patterns are nonempty and proper. For any proper cyclic pattern, \(2m\le k\); here \(m\le\lfloor(p+3)/2\rfloor\le p\). The two- and three-run patterns therefore introduce no hidden interval-count restriction. Parity \(\delta_P\equiv\rho_P\pmod2\) is maintained, including K3’s potentially negative deficit before condition (b) is imposed.

**Case II remains valid, including \(p=5\).** The generic construction in **SOURCE02:L93–109** supplies even \(d\), \(2\le d\le\kappa-1\), enough isolated \(\mathrm{bh}=1\) runs, and positive \(\delta_P\). Its properness proof retains an outside neighbor of \(Z\) that cannot belong to \(W\). The alternating selection occurs inside proper runs of eligible indices, so there is no unresolved cyclic first/last adjacency.

The numerical checks in **SOURCE00:L68–73** hold independently:

- L3: \(\delta_P\le p-1\le R-1\).
- U1: \(r_y+1\le2p\), or \(3\kappa-7<2p\).
- L1: \(4\kappa-4=2p-2<2p\).
- Singleton L2: \(r_y\le R\le2R-4\kappa+5\).
- Otherwise L2: \(2p-2\le2R-p-3\).

The last bound has equality at \(p=5,R=8\), which is allowed. Indeed \(d\le2\) there, so the multiple-item branch is unnecessary. The cardinality argument uses \(k\ge2\kappa+1\), with equality allowed when \(R=2p-1\).

**Step 1’s maximality argument is sound.** At **SOURCE00:L75–87**, an inclusion-maximal \(P'\) exists, is nonempty, and differs from \(Z\). Adding a defect changes \(\Phi\) by \(c_t+2,c_t,c_t-2\), all nonnegative. The omitted same-interval double contact would make \(P'\cup\{t\}=[k]\), impossible inside \(Z\).

If no K1 kill occurs, every outside addition must reach exactly \(4\kappa\). Consequently \(\Phi(P')=2\kappa\), every outside defect is extreme, and none is adjacent to \(P'\). Removing an endpoint \(e\) and inserting an outside \(t\) gives exactly the two displayed replacement formulas. A nonsingleton interval yields a K1 kill; a singleton must be extreme. Therefore
\[
2\kappa=\Phi(P')=2\kappa|P'|,
\]
so \(P'\) is one singleton.

The assertion that every other singleton is inclusion-maximal has a short justification: all defects are now extreme, and any two-defect set has
\[
\Phi\ge2(2\kappa-2)+2=4\kappa-2>2\kappa.
\]
Monotonicity excludes every larger superset. Repeating the argument establishes pairwise separation. Every replacement remains inside \(Z\subsetneq[k]\).

**Steps 2–4 close their exceptional cases.** For a separated pair, \(\rho+\delta=2p-2\). Unless \(\rho=0\) or \(\delta=0\), K2 kills. Since each mass is at most \(p-1\), this forces either all defects empty, or all defects of mass \(p-1\). An intermediate mass or mixed pair kills.

In FM, mass permits exactly two defects. Their deficits vanish, leaving at most two units of \(\mathrm{bh}\) for at least \(p\) nondefects, each requiring at least one: contradiction.

For three empty defects, \(m=3\), and **SOURCE00:L97–100** correctly gives
\[
I(P)=[3-p,\,2-\kappa],\qquad x(P)+p=2-\kappa.
\]
This is an exact endpoint hit. At \(p=5\), the window is \([-2,-1]\) and the shifted representative is \(-1\). H0 tests congruence modulo \(p\), so the shift is legitimate even though the unshifted representative fails the six-condition test.

**Step 5’s bookkeeping closes every overlap case.** At **SOURCE00:L102–121**, all \(Y\)-runs are nonempty, with
\[
N_+=3p-1-R,\quad \sum_Yr_y=R,\quad
\sum_Y\mathrm{bh}_y=4p-2-R.
\]
Two nonadjacent vertices of a cycle of length at least seven have at most one common neighbor \(y_0\). Every other \(y\) can be tested against some nonadjacent empty defect.

Failures of (a), (b), (c) respectively imply
\[
\mathrm{bh}_y\ge r_y+2,\quad p,\quad 3p-4-r_y.
\]
The last bound is valid and slightly weaker than integrality permits. Their minimum is \(r_y+2\) for \(r_y\le p-2\), and at least \(p-3\) otherwise. Three big runs would require \(3(p-1)>R\), so there are at most two.

With \(S=\{\text{big runs}\}\cup\{y_0\}\), the definitions \(b=\#\{\text{big runs other than }y_0\}\), \(e=[y_0\text{ exists}]\) give \(|S|=b+e\), including overlap. A big \(y_0\) receives only the lower bound one, avoiding double counting. Also \(|S|\le3<N_+\). Nonemptiness outside \(S\) yields
\[
M_S\le2R-3p+1+|S|\le p-1+|S|.
\]
Summing the deficit bounds yields
\[
M_S\ge2p-2|S|+b(p-3)+e.
\]
Thus \(2e\ge p+1+b(p-6)\). For \(b=0,1,2\), even the weaker choice \(e=1\) requires respectively \(p\le1,7/2,13/3\). Choice \(e=0\) is stronger. All six cases contradict \(p\ge5\).

**The CJ extension follows without importing an enlarged parent scope.** First, \(R\ge2p\) supplies an ordered identity subword of equal rotations. Otherwise
\[
2\kappa>p-1,\qquad4\kappa\le R+4\le2p+3.
\]
Because \(p\) is odd and \(2\kappa\) is even, \(2\kappa=p+1\). Hence \(R\in\{2p-2,2p-1\}\), exactly EDGE.

The extension retains CJ’s other conditions, including \(\Delta\le0\) or two disjoint heavy admissible intervals. It also retains the parent corrections: nonempty arcs, the corrected corollary scope and shortcut, and no wholesale strengthened \(p\le23\) conclusion. No finite census is a premise.

**The REFL-B0 transfer works for arbitrary initial block parities.** At [SOURCE06:L37–50](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-edge-r2-review-v1/snapshot/06-REFL-B0-r3.md:37), normalization preserves block lengths and avoidance. With \(B=0\), P3/P4 remain unavailable. FUS preserves \(R\) and raises \(H\) only in an odd–even–odd double fusion; PM0 preserves \(H\) for either receiving parity. Rereading maximal blocks introduces no further fusion across PM0’s nonempty merged rotation run. Thus \(R\) stays fixed and \(\kappa'\le\kappa\).

Under a counterexample to reflection rigidity, the accepted RED exits and terminal argument apply. The \(g=0\) exit contradicts I2/I3; otherwise the terminal word has genuine empty runs, all blocks odd and \(2\le\kappa'\le\kappa\). No initial oddness or \(o_F\le p\) assumption enters.

Now \(R\ge4\kappa'-4\), so extended CJ applies. Its corrected corollary forces
\[
\Delta'\ge2,\qquad5R<4p+6\kappa'-10,
\]
contradicting either retained numerical alternative exactly as before. The cases \(\kappa\le0\), absent reflections, or \(R=0\) remain covered by the supplied pair/K0*/AR imports.

The first OR branch is redundant: \(H\ge0\) gives \(\kappa\le p-1\), and \(R\ge p+\kappa-2\) implies the second inequality. Keeping the OR adds no restriction.

The inherited **MINOR** repairs are **SOURCE06:L42–43**: replace “an odd one” by “the next block, of either parity”; and **SOURCE06:L63–64**: P3 preserves \(R,B,\kappa\), while P4 changes them. SOURCE07/08 already identify both. The r3 wording delta changes neither proof.

These verdicts establish the stated partial equal-nonidentity-rotation results only; they make no full REFL, INV*, ordered Olson, or novelty claim.