# Sun P7 mixed-source branch — an explicit finite simple-group bound by elementary unitary packing

Owner **MathSun8-2**. Actual preceding `/bin/date`: **Mon Oct 26 08:08:41 PDT 2026**. **NEW WRITTEN CANDIDATE, not reviewed/adopted.** This provides an explicit group/outer-index bound ONLY for the stated mixed-source branch. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/GO, and no evaluation of the large integer bounds.

## 1. Generic finite NONABELIAN SIMPLE group lemma

**Lemma.** If a finite nonabelian simple group G has a nontrivial complex representation of dimension d, then

    |G| <= (4sqrt(d)+1)^(2d²).                          (PACK)

This does not assert a bound for arbitrary finite groups, central extensions or abelian simple groups. No Jordan theorem, CFSG, finite subgroup catalogue, character-degree table or external order theorem is imported.

A nontrivial representation has normal kernel not equal to G; simplicity makes it FAITHFUL. Average any positive Hermitian inner product over finite G to make it unitary. We may therefore regard G as a finite subgroup of U(d).

Let delta be the MINIMUM of ||g-I||_op over nonidentity matrices g in G. It is strictly positive. Choose g attaining it. Every conjugate u of g has the SAME distance delta from I, by unitary invariance. For ANY two conjugates u,v,

    ||[u,v]-I||_op=||uv-vu||_op
       <=2||u-I||_op||v-I||_op=2delta².

The equality follows by right multiplication by the unitary vu, and the inequality from uv-vu=(u-I)(v-I)-(v-I)(u-I) and submultiplicativity. If delta<1/2, this commutator is either identity or a nonidentity matrix at distance STRICTLY below delta. Minimality rules out the latter. ALL conjugates therefore commute. They generate a nontrivial ABELIAN normal subgroup of G; simplicity makes it G, contradicting nonabelianness. Hence delta>=1/2.

Consequently ANY two distinct group matrices have operator distance>=1/2, by multiplying their difference by an inverse unitary. Their Frobenius distance is also>=1/2. Regard complex d-by-d matrices as Euclidean R^(2d²). Every unitary center has Frobenius norm sqrt(d). The open Euclidean balls of radius1/4 around the |G| matrices are pairwise disjoint and all lie in the ball of radius sqrt(d)+1/4 about0. Comparing finite-dimensional ball volumes and cancelling the common unit-ball volume gives

    |G|*(1/4)^(2d²) <= (sqrt(d)+1/4)^(2d²),

which is PACK. Touching boundaries have zero volume and do not affect the argument. This is an elementary full-proof norm/packing consequence, not a scientific finite enumeration or a new priority claim for those classical tools.

## 2. EXACT mixed-source input and its finite irreducible dimension

Now take a least-GROUP-ORDER finite direct-P7 existence example at the SEPARATE named adopted normal-section reduction, so G is finite nonabelian simple. Its EIGHT original disjoint nonempty LEFT cosets have FULL indices7r_l with pairwise-coprime private r_l. Let an ACTUAL M contain a selected U_i, with[G:M]=7t.

Assume the mixed EXACT TWO-orbit source situation from the ENTIRE142LF `sun8-mixed-six-one-five-two-private-235-obstruction-v1.md`, SHA256 **97f7e607ca3948ff67194904f677473844231deeed4457412c81561aa53235d2**: one original H6 has6t+t orbits, another original H5 has5t+2t orbits on the SAME G/M, all full-source/private-coprimality/disjointness hypotheses retained. This142LF result is a NEW candidate requiring its own complete gate, not assumed adopted by this note.

Its fully supplied representation/moment argument constructs a NONTRIVIAL common irreducible W in C[G/M]. The only unexcluded simple-P7 mixed case has private2/5/3 ownership, EVEN t, and

    7<=d=dim W<=20 when v2(t)=1,
    7<=d=dim W<=160 when v2(t)>=2.                    (DIM)

All simpler branches already produce an ACTUAL seven-point quotient contradicting the named faithful-degree7 P7 exclusion. This note uses DIM exactly; it does not supply or silently accept another representation in a selected smaller model.

Because G is NONABELIAN SIMPLE and W is nontrivial, W is FAITHFUL. Thus PACK applies to the original G, not merely an unspecified image or quotient.

## 3. Explicit bounds for G, ALL eight original private factors and the actual outer index

If d<=20, then d<25 and4sqrt(d)+1<21, while2d²<=800. If d<=160, then d<169 and4sqrt(d)+1<53, while2d²<=51200. These are exact universal inequalities, not chosen numeric parameter tests. Therefore the mixed branch satisfies

    |G| < 21^800       if v2(t)=1,
    |G| < 53^51200     if v2(t)>=2.                    (GBOUND)

Every original index is7r_l<=|G| and the ACTUAL overgroup index is7t<=|G|. Hence EVERY original private factor and the outer t obey

    7r_l < B for ALL l,  7t < B,
    B=21^800 or53^51200 in the respective case.       (INDEX_BOUND)

No huge power is evaluated and no group/subgroup/coset enumeration or executable certificate is produced or authorized. The bounds do not claim that any object attaining or approaching them exists.

The separate136LF ENTIRE-normalizer theorem `sun8-mixed-private-235-entire-normalizer-order-four-v1.md`, SHA256 **e0c68d425b0e2bc30c6072acf3602b0d7b02e3045880227a20bc5ff49d506bd5**, additionally gives |N_G(U_i)/U_i|<=4 under its precise achieved-minimum-SUM/normalizer/owner/capacity hypotheses. When M is THAT normalizer and t=s, it implies r_i=s|Q|<=4s; no such inequality is asserted for an arbitrary different M. This structure is NOT needed for GBOUND: the direct inequality7r_l<=|G| is already stronger than combining r_i<=4s with a bound for s. Do not claim a sharper private bound from that weaker combination or conflate the two minima.

## 4. Exact scope, ancestry and residual

The generic PACK lemma has a complete elementary proof above. Its Sun application is CONDITIONAL on the explicit mixed142LF dimension theorem and the SEPARATE least-GROUP-ORDER/nonabelian-simple reduction, at their supplied/named boundaries. It is not a new proof of the entire normal-section/global Sun7/general Sun8-to-P7 ancestry. If G is not simple, the kernel and abelian-normal arguments do not justify a bound on its full order; no arbitrary normal/composition-factor/central-extension closure is inferred.

Older papers' no-G/t-bound statements remain correct at THEIR earlier scopes. This successor offers the explicit bound ONLY on a least-order SIMPLE P7 example HAVING the exact mixed6+1/5+2 source pair. Configurations without such a pair,5+1+1/Hom3, other alpha types, actual small-normalizer fibre lifts, private-composite legal enlargement and original arbitrary-group Sun8 remain unresolved. The bound is not proof that this finite branch is empty, a finite search result, global P7 bound or a witness.

A fresh ENTIRE math AND dependency/application gate must assess PACK, its faithful-W use, both numerical SYMBOLIC inequalities and every original-index transfer together with the COMPLETE142/136/200 high-source union. Prior positive returns or current inventory hashes cannot accept this new branch bound. No novelty, SOTA, priority, full-book, formal/kernel/human/configured-family/executable/triple acceptance follows; elementary unitary/norm/volume tools retain their ordinary/prior status.

All work follows actual v123 review RETURN and the new WHOLE primary ACK WRITTEN+SENT before prospective primary source/proof. OWN057/047/078/COUNT/M1/v26/v31 TWO late/v33 and every received parent/owner/reviewer finding remain permanent. ENTIRE withdrawn trial/guidance retains ZERO credit and is not repeated/replayed/back-converted. No new numeric parameter/control trial, decimal magnitude scout, scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/GO, dead-kernel restart, author/shared/frozen edit, git, deletion or publication. Same18/exclusiveOWN/HOLD/original science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/substantive<=30min checkpoints; no early final park, new owner/deadline, cognition/runtime census or round closeout. Original research continues.
