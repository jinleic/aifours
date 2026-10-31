# f34 — all-eight P7 bridge, finite-simple descent and GL(3,2)

Reviewer **PhysicsPPT44-2**. Actual native clock immediately before creation: **Wed Oct 28 17:37:58 PDT 2026**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR.** The all-eight bridge requires the explicit `Sun7(G)` hypothesis; direct-P7 finite-simple descent does not. Thus the all-groups/finite-nonabelian-simple equivalence is conditional on the **universal** Sun7 statement, which is not proved or independently authenticated here. The GL(3,2) six-coset completion and its Sun8 consequence are independently reconstructed without Sun7, NC7, A7 or Eisenstein imports. No unrestricted Sun8, formal/kernel, human, configured-family, priority or novelty acceptance follows.

## 1. Bound inputs and review boundary

- Complete assignment `f34-sun-global-p7-simple-reduction/assignment-v1.json`: SHA256 `1de3702ae2fd2a3f1e668f38a3355fad9415da749c33a0e3b1d323af5dd182c0`.
- Complete 107-LF `frontier-20261028-global-p7-simple-reduction-v1.md`: SHA256 `a79167480dae75b5962d54a58c9d5fa4f74d96d42ea4d54e98ad531f4c8e1ca7`.
- Complete 115-LF `frontier-20261028-gl32-elementary-nc7-v1.md`: SHA256 `c4aa1c2af01e226a6e7f45947c76e1a21294899162eae2014f97d8db8c6eb3c9`.
- Registered original actual-left-coset definitions and the elementary subgroup/index facts rederived below. I previously reviewed other Sun-coset transfer candidates in this run; this is not blind, independent-family or clean-cognition review. No historical quarantined result or author checker output is a proof premise; no author contact or nested agent was used.

An independently written finite check, its output and limitations are in §8. It supports particular finite incidence and support claims, not the general descent or Sun7.

## 2. Actual two-coset fact and all-eight bridge

`Sun_k(X)` says every k pairwise-disjoint **actual left cosets** of finite-index subgroups of X have a pair of subgroup indices with gcd≥k. If two such cosets have coprime subgroup indices, they must meet: the diagonal map from X/(H∩K) into X/H×X/K is injective, its finite domain size is divisible by both coprime indices and no larger than their product, and hence the map is surjective. This applies to arbitrary groups and nonnormal subgroups.

Assume `Sun7(G)` and an actual eight-coset Sun8 counterconfiguration with indices n_i. Pairwise disjointness and the counterconfiguration give `2≤gcd(n_i,n_j)≤7`. Applying Sun7(G) to each seven-subfamily yields a pair of gcd exactly 7. At least three original indices are divisible by 7: if there were at most two, omit one of them if present (or any label if none), leaving seven labels with at most one such index.

Any two seven-divisible indices have gcd exactly 7. Suppose some actual label j has 7∤n_j. For each seven-label i, choose a prime p_i dividing the nontrivial gcd(n_i,n_j); the bound and 7∤n_j force p_i∈{2,3,5}. Distinct seven-labels cannot use the same p_i, since they share no prime other than 7. There are therefore at most three seven-labels, and exactly three by the preceding paragraph. Their three primes must be 2,3,5, making **every** non-seven index divisible by 30. There are five non-seven labels, so two original indices share 30, contradiction.

Hence every n_i is seven-divisible. Their pairwise gcds are exactly 7, and writing `n_i=7r_i` yields `gcd(r_i,r_j)=1` for all i≠j. This is the actual all-eight P7 bridge, including the possibility that one r_i has a private factor 7. It uses Sun7(G) precisely in the three-seven-label deduction; the subsequent descent below does not use Sun7.

## 3. Finite core and direct-P7 normal-section descent

Call a direct P7 family eight actual disjoint finite-index left cosets with indices 7r_i and pairwise coprime positive r_i. For any such family in any G, intersect the eight cores `core_G(U_i)`. Each is finite-index normal as the kernel of the action on finite G/U_i. Their intersection K is finite-index normal and contained in every U_i. Original cosets are exact inverse images of their image cosets in G/K; disjointness and **all indices** are preserved. Thus any direct P7 family has a finite realization.

Choose a finite direct-P7 group F of **globally least positive group order**. If it has a proper nontrivial normal subgroup N, write for the actual original U_i

`c_i=[N:N∩U_i]`, `d_i=[F/N:NU_i/N]`, `c_i d_i=7r_i`, `C_i=π(g_i)π(U_i)`.

The index product follows from `N/(N∩U_i)≅NU_i/U_i` as coset sets. If C_i,C_j meet, the intersections of the original cosets with a shared quotient fibre translate into disjoint actual N-cosets of indices c_i,c_j. In particular, if both `gcd(d_i,d_j)=1` and `gcd(c_i,c_j)=1`, the quotient cosets meet by §2 and then their actual kernel fibres meet by §2, contradicting original disjointness.

At most one r_i is divisible by 7. If such a label exists designate it e; otherwise choose any e. The other **seven regular labels** have r_i prime to 7. For each regular label the sole factor 7 in c_i d_i lies entirely on exactly one side. Two regular labels cannot choose opposite sides: their r-indices are coprime, so opposite placements would make both their c-indices coprime and their d-indices coprime, forbidden by the preceding two-stage actual-coset argument. Therefore all seven regular labels place 7 on the same side.

### 3.1 Seven on the quotient side

The seven regular c_i are seven-free. Any pair of the eight c_i contains a regular label; a common divisor cannot be 7 and cannot come from both pairwise-coprime private r-indices. Thus **all eight c_i are pairwise coprime**, including c_e even if r_e contains additional factors of 7.

If any two actual quotient cosets C_i,C_j met, their disjoint kernel fibres would have coprime indices, impossible. Hence all eight C_i are pairwise disjoint. If d_e were seven-free, it would be coprime to every regular d_i, since the private r-indices are pairwise coprime; the two quotient cosets would then meet, contradiction. Thus every d_i is divisible by 7. Writing `d_i=7s_i` gives `s_i|r_i`, so the s_i remain pairwise coprime. The strictly smaller quotient F/N carries an actual direct P7 family, contradicting least order.

### 3.2 Seven on the kernel side

The seven regular d_i are seven-free. By the same private-factor argument, all eight d_i are pairwise coprime, including d_e. The multi-coset diagonal map from `(F/N)/(∩π(U_i))` into the product of the eight quotient coset spaces is injective. Its index is divisible by the pairwise-coprime d_i and bounded by their product; it is therefore onto. The **same eight actual quotient cosets** share a single point.

Their fibres in that point translate to eight pairwise-disjoint actual N-cosets of indices c_i. If c_e were seven-free it would be coprime to every regular c_i, so its fibre would meet one, contradiction. Thus every c_i is divisible by 7, and `c_i=7s_i` with `s_i|r_i`; the s_i are pairwise coprime. The proper subgroup N is strictly smaller and carries a direct P7 family, contradiction.

The two placements exhaust the seven regular labels. F has no proper nontrivial normal subgroup, so it is finite simple. A finite abelian simple group is cyclic of prime order: for p≠7 it has no seven-divisible subgroup index, and for p=7 it has only seven elements and cannot contain eight disjoint nonempty cosets. Thus F is nonabelian simple. This direct-P7 descent is independent of Sun7 and does not use a numerical-support program.

Under the separate **universal** Sun7 import, any arbitrary-group Sun8 counterconfiguration is direct P7 by §2 and hence yields a finite nonabelian simple direct P7 counterconfiguration by §3. Therefore Sun8 for all finite nonabelian simple groups implies Sun8 for all groups; the reverse implication is immediate. This does not show that any simple group violates or satisfies Sun8 generally, and the earlier source-status/priority of this reduction is not determined here.

## 4. GL(3,2): elementary group and subgroup analysis

Let V=F₂³ and G=GL(V). Counting ordered bases gives `|G|=7·6·4=168`. G acts transitively on its seven nonzero vectors and on its seven planes; over F₂ each plane is the kernel of a unique nonzero covector. Point and plane stabilizers have order 24 and index 7.

Elementary transvections generate G by Gaussian elimination; the only nonzero scalar is 1, and a row swap is a product of row additions. For distinct i,j,k, direct multiplication gives `[I+E_ik,I+E_kj]=I+E_ij`, so all generators are commutators and G is perfect.

Every finite group J of order dividing 24 is solvable. If 3∤|J| it is a 2-group, hence solvable by the centre/class-equation induction. Otherwise a Sylow-3 subgroup has count 1 or 4. Count 1 makes it normal with 2-group quotient. Count 4 gives a conjugation action into solvable S4, and its kernel lies in a Sylow-3 normalizer of order `|J|/4≤6`, hence is solvable; the kernel/image extension is solvable. S4 is solvable via `1<V4<A4<S4`, and groups of order dividing 6 are solvable.

If H<G had index d in {2,…,6}, the coset action image would be a quotient of perfect G of order dividing both 168 and d!, hence dividing 24. It would be solvable and perfect, so trivial, contrary to transitivity on d>1 cosets. Thus no subgroup has index 2,…,6.

Now let H have index 7, so |H|=24, and act on the seven nonzero vectors. If H fixes a nonzero vector, equal order makes it that point's full stabilizer. Otherwise it cannot have an orbit {u,v} of size 2, since u+v≠0 would be fixed. Its allowed orbit sizes are then 3,4,6 and must sum to 7, so the decomposition is 3+4. The sum of the 3-orbit is fixed, hence zero. Its three nonzero vectors are exactly the nonzero points of a plane, which H stabilizes; equal order makes H that full plane stabilizer.

A point stabilizer is transitive on the other six nonzero vectors by basis extension. Any plane contains either two or three of those six, so no point stabilizer fixes a plane. Hence the seven point stabilizers and seven plane stabilizers are distinct and exhaust all index-seven subgroups.

## 5. Actual point/covector coset incidence and six-set completion

For nonzero vectors p,a let `P(p,a)={T∈G:T p=a}`; this is an actual left coset of Stab(p). For nonzero covectors α,β let `L(α,β)={T∈G:αT=β}`; choosing T₀ with αT₀=β shows this is `T₀ Stab(β)`, an actual left coset. These 49+49 labelled cosets comprise all index-seven cosets.

Basis extension gives the exact pair rules. Two distinct P labels are disjoint iff they have the same p and different a, or different p and the same a; the L labels obey the identical same-coordinate rule. A mixed P(p,a),L(α,β) pair intersects iff `β(p)=α(a)`: equality is necessary by evaluation, and sufficient by mapping ker β isomorphically to ker α, mapping p to a inside those kernels when the value is 0, or mapping p to a as the chosen complements when it is 1.

For nonempty sets A of m nonzero vectors and B of n nonzero covectors, if every β(a) has one common value e, the following elementary bound holds. For e=0, one vector has three nonzero annihilators; two independent vectors have only one nonzero common annihilator, whose plane has three nonzero vectors, so m+n≤4. For e=1, if m,n≥2 then independence gives m,n≤2; if m=1 then n≤4 and if n=1 then m≤4. Thus m+n≤5 in all e=1 cases.

In a same-type disjoint family of at least two cosets, all labels share one coordinate: after two labels sharing a source, a third with another source would have to match two distinct targets at once to be disjoint from both; the common-target and covector cases are identical. A singleton can be assigned either mode.

Take six disjoint index-seven cosets, m point and n covector. If one type is absent, the six same-type labels share one coordinate; the missing seventh value supplies a disjoint coset. If both types are present and the modes are matched, either all point sources and covector first labels are fixed, or all point targets and covector second labels are fixed. Mixed disjointness forces constant opposite F₂ incidence values. The allowed nonzero labels have capacities 3 and 4, in one order or the other. Because m+n=6, at least one allowable label is unused, yielding an actual seventh coset of the same orientation. In the two crossed-mode cases, all relevant pair incidences have one constant value, so the preceding Fano bound gives m+n≤5, impossible. Singleton mode choices are included in this dichotomy.

Each index-seven coset has 24 elements. Six initial disjoint cosets plus the seventh give 7·24=168 elements, exactly G; the seventh is the **exact complement**. This proves the full six-completion statement, not merely existence of an unrelated index-seven coset.

## 6. Sun8(GL(3,2)) without Sun7

Suppose eight actual disjoint cosets have all original index gcds≤7. Their indices divide 168, and none is 1 because that coset is all G. By §4 none lies in 2,…,6.

If no index were 7, every non-seven-divisible index would lie in {8,12,24}. At most two can occur: repetitions of 8 or 12 and any pair involving 24 have gcd≥8. Every seven-divisible index has the form 7d with d>1 dividing 24. Pairwise gcd≤7 forces those d to be pairwise coprime. Since their only prime factors are 2,3, at most two such indices can occur. This permits at most four labels, not eight. Thus some coset has index 7.

Any other actual disjoint coset must have index gcd≥2 with 7 by §2, so all eight indices are `7d_i`. Pairwise gcd≤7 makes the d_i pairwise coprime, and they divide 24. At most two d_i can exceed 1; therefore at least six original cosets have index 7.

Their exact complement is an actual index-seven coset xH by §5. The remaining two nonempty original cosets lie inside xH. Choose representatives y_i inside each. Because y_iH=xH and y_iU_i⊆y_iH, each U_i≤H. Translating into H yields two actual disjoint H-cosets of indices `[H:U_i]=d_i`. These indices are coprime, contradicting §2. Thus Sun8(G) holds with no Sun7 or earlier NC7 import. The argument is for this concrete GL(3,2), not an unproved transport to other presentations.

## 7. Independent exact finite checks

I wrote `frontier-20261028-review-f34-gl32-and-p7-check.py`, SHA256 `389c5da2ea7e40c91377a66965bd89639ef6b1869401454e7546ab306ffa6e2d`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f34-gl32-and-p7-check.py`.

It independently generates all invertible F₂³ matrices as ordered bases, multiplies them exactly, enumerates finite generated subgroups by closure, checks subgroup multiplication closure and each actual left-coset partition, and compares the 98 point/covector-labelled sets to **all** actual index-seven cosets. It verifies every one of the 4,753 pair-incidence relations and exhaustively checks every disjoint unordered six-set and its actual set complement. Observed output:

```text
GL(3,2) order=168; subgroups=179; actual left cosets=6746;
subgroup indices {1:1,7:14,8:8,14:14,21:21,24:8,28:28,42:35,56:28,84:21,168:1}
index-seven cosets=98; pair relations checked=4753;
six disjoint unordered cosets=1568; exact-complement multiplicity {1:1568};
six-set counts by number of point-type cosets {0:98,2:294,3:784,4:294,6:98}.
```

The code uses neither author enumerator nor author incidence program. Subgroup generation is exhaustive because every finite subgroup has a finite generating set and adjoining each possible element inductively reaches it; generated subsets are separately closure checked. These computations reproduce the concrete numerical claims but do not replace the elementary proof or constitute a general simple-group result.

The same independent program enumerates nonempty squarefree supports on {2,3,5,7}, unordered with repetition, preserving necessary pair gcd between 2 and 7. Its output was:

```text
prefix_counts=[1,15,61,102,119,139,161,183,205]
eight_supports_with_at_least_three_sevens=15
such_supports_with_a_nonseven=0
```

For an actual counterconfiguration, a common prime cannot exceed 7, and truncating valuations retains every nontrivial common prime while the truncated gcd divides the original gcd. Hence this is an overapproximation of the arithmetic support problem, not an actual coset construction, a proof of Sun7, or a verification of the normal-section descent. The written proof in §§2–3 stands independently of this check.

## 8. Exact disposition and limits

| Claim | Disposition |
| --- | --- |
| All-eight seven-saturation | NO_SUBSTANTIVE_DEFECT conditional on Sun7(G), for every actual counterconfiguration |
| Direct-P7 finite-core and least-order simple descent | NO_SUBSTANTIVE_DEFECT without Sun7; both placements and private-seven owner paid |
| All groups iff finite nonabelian simple groups | NO_SUBSTANTIVE_DEFECT conditional on universal Sun7, with no claim that the simple cases are settled |
| GL(3,2) exact six-coset complement | NO_SUBSTANTIVE_DEFECT from the stated elementary subgroup and incidence argument |
| Sun8(GL(3,2)) | NO_SUBSTANTIVE_DEFECT without Sun7/NC7 imports, for this presentation only |

No mathematical gap requiring a counterexample to the claims above was found. The exact all-group Sun7 statement remains an explicit unproved import in this review; historical written-composition acceptance is not a primary-source, human or kernel certificate. No source/book equivalence, novelty, classification of finite simple groups, numerical finite cutoff or unconditional unrestricted Sun8 solution follows. Parent must read both complete candidates and this return before adoption; prior quarantine outcomes remain historical and are not retrospectively validated.
