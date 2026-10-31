# Band-block completion forced by ANY idempotent-separating host image

**Status: NEW AUTHOR WRITTEN NECESSARY REPRESENTATION + finite certificate algorithm; UNREVIEWED / UNADOPTED.** This concerns an embedding into an idempotent-separating homomorphic image of a physical band-by-CS product. It is not a characterization of the largest regular class in Q2 and not a negative answer to originalQ1.

## 1. An entire band partition is necessary, not merely individual upper cones

Let arbitrary S embed in U, and let `π:P(B,D)→U` be onto and idempotent-separating, with B in a band variety V and D completely simple. The physical host is regular, as reconstructed in `frontier-20261028-generalized-fact2-local-r-upper-bound-v1.md`, SHA `d7bab22d7c6f0ea6e6984a2c0d868aa430d0a436e54777470bb816615cd79baf`. Its source-independent idempotent lifts are unique: lift a preimage x of an idempotent image, choose z inverse to x², and xzx is an idempotent in that image class; uniqueness is idempotent separation.

Import the standard fact that an idempotent-separating congruence on a regular semigroup is over groups, exactly as in the upper-cone predecessor. This gives ORDER REFLECTION for idempotent lifts. If π(e)≤π(f), then ef and fe lie in the group class with identity e. Its identities imply `(ef)e=ef`, `e(fe)=fe`, hence `(ef)²=ef` and `(fe)²=fe`. Idempotent separation forces ef=fe=e. Thus e≤f upstairs.

Identify S with its image and write e~ for each unique idempotent lift. For each actor idempotent d define

`Γ_d={e∈E(S): actor(e~)=d}`.

These nonempty sets PARTITION E(S). Every Γ_d is a subsemigroup and embeds as a band into B: for e,f∈Γ_d, the two lifts have the same actor idempotent, so their physical product has identity group weight and is `(b_e b_f,d)`, an idempotent lift of ef. Thus ef∈Γ_d and `e↦b_e` is an injective homomorphism. In particular Γ_d∈V. Distinct comparable source idempotents MUST belong to the same Γ_d, by order reflection and primitive CS idempotents. This holds for EVERY actor and action, finite or infinite, without assuming S regular or that its actor is its syntactic quotient.

Therefore a necessary source-side condition is:

`E(S) has a partition into V-subbands which identifies EVERY comparable idempotent pair.` (P)

This does not claim the partition is a source congruence, or that its cells are maximal subbands, or that (P) suffices for a host image. It is a constraint on E(S), not an illicit global assumption E(S) is closed.

## 2. A sound terminating finite obstruction procedure

On a finite source table, start the equivalence relation on E(S) by merging every pair e≤f. Repeat: for EVERY same-block pair e,f, its product MUST be idempotent and in the same block. A nonidempotent product is a no-host certificate. Otherwise merge ef into that block and continue until stable. At most |E(S)|−1 genuine merges occur. Finally check the required V-identities in every resulting block. Failure gives another no-host certificate; passing is ONLY a necessary-condition pass, not a host or source-admission theorem.

Every step is sound because any partition in (P) contains each initial pair and must contain all products of its own members. Equivalence closure and these mandatory product merges therefore stay inside the unknown actual Γ-partition. A nonidempotent forced product contradicts Γ being a band. A violated V-identity contradicts the resulting source subband embedding in Γ⊂B. The procedure outputs each merge with its comparable-pair or already-same-block product justification, so this is a finite replayable derivation, not a bounded search over host sizes.

## 3. Actual exact controls and honest strictness boundary

`frontier-20261029-Q2-forced-band-block-checker-v1.py`, SHA `3fe1252646e719629b4107f8d778f21e982efedc3555672c03ff78c0df47eca8`, completed before ThuOct29 02:21:16 PDT2026. Full merge traces and literal obstruction indices are in `frontier-20261029-Q2-forced-band-block-results-v1.json`, SHA `365cfe51be9f2707d0dc2326040f674b89f30a5aff279bf593e1d1864e2890a6`.

- Twisted D8 with zero: four mandatory merges, then idempotents0,7 have nonidempotent product3. This recovers the earlier upper-cone obstruction, not a second independent result.
- Twisted D8 with a FRESH IDENTITY: the same four merges force the same nonidempotent product. Yet EACH individual upper cone is a one- or two-element semilattice: the D8-idempotents are primitive, and the new1 is the only possible distinct element above each. Thus the partition condition is STRICTLY stronger than upper-cone closure ALONE. This nine-source is genuinely WEU but NOT locally orthodox; it does NOT show strictness beyond the COMBINED local-r and upper-cone necessary conditions, and is NOT an originalQ1 counterexample.
- D8 alone passes with four singleton blocks, as it should for a positive CS source.
- Pinned original S68 passes with blocksizes2,2,7,7,8,8 after28 merges. No canonical-band injection is inferred from this necessary test.
- The normal band N3={0,a,b}, with zero and {a,b} leftzero, passes the SN-block test with one block3 but fails the SL-block test because a,b do not commute. This recovers the exact distinction between allowing a normal/SN host band and requiring a semilattice host; N3 itself is a positive SN host.

The checker pins the S68 table SHA `64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf`; these are same-author exact finite controls, not independent certificate verification. The universal Γ-partition theorem is the written proof, not an inference from those cases. Original fullQ1 and largest-class Q2 remain open; source/product conventions, imported group-class fact and new theorem still require disjoint review.
