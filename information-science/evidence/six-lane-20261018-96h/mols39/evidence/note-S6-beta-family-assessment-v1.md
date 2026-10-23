# Note S6 — parent correction on the beta route; equivariant lift excess of the frozen models; assessment of a
# "construct/mutate the index-3 skeleton, then lift" family (2026-10-19T04:34:51-0700, ContinueCFR21)

## 1. Record of the parent correction (parent IRC, 2026-10-19 ~04:3x PDT, after reading S4 in full)
The parent states that its earlier description of the fixed-beta extension as "strictly wider than fixing the old alpha"
was only potential, not established; that S4 shows the anchor's 6-row skeleton has ONLY ±alpha modulo row constants;
and that, if this measurement is certified, any 7-row lift with the same old beta restricts to an old 6-row lift
equivalent to the original DM39, so the fixed-beta extension is another representation of the anchor's free extension,
not a new family. No broader headroom is claimed. This matches reduction R1
(/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/reduction-R1-beta-route-v1.md, sha256 eabe1fc4375ed05492e684d38418bda2c294305269240503e6e96c27c1a4669b).
Certification of the S4 input (Lemma U) is in progress: an independently authored exhaustive lift counter
(review/lift_route2/, author did not read S4/R1 or the S4 probe) will be run on the anchor with Sage DM21 and a Singer-type
(57,8;1)-DM as controls.

## 2. Exact counts (probe code/probe_lift_excess_v2.py sha256 bd31e6e59deab3818462aa027b33958aece6ba7c657ccdd4de25fe3db74e7226; run evidence/runs-le2/LE2-frozen-models,
## supervised, pid=pgid 82642, stdout sha256 d27074013c29b72efecbf877a0cf8f66e712f94d925d6688a8056638bf26811d, receipt sha256 f58738e2475f63d20444e92942e4f58573cc86c93e8dd4cd1683d9e3c496dbd3)
For a frozen orbit model with group G and its declared orbit types: E = number of G-orbits on the 273 (pair, t in Z_13)
fibre labels (one fibre-sum equation each for an equivariant lift), U = equivariant lift unknowns (one representative per
column orbit, stabiliser and zero-row constraints), C0 = equivariant row constants (0 when the zero column is gauged).
| model | rows | E | U | C0 | excess U - C0 - E |
|---|---|---|---|---|---|
| z39_g6six (anchor model) | 6 | 35 | 38 | 0 | +3 |
| z39_z6p | 7 | 46 | 38 | 0 | -8 |
| z39_g6 | 7 | 49 | 38 | 0 | -11 |
| z39_g3 (f = 0 and f = 3) | 7 | 91 | 78 | 2 | -15 |
| z39_m1 | 7 | 138 | 114 | 0 | -24 |
Reading: in the six-row anchor model every in-model skeleton has an equivariant lift space of dimension >= 3, which fits
the existence of the anchor; in every frozen seven-row model the equivariant lift system is overdetermined, so a lift
needs a rank-deficient skeleton.
[HEURISTIC, characteristic-0 averaging, not exact over F_3 when 3 | |G|] By a Burnside-type average,
excess ~ (1/|G|)(-45 + sum over g != 1 of [eps_g (f_c(g)-1)(f_r(g)-1) - |Fix_Phi(g)|]), where f_c, f_r are the numbers
of fixed columns and rows and eps_g = mu_g mod 3. By structural-note-S2-v1 (with erratum), an element with f_r >= 2 and
eps = +1 has f_c in {0, 3} and f_r <= 3, and it fixes at least C(f_r,2) fibre labels, so each non-identity term is at most
+1. Hence no symmetry group makes the seven-row system underdetermined on this count.

## 3. Assessment of the "construct/mutate beta, then exact GF(3) lift" family
[HEURISTIC, for decision only] In the best frozen model (z39_z6p, excess -8), a random in-model skeleton has a
non-trivial equivariant lift with probability ~3^-9, and that lift is rainbow on all 46 fibre orbits with probability
~(2/3)^46 ~ 8e-9, so ~4e-13 per skeleton. That is consistent with the ~25 expected solutions in z39_z6p
(heuristics-v1.md) only if there are ~1e13-1e14 in-model skeletons. Balanced-fibre trades preserve the index-3 property
but give no gradient towards GF(3) rank deficiency, so local mutation behaves like sampling. Expect ~1e12-1e13 skeleton
generations plus lift tests per hit, and generating valid skeletons is itself a constrained design problem.
Recommendation: do not build a beta-mutation engine in this run. Singer-type mod-19 controls (rows deleted and then
re-lifted) would be engine controls only and are not prepared, because no engine is proposed. A route that is genuinely
wider than the anchor family would need either a model with non-negative excess (none among the frozen models, and the
heuristic bound above suggests none exists) or a construction that forces rank deficiency algebraically. No such
construction is known to this lane.
Scope: counts are exact for the stated models; everything else is heuristic. Nothing here bears on the existence of a
(Z_39,7;1)-DM or of six MOLS(39).
