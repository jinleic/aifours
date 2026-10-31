# f116 independent same-harness arithmetic review

Native clock observed immediately before this review was written: **2026-10-28T19:39:05-0700 PDT**.

## Verdict and exact scope

**FATAL 0; MAJOR 0; MINOR 1** in the assigned arithmetic scope. Subject to the explicitly named degree-`r` classification and the stated elementary group facts, I independently derive the `t≤35` prime-support bound, factorial-terminal and seven-cell arithmetic, and exact block quotient below. I found one false intermediate strict inequality in the extension; replacing its first `>` by `≥` repairs it without changing the final `>7` conclusion. This is **not** an acceptance of the source proof, a human or independent-family review, a formal/kernel proof, a novelty claim, or a resolution of an unrestricted Sun problem.

The conditional statement has all of these hypotheses: prime `r≥419`, not a prime-power repunit `(q^d−1)/(q−1)` with `d≥2`; `1≤t≤35`; and the **strict** threshold `r+1>7t!`. The conclusion is the exclusion of seven proper subgroup indices of `A_(r+t)` with all pairwise gcds **exactly 7**. The separate density argument gives infinitely many such `r` for each fixed `t`; it does not remove the threshold. All uses of `r=419` below are endpoint bounds for inequalities independent of that threshold; they do not claim that 419 meets the threshold for large `t`.

**MINOR — false intermediate inequality.** `frontier-20261028-alternating-thirty-five-p7-v1.md:19` states

`(r+h)/gcd(r+h,t!) > (r+1)/t! > 7`.

The first strict comparison is false: for `t=1,h=1`, both sides are exactly `r+1`, for every `r`. What always holds is

`(r+h)/gcd(r+h,t!) ≥ (r+1)/t! > 7`.

That is enough for the stated collision and the claimed conclusion. The frozen source was not altered. The required earlier f81 correction is separate: at `r=419,j=1` the ancestor's `r+j>420` fails, while `d_1=420>7`; for `j≥2` the repaired bound in f81 applies. The present proof uses the density section of that ancestor, not its uncorrected inequality.

## Frozen inputs, reading order, and import boundary

I first verified the manifest's complete SHA-256 as `45d6a1dd19ea3d528c71401327f6724e83524cbb43e902633a6a8fbb50e42818` (4,099 bytes, 61 LF). Before opening the source texts, I computed the complete SHA-256, byte and LF counts for every listed input; all matched. I then read all seven inputs in the declared order, starting with the required f81 correction and only then the orbit ancestor:

| # | Role | Full SHA-256 | bytes | LF |
|---|---|---|---:|---:|
| 1 | f81 correction | `ec8e0d0ded1ede1701c3348ad50d83190679e330a1955d23d9afc1001376bf0a` | 13752 | 73 |
| 2 | density ancestor | `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5` | 6917 | 53 |
| 3 | factorial terminal | `363205fefd1b34bde523523e87f9c981a0a45409f006c53391a46c4e29384186` | 5567 | 46 |
| 4 | exact quotient and seven-cell | `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f` | 8316 | 59 |
| 5 | extension through 35 | `1a045426cd7715c63b795e57af6d0cd32dc65bf1fb7dd196e735cb4e444c4a5e` | 4676 | 25 |
| 6 | author quotient control | `bb126c1a8ae17c8649f1fc0c5d437cd96ee7891718d0865fe162850f166ff908` | 1237 | 32 |
| 7 | author sieve control | `5975e0b492c895adf84f101c513479018cebc70d5381d619a96dcc240b5e2ded` | 1094 | 30 |

The author code was read as required but neither imported nor executed. I directly checked the **statement**, not the proof, of Baumeister–Burness–Guralnick–Tong-Viet, [Theorem 2(i)(d)](https://arxiv.org/html/2307.13976v2#Thmtheorem2). For the eligible odd prime `r`, a specified Sylow `r`-subgroup of `A_r` has unique maximal overgroup `AGL_1(r)∩A_r`. Its order is `r(r−1)/2` and its index is `F=(r−2)!`; every proper overgroup of the Sylow subgroup lies in it. The source's proof, classification dependencies and any novelty or prior-art position remain imports. In particular the theorem is about `A_r`, not a claimed classification of `A_(r+t)`.

The other dependencies are Sylow theory, orbit–stabilizer and Lagrange, the order and simplicity of alternating groups in these degrees, the normalizer order, elementary binomial identities and elementary prime counting. The following arguments do not use the earlier held mathematical outcomes or turn finite controls into a general group proof.

## 1. Odd/even positions and the 3/5 residue sieve

Put `n=r+t` and `E=floor(t/2)≤17`. Since `r` is odd, `r−1` and each `r+(2k−1)` are even composites. Consequently every prime of `|A_n|` in `[r−1,n]` is either `r` or one of the **odd** candidates `r+2k`, `1≤k≤E`. Moving from `t=2E` to `t=2E+1` adds only an even composite and does not increase this candidate count. Each candidate is greater than 5.

For `E≤13`, among `E` consecutive values of `k` at least `floor(E/3)` have `r+2k≡0 (mod 3)`. Hence the possible-prime support including `r` has size at most `1+E−floor(E/3)≤10`.

For `14≤E≤17`, the first 14 offsets include all three entries of the row for `r mod 5`:

| `r mod 5` | three offsets giving multiples of 5 |
|---:|---|
| 1 | 4, 14, 24 |
| 2 | 8, 18, 28 |
| 3 | 2, 12, 22 |
| 4 | 6, 16, 26 |

Their pairwise differences are 10, so they occupy three distinct residues modulo 3: at most one was already excluded as a multiple of 3. Thus at least two further candidates are composite and the bound is `1+E−floor(E/3)−2≤10`. For `E=17`, in fact exactly six multiples of 3 occur: offsets `2,8,14,20,26,32` if `r≡1 (mod 3)`, and `4,10,16,22,28,34` if `r≡2`. Consequently at most `1+17−6−2=10` large primes remain. The count is a bound on **possible** primes, not an assertion that all survivors are prime.

The independent finite receipt checks all eight permitted classes `1,2,4,7,8,11,13,14 (mod 15)` for all 35 values of `t`, and all seven disallowed classes separately. A prime greater than 5 cannot have a disallowed residue, because it would be divisible by 3 or 5. Applying the reduced-residue upper bound without this hypothesis is genuinely unsafe: classes 0, 9, and 12 have a sieve upper bound 11 at `E=17`. The control's small prime representatives establish only the residue examples, not prime-power-repunit eligibility or the large factorial threshold.

## 2. The singleton argument and the actual `7p` obstruction

Assume for contradiction that seven actual proper-subgroup indices `N_0,…,N_6` have pairwise gcd 7 and `F=(r−2)!` divides `N_0`. Simplicity of `A_n` implies any proper subgroup has index at least `n>7`: its coset action is faithful, and embedding `A_n` into `S_d` with `d<n` is impossible by orders. Thus `N_i=7a_i` with `a_i>1`. Since `F` contains 7² and every prime at most `r−2`, `gcd(N_0,N_i)=7` forces every prime of each `a_i` to lie in `[r−1,n]`; the even `r−1` is composite, so all such primes are at least `r`. Also `gcd(a_i,a_j)=1` for `i≠j`.

Every prime `p≥r` in `|A_n|` is greater than `n/2`, because `t≤35<r`; hence it has valuation one in `n!/2`. All six `a_i` are squarefree with nonempty pairwise-disjoint prime supports. The sieve gives at most ten supporting primes. If at most one support were a singleton, the six supports would require at least `1+5·2=11` primes. Therefore at least two are singletons; disjointness allows at most one singleton `{r}`, so another is `{p}` with `r<p≤n`. Its actual index is `7p`.

That index cannot occur. An index `7p` is `r`-free, so by Sylow we may conjugate the subgroup to contain an `r`-cycle `R`. At a transitive stage `A_N`, pass to the stabilizer of a point fixed by `R`; it remains proper, still contains `R`, and has the same index. If the process reaches `A_r`, the imported source forces `F | 7p`. This is impossible since

`F ≥ (r−2)(r−3) > 7(r+35) ≥ 7p`.

Otherwise at the first intransitive degree `A_(r+j)`, the orbit containing the `r` moved points has a complement of size `1≤u≤j≤t`, and its set-stabilizer index `B=binom(r+j,u)` divides `7p`. If `u≥2`, then `u<(r+j)/2` and

`B ≥ binom(r+1,2) > 7(r+35) ≥ 7p`,

again impossible. If `u=1`, then `B=r+j` is a divisor of `7p` strictly between 7 and `7p`, so `r+j=p`. The subgroup fixes the complementary point and consequently has index 7 in `A_(p−1)`, contradicting the minimum-index fact above. Thus no P7 index can be divisible by `F`.

Both numerical inequalities hold uniformly for `r≥419`: at 419 the respective margins `binom(r+1,2)−7(r+35)` and `(r−2)(r−3)−7(r+35)` are 84,812 and 170,294; when `r` increases by one they increase by `r−6` and `2r−11`. These inequalities do not use `r+1>7t!`.

## 3. Exact alternating-block quotient, including `u=1`

Consider an actual intransitive `H≤A_(r+j)` containing `R`. Let `U` be the orbit containing the moved points of `R`, let `|U|=m=r+j−u`, and let `|V|=u≥1`. The alternating set stabilizer `B=(S_U×S_V)∩A_(r+j)` has index `binom(r+j,u)`.

For `u≥2`, set `K=H∩(A_U×A_V)`, `P=π_U(K)`, `L=K∩(1×A_V)` and `h=[H:K]`. The common sign map gives `h∈{1,2}`, while the projection kernel identity gives `|K|=|P||L|`. Since `|B|=m!u!/2`, direct cancellation yields the **integer exact equality**

`[A_(r+j):H] = binom(r+j,u) [A_U:P] c`,

`c = u!/(h|L|) = (2/h)(|A_V|/|L|)`.

Here `L≤A_V`, so `|L|` divides `u!/2`; with `h=1` or `2`, `h|L|` divides `u!` and therefore `c` is an integer dividing `u!`. This includes `u=2`, where `A_V` is trivial. If `u=1`, the set stabilizer is `A_U`, `K=H`, `P=H`, and the same display holds with `c=1`; no fictitious `|A_1|=1!/2` is used.

The projection `P` is transitive on `U`: the image `Q` of `H` is transitive, `P` is normal in `Q` with `[Q:P]≤2`, and its orbits have equal size and number at most two. Two orbits would have size `m/2<r`, impossible because `P` contains the `r`-cycle. If `P=A_U`, the factorization terminates. If `P` is proper, continue with `P`, using transitive fixed-point descents as needed; the residual index is an integer divisor of the initial one, so remains `r`-free. Degrees decrease, and the only possible proper terminal at degree `r` puts `F` in the initial index, which Section 2 excludes in a P7 pattern. Hence each `r`-free P7 index has a finite **exact** product of binomials and their respective factors `c_i|u_i!`; the positions used at each intransitive step form the consecutive window `[j_i−u_i+1,j_i]` and all subsequent windows lie lower.

## 4. Seven-cell necessity and arbitrary-window cancellation

A cell `h∈{1,…,t}` is a seven-cell when `7|(r+h)`. If a chain has no seven-cell, every one of its windows has length at most 6, because any seven consecutive integer positions include one such cell. In a window `[j−u+1,j]`,

`binom(r+j,u) = (∏_(h=j−u+1)^j (r+h))/u!`.

Both numerator and denominator are 7-free, as is every integer divisor `c` of `u!`. Therefore the whole chain product is 7-free. Every index in a seven-pattern is divisible by 7, so every `r`-free label must consume at least one seven-cell. **This is only a necessity:** a window can contain a seven-cell while its binomial is 7-free because a factor 7 can cancel against `u!`; the receipt includes an exact example.

Now fix an arbitrary window of length `u≤t` and any cell `h` in it. Let `a=r+h`, `D=u!`, and write the other numerator factors as `M`. Since `D` divides `aM`, setting `g=gcd(a,D)` and cancelling the coprime `a/g` and `D/g` shows

`a/gcd(a,D) | binom(r+j,u)`.

Because `u!|t!`, `gcd(a,u!)` divides `gcd(a,t!)`; hence the uniform integer

`q_h = (r+h)/gcd(r+h,t!)`

also divides that binomial and thus the full index. Moreover

`q_h ≥ (r+1)/t! > 7`.

This is valid for **every** window containing `h`; it does not assert the generally false stronger divisibility `r+h | binom(r+j,u)`. If two distinct labels use the same cell, their index gcd is at least the common divisor `q_h>7`, impossible. Thus different labels consume different seven-cells.

At most one of the seven indices is divisible by the prime `r>7`; otherwise their gcd would be at least `r`. At least six are `r`-free and therefore need six distinct seven-cells. But any `t≤35` consecutive positions contain at most `ceil(t/7)≤5` seven-cells (exactly five when `t=35`). This is the required contradiction, conditional on the degree-`r` source import and stated group facts.

## 5. Fixed-`t` infinitude is separate

The density ancestor's elementary count can be reconstructed independently. A bad odd prime with repunit exponent `d=2` has `q+1` odd, so the prime power `q` is a power of 2: there are `O(log x)` such values below `x`. For `d≥3`, `q≤sqrt(x)` and `d≤1+log_2 x`, giving at most `O(sqrt(x) log x)` values even when all integer bases are overcounted. The central-binomial estimate `binom(2m,m)≥4^m/(2m+1)` and `binom(2m,m)≤(2m)^π(2m)` gives `π(x)≫x/log x`; thus bad primes have relative density zero. Removing the finitely many small exceptions does not change this. For any **fixed** `t`, the excluded interval `r+1≤7t!` is finite, so infinitely many eligible primes satisfy the threshold. This is not a claim that any particular sample prime meets the `t=35` threshold.

## 6. One observed independent finite control and mutation receipt

I wrote and ran `arithmetic-check-v1.py` **once**, with assertions enabled; it exited 0. It uses only Python standard-library exact integer arithmetic and explicit permutation closure, and does not import or call either author script. The program SHA-256 is `f52fe528a5e496362c7073c845b553928be402fcc418bad02be0a559a3c6793e`; its exclusive-create `arithmetic-receipt-v1.json` SHA-256 is `8242f653fce096d402501b9135ca9a671d4b535b3fd3e8e920fe8a6a6df4090d`. The run clock was observed at 19:38:14 PDT and the receipt-write clock at 19:38:16 PDT.

- The sieve controls cover `8×35=280` allowed and `7×35=245` disallowed residue/`t` cases, with parity-paired `t` checked. The ordered six-support size enumeration has 210 feasible patterns using at most ten primes; the minimum singleton count is two. Eleven primes admit the one-singleton pattern `(1,2,2,2,2,2)`.
- Seven synthetic odd integers `r=7·35!+delta`, one per residue modulo 7, **all satisfy** `r+1>7·35!`. They are not claimed prime. Across all `t≤35` the control checks 54,390 arbitrary windows, 516,705 individual cell-cancellation divisibilities, the at-most-five cell count, and the 7-free no-cell implication. Of 42,350 windows containing a seven-cell, 19,775 binomials are nevertheless 7-free and 22,575 are divisible by 7, demonstrating the one-way nature of the implication.
- Seven small explicitly generated alternating-block subgroups include `u=1` and `u=2`, both `h=1,2`, nontrivial kernels, and proper transitive projections. With notation from Section 3:

  | subgroup, `(m,u)` | `|H|` | `h` | `|P|` | `|L|` | `c` | actual index |
  |---|---:|---:|---:|---:|---:|---:|
  | `A5×A4`, (5,4) | 720 | 1 | 60 | 12 | 2 | 252 |
  | full sign-matched block, (5,4) | 1440 | 2 | 60 | 12 | 1 | 126 |
  | `D5×C3`, (5,4) | 30 | 1 | 10 | 3 | 8 | 6048 |
  | coupled `D5/C3` extension, (5,4) | 60 | 2 | 10 | 3 | 4 | 3024 |
  | `A5×A2`, (5,2) | 60 | 1 | 60 | 1 | 2 | 42 |
  | sign-matched, (5,2) | 120 | 2 | 60 | 1 | 1 | 21 |
  | `C5` with singleton block, (5,1) | 5 | 1 | 5 | 1 | 1 | 72 |

  `D5` here is the order-10 dihedral group. Each row is derived from actual generated permutations and its index agrees with the exact quotient; it is a finite sanity check, not a classification of all subgroups.
- Mutation controls catch omission of the 5-sieve (a possible-support bound of 12), claiming the full cell always divides its binomial, reversing the seven-cell implication, allowing a quotient factor `c=7` when `u=1`, using eleven rather than ten supporting primes, and applying the reduced-residue bound to disallowed classes. At the boundary `r+1=7t!` with synthetic `t=7`, the uniform divisor can equal 7, so this proof cannot simply replace the threshold `>` by `≥`. This is a limitation of the argument, not an actual subgroup counterexample. The false strict intermediate in the author extension is also directly caught at `t=h=1`.

**Limitations:** these exact controls sample arithmetic and small groups only. They do not enumerate general alternating subgroups, replay or verify the public classification proof, certify independent-family or human review, establish historical novelty, or change any held/withdrawn result. No external model, paid API, author contact, Git action, publication, or live-infrastructure change was used.
