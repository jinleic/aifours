# A nonweak-E, nonorthodox explicit idempotent-separating Q2 image

**Status: NEW AUTHOR WRITTEN with exact finite kernel control; UNREVIEWED / UNADOPTED.** This is a concrete instance of a specified generalized Fact2 target, not a general Q2 result or an original-Q1 source.

Let D be the 8-element completely simple semigroup from `frontier-20261028-straight-locally-inverse-q2-v1.md`, SHA `61fde8c421f151c0a526c559ba49a7f6df845fbf7ed478410e9d477607226699`: `D=M[C₂;{0,1},{0,1};P]`, with `P_(λ,i)=λi` in additive bits. Let `C₂⁰={0,1,t}` be a group C₂ with an absorbing zero adjoined, `t²=1`. Let `L={0,1}` be the two-element semilattice and let the group `C₂×C₂` act trivially on L.

Set `H=P(L,D×C₂)`, so H is the direct product of L and the completely simple actor `D×C₂`, and define

`π(b,d,g)=(d,0)` if `b=0`; `π(b,d,g)=(d,g)` if `b=1`.

The target `U=D×C₂⁰` has 24 elements; H has 32. Since zero absorbs and the band coordinate is meet, π is a surjective homomorphism. The idempotents of H are exactly `(b,e,1)` for `b∈L, e∈E(D)`, and their images `(e,0)` and `(e,1)` are all distinct. Hence π is **idempotent-separating** and noninjective; U itself is the required image, with semilattice (thus seminormal) band and CS actor.

U is regular, locally inverse, nonorthodox and **not weakly E-unitary**. Specifically, `e=((0,0,0),0)` is idempotent and below `x=((0,0,0),t)`, because `ex=xe=e`, but `x²=((0,0,0),1)≠x`. For nonorthodoxy, `(e₀₀,1)` and `(e₁₁,1)` are idempotent while their product is not, since `e₀₀e₁₁` is not idempotent in D. Local inverse follows because each local monoid is the product of a local group of D and a local inverse submonoid of C₂⁰. Thus this positive Q2 instance lies outside the WEU source class of Q1 and outside the orthodox class simultaneously.

The exact Python-kernel script `frontier-20261028-nonweu-nonorth-q2-control-v1.py`, SHA-256 `5f9fa163a5a3c24d3a55bde73f26d5b5ba06dc243828332bd063675d9859b06c`, completed before Wed Oct 28 21:33:20 PDT 2026. It checked all 1,024 ordered multiplication pairs of H under π, surjectivity to U, injectivity on all eight idempotents, inverses for each U element, and the displayed non-WEU and nonorthodox witnesses. No source theorem, nonstraight assumption, novelty, or independent review is needed for this finite construction.
