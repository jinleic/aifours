# Sun8 normal-extension successor: complete prime-five and prime-seven quotient transfer

Actual `/bin/date` before this NEW body: **Tue Oct 27 15:04:17 PDT 2026**. Owner **MathSun8-2**, same original math-6 and narrow definition-first release. **WRITTEN candidate**, not parent-adopted, kernel/formal, executable, configured-family/human or novelty-verified. No machine arithmetic, selected group/control test or legacy proof input.

## 1. Precise theorem and inputs

Retain the exact unrestricted eight-ACTUAL-left-coset assertion released in S2. Use `Sun8(X)` as the property defined in v2, not a premise claimed for all X.

**Theorem 1.1.** Let N be ANY normal subgroup of ANY group G. If `Sun8(N)` and `G/N` has prime order p with **p=5 or p=7**, then `Sun8(G)`.

This is a full extension theorem with an explicit kernel premise, not a numerical instance, a direct-product-only result or an unconditional original Sun8 solution. Neither G nor N is assumed finite. No splitting, normal U_i, equal original indices or cover is assumed. The two p values exhaust the stated theorem's literal quotient classes; they are not chosen diagnostic inputs.

Inputs actually used:
- Released original definitions and elementary subgroup/index facts, fundamental prime factorization and finite pigeonhole/counting.
- The elementary two-disjoint-coset gcd≥2 proof in v1 §2, valid for every group.
- **Arbitrary-group Sun7, STATEMENT ONLY**, licensed by the current controls: seven actual disjoint finite-index left cosets have a pair of indices with gcd≥7. No Sun7 proof component, old source/mixed/private-factor method or body is used.
- Exact actual-fibre identity v1 §3 and the common-fibre transfer v2 §3, whose proofs are elementary and supplied in those new packets.

Zhu3/4 is not needed for this theorem. No Sun5, Sun6, global Sun8(N) theorem, old P7/simple-bound theorem or old least-order descent is silently imported.

## 2. Forced seven-divisibility in ANY hypothetical eight-coset counterconfiguration

Suppose eight actual disjoint finite-index G-cosets have indices n_i with `gcd(n_i,n_j)≤7` for all distinct pairs. Apply licensed Sun7 to EVERY seven-member subfamily. Its certificate must have gcd exactly7, so both of its indices are divisible by7.

**Lemma 2.1.** At least THREE of the eight n_i are divisible by7.

If at most two were, choose a seven-member subfamily containing at most one of them (delete one if there are two). No pair in that subfamily could have gcd7, contradicting Sun7. This is the entire subfamily argument, not a selected subfamily probe. Moreover, on the set of seven-divisible labels, writing `n_i=7t_i` gives pairwise-coprime t_i because `7*gcd(t_i,t_j)=gcd(n_i,n_j)≤7`.

Only this direct statement-level consequence is used below. It gives no eight-P7 reduction, quotient rank or new constituent bound.

## 3. Common structural consequences when the quotient has order p=5 or7

Assume a counterconfiguration exists in an extension from Theorem1.1. Write Q=G/N, `A_i=π(U_i)`, `a_i=[Q:A_i]`, `b_i=[N:N∩U_i]`; the original n_i equals a_i b_i. Since |Q|=p is prime, every A_i is either Q or1.

Call a label **proper-image** when a_i=p, and **full-image** when a_i=1. Let their counts be m and r=8−m. A proper-image quotient coset is one actual point of Q; every full-image quotient coset is Q.

If m=0 or1, all eight quotient cosets have a common point. The common-fibre transfer, using the EXPLICIT Sun8(N) premise, contradicts the counterconfiguration. Hence

`m>=2`.                                                        (3.1)

For any two proper-image labels,

`p*gcd(b_i,b_j)=gcd(n_i,n_j)<=7`.

Since p=5 or7, this forces `gcd(b_i,b_j)=1`. If two proper-image quotient points were equal, the actual N-fibre would contain two disjoint cosets with coprime subgroup indices, impossible by the elementary two-coset fact. Thus ALL proper-image points are distinct:

`m<=p<8`, so r>=1.                                              (3.2)

**Lemma 3.1. Every full-image original index n_j is prime to p.** If p divided n_j, write n_j=p c. Pairwise coprimality of the at least two proper-image b_i permits one proper i with p not dividing b_i. The original gcd condition gives `p*gcd(b_i,c)≤7`, so gcd(b_i,c)=1 because p=5 or7. Hence gcd(b_i,n_j)=1. But the full-image j and proper-image i meet the same quotient point, giving two disjoint ACTUAL N-cosets of indices n_j and b_i. This contradicts §2's elementary two-coset fact. □

For EVERY full j and EVERY proper i, their common quotient point also gives

`2 <= d_ij:=gcd(b_i,n_j) <= 7`.                                 (3.3)

The lower bound is the actual N-coset consequence. The upper bound follows because d_ij divides the ORIGINAL pair gcd. For a fixed j the d_ij are pairwise coprime as i varies, since the b_i are pairwise coprime. These are SAME actual sources, not independent abstract divisors.

## 4. Complete p=7 proof

Lemma3.1 says no full-image original index is divisible by7. All seven-divisible labels are therefore the proper-image ones. Lemma2.1 gives m≥3, while (3.2) gives at least one full label j.

For fixed full j, every d_ij from (3.3) is between2 and7 and prime to7. Each has a prime divisor from `{2,3,5}`. Pairwise coprimality of the d_ij means these prime supports are disjoint. Thus m≤3. Consequently m=3, r=5, and all three primes2,3,5 must divide n_j.

This argument holds for EVERY full j. There are five such labels, so two original indices share the divisor `2*3*5`, which is greater than7. This contradicts the counterconfiguration. All p=7 cases are now closed, including m=0/1 by the common-fibre argument and m≥2 by the preceding proof. □

## 5. Complete p=5 proof

For proper-image labels the b_i are still pairwise coprime. At most ONE original proper-image index can be divisible by7, because two would have original gcd at least35. Lemma2.1 therefore forces at least TWO full-image labels whose original indices are divisible by7. Denote that set by F7. Lemma3.1 says all full-image indices are prime to5.

Fix j∈F7. The pairwise-coprime d_ij from (3.3) are between2 and7 and prime to5; their prime supports lie in `{2,3,7}`. Therefore m≤3. If m=3, all three primes2,3,7 divide n_j. This holds for every j∈F7, of which there are at least two, contradicting the original pair gcd≤7. Thus m≤2, and (3.1) forces

`m=2`, r=6.                                                    (5.1)

Write the two proper-image N-indices as b_1,b_2; they are coprime.

If neither is divisible by7, then for every j∈F7 both d_1j and d_2j have prime supports in `{2,3}` and are coprime and greater than1. Thus both2 and3 divide n_j. Two members of F7 would then share2,3,7, again impossible. Consequently exactly ONE b_i is divisible by7; relabel it b_1. Then b_2 is prime to7.

For each j∈F7, `gcd(b_2,n_j)≥2` has a prime divisor in `{2,3}` (n_j is prime to5 and b_2 to7). Two distinct members of F7 cannot share either2 or3, because they already share7 and their original gcd is at most7. Their nonempty `{2,3}` supports must therefore be disjoint. Since |F7|≥2, it follows that |F7|=2 and BOTH2 and3 divide b_2. Coprimality of b_1,b_2 makes b_1 prime to2 and3.

There are six full-image labels but only two in F7. Choose ANY other full label k. Its n_k is prime to5 by Lemma3.1 and prime to7 by its choice. Equation(3.3) requires `gcd(b_1,n_k)` between2 and7. Any such common divisor has a prime factor in `{2,3,5,7}`. But b_1 is prime to2,3 and n_k is prime to5,7, so no such divisor exists. This contradiction closes m=2 and therefore every p=5 case. □

## 6. Finite p-group quotients and the minimum-counter consequence

**Corollary 6.1.** Theorem1.1 extends to EVERY finite p-group quotient for p=5 or7, with the same Sun8(N) premise.

For completeness, a nontrivial finite p-group Q has nontrivial center: every noncentral conjugacy-class size is divisible by p, so the class equation makes |Z(Q)| divisible by p. A nonidentity central element has p-power order by Lagrange; a suitable p-power of it has order p. Let C be its central subgroup of order p, and H the actual preimage of C in G. Then H normal in G and H/N has order p. Theorem1.1 gives Sun8(H). Induct on |Q| and apply the same assertion to G/H with quotient Q/C. The trivial quotient is the tautological base. This is ordinary all-variable p-group/index reasoning, no program or tested p-group.

Combining with v2's R7 theorem also covers finite p-group quotients p>7. Thus, conditional on its existence, a minimum-order finite Sun8 counterexample (obtained by v2's fully source-preserving finite-core reduction and ordinary well-ordering) has NO nontrivial finite p-group quotient for ANY prime p≥5. In particular it has no quotient C_p with p≥5.

This does NOT prove the minimum counterexample simple, does not remove prime2/3 quotient possibilities and is not the old historically NR finite-simple/least-order descent imported as a premise. Existing old frozen statements retain their ASOF review status; this is a new explicitly proved successor only.

## 7. Exact actual-object caller, remaining gap and next step

For every theorem here, the forward caller is the SAME original U_i,g_i in G and the actual projection/fibre identities. Conversely the fibre intersection equivalence detects every original intersection, but the auxiliary divisor and quotient-point conditions do not construct a new G configuration. All repeated subgroup, index1, infinite-kernel and nonsplit-extension cases are retained. Sun8(N) is used exactly for m=0/1/common-fibre closure; it is NOT inferred from Sun7.

**Progress over v1/v2:** a complete conditional Sun8 normal-extension theorem through prime5 and prime7 quotients, then all finite p-group quotients p≥5. This is a genuine coupling result using actual fibres and the licensed seven-coset theorem, not an inconsequential list, another classical-family range or a conditional finite-simple size bound. No novelty priority is claimed.

**Still unproved:** general extension closure, actual mixed-fibre transfer through prime2/3 quotients, arbitrary finite-simple components, original Sun8, P7 emptiness/whole-source reduction and any genuine counterexample. The next genuinely admitted task is to isolate the exact simultaneous-fibre obstruction for prime2/3 quotients with the same actual sources; Sun5/6 may NOT be silently added as imports. If only an unavailable statement or an excluded guide would continue a branch, that branch will stop with the exact prerequisite. No claim of all-route exhaustion.

These proofs are derived from current definitions/elementary facts/STATEMENT-level Sun7 alone. No old 5+2/mixed source proof, private-factor method, v233/v234 mathematical material, legacy checkpoint/park/scout/source, primary PDF/book extraction, held guide or consuming confidence/selection path is used. Prior authorship/exposure and every process finding persist; no clean-cognition/independent-reconstruction claim.

No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/boundary probe, nested agent/modelCLI/paidAPI/newGO, Git/delete/publication/contact/infrastructure action, timer/poll/heartbeat. Machine work metadata only. N4 UNKNOWN historical child exit unestablished, auxiliary214 STOP and HOLDv2 unchanged. Same narrow written release; original STOP outside it persists. New deadline2026-10-31T21:23:27.000Z; no earlier cutoff, no final park, original solution or stronger acceptance.
