# Billhardt condition: source statement and bounded encoding

Date: 2026-10-14 (PT). This resolves the HMZ reviewer's source/encoding audit objection. No solver run is repeated here and no new nonembedding claim is made.

## Exact source statement

Hartmann, *E-Unitary Covers over Group Varieties*, Semigroup Forum 70 (2005), 61–70, DOI [10.1007/s00233-004-0138-9](https://doi.org/10.1007/s00233-004-0138-9), §4, Theorem 6 (credited there to Billhardt [1]):

> If S is an embeddable E-unitary regular semigroup and a, a′, b, b′, e, f, g ∈ S are elements satisfying
>
> (N1) a σ b, a′ ∈ V(a), b′ ∈ V(b) and e, f, g ∈ E(S),
>
> (N2) eaa′ = e, ebb′ = e,
>
> a′afg = fg, b′bfa′eafg = fa′eafg
>
> then
>
> (N3) eafg = ebfa′eafg.

This is a transcription with line breaks, spaces and the extracted private-use prime glyph normalized; no mathematical symbol, premise or conclusion has been changed. The exact pre-normalization bytes returned during the actor's web call are retained in `sources/hartmann2005-theorem6-tool-excerpt.txt`; its timestamp, original public URL, extraction provenance and hash are in the adjacent JSON file. The actor had read public author-uploaded text. A later static fetch gave HTTP 403 and an ordinary unauthed browser opened a challenge page; neither was bypassed. Therefore this is not described as a new successful direct fetch of the journal article.

There is also an independently accessible **author thesis** corroboration: Hartmann, *Ortodox félcsoportok és szemidirekt szorzatok* (2007), chapter 3, Theorem 3.4, printed p. 18 / PDF p. 20, has the same (N1)–(N3) formulas. The public [University of Szeged PDF](https://doktori.bibl.u-szeged.hu/id/eprint/1183/1/HM_dissz.pdf) was fetched successfully and is saved as `sources/hartmann2007-thesis.pdf`. It is in Hungarian; the displayed English sentence above comes from the retained 2005 article output, not an invented literal translation of the thesis.

## Mapping to the preserved Python source

All line numbers below refer to the delivered unchanged `search_obstruction.py`.

| Lines | Meaning |
|---|---|
| 27–29 | Z2 grading: even·even and odd·odd are even; mixed products are odd. |
| 30–31 | Every even element is idempotent; odd elements cannot be idempotent by grading. Thus the even part is exactly E(S). |
| 32–33 | Associativity on all triples. |
| 34–36 | Every odd element has a mutual inverse; even elements are their own inverses. |
| 38–42 | The local regular-band identity for the even band, using exact local-membership equalities. |
| 50 | `e,f,g=0,1,2`: **three pairwise distinct** even elements, not arbitrary possibly coincident elements. |
| 51 | `a,b,ap,bp=NE,…,NE+3`: **four pairwise distinct** odd elements. |
| 52 | `a′∈V(a)`, both inverse equations. |
| 53 | `b′∈V(b)`, both inverse equations. |
| 54 | `eaa′=e` and `ebb′=e`. |
| 55 | `a′afg=fg`. |
| 56 | `b′bfa′eafg=fa′eafg`. |
| 57 | Negation of conclusion (N3). |

For the remaining (N1) hypothesis `a σ b`, every homomorphism `γ:S→H` to a group sends idempotents to `1`. The inverse equations give `γ(a′)=γ(a)⁻¹`, and the odd·odd grading makes `a′b` even/idempotent. Hence `1=γ(a′b)=γ(a)⁻¹γ(b)`, so `γ(a)=γ(b)`. In particular `a σ b` in the greatest group image. This argument does not silently assume that the chosen Z2 grading is the least group quotient.

The encoded graded regular orthodox semigroup is E-unitary: multiplying an odd element by an even idempotent remains odd, so cannot produce an idempotent; the left and right E-unitarity conditions follow. The local regular-band test then gives local r-orthodoxy in this orthodox setting.

## Why the condition transfers to B ⋊ H

This is a source-dependent coordinate derivation/encoding check, not a new independent proof of Billhardt's band quasiidentity. Let `φ(s)=(β(s),γ(s))` embed `S` into a band-by-group semidirect product, so

`β(xy)=β(x)·^{γ(x)}β(y)`.

Since `a σ b`, let `h=γ(a)=γ(b)`; both inverse grades are `h⁻¹`. Introduce the following actual elements of `B`:

```
A=β(a), A′=^hβ(a′), B₁=β(b), B₁′=^hβ(b′),
E=β(e), F=^hβ(f), J=^hβ(g).
```

The inverse equations become `AA′A=A`, `A′AA′=A′` and their `B₁` counterparts. Expanding the first two premises in (N2) gives `EAA′=E=EB₁B₁′`. Applying `^h` to the base equations of the remaining grade-one premises gives

`A′AFJ=FJ`,

`B₁′B₁FA′EAFJ=FA′EAFJ`.

Thus these seven elements satisfy the same (N1)–(N2) premises **in the band B**; the least group image of a nonempty band is trivial. The quoted theorem's band specialization (bands embed by `b↦(b,1)` into `B⋊{1}`) gives

`EAFJ=EB₁FA′EAFJ`.

These are the two base coordinates of (N3), while their group coordinates are both `h`. Injectivity of `φ` gives (N3) in `S`. The only cited mathematical input in this reduction is precisely the displayed Billhardt condition for bands. No source-free algebraic proof of that quasiidentity is claimed, and none of the Lean roots asserts it.

## What the two unsuccessful searches establish

- **7 even + 4 odd:** UNSAT for the single encoded distinctness pattern; no case in which any two of `e,f,g` coincide, or any two of `a,b,a′,b′` coincide, was searched. There is no proof-logged UNSAT certificate.
- **9 even + 8 odd:** UNKNOWN after the solver timeout; no exclusion follows.
- Neither run establishes the absence of all counterexamples of its cardinality, embeddability of any class, or a solution of P1. The old 357 construction checks and 48 embedding certificates were not rerun.
