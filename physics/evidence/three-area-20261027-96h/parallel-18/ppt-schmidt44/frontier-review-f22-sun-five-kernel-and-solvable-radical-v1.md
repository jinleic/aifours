# f22 — five/small-prime kernels and solvable radical reduction

Reviewer **PhysicsPPT44-2**. Actual native clock immediately before creation: **Wed Oct 28 17:25:26 PDT 2026**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR.** The separate five-power candidate is valid with its explicit `Sun8(N)`, `Sun8(G/N)` and `Sun7(G)` premises; its successor validly removes the kernel Sun8 premise for p=2,3,5. The two-way solvable-normal-kernel and radical conclusions are **conditional on the arbitrary-group Sun7 import and the named kernel-transfer results**. Sun7 is not proved or independently authenticated here. No unrestricted Sun8, formal/kernel, human, configured-family, novelty or publication acceptance follows.

## 1. Inputs, exposure and caller

- Complete assignment `f22-sun-five-kernel-and-solvable-radical/assignment-v1.json`: SHA256 `dead33d2312db6aafde8f2868f872a4a3f1592967a0b0f651021b355d2397d0f`.
- Complete 107-LF `frontier-20261028-five-kernel-transfer-v1.md`: SHA256 `db77a984622e4d624fb22ec319ed0ee1ea7478eb1500d6281b06309df7a63fb3`.
- Complete 130-LF `frontier-20261028-solvable-kernel-reduction-v1.md`: SHA256 `af44cb81b44803145daff8fcca736fb14d17c0960bc1b1d53128ce4c7df94b29`.
- Registered actual-left-coset definitions; prior independently reconstructed seven-kernel review `frontier-review-f20-sun-seven-kernel-transfer-v1.md`, SHA256 `787750b7b009ea14c148987b1b38359ff57a2e9cc58fb4d4d9998830a041020d`; and dual/solvable-quotient review `frontier-review-f16-sun-c2-and-dual-k-v1.md`, SHA256 `44cd1e9b36b6737a26c05044295c2f6e2f60a0320869e1bae9c878a7caac8235`.

I have earlier Sun-coset familiarity and authored the cited reviews; this is not blind, independent-model-family or clean-cognition review. Previous quarantined outcomes and the author's support-check outputs are not proof premises. The current claims and the necessary actual-coset interfaces are reconstructed below. No author contact or nested agent was used.

## 2. Common actual-fibre facts and quotient heredity

For any group X, `Sun_k(X)` requires every k pairwise-disjoint actual left cosets of finite-index subgroups to have a pair whose subgroup indices have gcd≥k. It is vacuous if there are too few such cosets. Original groups and kernels may be infinite, subgroups need not be normal, and cosets need not cover.

For N normal in G, set Q=G/N and for an original actual coset g_iU_i put `C_i=π(g_i)π(U_i)`, `a_i=[Q:π(U_i)]`, `b_i=[N:N∩U_i]`, `n_i=[G:U_i]`. Since NU_i is a subgroup and `N/(N∩U_i)→NU_i/U_i` is a coset bijection, `n_i=a_i b_i`. When two actual quotient cosets meet, choose a common point and a common representative t. Each original intersection with tN becomes, after translating by t⁻¹, an actual N-coset of N∩U_i. The original disjointness keeps these fibres disjoint.

Two disjoint finite-index cosets in any group have noncoprime indices. If the indices were coprime, the diagonal injection from the intersection-subgroup coset space into the product of the two coset spaces would have cardinality both divisible by and at most the product, hence would be onto and the two prescribed cosets would intersect. Thus meeting quotient images require `gcd(b_i,b_j)≥2`. If b_j=1, that coset's nonempty fibre is the whole N, so C_j is disjoint from every other original image C_i.

For any epimorphism G→Q, `Sun_k(G)⇒Sun_k(Q)` without any kernel assumption: take the inverse images of arbitrary disjoint Q-cosets. They are disjoint actual G-cosets, and preimage-subgroup indices are exactly the quotient indices. This is the unconditional forward direction in the radical statement.

## 3. Five-power theorem, with its explicit kernel premise

Assume every finite-index subgroup of N has 5-power index, `Sun8(N)`, `Sun8(Q)` and `Sun7(G)`. Suppose eight original disjoint cosets have all original pair gcds≤7. Let I={i:b_i>1}, r=|I|. Two cluster original indices both contain 5, so their gcd is exactly 5; consequently `gcd(n_i/5,n_j/5)=1`, and each quotient index a_i divides n_i/5. The cluster a_i are pairwise coprime.

For r≤1, meeting quotient cosets would require two nontrivial b-indices, so all eight images are disjoint; `Sun8(Q)` gives a forbidden original pair. For r=8, the cluster a_i are pairwise coprime, so the diagonal map to the product of quotient coset spaces is onto. The actual eight quotient cosets have a common point, and the eight actual disjoint fibres contradict the explicit `Sun8(N)` hypothesis. Now 2≤r≤7.

Apply `Sun7(G)` to every seven-subfamily. Under original gcd≤7, each certificate has gcd exactly 7, so at least three original indices are seven-divisible. Since b_i is a 5-power, 7|n_i iff 7|a_i; at most one cluster a_i has 7 by cluster coprimality. If one cluster index carries 7, its original index carries 35, so no outside seven-index can contain 5. If none does, at least three outside indices carry 7 and at most one can also contain 5, because two seven-indices have gcd exactly 7. Thus there are two outside labels V,W with indices divisible by 7, prime to 5, and `gcd(a_V,a_W)=7`.

For any cluster label whose a_i is not seven-divisible, its quotient image is disjoint from both outside images. The quotient two-coset lemma makes both respective index gcds nontrivial; each divides an original gcd≤7. The possible shared primes are 2 or 3, and because V,W share no prime other than 7 they must be distinct. Thus `6|a_i`. Cluster pairwise coprimality allows at most one such cluster and at most one seven cluster. Since r≥2, r=2: label A has 7|a_A and B has 6|a_B. Relabel V,W so 2|a_V, 3|a_W; their gcd 7 excludes 3 from V and 2 from W, and both exclude 5.

There are six outside labels. A further outside seven label T would be prime to 5 because 35|n_A, and prime to 2 and 3 because of its exact gcd 7 with V,W. Its quotient image is disjoint from B's, but their index gcd≤7 cannot contain 2,3,5,7: T lacks the first three and B lacks 7. Impossible. Thus V,W are the only outside seven labels.

Choose one of the four remaining outside labels F. It lacks 7. Disjointness from V and W forces 2|a_F and 3|a_F. Disjointness from A forces a common prime ≤7; since a_A is coprime to a_B and 6|a_B, a_A lacks 2,3, and F lacks 7, so 5|a_F. Every one of those four outside indices is divisible by 30, making two original gcds at least 30. Contradiction. This pays the five-kernel theorem at the precise stated hypotheses and actual-fibre quantifiers.

Separately, if `Sun7(N)` is known under the five-power spectrum, applying it to any seven of eight N-cosets yields a pair gcd that is a 5-power ≥7, hence at least 25≥8. Thus Sun7(N) suffices for Sun8(N). The **universal** Sun7 import supplies it, but Sun7(G) alone is not silently assumed to imply Sun7(N).

## 4. Small-prime kernel theorem without any Sun8(N) premise

Let p∈{2,3,5}, every finite-index subgroup of N have p-power index, and assume `Sun7(G)` and `Sun8(Q)`. Suppose eight actual disjoint G-cosets are a counterconfiguration. As before let I={i:b_i>1}, r=|I|. If r≤1, all quotient images are disjoint and Sun8(Q) contradicts the original gcd bound. Assume r≥2.

Sun7(G) forces at least three seven-divisible original indices. Each cluster index is divisible by p; at most one cluster can be seven-divisible, because two would have gcd≥7p>7. Consequently there are at least two outside seven-labels. If a cluster index is seven-divisible, every outside seven-index is prime to p, since it otherwise shares 7p with that cluster. If none is, at least three outside seven-indices exist and at most one is divisible by p, since any two have gcd exactly 7. In either case choose two outside labels V,W such that both indices carry 7, both are prime to p, and their gcd is 7.

Let q,s be the two primes in {2,3,5} other than p. An outside quotient coset is disjoint from every other quotient coset. For any cluster label i whose original index lacks 7, its a_i also lacks 7. Its quotient gcd with each of V,W is nontrivial and at most 7. Because V,W are prime to p, the shared primes lie in {q,s}; because V,W have gcd 7, the two primes are distinct. Thus `qs|a_i` and `pqs=30|n_i`.

Two non-seven cluster labels would both have original indices divisible by 30, impossible. At most one cluster label is seven-divisible, and r≥2, so exactly two cluster labels exist: seven-label A and non-seven B. Then `qs|a_B`, `30|n_B`; relabel V,W so `q|a_V`, `s|a_W`, while `s∤a_V` and `q∤a_W`.

A third outside seven-label T would be prime to p by n_A's factor 7p, prime to q by its gcd 7 with V, and prime to s by its gcd 7 with W. Its disjoint quotient coset would need a common prime ≤7 with C_B, but B lacks 7 and T lacks p,q,s. Hence no such T exists. There are six outside labels, so choose F outside distinct from V,W; F is not seven-divisible. Its quotient gcds with V,W force `qs|a_F=n_F`.

For p=2, qs=15; for p=3, qs=10. In either case qs>7 divides n_B and n_F, contradiction. For p=5, qs=6. Both n_A,n_B contain 5, so their gcd under the bound is exactly 5; a_A and a_B divide n_A/5,n_B/5 and are coprime. Since 6|a_B, a_A lacks 2,3. The disjoint quotient cosets F,A must have a common prime ≤7; F lacks 7 and A lacks 2,3, so 5|a_F. Then 30 divides n_F and n_B, contradiction.

This proof uses neither Sun8(N) nor Sun7(N), and covers all r, including r=8: the deduction of **two outside seven-labels** under r≥2 already excludes r=7,8. It retains repeated labels/indices, nonsplit extensions, infinite G/N and the same actual quotient/fibre objects.

## 5. From prime kernels to solvable normal kernels

For p=7, the previously reviewed f20 theorem independently shows that the 7-power index spectrum itself implies Sun8(N), and `Sun7(G)` plus `Sun8(G/N)` gives Sun8(G). For p≥11, the previously reviewed f16 dual theorem applies without Sun7(G): disjoint finite-index N-cosets have nontrivial gcd, and every prime dividing a kernel index is at least p≥11, so their gcd is ≥8. Thus N has pair-gap 8 and quotient Sun8 transfers upward. Together with §4, these cover all prime-power kernel indices.

Let F be finite and R normal and solvable. Its derived series has finite abelian factors. Within each factor, its p-primary subgroups and products over any initial set of primes are characteristic. Pull these chains back through the derived subgroups of R. Since the derived subgroups are characteristic in R and R is normal in F, every resulting subgroup R_i is normal in F; every factor R_i/R_{i−1} is a finite p-group. The series need not make R nilpotent.

Assume `Sun8(F/R)` and the **universal** Sun7 statement. Descend the series from R_d=R to R_0=1. At each step the quotient map `F/R_{i−1}→F/R_i` has p-group kernel, so its finite subgroup indices are p-powers; universal Sun7 supplies the needed property of `F/R_{i−1}` for p≤7. The appropriate prime-kernel theorem transfers Sun8 to `F/R_{i−1}`. Induction gives Sun8(F). The reverse quotient direction is unconditional by §2.

## 6. Arbitrary groups with only solvable finite kernel images

Let R normal in arbitrary G, and suppose every finite homomorphic image of R is solvable. Assume `Sun8(G/R)`, universal Sun7, and the cited prime-kernel theorems. For a hypothetical original eight-coset counterconfiguration, let K be the intersection of the finitely many cores of its finite-index subgroups U_i. Each core is the kernel of a permutation action on the finite coset space G/U_i; K is finite-index normal and K⊆U_i for each i.

Put F=G/K and `Rbar=RK/K`. The original cosets are exact inverse images of the corresponding actual F-cosets because K⊆U_i, so the F-cosets remain pairwise disjoint with exactly the same indices. Rbar is a finite homomorphic image of R and is solvable. The quotient `F/Rbar` is a quotient of `G/R`; unconditional quotient heredity transfers Sun8 to it. Section 5 then gives Sun8(F), contradicting the projected configuration. Thus, under the named imports, `Sun8(G/R)⇒Sun8(G)`; the reverse holds unconditionally.

This does not assume R finite, that every group with only solvable finite images is itself solvable, or that arbitrary nonsolvable kernels transfer. Ordinary finite-derived-length solvable R is included because all its images are solvable.

## 7. Conditional finite minimum-counterexample conclusions

The same core reduction shows any original counterconfiguration produces a finite one with the same actual cosets/indices. If a minimum-order finite counterexample G has nontrivial solvable radical R, then G/R is smaller and has Sun8 by minimality; §5 transfers Sun8 to G, contradiction. Hence the solvable radical is trivial under universal Sun7 and the named kernel transfers. Its existence in a finite group follows because products of solvable normal subgroups are solvable normal, and a maximal product exists in finite order.

Separately, the solvable-**quotient** transfer established/reconstructed in f16 gives perfectness: nontrivial abelianization would yield a proper smaller commutator subgroup satisfying Sun8 and a finite solvable quotient, contradicting transfer. Thus the hypothetical minimum is both perfect and radical-free under all named imports. Neither property alone or together implies simple, and no simple-group classification or unconditional original solution follows.

The five-kernel candidate's weaker intermediate Fitting conclusion is also valid: combined with the seven-kernel and dual p≥11 results, it excludes normal p-subgroups except possibly p=2,3. Sylow subgroups of a finite normal nilpotent subgroup are characteristic in it and hence normal in G, so its prime divisors lie in {2,3}. The later radical-free conclusion is stronger under its broader set of named assumptions.

## 8. Independent bounded incidence check

I separately wrote `frontier-20261028-review-f22-small-prime-check.py`, SHA256 `e7aac070ae5c4c0aacf0d92e8548793333b35005040d42c30fb187973f725094`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f22-small-prime-check.py`.

For p=2,3,5 and each cluster size r=2,…,7, it explores squarefree quotient-index supports on {2,3,5,7}, with repeated supports allowed and ordering only removing label permutations inside each symmetric sector. It uses p·a_i as a divisor of an actual cluster original index, original gcd≤7, noncoprime quotient indices whenever an outside label is involved, and the necessary three-seven-label condition. Every actual shared prime in a required quotient gcd is ≤7 under the original bound, so forgetting other primes and higher valuations is an overapproximation. The bound of at most one seven cluster is independently valid because two cluster original indices containing both p and 7 would share 7p>7.

Actual output had **no model in all 18 (p,r) cases**. Explored nodes, ordered r=2,…,7, were:

```text
p=2: [1470,1357,1372,1581,2036,1]
p=3: [812,682,636,684,822,1]
p=5: [166,113,161,213,265,1]
```

The r=7 pruning reflects that at most one cluster and one outside label could be seven-divisible; it does not silently exclude a valid Sun7-forced model. This independently written finite check supports the incidence arithmetic only. It neither creates actual group cosets, verifies Sun7 or quotient Sun8, nor substitutes for §§2–7. The author's check was not rerun or treated as independent evidence.

## 9. Exact disposition and limits

| Claim | Disposition |
| --- | --- |
| Five-power candidate LF1–74 | NO_SUBSTANTIVE_DEFECT with `Sun8(N)`, `Sun8(Q)`, `Sun7(G)` explicit |
| Five-power `Sun7(N)⇒Sun8(N)` | NO_SUBSTANTIVE_DEFECT; spectrum and seven-coset premise both required |
| Successor small-prime p=2,3,5 kernel theorem | NO_SUBSTANTIVE_DEFECT; no kernel Sun8 premise is used |
| Quotient heredity, solvable-series lifting and arbitrary finite-core descent | NO_SUBSTANTIVE_DEFECT with the stated universal Sun7 and named p=7/large-prime transfers for the upward direction |
| Minimum finite counterexample perfect and radical-free | NO_SUBSTANTIVE_DEFECT conditional on the kernel- and quotient-transfer imports; no simplicity conclusion |

No gap needing an actual counterexample to these conditional claims was found. Unrestricted Sun8, arbitrary nonsolvable kernels, proof/primary-source authentication of the Sun7 import, source/book equivalence and novelty remain open. Parent must inspect complete candidate and review bodies before adoption. Earlier immutable quarantine records remain historical and are not retrospectively validated.
