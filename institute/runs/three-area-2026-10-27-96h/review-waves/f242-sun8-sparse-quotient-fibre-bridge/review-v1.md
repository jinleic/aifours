# f242 sparse-quotient fibre bridge: independent same-harness review

**Scope and result.** For the mathematical claims specified below, I found **0 F / 0 M / 0 m / 0 mathematical INCONCLUSIVE** at the stated hypotheses, with one explicitly imported, already-adopted f151 support criterion for the A8 application. Two historical/provenance assertions are **INCONCLUSIVE**, as separately identified below; neither is a premise. This is a **same-harness** review, not human review, independent-model-family review, formal or kernel verification, or novelty verification. **No global Sun8 claim, f184/f188 result, or conditional assembly is adopted.** The theorem remains conditional on the named kernel and quotient hypotheses.

Native `/bin/date` observed before composing this review: **2026-10-29T14:44:48-0700 PDT**. It is a clock observation, not an asserted creation time.

## Read and measurement record

1. I first opened the complete dispatched `manifest-v2.json`; I did not open v1. Before opening any declared input body I used `shasum -a 256` and `wc -cl` on the v2 manifest and all five inputs. The manifest is 4,994 bytes, 58 LF, SHA-256 `c6d2665185d1c81bd82d84cb9e845792ea3f5aaa76aabb4bf75726eee1804cb8`; it matches assigned prefix `c6d2665185d1`. Every declared byte count, LF count and hash matched:

   | Input, in manifest order | Bytes | LF | SHA-256 |
   |---|---:|---:|---|
   | `math-6-sun8-source-free-support-criteria-parent-v1.md` | 6,429 | 30 | `2ad5691a705089a6d724b2c9f21c075d76d31ddc471448abaa11240bc8d6637f` |
   | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | 6,883 | 56 | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` |
   | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | 3,056 | 11 | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` |
   | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | 3,164 | 10 | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` |
   | `frontier-20261029-sparse-quotient-fibre-bridge-v1.txt` | 9,645 | 175 | `406c41136f828891b76b61d0a75b406544d363c65035f4411e324e13ee84bc69` |

2. After these measurements and before the declared source bodies, I opened the mandatory administrative `memory://root/memory_summary.md` and `skill://independent-snapshot-review`; no mathematical premise or external-model procedure was taken from either. The manifest-first rule was followed; consequently the administrative memory summary was not the first read. The skill's separate external-model review procedure was not invoked, consistently with this assignment's same-harness and no-external-model constraints.
3. I then displayed every declared input, completely, in manifest order and in raw windows of at most 15 lines: f151 `1-15,16-30`; arithmetic overlay `1-15,16-30,31-45,46-56`; repeated-unit overlay `1-11`; cardinality overlay `1-10`; target `1-15,16-30,31-45,46-60,61-75,76-90,91-105,106-120,121-135,136-150,151-165,166-175`. Each last line was displayed. No mathematical reasoning preceded completion of these displays. No linked source bodies, v1 manifest, held material, sibling reviews, author code or external sources were opened or imported.
4. A reviewer-owned finite control was written and run only after all declared reads; its receipt appears below. Apart from the disclosed administrative reads/order and the limited historical INCONCLUSIVE findings, there was no deviation from the assigned mathematical and source scope.

## Per-claim dispositions

`0/0/0/0` means respectively F=0, M=0, m=0, INCONCLUSIVE=0 for the mathematical claim as stated, with the reasons and any import given in the reconstruction below. It is not an adoption of an unrestricted conclusion.

| Target claim | Verdict | Reason |
|---|---|---|
| Lines 8–18: definitions, repetitions, vacuity, and `J_T <= s` implying `B_T <= s` for `s >= 1` | 0/0/0/0 | A disjoint family of at least two nonempty cosets cannot include a whole-group coset; the index-only condition therefore applies to all its subgroup labels. Repetitions are essential. |
| Lines 20–30: general bridge and Sun8 corollary | 0/0/0/0 | The index, counting, and same-fibre argument below work for arbitrary groups and normal kernels, including `s=0`. The corollary uses exactly `r=5,s=2,T=7`. |
| Lines 33–45: all indices finite, product identity and gcd inheritance | 0/0/0/0 | The maps of left coset sets and finite index multiplication give `n_i=a_i b_i`; both `a_i` and `b_i` divide `n_i`. |
| Lines 43–54: at most `s` proper images; common fibre and its left-coset orientation | 0/0/0/0 | Repeated images count as repeated labels. Right translation by one common `t^{-1}` preserves disjointness, and conjugation by `t` is required. |
| Lines 61–80: order, point stabilizers, Sylow-p facts, generation, and proper-subgroup dichotomy in `PSL_2(F_p)` | 0/0/0/0 | The elementary matrices and generation are proved below; ordinary finite-group Sylow is an explicit import, not subgroup classification. |
| Lines 79–90: `J_7 <= 2`, arbitrary extensions, and the infinite rational-kernel example | 0/0/0/0 | The two index colours have gcd divisible by `p` or `p+1`; the rational group is divisible and has no proper finite-index subgroup. |
| Lines 92–100: f151 finite-kernel criterion and the A8 example | 0/0/0/0, **conditional on the stated f151 disposition** | The displayed f151 criterion gives `B_7 <= 5` at `k=0`; its stated A8 application gives the minimum-index hypothesis. No linked proof body or further alternating-group statement is imported. |
| Lines 103–120: failure of `B_7 <= 2`, even `J_7 <= 2`, to imply 3-Helly | 0/0/0/0 | The three explicit actual left cosets are pairwise intersecting and have empty triple intersection, by the nonsquare calculation below. |
| Lines 121–145: triangle's index restriction, non-implications, and remaining global gap | 0/0/0/0 | Every triangle index is `p+1>7`, so this triangle is not a low-gcd counterconfiguration. Repeated small-index subgroups invalidate all finite `J_7` bounds; no unrestricted kernel bound follows. |
| Lines 103–105: what an earlier independently written bridge required | **INCONCLUSIVE**, historical and not a mathematical premise | That earlier bridge is not an input and was not opened. The present explicit example independently proves the logical non-implication without relying on the earlier bridge. |
| Lines 1–3 and 149–167: author clock, claimed prior reading/history and historical process status | **INCONCLUSIVE**, provenance/status only | I did not observe those historical events or inspect their records. They are not used in this review. The author text's own stated non-adoption boundaries are respected. |
| Mandatory overlays: two arithmetic corrections, repeated-unit error and explicit A7 example | 0/0/0/0 for the explicit comparisons and A7 construction only | Independently checked below. Neither other linked bodies nor their source-conditional conclusions are adopted. |

## Independent reconstruction

### Definitions, index identity, and the fibre theorem

Throughout, `T>=2`, `r>=1`, and `s>=0` are integers; `Q=G/N`, `pi:G->Q`, and all subgroup indices used are finite. `B_T(X)<=r` concerns actual pairwise-disjoint left cosets; `J_T(X)<=s` concerns any `s+1` proper subgroup **labels**, including repeated labels, without a disjointness assumption. For `s=0`, its definition is exactly the absence of proper finite-index subgroups. If one proper subgroup has index `d<=T`, then repeating it `s+1` times violates `J_T<=s` for every finite `s`: for `s=0` there is no possible pair, and for `s>=1` every pair has gcd `d`. Also, in any family of at least two disjoint left cosets no subgroup can be all of `X`; thus `J_T<=s` implies `B_T<=s` for `s>=1`.

Assume, for contradiction, `r+s+1` pairwise-disjoint actual left cosets `C_i=g_i U_i` have `gcd(n_i,n_j)<=T` for every distinct pair, where `n_i=[G:U_i]`. Write `V_i=pi(U_i)`, `K_i=U_i cap N`, `a_i=[Q:V_i]`, and `b_i=[N:K_i]`. Normality makes `N U_i` a subgroup and `pi^{-1}(V_i)=N U_i`; hence `a_i=[G:N U_i]` is finite. The map `n K_i -> n U_i` is a bijection from the left cosets of `K_i` in `N` to those of `U_i` in `N U_i`, so `b_i=[N U_i:U_i]` is finite. Ordinary coset index multiplication, requiring neither `U_i` normal nor a finite ambient group, yields

`n_i=[G:N U_i][N U_i:U_i]=a_i b_i`.

Thus `gcd(a_i,a_j)` and `gcd(b_i,b_j)` each **divide** `gcd(n_i,n_j)` and are at most `T`. If more than `s` of the `V_i` were proper, take `s+1` of their labels: `J_T(Q)<=s` would force a pair of their indices with gcd greater than `T`, a contradiction. This counting remains valid when the `V_i` are equal; for `s=0` even one proper label is forbidden. Therefore at least `(r+s+1)-s=r+1` labels have `V_i=Q`.

Choose any `q in Q` and one lift `t in G`. For each of those labels `pi(C_i)=pi(g_i)V_i=Q`, so choose `x_i in C_i cap Nt`. Because `x_i` and any other `y in C_i` satisfy `y=x_i u` for a unique `u in U_i`, the condition `y in Nt` is exactly `pi(u)=1`, i.e. `u in K_i`. Hence `C_i cap Nt=x_i K_i`, and

`(C_i cap Nt)t^{-1}=(x_i t^{-1})(t K_i t^{-1})`.

Here `x_i t^{-1} in N` and, by normality, `t K_i t^{-1}<=N`; its index in `N` is `b_i` because conjugation by `t` is an automorphism of `N`. The same right translation is a bijection on `G`, so the resulting `r+1` left cosets in `N` remain pairwise disjoint. Their index gcds remain at most `T`, contradicting `B_T(N)<=r`. This proves `B_T(G)<=r+s`. It considers the entire original family to force the count, then selects `r+1` actual fibres; it does **not** assume all images are surjective. Taking `T=7,r=5,s=2` gives the named eight-coset conclusion under its two hypotheses.

### Elementary proof of the PSL2 quotient statement

Fix an odd prime `p>7`, write `F=F_p`, and let `P=PSL_2(F)`. The first column of a matrix in `SL_2(F)` can be any of `p^2-1` nonzero vectors. For each, the determinant-one condition is a nonzero linear equation in the second column and has `p` solutions. The distinct scalar matrices `I,-I` form the kernel used to define the projective quotient, so `|P|=p(p^2-1)/2` and the p-part of this order is exactly `p`.

Let `P` act on `F union {infinity}` by `[[a,b],[c,d]]:x -> (a x+b)/(c x+d)`, using infinity when the denominator vanishes and `infinity -> a/c` for `c!=0`. The action is transitive: `[[x,-1],[1,0]]` sends infinity to `x`, and the identity fixes infinity. Matrices fixing infinity have `c=0` and are exactly `[[a,b],[0,a^{-1}]]`; after quotienting by `+/- I`, their stabilizer `B_infinity` has `p(p-1)/2` elements and index `p+1`. Likewise the stabilizer of 0 is lower triangular.

Define `U(t)=[[1,t],[0,1]]` and `L(t)=[[1,0],[t,1]]`. Their projective images have order `p` as subgroups and are respectively normal in the infinity and 0 stabilizers: triangular conjugation sends `U(t)` to `U(a^2 t)` and `L(t)` to `L(a^{-2}t)`. Since each stabilizer has p-part `p`, ordinary Sylow conjugacy implies these normal order-p subgroups are the unique Sylow-p subgroups of their stabilizers. Also, any projective action kernel fixes infinity and 0 and is represented by a diagonal matrix; fixing 1 makes `a^2=1`, so its representative is `+/- I`. Thus the projective description has no hidden additional kernel.

The following explicitly proves the needed generation, without subgroup classification. For every nonzero `a`,

`W(a)=U(a)L(-a^{-1})U(a)=[[0,a],[-a^{-1},0]]`,

and `W(a)W(1)^{-1}=D(a)=diag(a,a^{-1})`. If `M=[[a,b],[c,d]] in SL_2(F)` has `a!=0`, then

`M=L(c/a) D(a) U(b/a)`.

If `a=0`, then `c!=0` by the determinant equation, and `U(1)M` has nonzero upper-left entry; the preceding decomposition and `U(1)^{-1}` handle `M`. Therefore the upper and lower unipotents generate all `SL_2(F)` and hence `P`. No maximal-subgroup classification or simplicity theorem is used.

Let `H<P` have index prime to `p`. By Lagrange and Sylow, `H` contains a subgroup of order `p` and, after conjugating `H` in `P`, contains `U_infinity`. If this conjugated `H` does not fix infinity, choose `g in H` sending infinity to a finite `y`, and left-multiply by `U(-y)`; call the result `k`. Then `k(infinity)=0`, and `k U_infinity k^{-1}` is an order-p subgroup of the stabilizer of 0. By uniqueness it is `U_0`. Thus `H` would contain both unipotent subgroups, hence all of `P`, contradicting properness. Consequently each proper `H` whose index is prime to `p` lies in a conjugate of `B_infinity`, and its index is a multiple of `p+1` by index multiplication.

For any three proper subgroup labels, either at least two indices are divisible by `p`, or at least two are prime to `p`. The first pair has gcd at least `p>7`; the second has gcd at least `p+1>7`. This proves `J_7(P)<=2`, including repeated labels. The two cases are both necessary to the argument; one must not assert that all proper-subgroup indices are multiples of `p+1`.

### Applications and Helly obstruction

The quotient result and the bridge give `Sun8(G)` for **any** extension with quotient `PSL_2(F_p)`, `p>7`, and kernel satisfying `B_7(N)<=5`; no splitting or finite-kernel premise is needed. For the explicit infinite example, take `N=(Q,+)` with `Q` the rational numbers. Every subgroup is normal. If `H<=Q` has finite index `d`, the finite quotient `Q/H` has order `d`, so `d y in H` for every rational `y`. Given any rational `x`, divisibility gives `x=d y`, hence `x in H` and `H=Q`. Therefore `N` has no proper finite-index subgroup and `B_7(N)<=1`, hence also `B_7(N)<=5`. The direct product `Q x PSL_2(F_p)` is infinite and satisfies the hypotheses.

The only nontrivial adopted mathematical import is the f151 disposition's **stated** finite-group criterion: when `mu(N)>=8`, a family of at least two disjoint cosets with all index gcds at most 7 has size at most `k+5`, where `k` counts distinct prime divisors of `|N|` greater than 7. At `k=0`, six such cosets are impossible, so `B_7(N)<=5`. The same disposition explicitly states its A8 application and `mu(A8)>=8`. Independently, `|A8|=8!/2=20160=2^6 3^2 5 7`, so `k=0`. Thus any, not necessarily split, extension with kernel A8 and this quotient satisfies Sun8 **conditional on that adopted disposition**. I do not import f151's linked bodies or any unreviewed alternating result.

For the non-Helly example, squaring on `F_p^*` has exactly `(p-1)/2` images: `a^2=b^2` implies `a=+/-b`, with the two values distinct. Select any nonsquare `z`. For points `x,y`, the set `E(x,y)={h in P:h(x)=y}` is a left coset of the stabilizer of `x`: if `g(x)=y`, it is `g Stab(x)`. Its index is `p+1` by transitivity. Put

`A=E(infinity,infinity)`, `B=E(0,0)`, and `C=E(1,z)`.

The identity lies in `A cap B`. `U(z-1)` fixes infinity and maps 1 to `z`, so lies in `A cap C`. `L(z^{-1}-1)` fixes 0 and maps 1 to `1/(z^{-1})=z`, so lies in `B cap C`. An element of `A cap B` is represented by `D(a)` and acts by `x -> a^2 x`; it cannot carry 1 to the nonsquare `z`. Therefore the triple intersection is empty. This independently proves that even `J_7<=2` (and hence `B_7<=2`) does not imply quotient 3-Helly. Each of these three indices is `p+1>7`, so this witness has pairwise index gcd `p+1`, **not** the low-gcd pattern of a Sun8 counterconfiguration; the example says nothing about whether such a non-Helly pattern can occur under those additional constraints.

### Mandatory overlay checks

For positive `t`, `1<=h<=t`, and `r+1>7t!`, the denominator `gcd(r+h,t!)` is at most `t!` and the numerator is at least `r+1`, giving `(r+h)/gcd(r+h,t!) >= (r+1)/t! > 7`. The first comparison can be equality: take `t=h=1,r=7`. For the second correction, at `r=419,j=1` one has `r+j=420`, not `>420`; for `j=2,...,6`, `r+j>=421>420` and `lcm(1,...,j)<=60`, so `(r+j)/lcm(1,...,j)>7`. This verifies only the displayed arithmetic, not any linked source's other hypotheses.

Repeated units are pairwise coprime regardless of how many there are. Independently, in the natural action of `A7`, let `H_i=Stab(i)`. A 3-cycle sends any `i` to any other point, so the action is transitive and each `H_i` has index 7. The `H_i` are distinct: for `i!=j`, a 3-cycle supported away from `i` and moving `j` lies in `H_i` but not `H_j`. Choose even `g_i` with `g_i(i)=1`; then `g_i H_i={g in A7:g(i)=1}`. Each `g` has a unique preimage of 1, so these seven left cosets are disjoint and partition `A7`, with every pair of indices having gcd 7. The same subgroup may also be repeated as seven index labels. This disproves the unqualified seven-index exclusion, including its distinct-subgroup and seven-disjoint-coset variants, but gives no eight-disjoint-coset counterexample and settles no additional source-specific P7 definition.

## Reviewer-owned bounded exact controls

Native clock before writing the control: **2026-10-29T14:43:29-0700 PDT**. The independently written standard-library integer script `reviewer-controls-v1.py` has SHA-256 `f612580337622db93fe0b3fdf8bb272f0ff8f49f5b001ec04524c862fd7123a2`. `/bin/date` immediately before the bounded run and script hash observation: **2026-10-29T14:43:58-0700 PDT**; `/bin/date` after it: **2026-10-29T14:44:02-0700 PDT**. It was run once with a 120-second tool deadline and exited **0**. A deadline/cap outcome would be UNKNOWN rather than an exclusion. No author script was run, compiled, or imported.

* In `S4` with `N=A4`, `U` the subgroup fixing one point, `K=N cap U`, a four-cycle `t`, and a transposition `x in U cap Nt`, the group/kernel/subgroup/intersection orders were `24/12/6/3`. The three elements of the translated fibre equal the correctly conjugated left coset. Both intended negative mutations—omitting conjugation and reversing its orientation—produced unequal sets, for precisely the predicted reason.
* For `p=11,13`, direct exact enumeration gave projective orders and upper/lower generated orders `660,1092`; point stabilizer orders `55,78`, indices `12,14`, respectively. With nonsquare `z=2`, the three pairwise intersection sizes were `[5,5,5]` and `[6,6,6]`, while each total intersection had size 0. Replacing the nonsquare by the square 4 produced a total intersection of size 1 in each case. Replacing the correct lower entry `z^{-1}-1` by `z-1` sent 1 to 6 and 7 rather than to 2, respectively.
* The same finite controls constructed proper matrix subgroups with indices `110,156`, divisible by `p` but not by `p+1`; their gcd with the respective point index is 2. These intended negatives refute the oversimplification that every proper index is a multiple of the point-stabilizer index. They are finite examples, not a classification or a proof for every prime.
* For `C2`, distinct-only quantification over its one proper subgroup is vacuous for two labels, whereas permitted repetition gives index pair `(2,2)` with gcd 2; the script checked repetitions for `s=0,...,10`. The written repetition argument above covers every finite `s`, including `s=0`.

## Imports and remaining gap

Imports: basic finite-set coset/index multiplication, Lagrange, ordinary Sylow existence/conjugacy, elementary prime-field arithmetic, and exactly the stated f151 finite support criterion and its explicit A8 minimum-index application. The 2x2 order, point stabilizers, unipotent normality and generation are reconstructed above rather than imported. No author PASS, author solver/checker/receipt, unreviewed source statement, author contact, external search/model/API, or sibling result is a premise.

The general bridge is conditional, not a proof that arbitrary kernels satisfy `B_7<=5` or arbitrary quotients have finite `J_7` bounds. It does not resolve a low-gcd non-Helly projected configuration, the unrestricted original Sun8 problem, source/book equivalence, an all-alternating or all-simple statement, priority, or novelty. No f184/f188 result, conditional assembly, or global Sun8 claim is adopted.
