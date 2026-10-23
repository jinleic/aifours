# ASSEMBLY-P parent summary and residual erratum v1

Recorded at 2026-10-19T12:01:26-0700. Read after immutable proof `059033b00b669e10f0fa49bdb2fdb55a135a85644f792ef2b3b3d6eb61dacfb5` and package `606bfdc3906ddd610454218b05b536a888ef50771a68610925e481133babc365`. Disposes Codex `59d1d744a77f45fb6790f4da5c70f787a849f6e4621074b4c7c627a2955a3a22`: six implications ACCEPT at their exact conditions,0F/0M/3MINOR summary/residual issues. This overlay changes no theorem statement, case split or main proof step. Pending ONE-SHORT-LS/ROT-SING remain pending. Every Old span occurs exactly once.

## m1 summary scope

Old:
````text
1. Normal form (rows NF, GRX, DAV): every avoider of length 4p-2 has an admissible normal form; every one has
   1 <= k <= o_F <= p (Sec. 5).
````

New:
````text
1. Normal form (rows NF, GRX, DAV): every avoider of length 4p-2 WITH o_F <= p has an admissible normal form; every one has
   1 <= k <= o_F <= p (Sec. 5).
````

## m2 endpoint table

Old:
````text
| k = p, kappa^ = p-1 | none accepted | [ROT-SING] | no | no |
````

New:
````text
| k = p, kappa^ = p-1 | no accepted uniform route asserted from ZP alone; ROT-KP+ remains applicable if actual (S1_(p-1)) holds | [ROT-SING] for the uniform route used here | no | S(p) only if the optional ROT-KP+ route is invoked |
````

## m2 inverse residual outer bound

Old:
````text
Without
[ROT-SING]: avoiders with o_F = p = F.
````

New:
````text
Without
[ROT-SING], an outer bound for the inverse-theorem residual is avoiders with o_F = p = F; ROT-KP+ already covers any such avoider whose rotation sequence satisfies (S1_(p-1)).
````

## m2 word residual outer bound

Old:
````text
Word level of length 4p-1: by (B0), only words
with o_F = p and kappa(w) in U(p) u {p-1} need a premise.
````

New:
````text
Word level of length 4p-1: words
with o_F = p and kappa(w) in U(p) u {p-1} lie outside the stated P0 criterion; this is not a claim they need a pending premise. In particular F=p gives R=3p-1, so EGZ twice yields disjoint p-term zero-sums among rotations and hence an ordered identity 2p-subword without a pending premise.
````

## m3 remove uncertified endpoint description

Old:
````text
ROT-SING+ (pending) states
  the cell k = p+1, kappa^ = p-1.
````

New:
````text
The k = p+1 endpoint is a separate candidate outside this review packet; no statement from it is used or certified here.
````

## m3 restrict reflection residual to supplied interface

Old:
````text
- Reflection half: restricted REFL needs o_F <= p. By RED, REFL(p) is equivalent to "no avoider in RES_<(p) with kappa >= 2";
  the small-k verdict excludes RES_<(p) with k <= p; RES_<(p) with k >= p+1 is open. REFL(p) is OPEN.
````

New:
````text
- Reflection half: the supplied restricted REFL interface needs o_F <= p. This assembly proves no extension beyond that range; the unsupplied RED/small-k interfaces are not certified by this packet.
````

