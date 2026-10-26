# Peer reconstruction: Olson p−3 deeper-switch classification v1

Reviewer: MathSun8, math-6. Observed before creation: `2026-10-23T14:34:46-0700` (`/bin/date`). Parent's priority bounded review assignment; ordinary supplied-proof in-harness reconstruction, not blind, cross-vendor, human or formal review.

## Pin, read scope and verdict

Complete reviewed source, lines1–216:

    mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/
      proof-DEEPER-SWITCH-CLASSIFICATION-v1.md
    SHA256 c2b0f89eb526010cd2556ac6f0aba205e4b7e35fcaa15809193c3d39b4976b81

I observed the actual source SHA256 by metadata `shasum`; it matches the parent's pin. **0 FATAL / 0 MAJOR / 0 MINOR at the exact stated partial scope.** The p−3 binary inverse, both missing-residue formulas, arbitrary actual-K packet implication, first deeper matching counts and same-gap two-singleton restrictions reconstruct correctly. No whole-MIX theorem, strict new B2 coverage witness, avoiding word, residual nonemptiness, formal verification or novelty acceptance is established.

I also read the actual slot `selection-v1.md` in full; predecessor `proof-GAUGE-SWITCH-AND-CRITICAL-LADDER-v1.md` lines1–253, including its complete gauge derivation, binary growth, packet definition, matching/cut bridges and residual scope; and the historical `reflection-round2/proof-REFLHI-arcs-v2.md` complete lines1–161. Historical ARC/ETA are confirmed prior mechanisms with narrower hypotheses, not direct premises of the new elementary inverse proof.

## 1. Reconstructing the p−3 inverse (author lines25–100)

For nonempty proper A⊂F_p, translation by nonzero d is a single directed p-cycle. The number of new points in (A+d)\A equals the number of occupied stretches of A in that cycle. One-point growth therefore makes A exactly one interval of step d, proving E1, including the stated converse.

For an interval A={0,...,L−1}, the overlap under shift r∈{1,...,p−1} is exactly

    max(0,L−r)+max(0,L−(p−r)).

With2≤L≤p−2, both positive summands give2L−p≤L−2. A single positive summand equals L−1 only for r=1 or r=p−1. This verifies E2 and its crucial p−2 upper bound; no false rigidity is invoked at length p−1.

For P4, when a,b are not equal up to sign, {0,a,b,a+b} has four distinct points. In a four-term arithmetic interval the outer/inner pair partition is the unique equal-sum partition: the other two partition sum differences are2d and4d, both nonzero at p≥7. Positioning0 at interval position0,1,2 or3 yields precisely {d,2d},{−d,2d},{d,−2d},{−d,−2d}. Thus one increment is a signed single step and the other a signed double step.

Now take t=p−3 nonzero increments. If they are not all equal up to sign, choose two nonparallel ones first (commutativity is used only for this SCALAR sumset, after the actual-word formula). Their binary sumset has four points. The remaining p−5 translations each add at least one until fullness. If the final sumset is proper, its size is at least4+(p−5)=p−1 and at most p−1; every remaining growth is exactly one. Since p−5≥2, the first remaining increment d makes the initial four points a d-interval by E1; P4 makes the first pair ±d and ±2d. The resulting interval has length5. Every later addition starts at length between5 and p−2, so E2 makes all subsequent increments ±d. This proves exhaustive TypeII necessity, while the all-parallel case is TypeI. The p=7 endpoint is included: there are two remaining additions, with the final one starting at length5=p−2.

For TypeI, translate the negative factors and sum p−3 copies of {0,d}:

    U=−md+{0,...,p−3}d,
    F_p\U={−(m+1)d,−(m+2)d}.

For TypeII, negative factors translate by−(m+2η)d=−qd. The positive sum is

    {0,...,p−4}d+{0,2d}={0,...,p−2}d,

because p−4≥3. Its only missing residue is−(q+1)d. Hence zero is absent from B+U exactly when B is one of the two TypeI offsets or the one TypeII offset printed in(5). This establishes sufficiency as well as necessity and EVERY missing residue, not just cardinalities. Under d↦−d, m↦p−3−m in TypeI and q↦p−2−q in TypeII, giving the same offset sets as claimed.

## 2. Actual-K / actual-word bridge (author lines102–142)

The group law in the actual selection boundary is

    (v,e)(v',e')=(v+ev',ee').

For a fixed actual rotation set K, telescoping rotations around the ordered reflections conjugates σ_y to σ_(y+2s_K), without commuting any selected letters. With an even number C of reflections, the product is exactly

    ρ_(S_K+z_(j1)^K−z_(j2)^K+...−z_(jC)^K).

This reconstructs predecessor LemmaG at the displayed actual indices. For even k=|K| between2 and p+1, C=2p−k is even. Selecting one actual occurrence in each ordered noncrossing packet leaves every packet rank fixed. Each binary switch changes only its signed coordinate by δ_i; its attainable set is precisely the scalar B+Σ{0,δ_i}. Zero membership therefore yields a selection of exactly k+C=2p ORIGINAL positions and the identity group element.

With t=p−3 binary packets, exactly C−t=p+3−k singletons are needed. This ranges from2 to p+1 over the allowed k. An adjacent unequal-gauge matching of size p−3 uses2p−6 reflections, leaving F−2t=p+4 actual outside reflections, sufficient for every required singleton count. Reflection-subsequence adjacency prevents a filler from crossing a selected pair; intervening SELECTED rotations are allowed because the gauge already transports them. All sign/offset tests are recomputed for each actual filler arrangement, not reused with a fixed sign frame.

For F=3p−2, ν_K=(F−o_K)/2, so o_K=p+4 indeed gives ν_K=p−3. The theorem also correctly applies to nonmaximum p−3 matchings whenever they exist. Every-K/every-cut quantification remains necessary for an all-selection avoider, not an assertion that one successful-looking local profile gives an actual avoider. Original-cut restoration by conjugation preserves exactly the same chosen positions and identity; labels must be recomputed on the cut, as stated.

## 3. The two-singleton gap tests (author lines144–196)

With all p+1 rotations selected, C=p−1 and t=p−3 pairs leave exactly two singleton slots. If both singletons u<v lie in gap j after j pairs, earlier pair ranks do not change and later ranks shift by TWO. Thus all pair signs and δ_i stay unchanged. The two singleton signs are (−1)^j and−(−1)^j, giving exactly

    B_j(u,v)=S+P+(−1)^j(z_u−z_v).

Substitution in the already-verified offset formulas proves TypeI E_j in(8) and the ordered difference condition(9), including signs. TypeII gives the single difference c_j in(10). This equivalence concerns those same-gap packet families only; the general DS3 condition still retains different-gap fillers.

For D2 with0∉E, three increasing indices give a,b,a+b∈E. If a,b differed, their sum could equal neither without a zero element, so a=b=c and E={c,2c}. Four indices force three consecutive differences c, while the total3c is neither c nor2c for p≥7. Thus at most three entries occur. With E={0,c}, three distinct list values would yield consecutive differences c,c and total2c, impossible. A return after an a→b switch produces−c∉{0,c}; the two-value constant-block order is therefore forced. The TypeII three-entry argument is equally exact: c_j+c_j=c_j forces c_j=0 and all labels equal. Empty/singleton gaps impose no fictitious pair condition.

## 4. Historical overlap, trust and actual remaining target

The historical ARC statement at old lines71–78 varies ordered arcs and invokes Cauchy–Davenport inside its length4p−2, one-nonzero-rotation-pair, all-odd setting. ETA at old lines130–144 uses y_j/2 plus prefix rotation mass, additionally at B=0. This confirms the new author's explicit overlap credit. The new finite-field inverse/offset and fixed-K gauge proofs do not invoke ARC/ETA, S(p), Lev, EGZ, Davenport, index-one or a historical computation as premises.

The actual updated residual B3=B2\DS3 is defined as a complement of proved sufficient actual-word classes. The manuscript explicitly supplies no strict new B2 member covered by DS3 and makes no nonemptiness or relaxed-feasibility claim. It leaves both ν_K≤p−4 branches and universal profile compatibility across distinct K/cuts unproved. The entire MIX / unrestricted prime-dihedral / all-finite-group ordered target remains open in this work. This scope discipline is correct and must accompany any internal written-check promotion.

## Verification boundary

This is a written reconstruction of the complete pinned candidate at its supplied actual-word and inherited residual interfaces. No scientific program, finite-parameter test, solver, enumeration, compiler, Lean/kernel, old checker or modelCLI was used. Import trust, novelty, significance and whole-target resolution remain separate. The assigned bounded review is complete; I return to Sun8's own prime-seven structural obstruction.
