# Sun8 — complete actual alternating/symmetric orbit-strata union: PRIME POWERS and prime windows

Owner MathSun8-2. Actual preceding `/bin/date`: **Sun Oct 25 17:05:09 PDT 2026**. **NEW COMPLETE WRITTEN CANDIDATE AT NAMED CLASSICAL INPUTS; NOT ACCEPTED.** This is ONE current manuscript for the entire group-family route, not a narrowed integer-index model or a convenient finite survey. It includes the earlier prime-window theorem and a NEW complete prime-power-degree theorem, with every original subgroup/coset retained.

## 1. Original target, exact new family and inputs

For G=A_n or S_n, Sun8 asks that EVERY EIGHT pairwise-disjoint LEFT cosets g_iU_i of arbitrary subgroups have some pair of ACTUAL indices with gcd≥8. No maximality, set-stabilizer, normalizer, P7/cofactor, minimum-order, finite-order cutoff or assumed partition belongs to this target.

The TWO complete group-family conclusions are:

**PP:** Sun8 holds for ALL A_(p^a) and S_(p^a), p PRIME>7 and a≥1.

**PW:** Sun8 holds for A_n and S_n whenever an ODD PRIME p>7 divides n, n≥2p, and ONE prime q satisfies n−p<q≤n. In particular it holds for ALL A_(2p),S_(2p), p prime>7, by Bertrand.

PP covers all prime natural degrees≥11 and their arbitrary powers, not only degrees with a prime in a last-p interval. PW is the valid earlier86LF result and remains included, not retracted or double-counted. Neither conclusion covers all alternating/symmetric degrees or all groups.

Only named classical inputs are **JORDAN-PRIME**, exactly Theorem1.1 of [Gareth A. Jones1209.5169v1](https://arxiv.org/html/1209.5169v1): a primitive finite permutation group containing a SINGLE prime-length cycle fixing at least THREE points contains A_n; and **BERTRAND**, for every integer u>1 a prime lies between u and2u. Ordinary finite-group/orbit/Sylow/block/index facts and elementary polynomial arithmetic complete the proofs below.

The22LF `sun8-prime-window-classical-inputs-v1.txt`, SHA `d32f2d06f2b70c45541f07c52d74e43c9cc781640157ed58edd86e3d4bb35bca`, gives the ACTUALLY READ statement/source/access limits. The full Jones native source and accessible Galvin note were read, but original Jordan proof DAG and original Erdős403 body were NOT reconstructed. No Galvin Mathematica estimate or scientific program was replayed/credited. These are named UNREPROVED classical inputs; the source's separate general-cycle/CFSG Theorem1.2 is NOT used. Reading its statement is not formal/kernel/human/configured-family acceptance.

There is NO Sun7/R8, pending125/99/63 uniform-source theorem, NC7/F7, rank-four, normal-section, CFSG coprime-index theorem or historical scientific computation as a correctness premise here. In particular PP/PW prove their original finite-group Sun8 instances DIRECTLY, rather than rely on the global Sun8-to-P7 interface.

## 2. ALL nonexceptional primitive subgroups have index divisible15

This is a useful actual natural-action fact for EVERY n≥8, not only the solved degree families. Let H≤G be primitive, with H NOT containing A_n. If3 did not divide its index, H would contain a Sylow3-subgroup of G. Every such Sylow contains a SINGLE3-cycle: choose a3-cycle of G, place it in a Sylow, and conjugate that Sylow into H by ordinary Sylow conjugacy. The cycle fixes n−3≥5 points. JORDAN-PRIME would force H≥A_n, contradiction. Thus3 divides [G:H].

The SAME reasoning at prime5 gives an actual SINGLE5-cycle fixing n−5≥3 points, so5 divides [G:H]. Consequently

15 divides [G:H] for EVERY primitive H not containing A_n.       (PRIM)

No coprime-index subgroup is fabricated; p-freeness of an ACTUAL subgroup index supplies the actual full Sylow subgroup and hence the isolated cycle. H need not be maximal. For G=A_n every proper primitive H is nonexceptional. For G=S_n the only proper exceptional H containing A_n is A_n itself, index2.

## 3. ONE middle prime divides ALL transitive-imprimitive subgroup indices

For EVERY n≥16 choose u=floor(n/2) and ONE prime q with u<q<2u by BERTRAND. Since q is an integer, q>n/2 even when n is odd, and q<n. In particular q>7 and is odd, so q divides |G| for both A_n/S_n.

Every transitive imprimitive H preserves an ACTUAL proper block system of a blocks of size b, ab=n,a,b≥2. Its order divides(b!)^a a!, the order of the corresponding S_b wreath S_a. Both a,b≤n/2<q, so q does not divide that order or |H|. Therefore

q divides [G:H] for EVERY transitive imprimitive H.              (IMPRIM)

The SAME q works for ALL such H. This does not choose different primes/partitions for each source, classify maximal subgroups, or treat an index divisor as a block system. For prime n there is NO transitive imprimitive H at all, because no ab=n with a,b≥2 exists.

## 4. ALL intransitive subgroup indices in prime-power degree contain p

Let n=p^a, p prime>7, a≥1. An intransitive H has an ACTUAL orbit of size k with1≤k<n; hence H lies in its set stabilizer. In S_n that stabilizer has index binomial(n,k). In A_n it has the SAME index: the full set stabilizer S_k×S_(n−k) contains an odd transposition because n≥11 and one part has at least two points, so intersecting with A_n halves both ambient/stabilizer orders. Thus binomial(n,k) divides the ACTUAL [G:H].

In the polynomial ring over F_p,

(1+x)^(p^a) = 1+x^(p^a),

by iterating the exact Frobenius identity a times. Every interior coefficient binomial(p^a,k) is0 modulo p. Consequently

p divides [G:H] for EVERY intransitive H.                        (INTRANS)

This is written symbolic coefficient reasoning, not a binomial-coefficient program or prime-field replacement of original coset geometry. It proves divisibility for actual containing set stabilizers; no converse from index arithmetic or lossless coset enlargement is assumed.

## 5. Complete proof of PP — ALL original eight cosets, no private-cofactor assumption

Assume a counterexample: EIGHT actual disjoint nonempty cosets and every pair of subgroup indices has gcd≤7. Every U_i is proper, because a full-group coset would meet every other coset.

If a=1, n=p is prime≥11, there are no transitive-imprimitive subgroups. All intransitive indices share p>7 by(INTRANS); at most ONE original U_i can be intransitive. All nonexceptional primitive indices share15>7 by(PRIM); at most ONE can be of that type. In A_n that exhausts proper subgroups, already far fewer than eight. In S_n at most ONE original A_n coset may occur in an eight-coset family: its two distinct cosets would exhaust S_n and leave no room for the other six nonempty cosets. This still gives at most three, contradiction. The prime-degree case uses no Bertrand computation.

If a≥2, then n≥121 and §3 supplies ONE global q>7. Every intransitive index shares p>7; every transitive-imprimitive index shares q>7; every nonexceptional primitive index shares15>7. Therefore at most ONE original U_i may occupy EACH actual action type, because two in the same type would already have a gcd>7. A_n has at most three possible sources under the counterexample assumption. S_n has at most those three plus one possible A_n coset. Neither can supply eight disjoint nonempty cosets. This proves PP completely for EVERY p>7 and EVERY a≥1, using actual action types and full indices, not an ansatz.

No partition of source indices into prime colours is independently selected: the actual orbit type determines its bucket, and SAME p/q/15 divisibility was proved for every subgroup in that bucket. Repeated subgroups/cosets do not evade the pairwise gcd contradiction. At no point are all original indices assumed to be multiples7.

## 6. Complete proof of PW — one GLOBAL last-p prime

For completeness the entire earlier prime-window theorem is retained here. Let p>7 divide n,n≥2p, and q be ONE prime with n−p<q≤n. Then q>n/2 and q>7, odd, dividing both |A_n|,|S_n|.

If [G:H] is p-free, H contains an ACTUAL Sylow p-subgroup P. Its fixed-point count f is congruent to n modulo p. If f≥p, an EVEN p-cycle on p of its fixed points commutes with P and lies outside P, making a strictly larger p-group inside G. Thus f<p; since p|n, f=0. Every P-orbit is a positive multiple of p. Also P contains a SINGLE p-cycle by Sylow conjugacy from an explicit p-cycle of G.

If H is intransitive, each H-orbit is a union of P-orbits, hence a positive multiple of p; with two or more such orbits every size is≤n−p<q. Its order divides a product of factorials of sizes<q, so q divides its index. If H is transitive imprimitive, §3's block-order argument applies with THIS q>n/2 and again q divides its index. If H is primitive, the SINGLE p-cycle fixes n−p≥p>7 points, so JORDAN-PRIME forces H≥A_n. Therefore EVERY nonexceptional p-free subgroup index contains the SAME q.

In a hypothetical original Sun8 counterexample, p>7 allows at most ONE index divisible by p. At least SEVEN actual U_i are p-free; all are nonexceptional in A_n, and at least SIX are nonexceptional in S_n because at most one A_n coset can occur. Two such indices share q>7, contradiction. This proves PW. At n=2p, BERTRAND gives p<q<2p, so ALL A_(2p)/S_(2p), prime p>7, are covered.

All private valuations/composite subgroup indices remain unrestricted. The proof does NOT require selecting a natural point/set stabilizer, a simple least-order group, a source-normalizer quotient or a common source section. p7, p2, n=p and a missing last-p prime cannot be substituted into this proof; PP treats prime n by its separate legitimate route.

## 7. Global ALL-degree orbit-strata residual — not another solved-family claim

For ANY n≥16, whether or not prime-power/prime-window, an original counterexample in A_n can have at most ONE nonexceptional primitive source by15 and at most ONE transitive-imprimitive source by the SAME middle q. Thus at least SIX of its eight original subgroups would be INTRANSITIVE. In S_n at most one further A_n coset is possible, so at least FIVE sources would be intransitive. This is an actual whole-original-source reduction, not an assertion that their enlarged set-stabilizer cosets stay disjoint.

For n not a prime power the uniform(INTRANS) divisibility by a single p has NOT been established and is generally unavailable from the Frobenius coefficient identity. The remaining problem in those degrees is the actual simultaneous intransitive orbit/subset-coset geometry with all original U_i and indices preserved. A binomial-index list or independent subset maps are NOT actual disjoint cosets. Nothing here bounds the number of such source subgroups without an additional argument.

The earlier86LF `sun8-alternating-prime-window-exclusion-v1.md`, SHA `364192f4143afabdb45afb1790cc708c0cd64a744154c6cade1c76f0e66a97cf`, remains unchanged. Its exact A_77 one-source/two-coset control is not an eight-coset witness and is not a premise of PP/PW. This v2 adds PP and the all-degree orbit-strata reduction; no old residual/history is edited or double-counted. The separate125/99/63 source-barrier union/M1 remains untouched and unaccepted; neither route accepts the other.

## 8. Assurance and original full remaining target

All new containment/cycle/orbit/block/index/coefficient/coset arguments are WRITTEN in this complete body. Jordan/Bertrand remain explicitly named UNREPROVED classical inputs; no original proof-DAG, historical program or Galvin Mathematica bound is newly certified. The native Jones statement was actually read, but its general-cycle/CFSG classification is NOT used. Full written reconstruction/parent disposition, stronger formal/kernel/human/configured-family/executable gates and novelty/priority/SOTA clearance are UNPERFORMED/UNCLEAR. These family conclusions may be standard/known; no independent discovery count is claimed.

The unrestricted original Sun8 problem is STILL OPEN here: all other alternating/symmetric degree cases not covered by PP/PW, other finite simple groups, arbitrary infinite groups, the actual mixed-alpha<=1/nonabelian/odd/maximal/self-normalizing/private-composite P7 source-lift frontier and global Sun7/R8 provenance remain. No genuine eight-coset counterexample, group-size/order/index bound, scalar-index substitute or full-book solution is delivered. This is an unbounded full-group-family proof, not completion by narrowing the original assignment.

No scientific interpreter/Eval/calculator/program/CAS/enumeration/symbolic/solver/replay/build/test/CLI/nested agent/newGO. Only written mathematics, static source reads and metadata clocks/hashes. Same original eighteen owners/fulltarget/root/cutoff/deadline, immutable source/finding histories and v9/v10/v11/HOLD. Primary continues at the stated original residual, not round closeout.
