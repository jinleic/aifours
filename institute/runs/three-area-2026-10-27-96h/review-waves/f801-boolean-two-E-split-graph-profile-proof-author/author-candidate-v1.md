# F801 — same-X profile identity for two E D0 and split graph D0

**Status: fresh, nonblind, same-harness GENERAL AUTHOR written reconstruction; not independently checked or parent-adopted.** Subject to the exact imports below, the simultaneous-profile identity in S1 §3 follows for every `d_E=2`, graph-`1+1` object, for both physically possible E occupancies `2` and `1+1`. This is a necessary identity on one actual X, not a realization theorem or a complete common-Y obstruction. In particular it does not itself settle the later U3 argument of S1.

## 1. Quantifiers, physical coordinates and imported interface

Fix **one** object at the packet's named actual normalized rank-two, five-span, `H_loc=0`/count interface. Its physical inverse and the given original-DC transported character `t` determine `x` and the analysis array `X(c)=(-1)^t(c)x(c)`; `t` is not reset or varied. Coordinates are `(ell,h,i,v)` with `ell,h∈F₂` and row label `i` and within-row coordinate `v` in `F₂²`. At `ell=1`, graph row `i` is `h=F_i`, its *actual same-v mate* is `h=1+F_i`, and `Σ_i F_i=1`. Four graph X values in each row have magnitude 1. The graph D0 mate X values have magnitude 2; other graph mates have X=0. Precisely two D0 mates occur, in distinct rows `a,a'`; the other graph rows are `c,c'`. Write `Δ=a+a'=c+c'≠0`. The equalities hold because all four row labels are the points of `F₂²`. The D0 mates occur at actual coordinates `z_a,z_a'∈F₂²`, with X values `2ε_a,2ε_a'` for `ε_i∈{±1}`.

At `ell=0` there are two E D0 at `v=0` in non-full rows `i≠0`, and six Z2 sites at `v≠0`, each with `|X|=2`; all remaining ell-zero X values, including the two full sites, vanish. For E occupancy `2`, the two sites are in one non-full row, necessarily one at each h. For `1+1`, they are in two distinct non-full rows, with either actual h choice. No assumption about which E rows, h values, or signs occurs in the proof.

Import the **same-X** eight zero-flat equations and seven nonzero quotient profiles:

`Z_(ell,i)(s,α) = (1/4) Σ_(h,v) X(ell,h,i,v)(-1)^[s h+α(v)]`,  `Z_(ell,i)(0,0)=0` for all `(ell,i)`.

For each `(s,α)≠(0,0)` the eight `Z` entries form either one `±2` singleton or four `±1` on one affine two-flat of `F₂×F₂²`, with product of the four signs `−1`. All seven columns are transforms of the same X and use the actual graph/mate positions above. These conditions and the local type/count bridge are imports from the named packet interface (in particular S6 and S10); no original-source, inverse, phase, residue, or caller derivation is claimed here. Neither independent spectra nor independently selected profile columns are inputs.

## 2. Graph rows and the actual occupied-row slice

Fix dual two-bit coordinates and write `q(v)=v₀v₁`; for a covector `ν=(ν₀,ν₁)` put `Jν=(ν₁,ν₀)` in the primal coordinate space. Then

`q(α+ν)=q(α)+q(ν)+α(Jν)`.

Let `P_i(v)=X(1,F_i,i,v)`. For `i=a,a'`, zero flat gives `Σ_v P_i(v)=-2ε_i`. Thus exactly one sign differs from the other three. Every sign table of this form has odd negative parity and unique algebraic normal form with quadratic coefficient one, so for unique `ν_i` and a sign `σ_i`,

`P_i(v)=σ_i(-1)^[q(v)+ν_i(v)]`.

For `i=c,c'`, zero flat gives `Σ_v P_i(v)=0`; every balanced four-point sign table is a signed nonconstant character, so `P_i(v)=κ_i(-1)^[θ_i(v)]`, where `κ_i=±1` and `θ_i∈(F₂²)*\{0}`. These statements apply to the given X, not a new choice of phases.

For any two-bit covector `γ`, summing first over `v₁` gives the exact identity

`Σ_v (-1)^[q(v)+γ(v)] = 2(-1)^q(γ)`.

Consequently `W_i(α):=Σ_v P_i(v)(-1)^α(v)=2σ_i(-1)^q(α+ν_i)` on an occupied row. Its zero-flat equation is `σ_i(-1)^q(ν_i)=-ε_i`, hence

`W_i(α)=-2ε_i(-1)^[q(α)+α(Jν_i)]`.                                            (2.1)

Including the **actual** `z_i` mate, rather than a formal missing point or a free sign, gives for either `s`

`Z_(1,i)(s,α) = (ε_i/2)(-1)^[s F_i] { -(-1)^[q(α)+α(Jν_i)] + (-1)^[s+α(z_i)] }`. (2.2)

Thus exactly one of the two s-slices is nonzero, it has magnitude one, and its label and value are

`s_i(α)=1+q(α)+α(z_i+Jν_i)`,                                                   (2.3)

`Z_(1,i)(s_i(α),α)=-ε_i(-1)^[s_i(α)F_i+q(α)+α(Jν_i)]`.                          (2.4)

All displayed exponents and slice labels are in `F₂`. This formula includes `α=0`: then `s_i=1` and the graph lambda value is `−(-1)^F_i ε_i`. On each unoccupied graph row the exact formula is

`Z_(1,j)(s,α)=κ_j(-1)^[sF_j] 1_[α=θ_j]`, `j=c,c'`.                            (2.5)

## 3. The actual mixed lambda plane, including both E shapes

The `(s,α)=(1,0)` column has exactly the two graph entries `−(-1)^F_a ε_a` and `−(-1)^F_a' ε_a'`, both magnitude 1. It cannot be a singleton. It is a four-entry plane containing exactly two ell-zero entries. If those E-side row labels are `p,p+Δ`, the signs obey

`Z_(0,p)(1,0) Z_(0,p+Δ)(1,0) = -ε_a ε_a' (-1)^[F_a+F_a']`.                 (3.1)

Indeed, the direction subspace of a two-flat meeting both ell-halves has a one-dimensional ell-zero kernel. Hence the two pairs have the same nonzero row difference; their four signs must have product `−1`.

For the E side, put `S_hi=Σ_v X(0,h,i,v)/2`. Zero flat yields `S_0i+S_1i=0`, and its lambda entry equals `S_0i`. At `i=p,p+Δ` each h-cell has an odd number of actual supports, while at both other rows each h-cell has an even number. There are eight supports total, independently of whether the two actual E sites have shape `2` or `1+1`; the other six are Z2 sites. Therefore the eight supports meet 4, 5 or 6 h-cells: respectively two active triples; an active triple plus an inactive pair or one inactive quadruple; or two inactive pairs. A quadruple must use a genuine non-full E site, so no full-site cell is a quadruple. These are necessary location restrictions, not a claim that each allocation or either E shape extends to a full object. In particular there is no E-side singleton in this *mixed lambda* case; the possible E singleton in other occupancy branches is not ruled out by this argument.

## 4. All six other columns and the same-X identity

An affine two-flat in the eight-point `(ell,i)` quotient meets the graph half in `0`, `2` or `4` points. A singleton cannot have a graph entry, since all graph entries here have magnitude at most 1 by (2.2)–(2.5). Therefore the number of graph entries in **each** of the six nonzero-α columns must be even. For each `α≠0`, put

`L(α)=1_[α=θ_c]+1_[α=θ_c'] ∈ {0,1,2}`.

The exact possibilities are:

| `L` | occupied slice relation | graph counts | necessary full-column geometry |
|---|---|---|---|
| 0 | `s_a=s_a'` | 2 on that slice, 0 on the other | 2-graph slice is a mixed plane with E pair difference `Δ` and sign product `−1`; zero-graph slice is an E singleton or E plane |
| 1 | `s_a≠s_a'` | 2 on each slice | each is a mixed plane; its E pair has the difference between its **actual** occupied and unoccupied graph rows, and the four-sign product is `−1` |
| 2 | `s_a=s_a'` | 4 on that slice, 2 on the other | four graph entries form the entire graph plane with sign product `−1`; the other is a mixed plane with E difference `Δ` and sign product `−1` |

The zero-graph slice remains a transform of the same actual E supports; neither its singleton nor its plane is asserted separately realizable. In any mixed plane, the two E signs multiply to the negative of the two displayed graph signs. As an extra explicit constraint when `L=2`, the graph-plane product condition is

`ε_a ε_a' κ_c κ_c' (-1)^[s+α(J(ν_a+ν_a'))] = -1`,                           (4.1)

where `s=s_a(α)=s_a'(α)` and `Σ_i F_i=1` was used. This sign condition is additional to, not a substitute for, the slice-parity identity below.

To derive that identity without assuming the table, on either s-slice the occupied-row support count is `1_[s=s_a]+1_[s=s_a']`, whose parity is `s_a+s_a'`. Adding the `L(α)` unoccupied rows and imposing even graph support yields

`s_a(α)+s_a'(α)=1_[α=θ_c]+1_[α=θ_c']  (mod 2)`                               (4.2)

for every nonzero `α`. It also holds for `α=0`: both occupied rows have slice 1 and both nonzero θ indicators vanish. Substituting (2.3) cancels the common `1+q(α)`, leaving

`α(z_a+z_a'+J(ν_a+ν_a')) = 1_[α=θ_c]+1_[α=θ_c']` for **all four** `α`.      (4.3)

If `θ_c=θ_c'`, the right side is identically zero; at their common nonzero θ the graph counts are `4,2`, and at each of the other two nonzero characters they are `2,0`. If `θ_c≠θ_c'`, the two covectors are independent. The right side is one precisely at them and zero at `0` and `θ_c+θ_c'`; it equals `α(J(θ_c+θ_c'))`, since the polar pairing `α(Jβ)` is nondegenerate and alternating on this two-bit space. In that case the two named θ columns have `L=1` and split slices, while `α=θ_c+θ_c'` has `L=0` and equal slices. The same formula also covers equal θ, where both sides of that polar expression vanish.

Nondegeneracy of the evaluation pairing now gives the announced vector identity in primal `v` coordinates:

**`z_a+z_a' + J(ν_a+ν_a') = J(θ_c+θ_c')`.**                              (4.4)

Equivalently, `z_a+z_a'=J(ν_a+ν_a'+θ_c+θ_c')`. Every term is read from the *same* actual X and its two actual D0 mates. No E sign, E location, graph Y spectrum, new transport, or parity of `ΣF_i` is needed for (4.4); the mixed-plane sign and the optional four-graph-plane condition remain additional necessary constraints. The proof is uniform in E occupancy `2` and `1+1`. The identity and these necessary conditions are not asserted sufficient for seven-profile realizability, a physical inverse, or a capped common Y.

## 5. Scope, open obligations, and coverage

S1 proposes a further same-Y parity argument and full `d_E=2,1+1` conditional no-go. This return independently reconstructs only the X-side identity and the specified necessary profile geometry. It does **not** certify S1 §§4–5, the graph phase/common-Y residue bridge, the paired U3 census, the Z4 contradiction, or an original caller. No counterexample to those claims is constructed. Graph occupancy `2`, other E counts, V, all-rank/tensor or NL242 statements, source identity, independent-family/human/kernel review, and novelty remain outside this proof. Parent review and separate disposition are required; no acceptance follows automatically. S2–S5's E-singleton gap/correction cautions are retained: no inference here eliminates their other-branch alternatives. S8 and S9 describe earlier parent finite runs at their stated limited scopes and are not execution or verification of this new argument.

**Actual read chronology.** After Main's direct actual-dispatch notice I read the complete dispatch. I read the complete manifest and prepared metadata in parallel, then the complete freeze receipt and final binding, then all 22 manifest controls through their endings as status/permissions only. I disclosed that metadata/control chronology to Main; Main confirmed their serial order was not required. Before any packet body I directly sent Main the PREBODY ACK naming the controls and the single ordered part. Only then I read part 01 serially raw, LF `1–20, 21–40, …, 881–900, 901–907`, through its ending, including complete long lines, before mathematical work or comparison. All genuinely held episodes **and all their consumers** remained NONINPUT. I did not follow the packet's outgoing links, read old code, sibling returns or any unspecified scientific source. This is no certificate about private cognition.

**Packet coverage and manifest-supplied pins.** Part 01 is 94,196 bytes, 907 LF, SHA-256 `cb27c6e8096055247d931057fb778465a7f7a354dcd009c723c649f44d230de9`. The following are all complete rendered bodies, identified by the dispatch manifest's supplied hashes, not independently rehashed here:

| ID | Body, relative to run root | LF | SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f788-boolean-two-E-one-plus-one-graph-author/author-candidate-v1.md` | 179 | `1c51df762a1878cae342b32b4a34fead49ca39c2813bdab41ba3e7a9ed3b737d` |
| S2 | `review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/parent-omitted-ell0-lambda-singleton-proof-gap-major-v1.md` | 7 | `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca` |
| S3 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-quotient-census-erratum-v1.md` | 9 | `90c4242e118be887f19b61ccba23f4af0c6062516142962b9a315557c0e03606` |
| S4 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-candidate-v1.md` | 121 | `e4e1c4a1812a03d0334dbee16dec50650d6a904e0e68b75dbcddae22e73aefa8` |
| S5 | `review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/author-candidate-v1-addendum-1.md` | 15 | `4dddaf7084e784b8c8d2b51b857320a26438a6a669b1ad9dee2f8d19268c4114` |
| S6 | `dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md` | 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S7 | `dispositions/info-6-entire-four-E-row-d0-actual-common-y-obstruction-parent-v1.md` | 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S8 | `review-waves/f755-boolean-remaining-D0-profile-and-U3-integer-finite-author/parent-u3-local-profile-v2-run-v1-receipt.json` | 256 | `d3cdcca328bf4c902c214ddbb9b5d42fccb41f56406147681c3baf2880f5aaf1` |
| S9 | `review-waves/f778-boolean-four-E-bent-parity-and-countermodels-finite-author/parent-v4-one-shot-run-v1-receipt.json` | 182 | `72ce3e26ffc187528890a9d0a808066ceb13b5d6fb9040644cf82f60b9871d08` |
| S10 | `parent-recovered-local-H-definition-and-general-g-foundation-v1.md` | 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |

All 22 complete status/permission controls are those listed and pinned in this wave's `manifest-v1.json`: method-scope restoration and owner direction; parent L1, privacy, core-Gram, AME and PH quarantines; the f439, f444, f448, f508, f513, f586, f602, f596, f653, f654, f659, f660 and f662 quarantine controls; parent remaining-D0 occupancy omission and f746/f749 design corrections. They supply no mathematical premise. Manifest SHA-256 `bbde77a3b5b829520bd343dcc0267b492b2edc472b836a118b30e0993d01b67a`, freeze receipt `9de47dacf2c02b130d82a746064c73af1ef2b6197e456c07fedbff1bcb0c51c6`, final binding `1dcfff34729c01c26c40e19c52fd725ab4d7444928e575abfe6b63b0e65dd845`, and prepared metadata `cb43a3e4c60c8374eb269763a0d3897f4e3c9a30185d3674ab665e4906b96fd1` are parent-supplied administrative metadata, not independent verification.

**NOT TESTED:** no child scientific program, numerical enumeration, solver, CAS, compiler, test, build, linter, external CLI, network, Git, installation or deletion was run. No scientific source program was prepared. This candidate is a written proof requiring separate independent scrutiny.
