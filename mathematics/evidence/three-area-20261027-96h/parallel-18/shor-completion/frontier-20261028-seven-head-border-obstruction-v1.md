# Shor completion: an all-order seven-head border obstruction

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:41:13 PDT 2026**.
**WRITTEN all-order necessary theorem, with exact symbolic identity checks and independent finite program controls. No unrestricted completion/no-go, formal proof, peer acceptance, independent-family review or novelty clearance is claimed.**

## 1. Theorem and same-code scope

Let D be ANY finite uniquely decipherable, factor-complete extension of the literal Shor code. Let `a^n` be its actual pure-a atom. Define from actual D-atoms, including multiple consecutive b's,

    P = {i mod n : a^i b^k in D for some k>=1},
    Q = {j mod n : b^l a^j in D for some l>=1}.

The independently written border reconstruction in `frontier-20261028-six-head-border-factorization-v1.md` gives `n>=26`, a **direct tiling** `P+Q=Z_n`, and the old anchors

    A={0,3,8,11} subset P,     Y={0,1,7,13,14} subset Q.

The tiling and both anchors belong to the SAME actual D. The direct-tiling theorem itself is prior (e.g. [Cordero, arXiv:2301.13566, Theorem1.1](https://arxiv.org/html/2301.13566v1)); it was also reconstructed from the actual words and guards in that predecessor. Here is the new all-order deduction:

> **Theorem.** Under just the direct tiling and anchors above, `|P|>=7`. Hence every such D has `|P|>=7`, `|Q|>=6`, and `n=|P||Q|>=42`.

In particular neither the five-head nor six-head border branch exists at ANY feasible order: **no restriction on `v_2(n)` or `v_3(n)` is needed**. The previous n=660/1320 six-head searches were substantially weaker than this written conclusion.

All arithmetic below is in Z_n. Since n>=26, 0,3,8,11 are distinct. Any additional P-elements named U,V are distinct from each other and from A. In any displayed collision, the two P-elements are distinct; if its two Q-elements happened to coincide after specialization, the same equality would force the two P-elements equal, which is excluded. Thus the eliminations remain valid for EVERY specialization of U,V, not merely generic variables.

## 2. Four and five heads

If `P=A`, cover6. Its only possible Q-elements `6,3,-2,-5` are all forbidden by the already present0 or1, because respectively

    6+3=1+8,    3+0=0+3,    -2+3=1+0,    -5+8=0+3.

If `|P|=5`, write `P=A union {U}` and cover the target `U+4`. The five possible Q-elements and their collisions with old Q-anchors are:

    candidate in Q       collision with an old Q-element
    U+4                  (U+4)+3 = 7+U
    U+1                  (U+1)+0 = 1+U
    U-4                  (U-4)+11 = 7+U
    U-7                  (U-7)+8 = 1+U
    4                    4+0 = 1+3

All are impossible by directness. Therefore the target cannot be covered, contradiction. This uses only Q-anchors1 and7.

## 3. Six heads: forcing two incompatible representations

Suppose `P=A union {U,V}`. For the target `U+4`, the same five collisions leave ONLY the sixth possibility, giving

    U-V+4 in Q.                                                (1)

Interchanging U and V gives `V-U+4 in Q`. Now cover `U+9`. Five of its six possible Q-elements are forbidden:

    candidate in Q       collision with an existing Q-element
    U+6                  (U+6)+8 = 14+U
    U+1                  (U+1)+0 = 1+U
    U-2                  (U-2)+3 = 1+U
    9                    9+0 = 1+8
    U-V+9                (U-V+9)+3 = (U-V+4)+8    [using (1)]

The only remaining option is `U+9 in Q`. By symmetry `V+9 in Q`. But now

    (U+9)+V = (V+9)+U,

with distinct P-elements U,V and distinct Q-elements `U+9,V+9`. This violates directness. Thus `|P|=6` is impossible and the theorem follows.

The argument uses no exhaustive search and no assumptions about an auxiliary completion. It is a finite chain of additive equalities valid in the actual cyclic group. It does not require or imply that any larger border factorization is realizable by a complete UD code.

## 4. Consequence for actual multi-b atoms

Let `N_out` count actual one-b D-atoms whose head residue is outside A. `frontier-20261028-zero-column-multib-escape-v1.md` proves on the SAME D that either

    N_out >= n-4 floor(n/5),

or D has at least `|P|-4` actual atoms `a^i b^k`, `k>=2`, with distinct heads outside A. Since the present theorem gives `|P|>=7`, the latter count is now **at least three**, not merely one. In particular at n=1320, fewer than264 outside-head one-b atoms would force at least three distinct new-head multi-b border atoms. This is still only a necessary alternative.

## 5. An additional prime-power filter and the 1320 border sizes

For a direct tiling with `v_2(n)=3`, if `8` divides `|P|`, then `|Q|` is odd. At primitive orders2,4,8, the tiling polynomial identity forces each cyclotomic factor `Phi_2,Phi_4,Phi_8` to divide P: none can divide Q since each evaluates to2 at1 but Q(1) is odd. Their product is `1+X+...+X^7`. Reducing P modulo `X^8-1` shows its counts are equal in all eight classes. The old heads0,8 share class0 and 3,11 share class3, so each class needs at least two P-elements and `|P|>=16`; in particular `|P|=8` is impossible. Because `v_2(n)=3`, a P-cardinality divisible by8 is in fact at least24.

For the particular necessary border problem `n=1320`, divisibility, the present `|P|>=7`, old `|Q|>=6`, and prime-uniformity eliminate size8 as just shown; size11 since Phi_11 forces P uniform mod11 while0,11 both occur; and size220 since |Q|=6 and Phi_3 forces Q uniform mod3 while1,7,13 all occur. The only remaining cardinalities **under these necessary filters** are

    |P| in {10,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132,165}.

None is asserted to be feasible. This is not an exclusion of n=1320, and n>=42 does not improve the separately recorded stronger lower-order bound.

## 6. Actual checks and assurance boundary

`frontier-20261028-seven-head-symbolic-check.py`, SHA256 `5a99d1a528228ddbb6165dca04e80a4d41ef9f4b7faf1359409d51adcc45027d` (59 LF, 2567 bytes), checks with integer coefficient triples every stated collision identity, every candidate list for targets6, U+4 and U+9, symmetry, and the final double hit. It also directly verifies SAT factorizations at n=60 and1320 after the old Q-anchors are removed; thus the obstruction is not claimed for arbitrary P/Q anchors. Symbolic identity checks do not themselves prove cyclic directness or all-order coverage; those are in the written proof.

An independent Boolean exact-one propagation implementation, `frontier-20261028-border-exact-one-replay.py`, SHA256 `b6c65ccc2c19aea96bd67c44ae520a6b3f3e151b5f17b945d0e373d7cf7ddc30` (124 LF, 5161 bytes), separately tested all48400 valuation-parametrized size-six cases at n=1320 (two chunks `[0,24200)` and `[24200,48400)` in its own `u=1 mod6` outer ordering). All48400 conflicted under propagation; zero unknown and zero search nodes. Its small Boolean solver was also compared in-kernel against direct exhaustive tiling enumeration on3305 cases for (n,|P|)=(4,2),(6,2),(6,3),(8,2),(8,4), and against80 seeded directly checked SAT controls at n=60,120,660,1320. Those checks support code/identity accuracy but neither are needed for, nor replace, the all-order proof.

These are same-harness written and described integer checks only. General border factorization is prior; the present specific anchor argument has not been novelty screened or independently reviewed. The original finite UD factor-completion problem remains OPEN, and no larger-border branch is adopted as feasible.

**END OF SEVEN-HEAD BORDER OBSTRUCTION.**
