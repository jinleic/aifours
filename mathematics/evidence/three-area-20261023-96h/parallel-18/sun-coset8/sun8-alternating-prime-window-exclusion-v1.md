# Sun8 — actual Sylow-support prime forcing in alternating/symmetric prime-window degrees

Owner MathSun8-2. Actual preceding `/bin/date`: **Sun Oct 25 16:54:07 PDT 2026**. **NEW COMPLETE WRITTEN CANDIDATE AT NAMED CLASSICAL INPUTS; NOT ACCEPTED.** This is an unbounded whole-group-family exclusion of the ORIGINAL eight-coset target, not a bounded subgroup survey, guessed arithmetic index list, eight-coset witness or full Sun8 theorem. No scientific interpreter/Eval/calculator/program/CAS/enumeration/symbolic/solver/replay/CLI/nested agent/newGO.

## 1. Exact original theorem and classical boundary

Assume an integer n has an ODD PRIME divisor p>7 and there is a prime q satisfying

n−p<q≤n.                                                     (WINDOW)

Since n is a nontrivial multiple of p, require n≥2p. Let G=A_n OR G=S_n in its ACTUAL natural n-point action. The claim is:

> **PRIME-WINDOW SUN8:** every EIGHT pairwise-disjoint LEFT cosets of arbitrary subgroups of G have some pair of subgroup indices with gcd AT LEAST8.

There is NO assumption that the indices are7r_i, that cofactors are prime/small/square-free, that subgroups are maximal/natural set stabilizers, that G has minimum order, or that any original subgroup normalizes another. The proof retains ALL original groups/cosets; it uses their actual indices/containment, not a converse from an index list.

**Unbounded corollary:** for EVERY prime p>7, the original Sun8 assertion holds for A_(2p) and S_(2p), at the named classical theorem boundary. Bertrand supplies a prime q with p<q<2p, exactly(WINDOW) at n2p. This is an INFINITE family, but not all alternating/symmetric degrees or all simple groups.

Declared classical inputs:

- **JORDAN-PRIME:** a primitive permutation group of degree n containing a SINGLE cycle of prime length p fixing at least three points contains A_n. Exact statement actually read as Theorem1.1 of Gareth A. Jones, [Primitive permutation groups containing a cycle, arXiv1209.5169v1](https://arxiv.org/html/1209.5169v1). The source identifies Jordan1871/1873/Dixon–Mortimer3.3E/Wielandt13.9 ancestry. This is a NAMED UNREPROVED CLASSICAL input, not a new formal proof. The separate nonprime-cycle/CFSG Theorem1.2 is NOT used.
- **BERTRAND**, used ONLY for the n2p corollary: for every integer u>1 there is a prime q with u<q<2u. This is a NAMED UNREPROVED CLASSICAL prime theorem, not a new prime search or self-contained prime-interval certification. The general(WINDOW) theorem needs only the supplied actual p/q conditions, not Bertrand/PNT.
- Ordinary Sylow conjugacy/containment, group index/order divisibility, orbits, blocks and factorial orders; all new load-bearing containment/cycle arguments are written below.

`sun8-prime-window-classical-inputs-v1.txt` freezes the exact bounded source excerpt and access qualifications. The original Erdős1932 PDF returned403; the accessible full Galvin note was actually read but its Mathematica-mentioned estimates were NOT replayed or credited. No publication-byte identity, independent reproof of Jordan/Bertrand, configured-family or novelty clearance is claimed. There is NO Sun7/R8, normal-section, NC7, rank-four, pending125/99, classical coprime-index-simple-group or CFSG correctness import in this proof.

## 2. Actual Sylow support for an index prime to p

Let H≤G have index prime to p. Then the p-part of |H| equals that of |G|, so H contains a Sylow p-subgroup P of G. This is an ACTUAL subgroup of H, not deletion of p from an index or a presumed quotient.

Because p is ODD, every p-subgroup of S_n is contained in A_n (its sign map to C2 is trivial). Thus the Sylow p-subgroups for A_n/S_n have the same order/action. Such a P has NO fixed points when p|n:

Let f be its number of fixed points. All other orbit sizes are positive powers of p, so f≡n≡0 modulo p. If f≥p, a p-cycle supported on p of its fixed points is an EVEN permutation, lies in G, commutes with P and is not in P. It generates with P a strictly larger p-subgroup, contradicting Sylow maximality. Hence0≤f<p and f≡0, giving f0. Every P-orbit therefore has size at least p and is a multiple of p.

Also P contains a SINGLE p-cycle. A p-cycle lies in G because p is odd, and is contained in some Sylow p-subgroup. Sylow conjugacy in G carries that Sylow to P and carries the cycle into P. It is not merely a product of cycles with no isolated p-cycle. This is where the exact natural permutation action matters.

## 3. ONE global q forces the index of EVERY nonexceptional p-free subgroup

Take the SAME q from(WINDOW) for every H. Since p≤n/2, q>n−p≥n/2. In particular q>7, q is ODD, and q divides |S_n| and |A_n|. We show that if [G:H] is p-free and H does NOT contain A_n, then q divides [G:H]. Exhaust the ACTUAL natural action of H.

**Intransitive H:** each H-orbit is a union of P-orbits, since P≤H. It has size a positive multiple of p. With at least two such orbits, every size is≤n−p<q. H lies in the product of their symmetric orbit stabilizers. Their factorial orders have NO factor q, hence q∤|H| and q|[G:H]. No orbit is replaced by a symbolic cell or independently chosen partition.

**Transitive imprimitive H:** an actual proper block system has a blocks of b points with ab=n and a,b≥2. Its set stabilizer is a subgroup of S_b wreath S_a, of order(b!)^a a!. Both a,b≤n/2<q. Therefore q does not divide that order or |H|, and again q divides [G:H]. This argument covers EVERY block size/count; no classification of maximal imprimitive subgroups is presumed.

**Primitive H:** §2 gives a SINGLE p-cycle fixing n−p≥p>7 points, in particular at least three. JORDAN-PRIME forces H≥A_n, contrary to the nonexceptional hypothesis. This branch is impossible. We do not substitute an imprimitive version of Jordan or invoke the source's stronger CFSG theorem.

The three cases exhaust all H. Thus, for the ONE fixed p/q pair,

p∤[G:H] and H not containing A_n  ==>  q|[G:H].              (FORCE)

For G=A_n every proper H is nonexceptional. For G=S_n the only proper exceptional H is A_n itself, of index2. The full group has index1 but cannot appear in a family of two or more disjoint nonempty cosets.

## 4. Full original eight-coset contradiction — NO Sun7 reduction

Suppose the original target fails for EIGHT disjoint cosets g_lU_l: every pair of ACTUAL subgroup indices has gcd≤7. All U_l are proper, because a full-group coset would meet every other nonempty coset.

Since p>7, at most ONE index is divisible by p. At least SEVEN original U_l therefore have p-free indices. In A_n all seven satisfy(FORCE), so their indices all contain the SAME q>7. Two of them already contradict the assumed pairwise gcd≤7.

In S_n at most ONE of the eight original cosets can be an A_n coset. There are only TWO such cosets; if two occurred they would exhaust S_n and leave no room for the other six nonempty disjoint cosets. Thus at least SIX of the at least seven p-free sources are nonexceptional and satisfy(FORCE). Again two actual indices share the SAME q>7, contradiction.

This proves PRIME-WINDOW SUN8 at JORDAN-PRIME. Bertrand then proves the complete all-primes p>7 n2p corollary. The proof is DIRECTLY for the original gcd-at-least8 assertion; it does NOT first presume P7 or consume the unauthenticated global Sun7 reduction. Consequently it also excludes actual P7 in those groups, with arbitrary full private cofactors, as a weaker corollary.

## 5. Boundary controls and an actual one-source local geometry

The hypotheses cannot be erased by this proof: p7 would not imply that at most one original index contains p under the gcd≤7 assumption; p2 would change the sign/Sylow argument; n=p would leave no fixed points for the p-cycle and is outside Jordan's stated hypothesis. If no prime q lies in the stated last-p window, no q-forcing conclusion is claimed. A locally chosen q depending on H would also NOT prove the contradiction; one q was chosen GLOBALLY before all subgroup cases.

There is a useful exact control connecting this new global representation to the remaining one-alpha6 barrier. It is NOT an eight-coset witness. Take G=A_77, selected U the point1 stabilizer, and W the set stabilizer of S={2,...,12}. Both are actual subgroups. Their indices are

[G:U]=77=7*11,
[G:W]=binomial(77,11)=7*binomial(76,10).

The private factors11 and binomial(76,10) are coprime. In the exact polynomial ring modulo11,
(1+x)^76=(1+x)^(6*11+10) ≡ (1+x^11)^6(1+x)^10;
coefficient x^10 is1, so binomial(76,10)≡1 mod11. No huge integer or interpreter evaluation is needed.

W is transitive on S and its66-point complement (even permutations within each part already supply transitivity), so [W:W∩U]=66=6*11. Let g=(1,13,2), an EVEN3-cycle. It sends S to{1,3,...,12}. Every element of gW sends1 into(gS)^c, which excludes1; hence gW is DISJOINT from U. This is an actual TWO-coset/source example with gcd of indices7 and ONE6t source at M=U,t11, not a local index-pattern fiction.

The natural A_77 action is two-transitive, so it has no nontrivial seven-block partition of77 points. Thus ONE source alone cannot justify the canonical seven-block step without additional original-family data. This control does NOT refute a future full-eight-coset one-source exclusion: these two cosets do not extend to a Sun8 counterexample by §4. Indeed n77,p11,q73 satisfy(WINDOW);73 is prime because no prime2,3,5,7 divides it and its square-root is<9. The new global Sylow-support theorem excludes ALL eight-coset counterexamples in A_77, not just this local pair. No eight-coset certificate, small-group enumeration or stronger witness gate is asserted.

## 6. Contribution ceiling and exact remaining original task

What is delivered: a COMPLETE original-group subgroup/coset exclusion for the prime-window degree family, and in particular ALL A_(2p)/S_(2p) for prime p>7, at the explicitly named classical Jordan/Bertrand boundary. The seven/eight original subgroups remain arbitrary; no maximal subgroup, natural set-stabilizer or normalizer assumption was inserted into the theorem. The local control is actual group geometry, not a conjecture counterexample. This may be standard/previously known; novelty/priority/SOTA clearance is UNPERFORMED/UNCLEAR and no independent discovery count is claimed.

What remains: ALL other alternating/symmetric degrees not satisfying the predicate, other finite nonabelian simple families, arbitrary infinite groups, the actual mixed-alpha<=1 original-source/maximal/nonabelian/odd/private-composite P7 frontier, and the full arbitrary-group Sun8 theorem. Nothing forces a prime-window divisor in every possible degree/group, and nothing upgrades the separate global Sun7/finite-core/R8 ancestry. The new family theorem alone cannot be silently substituted for the full target.

The classical source statements are named UNREPROVED inputs; their original proof DAG and any published computational estimates are NOT newly replayed or certified. All new Sylow/fixedpoint/orbit/block/index/actual-coset arguments above are WRITTEN, not formal/kernel/human/configured-family/executable verification. All frozen125/99/63/136/217/58 and M1/process histories are unchanged. Same original18owners/root/fulltarget/cutoff/deadline and v9/v10/v11/HOLD. No scientific execution, publication/contact, Git/deletion/config/shared-root writes, nested agent or GO; primary continues at the exact original residual, not a bounded-survey substitute or round closeout.
