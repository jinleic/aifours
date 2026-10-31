# F155: consolidated four-qubit depolarizing k=3 review

## Verdict and exact scope

**Same-harness written mathematical support at the stated regional and uniform-interval scopes, with the supplied additive errata applied. Outstanding findings: 0 FATAL, 0 MAJOR, 1 MINOR (the overbroad reflection sentence at candidate LF 376).** I reconstructed the load-bearing arguments below and independently ran the bounded exact controls linked in §9. No counterexample to an asserted, correctly scoped k=3 inequality was found. The MINOR does not invalidate the explicitly restricted theorem.

For `Φ_p(X)=(1−p)X+(p/2)Tr(X)I`, `Λ_p=Φ_p^{⊗4}`, `t=|1−p|`, `a=(1+t)/2`, `b=(1−t)/2`, and `R3=a⁴+2a³b`, the supported statements are:

| Branch | Exact input and parameter hypotheses | Supported conclusion and dependencies |
|---|---|---|
| P | Pure product input; every `p∈[0,4/3]` | Its output spectrum is the reference spectrum, so `Tr QΛ_p(ρ)≤R3` for every actual complex orthogonal rank-three Q. A nonmaximizing Q need not give equality. Uses C0 below. |
| U | Pure input with **all four** one-qubit marginals `I/2`; every physical p; no C restriction | `R3−Tr QΛ_p(ρ)≥(1/2)(p')²(1−p')`, `p'=min(p,2−p)`. Finite mixtures of U states retain the same gap. Uses E, U, C0. |
| D_p | Pure input; its actual sorted radii satisfy `δ≥t(√(39(15−S))−5)`; every physical p | Original fixed-Q inequality. Boundary equality in the sufficient condition is included. The class is p-dependent. Uses D, C0. |
| H | Pure input; **both** `4S+8C≤64/9` and the actual-state harmonic condition: `s≥1`, `s=0`, or `0<s<1` with (9) | Original inequality for every physical p. Equal radii supply only the harmonic condition, not the separate moment condition. Similarly, `Σr_i≤2` supplies `s≥1`, not the moment condition. Uses F, J, E, C0. |
| Regional hull | At each fixed p, any finite convex combination of pure states in `P∪U∪D_p∪H` | The same original inequality. Q remains fixed throughout the averaging. Uses the four preceding branches and M. |
| Uniform interval | **Every four-qubit density** and `|1−p|≤1/200`, equivalently `199/200≤p≤201/200` | Original inequality. Pure nonproduct tube inputs have the gap (27); far inputs have the positive (14) gap. Uses N0–N5, D, C0, M. This is independent of membership in H or D_p. |
| Endpoints | Every density at p=0 or p=1 | At p=0: `Tr Qρ≤1`, equality iff `supp ρ⊆range Q`. At p=1 every Q has equality `3/16`. The p=0 completion is explicitly additive erratum 127, not a hidden enlargement of the 121 hull. |

**Nothing global about original k=3 for all p and all densities follows.** In particular, p=2/3 and p=4/3 have t=1/3 and are outside the uniform interval. The regional hull is a proper subset at those parameters (an exact pure residual witness is given in §10). Passing finite controls outside that hull is not a proof there. No full majorization claim, other-index status, novelty claim, human review, independent-model-family review, formal proof, or kernel verification is supplied by this review.

The adopted disposition for k=5,6,10,11 was read only as a **scope-only** input. Neither its dual lemma nor its previous controls are premises for any k=3 step here. The historical files named in the candidate's dependency tables were not opened or executed; their hashes and author “checked” claims are not independent evidence. All mathematical dependencies used in this review are reconstructed from the inline 427-LF packet and definitions.

## 1. Frozen bindings, complete-read coverage, and actual chronology

Manifest-v1 SHA-256: `b76a11d666237befb1d00756835293d1b0b61e07ad77edcc41d8af2bb55b8321`. I first read that manifest, verified its hash and both input hashes/bytes/LF, then read the entire scope-only disposition (37 LF) and the entire candidate (427 LF), in that order. The candidate was read raw in contiguous ranges 1–110, 111–230, 231–340, 341–427. The initially truncated manifest requirements line was separately read raw in full.

**The candidate body had already been opened and fully read before the three additive errata were delivered/read.** I do not claim before-source receipt of those later-created errata. After the parent notifications, I read manifests v2, v3 and v4, verified their hashes and every v4 input's SHA/bytes/LF, and read errata 125, 127 and 128 completely, in that order. This is the actual additive read order, not a retroactive rendering of the v4 declared order.

| Binding | SHA-256 | Bytes / LF | Coverage / role |
|---|---|---:|---|
| manifest-v2.json | `e82ccb4a61bdeb64a820b300ff1f9ac14e22a46eb6845ebf0da12d186215f27d` | — | Complete manifest; first additive supplement |
| manifest-v3.json | `c47ab533b912173162451da1ec88344e70fe7bfe86963ff11182c894ab38e841` | — | Complete manifest; second additive supplement |
| manifest-v4.json | `3ebe180ae09307a8c1ed8aae0e58bb43e82d6c78a516342bb4676ac746a7ff7e` | — | Complete manifest; governing final input inventory |
| frontier-20261028-125-121-source-clock-erratum-v1.json | `1922f5bdcf9ce6ca8203445362853bcc0ae1f5bfce81503e144dd92012580c8c` | 2692 / 33 | Complete; applies the 21:31:56 clock only to the initial hash batch; no mathematical premise |
| frontier-20261028-127-121-fixed-Q-equality-erratum-v1.json | `a19cf2acdd3004cc2a21d02537366af0b5ca6543b09f885eec8b9dcbce4de9c6` | 2699 / 21 | Complete; withdraws LF 93's universal fixed-Q equality and adds the p=0 endpoint completion |
| frontier-20261028-128-121-prior-prefix-scope-erratum-v1.json | `873390c306531f1bf69efbdcfdac26b315a7051ad2ccccabaa92ecf964daf285` | 2839 / 25 | Complete; withdraws the final other-prefix nonclaim; no old proof imported |
| physics-2-depolarizing-balanced-rank-prefix-parent-v1.md | `cdda493b043002b208d8f92b7da352d2f165f6e03c07481a439b596be7b8b38d` | 5579 / 37 | Complete, scope only |
| frontier-20261028-121-consolidated-physical-k3.md | `91643ea8965e0e423f2b5010a18e967ddfaeb4c0f78a175ba6509dd9f2e5c36b` | 25795 / 427 | **All 427 LF read**; all inline mathematical dependencies reviewed |

The executable control receipt repeats all these input binding checks. No hash mismatch occurred. The later errata do not rewrite the 121 bytes or make an earlier self-audit cover later discoveries.

Erratum 127's precise counterexample is valid: p=0, ρ=`|0000><0000|`, Q onto `{0001,0010,0100}` gives `Tr Qρ=0<1=R3`. The corrected statement is a product **spectrum** equality and a fixed-Q **inequality**. None of the erasure, harmonic, moment, one-uniform, first-order, tube, far, or convexity arguments uses equality for arbitrary product-state Q. Thus the withdrawal does not leave a load-bearing gap.

## 2. Dependency graph and common-projector interface

The dependency graph used here is:

| Node | Reconstructed content | Consumers |
|---|---|---|
| C0 | Local-unitary covariance, reference spectrum, full-spin-flip p↔2−p identity and Q bijection | Every branch, including mixing after the pure proofs |
| E | Positive erasure expansion, reference layers, T1/T2 spin-flip identities, unconditional T0/T3/T4 bounds | U and H |
| J0 | `M(σ)≥0`, `H1(ρ)+ρ̃=4I−M(σ)` for pure σ=ρ̃ | J1/J2 and H |
| J1 | Pure marginal polygon and zero-amplitude support at a zero denominator | J2 |
| J2 | Exact negative-pivot Schur complement / harmonic IFF for λ₂≤3 | H |
| J3 | Equal-radius probability elimination proving the harmonic condition | Sufficient subcase of J2 only |
| F | Pauli purity identities → exact frame second moment → rank-12 Cauchy–Schwarz → K3(F)≤8 | H, via E |
| U | One-uniform Schmidt eigenvalues, T3=I/4 and improved T2 bound | U gap, via E |
| D | Weight-one Ky Fan bound + projector/input Pauli Parseval + Cauchy–Schwarz | D_p and N5 |
| N0 | Closest-product stationarity → complex normal support on weights 2–4 | N1–N4 |
| N1 | Exact A/M Hessian coefficient identities, weight additivity and negative margin | N4 |
| N2 | Normalized operator/Frobenius bounds, divided-gap S1, Q/off-Q constants | N3/N4 |
| N3 | Exact unitary conjugation with a rigorously bounded cubic remainder | N4 |
| N4 | Two block-majorants plus interlacing and N1 → tube gap | Uniform interval |
| N5 | Closest-product distance / Bloch-deficit union bound + D | Uniform interval far states |
| M | Fixed-Q finite convex averaging | Regional hull and all-density uniform interval |

The maximization over Q is never split and then recombined as though independently maximizing projectors coincided. All trace manipulations first hold for the same actual Q; Ky Fan bounds are upper bounds valid for that Q. Reflection is an explicit bijection of actual rank-three Q, not an independently chosen numerical optimizer.

## 3. C0 and E: reference, erasure identities, and p>1 reflection

The channel sends a pure one-qubit projector to eigenvalues `(a,b)` (possibly exchanging the eigenvectors when p>1). Local-unitary covariance follows immediately from the trace/identity definition. Thus the four-qubit product spectrum has weight-h values `a^(4−h)b^h`; its top-three sum is `a⁴+2a³b`, and direct expansion gives `16R3=3+8t+6t²−t⁴`.

For 0≤p≤1, `Φ_p=(1−p)id+pE` sitewise; multiplying four commuting maps yields exactly (3). For the fixed product Q in the packet, the layer traces are `(1,3,3,5/4,3/16)`. For arbitrary normalized ρ, the scalar bounds T0≤1 and T4=3/16 are immediate.

After diagonalizing each actual marginal, the T3 eigenvalues are `(4+Σ ε_i r_i)/16`. The largest three are obtained from all plus and the flips of the two smallest radii, with ties allowed, so their sum is `(12+r1+r2+3r3+3r4)/16≤5/4`. This uses joint eigenvectors of four commuting one-site operators, not arbitrary joint marginal spectra. It also holds for mixed ρ.

One-site Pauli twirling gives `Σ_a σ_i^a Xσ_i^a=4E_i(X)−X`; summing gives `T1=ρ+F/4`. The one-site identity `Y X^T Y=Tr(X)I−X=2E(X)−X` implies the four-site polynomial

`ρ̃=ρ−2T1+4T2−8T3+16T4`.

With `8T3=H1` and `16T4=I`, this gives exactly `4T2=H1+ρ+ρ̃+F/2−I`. Hence K3(F)≤8 and K3(H1+ρ̃)≤10 give, for the same Q, `Tr QT1≤3` and `4Tr QT2≤10+1+4−3=12`. The nonnegative erasure coefficients then give the reference comparison; at p=0 no strict positivity of a coefficient is needed.

For p>1, composing the one-qubit reflection with Φ_(2−p) gives Φ_p. Tensoring gives the **full** transpose identity (6). Its trace pairing sends Q to `Q'=Y^{⊗4}Q^T Y^{⊗4}`, another actual complex rank-three orthoprojector, bijectively. The input ρ is unchanged, and the reference multiset is unchanged. Thus an already proved statement at p'=2−p transfers with its **same t-restriction and input hypotheses**. There is no partial-transpose positivity assumption and no use of positive erasure coefficients at negative shrinkage.

## 4. J0–J3: harmonic IFF, pure polygon, zero support, and equal radii

All of this subsection is for a **pure** input and σ=ρ̃. Across any one|three Schmidt split, Cauchy–Schwarz on the at-most-two Schmidt coordinates gives `I_bar_i⊗σ_i≥σ/2`, including vanishing coefficients. Summing yields `H1(σ)≥2σ`, so `M=H1(σ)−σ≥σ≥0`. Also each spin-flipped local marginal is `I−ρ_i`, yielding `H1(ρ)+σ=4I−M` and λ₁≤4.

In local majority bases, D=H1(σ) is diagonal. If s≥1 then its least diagonal entry is s≥1. Subtracting the rank-one σ from D−I leaves at most one negative eigenvalue, so the second-smallest eigenvalue of M is ≥1 and λ₂(H1+σ)≤3. If s=0, purity of all local marginals forces a product state and branch P applies, with the fixed-Q equality qualification in erratum 127.

For 0<s<1, the pure marginal polygon is not an assumption on four arbitrary probability lists. The complementary three-qubit marginal has largest eigenvalue 1−p_i by Schmidt purity, so the probability that the other three majority projectors all occur is ≤1−p_i. The commuting-projector union bound makes it ≥`1−Σ_(j≠i)p_j`. Thus `p_i≤Σ_(j≠i)p_j` for the **actual** state.

The entries of D−I away from 1111 are a_x in (8). At weights 0,1,2 they are strictly positive; at weight three, missing i, they are s−2p_i≥0. If this vanishes, both bounds on the three-majority probability above are equal. Equality in the classical union bound forces probability of two or more minority events among those three sites to vanish. In particular the amplitude at that weight-three word vanishes. Thus every zero a_x has zero actual σ amplitude; the corresponding row/column stays zero during elimination. Also p_i≤s/2<1/2 makes the majority axes nondegenerate in this regime.

There is exactly one negative diagonal location in D−I, at 1111, with value s−1. In `D−I−|φ><φ|`, eliminating that pivot `−(1−s+q4)` leaves

`diag(a_x) − [(1−s)/(1−s+q4)] u u*`.

On its positive support, congruence by `diag(a_x^(−1/2))` gives the exact rank-one PSD condition `[(1−s)/(1−s+q4)]Σ P_x/a_x≤1`. Since the eliminated pivot contributes one negative eigenvalue, this is **equivalent**, not merely sufficient, to M−I having at most one negative eigenvalue. Consequently (9) is exactly the stated IFF for λ₂(H1+ρ̃)≤3. Equality gives a zero Schur eigenvalue, not a forbidden negative one. This IFF is **not** asserted to characterize K3(H1+ρ̃)≤10 or the original channel inequality.

For equal radii and 0<s<1, the a-values are `(3−s, 2−s/2, 1, s/2)` by weight. Eliminating P0 and P3 using `ΣP_h=1`, `ΣhP_h=s` gives exactly the displayed coefficients `(a1−K)P1+(a2−2K)P2−[1/(3−s)+1/(1−s)+4K]P4`. Here `a1=Ks/(4−s)<K` and `a2=sK<2K`, so the expression is nonpositive. Equality requires P1=P2=P4=0 in this open-s regime; the endpoints s=0 and s=1 were covered separately. The proof uses no symmetry of amplitudes beyond equal local radii.

An actual equality example is `(4|0000>+|0111>+|1011>+|1101>+|1110>)/√20`: p_i=3/20, s=3/5, W=1, q4=0. Exact inertia of M−I is (positive,zero,negative)=(14,1,1). Its one|three Schmidt ranks are two and, by permutation symmetry, all two|two coefficient matrices have rank three, so it is genuinely multipartite entangled. Equality here is therefore not restricted to products. This is harmonic equality only: its `4S+8C=196/25>64/9`, so equal radii alone do **not** put it in H.

A zero-support control is `(6|0000>+|1100>+2|1010>+(1+i)|1001>)/√43`. In majority bases of σ its minorities are `(7,1,4,2)/43`, so p1=p2+p3+p4 and a_0111=0 with P_0111=0. Its W is `377303/826965<1`, and M−I again has inertia (14,1,1). No division by zero was evaluated.

Finally λ₁≤4 and λ₂≤3 give λ₃≤3 and K3(H1+ρ̃)≤10. This is the precise harmonic-to-erasure bridge used by H.

## 5. F and U: moment condition, rank-12 consequence, and independent one-uniform gap

For pure ρ, the 12 vectors `σ_i^a|ψ>` form a frame whose sum of outer products is F: it is PSD, trace 12, rank at most 12. Let A_j sum squared real Pauli expectations of weight j and A1=S. Summing the equal purities of each one-qubit marginal and its three-qubit complement gives

`A3=12+S−2A2`.

Total pure-state Parseval gives `1+S+A2+A3+A4=16`, hence `A4=3−2S+A2`. Full spin flip changes a weight-j Pauli coefficient by (−1)^j, so `16C=1−S+A2−A3+A4`; substitution yields `A2=2+S+4C`.

The Gram squared Frobenius norm has 12 diagonal terms, `2S` from ordered distinct Paulis at the same site, and `2A2` from ordered distinct-site terms. Thus `Tr F²=12+2S+2A2=16+4S+8C` exactly. With x=K3(F), padding the rest of the spectrum to nine nonnegative entries gives

`Tr F²≥x²/3+(12−x)²/9`.

The derivative of the right side is `(8x−24)/9`, positive at and above 8, and its value at 8 is 208/9. Therefore `4S+8C≤64/9` forces x≤8, including the equality threshold and ranks below 12. This is a sufficient moment condition, not its converse. Combining it with the separate harmonic condition through the **same-Q** identities proves H.

For U, the one|three Schmidt eigenvalues are 1/2,1/2. Thus every E_i(ρ) has four eigenvalues 1/4, yielding `Tr QT1≤3`. Separately T3=I/4, so its rank-three trace is 3/4. The full spin-flip identity gives `4Tr QT2≤1+6+6−3=10`, using `Tr Qρ̃≤1` and `Tr Qρ≥0`. Against the reference layers, the improvements are at least 1/2 in T2 and 1/2 in T3. Their weighted sum is

`(1/2)t²p²+(1/2)tp³=(1/2)p²(1−p)`

for 0≤p≤1. Reflection gives the stated p' expression. No moment condition, restriction on C, coincident maximizing projector, product-only saturation, or unjustified extension of pure Schmidt eigenvalues to general mixed states is used. Mixtures of U states inherit the bound by fixed-Q averaging.

## 6. D: first-order bound and its exact hypotheses

Expand ρ and Q in the 256-element four-qubit Pauli basis. For a pure input, `Σ_(P≠I)〈P〉²=15` and the weight-one sum is S, so the weight-two-through-four sum is 15−S. For a rank-three orthoprojector, `Σ_(P≠I)(Tr QP)²=16Tr Q²−(Tr Q)²=39`. Complex input vectors cause no problem: these are real expectation values of Hermitian Paulis.

The weight-one operator is a sum of commuting local Bloch terms, with top-three sum L after sorting actual radii. For 0≤t≤1, the remaining weights contribute at most `t²√(39(15−S))` by `t^w≤t²` and Cauchy–Schwarz. This proves (13) for every actual Q. Using `t⁴≤t²` in the exact reference polynomial gives (14), including t=0. Its nonnegative bracket is exactly the D_p hypothesis. For p>1 first reflect Q and use t=p−1; there is no sign replacement in a negative-coefficient erasure expansion.

The exact controls included four non-diagonal Gaussian-rational rank-three projectors constructed by Gram inversion, not floating eigenprojectors. They verified the projector Parseval value 39, same-Q reflection, the squared Cauchy–Schwarz bound on the actual higher-weight remainder, and (14), at both p=2/3 and p=4/3. A rotated even-parity pure state additionally gave an exact, full 16-eigenvalue T3 inertia certificate with non-diagonal complex marginals and rational radii.

## 7. N0/N1: normal gauge and all-variable Hessian reconstruction

A maximum product overlap exists by compactness and is nonzero because product basis vectors span the space. Rotate a maximizer to |0000>, using channel covariance, and fix the overlap positive. Varying each one-qubit bra in both real and imaginary directions forces each weight-one amplitude of ψ to vanish. Thus (15) has a unit v supported **only** on weights 2,3,4. No uniqueness of the maximizer is needed.

For t>0, the product levels λ_h are strictly ordered. The V blocks on weight zero, weight one, and between zero and one vanish. An amplitude at a word u of weight h gives `V_(u,0)=a^(4−h)t^h v_u`; it couples weight one only to a virtual weight-(h+1) word. In W_ij for two weight-one words, u and u' can differ only by exchanging i and j, so they have the same weight. In the virtual products the two amplitudes also have the same h. Hence both A and M have **no cross-weight quadratic terms**. This proves the sum-over-h property without relying on finite samples or an unexplained optimizer.

For each normalized weight component, direct matrix-unit rules give:

* Weight two: `W00=−a²t`, `V_(ij,0)=a²t² c_ij`, and the gap is a²t, giving `A2=−a²t(1−t²)`. With Γ=TT*, `W_ii=−abt(1−n_i)` and `W_ij=abt²Γ_ij` for i≠j. The weight-three virtual sector adds `abt³(1−n_i)` on the diagonal and `abt³Γ_ij` off it, giving exactly (17). Factorization yields `M2=abt(1+t)[−(1−t)I+K]`, `K=tΓ+(1−2t)diag n`, K≥0 and trace 2(1−t) on the needed interval t≤1/200 (indeed t≤1/2 suffices). Thus K2(M2)≤0.
* Weight three: `W00=−atD3`, `V_(bar i,0)=at³g_i`, gap atD3, giving `A3=−atD3+at⁵/D3`. The diagonal W_ii is `−a²bt−b²t|g_i|²`; its off-diagonal is `t²b² conjugate(g_i)g_j`. The sole virtual weight-four block adds `(t⁵b/D3) conjugate(g_i)g_j`. Reassembling diagonal plus rank-one terms gives precisely (18), including its complex conjugations. Discarding the negative diagonal and bounding the positive rank-one top-two sum by its trace gives (19); its rational-function identity is exact.
* Weight four: `W00=−tD4`, `V_(1111,0)=t⁴v_1111`, gap tD4, and there is no virtual weight five for M. Therefore `A4=−tD4+t⁷/D4`, `M4=−abtI`, and their sum is exactly (20).

Homogeneity applies when a weight component has norm less than one. A is additive, and the variational definition gives `K2(Σ M_h)≤Σ K2(M_h)`. On 0<t≤1/200, the weight-two coefficient obeys `a²(1−t²)>15/64`; the bound (19) is more negative than `−(15/32)(1−t)t<−15t/64`; and (20) is at most `−(1−2t⁶)t<−15t/64`. Summing the norm-squared weights, which total one, proves (21). These negativity estimates are **not** extended to all physical t.

I reviewed these all-variable derivations rather than importing the cited author's checkers. Independent controls also verified the complex formulas at t=1/200,1/3,2/5, cross-weight sums, and all 121 complex coordinate-polarization probes at each of t=1/200 and t=1/3. The latter are finite coefficient controls, not by themselves an all-t interpolation proof. Mutating the weight-two A factor `(1−t²)` to `(1−t³)` was detected exactly at all three test parameters. The disclosed historic `a−ab=at` error is not used; in fact a−ab=a².

## 8. N2–N5: normalized unitary argument, constants, tube and far closure

In the Pauli basis `H_t(X)=Σ_(P≠I)t^(wt(P)−1)Tr(XP)P`, so it is polynomial at t=0. For `X=|v><0|+|0><v|`, trace and weight-one coefficients vanish and `Tr X²=2`; hence `||V_H||_F²≤512t²<(23/200)²`. For `X'=|v><v|−|0><0|`, the same Frobenius-square input value holds, and subtracting its exact weight-one part W0 gives the same bound for `W_H−W0`. Local Bloch vector lengths ≤1 imply `||W0||≤8`, hence `||W_H||<163/20`.

The exact diagonal reference has `d0−d1=2(1+t)³≥2`, `d1−d2=2(1+t)²(1−t)≥2`, and `||D||<5` on this interval. Dividing off-block entries by these gaps gives an anti-Hermitian S1 with `||S1||_F≤23/400`. Using `[D,S1]=−V_off`, a direct commutator bound even gives `||B||_F≤3(23/400)(23/200)=1587/80000<47/1000`. Therefore `||Qcal||<163/20+47/1000<41/5`.

For off Qcal, the off-block part of W0 is exactly the compression of its transverse operator G to weights ≤2: the Z part is block diagonal, and transverse flips beyond weight two stay inside the rest block and are discarded. Thus `||off W0||≤||G||≤4`. Frobenius projection does not increase the two correction norms, so `||off Qcal||<4+23/200+47/1000<21/5`. This justifies the otherwise important compression step in (24).

The conjugation expansion with `h=η√(1−η²)` has exact retained terms `D+h V_diag+h² B+η²W_H`; using `h²=η²−η⁴` gives (25). The tails are bounded respectively by the order-three D, order-two V, and order-one W commutator tails. For η≤9/40, `exp(2ηs1)<103/100`; even the geometric majorant `1/(1−2ηs1)` is below 103/100 at the endpoint. The displayed sum equals exactly `580473701/600000000<1`, so `||R||<η³`, uniformly including small t. There is no division by a vanishing t in these normalized estimates; t=0 itself is handled separately.

Set `H_*=D+h V_diag+η²Qcal`. Its norm distance from D is ≤441/1000, so both needed block separations exceed `2−2(441/1000)>11/10`. The block majorant (26) follows directly by factoring its PSD difference. The separation also ensures that its shifted lower block cannot overtake the upper one. Apply it to weight zero vs its complement to bound λ₁, and to weight one vs the rest inside that complement to bound its top two. Cauchy interlacing has the needed direction: the complement's first two eigenvalues are at least the full matrix's second and third. This produces the factor three in the fourth-order error, not a count of three independently optimized projectors.

The exact leading 00/11 blocks of Qcal equal `(16/t)A` and `(16/t)M`; this also follows directly from the S1 commutators, and was checked exactly with complex normal amplitudes. V_diag is zero in both leading blocks. Thus the leading total margin is `(16/t)(A+K2(M))≤−15/4`. The retained off-block error is at most `3(21/5)²η⁴/(11/10)`. The discarded `−η⁴B+R` changes K3 by at most `3(47/1000)η⁴+3η³`.

After dividing by η² and using η≤9/40, the total error is exactly bounded by

`54870831/17600000 < 13/4`.

The remaining normalized margin is therefore greater than 1/2. Returning from H to Λ multiplies by t/16 and proves the claimed tube gap `tη²/32`. No nondegeneracy within the four-dimensional weight-one block is required. The normal-support hypothesis is indispensable: the product curve `(40|0000>+9|1000>)/41` would have zero actual gap but a false positive RHS if a weight-one direction were admitted.

For the far part, choose the actual local majority eigenvectors. Their product overlap is ≥`1−(1/2)Σ(1−r_i)` by the commuting-projector union bound; maximality of m gives `η²=1−m≤(1/2)Σ(1−r_i)≤δ/2`. Therefore η≥9/40 implies δ≥81/800. Since `√(39(15−S))−5≤√585−5<20`, t≤1/200 gives a strictly positive bracket in (14), because `20t≤1/10<81/800`.

The product case, the tube, and the far set exhaust pure inputs. They overlap at the tube boundary, so there is no omitted transition. A finite spectral decomposition then covers every density with the same Q. Reflection supplies exactly the matching negative-shrink interval **up to p=201/200**, not p=4/3. At t=0 the channel output is I/16 and every Q has equality. This closes the uniform theorem at precisely its stated parameters.

## 9. Independently authored executed exact controls and receipts

No author checker or helper was imported/executed. I used Python `fractions.Fraction` for Gaussian-rational arithmetic and a separately authored Hermitian congruence inertia routine with symmetric 1×1 pivots and 2×2 zero-diagonal pivots. Numpy eigenvalues only proposed dyadic endpoints; **acceptance of each spectral endpoint used exact rational inertia**, not floating signs. An upper endpoint for the j-th largest eigenvalue was accepted only if at most j−1 eigenvalues were strictly above it; lower endpoints used the converse exact count. The top-three sum bounds are sums of those certified dyadic intervals. The product equality control uses its exact tensor-product spectrum because rounded spectral upper bounds alone cannot certify equality.

Both bounded programs actually ran with `python3 -B` and completed successfully. Every negative control listed below observed its intended reason. The result files contain amplitudes, rational margins, eigenvalue brackets, and pivot-count receipts; no finite experiment is described as a universal proof.

| Artifact | SHA-256 |
|---|---|
| [reviewer-exact-controls-v1.py](reviewer-exact-controls-v1.py) | `49513a7645f815f4f543c87b8eb5329de3393591e0b0644151ff624307fa780f` |
| [reviewer-exact-controls-v1.result.json](reviewer-exact-controls-v1.result.json) | `56719fc50de173fec56d1719d9adf7cd67d81d5d2d10f7a850deefc4462926c6` |
| [reviewer-supplement-controls-v1.py](reviewer-supplement-controls-v1.py) | `66b94be75767f614f9ae03ead75429de68722487ac0d0385fdcef9b4fb7184f3` |
| [reviewer-supplement-controls-v1.result.json](reviewer-supplement-controls-v1.result.json) | `5c0c80d8e4874678ae7d04425680cf717355f3099043eed5c513dc7ff0447dfe` |

The primary run recorded native start/end `2026-10-28T22:09:34.447349−07:00` / `22:09:42.728765−07:00`. The supplement recorded `22:13:12.740115−07:00` / `22:13:23.903140−07:00`. These are the programs' observed clocks, not claims about continuous research runtime or the source files' creation times. The supplement loads only the definitions in the pinned **reviewer's** own primary program, checks that helper hash, and does not rerun its top-level driver.

Executed positive controls include:

* All four manifests and the complete final input SHA/bytes/LF inventory; reference polynomial and five product erasure layers.
* Three general complex rational pure states: every erasure/spin-flip identity, trace normalization, Schmidt-derived PSD bound, all Pauli purity relations, and exact frame second moment. Four further actual complex rank-three projectors: exact Q²=Q, trace three, Parseval 39, rank≤12 frame inertia, same-Q reflection, actual (13)/(14) remainders at p=2/3 and p=4/3.
* Twelve harmonic instances: eight random even-parity states, an actual equal-radius equality state, an actual zero-support polygon-equality state, s=0 product, and s=2 GHZ. No local marginal axes were replaced by independently specified spectra.
* Hessian coefficient identities on all three normal weights at t=1/200,1/3,2/5; exact cross-weight additivity; a mixed-weight K2(M) inertia certificate; and 121 complex coordinate-polarization probes at each of two t values. The exact normalized S1/B construction and 00/11 block identities were also checked.
* All displayed rational tube constants, a direct normal-tube output check at t=1/200 with η=9/41, and three random far states at that endpoint. For the latter, `m≤min_i λmax(ρ_i)` gave exact rational bounds certifying that the **actual** closest-product distance was outside the tube. The normal-tube test certifies the representation needed by the local tube proof, not an unproved global-maximizer claim for its chosen |0>.
* Nine rational pure input controls at **both** p=2/3 and p=4/3. Membership decisions for D used certified rational square-root intervals; H used the exact moment and direct λ₂ inertia condition. The sample table below has at least one point inside and outside each of P,U,D,H.

| Exact input control | P | U | D_(t=1/3) | H |
|---|---:|---:|---:|---:|
| Random complex pure product | yes | no | no | no |
| Random rational local rotation/phase of one-uniform GHZ | no | yes | yes | no |
| Random near-one-uniform even-parity state | no | no | yes | no |
| Random full-support state 0 | no | no | no | yes |
| Random full-support state 1 | no | no | no | yes |
| Random near-product full-support state | no | no | no | no |
| Random near-product normal state | no | no | no | no |
| Equal-radius harmonic equality state | no | no | no | no |
| Polygon zero-support state | no | no | no | no |

For all nine, the original output comparison passed at both p values (exact spectrum for the product, exact LDL spectral bounds for the others). The U sample also passed its `2/27` gap, and both H samples passed exact K3(F)≤8 and K3(T1),K3(T2)≤3 controls. Samples outside the claimed classes remain **diagnostics**, not newly adopted regions.

Intended-reason negative controls:

1. **Wrong fixed-Q product equality:** the erratum-127 example gives zero rather than one at p=0.
2. **Lowered reference:** product spectrum K3=32/81 violates a reference lowered by 1/1000 at p=2/3.
3. **Removing the U hypothesis:** the product has zero gap and violates the U-specific claimed positive gap `2/27` if that gap is applied to products.
4. **Strict/lowered harmonic boundary:** the actual P0/P3 equality state has W=1 and λ₂=3; changing the RHS to 999/1000, or making the inequality strict, wrongly rejects it.
5. **Moment threshold mutation:** a synthetic PSD rank-12 trace-12 spectrum with top three each 401/150 and other nine each 199/450 has x=401/50>8 and second moment 130501/5625, between 208/9 and 209/9. Thus replacing 64/9 by 65/9 does not support the **rank/trace/moment lemma's** conclusion. This is expressly not claimed to be an actual Pauli-frame or channel counterexample.
6. **Hessian coefficient mutation:** replacing the weight-two `(1−t²)` factor by `(1−t³)` fails the exact identities at each of the three declared t values.
7. **Insufficient Hessian margin:** replacing 15/64 by 12/64 leaves normalized margin three, which cannot pay the displayed error and still retain the required 1/2 gap.
8. **Unsupported interval enlargement:** taking t=1/190 breaks `20t<81/800` in the far-state constant chain. This is a failure of that proof chain, not a counterexample to a larger uniform theorem.
9. **Admitting a tangent/weight-one normal:** the pure product curve above has actual gap zero, so the positive tube gap is false without the no-weight-one hypothesis.

No unrelated build, lint, formatter, author test suite, external model/API, web search, Git operation, publication, deletion, secret access, or infrastructure mutation was performed. Sympy was unavailable; no dependency installation was needed. All exact arithmetic used the independently written rational implementation.

## 10. Precise residual, outstanding finding, and final disposition

### Proper residual: not a global k=3 result

At p=2/3 (and by reflection p=4/3), the normalized vector with the following computational-basis amplitudes, divided by √2626, is outside every pure class in the regional union:

`(50, 1−2i, 3+2i, −3+i, 2+i, 3+2i, −i, 2−3i, 2−2i, −1−i, −2+2i, 1−3i, −1+3i, −1−3i, 3−i, −2−2i)`.

Its exact `S=6240006/1723969`, `C=19400/1723969`, and `4S+8C=25115224/1723969>64/9` exclude H; it is neither P nor U. The receipt's disjoint exact rational intervals put δ near 0.382 and the D right side near 5.356, so it fails D. A pure density is an extreme point: it cannot enter the convex hull of different pure states. Thus it is outside the entire claimed regional hull, not just outside a chosen parametrization. Its certified output sum is nevertheless below 32/81; this is a positive finite diagnostic, **not** an original counterexample and not a proof over that residual.

### Outstanding MINOR M1 — Preserve the uniform interval when applying reflection

*Location:* `frontier-20261028-121-consolidated-physical-k3.md`, **LF 376**, the clause “Equation (6) then covers the negative-shrink physical half, including p=4/3.”

In this paragraph the antecedent is the all-density t≤1/200 proof. Reflection sends p=4/3 to p'=2/3, whose t=1/3 violates that hypothesis. Equation (6) therefore extends the **uniform branch** only to `1≤p≤201/200`, not to p=4/3 or the entire negative-shrink physical half. The all-p regional branches may separately apply at p=4/3 under their own input hypotheses. Replace the quoted uniform-branch clause by the restricted interval statement; do not silently infer an all-density p=4/3 theorem. This is a precise scope gap in that sentence, not a physical counterexample. Priority P3; confidence 1.00. The explicitly stated theorem immediately afterwards retains t≤1/200, which is why this does not invalidate the proof at its declared scope.

The supplied 125/127/128 errata address three earlier local clock/equality/other-prefix defects; they are not outstanding new findings here. The mathematical fixed-Q equality error at LF 93 is not being accepted as true or silently used. The old k2/k4 proofs named by erratum 128 remain outside this review.

**Final disposition:** P, U with its gap, D_p, H with both hypotheses, their fixed-p finite convex hull, and the independent all-density `|1−p|≤1/200` branch are supported by the written reconstruction above. Equality/zero-support/pure-polygon/rank-deficiency endpoints needed by those arguments were included. There is no FATAL or MAJOR mathematical gap at these exact scopes after errata; there is one remaining MINOR scope sentence to correct. Overall correctness at the stated scopes: **correct**. Confidence in this ordinary written, same-harness review: **0.95**. No unrestricted original k=3 result or independent-family/formal/novelty certification follows.
