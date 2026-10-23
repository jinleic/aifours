# R2MIX second-family precision erratum

Recorded at 2026-10-19T13:38:03-0700. Apply after proof `b75e6dc7e72b8c0b1cd5388e8845a3bcd23854b0fbd83292fa6ff7c22ade0806` and [parent erratum v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-R2MIX-parent-erratum-v1.md) `c8528a68d7923ddc677457354b177167c3f2f038571816ebe2195bb33cc5badf`. Disposes [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-R2MIX-claude-v2.prompt.note.md) `0fa4eb33e2fcec461eac9c4286ed7ff5214fa9f8f4292e3888800397410f355a`: 0 FATAL/0 MAJOR/6 MINOR groups. Principal statements, ranges and finite-group proof steps unchanged; no pending MK or M3R result is accepted by this erratum.

## m1: only the needed portions were re-proved

At proof lines14-15,19,73,116 and the corresponding package summaries, read: "re-proved in the form needed". Theorem7 proves only the four O'-entries x'_tu=2, not M3R's stronger x'_(t i*)=2. Lemma4 supplies no converse of M3R C(b) and no bound z_(e i*)>=3. No downstream caller may import those stronger conclusions under the re-proof label.

## m2: explicit arbitrary-group descent for the R1 product condition

For R1X/NR, let N be the intersection of the cores of the original finite-index subgroups. N is normal and lies in every subgroup of BOTH families. The quotient map pi satisfies pi(XY)=pi(X)pi(Y), so the R1 equality Pi_tPi_a=Pi_tPi_b descends. Normality also makes inversion/conjugation commute with this quotient; indices, matrices and disjointness are preserved by the accepted R0 interface. Thus an arbitrary-group R1-instance would yield the finite-group R1-instance excluded by Theorem7+R2X. R2X's numerical hypothesis already descends directly.

## m3: ancillary granularity and product equivalence

Define Gamma_(y')(t):=gcd(n_t,T_(y')(V minus {t})). If tau_(y')({d,i*,e})=3, then T_(y')({d,i*,e})=3*lcm(n_d,n_e,n_(i*)) has 3-valuation2 and divides T_(y')(V minus {t}); since f_t>=2 the stated Gamma>=18 follows. This is the one-line ancillary fact used in the granularity diagnostic, not an unstated imported converse of Lemma4.

For the two product equalities in lines238-239, the converse direction follows from Pi_ePi_d=Pi_e(Pi_d cap Pi_e)(Pi_d cap Pi_(i*))=Pi_e(Pi_d cap Pi_(i*)); the forward ordered-factor argument is supplied in Lemma4. Both statements retain their finite-set meaning without a product-as-subgroup assumption. Reword "single-family,t-local routes" as "the previously recorded local and global route diagnostics"; M3R obstruction2 already uses opposite-family granularity and obstruction4 is O-global.

## m4: diagnostics describe this argument, not method impossibility

- Mutation1's estimate deg_d(e)<=3n_d/4-s-1 gives no contradiction **for R2-rows (s=0), or when s<=n_d/4-1**. At s=n_d/4 it already contradicts the exact degree without Lemma2. Product separation remains load-bearing in the actual R2X route, not every Proposition5(a) parameter instance.
- Mutation8: the distinguished degree changes to3n_d/4; the three-piece cap is no longer supplied by the stated Sun(4) argument. No actual four-piece group configuration or universal cap failure is asserted.
- Replace "needs both families" by "this argument uses both families".

## m5: historical package metadata

The package's v1-to-v2 summary must name all five changes reported by the proof header: inclusion-exclusion sentence, E3-a scope, E3 facts re-derived, mutation2 wording and section7's three-entry discussion. This remains author-reported draft history, not authenticated by reviewers who lacked v1. External navigation-only references are not premises. No new historical/progress claim follows.

## m6: local naming and dependencies

In Lemma1's proof use Psi_v:=g_vU_vg_v^-1 for the local conjugate stabilizer instead of reusing the global U*_v symbol for both configurations. The dependency order is: class arithmetic and L0.1 -> Lemma4; Lemma1 and LFC -> Lemma3; Lemmas2-4 -> Proposition5 -> R2X; Lemma6 and VFC/E3-a -> Theorem7; Theorem7+R2X -> R1X -> NR -> conditional M3E. No Lemma3-to-Lemma4 dependency is asserted.
