# Written consequence of the two §4(3) finite candidates

This is a source-hypothesis audit and written consequence, not a Lean/formal proof or a re-proof of the
imported existence theorem. Parent verification, hostile mathematical bridge review and priority review
remain separate. No novelty or met-gate claim is made here.

Authority: Tan–Zhou arXiv:2503.11934v1, pinned text `sources/tz/tan-zhou-2503.11934.txt`, SHA-256
`df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164`. LF lines are used below; the exact
LaTeX source is also pinned under `sources/tz/` (SHA `ca37944c…9550`).

## Finite inputs actually supplied

| Required object | Raw certificate | SHA-256 |
|---|---|---|
| gcDCQS(18⁴:2) | `evidence/gcdcqs18-z8z3z3/gcdcqs18_4_2_z8z3z3.txt` | `1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e` |
| FDGDD(3,4,5{18}) | `evidence/fdgdd18-d15-inflated/fdgdd_5_18_inflated_D15.txt` | `3e22f5021631ac82ea5b5fa6f884984bb874f1f9a384fd35bfeff523e731a998` |
| mcDSQS(20), also gcDSQS(20,2) | `sources/sxk/sxk_prop3_transcription.json` (cyclic development plus ten cells) | `3610b32c75738348751c4f58dd9243358e66c2b72d2a15d80bf91e0f49a0d057` |

The two target objects have complete raw certificates accepted by both worker definition-first routes,
retained intended-reason mutations, solver/producer replays and solver-free expansions. The local
mcDSQS(20) is the source's Lemma3.4 input from Shi–Xia–Krotov; every shift is checked by the order74 builder.
The gcDSQS(20,2)=mcDSQS(20) identification is justified in
`evidence/mcdsqs74-c21/construction-2.1-hypotheses.md`: a designated other-stem point has degree9 and is
therefore absent from exactly one of the ten classes, as required for gcSTS(19,1).

## For every integer t≥2: Construction2.3 then Construction2.1

**Imported known design.** Lemma3.8 (LF1070–1071), citing Witt1938[20] and Zhou–Chang2014[25], asserts
RDS(3,q+1,qᵗ+1) for every prime power q and positive t. With q=4 obtain RDS(3,5,4ᵗ+1). These references are
imports; their original proofs are not re-proved or independently kernel-checked here.

Delete one point ∞. Let B={A∖{∞}:∞∈A} and T={A:∞∉A}. As explicitly noted at LF343–345 in the proof of
Construction2.2, this gives a 1-fan S(3,({4},{5}),4ᵗ), hence a 1-FG of type1^(4ᵗ) (definition LF248–255):
B is an S(2,4,4ᵗ), and B∪T covers every triple once. The derived resolutions of the RDS are more than
this fan step needs; the pair/triple identities follow directly from the original Steiner3 design.

Apply Construction2.3 (LF444–447; 2mod6 proof branch LF449–541) with the following complete substitution:

| Source symbol/hypothesis | Substitution/check |
|---|---|
| m,g,n,s | 18,1,4ᵗ,2 |
| K1,K | {4},{5} |
| 1-FG(3,(K1,K),gn), type gⁿ | the deleted-point fan above, type1^(4ᵗ) |
| mgn+s≡mk1+s≡2(mod6) | 18·4ᵗ+2≡74≡2(mod6) |
| gcDCQS(m^k1:s) for k1∈K1 | the supplied gcDCQS(18⁴:2) |
| FDGDD(3,4,k{m}) for k∈K | the supplied FDGDD(3,4,5{18}) |
| conclusion | gcDCQS(18^(4ᵗ):2) |

Now apply Construction2.1 (LF292–335), filling every18-point group plus the shared2-point stem using the
mcDSQS(20)/gcDSQS(20,2). The conclusion is

    mcDSQS(18·4ᵗ+2), for every integer t≥2.

This uses the **FDGDD→Construction2.3** route. We do not substitute FDGDD into Construction2.2, which
requires RDGDD instead. We have not supplied an RDGDD(3,4,5{18}). Nor do we invoke Corollary2.6 or the
RDTD(3,4,18) sufficient gcd test: that is the different empty-stem construction used in the earlier32 lane.

## The boundary case t=1 is directly checked

Construction2.1 applied immediately to the finite gcDCQS(18⁴:2) yields order74. The full SQS(74) has been
built and directly checked, so no empty-family convention for the fan at t=1 is needed:

* original UTF-8-comment raw SHA `eaff77fc63cc408756f72b6f6213eb7449a13e1efc5ba0c40401fc51d4f216c3`;
* versioned raw ASCII-compatible SHA `1122f1f49eb61e03c44b0686fc773a912b24039936697fe13e4488af34a8eb4c`;
* both have identical noncomment bytes and16206 blocks, with37 classes at all74 points.

Thus, **conditional on acceptance of the finite inputs, the published Constructions2.1/2.3, and imported
Lemma3.8**, the written consequence is mcDSQS(18·4ᵗ+2) for all integers t≥1. The order74 case is finite
and directly checked; higher orders are the source's recursive mathematical consequence, not explicit
certificates or formal theorems generated in this lane.

## Do not mix up the other Construction2.3 tuple

(m,g,n,s)=(18,4,4,2) would output gcDCQS(72⁴:2), not gcDCQS(18⁴:2). The family argument above keeps m=18
and g=1 while growing the number of groups4ᵗ. The size6 H-design used to construct the supplied FDGDD18
is deliberately unframed; no frame-derived size6 existence hypothesis occurs in this family bridge.
