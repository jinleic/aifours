# The four-term obstruction does not localize to locally regular bands

**NEW AUTHOR WRITTEN + EXACT FINITE-CHECKED COUNTERMODEL; unreviewed/unadopted.** Native observation **Wed Oct 28 18:42:21 PDT 2026**. This is an additive scope boundary to `frontier-20261028-all-cs-globally-regular-band-obstruction-v1.md`, SHA `2f9f6a68a153449b61cda78305174c5b601e28fba49ec391bc1107aaba8e31af`. It does NOT change that note's globally regular result, construct a faithful source host, or decide the original locally regular target.

## 1. A five-element locally regular countermodel

Let B={0,1,2,3,4}, with multiplication table

```text
0 2 2 4 4
0 1 2 1 4
0 2 2 2 4
0 3 2 3 4
0 4 2 4 4
```

All5 squares are correct, and all125 associativity equations hold. Its local corners are exactly

```text
0B0 = {0}
1B1 = {1,2,4}
2B2 = {2}
3B3 = {2,3,4}
4B4 = {4}
```

The two nontrivial corners are the right-zero band on {2,4} with an identity (1 and3 respectively); hence every corner is a regular band. However B itself is NOT a regular band: for x=1,y=0,z=3, the two sides of `xyxzx=xyzx` evaluate to2 and4 respectively.

Put `x=0`, `u=1`, `v=3`, `y=1`. Direct table products give

`uv=u`, `vu=v`, `E=xuy=2`, `F=xvy=4`,
`EF=F`, `FE=E`, and `E≠F`.

Therefore the four-term lemma in §3 of the globally-regular obstruction is FALSE if global regularity is weakened to mere local regularity. One cannot move the lemma to the original permitted band variety without genuinely new information.

Both E and F have common natural-order upper bounds 1 and3; nevertheless the full set of inputs {x,u,v,y} has no common upper bound in B. Thus merely putting E and F in a common regular local corner does NOT put the intervening four terms in that corner or establish the lemma. Conversely, if a common upper bound of all four inputs existed, they and their products would lie in its regular corner, and the lemma would apply.

## 2. The nontrivial group action does not by itself repair the argument

The involution `α=(1 3)(2 4)` fixing0 is a band automorphism. For the notation of the global obstruction, take

`U=3`, `V=1`, `Z=3`, `X=0`.

Then `UV=U`, `VU=V`, while

`X α(U) α(Z)=2`, `X α(V) α(Z)=4`.

These two values form the distinct right-zero pair E,F above. This realizes the **specific abstract band equations and C2 action** used in the attempted obstruction. It is NOT a homomorphism of the full 45-element source and is NOT evidence that the source embeds into this band-by-CS product. Other source relations may still force equality in its actual canonical band; that remains open.

## 3. Exact checking and limits

`frontier-20261028-local-four-term-countermodel-checker-v1.py`, SHA `9f3e60cc23fcac26ee0bc965646c6f2303bce1e6006a0a755a510596de6511d3`, ran at **Wed Oct 28 18:42:21 PDT 2026** with `/opt/homebrew/opt/python@3.14/bin/python3.14 -B`, exit0. It checks all band idempotence/associativity cases, the five exact corners and each corner's full regular-band identity, the involution and all25 automorphism equations, the displayed global failure, all four-term products and both upper-bound sets:

```text
PASS B order5, 125 associativity cases, all local corners regular
corners=[(0,), (1, 2, 4), (2,), (2, 3, 4), (4,)]; global regular identity failure x,y,z=(1,0,3)
u,v=13 E,F=24 uv,vu,EF,FE=1342
C2 involutory automorphism=(0, 3, 4, 1, 2); common-upper all inputs=[] E/F=[1, 3]
```

The compact numeric strings on the third line are the checker's actual unseparated output: they mean u=1,v=3,E=2,F=4 and products1,3,4,2 respectively.

The example was discovered by the bounded local solver `frontier-20261028-local-four-term-lemma-search-v1.py`, SHA `3002d0e7da2c3d3e076f35535c3f99102cbfc7a7aeb35021fe6246c054fa66ad`, which reported a satisfying five-element structure at18:41:32. The literal verifier does not import the solver. No lower bound, global source nonembedding, independent witness review or formal proof is claimed. The exact open issue is whether the ENTIRE original source presentation forces the same-q R pair to collapse in the locally regular canonical band, not whether the four displayed equations alone do so.
