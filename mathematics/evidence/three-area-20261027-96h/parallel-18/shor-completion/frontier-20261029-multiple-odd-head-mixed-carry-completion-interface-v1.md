# Multiple odd head primes: an exact mixed-carry border and completion interface

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 14:12:10 PDT 2026**.

**WRITTEN UNREVIEWED INTERFACE, with finite integer controls.** This is a new all-variable representation of the actual border and actual finite-code requirements; it is not an obstruction for the full multiple-prime family, a completion, a formal proof, an independent-model-family review, or novelty clearance. No scalar or arc-consistency search verdict is used. The unrestricted Shor problem remains OPEN.

## 0. Original target and input boundaries

Let A={0,3,8,11}, Y={0,1,7,13,14}. An anchored cyclic border consists of P,Q⊆Z_n, A⊆P, Y⊆Q and P⊕Q=Z_n. The literal Shor code is

    S=b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2}.

Main asked for a genuine multiple-distinct-odd-head-prime residual beyond the head-15 scalar rectangle, seeking an all-variable obstruction or an actual completion interface. Section 2 gives **exact equations for all 2-adic allocations and all odd head parts**. Section 3 specializes them to a genuine, explicitly labelled odd-tail branch, including the head-15 case. Section 4 adds exact finite tests for the **same actual code D**, including arbitrary multi-b atoms. Neither branch is silently taken as the whole problem.

The code-to-border caller is the Restivo–Salemi–Sportelli actual-word border theorem, as stated in Cordero [arXiv:2301.13566v1, p. 3, Thm 1.1](https://arxiv.org/pdf/2301.13566v1). Its application is a named conditional import; a cyclic border by itself is not a completion. Elementary dilation/equal-gcd exclusion are reconstructed in §3. The only additional input used in §3.3 is explicitly named Łaba–Londner Corollary 6.2/T2. The exact mixed-carry equations and finite-code tests use no T2.

The owner has seen earlier same-author fibre/cofactor and head-15 work, including the scalar-rectangle obstruction `2a62c990…`. This is not blind or disjoint-exposure work. No earlier unreviewed/adopted theorem, fixed-order candidate, Q55/fibre result, solver output, or HELD/ZERO/NONINPUT body is a premise. Previous process/arithmetic/cadence disclosures and every historical quarantine remain in force.

## 1. Exact same-P/Q mixed-carry coordinates for arbitrary odd or even Q

Let n=D·M, D=2^K with K≥1, M odd. Throughout §§1–3, D denotes this binary scale, not a code. We use exactly the actual P,Q, not independently selected factors. For s∈{0,…,D−1} define

    U_s = {u mod M : s+D u∈P}.                                  (1.1)

For θ∈Z_M define a **set**, not necessarily a singleton,

    Λ(θ) = {λ mod D : CRT_n(λ,θ)∈Q}.                           (1.2)

CRT_n(λ,θ) is the unique residue mod n with those components. Thus P and Q are recovered exactly from the U_s and Λ(θ), and

    |P|=Σ_s|U_s|,         |Q|=Σ_(θ mod M)|Λ(θ)|.               (1.3)

The actual anchors give, for each a∈A and y∈Y,

    floor(a/D) mod M ∈ U_(a mod D),
    y mod D ∈ Λ(y mod M).                                       (1.4)

For r∈Z_D and a pair (θ,λ) with λ∈Λ(θ), put

    s_r(λ)=(r−λ) mod D,
    κ_r(θ,λ)=D^(−1)(θ+s_r(λ)−r) mod M.                          (1.5)

The inverse exists because M is odd. For a set U⊆Z_M write U(X)=Σ_(u∈U)X^u, with representatives 0,…,M−1, and write G_M(X)=1+X+⋯+X^(M−1).

> **Mixed-carry interface.** P⊕Q=Z_n holds **if and only if**, for every r∈Z_D,
>
>     Σ_(θ mod M) Σ_(λ∈Λ(θ)) X^(κ_r(θ,λ)) U_(s_r(λ))(X)
>          ≡ G_M(X)   (mod X^M−1).                              (1.6)

*Proof.* Fix target x=r+D z, with r mod D and z mod M. For q=CRT_n(λ,θ), the head row is forced to be s=(r−λ) mod D. Since s+q−r is divisible by D, the head p=s+D u satisfies p+q=x precisely when

    z ≡ u+(s+q−r)/D ≡ u+D^(−1)(θ+s−r) mod M.

Every actual q is accounted for exactly once by (θ,λ), including multiple lifts of the same θ. Therefore the coefficient of X^z on the left of (1.6) is exactly the **number** of actual representations of x. Equality to G_M for all r is exactly uniqueness and coverage of the same actual P,Q. ∎

This is a joint high-modulus constraint, not independent scalar checks of head differences or a claim that a factorization constructs a code. It is valid for even Q as well as odd Q, for any number of odd head primes, and for arbitrary 2-adic allocation. A mathematical use may take its Fourier transform, but must preserve all simultaneous U_s, Λ and carries; replacing them by unrelated feasible witnesses for each r is invalid.

## 2. Anchored rows and the multiple-prime cardinality

Suppose the actual head cardinality is |P|=d·2^a with d odd and at least two distinct odd prime divisors. Since n=D M, write

    Σ_s|U_s|=d·2^a,    Σ_θ|Λ(θ)| = n/(d·2^a).                (2.1)

Both odd-tail and even-tail cases remain in (1.6); no factor is assumed split. In particular, for the smallest example d=15, the actual primes 3 and5 must both divide |Q| by the anchored dilation/equal-gcd argument below, so those prime directions are **shared**. The user-specified A and Y are carried literally by (1.4).

At any fixed n and cardinalities, (1.3)–(1.6) are finite, exact, simultaneous equations. They decide the anchored **cyclic border** condition for the displayed U,Λ, not unrestricted Shor completion. The twofold quotient and opposite-corners examples previously studied merely satisfy relaxations; they do not satisfy (1.6) unless directly demonstrated.

## 3. An odd-tail structural branch: common 15-point fibres, not a completed lift

Assume additionally that |Q| is odd and |P|=d·2^a with d odd. Then K=a, because |P||Q|=2^K M. We reconstruct the elementary multiplier fact used below: if X⊕Z=Z_n and gcd(t,|X|)=1, then tX⊕Z=Z_n. For a prime ℓ∤|X|, the group algebra F_ℓ[Z_n] gives X^ℓZ=|X|^(ℓ−1)G=G; nonnegative integer coefficients are all 1 modℓ and sum to n, hence all equal1. Iterate over prime factors. Equal-gcd exclusion follows by CRT-lifting a unit between differences with the same gcd and applying the same dilation.

### 3.1 K≥4 and a common odd quotient

Because |Q| is odd, DQ⊕P=Z_n by dilation. Scaling is injective on Q. If K≤3, the head difference 8 and the scaled tail difference D·1 have common gcd D with n, contradicting equal-gcd exclusion. Hence K≥4 and D≥16.

Projection Q→Z_M is injective: if q≡q′ modM, then Dq≡Dq′ modn, so dilation injectivity gives q=q′. Put T=Q modM, an actual set of size |Q|. Since M≥|P||Q|/D=d|Q|, and the anchored odd-tail case below has d=15 and 3,5,11 dividing |Q|, M≥2475; hence Y⊆T literally, without residue collisions.

Restrict DQ⊕P to each row s modD and divide the row by D. It gives

    U_s ⊕ T = Z_M,       |U_s|=d             for EVERY s∈Z_D.   (3.1)

The four actual head anchors have s=a and normalized u=0 because D≥16, so

    0∈U_0∩U_3∩U_8∩U_11.                                      (3.2)

Also Λ(θ) is now a singleton for θ∈T and empty otherwise; let its single value be λ(θ). The actual Q-anchors give λ(y)=y modD for y∈Y.

For the particular smallest residual d=15, the anchored difference argument forces 3,5,11|Q, so M is divisible by 3²5²11. Both 3 and5 are shared; they are **not** assumed coprime/split.

### 3.2 The simultaneous lift equation is still indispensable

Equation (3.1) is a consequence of **P⊕DQ**, not an automatic proof of P⊕Q. With the singleton λ, the real lift condition is the all-r equation

    Σ_(θ∈T) X^[D^(−1)(θ+s_r(λ(θ))−r)]
                 U_(s_r(λ(θ)))(X) ≡ G_M(X)   (mod X^M−1).    (3.3)

Unlike (3.1), (3.3) mixes head rows according to the *same* tail lift λ and includes the carry. This is the first exact cyclic-border step that must be solved or contradicted after all common-complement rows are known. It remains unproved in general.

A concrete failure of the naive replacement "every row tiles with T, so the actual lift tiles" is immediate. Take

    D=16, M=2475, n=39600,
    U={5j:0≤j<15},
    T={y+75t:y∈Y, 0≤t<33} ⊆ Z_2475,
    U_s=U for all s,
    Q=T with its representatives in [0,2475),
    P={s+16u:0≤s<16, u∈U}.

The set Y has all five residues mod5. For any z mod2475, its mod5 residue determines y; then (z−y)/5 mod15 determines j; finally the remaining multiple of75 determines t mod33. Thus U⊕T=Z_2475, so all sixteen row identities (3.1) hold and P⊕16Q=Z_39600. The full cardinalities are |P|=240=15·16, |Q|=165 odd; A⊆P,Y⊆Q, and (3.2) holds. But **P⊕Q fails**: 0+1=1+0, with 0,1 in both P and Q. For r=1, the θ=1 and θ=0 terms in (3.3) both contribute to the coefficient of X^0. This example is deliberately not an anchored tiling; it violates a basic scalar condition as well as the full mixed-carry equation. Its purpose is to demonstrate that the whole-row/common-complement interface is not itself a lift certificate.

### 3.3 Same prime-power spectrum across all actual rows for d=15

For the odd-tail d=15 branch, each U_s has 15 elements and tiles Z_M with the **same** T. Let ν_ℓ(M) be the exponent of a prime ℓ in M. For every ℓ^j|M, the cyclic tiling identity forces Φ_(ℓ^j) to divide U_s(X) or T(X). A monic Φ_(ℓ^j) has value ℓ at 1. Counting ℓ-adic valuations of |U_s||T|=M shows that every such factor is owned by **exactly one** of the two masks and that exactly ν_ℓ(15) of them belong to U_s. Because T is the same for every row, the owned indices are the same for every s.

In particular there are fixed u,v≥1, independent of s, such that every U_s owns Φ_(3^u) and Φ_(5^v), and no other 3- or 5-power cyclotomic. The named Łaba–Londner Corollary 6.2 applies to each row tiling: |U_s|=15 has only two prime divisors 3 and5, so at most those two can be shared with |T|. Its (T2) conclusion gives

    Φ_(3^u·5^v) | U_s(X)        for every s∈Z_D.               (3.4)

The quotient/root statements have the same conditional import scope for every row. For example Φ_(3^u)|U_s means that after folding mod 3^u, each residue class mod 3^(u−1) has equal counts in its three top-digit lifts; the corresponding five-lift equality holds at 5^v. In the four anchor rows of (3.2), the normalized residue 0 is actually present, so its three and five digit lifts must be represented. This does **not** assert that the two digit constraints combine into a rectangular 15-point grid, or that an independently chosen row complement is realizable by one finite D.

## 4. Exact finite completion test for the same actual D

The mixed-carry equation is still only a border interface. The following exact tests preserve the original finite-code target, including arbitrarily many-b atoms. They are elementary finite constructions, not a bounded search result or a promise of feasible runtime.

Let n,L be fixed positive integers, with L≥max(n,15). In §4 only, D denotes a finite set of nonempty codewords over {a,b} of length at most L, containing S and a^n; it is not the binary scale D=2^K of §§1–3. Whenever (1.4)–(1.6) are invoked, their D still means 2^K. Derive P,Q **from this same code D** by

    P={i mod n:a^i b^k∈D,k≥1},
    Q={j mod n:b^l a^j∈D,l≥1}.                                (4.1)

The following two tests exactly decide unique decipherability and factor-completeness of D.

**UD test (finite suffix recursion).** For languages B,C set B^(−1)C={v:∃u∈B, uv∈C}. Put

    U₁=(D^(−1)D)\{ε},       U_(j+1)=D^(−1)U_j ∪ U_j^(−1)D.

Reject if ε appears; accept if a state U_j becomes empty or repeats without ε. The states consist only of suffixes of codewords, so there are finitely many. The reason is direct: U₁ lists the nonempty residuals after two distinct first atoms, and each recurrence removes the next shorter prefix from two competing atom-list concatenations. Reaching ε gives two different atom lists for one word; conversely cancel common initial atoms in any ambiguous pair and follow its successive residuals to ε. Repetition without ε precludes a later new residual.

**Factor-completeness test (flower-graph subsets).** Make a directed labelled graph with a hub and one separate internal path for each word d∈D, spelling d from the hub back to the hub. Every vertex is both initial and accepting. For a subset V of vertices and letter c∈{a,b}, let δ(V,c) be the union of all c-successors; start with V equal to **all** vertices. Explore reachable subsets. Reject if ∅ is reached; accept if the finite subset graph is exhausted without ∅.

Every path in the flower graph is a factor of some D* word, since its initial vertex is reachable from the hub and its terminal vertex can reach the hub. Conversely every factor of a D* word labels a path. A word is therefore a factor of D* iff its reachable subset is nonempty. Thus ∅ is reachable exactly when factor-completeness fails. This checks **all** words through a finite graph; no fixed length cutoff is imposed on the missing factor.

The exact actual-completion interface at fixed n,L is: require the two tests to accept, require S∪{a^n}⊆D, derive P,Q from (4.1), and use (1.4)–(1.6) with the *same* projections. With the named actual-border theorem, every real finite completion with n>14 and n,L in this search lies in this interface. Such an n must be even: if n were odd, the actual P-difference 8 and Q-difference 1 would have common gcd 1, violating the equal-gcd exclusion reconstructed in §3. Thus the decomposition n=2^K M with K≥1 required by §1 applies. Conversely, if the two tests accept, D itself is a finite UD factor-complete extension, not merely a border; the extra equations cannot create a false completion. No bound on n or L is supplied here, so this is not an all-order decision algorithm or a solved existence question.

For a head-15, odd-Q specialization, also require |P|=15·2^K, |Q| odd and (3.1)–(3.4). An even-Q or different multiple-prime branch stays governed by the **unrestricted** mixed system (1.6) and the same full-code tests, not by those odd-tail extra conditions.

## 5. Exact finite controls and remaining mathematical gap

The owner used only Python integers, set operations and finite queues in the eval kernel. The following controls were actually observed:

- The explicit n=39600 common-complement model in §3 has 240 heads, 165 tails, both literal anchor sets and complete P⊕16Q coverage. A direct check found that the undilated sum covers 3100 of 39600 residues; the displayed collision 0+1=1+0 proves nonuniqueness without trusting that count. The exploratory cell intentionally stopped on the first collision by raising `StopIteration`; the environment reported the corresponding runtime exception. It is a failed **actual lift**, not a solver UNSAT verdict.
- Synthetic D={a,b}: the suffix recursion returns UD and the flower-subset test returns factor-complete.
- Synthetic D={a,ab}: UD, but the flower test finds the missing factor bb.
- Synthetic D={a,b,ab}: not UD, while factor-complete.
- Synthetic D={a,ab,bb}: UD and factor-complete, demonstrating that the test does not assume a prefix code.

These are finite same-owner controls, not independent-model/human/formal/kernel acceptance. The scalar gcd and initial border identities are necessary only; the algorithmic tests would check an actual supplied finite D, and none is supplied here. No native solver, external model, selected historical control, CAS, floating arithmetic, or previous checker output was used.

**First exact missing step:** construct or exclude simultaneous U_s, Λ satisfying the mixed-carry equations (1.6), the literal A,Y anchors and the chosen actual cardinality, then meet both §4 full-code tests with one finite D. In the odd-tail d=15 branch, every row also has the common 15-point complement and shared prime-power/T2 constraints, but the example in §3.2 shows those row facts do not solve the lift. The even-Q branch and other odd head-prime combinations remain unrestricted in (1.6). No original completion/noncompletion or numerical order floor follows.

A fresh review must check the all-r/all-carry equivalence including multiple Q-lifts, the odd-Q projection and common-spectrum quantifiers, the LL/T2 import only where invoked, the finite suffix/flower tests, and the exact conditional status of the border caller. No prior review verdict is transferred.

**END OF MULTIPLE-ODD-HEAD MIXED-CARRY COMPLETION INTERFACE.**
