# Exact full-band comparable separation via the Horn semilattice quotient

**Status: NEW AUTHOR WRITTEN REDUCTION, with predecessor's exact finite control; UNREVIEWED / UNADOPTED.** This strengthens `frontier-20261028-canonical-semilattice-horn-separation-v1.md`, SHA `a9d9fe413a08e876bfbf51d6f573e1a83d1e5e74bc9042d495bb3785719e51f3`: its warning that semilattice collapse need not imply SN-band collapse remains correct for arbitrary/R/L pairs, but **for same-actor comparable idempotents the two collapses are equivalent**. This is not the missing R/L separation theorem and not a general Q1 resolution.

## 1. General band lemma

In any band B, the Green–Rees D relation is its least semilattice congruence, and each D-class is a rectangular band. This is a named standard import (see, e.g., the Green–Rees account in <https://www-users.york.ac.uk/~varg1/2023_11_08_York_Semigroups_Computing_in_Free_Bands-corrected.pdf>; the fact is applied here to arbitrary bands). If x≤y in the natural band order, `xy=yx=x`. If x and y belong to the same rectangular D-class, those two equations force the same row and the same column, so x=y. Consequently

`x≤y and x≠y  ⇒  [x]_D≠[y]_D`.                    (1)

In particular the maximal semilattice quotient separates EVERY distinct comparable pair of a band. This assertion is universal, not a sampled finite observation.

## 2. Application to the canonical band

Let S be a finite semigroup with a specified homomorphism to finite `D=M[G;I,Λ;P]`. Let β be the source coordinate in the canonical SN band B, and let e,f∈E(S) have `r(e)=r(f)=d` and e≤f. Since d is an idempotent actor, its physical self-weight is the identity, so the source equations `ef=fe=e` yield

`β(e)β(f)=β(f)β(e)=β(e)`.

Thus `β(e)≤β(f)` in B. By (1), `β(e)=β(f)` **iff** their images in B/D are equal. The latter quotient is exactly the semilattice presented by the source mixed-product relations of the predecessor, since imposing semilattice identities on the canonical SN-band presentation gives the semilattice reflection. Therefore the singleton Horn closures of that predecessor decide **exactly**, not just sufficient-condition-wise, whether the full canonical SN band separates this particular comparable pair.

In particular, a semilattice quotient collapse of distinct comparable same-r idempotents proves canonical β actually collapses them. By the universal property of the canonical band, no physical SN-band host **over this same r** can separate them. For an arbitrary-actor no-host conclusion one must separately import the actual-q pure-CS actor-transfer theorem, at its exact hypotheses; it is not used implicitly here. For unrelated or same-q R/L incomparable pairs, semilattice collapse need not imply β collapse, as the predecessor's 45-source control illustrates.

The Horn formulation uses n=|G||S| variables and m=|G||S|² mixed triples, with all singleton closures obtained in O(n(n+m)) rule activations under the stated adjacency accounting. Thus it decides *all same-r comparable pairs in the full canonical band* with polynomially many Horn operations on the input tables, without constructing the exponentially larger band. It does not decide all-source injectivity or R/L separation.

## 3. Existing exact control and full scope

The predecessor's final same-author Python-kernel control `frontier-20261028-semilattice-support-horn-v1.py`, SHA `01f0c7846cefa890192081c7ab4889ae9673ec76ec20bc985caa9396abaea88d`, checks the 45-source/18-actor instance. All 12 ordered distinct same-q comparable idempotent pairs are separated in the semilattice quotient; (1) shows that this is **the exact answer for their full canonical-band separation**, not just a sufficient test. All 18 same-q distinct R/L pairs collapse in the semilattice quotient even though the separately exhibited noncommutative host separates them, confirming that the comparable hypothesis cannot be omitted.

This result turns a single-source comparable-separation question into a finite Boolean/Horn certificate and, conditionally on reviewed actor transport, an all-actor obstruction certificate if a collapse occurs. The 45-source outcome is positive and is not a counterexample. No universal property of all WEU locally-r sources, SN R/L separation, printed-product equivalence, independent review, formal proof or novelty conclusion is claimed.
