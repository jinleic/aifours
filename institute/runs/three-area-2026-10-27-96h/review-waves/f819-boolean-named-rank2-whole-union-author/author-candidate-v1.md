# F819 — named actual-rank-two m116 obstruction union, conditional on exact imports

**Status.** Fresh, nonblind same-harness GENERAL AUTHOR written candidate, **not parent-adopted or independently reviewed**. At the precise common-object interface below, the proposed uniform parity argument is valid as reconstructed here, including `alpha=0`, all possible numbers of odd graph rows, and either two-E graph occupancy. Combined with the separately adopted even-`d_E`, whole-graph `d_E=0`, and `d_E=4` dispositions at their stated imports, it gives the named conditional obstruction. The named theorem is **not** a theorem about every unnamed rank-two caller, all five-span objects, `V`, or NL242. The import and source-identification bridges remain material obligations.

## 1. Quantified statement and the exact common object

For **every** actual normalized rank-two m116 physical object of the named five-span interface, and **every prescribed original-DC transported character `t` for that object** for which all the following imports hold simultaneously, no such object exists:

1. There is one physical `f/R, a, g, u, x=U0, y=U3`, with `u` ternary, the stated actual inverse and actual physical graph/mate identification. This is the named rank-two normalization, not separately chosen X-profiles, phases, graph and mate arrays, or Y-spectra. The support count is m=116. The local invariant `H_loc` is the number of `U1=0` blocks with a single `|U0|=4` peak, and `H_loc=0`; it is **not** the radical plane also denoted H in graph coordinates. Retain the named class counts: four `D0`, eighteen `D3`, six `Z2`, one `Z4`, and seventeen `Z0`, plus the actual graph and two full sites.
2. In the imported physical coordinates write `(ell,h,i,b) in F2 x F2 x F2^2 x F2^2`. The two full sites are `(0,h,0,0)`; the six E sites are `(0,h,i,0)` with `i != 0`; the 24 Z sites have `ell=0,b != 0`. The 16 graph sites are `(1,F_i,i,b)`, their mates are the **same physical `i,b`** at `(1,1+F_i,i,b)`, and `sum_i F_i=1` in F2. The four D0 sites lie among the six E sites and 16 graph mates. At graph sites `|x|=|y|=1`; at D0, `|x|=2,y=0`; at D3, `x=0,|y|=2`; at Z2, `|x|=|y|=2`; at Z4, `x=0,|y|=4`; at Z0, `x=y=0`; at the full sites `x=0`. The Z4 is the unique physical Z4, not a virtual location.
3. The **specific carried** `t` satisfies `xhat(t)=0`; it is not chosen or changed independently to arrange a desired slice. Set `X=(-1)^t x` and `Y=(-1)^t y` on this same object, so both complete spectra translate together. Retain all 64 actual U0 divisibilities and caps `<=8`. For

   `Z_(ell,i)(s,alpha) = (1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha(b))`,

   all eight zero-profile entries `Z_(ell,i)(0,0)` vanish. Each of the other seven columns, simultaneously for this X, is either a singleton `+/-2` or four `+/-1` values on one affine two-flat of `(ell,i)`, with four-sign product `-1`.
4. Retain the actual physical phase and general-`g` bridge, not free row covectors: on the graph, `Y=-a g X` and its sign multiplier is, after fixed row signs, `(-1)^(q(b)+lambda_i(b))`, where `q(b)=b_0 b_1` and the four `lambda_i` are the four distinct covectors of `(F2^2)^*`, hence `sum_i lambda_i=0`. This is the actual common phase of the named object. The general-`g` foundation has `g=4` at the two full E-plane sites, `g=-2` at the six other E sites, `g=0` at `ell=0,b != 0`, and the recorded general B-coset form for the arbitrary admissible `f/R`; it is not an example-specific choice. The physical inverse, normalization, and that graph-phase/residue connection are **imports**, not newly derived source or caller equivalences here.
5. The same Y has squared energy 128; `J=1` with the actual general-`g` bridge gives **every** full Walsh coefficient residue `4 mod 8`; all 64 actual common-U3 coefficients have absolute value `<=12`. The transported Y has the same energy, all residues and all caps. No bound is added for either individual full-site Y value.

The quantifiers do not say that an original caller automatically satisfies these imports; rather, the conclusion is conditional on all of them holding together for one actual object and its prescribed t. The descriptions above expose the hypotheses used in the proof and retain the source, phase, inverse, gauge and collateral boundaries of S2–S5. In particular, neither `H_loc=0` nor the displayed local class table identifies every undisplayed original-atom condition.

Let `d=d_E` count the four D0 sites on the six E sites, and let `k_i` count them among graph mates in row i. Then `0<=d<=4`, `0<=k_i<=4`, and `sum_i k_i=4-d`. The claimed obstruction has no omitted E allocation: for `d=2` the two E sites can lie in one E row or in distinct E rows, and the two graph mates can lie in one row or in two distinct rows. All actual locations, signs, odd F tables and admissible phases are retained.

## 2. Actual-X parity identity, uniformly in even `d`

Write `V=F2^2` for the physical b-space, identify its dual by the displayed coordinates, and set `Q(v_0,v_1)=(v_1,v_0)`; the same coordinate swap is used on covectors. For each graph row define

* `S_i(b)=X(1,F_i,i,b) in {+1,-1}`;
* `D_i` as the actual b-set of D0 graph mates in that row, with mate values `2 epsilon_i(b)` for `b in D_i`;
* `P_i` as the XOR of the b-positions where `S_i(b)=-1`; and
* `B_D=sum_i sum_(b in D_i) b`, all these sums in `V`.

The actual zero profile gives, row by row,

`sum_b S_i(b)+2 sum_(b in D_i) epsilon_i(b)=0`.  (2.1)

For every nonzero b-covector alpha, the graph-half support of the same `(s,alpha)` profile has even parity: an affine two-flat meets the graph half in 0, 2, or 4 positions, whereas a singleton has even entry `+/-2`. This holds for all four rows **on the same X**, including a possible graph singleton. Here is the exact implication used, rather than an assumption about individual row offsets. Let `n_i(alpha)` count negative graph signs at the two b-points with `alpha(b)=1`, and put `R_i(alpha)=sum_(b in D_i, alpha(b)=1) epsilon_i(b)`. From (2.1),

`Z_(1,i)(0,alpha)=n_i(alpha)-1-R_i(alpha)`.

Modulo 2, summing over the four rows cancels the four constants and turns both sign sums into location parities. Since the graph-profile sum is even,

`alpha(sum_i P_i+B_D)=0` for every `alpha != 0`, hence `sum_i P_i=B_D`.  (2.2)

No conclusion is drawn here that odd-row offsets agree, empty-row covectors agree, or a particular N-type is impossible.

Suppose now that `d` is even. Since `sum_i k_i=4-d`, the number `o` of rows with odd `k_i` is even, as is `e=4-o`. Equation (2.1) gives the following exhaustive graph-row forms:

* if `k_i` is even, `S_i=sign_i (-1)^xi_i` for a b-covector `xi_i`, including `xi_i=0`; then `P_i=Q xi_i`;
* if `k_i` is odd, `S_i=sign_i (2 1_(b=gamma_i)-1)` for a unique exceptional b-position `gamma_i`; then `P_i=gamma_i`.

For the even case the graph sum is `0` or `+/-4`, so every row is a signed affine character. For the odd case it is `+/-2`, giving the signed 3:1 row. The stated XORs follow because the XOR of all four b-points is zero, and the XOR of the two points of a nonconstant affine-character sign class is `Q xi_i`.

The **same physical phase** therefore gives a bent graph-Y row with covector `theta_i=lambda_i+xi_i` in an even row, and an affine graph-Y row with covector `kappa_i=lambda_i+(1,1)+Q gamma_i` in an odd row. The latter formula follows from `2 1_(b=gamma)-1 = sign (-1)^(q(b)+((1,1)+Q gamma)(b))`. Using (2.2), `sum_i lambda_i=0`, and even `o`,

`sum_(i even) theta_i + sum_(i odd) kappa_i = Q B_D`.  (2.3)

This applies uniformly at `d=0,2,4`, including zero even rows; it is not a claim that every graph-row profile or every d is physically realizable.

## 3. Whole-slice parity of the one actual Y

For `s in F2`, `alpha in V*`, `beta in (F2^2_i)*`, define

`A_ell(s,alpha,beta)=sum_(h,i,b) Y(ell,h,i,b)(-1)^(s h+alpha(b)+beta(i))`.

There are `12+d` actual D3 graph mates. Let `m_alpha` be the number of odd graph rows with `kappa_i=alpha`, and let

`v=B_D+Q sum_(i even) theta_i` in V.  (3.1)

For each even row the b-Walsh transform of its bent graph-Y row is `2` times a sign with exponent `q(alpha+theta_i)` plus its row, s and beta signs. An odd graph-Y row contributes zero or `+/-4`, occurring precisely at `alpha=kappa_i`. Every D3 mate contributes `+/-2`. Thus the `N=(12+d)+e` magnitude-two terms have even N, and `A_1` is divisible by 4. The parity of half their sign sum is `N/2` plus the number of negative signs; that number is determined by the product of the actual N signs. The odd-row magnitude-four terms add `m_alpha` modulo 2. Expanding that single sign product gives

`A_1(s,alpha,beta)/4 = c+s+m_alpha+alpha(v) (mod 2)`  (3.2)

for one object-dependent bit c. Explicitly, the beta exponent is

`sum_(i even) i + sum_i (4-k_i)i = sum_i i = 0`;

the s exponent is

`sum_(i even) F_i + sum_i (4-k_i)(1+F_i) = sum_i F_i+o = 1`.

In the alpha exponent, the even number of bent rows cancels the common `q(alpha)` term. Their remaining linear term is `alpha(Q sum_even theta_i)`. The XOR of all actual D3 mate positions is `B_D`, since the XOR of all four b-positions in each graph-mate row is zero. All row, mate and quadratic constants are absorbed into c. No sign in this calculation is independently selected.

Equation (2.3) yields

`sum_(i odd) kappa_i=Q v`.  (3.3)

Set `f(alpha)=m_alpha mod 2`. Because `o` is even, its support has size 0, 2, or 4. If the support is empty or all of `V*`, f is constant and its support XOR is zero, so (3.3) forces `v=0`. If it has two points, their nonzero difference is `Qv`; their indicator is the affine-line function `f(alpha)=c_0+alpha(v)`. Indeed `(Qv)(v)=0`, so this nonzero linear form has exactly that difference as its kernel. The case of repeated kappa values is included by taking multiplicity modulo 2; the all-four-odd-row case is included as well. Consequently `f(alpha)+alpha(v)` is constant on all four alpha values, **including alpha=0**. From (3.2), for one fixed bit `c'` attached to the physical object,

`A_1(s,alpha,beta)/4 = c'+s (mod 2)`  (3.4)

for every `s,alpha,beta`. Thus one entire s-slice is even and the opposite entire s-slice is odd. The result applies to this one transported Y; it does not permit changing t, the common phase, D3 mate signs, or coefficients frequency by frequency. It does not itself exclude `d=0` or `d=4`.

## 4. Entire `d=2` obstruction on the same physical Y

At `d=2` there are 14 actual D3 graph mates, and the physical `ell=1` spatial squared energy is `16+14*4=72`. For each `(s,alpha,beta)` the two full Y coefficients are `A_0+A_1` and `A_0-A_1`. Their two caps are equivalent to `|A_0|+|A_1|<=12`. Their common residue `4 mod 8` makes `A_0/4` and `A_1/4` integers of opposite parity. Every full coefficient has magnitude 4 or 12, and full Parseval gives exactly eight of magnitude 4:

`16 N_4+144(64-N_4)=64*128`, so `N_4=8`.  (4.1)

There are 16 `(alpha,beta)` in each s-slice. By (3.4), the even-slice `|A_1|` values are 0 or 8, and the odd-slice values are 4 or 12. Let n count the even-slice 8s and m the odd-slice 4s. Partial Parseval on the 32 ell-one sites yields

`4n+m+9(16-m)=(32*72)/16=144`, hence `n=2m`.  (4.2)

The exact pair possibilities and counts of full magnitude-4 coefficients are:

| `|A_1|` | permitted `|A_0|` | number of magnitude-4 full coefficients |
|---:|---:|---:|
| 0 | 4 or 12 | 2 or 0 |
| 8 | 4 | 1 |
| 4 | 0 or 8 | 2 or 1 |
| 12 | 0 | 0 |

Let h count the odd-slice 4s with `A_0=0`, and z count even-slice zero-`A_1` pairs with `|A_0|=4`. The exact budget is

`8=n+m+h+2z=3m+h+2z`, with `0<=h<=m`.  (4.3)

It forces `m<=2`, and the possible `(n,m,h,z)` are `(0,0,0,4)`, `(2,1,1,2)`, `(4,2,0,1)`, `(4,2,2,0)`. In every case the **entire one actual odd slice** has at most two nonzero `A_0` values, each of magnitude 8. If its s-value is `s_*`, inverse Walsh transform in the 16 `(i,b)` positions gives, for every physical `(i,b)`,

`|Y(0,0,i,b)+(-1)^s_* Y(0,1,i,b)| <= (2*8)/16=1`.  (4.4)

At the unique actual Z4, the physical b is nonzero, and the opposite-h site with the **same** i,b is a different Z site of magnitude at most 2. The same left-hand side is therefore at least `4-2=2` in absolute value, contradicting (4.4). No bound on the full sites is needed. This excludes every `d=2` object under the listed imports, whether the graph D0 occupancy is 2 or 1+1 and whether the E allocation is 2 or 1+1. It does not rest on selecting one E allocation, lambda branch, spectrum, or physical example.

## 5. Exact union and dependencies

* From S2's separately adopted even-E theorem, or equivalently from the same zero-profile interface: the six Z2 X entries and the `d` E-D0 X entries are the `6+d` nonzero ell-zero X sites, each of magnitude 2. Every ell-zero row has signed sum zero, so the total support count is even. Thus `d` is even. This excludes `d=1,3`; it does not assert feasibility of any remaining case.
* S4 separately adopts the **whole** `d=0` obstruction at the same named actual-object/inverse, local-H/count, prescribed-t, simultaneous-profile, phase/residue/J and common-Y-cap imports. It covers all five graph partitions `4`, `3+1`, `2+2`, `2+1+1`, `1+1+1+1`; it is not replaced by the parity lemma above. In particular S4's physical 2+2 forcing and the prior location-specific four-distinct result are imported at S4's own full scope, not reconstructed from the arithmetic census. Its finite corroboration has the qualifications recorded in S4.
* Section 4 excludes `d=2` at the same imports. S6 independently records the already adopted **split** `1+1` subcase; S7 is an unadopted written double-row author candidate and S8 is its split-row counterpart. They are useful nonblind packet context, not a new adoption. The uniform proof above includes both and does not assert that S9's finite local run proved the common full-Y obstruction.
* S5 separately adopts the whole `d=4` actual-common-Y obstruction, covering the E-singleton and E-plane lambda alternatives. It too is used only at its explicit actual physical, same-t and common-Y interface. Its written and finite scopes are those S5 states, not any larger source/caller scope.

All possible actual E counts are `0,1,2,3,4`; the evenness result excludes the odd counts, and the remaining three cases are excluded as above. These imports apply to the **same hypothetical object and the same prescribed t**, so the case distinction proves the conditional quantified no-object statement in Section 1. It is a new author-candidate union pending separate parent full read and scrutiny, not an automatic change to any earlier disposition.

## 6. Open frontier and assurance boundary

This obstruction pays only the explicitly named actual-rank-two m116 interface. Still unpaid are: an independently justified bridge from the printed/original problem and every relevant original five-span caller to precisely these physical classes, this rank-two normalization and its chosen original-DC transport; the original selected-`T`, rank and eight-zero reconstruction; all other ranks and any cases outside the local-H/count/phase/inverse/seven-profile/common-Y premises; all relevant collateral original-atom equivalences; and the original `V` complement/odd-cap constraints. Nor does it establish the full original five-span theorem, NL242, a positive witness, or equivalence of any unnamed caller. The `d=0` and `d=4` dependencies are imported scoped dispositions, not direct rereads of their linked underlying bodies. `H_loc=0` is not an authentication of a separate historical class table. Original-source identity, novelty, external-family, human and kernel/formal verification are not claimed.

S9 records one earlier parent-run `PASS_FINITE_LOCAL_NECESSARY_ONLY`: graph-projection and factorized residue scopes, not enumeration of common ell-zero X or full Y, and no certification of the physical inverse, actual phase, U3 cap, J, Z4, original caller or global theorem. That receipt is historical context, not execution of this candidate. S4's partial and local finite evidence and S5's finite factorization retain their own stated limitations. No old code, outgoing linked source, held episode or consumer is used as scientific input.

## 7. Complete packet and process coverage

Before the direct PREBODY ACK I read the complete manifest, freeze receipt, final binding, parent-live metadata supply, actual dispatch receipt, and all 22 manifest-listed status/permission controls. The controls concern status and permissions only. The ACK to Main named those controls and the single ordered part, and disclosed that no body or mathematics had yet been read/performed. After the ACK I read packet part 01 serially in raw windows `1–20, 21–40, ..., 701–720, 721–726`, including its ending and long lines, **before** mathematical work. Memory summary and the named protocol skills were read first as globally required. Administrative control file order was not mandated. No prior claim-specific scientific source was opened in this worker before the ACK; no clean-cognition certificate is inferred.

The one part has **726 LF**, parent-supplied SHA-256 `dda72dbf247a007ac66964ecb62625c370fc62d9aa16f10b7fb6483335450d3c`. The complete packet renders all nine following bodies, with parent-supplied SHA-256 pins and complete source LF counts; no direct-source re-hash or outgoing link follow is asserted. Paths are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`.

| ID | Complete rendered source | LF | Parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `parent-boolean-even-E-common-slice-and-two-E-uniform-candidate-v1.md` | 25 | `18c308d0416d44d4811e1485f849272f4098da69545a378776a3206752579baf` |
| S2 | `dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md` | 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S3 | `parent-recovered-local-H-definition-and-general-g-foundation-v1.md` | 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |
| S4 | `dispositions/info-6-entire-all-graph-D0-obstruction-and-two-E-residual-parent-v1.md` | 29 | `b8f74cc8316ce476cac0de23b82b626b99e1f526a54c1042cebbdd66c8a19c2e` |
| S5 | `dispositions/info-6-entire-four-E-row-d0-actual-common-y-obstruction-parent-v1.md` | 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S6 | `dispositions/info-6-two-E-split-graph-D0-entire-common-y-obstruction-parent-v1.md` | 17 | `6d0e6e3bc961fed11d047928a0f32b10c8011debe5642fbe2a12971cfc22d062` |
| S7 | `review-waves/f789-boolean-two-E-one-double-graph-author/author-candidate-v1.md` | 200 | `db6343f98e598ffbe8c480175bbef6d3aeaac4f1b69766c360e5841121679dd5` |
| S8 | `review-waves/f788-boolean-two-E-one-plus-one-graph-author/author-candidate-v1.md` | 179 | `1c51df762a1878cae342b32b4a34fead49ca39c2813bdab41ba3e7a9ed3b737d` |
| S9 | `review-waves/f803-boolean-two-E-split-graph-finite-source-author/parent-split-v2-run-v1-receipt.json` | 142 | `9dfe7696d76b3b46f91bf8b4bbda9fd21540bb546320bb9364e7d09bab03dbb3` |

All genuinely held episodes and **all** their proof, method, selection, planning, verification, reporting, confidence and downstream consumers remain NONINPUT. No child scientific program, test, solver, compiler, CAS, external CLI, old code, unlisted scientific source, outgoing link, network, Git, installation or deletion was used. No new source was assigned or created; no finite check, scientific execution, parent adoption, independent family, human review or kernel certification is asserted.
