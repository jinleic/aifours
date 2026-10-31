# f255 independent same-harness review: cross-fibre placement

## Overall disposition

**0 FATAL / 1 MAJOR / 1 MINOR. Original-Boolean-object necessity: INCONCLUSIVE at this frozen input scope.** The placement, parity, and sign-mismatch conclusions are mathematically supported **conditional on** the displayed common inverse/local-Walsh system and its stated normalization. I independently reconstruct their finite and algebraic consequences below. I found no counterexample within those conditional hypotheses, but the candidate does not derive the indispensable bridge from the original Boolean hypotheses to that system, and the only adopted disposition does not explicitly provide the bridge. This is a proof-input gap, not a counterexample to the proposed necessity.

The formal placement is not a block realization or Boolean witness. The `(G3,H)=(1,0)` residual, the other six f244 integer-relaxation pairs, `(0,4,8)`, rank two, and the full balanced NL242 target remain OPEN. This review is same-harness written/exact-control work, not human, independent-model-family, formal/kernel, or novelty verification.

## Frozen input and exposure record

Manifest `manifest-v1.json`: SHA-256 `ccd41880d913a0ae12913dcde161533e41ddf6234dff7f3acab1432e81aa4fd6`, verified before displaying it. Both input identities were verified before displaying either source:

1. Adopted f244 parent disposition, SHA-256 `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912`, 4,246 bytes, 24 LF. Read raw 1–15, then 16–24, including its ending.
2. Cross-fibre candidate, SHA-256 `686dd9177d6ff8788b6463d8d4e444e8bda4231ce7060a76ad0cfdea5f39144c`, 13,894 bytes, 183 LF. Read raw 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, and 181–183, in that order, before mathematical work.

Only explicit f244 statements are adopted. Its linked author and reviewer bodies were not opened; neither was the candidate's second cited disposition. f239, CR7, f161/f162, the withdrawn roster, held/withdrawn bodies, author code/PASS/solver, other review output, external models/APIs, Git, deletion, and publication were not inputs or actions.

## Per-claim verdicts

| Claim | Verdict and exact scope |
|---|---|
| The original Boolean hypotheses imply the common system used in candidate (1), the stated fibre values, and its normalization | **M1; INCONCLUSIVE.** The premise bridge is neither supplied explicitly by the frozen f244 disposition nor derived in the candidate. |
| Rank-three four-atom transform, its zero set, 23-point `B3`, and common-hyperplane count | **0F/0M/0m conditional on the common system.** Reconstructed below without adopting an undefined block-type lookup; f244 explicitly supplies the relevant eight-atom relation/23 count. Original-object application remains subject to M1. |
| `X2=X3≠0` and `Π2=Π3` | **0F/0M conditional; m1 in the explanation of the mod-4 expansion.** The stated equality is correct for the actual cardinalities 4 and 8. Original-object necessity remains subject to M1. |
| Every translated four-atom support meets the eight-atom support in at most two points | **0F/0M/0m conditional.** The geometric-line proof and all-translation step reconstruct; exhaustive canonical finite controls found no counterexample. Original-object necessity remains subject to M1. |
| All-translation mismatch condition (S) | **0F/0M/0m conditional.** Both mod-4 signed sum and XOR are derived, with exact quantifiers below. Original-object necessity remains subject to M1. |
| Explicit placement and signs | **0F/0M/0m for the limited formal example.** It meets all tested restrictions, and demonstrably fails the local ternary equations. It is not a witness. |
| Full exclusion, another class-count pair, other ranks, original target, or novelty | **INCONCLUSIVE / not claimed or tested.** |

## M1 — missing Boolean-to-local-system bridge

Candidate §2 says the f244 disposition supplies the fibre-transform facts and

`16 U_s(c) = 3 Walsh_R(σ_s)(c) − 2 t_s(c)`, with `t_s=Walsh_R(σ_s 1_{A_s})`.  (1)

However, the actual 24-LF disposition does not state (1), define `k`, `σ_s`, the normalization of `U_s`, or explicitly say that the relevant fibre values are exactly `k=2σ_s(3−2·1_{A_s})`. It names the block types, `m`, `e_s`, and an eight-atom transform, but does not give the full inverse/normalization connecting them to the original Boolean object. The candidate asserts (1), rather than deriving that link. Its bibliography additionally names a caller disposition that is **not** among this manifest's inputs; I did not open it or use its contents. The fact that the adopted f244 disposition reports a prior proof or mentions other identities does not make those unstated identities premises here.

To close M1, supply a literal, explicitly adopted statement establishing the Boolean-to-`u,k,U_s` definitions, normalizations, ternary values, `m=Σ u²`, and (1), or derive those facts from the frozen Boolean assumptions in the candidate. Then the conditional reconstruction below can be re-evaluated at the original-object scope. This finding does not say that (1) is false or that the proposed theorem has a counterexample.

## m1 — parity expansion needs a multiple of four, not just an even count

For an even atom count `e` and `n⁻` negative atom signs, the general identity is

` t(c)/2 ≡ e/2 + n⁻ + X·c (mod 2) `.

Candidate (3) is correct here because `e2=4` and `e3=8`, so `e/2` is even. Its introductory explanation mentions only evenness, which by itself does not imply the displayed formula: two positive atoms at `c=0` give `t(0)/2=1` but `n⁻+X·0=0`. This is a clarity/generalization defect, not a counterexample at the candidate's 4/8-atom scope.

## Independent conditional reconstruction

The following derivation explicitly assumes the missing bridge's local system: `u(c,·)∈{−1,0,1}^4`, `m=Σ_{c,y}u(c,y)^2=116`, `U_s` is its four-point Walsh transform, (1) holds for the three nonzero fibre labels, `|A1|=0`, `|A2|=4`, `|A3|=8`, and the adopted f244 eight-atom relation and 23-divisible-position statement hold. No statement from the unlisted caller body is used.

### 1. Local parity, rank, and the common zero count

For each nonzero `s`, since `(3−2·1_A)^2=9−8·1_A`, six-dimensional Parseval in (1) gives

`Σ_c U_s(c)^2 = 144−2|A_s|`,

namely 144, 136, 128 for `s=1,2,3`. Four-point Parseval and `m=116` give `Σ_c U_0(c)^2=4·116−(144+136+128)=56`.

Since `A1=∅`, (1) makes every integer `U1` divisible by 3. Its four-point range gives `U1∈{0,±3}`. The energy 144 gives exactly 16 nonzero `U1` blocks. In each such block, exactly three of the four ternary entries are nonzero and the other three local transforms have absolute value 1. In all other 48 blocks, `U1=0`, so every local transform is even. Consequently neither `U2` nor `U3` can equal ±3, and reduction of (1) modulo 3 yields the exact equivalence

`U_s(c)=0  ⇔  t_s(c)≡0 (mod 3)` for `s=2,3`.

For four distinct `A2` atoms, affine rank is either two or three. A rank-two plane has `t2=0` at either 48 positions (even sign product) or zero positions (odd product). Because all 16 `U1≠0` rows have `|U2|=1`, 48 zeros would force `ΣU2²=16`, while no zeros would force `ΣU2²≥16+48·4=208`; each contradicts 136. Thus `A2` has affine rank three. Its four signed characters have 24 zeros and eight alignment positions. Write `H2={t2≡0 mod 4}` and `F2={|t2|=4}`. Then `H2` is an affine hyperplane, `F2` an affine three-flat contained in it, and `U2=0` precisely on `H2\F2`.

The f244 residual supplies 23 positions where `t3` is divisible by 3, hence 23 zeros of `U3`. The following independently recovers the candidate's 17 common zero positions without relying on unspecified meanings for the lettered block types. For a row with `U1=0`, the local ternary possibilities are: the zero row; one peak `±4` among `U0,U2,U3`; or a pair of `±2` among those three. The `U2` energy and its 24 zeros force exactly two `U2` peaks; the `U3` energy and its 23 zeros force exactly one `U3` peak.

Let `a,b,c` count the three pair types `(U0,U2)`, `(U0,U3)`, `(U2,U3)`; let `d` count `U0` peaks and `o` zero rows. Using the three energies and the 48-row total gives

`a=4−2d,  b=6−2d,  c=18+2d,  o=17+d`.

Thus `I=|{U2=U3=0}|=o+d=17+2d`. These common zero positions belong to `B3∩H2`.

### 2. Eight-atom normal form and the unique hyperplane

The adopted residual says that the eight atoms have affine rank six and one weight-four relation with even sign syndrome. Write the related plane as `{a,a+p,a+q,a+p+q}` and the other atoms as `{a+b1,a+b2,a+b3,a+b4}`, where `p,q,b1,b2,b3,b4` are independent. An affine change of dual coordinates absorbs the six independent relative signs. With `u=(p·c,q·c)` and `v=(b1·c,…,b4·c)`, up to an irrelevant signed character,

`t3=4·1_{u=0}+Σ_i(−1)^{v_i}`.

Thus

`B3={(u,v): u≠0, |v|=2} ∪ {(0,v): |v|=1 or 4}`,

of size 23, and `H*={|v| even}` contains 19 of them. For the character indexed by `(α,β)`, direct expansion gives `(3 if α=0 else −1)K2(|β|)+K1(|β|)+K4(|β|)`, where

`K2=(6,0,−2,0,6)`, `K1+K4=(5,1,1,−3,−3)`.

The only nontrivial coefficient of magnitude at least 11 is `+15` at `(0,1111)`. Hence an affine hyperplane containing at least 17 of the 23 points must be `H*`, and the maximum occupancy is 19. Since `I≥17`, `H2=H*` and `d≤1`.

No affine three-flat in `H*` is disjoint from `B3`: let `L={0,1111}` in the even `v` space. A zero-dimensional `u` projection gives a full eight-point fibre and meets `B3`; a one-dimensional projection has a nonzero-`u` four-point fibre, at least two of whose points lie outside `L`. For a two-dimensional projection, all four fibres are parallel two-point lines; if each nonzero-`u` fibre avoided `B3`, all three would equal `L`. Affineness forces the zero-`u` fibre also to equal `L`, containing `(0,1111)∈B3`. If `d=1`, then `I=19` and `B3∩F2=∅`, impossible. Therefore `d=0`, `I=17`, and

`H2=H*`, `|F2∩B3|=19−17=2`.

### 3. Equal XOR and atom-sign product

In both actual cardinalities `e/2` is even, so `(t_s(c)/2 mod 2)=n_s⁻+X_s·c`. For the rank-three four-atom set this affine function has zero set `H2`; for the eight-atom normal form it has zero set `H*`. Equality of the nonconstant affine functions' zero hyperplanes yields `X2=X3` and `n2⁻≡n3⁻ (mod 2)`, equivalently `Π2=Π3`. The plane XOR is zero and the outer XOR is `b1+b2+b3+b4≠0`, so the common XOR is nonzero.

### 4. The affine-line lemma and all translated intersections

Let `δ=(Δu,Δv)=(0,1111)` in the dual block coordinates, and `L={0,1111}`. On `H*`,

`B3 = ((F2²\{0})×(V_even\L)) ∪ {(0,1111)}`.

For a three-flat `F⊂H*` meeting `B3` in two points: projection dimension 0 gives intersection 1 or 6, impossible. In projection dimension 1, a pair of nonzero `u` fibres contributes at least four; otherwise the nonzero-`u` four-point fibre must contain `L`, so its two contributing points differ by `1111`. In projection dimension 2, each fibre is a parallel two-point line. If their direction is not `L`, the three nonzero fibres contribute at least three points; if it is `L`, a nonzero fibre contributes either zero or two, so an intersection of exactly two is one such parallel line. Hence `F2∩B3` differs by `δ`, and `δ∈dir(F2)`.

On `F2`, all four signed `A2` characters align. Their ratios are therefore constant on `F2`, so every `A2` atom has the same pairing with `δ`. All plane atoms have one value and all four outer atoms the opposite value. Thus `A2` cannot meet both parts. Three plane atoms would fix both `u` coordinates on `F2`, contrary to the dimension-0 case. Three outer atoms plus `X2=X3` force the fourth outer atom. In that all-outer case the equality of sign products and the positive plane syndrome force `F2=F2²×{v0,v0+1111}` with even `v0`; its intersection with `B3` has size 1 if `v0∈L`, otherwise 6. This contradicts size 2. Hence `|A2∩A3|≤2`.

The same proof applies to every `A2+t`: even cardinality preserves its XOR and sign product, and translating the signed atom function multiplies `t2(c)` by a character, preserving `H2` and `F2`. Equivalently, a complement shear can translate fibre 2 by arbitrary `t` and fix fibre 3. Therefore, for every `t∈R`,

`|(A2+t)∩A3|≤2`.

### 5. Exact all-translation sign mismatch

Because each `t_s` is even, (1) implies `Walsh(σ_s)` is divisible by 4. Reducing (1) modulo 8 gives

`Walsh(σ_s)(c)/4 ≡ t_s(c)/2 (mod 2)`.

The two right sides agree by the equal XOR and sign product, so `Walsh(σ2)≡Walsh(σ3) (mod 8)`. Multiplying the first transform by any character `(-1)^{t·c}` preserves its residue modulo 8, since it is already divisible by 4. Thus for **every** `t`, the transform of `d_t(r)=[σ2(r+t)−σ3(r)]/2` is divisible by 4. Evaluation at `c=0` gives `Σ_r d_t(r)≡0 (mod 4)`; comparing general `c` with `c=0` gives `Σ_r d_t(r)(c·r)≡0 (mod 2)`, equivalent to

`⊕_{r:d_t(r)≠0} r=0`.

An independent formulation makes the quantifiers explicit. Let `D_s={r:σ_s(r)=−1}`. Then `d_t=1_{D3}−1_{D2+t}`, so the signed sum is `|D3|−|D2|` and the XOR of the mismatch support is `X(D3)⊕X(D2)⊕(|D2| mod 2)t`. The full all-`t` assertion is equivalent to `|D2|` even, `|D3|≡|D2| (mod 4)`, and `X(D2)=X(D3)`. A check only at `t=0` is not equivalent.

## Formal placement and counterexample search

In coordinates `p=1,q=2,b1=4,b2=8,b3=16,b4=32`, the candidate has

`A3={0,1,2,3,4,8,16,32}`, `A2={0,1,14,51}`,

with all atom signs on `A3` positive and `A2` atom signs `+,+,−,−`. Both XORs are 60 and both sign products are positive. The alignment flat has `F2∩B3={14,50}` and its intersection is in direction 60. Every translation satisfies the intersection bound. Let `σ3` be positive everywhere and `σ2` negative exactly at `{14,51,4,57}`; the latter set has four elements and XOR zero. For all 64 translations the mismatch sum is −4 and its support XOR is zero.

At `c=0`, the claimed common equation would require `U2=(3·56−2·0)/16=21/2`, not an integer, and `U3=(3·64−2·8)/16=11`, outside a four-point ternary-transform range. Thus these supports/signs are only a formal placement and **not** an actual common block, Boolean realization, or evidence that the residual is feasible.

I searched for counterexamples to the finite geometric implication in the complete canonical eight-atom normal form, not for a full Boolean target. For all 9,920 four-atom supports with the required nonzero XOR, all eight sign assignments with the required product were covered up to global sign. Of these, 1,152 supports and 2,304 signed supports satisfy `|F2∩B3|=2`; all 64 translations of each qualified support have intersection at most two. No counterexample was found to that conditional implication. This enumeration does not bridge M1 and does not exhaust Boolean functions or prove feasibility.

Intended-reason negative controls show why the hypotheses matter: the four outer atoms satisfy the XOR/sign-product equalities but have overlap 4 and `|F2∩B3|=1`; a rank-two four-plane has zero XOR and a 16-point alignment flat; an odd outer sign product puts its alignment flat outside `H*`; a translate of the outer set can be disjoint at `t=0` yet have overlap 4 at another shift; mismatch sets `{1,2,3}` and `{0,1,2,4}` separately violate the mod-4 and XOR clauses; equal one-point negative sets satisfy (S) at `t=0` but violate its XOR clause after a nonzero translation. None is claimed as a counterexample under the complete conditional hypotheses.

## Reviewer-owned bounded exact control

`reviewer-control.py`, SHA-256 `5180127f56b60e2e15fa191bb06638e019998ce4582555177747669d801f9250`, ran once after the complete frozen reads with tool deadline 120 s. Native start and end were both `2026-10-29T15:24:03-0700 PDT`; monotonic elapsed time was 0.110752 s; the process returned exit 0. It checked 63 nontrivial characters, all 126 affine hyperplanes, all 620 three-flats of `H*` (intersection histogram `{1:2,2:18,3:57,4:228,5:90,6:210,7:6,8:9}`), the complete support/sign/translation search stated above, the 64 translations of the formal example, both local failures, and seven intended-reason negatives. This is finite arithmetic evidence only, not an original-object derivation, a Boolean witness, or formal/kernel verification.
