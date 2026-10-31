# Upper idempotent cones in band-by-completely-simple images

**Disposition: same-harness written support at the explicit construction and import boundary.** Let V be a variety of bands. Let `D=M[G;I,Λ;P]` be a completely simple semigroup, let `α:G→Aut(B)` act on a band `B∈V`, and take the full Cartesian product `H=B×D` with

`(a,(i,g,λ))(b,(j,h,μ))=(a α_{g p_{λj}}(b),(i,g p_{λj}h,μ))`.

If an arbitrary semigroup S embeds in an idempotent-separating homomorphic image of H, then for every idempotent z of S its upper cone `↑z={e∈E(S):ze=ez=z}` is closed under multiplication and is isomorphic to a subband of B, hence belongs to V. Regularity of S itself is not required. The actor and action may be infinite; no actor quotient of S is assumed.

A nine-element zero extension of a completely simple Rees matrix semigroup is locally inverse and locally r-orthodox, but its idempotents are not closed. It therefore embeds in no such image for **any** band B or completely simple actor of the displayed form. This is an obstruction for this generalized target, not a verified interpretation of printed Q2, not sufficiency, and not a counterexample to the original weakly E-unitary Q1 source class.

For a weakly E-unitary S every upper cone is automatically a band. If S is also regular and locally r-orthodox, its upper cones are locally regular and, using the separately [corrected band-identity disposition](math-4-local-regular-seminormal-band-equivalence-parent-v1.md), seminormal. The zero example is not weakly E-unitary. No Hartmann-based zero-source sufficiency, Q1/Q2 closure, novelty, human, independent-model-family or formal/kernel verification is claimed.

Native clock observed before composing: **2026-10-29T07:18:48-0700 PDT**; not a file-creation time.

## Parent reconstruction

The product H is associative by the group action law. Its regularity can be verified directly: for `x=(b,(i,g,λ))`, choose j,ν, set `w=g p_{λj}`, `h=p_{λj}^{−1}g^{−1}p_{νi}^{−1}`, and take `y=(α_{w^{-1}}(b),(j,h,ν))`. The band law and action identity give `xyx=x`, `yxy=y`. The actor idempotents are `d_{iλ}=(i,p_{λi}^{−1},λ)`; at one such fixed cell, the twist is 1 and `(a,d)(b,d)=(ab,d)`.

For a regular semigroup, the named [Szendrei survey, §2](https://arxiv.org/html/1909.05280v1#S2.p3) states that an idempotent-separating congruence is over groups. Parent read this statement directly; the review also reconstructs the needed direction. Every image idempotent has a unique idempotent lift: for an inverse v of x², `xvx` is idempotent and maps to the idempotent image of x, and idempotent separation gives uniqueness. If lifts e,f have ordered images `π(e)≤π(f)`, ef and fe lie in the group fiber of e. Its identity is e, so `(ef)e=ef` and `e(fe)=fe`, making both ef and fe idempotent; uniqueness forces `ef=fe=e`. Thus idempotent order reflects.

For a fixed z∈E(S), order reflection puts every lifted e≥z above the lifted z. Actor projection preserves that order, and completely simple idempotents are primitive, so all these lifts have one actor idempotent d. Their products are `(b_e b_f,d)`, hence idempotent; their images stay above z. Uniqueness of lifts makes `e↦b_e` an injective homomorphism into B. Closure under subbands gives the variety assertion.

For the concrete example use `D=M[C₂;{0,1},{0,1};P]` with `p_{λi}=λi` in additive bits and adjoin a zero. The idempotents `e=(0,0,0)` and `f=(1,1,1)` multiply to `(0,1,1)`, whose square is `(0,0,1)`, so the zero cone is not a band. Each nonzero local monoid is a two-element group with zero adjoined; the zero corner is trivial, so the example is locally inverse. The added zero lies below its nonidempotents, so weak E-unitarity fails.

For the WEU boundary, `z(ef)=(ef)z=z` whenever e,f≥z. This witnesses `z≤ef` in the natural order, so WEU makes ef idempotent and puts it back in the cone. If S is locally r-orthodox, each local band `e(↑z)e` lies in the regular band `E(eSe)`, hence is regular. The stronger seminormal conclusion uses the separate f144 corrected composite and its Green–Rees/content import; it was not independently proved by the f156 reviewer.

## Evidence and limitations

Parent read the complete 35-LF [upper-cone candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-20261028-q2-upper-cone-obstruction-v1.md), SHA-256 `283fb012e02f730a86aaa72ecbb77f695de5bd572c73dfeed794a0ab77e7720a`, followed by its complete 9-LF [WEU boundary](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-20261028-q2-upper-cone-weu-boundary-v1.md), SHA-256 `fb0f8f8ecaec11f3789c145a54b4e7cb1a2ea43291e96ced83017ff4a7eebc70`, and the complete 217-LF [f156 review](../review-waves/f156-semigroup-q2-upper-cone-obstruction/review-v1.md), SHA-256 `484160bddeac8f3cd802d964d028d90c6cb389ea599f6bbb6ae8f68d6dc71209`. Its [manifest](../review-waves/f156-semigroup-q2-upper-cone-obstruction/manifest-v1.json) is `a4b862a8a5fa78ce20686ae2df5aa0ed87d3d27081c473bfdd52097f1d86b9ef`.

The review found 0 FATAL / 0 MAJOR / 0 MINOR scientific findings. Its independent [v3 exact receipt](../review-waves/f156-semigroup-q2-upper-cone-obstruction/reviewer-control-receipt-v3.json), SHA-256 `a4e864031518b492cd923399c98e8c16d9baec9a341f191b0de500e6a8856d0b`, reports all 729 associativity triples, actual local corners and the nonidempotent product, plus a non-normal-band/nontrivial-action host and an idempotent-separating image. Earlier reviewer control attempts failed for reviewer-fixture and receipt-construction reasons and are preserved, not counted as successful evidence. A public source download also created `/tmp/f156/1909.05280v1.html` outside the assigned output directory; that process deviation is disclosed and the file is not deleted.

The construction above, Rees representation and over-groups lemma are the exact mathematical scope. Neither the candidate's conditional Hartmann sufficiency nor any prior held outcome is adopted.
