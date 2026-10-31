# F157: order-2640 even-tail, self-contained candidate — independent review

## Disposition

**PASS at the frozen conditional scope. FATAL: 0; MAJOR: 0; MINOR: 0. No unresolved mathematical or finite-enumeration gap found.** All twelve surviving cardinality branches are excluded by necessary conditions whose reductions I reconstructed, with the finite claims independently enumerated as described below. This is an independent **same-harness** review, not human review, independent-model-family review, formal/kernel certification, or novelty verification. Parent adoption remains a separate action.

The supported conclusion is precisely: there is no finite, uniquely decipherable, factor-complete code D containing the literal S in the candidate, with actual pure-a atom a^2640, whose actual b-run tail border Q has even cardinality. Every P and Q in this statement is extracted from the **same D**, using actual atoms a^i b^k and b^ell a^j with positive b-run length; no auxiliary code or one-b-only slice is substituted.

**Odd-|Q| at order 2640 is untouched. Other orders and the original all-order finite-completion problem are untouched and remain OPEN.** Nothing in this review proves an unconditional order-2640 exclusion.

## 1. Frozen input and read coverage

- Manifest: `manifest-v1.json`, SHA-256 `e877bec84b923e71a870b720b4eb414ac9d59395e4e1f8db176fd569a895d77c`, 2,409 bytes; matched the assignment before candidate interpretation.
- Candidate: `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261028-2640-even-tail-self-contained-review-v1.md`.
- Candidate SHA-256 `53296d698836288dc2354e1fb24e4c25f35b2c67454590b4d5a173134bd4706a`, 38,065 bytes, 262 LF, final LF present: all matched before interpretation.
- **All 262 LF read completely**, in consecutive exact raw ranges 1–70, 71–140, 141–210, and 211–262. No omitted ending, abbreviated source chain, or previous fibre packet was used.
- All 28 named §10 dependencies subsequently matched their printed SHA-256, bytes and LF, and were read completely through `reviewer-pinned-dependency-render-v1.txt`, consecutive raw ranges covering its full 1–1455 lines. This includes the JSON cover certificate, generator/checker, all branch producers/replays, and the small algebra/symbolic checks. `reviewer-pinned-dependency-audit-v1.json` records each pin individually.
- **No author program was imported or executed.** My mathematical enumeration program was authored and run from the prose before I read the pinned author implementations. Later source reading was static inspection. The author cover was decoded as JSON data and checked independently, not executed.
- Named public primary sources were read directly; no web search, external model/API, author contact, held mathematical output, Git, deletion, publication, or infrastructure mutation was used. Only reviewer-prefixed artifacts and this report were created in the assigned review directory.

## 2. Direct readings of imported statements and hypothesis audit

### 2.1 Actual b-run borders

I directly read Cordero, *Factorizations of Cyclic Groups and Bayonet Codes*, [arXiv:2301.13566v1, printed p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1#page=3). Its assumptions are a finite maximal code M with b,a^n in M; its conclusion is a size-n factorization by the actual a^k b^+ and b^+ a^k exponent sets. It is not a theorem about an arbitrary chosen one-b slice.

The candidate does not need to import maximality for D: its explicit directness and coverage proof establishes the needed border tiling from the stated finite UD and factor-completeness hypotheses alone. Thus no silent passage to a different maximal extension is necessary. The named theorem corroborates the border convention, but its finite-maximal hypothesis is not a missing premise in the candidate's elementary proof.

### 2.2 Sands divisor exclusion

I directly read Łaba–Londner, [arXiv:2106.14042v3, printed p. 10, Definition 2.4 and Theorem 2.5](https://arxiv.org/pdf/2106.14042v3#page=10). For **sets** U,V in Z_M it states that U⊕V=Z_M iff |U||V|=M and Div(U)∩Div(V)={M}. Their Div includes equal-element differences; removing those converts this exactly to the candidate's Delta(U)∩Delta(V)=empty. No two-prime hypothesis occurs in this divisor-exclusion theorem; the nearby, different Sands replacement theorem must not be substituted for it.

Here P,Q really are finite sets of residues, and the border proof gives their direct tiling of Z_2640. Hence the necessary divisor exclusion applies despite 2640 having four distinct prime divisors. The candidate's unit-replacement explanation is also valid: multiplication by a unit preserves a mask's vanishing at primitive roots of any given order; the mask tiling identity and cardinality therefore preserve the tiling with the unchanged other factor. A shared nonzero gcd class can be aligned by a unit and would then create a collision.

### 2.3 Coven–Meyerowitz T2

I directly read Łaba–Londner, [arXiv:2106.14042v3, printed p. 3, Theorem 1.1](https://arxiv.org/pdf/2106.14042v3#page=3), and checked the same introduction statement in the [cited HTML rendering](https://arxiv.org/html/2106.14042v1#S1.Thmtheorem1). Its relevant implication is: a finite integer tile whose cardinality has at most two distinct prime factors satisfies T2. T2 combines cyclotomic divisors with **different underlying primes**, not arbitrary two powers of the same prime.

The exact uses are P-cardinality 12=2^2·3, 24=2^3·3, and 22=2·11. Each P, with canonical integer representatives, tiles Z with translation set Q+2640Z, by the same actual border tiling. Thus all three are finite integer tiles of the required cardinalities. Combining Phi_3 with a P-owned Phi_(2^s), or Phi_11 with a P-owned Phi_(2^s), satisfies the distinct-underlying-prime condition. The four-prime factorization of the period is **not** an obstacle to this cardinality-based theorem. No T2 implication is assumed for a general three-prime tile or for Q in these deductions.

### 2.4 Łaba–Londner common-prime alternative

I directly read [arXiv:2106.14042v3, printed p. 26, §6.1, Corollary 6.2 and its proof](https://arxiv.org/pdf/2106.14042v3#page=26). It assumes U⊕V=Z_M and, after ordering the primes, every p_i with i>=3 divides at most one cardinality; both factors then satisfy T2. The candidate states this accurately and explicitly does **not** rely on it. In fact, here primes 3,5,11 occur to exponent one in 2640 and cannot divide both cardinalities, so only 2 can be common; the alternative would have satisfied hypotheses as well. I did not replace the stated, narrower T2 proof by an unacknowledged use of this corollary.

The imported statements were read, not reproved. The exact local algebra controls below check the elementary identities and finite searches, **not** the deep T2 theorem itself.

## 3. Reconstruction of the common reductions

### 3.1 Same-D factorization

Finiteness gives a largest atom length L. An embedding of a^(2L+1) in D* has an atom entirely inside that run, so an actual positive pure-a atom exists. Two distinct pure-a atoms would commute and give different atom lists for the same word. The atom b is in S, so another pure-b atom b^k is likewise forbidden by UD. The empty word cannot be an atom under the stated injectivity condition.

For directness, two different residue pairs (i_t,j_t) with the same sum mod n admit actual representatives u_t=a^(i_t)b^(k_t), v_t=b^(ell_t)a^(j_t). Choose a common integer G larger than both actual i_t+j_t and in their residue class, and guards H,K at least the respective b-run lengths. The lists

(b)^(H-ell_t), v_t, (a^n)^((G-i_t-j_t)/n), u_t, (b)^(K-k_t)

are D-factorizations of b^H a^G b^K. The positive central pure-a part separates the left b-to-a border and right a-to-b border. A zero-a border is only b; treating it as part of the guard does not erase a genuinely different residue pair. Equality of the atom lists would force the same actual borders and therefore the same residue pair. UD forbids the proposed collision.

For coverage, embed b^L a^g b^L with g>L in D*. The atom containing the last left b begins inside the left guard and cannot reach the right b; it is an actual b^ell a^j. Similarly the first right b belongs to an actual a^i b^k ending inside the right guard. They are distinct atoms. Atoms between them are pure-a atoms, so g=i+j mod n. Choosing g in each residue class proves coverage. Consequently P⊕Q=Z_2640 and |P||Q|=2640. This argument uses the actual multi-b borders of one D throughout.

The literal words supply A={0,3,8,11} in P and Y={0,1,7,13,14} in Q. Independently computed Delta(A)={3,5,8,11}=G_A and Delta(Y)={1,2,6,12}=G_Y match the packet.

### 3.2 The seven-head bound

The written exclusion of |P|=4,5,6 is valid. For P=A, every candidate for covering 6 conflicts with old Q and a distinct old head. For A plus one new head U, every candidate for covering U+4 is similarly forbidden. For A plus U,V, coverage of U+4 and V+4 forces U−V+4 and V−U+4 into Q; the five displayed exclusions for U+9 leave U+9 in Q, and symmetry leaves V+9 in Q. Their cross sums collide with distinct heads U,V. Specializing a purported new Q value to an old Q value cannot repair a collision with distinct P values. This is an all-residue algebraic argument, not a sampled numerical check.

### 3.3 Prime balance and parity

From the mask identity, each nontrivial cyclotomic divisor of X^2640−1 divides at least one mask. At prime powers, evaluating at 1 and using |P||Q|=2^4·3·5·11 shows ownership is exclusive. In particular, each single-exponent prime 3,5,11 is owned by the side whose cardinality is divisible by it, giving uniform counts mod that prime. P owns exactly v_2(|P|) of Phi_2,Phi_4,Phi_8,Phi_16. This ownership conclusion uses the total 2-adic valuation; cardinality divisibility alone would not identify which two-power indices are owned.

For |P|=3·2^a (the used cases a=2,3), assuming Phi_2 is absent leaves a owned indices s>=2. T2 and Phi_3 supply Phi_(3·2^s). The pair product is 1+X^(3·2^(s−1)); products over distinct s are coprime products of distinct cyclotomic factors. With P(X)=sum_(j=0)^2 X^j P_j(X^3), each P_j is divisible by R(T)=product_s(1+T^(2^(s−1))). R is even and R(1)=2^a. Decomposing its quotient into even/odd parts makes both even and odd coefficient sums of P_0 multiples of 2^a. Old heads 0 and 3 make both sums positive, contradicting their total 2^a. Thus Phi_2 belongs to P. T2 then gives Phi_6, and divisibility by 1+X^3 forces equal even/odd counts in each mod-3 class. This justifies both P12 and P24 head allocations.

For |P|=22, P has two heads per mod-11 class and owns one Phi_(2^s). T2 pairs it with Phi_11 to give 1+X^(11·2^(s−1)). Folding mod 11·2^s forces paired counts separated by half that period. Old 0 and 11 already fill class 0; their separation is compatible only with s=1. Hence every mod-11 class has one even and one odd head. Q owns Phi_4,Phi_8,Phi_16; its mod-16 counts are constant a on each even class and b on each odd class, a+b=15. Old 0,1 give a,b>=1. There is no Q-screen point congruent to 4 mod 6, so Q's 40 points in class 1 mod 3 are odd; 8b>=40 implies 1<=a<=10. These are all necessary constraints, not assumed fibre factorizations.

## 4. Exhaustiveness of the cardinality partition

My independent enumeration recovered the P-screen size 224, Q-screen size 658, and all printed mod-3/mod-5/mod-11 count vectors. I checked the eight printed disjoint conflicts in the 24-point P class 1 mod 3, proving its independent-set capacity is at most 16.

The pinned Q certificate was independently decoded and checked: exactly 266 nonempty, pairwise disjoint conflict cliques partition all 658 screen points; every intra-clique pair has gcd in G_A. Thus |Q|<=266. Separately, my different simple degree-ordered first-fit algorithm constructed a **270-clique** cover, also checked pairwise and sufficient by itself to exclude Q=330. I do not misreport my 270 as a reproduction of the author's 266.

The full raw divisor list with 7<=|P|<=224 and even |Q|=2640/|P| is:

8,10,11,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132,165,220.

The exact exclusions are:

- P=8 gives Q=330, exceeding either checked clique bound.
- P=11 would have one head per mod-11 class, contradicting old 0 and 11.
- P=60,66,120,132,165 require respectively 20,22,40,44,55 heads in class 1 mod 3, exceeding 16.
- P=110,220 require respectively 22,44 heads per mod-5 class; screened classes 2 and 4 each have only 12.

This leaves exactly the twelve branches P=10,12,15,20,22,24,30,33,40,44,55,88. No leftover even-Q cardinality is assumed infeasible without an argument.

## 5. Finite-search contract and code audit

I independently implemented selection of a pairwise gcd-compatible subset with overlapping exact quotas. The instance consists of the complete stated candidate set, forbidden gcd classes, all specified quota groups, and mandatory anchors. A chosen vertex decrements **every** group containing it, not just a branching group. Its conflict neighbors are removed. Exclusion removes only that vertex. Every legal completion belongs to exactly one child. Negative quota, exhausted group capacity, and deletion from a zero-quota group are necessary rejections.

My implementation additionally propagates a group whose available size equals its quota: every vertex in that group is forced. A conflict between forced vertices, loss of a previously forced vertex, or quota underflow is a genuine impossibility. Only completely exhausted states are memoized as UNSAT, keyed by the active set and all remaining quotas. Prior selections have no unrecorded constraint: their forbidden neighbors have already been removed and their quota contributions recorded. The witness validator checks candidate membership, distinctness, all anchors, every exact quota, and every selected pair independently of the recursion.

For two-quota tests, retaining only the union of the two groups is sound: actual Q intersects it in a subset with exactly those quotas. All old Y are still used for the individual screen, while only old anchors in the retained union are mandatory. Full-fibre tests retain all candidates and all Y. A SAT answer for a small union is only a relaxation, never a full Q or a code. Dropping other prime quotas weakens an instance and therefore cannot create a false exclusion from completed UNSAT.

The head partitions are exhaustive because each actual P has exactly the indicated prime/parity head counts. Every such partial choice is explicitly enumerated; old A are joined before pair filtering and Delta computation. Passing to H=Delta(partial heads union A) drops constraints from unselected heads, hence relaxes the actual tail problem. For P22/P44 the independently verified forced-240 lemma supplies one additional necessary gcd class. Grouping identical H is safe because the entire candidate screen, pair graph, quotas and anchors depend only on H and the stated fibre parameter; the recorded frequencies preserve coverage.

I read the pinned bitset and set/complement implementations completely. The consumers of each H and each fibre parameter are the actual tail-screen/quota loops; none is silently dropped. In particular, P12's SAT boolean is explicitly routed to the s=4 fibre loop, not counted as UNSAT or discarded. The source cache updates occur only after both children fail. Old anchors are selected once and decrement all their groups. No native SAT solver, floating-point test, hidden oracle, or timeout-to-UNSAT conversion occurs in the pinned search code.

The author-program historical node totals were **not rerun or independently certified as historical runtime facts**. They are not needed as mathematical premises: my different implementation recomputed the necessary partitions and all exclusions. Its node totals differ because it propagates forced groups; this is expected, not evidence of a missing case.

As an additional bounded check of my own search implementation, `reviewer-oracle-and-certificate-v1.py` compared it with a no-pruning powerset oracle on **606 deterministic cases**, at most 11 vertices, including intersecting groups, zero/negative quotas, missing/conflicting mandatory anchors, forced groups, and both SAT/UNSAT. There were **0 disagreements**: 42 SAT and 564 UNSAT. This oracle check is a finite implementation control, not a formal correctness proof or a substitute for the invariants above.

## 6. Per-branch verdicts and exact dependencies

All rows depend on the same-D border tiling, old A/Y, Sands exclusion, and the indicated prime balances. Only rows marked T2 use the imported T2 theorem. The reported partition counts in this section are from my executed reviewer program, not copied author verdicts.

| P, Q | Necessary allocation / exact independent exclusion | Additional load-bearing dependencies | Verdict |
|---|---|---|---|
| 10,264 | All C(12,2)^2=4,356 choices from mod-5 classes 2,4: 866 conflict, 3,490 valid, 210 H. Then 408 fail mod-3 capacities and 2,636 fail mod-11 capacities. Remaining 446 choices / 64 H: every `(3,0,88),(11,2,24)` quota instance with mandatory 0,13 is UNSAT. Reviewer max 845 nodes. | P uniform mod 5; Q uniform mod 3 and 11; two-quota restriction soundness. | PASS |
| 12,220 | All 4,356 class-1-mod-3 head choices for each owned second index s=2,3,4. Conflict/high-bit balance partition and the real two-quota residual are audited in §7; the 146 full-fibre residual cases are all UNSAT. | **T2**, mod-3 parity and high-bit folding; Q's remaining Phi_4,Phi_8 at s=4; eight mod-8 quotas and old Y. | PASS |
| 15,176 | P needs five heads in class 1 mod 3; at most one of them can lie in mod-5 class 3. All C(8,5)+C(8,4)·16=1,176 allocations: 992 conflict, 184 valid, 20 H. 78 fail mod-16 capacity; remaining 106 choices / 9 H: full mod-16 counts 11 and mod-11 counts 16, all Y, are UNSAT. Reviewer max 43 nodes. | P uniform mod 3 and 5; old 3,8 consume two of P's three class-3-mod-5 places. P odd makes Q own all four two-power factors, hence uniform mod 16; Q owns 11. No T2 needed. | PASS |
| 20,132 | All C(12,4)^2=245,025 choices: 141,425 conflict; 103,600 valid, 223 H. None fail mod-3 capacity; 97,146 fail mod-11 capacity. Remaining 6,454 / 69 H: `(3,0,44),(11,2,12)` with 0,13 are all UNSAT. Reviewer max 409 nodes. | P uniform mod 5; Q uniform mod 3 and 11. | PASS |
| 22,120 | One even/odd in each of mod-11 head classes 1,2 gives 6^4=1,296 choices; 272 conflict, 1,024 valid, 37 augmented H. 64 fail prime capacities; 452 have no allowed a. Remaining 508 choices / 24 H give 139 `(H,a)` cases. All mod-16 quotas plus `(3,1,40),(5,1,24)`, all Y, are UNSAT. Reviewer max 595 nodes. | **T2** P22 pairing proof; 1<=a<=10; forced gcd 240 lemma; Q prime-3/5 balance. | PASS |
| 24,110 | Four even/four odd heads in mod-3 class 1: all C(12,4)^2=245,025 choices; 239,696 conflict, 5,329 valid, 45 H. None fail mod-5 capacity; 128 fail mod-11 capacity. Remaining 5,201 choices / 43 H: `(5,0,22),(11,2,10)` with 0,13 are all UNSAT. Reviewer max 597 nodes. | **T2** P=3·2^a parity proof; Q prime-5/11 balance. | PASS |
| 30,88 | The 24-point mod-3-class-1 head screen splits into 8 T and 16 Z. P has room for at most four Z because old 3,8 occupy two of six mod-5-class-3 places. Independently checked every Z-to-T blocker and all 256 T-subsets: total class capacity <=8<10. | P prime-3/5 balance; disjoint two-blocker pairs / four-blocker neighborhoods. No tail solver or T2. | PASS |
| 33,80 | Same T/Z split; Z are all 0 mod 11. Old 0,11 consume two of three mod-11-class-0 places, so at most one Z. Capacity <=8+1=9<11. | P prime-3/11 balance, checked screen membership. | PASS |
| 40,66 | Independently checked the forced gcds 4,16,660,1320. The resulting old-Y screen has 457 vertices. Full mod-3 counts 22 and mod-11 counts 6, all Y, are UNSAT (reviewer 2,545 nodes / 458 capacity or forced prunes). | P mod-5 quota 8 and explicit forced-gcd proofs in §6.1; Q prime-3/11 balance. No T2. | PASS |
| 44,60 | All C(12,4)^2=245,025 choices in head mod-11 classes 1,2; 141,425 conflict, 103,600 valid, 195 H after adjoining 240. None fail mod-3 capacity; 43,562 fail mod-5 capacity. Remaining 60,038 choices / 161 H: `(3,0,20),(5,1,12)` with 0,1 are all UNSAT. Reviewer max 6,789 nodes. | P prime-11 balance; forced gcd 240 lemma; Q prime-3/5 balance. No T2. | PASS |
| 55,48 | P must choose 11 of each 12 candidates in mod-5 classes 2,4. Four printed disjoint gcd-1 conflict pairs require four omissions but only two are available. Independently enumerated all 12^2=144 omission choices; all conflict. | P prime-5 balance; all four pair memberships/gcds checked. | PASS |
| 88,30 | Forced gcds 4,55,240 checked. Actual Q's mod-5 classes 1,2,3 contain 18 points, of which ten are 1 mod 3 and eight are among the printed 16 seeds. All C(16,8)=12,870 seeds: 12,657 internal conflicts, 33 class overflows, 180 slot-capacity failures, zero residual. | P prime-11 quota 8; forced-gcd proofs in §6.1; Q prime-3/5 balance; at most one class-1-mod-3 point per `(mod 5,mod 16)` slot. No T2. | PASS |

### 6.1 Explicit forced-gcd and slot arguments

**P40:** If gcd 4 is absent, the additionally screened mod-5 classes 2,4 each have exactly eight candidates, forcing 872 and 459 with forbidden gcd 1. If gcd 16 is absent, the analogous forced pair is 872,1779, also gcd 1. If gcd 1320 is absent, the six printed disjoint half-turn pairs cover the 12 class-4 candidates, giving capacity six<eight. If gcd 660 is absent, there are two four-cycles and four singletons in class 4. Eight chosen heads force all four singletons and an opposite pair in each cycle. I enumerated all admissible eight-subsets, obtaining exactly the four stated cases; every case leaves exactly {11,396,1056,1331,1716,2376} in mod-5 class 1, capacity six<eight. Thus all four gcd classes must occur in P and be forbidden to Q. The earlier failed source and timed-out replay mentioned by the author were not used.

**Forced 240 for P22/P44:** Restrict to any two heads in each of mod-11 classes 2,10,9,7,3, retaining old head 3. If P avoided 240, all ten would lie in the 63-point Screen(A,G_Y union {240}) restriction. My exact five-group search is UNSAT (3,229 nodes). This proves the lemma for every P having at least two in these classes, including P22 and P44. The printed ten-head control independently validates after removing 240 and has a genuine gcd-240 pair.

**P88:** Avoiding gcd 4 forces the entire eight-point classes 1 and 4 mod 11, including 155,576, with forbidden gcd 1. Avoiding 55 forces 456 in class 5 and 35 in class 2: omitting either leaves 11 candidates with four disjoint 55-conflict pairs, capacity at most seven<eight. Those two forced heads have gcd difference 1. Avoiding 240 leaves ten candidates in each of classes 2 and 10; five disjoint printed cross-conflicts give total capacity <=15<16. I checked every stated endpoint, its screen/class membership, and its gcd.

For the tail slot step, class-1-mod-3 points occur only in mod-5 classes 1,2,3 and are odd. Two distinct such points in one `(mod 5,mod 16)` slot differ by a nonzero multiple of lcm(3,5,16)=240; since 2640=11·240 and the residues are distinct, their gcd difference is exactly 240. Therefore at most one can be selected per slot. Counting individually seed-compatible slots, while **ignoring** conflicts between different slots, overestimates possible completions. Rejecting for too few such slots is consequently sound. All 180 remaining seeds fail this relaxed capacity test; no unexamined slot-assignment problem remains.

## 7. P12's genuine SAT residual and its resolution

The second P-owned two-power factor is uniquely Phi_(2^s), s in {2,3,4}, in addition to Phi_2. T2 with Phi_3 yields 1+X^(3·2^(s−1)); hence for the entire four-head mod-3 class 1, the u=(x−1)/3 counts fold equally between r and r+2^(s−1) mod 2^s. All complete head allocations were tested with this condition, not a selected sample.

| s | G_Y conflicts | high-bit failures | valid choices | distinct H | two-quota UNSAT choices | two-quota SAT choices |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 2592 | 1508 | 256 | 6 | 256 | 0 |
| 3 | 2592 | 1620 | 144 | 10 | 144 | 0 |
| 4 | 2592 | 1664 | 100 | 35 | 84 | **16** |

The two quotas are `(5,0,44),(11,2,20)` with mandatory 0,13. I independently found SAT for the six H below, validated each returned witness, and directly validated the printed 64-tail witness for the second H. Its mod-8 counts are [13,4,12,6,12,6,7,4], not the necessary common-even/common-odd fibre counts. It is therefore a real two-quota SAT witness but **not** a full border, full Q, or code.

At s=4, P owns Phi_2 and Phi_16, so Q owns Phi_4 and Phi_8. Their product 1+X^2+X^4+X^6 forces folded mod-8 counts a on each even class and b on each odd class. Since |Q|=220, a+b=55; old 0,1 force 1<=a<=54. Exhaustively applying individual capacities gives:

| residual H | head-choice frequency | allowed a (inclusive) | exact cases |
|---|---:|---|---:|
| {3,4,5,8,11,16,20,24,40,44,165,176} | 4 | 15–38 | 24 |
| {3,4,5,8,11,16,20,24,44,80,88,165} | 4 | 15–38 | 24 |
| {3,4,5,8,11,20,24,44,165} | 4 | 15–40 | 26 |
| {3,5,8,11,16,24,40,80,88,165,176} | 2 | 15–30 | 16 |
| {3,5,8,11,16,24,40,165,176} | 1 | 11–38 | 28 |
| {3,5,8,11,16,24,80,88,165} | 1 | 11–38 | 28 |

These frequencies sum to 16 and the case counts sum to **146**. For every case my exact search retains all eight mod-8 quotas, both original quotas, all five old Y anchors, and all H-pair conflicts on the full screen. **All 146 are UNSAT.** Forced-group propagation reduced my maximum to 27 nodes; this does not claim to reproduce the author's different 5,843-node traversal. The six residuals are resolved by these extra necessary fibre conditions, **not by pretending the earlier two-quota test was UNSAT**.

## 8. Executed independent controls and intended-reason mutations

All computation used Python 3.14.3, integer arithmetic and finite subsets only. Main exact enumeration ran from 2026-10-29T05:01:24.975483+00:00 to 2026-10-29T05:01:36.103359+00:00 (11.12793 seconds). Its receipt has no UNKNOWN instance. Every search had an explicit node/time bound that would report UNKNOWN rather than exclude a case; no bound was reached. The separate oracle/certificate control ran from 2026-10-29T05:04:07.056247+00:00 to 2026-10-29T05:04:07.115436+00:00 and all assertions passed.

Executed positive and intended-reason negative controls include:

1. **Small P55 branch:** all 144 exact omission choices fail G_Y. Removing only forbidden gcd 1 yields a checked 22-element two-class selection; reinstating 1 rejects it. This isolates the matching obstruction instead of merely checking an arbitrary impossible input.
2. **Forced-240 lemma:** the printed ten-head selection satisfies both heads per class, old-head screen, mandatory 3 and all G_Y pair conditions after 240 is removed. It contains a gcd-240 pair and is rejected for precisely that extra constraint.
3. **P10 quota control:** removing only the extra partial-head gcd classes yields a validated 106-point two-quota SAT selection. Reinstating a residual H rejects it by added gcd classes {4,16,132,264,660}; all 64 original H instances were independently UNSAT. This is not a full 264-tail witness.
4. **P12 positive residual:** the literal 64-point witness satisfies both quotas, H-pair compatibility, old-Y screening, mandatory 0,13. Adding old 1,7,14 gives a **67-point** witness with all five old anchors and the same two quotas; this preserves anchors while dropping only the fibre constraints (and their implied full cardinality). It remains explicitly a relaxation.
5. **P12 pair-conflict mutation:** replace 50 by 55 in the 64-point witness. Candidate screen membership, distinctness, both exact quotas, and mandatory 0,13 are preserved, but pair (55,60) has forbidden gcd 5. The independent pair check rejects it for the intended reason.
6. **Certificate mutation:** swap 0 and 330 between singleton {0} and clique {330,674}. The exact 658-point partition, 266 nonempty groups, and all cardinalities are preserved, but new pair (0,674) has gcd 2 outside G_A. The independent cover validator rejects it for the intended clique reason.
7. The independently authored algebra control checked the binomial/cyclotomic coefficient identities for primes 3 and 11 and all s=1,2,3,4 used here. This is only a control of elementary identities, not empirical verification of T2.

### Durable replay artifacts

All paths below are in this review directory. Source/receipt bindings are computed SHA-256 values, not author assertions.

| Artifact | SHA-256 | Role |
|---|---|---|
| `reviewer-independent-exact-v1.py` | `6590dd5bb41b362fc213f6cfe6142c56badd1fc90fbdcbced213776cef6ed905` | Independently designed all-branch enumeration, full quotas and witnesses; never imports author code. |
| `reviewer-independent-exact-v1-receipt.json` | `40c3ea559cbd1c950f5360354fdc2263614ada76e5026ad2382bc17b50217027` | Clock/runtime/source binding, every searched H/frequency/a, outcomes, witnesses and controls. |
| `reviewer-oracle-and-certificate-v1.py` | `a2d4217bd5ff67bdf7f5dcc814c3a9205d5763cff0cb9cf56b4a6451f58b56f8` | Powerset oracle for reviewer code, pinned certificate data verification, strengthened P12 control. |
| `reviewer-oracle-and-certificate-v1-receipt.json` | `15cbc9dd82c0abb1da331cf8b1e9b7b284daf60b46db38d578fdb667a98737c1` | 606 comparisons, intended-reason certificate mutation and all-anchor P12 relaxation. |
| `reviewer-pinned-dependency-audit-v1.json` | `7f7b6ad75235ad6306694e904a33d4dbf0d8667dceca924820c672504dc096f1` | All 28 dependency SHA/byte/LF verifications before their source rendering. |
| `reviewer-pinned-dependency-render-v1.txt` | `f261890d3ac3b63db2d0d2cdcbd838471998d54a3fa422d97c4ff16d71c4b42e` | Complete numbered literal rendering read in full; static source review only. |

The main script exclusively creates its named receipt, so replay in the same directory must not overwrite the original evidence. The second control exclusively creates its own receipt and reads the first. The durable evidence is the existing completed receipts; neither author historical node totals nor any earlier failed/timed-out run is being promoted to evidence by this review.

## 9. Final exact-scope assessment

The actual border construction, seven-head reduction, size sieve, T2 hypotheses and elementary polynomial deductions, every explicit forced gcd/matching/slot argument, every partial-head partition, and every finite tail residual have passed this review at the stated scope. The independent code was actually run for the small branches **and** the claimed residual branches, rather than treating an author's PASS/UNSAT label as evidence. No mathematical FATAL, MAJOR, MINOR, or unresolved INCONCLUSIVE item remains in this frozen candidate.

The conclusion remains conditional on the explicitly stated finite UD/factor-complete same-D setting and the classical imported tiling theorem. It excludes **even** actual tail-border cardinality at order 2640 only. **Odd-|Q|, other orders, and the original all-order problem remain OPEN and unreviewed here.**
