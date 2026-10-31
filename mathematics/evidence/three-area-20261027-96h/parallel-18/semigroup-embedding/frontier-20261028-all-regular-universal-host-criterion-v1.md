# Every regular source has one universal physical-host actor

**Status: NEW AUTHOR WRITTEN CONDITIONAL ON NAMED UNIVERSAL/GUAGE PROOFS; UNREVIEWED / UNADOPTED.** This removes the actual-syntactic-q-is-CS hypothesis from the arbitrary-actor reduction by using the least CS quotient. It is an exact criterion, not a proof that the criterion always holds for original sources.

## 1. Exact theorem for arbitrary regular S

Let S be any nonempty regular semigroup, finite or infinite, and let `η:S→Dν=S/ν` be its universal/least CS quotient, constructed in `frontier-20261028-universal-cs-group-presentation-v1.md`, SHA `22f600563e2edf428ed122050c2cf95472078edb70a265c468d89535a005f16c`. Let V be an isomorphism-closed class of bands. Then:

**S has a faithful physical V-band-by-CS host with a band B iff it has one over η using the SAME band B, possibly with a different local-group action.**

Indeed, the actor map r:S→D₀ of any host factors uniquely through η by the universal property, `r=hη`. The general same-band lifting lemma in `frontier-20261028-finest-actor-same-band-lift-v1.md`, SHA `fa8bcc7beb069fbe873380429415f9c90723420a241abd078fe206973d1d8c3c`, applies to ANY CS hom h without purity or onto assumptions. It transforms source coordinates by the inverse Rees row gauge, restricts the group action through the local-group homomorphism, and preserves the identical B and source injectivity. The reverse is immediate because Dν is CS. No q-purity, q-CS, weak-E, local-r, or actor-coinduction input is used. □

If a faithful host exists then η must be pure: if η(s) is idempotent, then r(s)=hη(s) is idempotent, so the physical source image is idempotent; faithfulness forces s²=s. Therefore a **nonpure least-CS quotient is an absolute obstruction** to a physical band-by-CS host, independent of the band variety. For regular S this is equivalent to its actual idempotence-context quotient not being CS, by the separate least-CS note.

## 2. Canonical exact criterion

For a variety V of bands (in particular SN), form the canonical V-band product over η by all group/source mixed relations. Its universal mapping property gives

`S has some physical V-band-by-CS host  ⇔  κ_η is injective`.  (1)

If η is not pure then κ_η cannot be injective: choose nonidempotent s with η(s) idempotent; the physical image κ_η(s) is idempotent, so κ_η(s²)=κ_η(s) with s²≠s. If η is pure, the earlier direct idempotent-separation lemma applies, so (1) is equivalent to separation by its band coordinate of every pair of distinct idempotents in the same η-fibre. The named canonical construction and quotient identities remain explicit prerequisites; no separation property is proved here.

This criterion uses a universally finest CS actor on every regular source. When original source assumptions imply pure-CS actual q, Dν is exactly the finest pure actor q̂ from the predecessor theorem. It is not generally the coarsest actual actor q, and band minima may differ between them, as S68 demonstrates.

## 3. Finite decision and optimization, with no source-class precondition

For a finite regular input S, ν is computable by enumerating all congruences, retaining those with CS quotient and intersecting them; its quotient is CS by the universal theorem. Its Rees group G is finite and `|G|≤|S|`. The canonical V-band over η, for V=SN, is a quotient of the free band on `|G||S|≤|S|²` generators; Green–Rees makes it finite. Hence source injectivity and existence of any SN-band-by-CS physical host are decidable by a terminating finite computation for EVERY finite regular S, even when it is not weakly E-unitary or locally-r. This is not a feasibility/complexity claim.

If (1) holds, the exact minimum band cardinality over all actors is obtained by enumerating every G-invariant congruence θ of that finite canonical band for which the induced η-source map stays injective, and minimizing the quotient size. Completeness follows from the SAME-band theorem and the finite action-generated subband of any host. If (1) fails no such host exists. This is a decision of one finite multiplication table, not a resolution of the all-source original question.

The physical convention, Rees representation, regular-image CS theorem, universal η proof and same-band gauge are the actual named dependencies. No complete printed-question equivalence, formal proof, novelty or independent review is claimed.
