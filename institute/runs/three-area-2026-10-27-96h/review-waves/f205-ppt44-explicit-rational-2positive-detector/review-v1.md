# Independent same-harness review: explicit 4×5 detector and fixed-pair link gap

**Disposition: 0 F / 0 M / 0 m on the frozen claims; INCONCLUSIVE (outside those claims): the unrestricted 4×4 target, novelty and literature attribution, and 2-block positivity of the distinct older candidate.** The source, rank-two margin, negative PPT pairing, map consequence, and both fixed-source link-gap bounds are reconstructed below. A finite exact calculation is used for explicitly displayed finite matrices; the all-input conclusions also use the written arguments below.

Native clock observed before writing: **2026-10-29T13:17:10-0700 PDT**. This is an observation before writing, not an assertion of creation time.

## Frozen inputs and actual sequence

First research artifact opened was this wave's `manifest-v1.json`. Its measured SHA-256 was `03efc75f830a8632585843237e661ee40e57f5fb00b23abd4b04fe9507f6cac4`, matching the assigned prefix `03efc75f830a`. The initial manifest display truncated its last long requirements line, which was then displayed completely as `:raw:43-43`. Before opening any declared input body, I measured all four inputs together with `shasum -a 256` and `wc -cl`; every hash, byte count and LF count matched the manifest. I then read the input bodies in the manifest's order, in the following actual raw line windows, including their last lines:

| Order | Frozen input | SHA-256 | bytes / LF | Complete raw windows actually displayed |
|---|---|---|---|---|
| 1 | `institute/runs/three-area-2026-10-27-96h/dispositions/physics-3-ppt44-z-correlated-decomposability-parent-v1.md` | `a0912ca962a91a7cfead6467dee59e87df9e947576a9e1eb8756f2e1d9a2a4f5` | 6886 / 23 | 1–12, 13–23 |
| 2 | `physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-kg-explicit-rational-2positive-detector-v1.json` | `41cb89bc018e76b94b098f351458f0d29a4c3e29c3bde5e1e14afd65d06391d4` | 5455 / 15 | 1–8, 9–15 |
| 3 | `physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-kg-explicit-witness-link-gap-v1.json` | `0805b80e9046994222efeec208e3853f2c67eed9505c735ba89777aace5f49fd` | 2668 / 11 | 1–11 |
| 4 | `physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-kg-explicit-witness-check.py` | `84b2bb38f1b0fbdbac6ebfded341c0773337c6efd1f398aa1671697f38b89386` | 2937 / 72 | 1–12, 13–24, 25–36, 37–48, 49–60, 61–72 |

Paths above are relative to `/Users/jinleic/repos/aifours/`. Procedural memory/skill metadata was also read, but no further scientific source was opened. In particular, the checker was **read only**, and neither it nor the source checker it refers to was run, imported, or compiled. The author's recorded PASS, run receipts and linked bodies are not premises for this review. The adopted parent disposition's phase-covariant 4×4 results provide scoped context, but are not used in the following 4×5 proof.

## Claim-by-claim verdicts

`0F/0M/0m` means no finding at those severities for that particular claim, not formal verification.

| Frozen claim | Verdict | Reconstruction |
|---|---|---|
| The nine defined source vectors are orthogonal; `R ≥ 0`, `rank R = 9`, `Tr R = 31`, and `R^Γ ≥ 0`, `rank R^Γ = 10` | **0F/0M/0m** | Explicit eigenvalues and partial-transpose blocks below. |
| The stated projectors give integer `W_int` and `Tr(W_int R) = −18` | **0F/0M/0m** | Exact projectors and three pairing terms below. |
| The five-minor polynomial identity and determinant perturbation bound hold for complex rank-≤2 inputs | **0F/0M/0m** | All five minors are expanded; the column telescope is uniform. |
| The three global cases prove the uniform rank-≤2 margin `6/11` | **0F/0M/0m** | All inequalities and exact endpoint slacks below. |
| The given Choi convention defines a strictly 2-positive indecomposable `M_4 → M_5` map and detects `R/31` | **0F/0M/0m** | Explicit Choi quadratic-form reduction and PPT pairing below. |
| For every `T`, `Q_PK(T) ≥ (1/2)||T−(Tr T/5)I||_F²` | **0F/0M/0m** | The entire finite link matrix block certificate is given below. |
| For nonzero rank-≤4 `T`, the explicit detector has positive link form, with margin `18·10^10−348` | **0F/0M/0m** | Rank/trace Cauchy–Schwarz and source operator bound below. |
| The separate `W_cand` has fixed-source rank-≤4 link margin `132/5` | **0F/0M/0m**, for the stated link form only | Its independent 2-block positivity is **INCONCLUSIVE**, and is not needed for this particular inequality. |
| These two fixed pairs cannot realize a negative rank-≤4 link of the specified filter form | **0F/0M/0m**, at that exact fixed-pair scope | This does not exclude other witnesses, other sources, or other approaches. |
| Literature identity/priority or novelty, and resolution of the original unrestricted 4×4 problem | **INCONCLUSIVE / outside frozen scope** | No literature search or external expansion was performed. The parent disposition's open-status boundary is unchanged. |

## Source and partial transpose

Use Bob-second basis index `5i+b`. Write `[v]=|v><v|`, and take the vectors and weights exactly as in the frozen packet:

```
A=|00>+|11>+|22>,   B=|01>+|12>,  D=|10>−|21>,
C=|02>+|34>,        E=|20>+|33>,  F=|23>, G=|30>, I=|32>, H=|04>,
R=[A]+[B]+[D]+3([C]+[E]+[F]+[G]+[I]+[H]).
```

Their supports are disjoint, so the nine vectors are mutually orthogonal. Squared norms in that order are `3,2,2,2,2,1,1,1,1`. Thus the nonzero eigenvalues of `R` are `3,2,2,6,6,3,3,3,3`, giving `R ≥ 0`, rank 9, trace 31, and the later bound `R ≤ 6 I_20`.

For a direct PPT certificate, partial-transpose Bob in each matrix unit. With the same indices, `R^Γ` splits into the following nonzero nonsingleton blocks, all other off-block entries zero:

- indices `(1,5)` and `(7,11)`: `[[1,1],[1,1]]`;
- indices `(4,17)` and `(13,15)`: `[[3,3],[3,3]]`;
- indices `(2,6,10)`: `[[3,1,1],[1,1,−1],[1,−1,3]]`.

The two-by-two blocks have rank one and are PSD. The three-by-three block has successive exact Schur pivots `3, 2/3, 0`, with a zero residual row at the last pivot, hence is PSD of rank two. The remaining positive singleton entries are `(0:1), (12:1), (18:3), (19:3)`; the other singleton entries at indices `3,8,9,14,16` vanish. Therefore `R^Γ ≥ 0` and its rank is `4+2+4=10`. This construction is independently reproduced by the finite control in §Controls, rather than inferred from the author's checker.

## Projectors, integer witness, and pairing

The orthogonal projectors are

```
P_R = [A]/3 + ([B]+[D]+[C]+[E])/2 + [F]+[G]+[I]+[H],
P_K = I_20 − P_R,             P_K0 = P_R − [A]/3.
```

They project respectively onto `range R`, `ker R`, and the eight-vector part of `range R` orthogonal to `A`. Since all basis vectors have integer entries and the only denominators are 2 and 3, `18·10^11 P_K + 18 P_K0` has integer entries; `[A]` is integral as well. Thus

`W = 18·10^11 P_K + 18 P_K0 − 58[A]`

is integer Hermitian. Orthogonality gives `Tr(P_K R)=0`, `Tr(P_K0 R)=31−3=28`, and `Tr([A]R)=||A||^4=9`. Therefore

`Tr(W R)=18·28−58·9=−18`, and `Tr(W R/31)=−18/31`.

On the direction `A`, `W` itself has negative expectation `−522`; consequently the rank restriction in the next section is essential, not an assertion that `W` is PSD.

## Five minors and perturbation for every rank-≤2 input

For `Y=P_R X` use the unique range parametrization

```
Y = [[a,b,c,0,h], [d,a,b,0,0], [e,−d,a,f,0], [g,0,i,e,c]].
```

All variables may be complex. Direct determinant expansion yields, with zero-based row/column indices:

```
M[012|012] = a³ − ace + b²e − cd²,
M[013|123] = e(b² − ac),
M[123|014] = −c(d² + ae),
M[013|013] = e(a² − bd),
M[123|124] = c(a² + bd).
```

Substitution and cancellation prove the polynomial identity, not merely pointwise samples:

`a^4 = a M[012|012] − a M[013|123] − a M[123|014] − (c/2) M[013|013] − (e/2) M[123|124]`.

Let `X` have rank at most 2 and Frobenius norm 1, and put `E_0=X−Y=P_K X`, `u=||E_0||_F`, `t=|a|`. Each 3×3 minor of `X` vanishes. For any listed row/column submatrix, telescope `det(Y)−det(X)` one column at a time. Each of the three terms contains one restricted column of `E_0`, with norm at most `u`, and two restricted columns from either `X` or `Y`, each of norm at most 1 because `||Y||_F≤||X||_F=1`. Hadamard's determinant inequality therefore gives `|M(Y)|≤3u` for each of the five minors. Orthogonality of the source vectors and `||Y||_F≤1` give `|a|,|c|,|e|≤1`. Consequently

` t^4 ≤ 3u(3|a|+|c|/2+|e|/2) ≤ 12u`, hence `t^8 ≤ 144u²`.

There is no real-variable restriction here: the determinant is polynomial in the entries and the bounds use complex moduli.

## Uniform rank-two margin: complete case split

Set `s²=||P_K0 X||_F²` and `α=10^−11`. Orthogonality gives

`1=u²+3t²+s²`, and, using `<A|X>=3a`,

`<X|W/(18·10^11)|X> = u²+α(s²−29t²)`.

The following exhaustive cases apply to every unit rank-≤2 `X`:

1. **`s²≥30t²`.** Then `s²−29t²≥s²/30`, and `1≤u²+(11/10)s²`. Since `α≤33`,
   `u²+α(s²−29t²) ≥ u²+αs²/30 ≥ (α/33)(u²+(11/10)s²) ≥ α/33`.
2. **`s²<30t²` and `u²≥1/2`.** Since `t²≤1`, the expectation is at least `1/2−29α ≥ α/33`. The exact difference from `α/33` is `824999999521/1650000000000 > 0`.
3. **`s²<30t²` and `u²<1/2`.** The norm identity gives `1<u²+33t²<1/2+33t²`, so `t²>1/66`. The determinant bound gives `u²>1/(144·66^4)`. Therefore the expectation is strictly greater than `1/(144·66^4)−29α ≥ α/33`. The exact last-comparison slack is `40388093/533664450000000000 > 0`.

Multiplying by `18·10^11` yields `18·10^11 α/33=6/11`. By homogeneity,

`<X|W|X> ≥ (6/11)||X||_F²` for every complex matrix `X` of rank at most two, including `X=0`.

## Map, detection, and Schmidt-number consequence

Define `Φ_W(|i><j|)=Σ_bd W_(i,b;j,d)|b><d|` as in the packet. For vectors `v=Σ_ki v_ki|k,i>` in `C²⊗C⁴` and `z=Σ_kb z_kb|k,b>` in `C²⊗C⁵`, set `X_ib=Σ_k conjugate(v_ki) z_kb`. Then `rank X≤2` and direct index expansion gives

`<z|(id_2⊗Φ_W)(|v><v|)|z> = <X|W|X>`.

Conversely, every rank-≤2 `X` has such a factorization. Thus the displayed bound proves 2-positivity. The Choi matrix of `Tr(.) I_5` is `I_20`, so `Φ_W−(6/11)Tr(.)I_5` is 2-positive: this is the precise strict-margin assertion.

For a decomposable Choi witness `W=P+Q^Γ`, `P,Q≥0`, and a PPT `R`, one has `Tr(WR)=Tr(PR)+Tr(QR^Γ)≥0`. The negative value `−18` therefore proves indecomposability. Since a state of Schmidt number at most two is a convex sum of rank-≤2 vector projectors, the same negative pairing shows the explicit PPT state `R/31` has Schmidt number at least 3. This is a 4×5 conclusion only; it does not settle the unrestricted 4×4 target.

## Fixed-pair link gap: exact finite matrix and rank argument

For `T∈C^(5×5)` write `Q_V(T)=Tr[V(I⊗T)R(I⊗T)^*]`. Let the nine source vectors be `v_j` with the above weights `w_j`, and for index `(p,q)` define `U_(j,pq)=(I⊗|p><q|)v_j`. Construct, directly from the nine displayed vectors and `P_K`,

`(L6)_(pq,rs)=6 Σ_j w_j <U_(j,pq),P_K U_(j,rs)>`.

For row-major `t_(pq)=T_pq`, `t^* L6 t=6 Q_PK(T)`. Set `u=vec(I_5)`, and `H=5L6−15I_25+3uu^*`. The following explicit integer blocks are obtained by the stated formula, not by importing the author's link checker. All off-block entries vanish. In row-major indices, the block on `(0,6,12,18,24)` is

```
[ 68 −22  −7 −42   3 ]
[−22  38 −22   3   3 ]
[ −7 −22  68   3 −42 ]
[−42   3   3  33   3 ]
[  3   3 −42   3  33 ]
```

Its exact successive Schur pivots are `68, 525/17, 675/14, 3/2, 0`, with zero residual row at the last pivot. The two remaining nonsingleton blocks are

```
indices (1,7):  [[35,5],[5,155]],    pivots 35, 1080/7;
indices (5,11): [[155,−5],[−5,35]],   pivots 155, 1080/31.
```

The 16 singleton entries, `index:value`, are

`2:75, 3:30, 4:45, 8:120, 9:120, 10:75, 13:45, 14:30, 15:90, 16:45, 17:150, 19:120, 20:150, 21:45, 22:90, 23:120`.

All nonzero pivots are positive, and the zero pivot has a zero residual row, so `H≥0`, rank `4+2+2+16=24`. Moreover `(I⊗I)v_j=v_j∈range R`, so `L6 u=0`. From `H≥0` it follows that

`L6 ≥ 3(I_25−uu^*/5)` and hence `Q_PK(T) ≥ (1/2)(||T||_F²−|Tr T|²/5) = (1/2)||T−(Tr T/5)I_5||_F²`.

If `rank T≤4`, let `P` be the orthogonal projector onto `range T`. Then `PT=T`, and Hilbert–Schmidt Cauchy–Schwarz gives `|Tr T|=|Tr(PT)|≤||P||_F||T||_F≤2||T||_F`. Therefore `Q_PK(T)≥(1/10)||T||_F²`.

Also `R≤6I` and

`Q_[A](T)=<(I⊗T)^*A|R|(I⊗T)^*A> ≤ 6 Σ_(i=0)^2 ||T^*|i>||² ≤ 6||T||_F²`.

`P_K0` and the other positive terms may be dropped when forming lower bounds. Consequently, for rank-≤4 `T`,

```
Q_W(T) ≥ (18·10^11/10 − 58·6)||T||_F²
       = 179999999652 ||T||_F² > 0  for T≠0.
```

For the distinct fixed expression `W_cand=300P_K+(3/10)([B]+[D]+[G]+[I])−(3/5)[A]+(3/100)I`, the same reasoning gives

`Q_W_cand(T) ≥ (300/10−(3/5)·6)||T||_F² = (132/5)||T||_F² > 0` for nonzero rank-≤4 `T`.

The second bound is an algebraic link statement and does **not** establish that `W_cand` is 2-block positive. Because no nonzero rank-≤4 `T` gives a negative link for either specified witness with this specified `R`, neither fixed pair meets the negative rank-≤4 condition for the stated Bob-side filter bridge. This is not a no-go theorem for other witnesses, other sources, or all 4×4 constructions.

## Controls, receipts, and intended-reason negatives

Both controls were independently written in this wave directory, with standard-library exact integer/Fraction arithmetic. They do not open, run, import, or compile author code. Each was run under a 120-second command cap; neither timed out. The second imports only the first **reviewer-owned** script to display its finite blocks.

| Control | SHA-256 | Native clock before → after | Exit | Exercised result |
|---|---|---|---|---|
| `reviewer-exact-controls-v1.py` | `6aca552f39fe454996af73b355d094196ff5dae614c68785d00f6cb69c8cbeee` | `/bin/date`: `2026-10-29T13:15:52-0700 PDT` → `2026-10-29T13:15:53-0700 PDT` | 0 | Orthogonality, source and PPT Schur ranks, integer witness and pairings; polynomial expansion; exact case slacks; all 25×25 link Schur pivots. |
| `reviewer-link-blocks-v1.py` | `a6021e2f85fdbbde730e0a28c69a83af2f2ae65d65306a15ff20a56ecd0f3cc8` | `/bin/date`: `2026-10-29T13:16:15-0700 PDT` → `2026-10-29T13:16:15-0700 PDT` | 0 | Re-executed the reviewer-owned construction and printed the exact `R^Γ` and `H` blocks displayed above; the imported reviewer script was also measured at the same hash. |

Concrete controls include the rank-two input `|00>+|11>` with squared norm 2 and witness value `1199999999768`, and rank-three `A` with value `−522`. Intended-reason negative controls were:

- Flip the last sign in the five-minor identity: the residual is `a²ce+bcde`, nonzero for `a=c=e=1,b=d=0`.
- Change the source weight of `[C]` from `+3` to `−3`: its expectation on `C` becomes `−12`, so PSD correctly fails.
- Change the detector coefficient `−58[A]` to `−56[A]`: its source pairing becomes zero, not negative.
- Drop the rank restriction from the `1/10` link bound: `T=I_5` has rank 5, `Q_PK(I_5)=0`, but the claimed lower side would be `1/2`.
- Falsely strengthen the all-`T` gap constant from `1/2` to `10`: for `T=|0><1|`, the control gives `(L6)_(01,01)=10`, so `Q_PK(T)=5/3<10` while the centered squared norm is 1.

These finite controls check the displayed identities and PSD matrices; they do not replace the universal determinant, case, or rank/trace proofs.

## Imports, remaining gap, and deviations

The only mathematical tools used beyond direct arithmetic are elementary finite-dimensional Hermitian spectral/projector facts, the determinant multilinearity and Hadamard bound, Hilbert–Schmidt Cauchy–Schwarz, rank factorization, and the Choi/decomposable-witness correspondence, whose relevant quadratic-form and PPT implications are displayed above. No named theorem from a linked body or from the disposition is imported into this 4×5 argument. The packet's external literature attribution was not checked. The fixed-pair link gap leaves the original unrestricted 4×4 question and other possible pairs open; the older witness's 2-block positivity is also not established here.

**Contract deviations:** none identified. No source or infrastructure was mutated; no author code, external search, other model/API, sibling review, solver exclusion, or held material was used. The initial truncated manifest line was re-read in full before the input-body sequence. This is **same-harness review**, not human review, independent-model-family review, formal/kernel verification, or novelty verification.
