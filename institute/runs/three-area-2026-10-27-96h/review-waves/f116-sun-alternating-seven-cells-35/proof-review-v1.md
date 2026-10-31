# f116: proof review of the seven-cell alternating direct-P7 exclusion through 35 positions

Native clock observed immediately before this file was composed: **2026-10-28T19:49:03-0700 PDT**. Same-harness independent scientific review; not human, not independent-model-family, not formal/kernel, not novelty or priority clearance.

## 1. Binding manifest, pins, read order

Manifest `manifest-v1.json`, SHA-256 `45d6a1dd19ea3d528c71401327f6724e83524cbb43e902633a6a8fbb50e42818`, 4099 bytes, 61 LF (verified before reading). All seven inputs were hash-, byte- and LF-checked before being read completely, raw, in the declared order; every value matched.

| # | Role | Actual SHA-256 | bytes/LF |
|---|---|---|---|
| 1 | f81 correction (read first, before any orbit source) | `ec8e0d0ded1ede1701c3348ad50d83190679e330a1955d23d9afc1001376bf0a` | 13752/73 |
| 2 | orbit-induction / density ancestor | `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5` | 6917/53 |
| 3 | factorial terminal through 33 | `363205fefd1b34bde523523e87f9c981a0a45409f006c53391a46c4e29384186` | 5567/46 |
| 4 | exact quotient and seven-cell through 33 | `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f` | 8316/59 |
| 5 | seven-cell extension through 35 | `1a045426cd7715c63b795e57af6d0cd32dc65bf1fb7dd196e735cb4e444c4a5e` | 4676/25 |
| 6 | author quotient control (read, **not run**) | `bb126c1a8ae17c8649f1fc0c5d437cd96ee7891718d0865fe162850f166ff908` | 1237/32 |
| 7 | author sieve control (read, **not run**) | `5975e0b492c895adf84f101c513479018cebc70d5381d619a96dcc240b5e2ded` | 1094/30 |

Mandatory pre-source correction applied: `orbit-induction-v1.md:26` asserts `r+j>420`, false at `r=419, j=1` (equality); the repaired bound is `d_1=r+1>=420>7` and, for `2<=j<=6`, `r+j>=421>420>=7L_j`. This successor uses only Section 5 (density, lines 38-45) of that file; I verified that Section 5 does not depend on line 26. No frozen input was edited. Author scripts were read as documentation of what they check and were neither imported nor executed.

## 2. Verdict

| Input | FATAL | MAJOR | MINOR | Verdict |
|---|---:|---:|---:|---|
| 3. factorial terminal (t<=33) | 0 | 0 | 0 | Reconstructed; no defect found, conditional on the A_r import. |
| 4. quotient + seven-cell (t<=33) | 0 | 0 | 2 | Reconstructed; one scope-presentation and one expository MINOR; mathematics holds, conditional on the A_r import. |
| 5. extension (t=34,35) | 0 | 0 | 1 | Reconstructed; one false strict intermediate inequality (conclusion intact). |
| 2. density section only | 0 | 0 | 0 | Elementary count reconstructed and correct. |

**Overall: 0 FATAL, 0 MAJOR, 3 MINOR; not INCONCLUSIVE.** Exact claim verified, conditional on the single external import of Section 3: for every prime `r` that is not of the form `(q^d-1)/(q-1)` (`q` prime power, `d>=2`), every `1<=t<=35`, and `r >= max(419, 7*t!)` (equivalently `r+1>7t!`), the group `A_(r+t)` has no seven proper subgroups whose indices have pairwise gcd exactly 7; for each fixed `t` the set of such `r` is infinite with relative density one among primes. Not verified and not claimed: pairwise gcd `<=7` configurations, unrestricted Sun8, any `t>=36`, any `r` with `r+1<=7t!`, non-eligible primes, the source proof, novelty, or any historical hold.

## 3. Primary public source: exact statement, matching hypotheses, classification

Read directly at `https://arxiv.org/html/2307.13976v2#Thmtheorem2` (header: `arXiv:2307.13976v2 [math.GR] 13 Mar 2024`; Baumeister, Burness, Guralnick, Tong-Viet, *On the maximal overgroups of Sylow subgroups of finite groups*). The rendered body shows a line `Date: August 24, 2026`, inconsistent with the arXiv header; `[INFERENCE]` a render-time date artifact, not relied on.

**Theorem 2 (verbatim hypotheses).** `G` almost simple with socle `T`; `R` a Sylow `r`-subgroup of `G`; `r` an odd prime; `G/T` an `r`-group. Then `M(R)={H}` iff one of the listed cases holds; case **(i)(d)**: `G=T=A_n`, `n=r`, `r!=11,23`, `H=AGL_1(r) ∩ G`, and either `r=5` or `r` is not of the form `(q^d-1)/(q-1)` with `q` a prime power and `d>=2`.

**Matching to the packets' use.** `G=T=A_r` (so `G/T` trivial, an `r`-group), `r>=419` odd prime (so `r!=11,23` and `A_r` simple), `r` eligible by hypothesis. `|A_r|_r = r`, so the Sylow `r`-subgroup is `R=<r-cycle>`, and `AGL_1(r)` contains odd permutations (an `(r-1)`-cycle), so `|AGL_1(r) ∩ A_r| = r(r-1)/2` and `[A_r : AGL_1(r)∩A_r] = (r-2)!`. Consequence used (correctly) by the packets: every **proper** subgroup of `A_r` containing `R` lies in a maximal subgroup containing `R`, hence in `AGL_1(r)∩A_r`, so its index is divisible by `(r-2)!`. The source says nothing about `A_(r+t)`, `t>=1`; everything beyond degree `r` is the packets' own derivation, reconstructed in Section 4.

**Classification of the import: UNVERIFIED EXTERNAL, statement-matched, proof not replayed.** The alternating case is Proposition 4.2 of the source. For `n<=24` it is delegated to Magma (not reproduced; irrelevant here since `r>=419>=25`). For `n>=25`, Case 3 (`R` primitive, `n=r`) argues: `N_G(R)=AGL_1(r)∩G` is maximal (citing Liebeck–Praeger–Saxl [37]); by Burnside's theorem either `M(R)={N_G(R)}` or `R<L<G` with `L` 2-transitive almost simple; inspecting Guralnick [25] (*Subgroups of prime power index in a simple group*, 1983) with `n>=25` leaves only socle `L_d(q)` with `r=(q^d-1)/(q-1)`. `[INFERENCE]` [25] and [37] rest on the classification of finite simple groups, so the import is CFSG-dependent. I did not read [25] or [37]. Peer-review/publication status of the source was not determined (no web_search permitted) and is not claimed.

## 4. Independent reconstruction, step by step (line references to inputs 3-5)

Throughout `n=r+t`, `t<=35<r`, so `v_r(n!)=1`, Sylow `r`-subgroups of `A_n` have order `r` and are generated by `r`-cycles; an index `N` with `r∤N` forces `r | |H|`, so `H` contains a Sylow `r`-subgroup, conjugate to a fixed `R=<ρ>`; replace `H` by that conjugate (same index).

**(a) Index lower bound** (`seven-cell-p7-v1.md:19`). A proper `H<A_N`, `N>=5`, of index `k` gives a transitive action on `k` cosets with normal kernel; simplicity makes it faithful, so `N!/2 <= k!`, which fails for `k<=N-1` and `N>=3`. Hence `k>=N`. Correct.

**(b) Setwise-stabilizer index** (`seven-cell-p7-v1.md:21,31-33`; `factorial-terminal-33-v1.md:17`). For a `u`-subset `V` with `|U|=n-u>=2`, `S_U×S_V` contains a transposition, so `A_n` is transitive on `u`-subsets and `[A_n : Stab_{A_n}(V)] = C(n,u)`. Correct.

**(c) Transitive point-stabilizer descent** (`:21,41`; `:15`). If `H<A_(r+j)` is transitive and `x` is one of the `j>=1` points fixed by `ρ`, then `|H|=(r+j)|H_x|`, so `[A_(r+j-1):H_x]=[A_(r+j):H]`, `R<=H_x`, and `H_x` is proper (else `|H|=|A_(r+j)|`). Index, properness, `r`-freeness and `R`-containment are all preserved. Correct.

**(d) Exact alternating-block quotient, formula (1)** (`seven-cell-p7-v1.md:31-39`). `H<A_(r+j)` intransitive, `U` the `H`-orbit of `supp(ρ)`, `|U|=m=r+j-u`, `u>=1`, `B=(S_U×S_V)∩A_(r+j)=Stab(U)`, `K=H∩(A_U×A_V)`, `P=π_U(K)`, `L=K∩(1×A_V)=ker(π_U|_K)`, `h=[H:K]`. For `u=1`: `B=A_U`, `K=H`, `[A_(r+j):H]=(r+j)[A_U:H]` (`c=1`). For `u>=2`: `B={(σ,τ): sgn σ = sgn τ}` has order `2|A_U||A_V|`, so `h∈{1,2}`, `|K|=|P||L|`, and
`[A_(r+j):H] = C(r+j,u)·|B|/|H| = C(r+j,u)·2|A_U||A_V|/(h|P||L|) = C(r+j,u)·[A_U:P]·c`, `c=(2/h)|A_V|/|L| = u!/(h|L|)`.
`c` is an integer (`L<=A_V`, and `h=1` gives `2|A_V|/|L|`, `h=2` gives `|A_V|/|L|`) and `c·h|L| = u!`, so `c | u!`. The `[B:A_U×A_V]=2` step genuinely requires `u>=2` (for `u=1` the index is 1), which the packet handles separately. Correct. `R<=K` since `ρ` is even on `U` and trivial on `V`, so `ρ|_U ∈ P`.

**(e) `P` is transitive on `U`** (`:41`). `K ⊴ H` (index `<=2`) so `P=π_U(K) ⊴ π_U(H)`, which is transitive on `U`. The `P`-orbits are blocks permuted transitively by `π_U(H)` with `P` acting trivially on them, so their number is at most `[π_U(H):P] <= [H:K] <= 2` and they have equal size. Two orbits would each have size `|U|/2 < r` (as `|U| <= r+t < 2r`), impossible because `ρ|_U ∈ P` moves `r` points inside one orbit. Correct (see MINOR 3 for the elided step).

**(f) Iteration, disjoint windows, exact product (2)** (`:41-43`). From `H<A_(r+t)` containing `R`: while transitive, descend by (c) (index unchanged); at an intransitive stage at degree `r+j` with complement size `u`, apply (d): the factor `C(r+j,u)·c` has numerator `∏_{h=j-u+1}^{j}(r+h)`, i.e. the window `{j-u+1,…,j}`, and the continuation subgroup `P<=A_U` lives at degree `r+j-u`, so every later window lies strictly below `j-u+1`; windows are pairwise disjoint and decreasing. Termination: either some `P=A_U` (factor 1), or a proper subgroup of `A_r` containing `R` is reached (by `u=j` with `P<A_r`, or by descending to degree `r`), which by Section 3 contributes a factor divisible by `(r-2)!`. Hence every `r`-free index `N` satisfies **either** `N=∏_i C(r+j_i,u_i)c_i` exactly with `c_i | u_i!` and disjoint windows, **or** `(r-2)! | N`. Correct; the exactness (not mere divisibility) is what (h) needs, and the finite control below confirms it on 181 actual intransitive subgroups with observed `c∈{1,2,3,6,12}`.

**(g) No subgroup of index `7p`, `r<p<=r+t`** (`seven-cell-p7-v1.md:21-23`; `factorial-terminal-33-v1.md:15-19`; `thirty-five-p7-v1.md:13`). `7p` is `r`-free; descend by (c). Reaching degree `r` gives `(r-2)! | 7p`, impossible since `(r-2)! >= (r-2)(r-3) = 173472 > 7(r+35) = 3178 >= 7p` at `r=419` and the gap only widens. At the first intransitive stage, `C(r+j,u) | 7p`. For `2<=u<=35<=(r+j)-2`, unimodality gives `C(r+j,u) >= C(r+j,2) >= C(r+1,2) = 87990 > 7p`. For `u=1`: `r+j | 7p` with `7 < r+j <= r+t < 7r < 7p`, so `r+j=p`; the subgroup fixes the complementary point, so it is a subgroup of `A_(p-1)` of index `7p/p = 7 < p-1`, contradicting (a). Correct for all `t<=35`, `r>=419`.

**(h) At most ten primes of `|A_n|` in `[r-1, r+t]`** (`seven-cell-p7-v1.md:25`; `factorial-terminal-33-v1.md:25-37`; `thirty-five-p7-v1.md:9-11`). `r-1` and `r+odd` are even `>2`; candidates are `r` and `r+2k`, `1<=k<=E=floor(t/2)`. `3 | r+2k` iff `k ≡ r (mod 3)`, at least `floor(E/3)` such `k`, all `>3` hence composite. `E<=13`: `1+E-floor(E/3) <= 10` (equality at `E=13`). `5 | r+2k` iff `k ≡ 2r (mod 5)`; for `E>=14` the three smallest such `k` are `{2,7,12},{4,9,14},{1,6,11},{3,8,13}` for `r≡1,2,3,4 (mod 5)` (offsets `4,14,24; 8,18,28; 2,12,22; 6,16,26` as stated), consecutive members differ by 5 so their residues mod 3 are distinct, so at least two are not multiples of 3: `E=14,15,16` give `<= 9,9,10`. `E=17` (`t=34,35`): `k≡r (mod 3)` has exactly 6 solutions in `1..17` for `r≡1,2` (offsets `2,8,…,32` / `4,10,…,34`), so `<= 1+17-6-2 = 10`. All correct; my independent mod-15 sieve gives worst case exactly 10 (attained, e.g. `r ≡ 2 (mod 15)`, `E=17`), while the direct count of actual primes in `[r-1,r+t]` over all 2182 primes `419<=r<=20000` never exceeds 9.

**(i) No factorial terminal in a seven-pattern** (`seven-cell-p7-v1.md:27`; `factorial-terminal-33-v1.md:39-40`; `thirty-five-p7-v1.md:13`). If `F=(r-2)! | N_0`: `7^2 | F` (as `14<=r-2`) and every prime `<=r-2` divides `F`. For `i≠0`, `gcd(N_0,N_i)=7` forces `N_i=7a_i`, `7∤a_i`, no prime `<=r-2` divides `a_i`, `a_i>1` by (a); so every prime factor of `a_i` lies in `[r, r+t]` (`r-1` is not prime), each such prime exceeds `n/2`, so `v_q(n!)=1` and `a_i` is squarefree; the `a_i` are pairwise coprime. Six nonempty pairwise-disjoint supports inside at most ten primes force at least two singletons (`1+5·2=11>10`), at most one of which is `{r}`; the other gives an actual index `7p`, `r<p<=r+t`, contradicting (g). Correct for all `t<=35`.

**(j) Seven-cell necessity** (`seven-cell-p7-v1.md:45-47`; `thirty-five-p7-v1.md:17`). All seven indices are divisible by 7. For an `r`-free index, (i) excludes the factorial branch of (f), so `N=∏C(r+j_i,u_i)c_i` exactly. If no window contains a cell `h` with `7 | r+h`, then every `u_i<=6` (seven consecutive `r+h` cover all residues mod 7), each `C(r+j_i,u_i)` is an integer with 7-free numerator, and `c_i | u_i! | 720` is 7-free; so `7∤N`, contradiction. Correct. (Negative mutation C2 confirms that weakening `c_i | u_i!` to `c_i | (u_i+1)!` breaks this step at `u=6`.)

**(k) Distinct labels cannot share a cell** (`seven-cell-p7-v1.md:49-51`; `thirty-five-p7-v1.md:19`). If `h` lies in the window of `C(r+j,u)`, then `(r+h) | C(r+j,u)·u!`, and with `g=gcd(r+h,u!)` coprimality of `(r+h)/g` and `u!/g` gives `(r+h)/g | C(r+j,u)`; since `u! | t!`, `D_h := (r+h)/gcd(r+h,t!)` divides `C(r+j,u) | N`. Two labels sharing `h` give `D_h | gcd(N,N') = 7`, but `D_h >= (r+h)/t! >= (r+1)/t! > 7` by the hypothesis `r+1>7t!`. Correct (see MINOR 1 on the strict intermediate written in the extension). This is the **only** place the hypothesis `r+1>7t!` is used, and it is sharp at `(r,t,h)=(419,5,1)`: `(r+1)/gcd(r+1,5!) = 420/60 = 7`.

**(l) Pigeonhole** (`seven-cell-p7-v1.md:53`; `thirty-five-p7-v1.md:19`). At most one index is divisible by `r>7`, so at least six are `r`-free; each consumes at least one seven-cell by (j), and consumed cells are pairwise distinct by (k); but `{1,…,t}` contains at most `ceil(t/7) <= 5` cells for `t<=35`. Contradiction. Correct, and `35` is exactly where this argument stops: at `r=419, t=36` the cells `1,8,15,22,29,36` are six (mutation C1).

**(m) Eligible-prime density** (`orbit-induction-v1.md:38-45`, reconstructed, not merely accepted). Bad primes `<=x` of the form `q+1` (`d=2`) need `q` even prime power, `q=2^a`, at most `log_2 x` of them. For `d>=3`, `q^{d-1} <= (q^d-1)/(q-1) <= x` gives `q <= √x`, and `2^d-1 <= x` gives `d <= log_2(x+1)`, so at most `√x·log_2(x+1)` pairs. Chebyshev lower bound: for `p<=2m`, each term `floor(2m/p^a)-2floor(m/p^a) ∈ {0,1}` and vanishes once `p^a>2m`, so `p^{v_p(C(2m,m))} <= 2m` and `C(2m,m) <= (2m)^{π(2m)}`; with `C(2m,m) >= 4^m/(2m+1)`, `π(2m) >= (2m·log 2 - log(2m+1))/log(2m)`, hence `π(x) >> x/log x` by monotonicity. So `#bad(x)/π(x) = O(log^2 x/√x) → 0`; removing `11, 23`, primes `<419`, and (for fixed `t`) primes `<7t!` is a finite change. **Conclusion: for each fixed `t<=35`, infinitely many eligible `r` with `r>=7t!`, of relative density one; unconditional and elementary (no PNT import).** Finite illustration: `π(10^6)=78498`, bad primes `<=10^6`: 43 (ratio `5.5e-4`), of which 33 lie in `[419,10^6]` (first: `757,1093,1723,2801,3541,5113,8011,8191,…`; largest `830833`).

## 5. Findings

**MINOR 1 — false strict intermediate inequality.** `thirty-five-p7-v1.md:19` writes `(r+h)/gcd(r+h,t!) > (r+1)/t! > 7`. The first `>` is equality whenever `h=1` and `t! | r+1`: always at `t=1`, always at `t=2` (`r+1` is even), and at `t=3` when `6 | r+1` (e.g. `r=419`: `420/gcd(420,6)=70=(r+1)/3!`). Checked at `r=419,421,431,853`. The correct chain is `>=` then `>7` (as `seven-cell-p7-v1.md:50-51` states it); the conclusion `D_h>7` is intact. Also raised by a parallel same-harness reviewer; independently verified here. No edit to the frozen file.

**MINOR 2 — effective scope per `t` is not stated, and the sample primes cover only `t<=4`.** `seven-cell-p7-v1.md:3-5` and `thirty-five-p7-v1.md:3` state the hypothesis `r+1>7t!` honestly but nowhere translate it: it is `r >= 7·t!`, i.e. `r>=840` for `t=5`, `r>=5040` for `t=6`, `r>=35280` for `t=7`, `r>=2.54e6` for `t=9`, `r>=9.15e12` for `t=15`, `r>=7.23e40` for `t=35`. For the packets' own sample primes `419, 421, 431` the theorem instance covers exactly `t∈{1,2,3,4}`; the author controls (`seven-cell-p7-v1.md:57`, `thirty-five-p7-v1.md:25`) run the seven-cell/window lemma at these `r` for all `t<=35`, where for `t>=5` the hypothesis is false and the lemma run is not a theorem-instance check. Further, the hypothesis has no slack at `(r,t)=(419,5)` (Section 4(k)). Suggest adding the per-`t` table (Section 6) and labeling the `r=419, t>=5` runs as lemma controls only. Not a mathematical error.

**MINOR 3 — elided step in `P` transitivity.** `seven-cell-p7-v1.md:41` ("If it had two equal orbits…") uses without saying so that the number of `P`-orbits is at most `[π_U(H):P] <= 2` because `π_U(H)` permutes the `P`-orbits transitively while `P` fixes each. Valid; state it.

**No defect found** in (a)-(m) otherwise. The `f81`-identified `r+j>420` error in the ancestor is not load-bearing here.

## 6. Exact proof scope for each `t` and for fixed primes

Conditional on Section 3's import, the exclusion holds for `A_(r+t)` exactly when `r` is an eligible prime and `r >= max(419, 7·t!)`. Least eligible prime per `t` (from the control; primality deterministic by Miller–Rabin with bases `2..37` for `r < 3.19e23`, i.e. `t<=23`; for `t>=24` the listed `r` is a **probable** prime only, not certified):

| t | threshold `7·t!` | least eligible `r` | t | threshold `7·t!` | least eligible `r` |
|---:|---:|---:|---:|---:|---:|
| 1-4 | 7, 14, 42, 168 | 419 | 9 | 2540160 | 2540173 |
| 5 | 840 | 853 | 10 | 25401600 | 25401611 |
| 6 | 5040 | 5051 | 12 | 3353011200 | 3353011229 |
| 7 | 35280 | 35281 | 15 | 9153720576000 | 9153720576001 |
| 8 | 282240 | 282241 | 23 | 180964117172194836480000 | 180964117172194836480031 (last certified row) |

Rows 11, 13, 14, 16-22 and 24-35 are in `proof-control-v1.txt` (`t=35`: threshold `72332035764703014507666559362662400000000`, probable prime `…400000271`). Fixed primes: `r=419, 421, 431` → `t∈{1,2,3,4}`; `r=853` and `r=5003` → `t∈{1,…,5}`; `r=5051` → `t<=6`. For `t<=5` (seven) and `t=6` (eight) at small `r`, the corrected orbit-induction ancestor (f81) gives the complementary unconditional-in-`r>=419` statement; the seven-cell route is the one that reaches `t=35`. Not covered by anything reviewed here: `t>=36` (six cells fit; mutation C1), `r+1<=7t!`, repunit-form primes (e.g. `757, 1093, 8191, 65537, 131071, 524287`), pairwise gcd `<=7`, unrestricted Sun8.

## 7. Independent finite control (one observed run) and negative mutations

Reviewer-authored `proof-control-v1.py`, SHA-256 `4c4025fb92d5f6cc6b2e0810ab25f481fc8a0f0415dc750853e3bda8500e27cf`, 18664 bytes / 518 LF; standard library only, exact integers, permutation groups by explicit closure; author code neither imported nor run. Single run `python3 proof-control-v1.py proof-control-v1.txt`, Python 3.14.3, started `2026-10-28T19:47:37-0700`, ended `19:47:39-0700`, exit 0; receipt `proof-control-v1.txt`, SHA-256 `4eac36d6f8cb79b712e317964d9bfced2e352d7a9dfaf0509661f9295eedac27`, 6259 bytes / 65 LF.

- **Control A (nontrivial, actual subgroups):** 207 subgroups of `A_8` (191) and `A_9` (16) generated by a 5-cycle plus random even or block-stabilizer elements; 26 transitive (index preserved under point-stabilizer descent), 181 intransitive, each satisfying the exact formula `[A_n:H]=C(n,u)[A_U:P]c` with `c=u!/(h|L|) | u!`, `P` transitive on `U` and containing the 5-cycle. Observed profile `(u,h,|L|,c)`: `(1,1,1,1)×60, (2,1,1,2)×36, (2,2,1,1)×25, (3,1,1,6)×4, (3,1,3,2)×28, (3,2,1,3)×3, (3,2,3,1)×17, (4,1,2,12)×1, (4,1,12,2)×4, (4,2,4,3)×1, (4,2,12,1)×2` — `c≠1` and both `h` values occur, confirming the packet's "c may be any permitted integer" and the `2/h` factor. Deterministic witness `H=<ρ>×<(5 6 7)>` in `A_8`: index `1344 = 56·12·2`, `h=1, |L|=3`.
- **Control C:** all 2182 primes `419<=r<=20000`, `t<=35`: seven-cells `<=5` (max 5) and actual primes in `[r-1,r+t]` `<=10` (max 9 at `r=1277, t=30`); for `r∈{419,421,431,1009,10007}` and all `1<=u<=j<=35`: `(r+h)/gcd(r+h,u!) | C(r+j,u)` for every window cell and `7∤C(r+j,u)`, `u<=6`, for every cell-free window; no-7p inequalities at `r=419, t=35`; independent mod-15 sieve worst case 10; boundary witness `(419,5,1)`.
- **Control D:** repunit-density count at `10^6` (Section 4(m)); eligibility helper agrees on `419, 421, 431, 853` (eligible) and `5, 7, 13, 17, 31, 257, 307, 65537` (repunit form).
- **Control E:** per-`t` scope table (Section 6).
- **Negative mutations, all DETECTED:** A1 drop the `2/h` factor in `c` → wrong index on 72/72 `h=1, u>=2` samples; C1 claim `<=5` cells for `t=36..41` at `r=419` → fails at `t=36`; C2 weaken `c | u!` to `c | (u+1)!` on the cell-free window `{2,…,7}` at `r=419` → `7 | C(426,6)·7`; C3 tighten the sieve bound to 9 → fails (10 attained).

These are finite controls of the written lemmas; they do not prove the universal statement, do not replay the source, and enumerate no subgroup of any `A_(r+t)` with `r>=419`.

## 8. Dependencies and limits

Dependencies: (1) arXiv:2307.13976v2 Theorem 2(i)(d), statement matched, proof unverified, `[INFERENCE]` CFSG-dependent via [25],[37]; (2) standard Sylow, Lagrange, orbit-stabilizer, simplicity and order of `A_n` (`n>=5`), unimodality of binomials, elementary number theory. No PNT, no Sun7/R8, no coset-cover relaxation, no held or withdrawn body, no author contact, no external model, no web search. This review is same-harness and nonblind to the packets; it is not human, independent-family, formal/kernel, exhaustive-enumeration, prior-art, novelty, or historical-hold clearance. No frozen input was modified; artifacts written: `proof-review-v1.md`, `proof-control-v1.py`, `proof-control-v1.txt`.
