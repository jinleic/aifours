# Addendum 10 — the t−r relative-commutator defect bound is attained by finite actual groups

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 16:03:12 PDT 2026**.
**NEW WRITTEN universal family/conditional-coupling sharpness candidate. No original avoiding word, discovery/novelty or adoption claim.**

## 1. Separate declared inputs and exact result

This continues the S1 original-word/noncrossing-coupling branch using ONLY the admitted original definitions and explicitly elementary finite-vector/group/rank/counting facts, all specialized uses proved below.
It uses NO public-paper theorem or bound, no p-group existence proof, no polynomial zero count, no group algebra/augmentation ideal or representation theorem, and no old proof/candidate/held guide.
The actual group law is defined directly as a finite GROUP operation. It is not a group algebra or a matrix model asserted WLOG.
Dimitrov proof/method and prospective augmentation/group-algebra route remain STOPPED. Extra displayed context and all consuming method/selection/confidence remain NONINPUT.
Prior exposure is not erased; no clean-cognition/noninfluence certificate.

A9 proved that a noncrossing family with t packets and r roots, whose packet products lie in normal K and aggregate to1, has chronological error expressible by at most t−r SINGLE relative commutators.
The theorem here shows that a uniform smaller bound is impossible, even in finite groups with an ACTUAL proper normal K and at the ORIGINAL n-occurrence selector cardinality.
The full construction and lower bound are given independently, not inferred from a review of A9.

**Theorem A.** For EVERY positive integer s and EVERY odd prime p there exist:

- an actual finite group G, n=|G|, and an actual PROPER normal K;
- an actual word of the FULL original length2n−1;
- a selected n-occurrence set U with a noncrossing packet partition having t−r=s;
- all actual packet products in K, with their first-occurrence aggregate1;

such that the chronological product over U has relative commutator length EXACTLY s with respect to K.
Here a relative commutator factor means u v u^-1 v^-1 with u∈G,v∈K; length is the least number of such factors in a product.
The ambient word has OTHER correct n-occurrence identity selectors. It is not a counterexample to O(G).

## 2. Actual finite group and proper normal subgroup

Let V=F_p^(2s), with basis e_1,…,e_(2s).
Let W be the vector space with basis w_(ij),1≤i<j≤2s. Define the alternating bilinear map

`Ω(u,v)=sum_(i<j)(u_i v_j−u_j v_i) w_(ij)`.

Define a group on the ACTUAL finite set V×W by

`(u,A)(v,B)=(u+v,A+B+Ω(u,v))`.

Both bracketings of three factors have central coordinate
`A+B+C+Ω(u,v)+Ω(u,w)+Ω(v,w)` by bilinearity, so multiplication is associative.
The identity is(0,0), and the inverse of(u,A) is(−u,−A) because Ω(u,u)=0.
The subset {0}×W is central. Thus this is an actual group, of order

`n=p^(2s+binomial(2s,2))`.

No multiplication table, selected coordinate tuple or computation is used to test it.

Let V0=span{e_2,e_4,…,e_(2s)} and K=V0×W.
It is a subgroup because V0 is closed under addition and all second coordinates lie in W.
Conjugation leaves a group's first coordinate v unchanged and changes only its W coordinate, so K is normal.
It is proper because e_1∉V0. Its quotient is the ACTUAL additive group V/V0; no quotient faithfulness or external group classification is assumed.

## 3. Every relative commutator has rank at most2

Associate each C∈W to its skew-symmetric2s×2s matrix whose upper-triangular coefficients are those of C.
For Ω(u,v), this matrix is `u v^T−v u^T`; its image lies in span{u,v}, so its rank is at most2.
This is an exact all-variable linear-algebra bound, not a numerical rank computation.

The actual group law gives

`(u,A)(v,B)(u,A)^-1(v,B)^-1 = (0,2Ω(u,v))`.

Central coordinates A,B cancel, so this describes EVERY group commutator, in particular every relative commutator with the second factor in K.
All these elements lie in the central {0}×W, and their products add their W coordinates.
A product of m relative commutators therefore has associated matrix rank at most2m: its image is contained in the span of at most2m displayed vectors.
No assumption that every skew matrix is a single commutator is made.

## 4. An actual error requiring exactly s relative commutators

For i=1,…,s set

`a_i=(e_(2i−1),0)`, `x_i=(e_(2i),0)∈K`.

Use s disjoint three-occurrence components

`a_i, x_i^-1, a_i^-1 x_i`.

Within component i, the outer packet consists of its first/third actual occurrences and has product x_i; the inner singleton packet has product x_i^-1.
The pattern is noncrossing, with s roots and2s packets, and first-occurrence aggregate

`x_1 x_1^-1 … x_s x_s^-1=1`.

Its ACTUAL chronological product is the product of s relative commutators

`E=product_(i=1..s) a_i x_i^-1 a_i^-1 x_i`
` =(0,−2 sum_(i=1..s) Ω(e_(2i−1),e_(2i)))`.

The sign and coefficient follow directly by applying the group law to each four-factor product; replacing v by−v in §3 gives−2Ω.
Each x_i^-1 lies in K, so these are legitimate relative commutators.
Thus the relative commutator length of E is at most s.

Its associated skew matrix is−2 times a block diagonal matrix with s blocks `[[0,1],[-1,0]]`.
Every such block has zero kernel, and−2 is nonzero for EVERY odd prime p. Thus the WHOLE matrix has rank EXACTLY2s.
By §3 a product of fewer than s relative commutators could have rank at most2(s−1), contradiction.
The relative commutator length of E is therefore EXACTLY s.
This is a proof for ALL p,s in the domain, not selected finite witnesses or a computation of a particular commutator width.

## 5. FULL original length/cardinality, with no avoiding-word confusion

The above components use3s actual positions.
There are enough positions to pad to the group's ACTUAL order n: indeed

`n ≥ p^(2s) = (1+(p−1))^(2s) ≥ 1+2s(p−1) ≥ 1+4s ≥ 3s+1`.

These are universal inequalities for p≥3,s≥1, not sampled parameters.
Append n−3s identity letters as SINGLETON ROOT packets and let U be these first n positions.
Its packet count and root count are

`t=2s+(n−3s)`, `r=s+(n−3s)`, so `t−r=s`.

Every added packet has product1∈K. The first-occurrence aggregate remains1 and the chronological product remains E, of exact relative commutator length s.
U contains EXACTLY n distinct ACTUAL occurrence labels, not a shortened word or a compressed formal block.

Now append another n−1 identity letters outside U. The full word has EXACTLY2n−1 original positions.
The number of identity positions is at least2n−1−3s≥n, by n≥3s+1.
Selecting n such identity occurrences gives a correct original-order identity selector.
Thus the full word is NOT avoiding, and the theorem is NOT an original Olson counterexample.
It is an exact original-cardinality countercertificate showing that the displayed noncrossing kernel-zero U can carry irreducible error complexity t−r.

The packets here have sizes2 or1; they are not asserted to satisfy the uniform |G/K|-packet hypothesis of any separate normal-extension theorem.
Their use is the general actual-packet coupling lemma, which explicitly allowed arbitrary packet sizes. No uniform-size premise is silently claimed.

## 6. Exact significance and degenerate scope

The upper bound t−r in A9 is attained for every positive s in a universally specified finite family, even with a proper normal subgroup and original n/2n−1 cardinalities.
Thus a proof cannot uniformly replace the entire selected suffix-defect product by fewer relative commutators merely because the forest is noncrossing or its packet aggregate is1.
It must use additional ACTUAL value/incidence coupling, not only the number of roots or a normal-subgroup containment statement.

This is a sharpness/obstruction theorem for a transport primitive, not a no-go for some OTHER selector or a statement that every actual word has such a hard defect.
The case s=0 is the separated zero-defect regime and needs no construction. Characteristic2 is excluded from THIS construction because2Ω would vanish; no char2 result is inferred by division or a limit.
The existence of original selectors in these finite groups is not presented as new p-group discovery; the entire p-group existence subtarget is already PRIOR/REPRODUCTION under Main's statement-only screen.
Novelty/priority of this elementary commutator-width construction is unestablished and not claimed.

## 7. Dependency and control ceiling

Ordinary inputs are elementary finite vector spaces, bilinear maps, matrix-image rank bounds, group associativity/inverses/normality and integer counting; the group construction and every specialized use are proved inline.
No exterior-algebra classification theorem, group algebra, p-group source proof, actual program, selected control or external paper is imported.
This needs its own frozen full mathematics AND actual-caller/source-separation review before adoption; no existing scope or confidence is enlarged by this file.

Every affected Dimitrov source/proof/method line and prospective augmentation/group-algebra route remains STOPPED; extra displayed context/method/selection/confidence NONINPUT.
A5/A6 existence PRIOR/REPRODUCTION, all other original/mixed-prime claims at their separate unreviewed cuts; original ALL-finite-group and old odd-prime dihedral gaps unresolved.
All STOP/HOLD/ZERO outside S1, nine held formulas/consumers, v214-A/threshold/v227, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and findings persist.
No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numerical/state/control/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infrastructure action or timer/heartbeat loop.
WRITTEN/same harness, not formal/kernel/human/configured-family/executable/novelty acceptance. Same18/new exclusive append-only root/actual20min substantive cadence with honest gaps/science ends2026-10-31T21:23:27.000Z.

**END OF COMPLETE FINITE-GROUP SHARPNESS RESULT.**
