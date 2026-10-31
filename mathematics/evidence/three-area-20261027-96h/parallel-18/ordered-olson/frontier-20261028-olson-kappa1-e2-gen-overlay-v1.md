# Mandatory GEN/IPGEN qualification for the κ=1, e_F=2 family

Native `/bin/date` immediately before this write: **Wed Oct 28 19:32:10 PDT 2026**. This is an ADDITIVE qualification, not an edit of the immutable family `frontier-20261028-olson-kappa1-e2-ref-fail-family-v1.md`, SHA256 `e9d49c28052f4821568eaec81085c793c1110413416b3c0f322caeec7bd2cdce`. Read this and the SEL overlay `frontier-20261028-olson-kappa1-e2-sel-overlay-v1.md`, SHA256 `278edd81bb512c1a4ff0c3e54c76eec57f38d953422c2e64007e190f4cbcc6ce`, BEFORE the family source. Source chronology is not backdated.

## 1. Corrected residual membership

The family's actual reflection multiplicities do fail the literal SEL predicate as stated in the SEL overlay. However, a later direct construction shows that EVERY word of this family is in the historical **GEN**, hence **IPGEN**, actual-certificate class. The full L_RES residual requires the IPGEN predicate to fail. Therefore this family is definitively **OUTSIDE the complete L_RES set**, independently of whether the historical GEN/IPGEN implication has been accepted as a theorem.

Its original actual claims—zero-free cyclic singleton gaps, ν_M=(p+5)/2, κ=1/e_F=2, REF-failure and the explicitly selected original identity word—remain unchanged. It proves nonemptiness only for that enumerated BASE class including SEL failure, not for the complete residual. No new strict provider coverage, priority or L_RES counterexample is claimed.

## 2. A finite explicit certificate on the actual word

The source word is

`Z^(2p−7) ρ A A Z B B Z ρ T_1 ρ T_2 ρ ... T_(p−1) ρ`

with Z=σ_0, A=σ_a, B=σ_(−a), ρ=r^a, T_j=σ_(ja), p>=11 and a!=0. Use the original cyclic cut and OMIT the first actual Z. The remaining `4p−2` actual positions are partitioned consecutively as follows:

1. `p−4` two-letter blocks `ZZ`.
2. One rotation-wrapped eight-letter block `ρ [ A A | Z B | B Z ] ρ`. Its six-letter interior is a concatenation of THREE same-type two-reflection bases; the endpoints are actual rotations.
3. For each `j=1,...,(p−1)/2`, one actual balanced four-letter block `T_(2j−1) ρ T_(2j) ρ`.

These blocks use every retained actual position exactly once. Their literal GEN grammar is `same-type two-letter`, `consecutive concatenation`, `rotation wrap`, and `GOOD balanced four-letter`—no SIX base, forbidden reflection-wrap, hidden unit, or held old scientific output is used.

For each tail block, let A_rot be the exponent sum of its two rotations, B_ref the exponent difference of its two reflections, and C the exponent of ALL FOUR actual letters. Directly in the original FRFR order,

`A_rot=2a`, `B_ref=−a`, `C=−a`.

Thus `A_rot != B_ref` because `3a!=0` for p>=11; the literal GOOD criterion holds. Explicit option weights for EMPTY, both rotations, both reflections and ALL are

`1, u=−1/3, v=−5/3, w=1`.

They satisfy `1+u+v+w=0`, `u+v+2w=0` and `A_rot*u+B_ref*v+C*w=0`. All inverses exist at the stated primes. These are actual even-size/even-reflection selections; no scalar point is substituted for an unperformed selection.

The prefix contributes depth p−4, the rotation-wrapped three-FF interior depth4, and the `(p−1)/2` GOOD blocks contribute depth p−1. Total depth is exactly `2p−1` on the actual length4p−2 partition. The explicit syntactic tree suffices for membership; the paper's already written direct identity selector does not depend on using the nilpotence theorem.

## 3. Source and check boundaries

The literal grammar was actually read at `mathematics/evidence/six-lane-20261018-96h/olson/continuations/correct-length-residual-cover-followon/proof-EXTENDED-UNITS-AND-SIX-BLOCK-OBSTRUCTION-v1.md:65–127,197–209`, SHA256 `8d6d8a7a9e93d03186d3a31236516ae39d400af33d19c5584a9905f1e3ab9871`; the explicit IPGEN superset rules were read at `.../resid-band-followon-20261022/proof-LOWER-BAND-SELECTOR-AND-INVERSE-INSERTION-v1.md:169–180`, SHA256 `80d43628cd3f1773a8cd5826be436259ab843bd4147b07164796b53794d55c3f`. These are scoped reads, not a claim that either complete historical proof body or all old gates was revalidated.

Fresh local `frontier-20261028-olson-kappa1-e2-gen-certificate-checker.py`, SHA256 `494c1d2f436e84d36ce9ec23f987a5c28d70895e565912af5feb8bd05673cc57`, returned `PASS_EXPLICIT_GEN_PARSE` in `frontier-20261028-olson-kappa1-e2-gen-certificate-check-results.json`, SHA256 `0e91da142e8d103d32ae6b69f021bc4f4892a1d6a3cd77149f69801206febe34`. At p=11,13,17,19 it checked the exact omitted original index, full actual block partition, local FRFR points and all three weight moments, total half-length/depth, and a deliberately non-GOOD tail mutation. This is a finite parse check, not an all-word parser, formal proof or full historical-source audit.

OLD and other GS/DS3 classifications remain unchecked, but they are no longer needed to conclude that THIS family fails the full residual's required IPGEN-failure condition. This episode adds no L_RES counterexample, no proof of L_RES, no independent-model-family or formal/novelty promotion.

**END — mandatory explicit GEN/IPGEN exclusion.**
