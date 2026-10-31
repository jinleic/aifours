# Independent same-harness review: rank-two eight-zero m=116 fibre obstruction

## Verdict, scope, and imports

**Mathematical result: supported at the frozen scope; 0 fatal and 0 major mathematical findings. One minor source-attribution/scope finding, and the execution and broader-status claims listed below are INCONCLUSIVE.** Given a balanced nine-variable Boolean function with Walsh peak at most 28, rank-two even polar, eight Walsh zeros, `m=116`, and fibre pattern `(e1,e2,e3)=(0,4,8)` up to permutation, I independently obtain `g3 != 3` and `g3=1 => H=0`. The seven pairs listed below are necessary residuals, **not realizability claims**. The whole `(0,4,8)` case is **OPEN**; this review proves neither a balanced witness nor a full exclusion, and makes no global NL242 or novelty claim.

Severity conventions: F = fatal, M = major, m = minor; `supported (0F/0M/0m)` means the indicated claim survived this review, not that it is independently-family or formally verified. INCONCLUSIVE applies when the frozen inputs do not establish the claim. The per-claim dispositions are:

1. **Target assumptions, parity, the quadratic, the `m` energy identity, `z=64` and the value 12: supported (0F/0M/0m) by the independent reconstruction in §2.** The convenient odd-coset lower bound is also reconstructed, although `m=116` and even energy alone already force `z=64`.
2. **Four-entry block table, `e1=0` reduction and signed-transform congruences: supported (0F/0M/0m), §3.**
3. **Four-atom histogram, zero-set flat geometry and global count parametrization: supported (0F/0M/0m), §4.**
4. **Eight-atom relation table and `g3 != 3`: supported (0F/0M/0m), §5.**
5. **Normal form at `g3=1`, hyperplane bound, flat obstruction and `H=0`: supported (0F/0M/0m), §6.**
6. **Seven literal residual pairs, arithmetic relaxation and open boundary: supported (0F/0M/0m), §7.** Their existence is INCONCLUSIVE; a class-count relaxation is not a common spectrum or Boolean function.
7. **Source attribution: m.** Target lines 25–27 and 166–174 refer to other adopted caller/phase dispositions, but their bodies are not declared review inputs and blanket caller/coupling imports are not themselves expressly stated in the supplied scope-only disposition. Their adoption, contents, and proofs are **INCONCLUSIVE here**, not premises. The specific identities needed by this candidate are independently derived from the original Boolean assumptions below; a parent disposition relying on this review should include or cite that derivation rather than treat the unprovided linked bodies as checked. The expressly scoped `T != 0` statement in the declared disposition is the only non-elementary adopted statement needed here; finite-field algebra, Parseval and character orthogonality are used directly. The conclusion `q|R=0` is **derived**, not adopted.
8. **No hidden withdrawn-roster, period-packet, or CR7 dependence: supported for the displayed candidate's reasoning as reconstructed here.** The target mentions those materials only to disavow them; none is needed by §§2–7. This is not a review of any unprovided body. In particular I do not import any `q|R=0` premise, f161/f162, a held result, author PASS, author computation, solver output or sibling review.
9. **Author execution/history assertions and status of other research branches: INCONCLUSIVE.** The target's statements about its author's non-execution, storage/history and all other branches' present status are not established by the two frozen inputs. The non-claim about a global witness/exclusion is preserved; no other branch is adjudicated.

## 1. Actual sequence and deviations

A higher-priority runtime instruction caused the general memory summary to be read before the manifest; it was not a scientific input. The **manifest was the first wave packet opened**. I then measured, before opening either declared input body:

| Item in measured/read order | SHA-256 | bytes | LF |
|---|---|---:|---:|
| `review-waves/f244-nl242-rank2-eightzero-116-fibre-obstruction/manifest-v1.json` | `5a4e50099914d5c175dcb8405fdffc1dcd3d47c8523dcd63558c517813c7c3ad` | 2851 | 30 |
| `dispositions/info-6-six-walsh-zeros-excluded-conditional-parent-v1.md` | `c1a85da652e8308e20c9129ebf1d031b1d97e343edfdb6f9620d38e18525a03e` | 4566 | 21 |
| `information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/successor-20261029-rank2-eightzero-116-fibre-obstruction-v1.md` | `29a608826ee2c3dd80a3d47875ae10f720de4291375cc57473d36e8523c3b394` | 13731 | 174 |

The manifest hash has the assigned prefix `5a4e50099914`; both input measurements match all declared values. The two applicable general skill instructions were read after these measurements and before either mathematical input body; they supplied no mathematical premise. Next the scope input was displayed in raw windows `1–15, 16–21`; then the target in raw windows `1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–174`. Thus the final line of each was displayed and no mathematical reasoning occurred before both bodies were complete.

Native `/bin/date` observations were `2026-10-29T14:43:19-0700 PDT` before the first reviewer artifact write, and `2026-10-29T14:45:27-0700 PDT` before writing this review; these are observations before writes, not asserted file-creation times. The first reviewer-control attempt failed on the system Python version; its exact receipt and correction are disclosed in §8. Apart from the general-memory-before-manifest ordering and that failed reviewer-owned run, there were no deviations. Only the wave directory was written. No linked mathematical body, author script or result, external search/model/API, Git, publication or infrastructure mutation was used.

## 2. Independent original-object setup

Let `A={x:f(x)=1}` and `F(x)=(-1)^f(x)`. Balance gives `|A|=256`. For a frequency `a`, let `N(a)=#{x in A:a·x=1}`. For nonzero `a`, `W(a)=4(N(a)-128)`; at `a=0`, both `W(0)` and `N(0)` are zero. Thus for **all** `a`, `k(a)=W(a)/4` is integral and `k(a) ≡ N(a) (mod 4)`. If `T` is the XOR of `A`, then `k(a) mod 2 = a·T`. By the expressly scoped adopted statement, `T != 0`; consequently `K=T^perp` is eight-dimensional, `k` is even on K and odd off K, and all zeros are in K.

For `a,b in K`, define `q(a)=k(a)/2 mod 2` and `M(a,b)=sum_{x in A}(a·x)(b·x) mod 2`. The integer identity `N(a+b)=N(a)+N(b)-2#{x in A:(a·x)=(b·x)=1}` shows `q(a+b)=q(a)+q(b)+M(a,b)`. Its polar B is bilinear and alternating on K, because `M(a,a)=a·T=0`. This obtains the parity and coupling used in the proof directly, without importing the unprovided caller.

Choose a linear section of the 256 unordered pairs `{x,x+T}`. Define `u=(F(x)+F(x+T))/2` and, after a harmless character twist chosen using any fixed `t` with `t·T=1`, `v=(F(x)-F(x+T))/2`. Both take values in `{−1,0,1}`, exactly one is nonzero on each pair, and `|supp u|=m`. The eight-dimensional transforms satisfy `Walsh(u)=2k` on K and `Walsh(v)=2k` on the odd coset. Parseval therefore gives

`sum_{a in K} k(a)^2=64m`, and `sum_{a notin K} k(a)^2=64(256-m)`.                         (A)

For completeness the target's claimed odd-coset bound also follows independently. Put `Q(a)=(N(t+a)-1)/2 mod 2` for `a in K` and `gamma(a)=(-1)^Q(a)`. The preceding identity shows the polar of Q is the same B, and `k(t+a) ≡ gamma(a) (mod 4)`. For the eight possible odd values in `[−7,7]`, put `d=1` if `|k|` is 1 or 3 and zero otherwise. Directly, **pointwise**,

`k^2 = 35 - 2k gamma - 32d`.                                                   (B)

Equivalently, if `x=k gamma`, choose `h'=1` for `x in {−3,5}` and 0 otherwise; take `delta=gamma` for `x=−3`, `delta=−gamma` for `x=1`, and 0 otherwise. This verifies the candidate's `k=gamma(12h'−7)−8delta`. Let `D=sum d=n1+n3`. Since Q has polar rank two, its eight-dimensional sign transform has exactly four nonzero values, all of magnitude 128: the autocorrelation is zero outside the six-dimensional radical and is a character times 256 on it. Combining (A), (B), and the inverse transform gives `sum_odd k gamma=64S`, where S is a signed sum of four values of v, each in `{−1,0,1}`. Therefore

`m=116+D/2+2S >= 108+D/2`.

Now let `R=rad(B)`, of dimension six. A quadratic with rank-two polar has `z=#{a in K:q(a)=0}` equal to 128 if its restriction to R is nonzero, or 64 or 192 if that restriction is zero (the quotient is a nondegenerate two-dimensional quadratic). On `q=0`, peak at most 7 and even parity allow only `0,±4`; on `q=1` only `±2,±6`. Since exactly eight k-values vanish, (A) yields

`64m <= 16(z−8)+36(256−z)`.

At `m=116` this bounds `m<=102` for `z=128`, and `m<=82` for `z=192`; both contradict 116. Thus `z=64`, and necessarily `q|R=0` with anisotropic two-dimensional quotient. Write `K=R⊕F2^2`, so q vanishes on the R fibre and equals 1 on each of the other three. The first fibre contains eight zeros and 56 values `±4`. If `e_s` is the number of `±2` entries on nonzero fibre s, then (A) gives

`64*116 = 16*56 + 4 sum_s e_s + 36(192-sum_s e_s)`, hence `sum_s e_s=12`.

The ordered pattern `(0,4,8)` is an additional assumption, not a classification of all patterns.

## 3. Four-point blocks and the e1=0 reduction

Using coordinates dual to `K=R⊕F2²`, write u as 64 four-entry blocks. For `s in F2²`, let `U_s(c)=sum_z u(c,z)(-1)^(s·z)`. The fibrewise Parseval identity gives

`sum_c U_0(c)^2=56`, and `sum_c U_s(c)^2=144-2e_s` for `s!=0`.             (C)

Direct enumeration or a four-point Walsh transform of weights 0 through 4 gives exactly the following local absolute-value types, with `j` nonzero: `A_j=(weight 3; |U0|=1, |Uj|=3, the others 1)`, `B=(3;3,1,1,1)`, `C_j=(2; |U0|=|Uj|=2, the others 0)`, `D_j=(2; |U0|=|Uj|=0, the others 2)`, `E=(4;2,2,2,2)`, `F=(1;1,1,1,1)`, `G_j=(4; |Uj|=4, the others 0)`, `H=(4; |U0|=4, the others 0)`, and `O=(0; all zero)`. The reviewer enumeration covers all 81 signed ternary blocks; it is not a Boolean-function existence search.

For nonzero s let `v_s(r)=k(r,s)/2`, `sigma_s=sign(v_s)`, `tau_s=sigma_s 1_{|v_s|=1}`, and `t_s=Walsh_6(tau_s)`. Then `v_s=3sigma_s−2tau_s`, and the partial inverse transform gives `16U_s=3Walsh_6(sigma_s)−2t_s`; therefore `U_s ≡ t_s (mod 3)`. At `e1=0`, `t1=0`. Since `|U1|<=4`, each U1 is 0 or `±3`; (C) gives exactly 16 entries of absolute value 3. These are precisely 16 `A1` blocks. The remaining possible types are exactly `C2,C3,D1,G2,G3,H,O`.

## 4. Four signed atoms and complete count equations

The four distinct atoms of `tau2` have affine rank 2 or 3. In rank 2 they form an affine plane: sign product −1 gives `(N0,N2,N4)=(0,64,0)` and sign product +1 gives `(48,0,16)`. In rank 3 the three character ratios are independent; counting their eight patterns gives `(24,32,8)`. On the reduced class list `|U2|` can only be `0,1,2,4`, while the four-atom transform only takes even values of magnitude at most 4. Hence `U2=0` iff `t2=0`, by the mod-3 congruence.

Put `x=c2+d1`, `y=g2`. From (C), `16+4x+16y=136`, hence `x+4y=30`; the number of U2 zeros is `48-x-y`. The first two four-atom histograms cannot satisfy these equations with nonnegative x,y. The third forces `x+y=24`, so `y=2`, `x=22`. For rank 3, absorb the signs into the three independent character ratios. The zero patterns of `1+chi1+chi2+chi3` are those with exactly two negative ratios. Together with the all-positive pattern they form an affine five-flat `H2`, and the all-positive pattern is an affine three-flat `F2` inside it. Thus the U2-zero set is exactly `H2 \ F2`.

Let `g=g3`, `h=H`, and use lowercase for all counts. From the U0 energy, U2 energy, 64 blocks and total block weight 116,

`g2=2`, `c3=8−2g−2h`, `c2=2+2g−2h`, `d1=20−2g+2h`, `o=16+g+h`.

All counts are nonnegative exactly when `g,h>=0`, `g+h<=4`, `h<=g+1`; the U3 energy equation is then satisfied. The U3-zero classes are `C2,G2,H,O`, so their number is

`c2+g2+h+o=20+3g`.                                                        (D)

No reduced class has `|U3|=3`; hence the mod-3 congruence shows this is exactly the number of positions where the eight-atom `t3` is divisible by 3.

## 5. Eight signed atoms: why g3 cannot be 3

Translate one of the eight distinct atom positions to zero and let their affine rank be r. The divisible-by-3 predicate depends only on r independent character ratios and is constant on fibres of size `2^(6-r)`. If `g=3`, (D) demands 29 such positions, so r=6. In that case the eight augmented columns `(1,a_i)` have rank 7 and one nonzero binary relation. Its weight is even, because of the leading 1; distinct atoms rule out weight 2. Thus its weight `w` is 4, 6 or 8. The product of the atom signs on that relation fixes an even or odd syndrome.

The 64 character patterns correspond to the 128 sign patterns of the fixed syndrome modulo simultaneous sign reversal: the predicate is invariant under reversal, and rank six makes the ratio map injective. A sum of eight signs is divisible by 3 exactly at minus-sign weights `k=1,4,7`. For each relation weight, the two counts are one half of

`sum_{k in {1,4,7}} sum_{j ≡ syndrome (mod 2)} C(w,j) C(8−w,k−j)`.

Explicitly, with even and odd syndromes respectively, `w=4: (23,20)`, `w=6: (17,26)`, `w=8: (35,8)`. For instance at w=4 the even contributions at weights 1,4,7 are `4,38,4`, summing to 46 and giving 23 after division by 2. None is 29. Therefore **g3=3 is impossible**. The reviewer control independently enumerated the signs and character evaluations for an explicit rank-six support of each relation weight; it also checked that 29 is absent.

## 6. At g3=1: 23-point set, hyperplanes, and flats

If `g=1`, (D) gives 23, again odd, so the rank is six. The preceding table permits 23 only for a weight-four relation with even syndrome. Those four atom positions form an affine plane, and even syndrome means their sign product is +1. Choosing a basis consisting of two plane differences and the four independent outside differences, then translating character signs and multiplying by an irrelevant overall character, gives the same zero-mod-3 set as

`t3(u,v)=4*1_{u=0}+sum_{j=1}^4 (-1)^{v_j}`, `u in F2²`, `v in F2⁴`.

Indeed the four plane characters sum to 4 at one u and vanish at the other three. Thus its divisible-by-3 set is

`B0={(u,v):u!=0, |v|=2} union {(0,v):|v|=1 or 4}`,

with `18+5=23` points. The U2- and U3-zero classes intersect exactly in H and O, so with §4,

`|B0 intersect (H2\F2)|=h+o=17+2h`.                                  (E)

For a character `(alpha,beta)`, `w=|beta|`, the Fourier coefficient of `1_B0` equals

`(3 if alpha=0 else −1) K2(w) + K1(w)+K4(w)`,

where `K2=(6,0,−2,0,6)` and `K1+K4=(5,1,1,−3,−3)` for `w=0,…,4`. At `alpha=0` the five values are `(23,1,−5,−3,15)`; at `alpha!=0` they are `(−1,1,3,−3,−9)`. Hence every nontrivial coefficient has absolute value at most 15, with equality only at `(alpha,beta)=(0,1111)` and coefficient +15. A hyperplane contains at most `(23+15)/2=19` points; equality occurs only for `H*={v:|v| even}`. Equation (E) excludes `h>=2`. If `h=1`, its value is 19, forcing `H2=H*` and `F2` disjoint from B0.

It remains to rule out that three-flat. Write `V_even={v:|v| even}`, a three-space, and `L={0,1111}`. Inside H*,

`B0 = ((F2²\{0}) x (V_even\L)) union {(0,1111)}`.

For any affine three-flat F, project to the u coordinates. Projection dimension 0: if u=0, its full V_even fibre contains 1111; otherwise the fibre contains a point outside L. Dimension 1: a nonzero-u fibre has four points, too many to fit in L. Dimension 2: all four fibres are parallel affine lines; avoiding B0 forces each of the three nonzero-u fibres to be exactly L. Their common direction is therefore L, and the fibre offsets form an affine map `F2² -> V_even/L`. An affine map zero at all three nonzero inputs is also zero at 0, so the zero-u fibre is L and contains 1111. Every case intersects B0, a contradiction. Thus **g3=1 implies H=0**.

## 7. Literal residual and what remains open

Before §§5–6, nonnegativity allows precisely `(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(4,0)`. Removing `g=3` and `g=1,h>0` leaves the following seven and only these seven class-count pairs:

| `(g,h)` | `c2` | `c3` | `d1` | `g2` | `o` |
|---|---:|---:|---:|---:|---:|
| `(0,0)` | 2 | 8 | 20 | 2 | 16 |
| `(0,1)` | 0 | 6 | 22 | 2 | 17 |
| `(1,0)` | 4 | 6 | 18 | 2 | 17 |
| `(2,0)` | 6 | 4 | 16 | 2 | 18 |
| `(2,1)` | 4 | 2 | 18 | 2 | 19 |
| `(2,2)` | 2 | 0 | 20 | 2 | 20 |
| `(4,0)` | 10 | 0 | 12 | 2 | 20 |

Every row additionally has `A1=16`; `g` and `h` are the G3 and H counts. For example `(1,0)` gives exactly `A1=16,C2=4,C3=6,D1=18,G2=2,G3=1,H=0,O=17`; these total 64 blocks, have weight 116, and squared U sums `(56,144,136,128)`. This is a **nonempty integer class-count relaxation only**. It does not provide compatible signed atom placements, a shared full Walsh spectrum, all remaining nonzero-shift caller constraints, or a Boolean f. Enforcing those constraints or constructing an actual target is the remaining gap. **The full `(0,4,8)` fibre case remains OPEN**, and neither the seven rows nor this review establish any target's existence.

## 8. Reviewer-owned exact controls and limitations

The only control artifact is `reviewer-exact-controls-v1.py` in this wave directory, written independently using Python standard-library integer arithmetic and without importing author code. Each run had a 120-second tool deadline; a timeout would have meant UNKNOWN, never exclusion.

- First attempt: `/bin/date` before `2026-10-29T14:44:11-0700 PDT`, script SHA-256 `bfba9003854e2387b07cff1819b3b34169f0dc64bbf7f6348808d842bf655c46`, `/usr/bin/python3 -B`, **exit 1**, `/bin/date` after `2026-10-29T14:44:16-0700 PDT`. The system Python 3.9 lacks `int.bit_count`; the run stopped before a control completed and provides no mathematical evidence. I changed the reviewer script's popcount to `bin(x).count('1')`; this failed intermediate script is not the final artifact.
- Corrected run: `/bin/date` before `2026-10-29T14:44:32-0700 PDT`, final script SHA-256 `49167ba37f6e9dcc069d48d562a564a6f20dba1e37a648d9c09ef81eb764ae88`, `/usr/bin/python3 -B`, **exit 0**, `/bin/date` after `2026-10-29T14:44:36-0700 PDT`. It completed all of the following, within the deadline: all 81 ternary blocks; all 16 sign choices on each of two representative four-atom supports including all 16 associated flat identities; six eight-atom relation/syndrome cases checked both by binomial sums and all 256 signed transforms on representative supports; all 63 nonzero Fourier coefficients and 126 hyperplanes of B0; all 155 linear three-subspaces and 620 affine three-flats of H*; all 256 rank-two quadratic phases in a fixed symplectic coordinate system; and the 11 raw versus seven surviving integer count pairs. The 620 flat intersection histogram was `{1:2,2:18,3:57,4:228,5:90,6:210,7:6,8:9}`.
- Intended-reason negatives: the zero block is not H; a damaged 31-point set is not a five-flat; 29 does not occur in the six eight-atom relation counts; an explicit **two**-flat disjoint from B0 exists, so the three-flat claim is not mistakenly applied to dimension two; the z=64 energy cap does not exclude `m=116`; the pairs `(3,0)` and `(1,1)` exist in the arithmetic relaxation but are removed only by the respective obstructions; and changing the pointwise D coefficient from 32 to 16 is detected. These checks complement the written arguments; they are not an exhaustive search over Boolean functions or proof of realizability.

This is **same-harness scientific review**, not human, independent-model-family, formal/kernel, or novelty verification. Its final SHA-256 is supplied in the reviewer's reply, not embedded here.
