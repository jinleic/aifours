# Exploratory lemma (parent lead, checked here): analytic exclusion of K1 at n = 8 — status EXPLORATORY

Lemma K1-AG. Let 𝒩 be a 6-net consisting of six direction classes of AG(2,8) and Ψ an assignment of unit vectors of
C⁸ to the 64 points that is an ONB on every line of 𝒩. Then Ψ has exactly 8 rays (all vectors lie, up to phase, in
the ONB of any line), i.e. the corresponding QLS (after any regridding) is classical.

Proof (parent's argument, details checked). Choose a net class as "rows" (direction ∞) and a row line as frame, with
coordinates (r, c) ∈ GF(8)² so that the frame is r = 0 and its vectors are e_c (one unitary). The other five net
classes are c + t·r = b with t ∈ A ⊂ GF(8), |A| = 5; let T = GF(8) ∖ A = {t1, t2, t3} and t0 = t1 + t2 + t3.
(a) t0 ∉ T (t0 = t1 would force t2 = t3); so the t0-class belongs to the net.
(b) For r ≠ 0 the point (r, c) lies on the t-line through (0, c + t r) for each t ∈ A, so supp Ψ(r,c) ⊆ c + rT
    (Prop 1 + orthogonality on net lines).
(c) On the net line c + t0 r = b the seven points q_r = (r, b + t0 r), r ≠ 0, have supp ⊆ b + r(T + t0) = b + rV with
    V = T + t0 = {t2+t3, t1+t3, t1+t2}: three distinct nonzero elements with sum 0, so W = V ∪ {0} is a 2-dimensional
    F2-subspace. For r ≠ r′ (both nonzero) rW ≠ r′W (otherwise a = r′/r ≠ 1 would stabilize the 3-set V inside the
    cyclic group GF(8)* of order 7, impossible), and two distinct 2-dimensional subspaces of F2³ meet in a
    1-dimensional one; hence |rV ∩ r′V| = 1.
(d) The seven vectors Ψ(q_r) are pairwise orthogonal (same net line) and their supports avoid b and pairwise meet in
    at most one coordinate, hence (Lemma 2) are pairwise disjoint; seven nonempty disjoint subsets of the 7
    coordinates other than b are singletons. Every point off the frame lies on some t0-line, so every entry has
    weight 1 in the frame: Ψ is classical. ∎
Bridge needed for K1: in a K1 configuration S′ the 6-net {rows, columns, four classical symbol classes} must be
identified with six AG(2,8) direction classes — Egan–Wanless Table 6 (n = 8, k = 4: one paratopism class; the linear
set is a representative) — and the identification is applied through the regridding Lemma R of
review/PROOF_N8_PARTIAL.md (re-indexing points preserves ONB-on-lines and the ray count); no frame-transitivity
argument and no FIXED-net SAT run is needed on this route.

Exact checks (code/k1_analytic_checks.py → evidence/k1_analytic/checks.json, 08:44 PDT, all_ok = true): for all 84
3-subsets T: (a); (b) V nonzero, distinct, V ∪ {0} closed (impl1) and of rank 2 (impl2, F2 matrices); (c)
|rV ∩ r′V| = 1 for all 21 pairs (impl1) and dim(rW ∩ r′W) = 1 (impl2); (d) for every b the seven sets b + rV avoid b
and pairwise meet in exactly one element. Mutations: for every T some other net direction t ≠ t0 fails the pairwise
property; Z8 arithmetic in place of GF(8) fails it. Both implementations agree; impl2's multiplication matrices
agree with impl1's product on all 64 pairs.

Relevance to K2 (assessment): in K2 the classical part is a 5-net (3-MOLS(8)), which need not be affine (Egan–Wanless
Table 5: 38 maximal classes of 3-MOLS(8)). Even in the affine case the allowed sets are c + rT with |T| = 4, shared
disjointly by two quantum squares; for a 4-set V ⊆ GF(8)* every x ∈ GF(8)* lies in exactly 4 of the seven sets rV,
so Σ_{r<r′} |rV ∩ r′V| = 7·C(4,2) = 42 over 21 pairs (average 2): some pair always meets in ≥ 2 elements and the
singleton-forcing step has no direct analogue. The lemma makes K1 = ∅ (used to justify P4 in every frame for K2)
independent of the FIXED SAT certificate and of the PGL(2,8) frame argument; it does not by itself decide K2.
