# Actual odd complement: coupled 256-coefficient criterion and intersection obstructions

**Status: prospective GENERAL AUTHOR candidate; parent disposition and independent review are separate.** The main results below are an exact, constructive if-and-only-if for the odd half of **each fixed actual ternary even half**, and additional simultaneous support-intersection, autocorrelation and four-fibre restrictions. They apply to both named six-span branches. They do not give an actual capped complement, exclude either branch, settle even-half feasibility, or prove a global NL242 result. No scientific code was prepared or executed.

## 1. Exact scope, physical object, and imports

Work over F₂. Fix a selected nonzero original vector `T` in F₂⁹ and an original linear functional `a0` with `a0·T=1`; put `V=a0⊥`, identified with F₂⁸. Every original point is uniquely `y` or `y+T` with `y∈V`. Let an **actual** even pairfunction

`u: V → {−1,0,1}`,  `|supp(u)|=116`,  `Σ_y u(y)=0`

be given, and put `C={y:u(y)=0}`, so `|C|=140`. In the named caller it additionally obeys all actual even-half Walsh, rank/quadratic, eight-zero, fibre, `G3=1`, local `H=0`, atom and cross-fibre requirements. In particular local `H=0` means **no `U1=0` block has a single `|U0|=4` peak**, not a different historical class convention. The f244 source/atom and original-class correspondences not displayed in the packet remain named conditional imports, as do the linked canonical, rank-four and rank-two five-span no-go bodies. No link in the packet was opened. No historical source-label identity is asserted.

Use the same decomposition `V=F₂⁶×F₂²`, writing `y=(c,w)`, for the four partial transforms `U_s(c)=Σ_w u(c,w)(−1)^(s·w)`, with `a=U1/3` and `g=U2`. The two branches are the **same physical u** alternatives from S2–S3: after their common normalization, `S=supp(a)` has the `(E; four B cosets)` counts `(4;0,4,4,4)` with the two full `g` blocks together, or `(4;2,2,4,4)` with the two full blocks split, respectively, with the B entries permutable. Both have affine span six and the actual shared-shell/phase restrictions of S2; neither a shell nor a set of projected spectra is assumed to be a full u. Any use of S1 to assert these are the *only* surviving branches is conditional on its named, undisplayed five-span imports.

The explicit local-count interface from S2 and S4 gives, for this same u, **16** four-point blocks containing three nonzero u entries, **28** containing two, **3** containing four, and **17** containing zero. Thus the actual `C` has, respectively, 16 singleton, 28 pair, 3 empty and 17 full four-point fibres. Indeed the 16 are the `U1=±3` blocks; the 28 comprise the 4 `D0`, 18 `D3` and 6 `Z2` two-entry blocks; the three fully occupied u blocks are the two `|U2|=4` blocks and the single `|U3|=4` block; and the 17 are zero-u blocks. This count is not an independent formal choice of C.

All Fourier transforms below are **unnormalized**: for `p:V→R`, `p̂(ξ)=Σ_y p(y)(−1)^(ξ·y)`. The pairing is the original `V*×V` pairing, and all 256 frequency and spatial points are included.

## 2. Selected original T, parity and the specified balance

For a physical `v:V→{−1,0,1}` with `v²=1_C`, reconstruct the original sign function by

`s(y)=u(y)+v(y)`,  `s(y+T)=u(y)−v(y)`.

These values are exactly ±1 because the supports are complementary. Its Boolean support is `{x:s(x)=−1}` and its balance is exactly `Σu=0`. Because support size is 116 and `Σu=0`, there are precisely 58 negative u-pairs. The XOR of the reconstructed Boolean support is

`P_C + (58 + #{y∈C:v(y)=+1} mod 2) T`,  where `P_C=⊕_{y∈C} y ∈ V`.

The 140 split pairs contribute their y's; a positive v puts the negative original point at `y+T`. As `V∩<T>={0}` and 140 is even, this XOR is the **selected original T if and only if**

`P_C=0` and `#{y∈C:v(y)=−1}` is odd.                                      (2.1)

This is a two-part physical condition, not an inference from an arbitrarily selected normalized zero. If the chosen common normalization is `u_N(z)=ε(−1)^(β·z)u_O(Az+b)`, with ε=±1 and A invertible, the **specific** transported original balance is `û_N(β)=ε û_O(0)=0`. When β has zero two-bit fibre component, this reads `Û0_N(t)=0` at the specific `t` supplied by that transformation, not at some subsequently chosen zero. A normalized u is not an original balanced caller unless this exact condition is transported back. The support XOR satisfies `P_{C_O}=A P_{C_N}` because `|C|` is even. For the corresponding character modulation of v, the sign product changes by `(−1)^(β·P_{C_N})`, hence its odd parity is invariant once `P_C=0`. The same statement covers changing the linear original section by a character; coordinates and the original T must be carried throughout.

For every such physical v and every ξ, expansion modulo four gives the useful identity

`v̂(ξ) ≡ 140 − 2( N_− + ξ·P_C ) (mod 4)`,                                  (2.2)

where `N_−=#{y∈C:v(y)=−1}`. Consequently (2.1) is equivalent to **all 256** values `v̂(ξ)/2` being odd: the ξ=0 value forces odd `N_−`, and all remaining ξ force `P_C=0`. This implication requires the actual inverse, not a formal list of amplitudes.

## 3. Exact constructive iff, with all 256 coefficients coupled

**Theorem.** Fix any actual `u` as above, including the exact original balance, and fix its actual set `C`. There is a physical complement v whose reconstructed Boolean function is balanced, has the selected XOR T, and has all 256 odd-half original Walsh magnitudes at most 28 **if and only if** there are 256 integers `k(ξ)`, indexed by the whole `V*`, such that

1. `k(ξ) ∈ {−7,−5,−3,−1,1,3,5,7}` for every ξ; and
2. for **every** `λ∈V*`,

   `Σ_{ξ∈V*} k(ξ) k(ξ+λ) = 64 · Ĉ(λ)`,                              (3.1)

   where `Ĉ(λ)=Σ_{y∈C}(−1)^(λ·y)` is computed from the *same fixed physical complement*.

These are 256 coupled integer quadratic equalities, not 256 independent amplitude choices. At `λ=0`, (3.1) is `Σ k²=8960`; all 255 nonzero shifts are also mandatory. A solution constructs the actual physical complement explicitly by

`v(y)=(1/128) Σ_{ξ∈V*} k(ξ)(−1)^(ξ·y)`.                               (3.2)

Conversely every admissible v gives the unique `k=v̂/2`. Thus an exhaustive finite search through the displayed eight-valued integer system, followed by (3.2), is a completely specified decision/construction procedure **in principle**; none was run and no existence result is claimed.

*Proof.* If v exists, the original odd Walsh values are `2v̂=4k`. The bound gives the eight permitted odd k values by (2.2). Orthogonality gives

`Σ_ξ v̂(ξ)v̂(ξ+λ)=256 · (v²)̂(λ)=256 Ĉ(λ)`,

which is (3.1) after division by four. Conversely take any k satisfying the two conditions and define v by (3.2). Fourier inversion gives `v̂=2k`, and the same identity in reverse gives `(v²)̂=Ĉ` for every λ. Fourier inversion on V yields **pointwise** `v²=1_C`; since v is real, it is exactly zero off C and ±1 on C. Odd k and (2.2) now force both parts of (2.1), so the reconstruction has selected XOR T; its balance is the specified `Σu=0` and its odd Walsh cap is `|4k|≤28`. The even-half original Walsh values are `2û`; their cap and all named even-side conditions must already be present in the chosen u. This proves both directions without assuming independent signs, a spectral tally, or an already existing Boolean caller. ∎

For either branch `b∈{together,split}`, the resulting full **conditional** frontier is: quantify over actual ternary u satisfying that branch's shared-shell conditions, all named even-half constraints and the specified transported balance, and require one k solving (3.1). Given such a pair, the displayed formulas build the original function; every original function in the stated scope produces such a pair. If an exact f244 atom/class correspondence or other load-bearing condition is not available in the packet, it remains an additional named condition on u, not an assertion supplied by (3.1). In particular, solving (3.1) for one fabricated or merely projected C would not establish a named caller.

## 4. A computable selected-XOR obstruction from the actual four-point fibres

Let `S={c:|C_c|=1}={c:a(c)≠0}`. For `c∈S` write the unique point of `C_c` as `γ_c∈F₂²`; for each two-point fibre define its nonzero direction `δ_c=w+w'`. The full and empty fibres contribute zero XOR, so

`P_C = ( ⊕_{c∈S} c ,  ⊕_{c∈S} γ_c + ⊕_{|C_c|=2} δ_c )`.              (4.1)

The first coordinate is automatically zero for any actual a with `a∈{0,±1}`, `|S|=16`, and `|â(r)|=4` for all r: `â(0)−â(r)` is 0 or ±8, hence `Σ_{c∈S:r·c=1} a(c)` is divisible by four and its number of summands is even. Therefore `r·⊕S=0` for every r. The second coordinate in (4.1), however, must separately vanish for the selected T. It depends on the **actual missing point in every three-entry u block and the actual directions of all 28 two-entry blocks**.

Write the three nonzero elements of F₂² as `h1,h2,h3=h1+h2`, and let `n_i` be the number of pair fibres of direction `h_i`. Then `Σ n_i=28`, so either all three n_i are even or exactly two are odd. In the first case selected XOR requires `⊕_{c∈S} γ_c=0`; in the second, if `n_i,n_j` are odd, it requires `⊕_{c∈S} γ_c=h_i+h_j`, the remaining nonzero direction. Failure rules out **every** choice of v signs for that fixed physical u. This is not a substitute for the remaining all-frequency constraints.

## 5. Global energy, support intersections, and the saturation frontier

For a solution k of (3.1), let `N2,N6,N10,N14` count `|v̂|=2,6,10,14`, equivalently `|k|=1,3,5,7`. Parseval and the total 256 coefficients give

`N2+N6+N10+N14=256`,  `N2+9N6+25N10+49N14=8960`,
`3(N14−N2)−2N6=320`,  `N6≡2 (mod 3)`,  `N14≥108`.               (5.1)

Equality gives precisely `(N2,N6,N10,N14)=(0,2,146,108)`. This tally alone does not satisfy (3.1) or produce v.

Define the *actual* support overlap and signed derivative, for `h∈V`, by

`r(h)=|C∩(C+h)|`,  `D(h)=Σ_y v(y)v(y+h)`.

For `h≠0`, the involution on the intersection gives even `r(h)`, `24≤r(h)≤140`, and

`D(h)=r(h)−4m(h)`,  `0≤m(h)≤r(h)/2`,                                (5.2)

where `m(h)` is the number of unordered overlapping pairs carrying opposite v signs. These equations couple signs to the same physical C.

Set `d(ξ)=(49−k(ξ)²)/8 ∈ {0,3,5,6}`. Then `Σ d=448`. For each nonzero h put `M(h)=Σ_{ξ:ξ·h=1} d(ξ)`. Fourier inversion of `v̂²` gives the simultaneous identities and restrictions

`D(h)=−(1/8)Σ_ξ d(ξ)(−1)^(ξ·h)=M(h)/4−56`,                          (5.3)
`M(h)≡4r(h) (mod 16)`,
`max(0,224−4r(h)) ≤ M(h) ≤ min(448,224+4r(h))`.                      (5.4)

Thus **one and the same placement** of the 256 deficiencies must meet (5.4) for all 255 nonzero h and for the actual overlap function of u. In particular `|D(h)|≤min(r(h),56)`; if `r(h)≡2 (mod 4)` and `r(h)≥56`, the congruence sharpens this to `|D(h)|≤54`. A multiset obeying only (5.1) need not admit any such placement.

The complete nonzero derivative energy is fixed by the saturation counts:

`Σ_{h≠0} D(h)² = (1/16)Σ_ξ k(ξ)^4 − 140²`
`                         = 2240 + 40N6 + 72N2 ≥ 2320`.               (5.5)

Equality holds **if and only if** the unique formal saturation tally in (5.1) holds. Equations (5.2)–(5.5) are a global intersection/energy constraint beyond `N14≥108`: each derivative must simultaneously be an integer of the permitted parity and size for this particular C, while their squared sum and all deficiency transforms are fixed. No claim is made that these necessary constraints alone are sufficient.

For the three nonzero *within-block* shifts `(0,h_i)`, the actual 17 full C fibres and the pair directions give

`r(0,h_i)=68+2n_i`,  `m(0,h_i)≥3+ceil(n_i/2)`,
`r(0,h_i)/2−m(0,h_i)≥3+ceil(n_i/2)`.                                (5.6)

The latter two inequalities follow from (5.2) and `|D|≤56`: at least that many unordered overlapping pairs must disagree and at least that many must agree in **each** direction. Summing over the three distinct within-block directions, at least `23 + (# of odd n_i)/2` such pairs must disagree, and at least that many must agree. Thus the lower bound is 23 when all n_i are even and 24 when two are odd. This uses all 17 full and all 28 pair fibres of the same u, not a spectral surrogate.

## 6. Simultaneous four-fibre saturation congruences

Write `k(r,s)` on the same `F₂⁶×F₂²` dual decomposition. For each of its four s-fibres let `A_s,B_s,C_s,D_s` count the 64 values of magnitudes `1,3,5,7`, respectively. Set

`V_s(c)=Σ_w v(c,w)(−1)^(s·w)`.

Let `b_s` count the pair/full physical C fibres for which `|V_s(c)|=2`, and `p_s` count full fibres for which `|V_s(c)|=4`. Every singleton contributes `V_s²=1`, each pair contributes 0 or 4, and every full fibre contributes 0, 4, or 16. Six-dimensional Parseval therefore gives the exact equality

`A_s+9B_s+25C_s+49D_s = 16Σ_c V_s(c)²`
`                                  = 256+64b_s+256p_s`,
`B_s+3C_s+6D_s = 24+8b_s+32p_s`,                                    (6.1)
`B_s+3C_s+6D_s ≡ 0 (mod 8)` for **each** of the four s.             (6.2)

These are four simultaneous restrictions on the *same* 256 coefficients and the same actual v. Moreover, if `o` is the number of the 17 full C fibres having an odd number of negative v signs, their four-point Fourier transforms are respectively four values of magnitude 2 for each odd full fibre, and one value of magnitude 4 for each even full fibre. Each pair fibre has two magnitude-2 transforms. Consequently

`Σ_s b_s=56+4o`,  `Σ_s p_s=17−o`,  `0≤o≤17`.                       (6.3)

In the boundary case `N14=108`, `N2=0` and `N6=2`; using `B_s+C_s+D_s=64` in (6.2) yields the further four simultaneous congruences

`C_s ≡ B_s (mod 8)` for every s.                                       (6.4)

Even this strengthened boundary description is not a witness: it still must meet (3.1), the actual support and signs, (2.1), and every even-half original-caller condition. The labels s and the given c/w decomposition must be transported as one common physical coordinate system.

## 7. Boundaries, derivations, and read/process declaration

The energy identity (5.5) follows from `Σ_h D(h)²=(1/256)Σ_ξ v̂(ξ)^4=(1/16)Σ_ξ k(ξ)^4`, `D(0)=140`, and (5.1). Formula (5.3) follows from `Σ_ξ k(ξ)²(−1)^(ξ·h)=64D(h)` and the vanishing character sum for `h≠0`. For (6.1), `Σ_r k(r,s)²=16Σ_c V_s(c)²`; no product, peak location or sign is selected independently. The finite restrictions have no unhandled `h=0` case: (3.1) includes λ=0, while (5.2)–(5.6) explicitly concern nonzero h. The two named six-span branches and every actual u within each are covered; a complement with `P_C≠0`, an even number of negative signs, an unbalanced original u, a single failed odd cap, or a failed nonzero-shift equation is excluded by the corresponding stated necessity.

**Remaining gap.** No u in either branch has been constructed here with the complete four-fibre/original-balance interface; no 256-entry k solving (3.1) has been exhibited or ruled out for such a u. The absent f244 atom/source and linked no-go bodies remain the named conditional imports above. A formal tally or independently placed spectra is not an actual u/v witness. This candidate asserts neither exclusion of a complete branch nor any global NL242 theorem, source identity, publication priority, human/independent-family/formal acceptance, or parent disposition.

**Read/process declaration.** Before any packet-body access or target mathematics I read the complete manifest, freeze receipt, final binding, live metadata supply, actual dispatch receipt, and all 23 manifest-listed status-only controls; I wrote `prebody-ack-v1.md` and directly delivered the prebody ACK to Main. Controls were not mathematical inputs. I then read the sole literal packet in order as raw windows LF 1–10, 11–20, …, 291–300, 301–307, including all five source endings S1 1–27, S2 1–46, S3 1–37, S4 1–162, S5 1–13. Each display had at most 10 lines and was below 30000 bytes; no clipping occurred and no recovery was needed. Parent-supplied packet SHA-256 is `4e77cd601badd5989e0860ff2b4a21af21aca1d789c53b40f7b9e5dd1d47d2a3`; these administrative metadata are not an independent hash or provenance certification. No linked/unlisted mathematical body, held episode or its consumers was opened or used. There was no network, scientific execution, test, compilation, child subprocess, code, source-following, Git, deletion or external-model call. No prepared code hash exists. No process deviation is known in this assignment.
