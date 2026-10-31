# Independent review: zero-column escape and Shor border obstructions

Native `/bin/date` observed before this file's exclusive creation: **2026-10-28T19:03:34-0700 PDT**.
Binding assignment: `manifest-v3.json`, SHA-256 `c5a4d16c2466a145ca76695d51763320ea13dbd3772f5dcd121cedb3ed760e20`. This is a same-harness, written-mathematics review, not an external-family, human, proof-assistant, or novelty review. No author contact, author-code execution, or held/withdrawn/quarantined body was used.

## Verdicts

| Candidate | Verdict (FATAL / MAJOR / MINOR) | Reviewed conclusion |
|---|---:|---|
| Zero-column / multi-b escape | **0 / 0 / 1** | The inequality and the strict-small-outside multi-b alternative follow after the small proof repair below. |
| Seven-head border obstruction | **0 / 0 / 0** | No mathematical defect found in the specified statements: the direct anchored border has at least seven heads; the Fourier/divisor filters follow. |
| Eight-head border obstruction | **0 / 0 / 0** | No mathematical defect found: both seven-head cases fail, so the actual same-code border has at least eight heads; the stated valuation and 1320 consequences follow. |

**MINOR 1 — missing initial padding in the written proof.** `frontier-20261028-zero-column-multib-escape-v1.md:36` says that interior padding and padding after the last b suffice. The first chosen heads are the same *residue* `h`, not necessarily equal literal exponents, so those two locations alone cannot generally equalize the initial a-runs. Also pad **before** the first one-b atom. The concrete corrected two-list construction is given below. This is a local proof repair, not a counterexample to the inequality; it is needed if the original text is read literally. The stronger `|P|-4` conclusion is used under the explicit hypothesis `N_out < n-4 floor(n/5)`, not inferred merely from the existence of one multi-b atom.

## Identity, completeness of inputs, and source boundary

All five input files were SHA-256 checked *before* their bodies were read, then read completely in the manifest order, using exact raw windows. Observed byte and LF counts match the manifest. No hash mismatch or process finding was observed. Names below are relative to `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/`.

| Order | File | SHA-256 | Bytes / LF |
|---:|---|---|---:|
| 1 | `frontier-20261028-zero-column-multib-escape-v1.md` | `ae6ffc9c29f74b1ea4951a50c2c9b79e82ebd2362883896122c93ef55eeb49b5` | 5796 / 58 |
| 2 | `frontier-20261028-seven-head-border-obstruction-v1.md` | `713afb914e2781c8367e31726c298bc158c2c5b61176277c2d219762dfd96e24` | 7566 / 91 |
| 3 | `frontier-20261028-seven-head-symbolic-check.py` | `5a99d1a528228ddbb6165dca04e80a4d41ef9f4b7faf1359409d51adcc45027d` | 2567 / 59 |
| 4 | `frontier-20261028-eight-head-border-obstruction-v1.md` | `803c69db29d403a1a2fec137dcd9f50e132356802b00b7d64ac2e9138de4b412` | 5892 / 76 |
| 5 | `frontier-20261028-eight-head-certificate.py` | `6e629ecf8906ad4dc7b3d3e4b87dd44a8ffaa12c59b7ce3e908f15ec36a9eeb6` | 4036 / 91 |

For the named local imports, I read the relevant definition/proof sections of `frontier-20261028-six-head-border-factorization-v1.md:1-95` (SHA-256 `56fd2cff931af2da61e2f8a17c513d8af5c3cc8064c9d9ed66c5c361fb3a6051`) and `frontier-20261028-no-saturated-bayonet-lines-v1.md:1-44` (SHA-256 `47230ac1429a23915214a804f2fd8a91a21f6ddc326f2914e03ebdbf2cb19114`); their unrelated later claims were not reviewed. I independently reconstructed the premises used below rather than adopting those packets' conclusions uncritically.

The literal anchor membership is also visible in Kraizberg, [*A Weak Structural Form of Commutative Equivalence in Finite Codes*, §1.1](https://arxiv.org/html/2603.27656v1): its Shor set is `b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2}`. Cordero, [*Factorizations of Cyclic Groups and Bayonet Codes*, Theorem 1.1](https://arxiv.org/html/2301.13566v1#S1.Thmtheorem1), states the named prior border factorization for finite maximal codes containing `b,a^n`; here I also checked its relevant finite factor-complete special case directly as follows. These source checks do not establish the novelty or present open status of the new deductions.

## Reconstructed prerequisites and zero-column estimate

1. **Actual one-b count.** For a finite factor-complete UD code `D` over `{a,b}`, let `L` be maximum atom length and assign Bernoulli word weight `p^#a(1-p)^#b`, `0<p<1`. UD gives `K(p)=sum_{d in D} weight(d) <= 1`: the `k`-atom products are all distinct and have at most `kL` possible lengths, each length carrying total weight at most 1. In fact `K(p)=1`. If it were smaller, the total weight of `D*` would be `1/(1-K(p))`; yet every length-`t` binary word occurs inside a `D*` product, and trimming to its intersected boundary atoms uses fewer than `L` extra letters on either side. With `delta=min(p,1-p)>0`, the total weight of products of lengths between `t` and `t+2L-2` is bounded below by `delta^(2L-2)/(2L-1)`, since each such product has at most `2L-1` length-`t` factors. This contradicts the vanishing tail of a finite weighted sum. There is exactly one pure-a atom, `a^n`, by UD. Expanding `K(1-y)=1` at `y=0`, the linear coefficient is `|B|-n`; finiteness gives **`|B|=n`**. This calculation counts actual atoms, not just endpoint residues.

2. **Actual b-run border.** Set `P={i mod n: a^i b^k in D, k>=1}` and `Q={j mod n: b^l a^j in D, l>=1}`. Since `b` is an atom, no other pure-b atom is possible. For two representations `i_1+j_1 = i_2+j_2 (mod n)`, choose actual endpoint atoms and pad with `b` atoms outside and `a^n` atoms in the central run to get the same `b^L a^G b^K`. If the residue pairs differ, the actual lists differ, contradicting UD. Thus `P+Q` is direct. Conversely, embed `b^L a^g b^L` as a factor of a product, with `L` maximum atom length and `g>L` in any prescribed residue class. The atoms at the last left and first right b have the above Q/P forms; intervening atoms are `a^n`. Hence every residue is covered. The anchors `A={0,3,8,11}` and `Y={0,1,7,13,14}` belong to these **same-code** sets. Pairwise padded old-word products force these anchor heads and tails to be distinct mod n and their 20 cross-sums to be distinct. The independent exact check shows no `n=1,...,25` has 20 distinct old cross-sums, hence `n>=26` (the old anchors alone have distinct cross-sums at 26). The five target-2 collisions in the named predecessor, also independently checked, show `Q` cannot equal `Y`; therefore `|Q|>=6`.

3. **Repaired direct row-column argument.** Pick actual one-b atoms `u_t=a^{i_t} b a^{j_t}` and `v_t=a^{r_t} b a^{s_t}` for `t=1,2`, with `i_1 ≡ i_2 (mod n)`, `s_1 ≡ s_2 ≡ 0`, and `j_1+r_1 ≡ j_2+r_2`. Choose nonnegative common exponents `G_1,G_2,G_3` respectively congruent to `i_t`, `j_t+r_t`, `s_t` and large enough for both t. The actual word lists

   `(a^n)^((G_1-i_t)/n), u_t, (a^n)^((G_2-j_t-r_t)/n), v_t, (a^n)^((G_3-s_t)/n)`

   both spell `a^G_1 b a^G_2 b a^G_3`. Distinct selected residue pairs give distinct lists. Hence `J_h+I_0` is direct and `|J_h| c_0<=n`. The same padding argument rules out two distinct one-b atoms with identical endpoint residue pairs. Since `|B|=n`, summing the four row caps gives **`N_out >= n-4 floor(n/c_0)`**.

4. Since `A⊆I_0`, either `c_0>=5` and `N_out>=n-4 floor(n/5)`, or, whenever that numerical bound fails, `c_0=4` and `I_0=A`. For every `p in P\A`, an actual representative `a^i b^k` cannot have `k=1`, since that would put its head in the zero-tail column; it has `k>=2`. Distinct p require distinct atoms. Thus the strict-small-outside branch has at least `|P|-4` different new-head multi-b atoms. This justifies the quantitative escape and its later strengthenings. The old conditional six-head/valuation example in candidate 1 is now **vacuous**, because candidate 2 rules out six heads altogether; its modular implication is nonetheless consistent.

## Independent reconstruction of the border proofs

**Four through six heads (`seven-head...md:27-61`).** For `P=A`, target 6 has precisely the four listed complements `6,3,-2,-5`, each colliding with existing 0 or 1 in Q. For `P=A∪{U}`, the five entries at target `U+4` exhaust `t-P` and each collides with a known Q anchor. With a sixth head `V`, that same target forces `E=U-V+4 in Q`, and symmetry forces `V-U+4`. At target `U+9`, the five listed forbidden columns leave only `U+9`; swapping U,V also forces `V+9`. The resulting `V+(U+9)=U+(V+9)` is a genuine double representation because U and V are distinct actual P-elements. The arithmetic remains valid after arbitrary specialization modulo n; no generic-variable noncollision assumption is needed. Thus `|P|>=7`, and with `|Q|>=6`, `n>=42`.

**Seven heads (`eight-head...md:21-58`).** In each entry `K/(p,p')` I checked the exact identity `(t-s)+p=K+p'`, prior availability `K in Q`, and that p and p' are distinct members of the assumed P. Coverage of `U+4` leaves precisely the V and W columns; swapping V,W permits the choice `E=U-V+4`. The next row forces `F=W-U+4`, and target `W+9` has exactly the two listed surviving columns.

* If `B=W+9`, the following three rows force `C=U-W+9`, `D=U+12`, and `H=W-2V+12`; the final row forbids all seven representations of `U-V+W+12`.
* If `B=W-V+9`, the next three rows force `D=W+12`, `H=U-2V+W+12`, and `I=W-2V+15`. The identity `H+3=I+U` is a collision because `3 != U` in P.

The second branch's Q knowledge is reset to the common root facts; it does not import any first-branch assumption. Every survivor is a source column, and distinct P sources produce distinct `t-s` even after specialization. Together with the previous proof this gives **`|P|>=8`** and the strict-small-outside branch has **at least four** actual multi-b atoms on distinct heads outside A.

**Fourier and size audit (`seven-head...md:73-81`, `eight-head...md:68`).** If `v_2(n)=3` and `8 | |P|`, then `|Q|` is odd. At primitive 2nd, 4th and 8th roots, `P(X)Q(X) ≡ 1+...+X^(n-1) mod (X^n-1)` makes one factor vanish; Q cannot contain any of `Phi_2,Phi_4,Phi_8`, since each evaluates to 2 at 1 while Q(1) is odd. Their product `1+...+X^7` divides P, making the P-counts uniform mod 8. Old heads 0,8 and 3,11 require each class to have at least two members, hence `|P|>=16`; since `v_2(|P|)=3`, actually `|P|>=24`. In particular `|P|=8` is impossible and **`|P|>=9` for `v_2(n)=3`**.

For `n=1320=2^3·3·5·11`, cardinality 9 does not divide n, so **`|P|>=10`**. For size 11, `|Q|=120` is not divisible by 11 and `Phi_11` forces P uniform mod 11, contradicting the two old heads 0 and 11. For size 220, `|Q|=6`, `|P|=220` is prime to 3, and `Phi_3` forces Q uniform mod 3 with two per class, contradicting old tails 1,7,13 in one class. Together with the Q-size bound and the 2-adic exclusion, the remaining necessary-filter sizes are exactly

`{10,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132,165}`.

At n=1320 the escape threshold is 264. Fewer than 264 outside-head one-b atoms would require four distinct new-head multi-b atoms. These are necessary conditions only.

## Independent exact work and limitations

I wrote `independent-check-v1.py` (SHA-256 `017c6d6d82aec672d7fa049606a7d9b6790d8a6a94ba41b1884bea4d9c8fcc7e`) from the written definitions, without importing or executing either author script. Its run and exact stdout, exit 0, and observed pre-receipt clock are recorded in `independent-check-receipt-v1.json` (SHA-256 `904301d283ced730757729272bd55cda4da67e66f86cff135d74aac2fbf73e42`). It parses the *pinned candidate text*, not a recopy of the eight-head tables:

* Seven-head: exact integer-affine checks of all 4 bare-head, 5 five-head and 5 six-head displayed collisions, exhaustive target complements, symmetry and the final double hit. Separately checked all 5 Q=Y collisions.
* Eight-head: all **10** literal rows, **59** collision cells, all survivor columns, previously established Q dependencies, distinct symbolic P-members, branch separation and the final equality. The mathematical specialization argument above supplies the all-order logic; numeric samples alone would not.
* Independent Sardinas–Patterson enumeration: `n=4` has 455 layers, 134 UD and 276 anchor checks; `n=5` has 10,626 layers, 1,226 UD and 2,568 anchor checks. All UD cases satisfy the generalized row-packing inequality; an explicit non-UD four-cell layer violates it and is rejected.
* Independent exact-cover enumeration at `26<=n<=56` for all P sizes 4–7 and `|Q|>=5`: after anchor-directness pruning, 389 P sets remain (8, 40, 112, 229 respectively); all have no anchored Q tiling. These are finite controls, not the all-order proof. Direct positive tilings at n=60 and 1320 exist when the old Q anchors are deliberately dropped, confirming the anchor hypothesis is load-bearing.
* The `n=1320` divisor list and threshold were recomputed with integer arithmetic.

**Named imports not independently verified:** the historical reported executions of `frontier-20261028-zero-column-tradeoff-check.py` and `frontier-20261028-border-exact-one-replay.py`, including the latter's 48,400 propagation cases, 3,305 small comparison cases and 80 seeded controls; neither was executed as proof (the independent synthetic counts above are separate). The stronger historical lower-order bound mentioned in `seven-head...md:81` was not audited. The two pinned author checkers were read but their claimed historical outputs were not replayed. No independent-family, human, formal/kernel, or novelty/priority audit was performed; the current literature status of the overall completion problem was not established here.

**Scope conclusion:** These deductions neither construct a finite UD factor-complete extension nor prove that one exists. They do **not** rule out n=1320: the listed border sizes have merely survived necessary filters, not been shown feasible. No all-order nonexistence or original-problem resolution follows from this review.
