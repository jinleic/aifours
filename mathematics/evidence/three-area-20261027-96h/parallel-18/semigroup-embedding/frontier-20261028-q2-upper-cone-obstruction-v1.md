# An upper-idempotent-cone obstruction to generalized Q2

**Status: NEW AUTHOR WRITTEN NECESSARY CONDITION, plus exact finite control; UNREVIEWED / UNADOPTED.** This is a result about the precise natural target: an embedding into an idempotent-separating homomorphic image of a physical band-by-completely-simple product. It is not a claim about every possible interpretation or extension of printed Q2, or a counterexample to Q1's weakly E-unitary hypotheses.

## 1. Upper-cone theorem

Let V be any variety of bands, and suppose an arbitrary semigroup S embeds in U, where `π:H=P(B,D)→U` is an onto idempotent-separating homomorphism, B∈V, and D is completely simple. Then, for every idempotent z∈S,

`↑z = {e∈E(S): ze=ez=z}`

is a subsemigroup of S and in fact embeds as a **band in V**. This is a necessary condition, not a claimed sufficient one. No regularity assumption on S itself is used.

Proof. The full physical product H is regular (explicit inverse formula in `frontier-20261028-generalized-fact2-local-r-upper-bound-v1.md`, SHA `d7bab22d7c6f0ea6e6984a2c0d868aa430d0a436e54777470bb816615cd79baf`). Each idempotent of U has a unique idempotent lift: existence follows by taking x with π(x) idempotent and an inverse y of x², so xyx is idempotent and has the same image; uniqueness is idempotent separation.

We use the standard regular-semigroup fact **an idempotent-separating congruence is over groups**: each congruence class containing an idempotent is a group. It is explicitly stated in Szendrei's 2019 survey §2, <https://arxiv.org/html/1909.05280v1>; we import it at that scope rather than deriving it from the finite control. It implies reflection of the natural order between idempotents: if e,f∈E(H) and `π(e)≤π(f)`, then both ef and fe lie in the π-class of e, a group with identity e. Thus `(ef)e=ef`, making `(ef)²=ef`; idempotent separation gives ef=e. Similarly `e(fe)=fe` makes `(fe)²=fe`, and then fe=e. Hence e≤f.

Identify S with its image in U and write `z̃` for the unique lift of z. For any e∈↑z let `ẽ` be its idempotent lift. Order reflection gives `z̃≤ẽ`. The actor projection H→D preserves idempotent order, and distinct idempotents of a completely simple semigroup cannot be comparable. Thus every `ẽ` has the SAME actor idempotent d as z̃. Write `ẽ=(b_e,d)`. At this actor idempotent, the physical group weight is 1, so for any e,f∈↑z,

`ẽf̃=(b_e b_f,d)` is idempotent.

Its image ef is idempotent, and `z(ef)=(ze)f=zf=z=(ef)z`; hence ef∈↑z. Its unique lift is ẽf̃, so `e↦b_e` is an injective semigroup homomorphism from ↑z into B. Since a subsemigroup of a band is a band, and V is closed under subbands, ↑z is a band in V. □

The argument does not require the host actor to equal an actual syntactic quotient of S. It applies to **every** permitted completely simple actor, including infinite actors and nontrivial group actions. For V=SN each upper cone must itself be a seminormal band. This is a new dual-side condition beyond the lower local-corner condition; we do not claim it is sufficient.

## 2. A nine-element locally inverse counterexample

Let `D=M[C₂;{0,1},{0,1};P]`, with `P_(λ,i)=λi` in additive bits, and let `S=D⁰` be D with a new absorbing zero. S is regular. Each nonzero local monoid is a group with zero adjoined, and the 0-corner is trivial, so S is locally inverse and hence locally r-orthodox.

The idempotents of D in cells `(0,0)` and `(1,1)` are `e=(0,0,0)` and `f=(1,1,1)`, but `ef=(0,1,1)` is not idempotent. Since the new 0 is below every idempotent, `↑0=E(S)` is not closed. By §1, **S cannot embed in an idempotent-separating image of any physical band-by-CS product, for any band B or CS actor**. Thus locally r-orthodoxy alone is not sufficient for this natural generalized Q2 target. S is outside Q1's original weak-E class: 0 lies below nonidempotent elements.

The exact Python eval-kernel control `frontier-20261028-q2-zero-nonorth-control-v1.py`, SHA-256 `d97741b0b7f64fae534558aa811c3651e72c98821ce06a6abb533fbb17dcada2`, completed before Wed Oct 28 21:35:06 PDT 2026. It checks all 729 associativity triples, all five idempotents, inverses for every element, commuting local idempotents in every corner, zero below all idempotents, and the stated nonidempotent ef. The universal no-host conclusion comes from §1, not from that finite search.

## 3. A conditional exact boundary for zero semigroups

For any regular S with zero, §1 with z=0 says membership in the seminormal-band generalized target forces S orthodox and E(S) seminormal. Conversely, the source-dependent candidate `frontier-20261028-orthodox-q2-band-variety-characterization-v1.md`, SHA `3ce438c1814af2211eb0f5927730bf27c32fe1c6c76038c5c14a7751caf7e375`, would embed every such orthodox S in an idempotent-separating image of a seminormal-band-by-group product. Thus, **conditional on the Hartmann thesis proof import and its source-interface review**, the zero-source subclass has an exact iff: orthodox and E(S) seminormal. If the separate locally-regular/SN candidate and its mandatory erratum are reviewed, this is equivalently orthodox plus locally r-orthodox. Do not conflate this conditional sufficiency with the independently written upper-cone necessity or claim an all-source characterization.
