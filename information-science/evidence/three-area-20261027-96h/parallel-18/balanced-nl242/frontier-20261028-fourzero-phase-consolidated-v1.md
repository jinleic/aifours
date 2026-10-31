# info-6: consolidated four-zero radical-phase packet

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before composing: **2026-10-28T21:31:05-0700 PDT**. This is one self-contained written packet for the **original nine-variable Boolean target**. The rank-six/four-zero reduction at T≠0 has the exact same-harness written support recorded in f131 below. The mod-8 fiber rigidity, unequal-phase theorem, and translation normalization here are **UNREVIEWED AUTHOR CLAIMS** until a separate full-scope review and parent disposition. The formal fiber examples are explicitly non-witnesses. No global or four-zero nonexistence, actual target witness, novelty, human review, independent-model-family review, or Lean/kernel verification is claimed.

## 1. Exact claim and open cases

Let f:F₂⁹→{0,1} be balanced and suppose `max_a |W_f(a)|≤28`, with

    W_f(a)=Σ_x (−1)^{f(x)+a·x},      k(a)=W_f(a)/4.

Let M be its 256-point one-support, `T=⊕_{x∈M}x`, and `Z={a:k(a)=0}`. Then:

1. **T≠0**, and Z has even size between 4 and 148. If the even-half polar rank is ≤4, then |Z|≥8.
2. If **|Z|=4**, the even-half polar has rank 6 and Z is exactly its two-dimensional radical R. The number of magnitude-16 Walsh coefficients is 108 or 140.
3. In this four-zero case there are canonically defined linear functionals `λ,ρ∈R*`, representing respectively the even-half mod-8 phase and the odd-half quadratic phase. They satisfy **λ≠ρ**.
4. Under input translation, λ and ρ acquire the **same** arbitrary radical character. Thus every putative four-zero target has an equivalent translate with `ρ=0` and `λ≠0`; its normalized odd Q has weight 112 or 144 and the translated count `A₋₂+A₆` is respectively 72 or 56 when the even-half q-zero count is 112 or 144.

The rank-six statement in item 2 is already parent-supported **only at f131's precise T≠0 scope**. The T≠0 proof and all phase/normalization claims are written out below but have not received the same disposition in this packet. The statement is conditional on an actual function; it does not assert any phase or rank is realizable. Targets with six or more zeros, and the rank-six four-zero branch itself, remain open here.

## 2. Exact Boolean caller and the T=0 exclusion

Since |M|=256, W_f(0)=0. For a≠0 let `n_a=#{x∈M:a·x=1}`. Then

    k(0)=0,     k(a)=n_a−128 for a≠0,     k(a)≡a·T (mod 2).                 (4)

All k are integers, `|k|≤7`, and Parseval and Booleanity give the complete autocorrelation caller

    C(b)=Σ_a k(a)k(a+b)=2¹⁴·1_{b=0}.                                         (5)

Conversely, if an integer array k has k(0)=0, |k|≤7 and satisfies (5) for **every** b, then `U(x)=Σ_a k(a)(−1)^{a·x}` has U(x)²=2¹⁴. Hence U/128 is a Boolean sign table, its inverse Walsh transform is 4k, and k(0)=0 makes it balanced. This converse requires a **single frequency-labeled array and all 511 nonzero-shift equations**, not independent scalar profiles or a collection of unlabeled fibers.

The quadratic caller used below follows directly from (4). If T=0, every k is even and `q=k/2 mod2` is a Boolean quadratic on all of F₂⁹: for any coordinate basis, expanding the integer parity `a·x` modulo four shows degree≤2. Since q(0)=0, the nonzero quadratic-or-lower function 1+q has at least `2^(9−2)=128` ones. On that set |k|≤4; elsewhere |k|≤6. Equation (5) at zero would give

    16,384=Σ_a k(a)²≤128·16+384·36=15,872,

impossible. Hence T≠0 for the stated peak bound. The elementary minimum-support lemma used here and later follows by induction from `p(x',x_n)=p₀(x')+x_n p₁(x')`: if p₁=0 double wt(p₀), and otherwise `wt(p₀)+wt(p₀+p₁)≥wt(p₁)`.

## 3. Self-contained four-zero geometry

Put `K=T^⊥`, an **eight-dimensional** frequency subspace. By (4), k is even on K and odd outside. Define `q=k/2 mod2` on K and `Z₈={a∈K:k(a)≡0 mod8}`. The moment expansion of (4) makes q quadratic; its polar is the alternating bilinear form B. Let `z₈` denote the indicator of Z₈.

For every five-dimensional L≤K, any even L-coset A and one fixed odd L-coset B₀ form an affine frequency 6-flat. The balanced affine-energy identity gives

    E(A)+E(B₀)≡0 (mod32),       E(C)=Σ_{a∈C}k(a)².                            (6)

For completeness: the spatial annihilator has dimension three; its 8-point signed character sums v_C are even, and their signed total is a Walsh coefficient divisible by four. Thus `Σ_C v_C²≡0 mod8`, and quotient Parseval gives `Σ_flat k²=4Σ_C v_C²≡0 mod32`. Balancedness supplies W≡0 mod4 and k(0)=0; the odd coset in this derivation is a convenient choice, not an extra hypothesis.

Write `n_q(A)=Σ_A q` and `n_z(A)=|A∩Z₈|`. The possible squares of an even integer modulo 32 yield

    E(A)≡16[n_q(A)/4+n_z(A)] (mod32).                                       (7)

The quotient is integral. A five-variable quadratic of polar rank 0,2,4 has weights `{0,16,32}`, `{8,16,24}`, or `{12,16,20}`. If rank≤2, `n_q/4 mod2` is identically zero across cosets. If rank 4, let r generate its one-dimensional radical; the restriction is balanced exactly when `q(r)+B(a,r)=1`, otherwise its weight is 12 or 20, so

    n_q(a+L)/4 ≡ 1+q(r)+B(a,r) (mod2).                                      (8)

Equations (6)–(8) imply the fifth derivative of z₈ along L is affine in its base point; hence deg z₈≤6. If rank(B)≤4, the radical of a rank-four restriction lies in the global radical by `dim(L∩rad B)≥1`, so (8) is constant and deg z₈≤5. As 0∈Z₈, the minimum-support lemma gives |Z₈|≥4, or ≥8 at rank≤4. Also deg z₈<8 makes |Z₈| even.

When |Z₈|=4, every derivative of z₈ has degree≤5 and is zero or has weight at least 8. A difference of two support points produces overlapping translates, so its derivative has weight <8 and vanishes. Thus Z₈ is one coset of its period space; since it contains zero, it is a linear 2-plane. If a radical vector r lay outside it, choose a 5-space L containing r and disjoint from Z₈. The coset expression (8) is then constant, but the four points of Z₈ occupy four different L-cosets and the other four cosets are empty. This contradicts (6)–(7). Thus `rad B⊆Z₈` and rank(B)≥6.

Rank eight is also impossible. Because q vanishes on the plane Z₈, it is totally isotropic. Extend `Z₈=span(e₁,e₂)` to a symplectic basis, take `D=span(f₁,f₂,e₃)` and `L=D^{⊥_B}`. Then dim L=5, rank(B|L)=2, and L∩Z₈=0. All q-weights on L-cosets are divisible by eight, while the Z₈-parities again split into four ones and four zeros, contradicting (6)–(7). Thus rank(B)=6 and `Z₈=rad B`.

Under |k|≤7, Z₈ is the actual Walsh-zero set. In rank six q vanishes on its two-dimensional radical and descends to a nondegenerate six-variable quadratic, whose zero count is 28 or 36. Hence `#{q=0}=112 or 144`; after the four zeros, exactly 108 or 140 coefficients have |k|=4, i.e. |W|=16. Independently, the 256 odd k contribute at most `256·49` to (5), and the 256−|Z| nonzero even ones at most 36 each, so evenness gives |Z|≤148.

**f131 qualification.** The reviewed/adopted reduction assumes T≠0 and concerns nine-variable f, not an eight-variable f; the preceding T=0 argument is a separate author reconstruction. The reviewer did not adopt an out-of-manifest formal histogram. Its four recorded minors are carried as stated; the abstract rank-six control is not a Boolean witness.

## 4. The even mod-8 and odd quadratic phases

Assume now exactly four Walsh zeros, and write R=Z=rad B. On the odd half choose a₀∉K and set

    Q(x)=(k(a₀+x)−1)/2 mod2,       x∈K.

The polar of Q is B. To see this without a source shortcut, for any a,b the support parity expansion gives

    k(a+b)−k(a)−k(b) ≡ −2Σ_{x∈M}(a·x)(b·x) (mod4),                         (9)

with the harmless 128 corrections at zero suppressed modulo four. The corresponding second difference based at any a₀ is the same modulo four. Dividing by two on K gives the polar of q, and dividing the odd second difference by two gives the polar of Q. Consequently `Q(x+r)+Q(x)` is independent of x for every r∈R and defines a linear functional `ρ:R→F₂`. If ρ≠0, Q is balanced of weight 128; if ρ=0, Q descends to a rank-six quadratic on K/R and has weight 112 or 144.

There is also a linear `λ:R→F₂` such that

    k(a+r) ≡ k(a)+4λ(r)q(a) (mod8),       a∈K, r∈R.                        (10)

Here is the complete caller for (10). Choose K=F₂⁶_x⊕R. Because q vanishes on R, it descends to a nondegenerate six-variable quadratic. By symplectic normal form it is linearly equivalent to either `x₀x₁+x₂x₃+x₄x₅` or that form plus `x₀+x₁`; use its squarefree integer polynomial as a lift g₀. Expand each integer parity a·u modulo eight. For a basis b_i of K, all first support moments `m_i=Σ_{u∈M}(b_i·u)` are even, and

    k(a)/2 ≡ Σ_i (m_i/2)a_i − Σ_{i<j}m_ij a_i a_j
                +2Σ_{i<j<ℓ}m_ijℓ a_i a_j a_ℓ                  (mod4).       (11)

The coefficients modulo two are q, so `k/2≡g₀+2h (mod4)` for a Boolean polynomial h of degree≤3. Write `h=h₀(x)+r₁h₁(x)+r₂h₂(x)+r₁r₂h₁₂(x)`, with degrees of h₁,h₂ at most two and of h₁₂ at most one. On q(x)=0 the only zeros are the four points of R: k/2 is 0 mod4 at x=0 and 2 mod4 otherwise. Thus h is independent of r on q=0, so h₁,h₂,h₁₂ vanish there.

If a six-variable degree≤2 polynomial p vanishes on the zero set of nondegenerate q, then p=0 or p=q: supp(p) and supp(q+p) partition the q-one set, whose size is 28 or 36, whereas a nonzero quadratic in six variables has weight in `{16,24,28,32,36,40,48,64}`; no two nonzero such weights sum to 28 or 36. The same argument makes a degree≤1 p vanish, since it cannot equal q. Hence h₁,h₂ are each 0 or q and h₁₂=0, giving (10). λ is unique because q has one-points.

## 5. The phases are unequal

Suppose λ=ρ and write `χ(r)=(−1)^{λ(r)}`. For each coset F=a+R define

    E_F=Σ_{r∈R}k(a+r)²,       S_F=Σ_{r∈R}χ(r)k(a+r).

The sign of S_F depends on the representative, not its square. The zero fiber has E_F=S_F=0. On every other q-zero even fiber the modulated entries are ±4, so `S_F²≥10E_F−640`. On a q-one even fiber, (10) and the character turn all four entries into one of `{−6,2}` or `{−2,6}`. If n of the first class equal −6, then `E_F=16+32n`, `S_F²=(8−8n)²`, and `S_F²−10E_F+864=64(n−3)(n−4)≥0`.

On an odd fiber, Q changes by ρ=λ and negating an odd coefficient exchanges the two Q classes. Thus the modulated entries lie in `{−7,−3,1,5}` or its negative. For either class `S_F²≥10E_F−1464`: maximize `10Σx_i²−(Σx_i)²` on [−7,5]⁴. The expression is convex in each coordinate; its maximum occurs at a vertex. With n entries −7 it is `600+720n−144n²`, at most 1464.

Let z=|{q=0}|∈{112,144}. The three fiber types occur `(z−4)/4`, `(256−z)/4`, and 64 times. Equation (5) and the inequalities give

    Σ_F S_F² ≥ 10·16,384 − 640(z−4)/4 − 864(256−z)/4 − 1464·64
              = 16,384+56(z−16) > 16,384.                                    (12)

On the other hand, character orthogonality and the **same** autocorrelation caller imply

    Σ_F S_F² = Σ_{r∈R}χ(r)C(r) = C(0)=16,384.

This contradiction proves **λ≠ρ**. It is a written all-variable argument; it does not depend on a solver UNSAT result or on a selected histogram. ∎

## 6. Translation-normalized search form

For t∈F₂⁹ set `f_t(x)=f(x+t)` and `ψ_t(r)=r·t`. The support has even size, so T is unchanged; `k_t(a)=(−1)^{a·t}k(a)`, preserving the zero set, q and B. On even k,

    (−1)^ε k ≡ k+4ε q  (mod8),

and on odd k, negation toggles `(k−1)/2 mod2`. Therefore

    λ_t=λ+ψ_t,       ρ_t=ρ+ψ_t,       λ_t+ρ_t=λ+ρ.                          (13)

Every character of the two-plane R occurs for 128 input translations. Choose ψ_t=ρ. Then ρ_t=0 and `λ_t=λ+ρ≠0`; a radical-basis change may label this nonzero character as the first coordinate. The normalized odd Q is nonbalanced of weight 112 or 144. In each q-one radical fiber exactly two scaled coefficients have `(k_t/2)≡3 mod4`, giving `A₋₂+A₆=(256−z)/2`, namely 72 for z=112 and 56 for z=144. These are **translated signed counts**, not an assertion that the original signed histogram is translation-invariant. Complementing globally if needed sets f_t(0)=0 without changing either phase or any Walsh magnitude.

## 7. Concrete remaining obligations and non-witness barrier

The unequal-phase theorem leaves a genuine four-zero problem. To close the original target, a subsequent construction or exclusion must handle at least:

1. **Common quotient placement.** Assign all 128 radical fibers to actual positions of the same seven-dimensional frequency quotient, not merely as an unlabeled multiset. The even half must share one rank-six q with zero plane R; odd Q and the magnitude/peak indicator must be compatible with that same geometry.
2. **All remaining correlations.** The three nonzero directions in R are only three of 511. The other **508** nonzero-shift equations in (5), including cross-fiber terms and their phase orientation, remain mandatory.
3. **Boolean inverse.** A single labeled k satisfying all of (5), k(0)=0 and |k|≤7 yields a balanced truth table by §2; partial sums, a formal histogram, a quadratic, or isolated fiber solutions do not. A candidate truth table would require independent complete Walsh/weight recomputation before any witness claim.
4. **Other zero counts.** The λ/ρ conclusion applies only when |Z|=4. Balanced peak≤28 targets with at least six zeros are not excluded. The separately adopted ≥92 peak theorem may bridge NL≥242 to NL=242; that bridge is not re-proved or expanded here.

Three exact **formal tuple multisets** were constructed for the three unequal phase types; each has the stated scalar/dual checks and C(r)=0 for the three nonzero r∈R. They are recorded in `frontier-20261028-fourzero-directed-fiber-barrier-v1.md`, SHA-256 `1aaf926179a277ab1c27b9222dc0fe7eafa82d318804cab49fb15090f0b62b93`, 45 LF, with direct tuple and dual replay receipts. They are not assigned to quotient frequencies, do not constitute one common q/Q/P, do not test the other 508 correlations, and are not Boolean or code witnesses. Their satisfaction of a relaxation is not an argument for actual existence.

## 8. Status, controls and exact pins

f131's same-harness written disposition is `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-four-zero-rank6-radical-parent-v1.md`, SHA-256 `12efd10b4a9de2ac70cd49541e36e6a0c5df6bd4deecbb74e085c2eb48795dc3`, 31 LF. Its review is `review-waves/f131-walsh-four-zero-rank6-only/review-v1.md`, SHA-256 `f30ca6b42504acc0cdb4dda2569786e293adbd4acfd9e73070113feae8878c5e`, 116 LF, 0 FATAL/0 MAJOR and M1–M4 as qualified above. The phase/normalization and formal-fiber statements in this consolidated packet are **not** promoted by f131.

The locally executed same-owner controls include all 4,194,304 six-variable quadratics for the vanishing lemma, exact dynamic-programming pairing controls, all equal radical-phase four-tuples and a sign-orientation mutation, and 16 genuine balanced-function translations plus the 64 abstract phase transformations. They support the stated finite identities only; they are not an independent-model, human or formal proof.

| Load-bearing or evidence file (same owner root unless absolute) | SHA-256 | LF | Status |
|---|---|---:|---|
| `frontier-20261028-radical-fiber-autocorrelation-v1.md` | `7fef5e3cec28f32fe824f742ccdf1124b6b2019527e671e14ba9f4eee15a3260` | 56 | λ source, unreviewed |
| `frontier-20261028-fourzero-radical-phase-exclusion-v1.md` | `49b97bf0463870565cd8351ed44d86df1933cbf850767c86517072f13a8142ca` | 57 | inequalities, unreviewed |
| `frontier-20261028-fourzero-unequal-radical-phases-v1.md` | `3ad74c82b53f1ed16834dac944fd49075fcd53fa05d604b38afbc78a96222761` | 56 | phase source, unreviewed |
| `frontier-20261028-radical-fiber-check.py` | `a7ad873c202382111ed218552de9675bb639aa8cdd1dac71ad4d9e5678b9a8e4` | 60 | finite control |
| `frontier-20261028-radical-fiber-check-result.json` | `271ba7933430e2d32999afd816a1055d48e926e02061cc7e6b52cacb60d5f6e7` | 15 | finite receipt |
| `frontier-20261028-equal-phase-character-check.py` | `cfe6a14ada0380091f7dc9b046c28647c109e9adc4de2fe924c19817dda6a57b` | 44 | finite control |
| `frontier-20261028-equal-phase-character-check-result.json` | `1c2012652a38c8210eee836e0c3f0dfc24e4d70d636c33ed895f3ef5b4878714` | 27 | finite receipt |
| `frontier-20261028-radical-translation-check.py` | `dec8d8a303ac77a111ac077263cc945f71919d9ecc88df1096c670d2aa4ca513` | 56 | finite control |
| `frontier-20261028-radical-translation-check-result.json` | `b27f503898ef546930746c77827190cebfb80ad372951726a8c88d5cfdc521bd` | 14 | finite receipt |
| `frontier-20261028-fourzero-directed-fiber-barrier-v1.md` | `1aaf926179a277ab1c27b9222dc0fe7eafa82d318804cab49fb15090f0b62b93` | 45 | formal non-witness evidence |

All historical HELD/ZERO/NONINPUT records remain unadopted; no held mathematical outcome is used as a premise. The predecessor-specific claim that an outside formal model is excluded was not part of f131's adopted scope and is not needed here. **END.**
