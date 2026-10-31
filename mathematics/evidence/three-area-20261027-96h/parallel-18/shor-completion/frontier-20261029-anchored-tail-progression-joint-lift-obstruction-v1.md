# Shor completion: an actual-anchor obstruction to an undilated joint lift

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 14:23:49 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE.** The theorem below is a concrete all-parameter obstruction for a specified actual-tail family, not a representation-only variant and not a claim about arbitrary Q. It uses the actual, undilated direct tiling and the literal head anchors together. The cyclic-tiling theorem has an elementary written proof; only the conditional original-code caller at the end imports an external theorem. The unrestricted Shor completion problem remains OPEN.

## 0. Statement and scope

Put

    A={0,3,8,11},      Y={0,1,7,13,14}.

Let R>1 and D≥1 be arbitrary integers, and let n=75RD. For each y∈Y choose an arbitrary integer b_y satisfying b_y≡y (mod 75). In Z_n define the **same actual tail**

    Q = { b_y+75t (mod n) : y∈Y, 0≤t<R }.                      (0.1)

The five starts may differ and the progressions may wrap modulo n. Since the y's are distinct mod75, and R≤RD, the 5R displayed residues are distinct.

> **Theorem.** No P⊆Z_n with A⊆P satisfies the undilated direct tiling P⊕Q=Z_n. In fact the proof uses only the head anchors 0,3,11; the tail statement does not need to assume Y⊆Q. Consequently it also covers every Q of (0.1) that does contain all five literal tail anchors.

There is no parity, prime-splitting, T2, extra head cardinality, special choice of D, or named earlier candidate assumption. Necessarily |P|=15D. For example, R=33 and D=16 cover a head cardinality 240=15·16 at n=39600, with genuine shared odd head-prime factors 3 and5; this is **not** an exclusion of every tail Q at that order. For general D, the odd part of |P| may contain any number of additional distinct primes.

The written argument below is self-contained up to the elementary algebra of cyclotomic polynomials. The owner has prior same-author exposure to five-power, head-15, fibre/cofactor and other prior work; no blindness, clean-cognition or independent-provenance claim is made. In particular no f232/f233 review or adoption, no previous theorem, scalar/arc-consistency verdict, solver outcome, or HELD/ZERO/NONINPUT body is used as a premise. No old review is transferred.

## 1. A periodic factor forced by the actual tail

Set B={p+b_y (mod n):p∈P,y∈Y}. Because the displayed b_y+75t are distinct and P⊕Q is direct, the map (p,y)↦p+b_y is injective and

    B ⊕ {75t:0≤t<R} = Z_n.                                     (1.1)

For r=0,…,74 let

    B_r={h∈Z_(RD): r+75h ∈ B}.

Restricting (1.1) to the r-class and dividing by75 gives

    B_r ⊕ {0,1,…,R−1} = Z_(RD).                               (1.2)

Let f_r be the indicator of B_r. Subtracting the two consecutive convolution identities for x and x−1 in (1.2) gives f_r(x)=f_r(x−R). Thus f_r is R-periodic. Since every length-R window sums to1, **exactly one** residue modR is occupied, and B_r is one full coset of RZ_(RD). In particular,

    b,b′∈B, b≡b′ (mod75)  ⇒  b≡b′ (mod75R).                 (1.3)

This is an exact consequence of the actual factorization, not a quotient relaxation. It keeps the joint endpoint/carry information that was missing from independent-row checks.

## 2. All head residue classes in an active mod5 fibre occur

Write k_r=|{p∈P:p≡r (mod75)}| for r∈Z_75, and set

    K(X)=Σ_(r=0)^74 k_r X^r,
    F(X)=1+X+X^7+X^13+X^14,
    G(X)=1+X+⋯+X^74.

By (1.2), each B_r has exactly D elements. Directness of P+B_starts and b_y≡y (mod75) give

    K(X)F(X) ≡ D G(X)      (mod X^75−1).                        (2.1)

The gcd of F and X^75−1 over Q[X] is exactly Φ_5. Indeed F(1)=5, F has one exponent in each class mod5 and hence Φ_5|F. Mod Φ_3 the remainder is 2X. With

    Φ_15=X^8−X^7+X^5−X^4+X^3−X+1,

its remainder is

    3−X^2+X^3−2X^4+X^5+X^6−X^7,                               (2.2)

which is nonzero. The remaining divisors Φ_25 and Φ_75 have degrees 20 and40, greater than deg F=14. Since X^75−1 has simple roots, these checks establish the claimed gcd.

At every 75th root ξ with ξ^5≠1, (2.1) gives K(ξ)=0. Hence

    H(X)=(X^75−1)/(X^5−1)=1+X^5+⋯+X^70 divides K(X).          (2.3)

Since deg K≤74, write K=H C with deg C≤4. Coefficient comparison yields

    k_r = c_(r mod5)  for all r∈Z_75,                           (2.4)

where c_0,…,c_4 are nonnegative integers and Σ c_i=D. Because 0,11,3 belong to P, c_0,c_1,c_3 are positive. Therefore **every one** of the fifteen residues in each of the classes 0,1,3 mod5 is represented in actual P.

For each represented r∈Z_75 define h(r)∈Z_(75R) as the residue mod75R of any P-element congruent r mod75. It is well defined by (1.3), using the same fixed b_0 on both elements. In particular

    h(0)=0,  h(3)=3,  h(11)=11         in Z_(75R).              (2.5)

Whenever represented r,r′ satisfy r′−r≡y−z (mod75), (1.3) applied to p_r+b_y and p_r′+b_z gives the **same-lift edge identity**

    h(r′)−h(r) ≡ b_y−b_z             (mod75R).                (2.6)

All subsequent paths use the same h and the same actual starts b_y; no separately selected quotient factors are combined.

## 3. A 15-step anchor cycle handles every R sharing 3 or 5

For each r≡0 (mod5), both r+1 and r−5 are represented. In (2.6) take the edge r→r+1 from y−z=1−0=1, then r+1→r−5 from y−z=1−7=−6. It follows that

    h(r−5)−h(r) ≡ Δ := 2b_1−b_0−b_7    (mod75R).             (3.1)

Iterating fifteen times returns to r modulo75, so 15Δ≡0 (mod75R), equivalently

    5R | Δ.                                                      (3.2)

Write b_y=y+75a_y. Then

    Δ = −5+75(2a_1−a_0−a_7).

Hence (3.2) forces

    R | −1+15(2a_1−a_0−a_7).                                  (3.3)

This is impossible whenever gcd(R,15)>1. This includes all independently shifted R-blocks when R is divisible by3 or5, and already supplies a direct actual-anchor obstruction in those cases.

## 4. Coprime R: the second anchor cycle closes the remaining case

Now suppose gcd(R,15)=1. Equation (3.2) gives Δ≡0 (modR). Set τ=b_1−b_0 (modR). The two distinct start-pairs realizing the **same** mod75 difference1, namely (1,0) and (14,13), give by (2.6)

    b_1−b_0 ≡ b_14−b_13           (mod75R).                    (4.1)

Likewise the pairs (7,1) and (13,7), both realizing difference6, give

    b_7−b_1 ≡ b_13−b_7           (mod75R).                     (4.2)

Combining (3.2), (4.1), and (4.2) moduloR yields

    b_7≡b_0+2τ,  b_13≡b_0+3τ,  b_14≡b_0+4τ.                  (4.3)

For any r≡0 (mod5), take r→r+1 with difference 1−0, then r+1→r+15 with difference 14−0. The endpoint is again in class0; moduloR its h-value changes by

    (b_1−b_0)+(b_14−b_0) ≡ 5τ.                                (4.4)

Repeating this r→r+15 cycle five times returns to r mod75, so 25τ≡0 (modR). Since gcd(R,5)=1, τ≡0. Thus all five starts b_y are congruent moduloR.

By (3.1), h(r−5)≡h(r) (modR) for every r in class0. Starting from h(0)=0 and moving by5 shows h(10)≡h(15)≡0 (modR). Use the actual class1 anchor through edge 10→11 with y−z=1−0, and the actual class3 anchor through edge 15→3 with y−z=1−13=−12. As the starts are congruent modR,

    h(11)≡0,       h(3)≡0          (modR).

By (2.5), R divides both 11 and3, forcing R=1, contrary to R>1. Together with §3 this proves the theorem for every R>1 and D≥1. ∎

## 5. Nonvacuity and relation to the requested lift

The tail-family restriction is nonempty even with all literal Y-anchors. For arbitrary R,D choose

    b_y = y−75(y modR),
    P₀ = {5j+75Rk : 0≤j<15, 0≤k<D}  (mod n).                  (5.1)

Each y is actually in Q, by choosing t=y modR. Moreover P₀⊕Q=Z_n for **any** choice of the starts: the residues b_y+5j cover Z_75 exactly once because y runs once through each class mod5 and j runs through Z_15; for each such residue, t+Rk runs exactly once through Z_(RD), up to a fixed carry. Thus the proposition is not vacuous. P₀ contains only the head anchor0, not3,8,11; it is not a Shor completion witness.

For R odd and D=2^K, this family falls within the odd-tail common-row setting of the earlier mixed-carry interface: Q projects to Y+75[0,R−1] modulo 75R regardless of its independently chosen starts, and P has |P|=15·2^K. The theorem shows that **no full undilated lift of that projected tail**, of the specific common-length progression form (0.1) and with actual anchors, exists. The proof is stronger than checking a selected scalar gcd pair and does not assume that all tail starts have the same high-bit lift. It does not exclude arbitrary lifts that are not common-length 75-progressions, even at the same n or |P|.

## 6. Exact finite arithmetic controls and caller boundary

The owner used exact Python integers in the eval kernel only:

1. Polynomial long division checked F mod Φ_3 =2X, F mod Φ_5 =0, and the coefficient list of (2.2); the degree comparisons are written in §2.
2. Eighteen nonvacuity controls covered R∈{2,3,5,7,11,33}, D∈{1,2,4}, with starts as in (5.1). For each, the kernel enumerated P₀,Q and all sums, checked |P₀|=15D, |Q|=5R, full direct coverage, inclusion of all five Y-anchors, and P₀∩A={0}. These include both gcd(R,15)>1 and gcd(R,15)=1. They do not prove the all-R,D theorem or provide an anchored completion.
3. The integer differences 1−0=1, 1−7=−6, 14−0=14, and 1−13=−12 are the edge labels used in §§3–4; no selected solver or floating calculation is used.

These are same-owner finite controls, not independent-model-family, human, formal/kernel or novelty verification. A fresh review must check the progression decomposition, cyclotomic gcd, simultaneous h-edges, two cycles and their divisibility directions. No unreviewed predecessor or review result is a premise.

**Original-code caller, conditional:** the Restivo–Salemi–Sportelli actual-word border theorem, as stated in Cordero [arXiv:2301.13566v1, p. 3, Thm 1.1](https://arxiv.org/pdf/2301.13566v1), maps a hypothetical finite UD factor-complete extension of the literal Shor code with actual pure-a order n to its SAME actual head/tail border P⊕Q=Z_n, containing A and Y. Therefore, subject to that named caller, no such extension has its actual tail border of the form (0.1). This conditional corollary does not turn failure of the selected tail family into a global noncompletion theorem. No order floor, general no-go, finite-code witness, or parent adoption is asserted.

**END OF ANCHORED-TAIL PROGRESSION JOINT-LIFT OBSTRUCTION.**
