# Reciprocal W_I — where any point must live, and the exact barrier

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 22:49:19 PDT 2026**. InfoSPR7/info-2.

This is a **BARRIER NOTE**. §1 is exact and repeats imported facts. §2 is a FORMAL leading-order computation; it is labelled as such and proves nothing. §3 states the exact residual and names the next representation.

The work is symbolic. No numeric instance, interpreter, eval, program, CAS or GO is used.

Imports, none edited:

- v10 (`f19221c0…ebfb7`) with erratum-1 (`cd14290a…93e1`);
- the window lemma (`1e02dd48…63d9`);
- the middle-width note (`5d921b5c…6bec`);
- the small-r theorem (`a22b4ed1…89e6`);
- the monotonicity lemma (`7a56acab…12ab3`).

## 1. Exact facts in force

- **Middle width.** 2w3=f1+e1f0, with e1=Σ1/x_i and 1/x2+1/x3<1/s+c.
- **Exact emptiness.** For L≥2, W_I has no point with h≤L, c+1/c≤L and r≤10^{-8}L^{-3}.
- **Monotonicity.** Δrev(p)<Δrev(q)<(q/p)²Δrev(p) for all 0<p<q.

## 2. FORMAL leading order: points need r and s of order one

**Not a proof.** This section assumes x1 is small compared with r and s, and drops σ3, M1, N3 and all d0 corrections.

Under these assumptions, w3>0 reduces to

`f2/|f1| < 1/x2+1/x3 < b+1`, where a=1/r and b=1/s.

Write η=H3+f0. Then

`f2/|f1| ≈ (A+ηB)/(C+ηD)`, with:

- A=σ1(2σ1²+2σ2);
- B=σ1²+2σ2;
- C=3σ1²−2σ2;
- D=2σ1.

Since AD−BC=σ1⁴+4σ2²>0, this Möbius function decreases in η. Its infimum is B/D=(σ1²+2σ2)/(2σ1).

With σ1≈a+b and σ2≈ab, the condition becomes

`(a−b)/2 + ab/(a+b) < 1`.

Since ab/(a+b)≥b/2, this forces b<2, that is s>1/2, and a−b<2. So, FORMALLY, any W_I point has its two C2 contacts r<s at order one, with s>1/2.

There the small-parameter expansion is no longer valid: window consequence B only gives d0<r^{3/2}(2−3r)^{-1/2}, which is of order one. This agrees with, but does not extend, the exact small-r theorem.

## 3. Exact residual and next representation

**Undecided.** W_I is still open on:

- the complement of the exact small-r region;
- formally, a COMPACT middle region in which r, s, c, h and w are all of order one and no small parameter is available.

W_II and W_III are fully undecided. So are the reciprocal class and universal SPR7.

**Barrier.** Hand-written symbolic inequalities are not enough to settle a five-dimensional compact semialgebraic region in which every term competes.

**Next representation.** An exact rational certificate on the compact chart region would settle it. Candidates:

- Bernstein or interval subdivision with exact rational sign proofs of −w3, or of a violated monotonicity window, on each cell;
- a Positivstellensatz/SOS identity.

Either one also covers the transition to the asymptotic regimes, which are already exact at small r. Producing and replaying such a certificate is SCIENTIFIC EXECUTION. Under scientific-admission-hold-v2 it requires a separate named GO with supervised resources, so **none is requested or performed here.**

## Assurance

This note is not formal, kernel, human, family, cross-vendor, executable or novelty acceptance, and not a GO request granted. All four owner process majors and all parent findings remain; the cutoff and deadline are unchanged.
