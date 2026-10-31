# f254 review A: arbitrary-kernel rough-quotient transfer

**Scope and result.** Same-harness written review of the general theorem and its proof only. Within that scope: **FATAL 0 / MAJOR 0 / MINOR 0 / INCONCLUSIVE 0**. The theorem is supported at exactly the quantified conditional scope below. The candidate's examples and comparisons are deliberately **not assessed or accepted** by this slice. This is not a parent disposition, human review, independent-model-family review, formal/kernel verification, or novelty/priority assessment.

Actual `/bin/date` observation before review-file creation: `2026-10-29T15:17:26-0700 PDT`.

## Frozen inputs and reading discipline

Manifest `manifest-v1.json` SHA-256: `1050c6b0437530ca9a3cb2eb5f9b698779821dac5b1c11bb66cb49c1d8d2b757`. Before opening any source body, I verified the manifest and all five source hashes, byte lengths and LF counts against it; each source was UTF-8, had a final LF and contained no CR. Then I displayed every source completely in the declared order, in exact raw windows of at most 15 lines, including each ending, before mathematical analysis. All paths are the exact paths in the manifest.

| Order | Role | SHA-256 | Bytes | LF | Raw windows |
|---|---|---|---:|---:|---|
| 1 | First alternating overlay | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 | 1–15, 16–30, 31–45, 46–56 |
| 2 | Repeated-unit fatal overlay | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 | 1–11 |
| 3 | P7 cardinality clarification | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 | 1–10 |
| 4 | Cyclic-CRT additive erratum | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 | 12 | 1–12 |
| 5 | Complete candidate | `0522bf11ac96d7d688b27d1602cf2d11124c8b05c95c0d3b5023b1ffb5476176` | 7914 | 149 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–149 |

The four overlays are retained with their exact own qualifications; none is used as a premise for the proof reconstructed here. No f161/f162, held/withdrawn, selected prime-2/3, author PASS/code, linked-source or sibling-review body was consulted. No external model/API, Git, deletion or publication was used.

## Claim-by-claim disposition

`F/M/m/I` means fatal/major/minor/inconclusive finding count for the indicated reviewed claim, not a formal proof certificate. Candidate line ranges below refer to input 5.

| Claim | Lines | F/M/m/I | Disposition |
|---|---|---|---|
| Fully quantified conditional theorem and its T=7 specialization | 8–30 | 0/0/0/0 | Supported as stated, including arbitrary normal kernel and no splitting, normal-subgroup-index, or finiteness assumption on G. |
| Finite-quotient roughness iff rough indices of **all**, including nonnormal, finite-index subgroups | 33–41 | 0/0/0/0 | Both directions reconstructed below, including infinite Q. |
| Simultaneous intersection of arbitrary actual left cosets with pairwise-coprime indices | 45–57 | 0/0/0/0 | Supported by the injective coset-set map and finite-index product, not by pairwise intersection alone. |
| Index product and derivation of pairwise-coprime quotient indices | 61–73 | 0/0/0/0 | Supported for infinite G and arbitrary, possibly nonnormal, U_i and quotient images. |
| One actual common fibre, its cosets, and common right translation/conjugation | 74–80 | 0/0/0/0 | Supported with all original labels retained; normality of N is used explicitly. |
| Kernel gcd bounds and contradiction | 80–83 | 0/0/0/0 | Supported for every pair, without replacing any index by an estimate. |
| Edge conditions r=1, T>=2, unit/repeated indices, infinite groups, nonnormal U_i | 8–83 | 0/0/0/0 | Supported by the same proof; detailed below. |
| Candidate's examples, claimed comparisons and novelty/status interfaces | 86–119 | —/—/—/1 | **INCONCLUSIVE / outside this slice**; none is accepted as a premise or independently audited here. |

The dash in the final row means unassessed, not zero findings. The table's first seven rows, not the examples, determine the reviewed theorem verdict.

## Independent reconstruction

### 1. Exact statement

Let `T >= 2` and `r >= 1` be integers, `G` any group, `N` any normal subgroup, `Q = G/N`, and `M_T` the product of all primes at most T. Write `B_T(X) <= r` for the assertion that every family of `r+1` pairwise-disjoint nonempty **left** cosets of finite-index subgroups of X has a pair whose actual subgroup-index gcd exceeds T. Repeated subgroups are permitted.

The reviewed implication is: if every finite homomorphic quotient of Q has order coprime to `M_T`, then `B_T(N) <= r` implies `B_T(G) <= r`. For T=7, `M_T=210`; with `r=7` this is precisely `Sun8(N)` plus the rough-quotient premise implies `Sun8(G)`. Nothing in this statement proves the kernel premise or makes the quotient premise automatic.

### 2. Both roughness directions

Suppose every finite-index subgroup V of Q has `[Q:V]` coprime to `M_T`. For every surjective homomorphism `Q -> F` with F finite, its kernel is finite-index with index `|F|`; hence `|F|` is coprime to `M_T`.

Conversely, suppose every finite quotient has order coprime to `M_T`. For arbitrary finite-index `V <= Q`, the action of Q on the finite set of **left** cosets `Q/V` has finite image and kernel `K = core_Q(V) <= V`. Thus `F=Q/K` is finite and `[Q:V] = [F:V/K]` divides `|F|`. Therefore `[Q:V]` is coprime to `M_T`. The core handles nonnormal V; the finite action exists even when Q is infinite. Index one and the trivial finite quotient pose no exception.

### 3. Simultaneous intersection, not a Helly assumption

For arbitrary finite-index `H_1,...,H_k <= X` with pairwise-coprime `a_i=[X:H_i]`, set `H=intersection_i H_i`. The map of finite **sets**, not quotient groups,

`X/H -> product_i X/H_i`, `xH -> (xH_i)_i`,

is well-defined and injective: equality in every coordinate means `y^{-1}x` lies in every `H_i`, hence in H. Therefore `[X:H] <= product_i a_i`. Also `[X:H] = a_i [H_i:H]` for each i; since the a_i are pairwise coprime, their product divides `[X:H]`. The only possibility is equality, so the injective map is surjective. Consequently **every prescribed tuple of actual left cosets**, simultaneously and not merely pairwise, has a common element. All assertions are finite-index statements and remain valid for infinite X and nonnormal H_i.

Unit indices, including repeated occurrences of 1 and repeated copies of X, are harmless. If a subgroup is repeated and the displayed indices are pairwise coprime, its repeated index must be 1; there is no false claim that the value 1 itself can occur only once.

### 4. Quotient indices, common fibre and kernel indices

Assume for contradiction that `B_T(N) <= r` and that `C_i = g_i U_i`, `i=1,...,r+1`, are pairwise-disjoint actual left cosets in G with all `gcd(n_i,n_j) <= T`, where `n_i=[G:U_i]` is finite. Let `pi:G -> Q` be the quotient map and define

`K_i=U_i cap N`, `a_i=[Q:pi(U_i)]`, `b_i=[N:K_i]`, and `A_i=pi(g_i)pi(U_i)`.

Normality of N makes `NU_i=pi^{-1}(pi(U_i))` a subgroup; `[G:NU_i]=a_i`. The map `N/K_i -> NU_i/U_i`, `nK_i -> nU_i`, is a bijection of left-coset sets, so `[NU_i:U_i]=b_i`. Since `U_i <= NU_i <= G` and `[G:U_i]` is finite, all these indices are finite and the subgroup-chain formula gives **exactly** `n_i=a_i b_i`. No quotient-group structure or normality of U_i or K_i is assumed.

By Section 2, each a_i is coprime to `M_T`. For every pair, `gcd(a_i,a_j)` divides `gcd(n_i,n_j) <= T`. If that quotient gcd exceeded 1, one of its prime divisors would be at most T, contradicting roughness. Hence the a_i are pairwise coprime. Section 3 supplies a single actual `q` in **all** the `A_i`; this does not assert that arbitrary pairwise-intersecting quotient cosets have a common point.

Choose one `t in G` with `pi(t)=q`. Because `q in A_i`, choose `x_i in C_i` with `pi(x_i)=q` for each i. The same fibre is `pi^{-1}(q)=Nt=tN`. Since `x_i in Nt` and N is normal, `x_i N=Nt`, and therefore

`C_i cap Nt = x_i (U_i cap N) = x_i K_i`.

The common right translation by `t^{-1}` gives

`(C_i cap Nt)t^{-1} = (x_i t^{-1})(t K_i t^{-1})`.

Here `x_i t^{-1} in N`, and `t K_i t^{-1} <= N`. Conjugation by t is an automorphism of N, so its index is exactly `b_i`. Thus every displayed set is a nonempty actual left N-coset of a finite-index subgroup. Intersecting with one fibre and applying the **same** bijective right translation preserve pairwise disjointness; no label or coset is selected away. Finally, `b_i | n_i` for every i, whence `gcd(b_i,b_j) | gcd(n_i,n_j) <= T`. These `r+1` disjoint N-cosets contradict `B_T(N) <= r`.

### 5. Edge conditions

* `r=1` gives exactly two labelled cosets; every map, divisibility and contradiction above works unchanged. If a group has too few disjoint nonempty cosets, the relevant B-statement is vacuous, as the universal definition requires.
* The argument is valid for each integer `T>=2`; it uses only that every prime divisor of an integer greater than 1 and at most T occurs in `M_T`. There is no inference from a bounded gcd to quotient coprimality without the roughness premise.
* G, N and Q may be infinite. Only coset **indices** and finite coset-set cardinalities are counted; no division of infinite group cardinalities is used. For instance, independently of the candidate examples, the additive group of rationals has no nontrivial finite quotient: any finite image has exponent m and every rational is m times another rational. Thus the roughness hypothesis genuinely includes an infinite quotient, although that illustration is not a premise of the proof.
* Neither U_i nor `pi(U_i)` nor `U_i cap N` is assumed normal. The only normality used is `N normal in G`; the coset maps are set maps, and conjugation by t preserves N and subgroup index. The finite control below separately exercises a nonnormal original subgroup and a nonabelian rough quotient.

## Final bounded finite control — diagnostic only

I wrote my own `reviewer-A-control.py` in this wave, SHA-256 `800908f2958f771bb45f8c1a0b49bd845d7a03d038d6f924148f2edfdc2a218c`. It is a bounded sanity check, **not** a proof for general groups or an evaluation of the candidate's examples. `/bin/date` immediately before and after execution gave `2026-10-29T15:17:19-0700 PDT` and `2026-10-29T15:17:19-0700 PDT`; monotonic elapsed time was `0.024275 s`, the configured subprocess timeout was 120 s, and the actual exit status was **0**. Captured stdout SHA-256 was `1dc8c209f8507cc9473ba56e5b509e3de8afd0349596b389154df665500122a0`; stderr was empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The control explicitly constructs `G=C2 x (C23 semidirect C11)` and its kernel `N=C2`. The quotient order 253 is coprime to 210; its nonnormal C11 subgroup is directly conjugated out of itself. The chosen bad two-coset family has actual G-indices 46 and 22, quotient indices 23 and 11, and kernel indices 2 and 2. Here `B_T(N)<=1` is intentionally **false** for T=2 and 7, so this is a check of the contradiction mechanism, not a theorem application with a satisfied kernel premise. It enumerates all 23 x 11 actual quotient-coset pairs and checks common-fibre right translation. Its negative controls check the intended failure reasons: original disjointness need not descend to quotient disjointness, and pairwise intersection without pairwise-coprime indices does not imply a triple intersection.

```text
PASS finite control: |G|=506, |Q|=253, U1 nonnormal, indices n=(46,22), a=(23,11), b=(2,2)
PASS all 253 pairs of actual quotient cosets intersect once
PASS r=1, T=2 and T=7 bad-family fibre mechanics; B_T(N)<=1 premise intentionally fails
PASS common right translation gives distinct actual N-cosets with preserved gcd 2
NEGATIVE AS INTENDED: disjoint original cosets have intersecting quotient images
NEGATIVE AS INTENDED: pairwise-intersecting index-2 cosets have empty triple intersection
```

## Exact residual and nonclaims

This conditional theorem does **not** establish unrestricted Sun8, any Sun8 counterexample, `B_T(N)<=r` for an arbitrary kernel, or a transfer result for a quotient with a finite image whose order shares a prime at most T. Failure of this sufficient hypothesis is not a proof that transfer fails, nor is roughness shown necessary. No global quotient Helly property is asserted. The candidate's examples, cross-result comparisons, historical holds, selected-index methods, other source dispositions, and their provenance are not adopted or rehabilitated. Neither this hand reconstruction nor the finite diagnostic supplies human, independent-family, formal/kernel, source-priority or novelty verification.
