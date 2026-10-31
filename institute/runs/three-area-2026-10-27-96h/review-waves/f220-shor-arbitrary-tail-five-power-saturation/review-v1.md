# f220 independent same-harness written review

Native clock observed immediately before writing: `2026-10-29T13:47:57-0700 PDT`.

## Disposition and per-claim findings

**Cyclic necessary-condition theorem:** I reconstructed the stated argument for every anchored tiling and every parameter in the frozen scope. I found **no FATAL or MAJOR mathematical defect**. The cyclotomic field-degree input is independently reconstructed below rather than adopted from the author's assertion. This is an individual same-harness review, not a parent acceptance decision.

| Claim | Reviewer disposition; finding severity |
|---|---|
| Dilation, equal-gcd exclusion, `330 | n`, divisibility of `|Q|`, and exact uniformity modulo 33 | Reconstructed. FATAL none; MAJOR none; MINOR none; INCONCLUSIVE none. |
| Universal opposite-parity gcd rule | Reconstructed for the full parameter range. FATAL none; MAJOR none; MINOR none; INCONCLUSIVE none. |
| Exact parity class of all tails, common `f(j)` in `Y`, and the five anchored values | Reconstructed without choosing the six other values. FATAL none; MAJOR none; MINOR none; INCONCLUSIVE none. |
| All stated Fourier nonvanishing cases, including the relative field degree for order 5 and 25 | Reconstructed; no conditional cyclotomic import remains. FATAL none; MAJOR none; MINOR none; INCONCLUSIVE none. |
| Both Fourier inversions and the 25-way uniform and signed head counts | Reconstructed. FATAL none; MAJOR none; MINOR none; INCONCLUSIVE none. No individual mod-3 uniformity is asserted. |
| `|P| >= 100`, and exclusion of `25` and `50` | Reconstructed. FATAL none; MAJOR none; MINOR none; INCONCLUSIVE none. |
| Equality `|P| = 100`, including the signed-count dichotomy, folded contradiction, and `P mod 66 = 25*A` as a multiset | Reconstructed. FATAL none; MAJOR none; MINOR none; INCONCLUSIVE none. |
| Explicit twofold quotient and its six parity/mod-3 table entries | Reconstructed as a **relaxation only**. FATAL none; MAJOR none. **MINOR clarification:** its unweighted `w=1` profile is a normalized quotient, whereas any actual tiling in scope has `5 | w`; weighting it by `w=5` preserves the folded consistency but is not a lift. The source already says it is not a direct tiling. |
| Code-to-anchored-tiling caller attributed to the Restivo–Salemi–Sportelli border theorem, as cited by the author | **INCONCLUSIVE, conditional external import**, outside the cyclic proof: its complete theorem and its application are not in the pinned input and were not inspected or reconstructed. No code-level implication is independently certified. |
| Existence or exclusion of full lifts in the `|P|=100` case, and constraints at roots of order 125 or higher | **INCONCLUSIVE/open**, as the author states. This is a scope boundary, not an invented counterexample to the necessary conditions. |

The MINOR observation does not invalidate the quotient cover or the theorem. In particular, this review does not turn the quotient into an anchored cyclic tiling, a code witness, an all-order Shor closure, or a novelty claim.

## Frozen inputs and actual read coverage

The manifest was the first research artifact. The required administrative memory/skills were read before the manifest; no mathematical input body was displayed before the complete input pin check. Manifest:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f220-shor-arbitrary-tail-five-power-saturation/manifest-v1.json`

Live SHA-256: `b8459036b2368dfbcb08cd8b3086587484853adf098db5ba06776c9d122671d7`, exactly the assigned digest. There was one declared input, so there were no separately declared mandatory errata:

1. `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-arbitrary-tail-five-power-saturation-v1.md` — live SHA-256 `136274e5e5508a24885389011ef15ef8e074f2b4df635aaad982d7a205b8d32a`, `16106` bytes, `184` LF; all three match the manifest.

Only after that match, the single body was displayed completely in this actual order, each request exact and raw: `1-15`, `16-30`, `31-45`, `46-60`, `61-75`, `76-90`, `91-105`, `106-120`, `121-135`, `136-150`, `151-165`, `166-180`, `181-184`. Thus line 184, the final `END` line, was displayed. No mathematics was reconstructed before the final window. The long scope and requirements lines of the manifest were also displayed in exact raw form. No linked-but-unlisted source, author code, author PASS, sibling result, held material, external web, model/API, or solver status was used as a premise.

## Independent reconstruction

### 1. Dilation, divisibility, and uniform tail classes

Write group-ring sums as `p`, `q`, and `G = sum_{x in Z_n} x`. If a prime `ell` does not divide `|P|`, the Frobenius identity in `F_ell[Z_n]` and `p q = G` give

`p^ell q = p^(ell-1) G = |P|^(ell-1) G = G`.

Here `p^ell` is the sum of the `ell`-dilated elements with their multiplicities. Every integer coefficient of this dilated product is nonnegative and congruent to 1 modulo `ell`; their total is exactly `|P||Q| = n`. Hence each coefficient is 1. In particular the dilation is injective on `P` and gives another direct tiling. Iteration gives the same result for every positive `t` coprime to `|P|`.

If nonzero differences `d_P`, `d_Q` have the same gcd `g < n` with `n`, write `d_P = g u`, `d_Q = g v`; `u,v` are units modulo `n/g`. The unit `v/u` modulo `n/g` lifts to a unit `h` modulo `n`: retain that congruence for primes already dividing `n/g` and impose `h = 1` modulo each other prime dividing `n`. Since `|P|` divides `n`, `h` is coprime to `|P|`. The dilated tiling `hP + Q` would contain the collision arising from `h d_P = d_Q`, a contradiction. This proves the equal-gcd exclusion. As an intended-reason hand negative, coprimality cannot be dropped: in `Z_4`, `{0,1} direct-sum {0,2}` tiles, but doubling the first set gives `{0,2}`, which collides with the second.

The tail anchors 0 and 1 have difference 1; head anchors have differences 3, 5, 8, and 11. Equal-gcd exclusion therefore forces `2*3*5*11 = 330` to divide `n`. If `ell` in `{3,5,11}` failed to divide `|Q|`, dilating **Q** by `ell` would put the scaled difference of the tail anchors equal to the actual head difference `ell`, another collision. Thus all three primes divide `|Q|`.

Consequently write `n=2^K 5^v R`, `|P|=5^e 2^a`, `|Q|=5^(v-e) 2^b R`, with `K>=1`, `v>=e+1`, `a+b=K`, `R` odd and prime to 5, and `33 | R`. Since `R` is coprime to `|P|`, `RP + Q` is a direct tiling and all `RP` elements lie in the zero class modulo `R`. Counting targets in any fixed class modulo `R` gives exactly `5^(v-e) 2^b` tail elements there. Therefore every class modulo 33 contains exactly

`w = 5^(v-e) 2^b (R/33) > 0`

tails. In fact `5 | w`; this extra bookkeeping is relevant to the normalized quotient below. The proof uses no squarefree or fixed-order assumption.

### 2. Opposite parities and the arbitrary-tail graph

Take opposite-parity tails with difference `x` and put `g=gcd(x,n)`, which is odd. If `5 | x` but `25` does not divide `x`, then the 5-adic valuation of `g` is exactly 1 because `25 | n`. Set `t=g/5`; it is coprime to `|P|`, and the actual head difference 5 in `tP` has gcd `g` with `n`. This contradicts equal-gcd exclusion against `x`. If `5` does not divide `x` but `3 | x` or `11 | x`, use respectively `t=g/3` or `t=g/11` and the actual head difference 3 or 11. Those `t` are again coprime to `|P|`. Thus

`q,q' opposite parity and 25 not dividing (q-q') => gcd(q-q',165)=1`.

Equivalently, opposite-parity tails sharing a mod-3, mod-5, or mod-11 residue must share a mod-25 residue.

No even tail can be 1 modulo 3: comparison with the odd anchors 1, 7, and 13 would force three distinct mod-25 values. The class 3 modulo 33 cannot contain an odd tail, since comparison with even anchors 0 and 14 would force both 0 and 14 modulo 25. Class 25 modulo 33 is odd, and its comparison with 14 fixes its mod-25 value at 14; comparing it with the even class 3 fixes that class at 14 as well. Likewise class 11 is even by comparison with 14 and 0; class 22 is odd and has value 0 by comparison with 0, fixing the even class 11 at 0. All these classes exist by the uniformity just proved. An odd tail that is 0 modulo 3 would then have to agree modulo 25 with both 0 and the class-3 tail; an odd tail that is 2 modulo 3 would have to agree with both 14 and the class-11 tail. Both are impossible. Therefore a tail is odd **if and only if** it is 1 modulo 3.

For each `j mod 11`, the nonempty 1-mod-3 class supplies an odd tail and the nonempty 0-mod-3 class supplies an even one. Every opposite-parity pair with label `j` has the same mod-25 value; using either class as a bridge gives one common value `f(j)` for **all** tails with that label. The five anchors yield

`f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7`.

For arbitrary labels `j,k`, choose the odd tail at `j` and an even tail at `k`. If `f(j)=f(k) mod 5`, the rule forces equality mod 25. The five displayed anchor values represent all five mod-5 residues exactly once. Hence every `f(j)` is one of `Y={0,1,7,13,14}`. No values of the other six labels are chosen in this proof.

### 3. Cyclotomic field degree and arbitrary-function nonvanishing

The following is a reconstruction of the named degree input, not an appeal to its citation. For the needed `m` in `{5,25,55,275}`, and indeed for any positive `m`, the cyclotomic polynomial is irreducible over `Q` by the following elementary argument. Monic rational factors of `X^m-1` are in `Z[X]`: Gauss's lemma applies because the product of primitive integer polynomials is primitive, as reduction modulo any prime makes two nonzero polynomials whose product remains nonzero.

Let `F` be the irreducible factor containing a primitive `m`th root `alpha`. For a prime `ell` not dividing `m`, let `G` be the irreducible factor containing `alpha^ell`. If `F != G`, then `F | G(X^ell)` over the integers. Modulo `ell`, Frobenius makes the latter `G(X)^ell`. But the reductions of `F` and `G` are coprime: their product divides `X^m-1`, and that polynomial is squarefree modulo `ell` because its derivative is `m X^(m-1)` and `ell` does not divide `m`. This is a contradiction. Thus `alpha^ell` is a root of `F`. Iterating over the prime factors of any `k` coprime to `m`, every primitive root `alpha^k` is a root of `F`. Conversely all conjugates of `alpha` have order exactly `m`, since a smaller-order conjugate would force `alpha` to have that order. Therefore `F` is exactly the product over all primitive `m`th roots and has degree `phi(m)`. This also verifies the finite-field squarefreeness/Frobenius inputs used in the argument.

For `xi` of exact order `5^s`, `s=1` or `2`, and primitive 11th root `eta`, the product `alpha=eta*xi` has exact order `11*5^s`. CRT exponents recover `eta` and `xi` separately from `alpha`, so `Q(alpha)=Q(eta,xi)`. The preceding proof gives degrees `phi(11*5^s)=10 phi(5^s)` and `phi(5^s)=4*5^(s-1)`. The dimension-tower identity, obtained by multiplying a basis of the smaller field by a basis over it, yields

`[Q(eta,xi):Q(xi)] = 10`.

Thus the minimal polynomial of `eta` over `Q(xi)` is the monic degree-10 polynomial `Phi_11=1+X+...+X^10`. Coprimality of the conductors is genuinely needed: if `xi` has order 25 and `eta=xi^5` has order 5, then `eta` is already in `Q(xi)` and the relative degree is 1, not 4.

For roots `omega` of order dividing 2, `tau` of order dividing 3, `eta` of order dividing 11, and `xi` of order dividing 25, the tail rule and the `w` tails in each mod-33 class give exactly

`Qhat = w (1 + omega*tau + tau^2) sum_(j=0)^10 eta^j xi^f(j)`.

If `eta != 1` and `xi != 1`, a zero of the sum would make its degree-at-most-10 polynomial in `eta` a scalar multiple of `Phi_11`. Its coefficients at 0 and 1 are `1` and `xi`, which are different. If `eta=1` and `xi` has order 25, `F(X)=sum_j X^f(j)` is nonzero with degree at most 14, less than `deg Phi_25=20`. If `eta=1` and `xi` has order 5, the five residue coefficients have total 11 and cannot be equal; a degree-at-most-4 polynomial vanishing at `xi` would be a multiple of `Phi_5`. These arguments apply to every function meeting the stated graph and anchor constraints.

For `tau=1`, the prefactor is `2+omega`, namely 3 or 1. For `omega=-1` and nontrivial `tau`, it is `1-tau+tau^2=-2*tau`. All are nonzero. Conversely, for `omega=1` and nontrivial `tau`, the prefactor is zero, so no individual mod-3 head uniformity follows from this argument. No assertion is made for higher 2-adic characters or order at least 125.

### 4. Fourier inversion, lower bound, and equality

The nontrivial-`xi` characters just used are nontrivial on `Z_n`: their 5-power component cannot cancel the coprime-order 2-, 3-, and 11-components. Since `P+Q` is a direct tiling, `Phat*Qhat=0` at each such character. Fourier inversion here follows from the finite geometric-series identity `sum_chi chi(x-y) = |G|` if `x=y` and 0 otherwise.

For fixed nontrivial `xi`, the `omega=+/-1`, `tau=1`, all-`eta` vanishing equations invert on `Z_2 x Z_11`. Thus, for every parity `epsilon` and label `j`, every nontrivial mod-25 Fourier coefficient of `H_(epsilon,j)(s)` vanishes. Inverting on `Z_25` gives the constant nonnegative integer `c_(epsilon,j)`. The four actual anchors occupy the distinct buckets `(even,0)`, `(odd,0)`, `(odd,3)`, `(even,8)`; each corresponding `c` is at least 1. Consequently `|P|=25 sum c >= 100`, ruling out 25 and 50 in the stated family.

For the second inversion, use `omega=-1`, all `tau`, and all `eta`. Inverting on `Z_3 x Z_11` gives that `H_(0,i,j)(s)-H_(1,i,j)(s)` is independent of `s`, for every `i,j`. This is precisely the signed statement, and is weaker than individual uniformity in `i`.

If `|P|=100`, the four anchor buckets are the only nonempty ones and contain one head per mod-25 class. Let `E(s),O(s)` be the mod-3 values in the even and odd `j=0` buckets. The constant vector `e_E(s)-e_O(s)` is either nonzero, in which case its positive and negative coordinates uniquely identify constant and distinct `E,O`, or zero, in which case `E(s)=O(s)` for every `s`. The signed condition makes the sole odd `j=3` row's mod-3 label constant, fixed to 0 by anchor 3; similarly the sole even `j=8` row is fixed to 2 by anchor 8.

To exclude the zero-vector alternative, fix a folded target with parity 0, mod-3 value 0, arbitrary mod-11 label `J`, and mod-25 label `z`. Each residue of `Z_1650` has `n/1650 = (100*33*w)/1650 = 2w` actual tiling representations after folding. In each `j=0` row, the only possible head mod-25 residue is `s=z-f(J)`. If `E(s)=O(s)`, exactly one of the two rows has a parity-compatible required Q residue: the even row if their common value is 0 or 1, and the odd row if it is 2. The `j=8` even row would require an even tail congruent to 1 mod 3, and the `j=3` odd row would require an odd tail congruent to 0 mod 3; both are impossible. The one permitted mod-33 tail class contains exactly `w` tails, giving only `w` folded representations instead of `2w`. Contradiction.

Hence `E,O` are constant and distinct. Anchors 0 and 11 force `E=0`, `O=2`. Together with the `j=3` and `j=8` rows, CRT gives exactly residues 0, 11, 3, 8 modulo 66, each 25 times and once for every mod-25 head value. This is the asserted multiset saturation identity; it does not prove or disprove a full tiling.

### 5. Quotient table and arithmetic normalization

For the displayed `P0` and `Q0`, CRT gives `|P0|=100`, `|Q0|=33`, and includes both literal anchor sets. At each target parity and mod-3 value, the exact admissible `(head anchor, tail mod-3)` pairs are:

| parity | target 0 | target 1 | target 2 |
|---|---|---|---|
| 0 | `(0,0),(11,1)` | `(3,1),(8,2)` | `(0,2),(8,0)` |
| 1 | `(3,0),(8,1)` | `(0,1),(11,2)` | `(3,2),(11,0)` |

For each pair, the target mod-11 coordinate determines the tail label, and the target mod-25 coordinate then determines the unique head residue. Thus each of the 1650 quotient residues has **two**, not one, representations. In an actual equality-case tiling, the folded Q profile has `w` copies at each of its 33 support residues, so the corresponding folded multiplicity is `2w`. The formula above forces `5 | w`; in particular, the listed unweighted `Q0` with `w=1` is only a normalized support-level relaxation and cannot itself be the literal folded profile of an actual tiling under the theorem. Giving every `Q0` residue multiplicity 5 yields the required folded count 10 and includes the anchors in the support, but it is still only a multiset in the quotient. It constructs no lift and supplies no direct-sum or code witness. This is the MINOR wording clarification in the disposition.

## Independent bounded controls and intended-reason negatives

Reviewer-owned source, not author code:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f220-shor-arbitrary-tail-five-power-saturation/reviewer-exact-controls.py`

Source SHA-256 immediately before execution: `3dec87efabb42994f6a0b7e968fe595299d954589296c113a173a36425dc6c73`. The sole control run used `python3 -B reviewer-exact-controls.py`, with standard-library integer arithmetic only and a 120-second tool deadline. Actual `/bin/date` observations: start `2026-10-29T13:46:31-0700 PDT`, end `2026-10-29T13:46:31-0700 PDT`; actual exit `0`, and stdout ended `ALL EXACT CONTROLS PASSED`. No timeout or incomplete run occurred. The source is retained in this wave; the author source was neither imported nor executed.

* The parity/graph control represented each of the 33 mod-33 classes by possible `(parity, mod-25)` values, enforced all five anchors and the opposite-parity rule, and performed sound pairwise-support pruning. It stopped after 3 rounds with 105 surviving values: the prescribed parity, one anchored value on each of the five anchored labels, and all five possible values on each of the six free labels. Sound pruning supplies only a necessary-condition control, not a tiling existence search. An intended-reason negative removes anchor 14 and explicitly constructs 33 mutually compatible class representatives, retaining 0,1,7,13, with wrong-parity tails; it is a rule-plus-coverage relaxation, not a direct tiling.
* Exact monic integer polynomial division produced degree pairs `(4,40)` and `(20,200)` for `Phi_(5^s)` and `Phi_(11*5^s)`, and showed `1-X` nonzero modulo the former. These finite calculations corroborate but do not replace the written irreducibility proof. The noncoprime-conductor negative is `eta=xi^5` above.
* All `5^6=15625` allowed free-label functions were checked by integer residue counts; 210 distinct five-bin histograms occurred, and none can be constant with total 11. Their exponents all have degree at most 14. As an intended-reason negative, 10 terms with two in each residue give `2 Phi_5` and vanish at a primitive fifth root; separately, eleven identical coefficients give `Phi_11` and vanish at a primitive eleventh root. Neither negative respects all the original anchors/length assumptions.
* Exact reduction modulo `Phi_3` checked `1-X+X^2 = -2X`, while the negative `1+X+X^2 = 0` demonstrates why the missing `omega=1`, nontrivial-`tau` inversion is unavailable. The anchor-bucket count was four and its three-anchor negative was only 75. The signed-vector enumeration confirmed the three zero pairs and six unique nonzero pairs; for all three zero pairs the selected folded target has `w`, while `(E,O)=(0,2)` has `2w`. Changing `E` while holding `O=2` changes the signed vector, checking that signed constancy is essential.
* Exact integer CRT and a representation counter independently checked both anchor sets, all six table cells, the mod-66 histogram, and all 1650 quotient residues at multiplicity exactly 2. Multiplying the Q profile by 5 gave multiplicity 10 everywhere. The intended-reason negative checks that the unweighted cover is not multiplicity 1, so it is not a direct cyclic tiling.

## Imports, deviations, and assurance boundary

The cyclic theorem uses no unpinned mathematical premise in this review. The needed cyclotomic irreducibility and coprime-conductor degree, finite-field Frobenius/squarefreeness, CRT, geometric-series Fourier orthogonality, and integer count steps are reconstructed above using elementary arithmetic and the displayed assumptions. The attributed actual-word border theorem and its exact code-caller application remain an explicitly **conditional, unverified external import**; they play no role in the cyclic proof.

No process deviation from the assigned frozen read/control sequence is known in this review. The source's same-author history and historical process disclosures are not independently audited here. No Git operation, deletion, publication, infrastructure mutation, author contact, author-code execution, solver-based exclusion, independent-model-family review, human review, formal/kernel verification, or novelty check was performed. The normalized quotient and bounded controls do not decide whether any anchored direct tiling or Shor code completion exists. Parent integration and any separate acceptance gate remain the parent's responsibility.
