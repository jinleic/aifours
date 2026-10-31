# f50 — independent review of the PH7 two-cycle algebraic endpoint

**Reviewer:** MathKacMoody-2, same harness as author. **Clock before writing:** Wed Oct 28 17:47:14 PDT 2026. **Status:** WRITTEN-supported at the exact inputs and computational trust boundary below; not parent adoption, an independent-model review, a human or formal proof, or a novelty/priority judgment.

## Verdict, findings and scope

- **FATAL 0, new MAJOR 0, new MINOR 0.** I reconstructed the claimed actual same-matrix PH7 construction for all `c,d>0` and all `z` in the closed, exactly specified interval `[7/9,z_*]`, including `z=z_*`, at ordinary real-analysis and finite-algebra inputs. The exact checks are executable SymPy checks, not a proof assistant.
- **Existing documentary MINOR, explicitly corrected by the author's mandatory erratum:** the unchanged v4 manuscript LF112,135,162 overstates what the earlier *v2 checker* verified. Its six rates were fixed rational values; that checker is not a certificate for arbitrary six rates or for these algebraic `U,V`. The erratum LF3–16 corrects this and restricts its new algebraic check to `(U,U,U;U,V,V)`. I independently reconstructed and checked that restricted family below, and do not rely on the author's new checker as a correctness premise. The overstatement remains part of the frozen record; the erratum, not silent rewriting, controls it.
- Conditional on the separately named old topology-unrestricted lower bound for PH order at most six, the actual upper bound gives minimum **exactly 7** on `[7/9,z_*]`. At the additional named old direct upper-band/overlap interface it extends to `[13/20,z_*]`. Neither old proof is freshly reconstructed here, and neither is part of the new matrix upper construction. In particular the purported old unrestricted lower is not proved anew by this review.
- No PH7 witness or exclusion at `8/9`, no optimum for this or any other topology, no whole minimum-order classification, no new topology and no novelty claim is established. The small endpoint improvement is not an `8/9` solution.

## 1. Provenance, source order and prior familiarity

I first pinned my current math-3 primary candidate before this assignment. I read the complete 25-LF assignment, then the entire mandatory 20-LF v4 erratum **before** the entire 174-LF v4 manuscript, including its §§6–7. The same reviewer had previously completed and returned the f18 reviews of the author's 813/1000 and 41/50 PH7 bands, and had read the registered target and named older PH boundaries then. Therefore this is not a blind or independent-family review. This review builds its own restricted-family equations and finite checks; it does not transfer the older f18 verdict or import the author's checker/output. The exact v3 cubic definition and endpoint interval, used only for the endpoint-comparison claim, were additionally read at v3 LF1–21 after the assigned two inputs; I did not review its full PH7 proof here.

| Item | LF | SHA-256 |
|---|---:|---|
| `review-waves/f50-ph7-algebraic-endpoint-v4/assignment-v1.json` | 25 | `604db363c239ed2783423cd74e8995a553b32a0b4c65805cbb82542797a87dd5` |
| `phase-type/frontier-20261028-ph7-two-cycle-endpoint-v4-erratum-v1.md` | 20 | `b5526a1556a61786c5cc382e924087a318b31b6640b35d30a41fe9d3fe22cc30` |
| `phase-type/frontier-20261028-ph7-two-cycle-endpoint-v4.md` | 174 | `4f63347198b12ce6dfefb5c7c94adf95fcc262234d29ce055e6f789bff27e191` |
| `phase-type/frontier-20261028-ph7-algebraic-endpoint-v3.md` | 179 | `99ec7400496a91963cffd55a16202e4ca07d5e5e90e734bcf6585931b2d14ed2` |

`phase-type/` in this table abbreviates `mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/`, not my write root. The assignment and author inputs were not modified. The v3 hash binds the file, not a claim that its whole 179 LF were read during this assignment.

## 2. Reconstructing the root and the exact comparison

Manuscript LF27–68 defines

\[
D_z(y)=y((y+1)^2+z)^2,\quad p_0=5U+2V-4,\quad
q_0=10U^2+10UV-20U+V^2-8V-2z+10,
\]
\[
R=(y+U)^5(y+V)^2-D_z(y)(y^2+p_0y+q_0),\qquad
F=(E_4,E_3,E_1)
\]
with `E4=[y^4]R`, `E3=[y^3]R` and `E1=[y]R-2V[y^2]R`. The leading three coefficients `[y^7]R,[y^6]R,[y^5]R` vanish identically; this was checked directly from these definitions. Define `x0=(1338787907,1042029691,820420441)/10^9`, `r=10^-7`, `J=DF`, `A=J(x0)^(-1)` and `Phi(x)=x-A F(x)` as in LF57–64.

My checker computed the exact rational inverse, verified `A J(x0)=I` and bounded every coefficient of the polynomial matrix `I-A J(x0+delta)` by its absolute coefficient times `r` raised to the total degree. It then summed each row. All three bounds are strictly `<1/100`; the exact maximum is recorded in the output JSON. It also checked `||A F(x0)||_infinity<r/100` exactly. Thus the max-norm mean-value estimate gives `||Phi(x)-Phi(x')||<=||x-x'||/100`, while `||Phi(x)-x0||<=2r/100<r` on the whole closed box. Iteration in the complete box gives a fixed point in its interior and a unique fixed point in the box; invertibility of `A` makes this the unique `F=0` there. This is a non-sampling certificate for a genuine real algebraic triple. No global uniqueness is asserted.

The interior conclusion gives exactly

\[
820420341/10^9<z_*<820420541/10^9<8/9.
\]
It also shows `z_*>41/50`. The earlier v3 source LF11–20 specifies its own root as the unique zero of a displayed integer cubic in `(820409/10^6,82041/10^5)`. A separate exact checker evaluated the two endpoint signs and proved the derivative positive over that whole interval by its three Bernstein coefficients. Hence that root exists uniquely there, and its upper bound `820410000/10^9` is strictly less than this v4 lower bound. This certifies only the comparison of the two defined roots, not the rest of v3's PH proof.

## 3. The same raw matrix and every feedback term

For the six rates `(U,U,U;U,V,V)`, let `e_j` be their elementary symmetric functions and put `A0=e1`, `B0=e2`, `C0=e3`. Define `H0,L,N,p,q,w,B,C,phi,R2,R1,R0,D1,D2,D3` exactly as in manuscript LF78–93, in particular `p=N/L`, `q=(A0-4)p+H0-2z`, `w=p+4-A0`, `B=p-2U`, `C=q-Up+U^2`, and `Q(y)=y^2+py+q`. The actual `G`, `beta=(C,B,1,0,0,0,0)` and `gamma=K e7` are the entries at LF95–105; there is no separate guessed denominator matrix.

For that actual matrix, direct determinant expansion with **free** `U,V,w,phi,D1,D2,D3` yields the complete polynomial identity

\[
\det(yI-G)=(y+w)(y+U)^4(y+V)^2
 -\phi(y+U)^3-D_1(y+V)^2-D_2(y+V)-D_3.\tag{1}
\]
The rank-one determinant identity for the same `G` and arbitrary `B,C` gives

\[
\beta\,\operatorname{adj}(yI-G)e_7
 =C+B(y+U)+(y+U)^2=Q(y).\tag{2}
\]
These statements are polynomial identities, not inverse formulas assumed at roots. They retain both feedbacks and their interaction through the actual determinant. After the displayed rational coefficient substitutions I independently checked that `L` times `(1)-D_z(y)Q(y)` is identically zero in the full formal variables. Thus for every `L!=0`,

\[
\det(yI-G)=D_z(y)Q(y),\qquad
\beta\operatorname{adj}(yI-G)\gamma=KQ(y).
\]
This is not a general arbitrary-six-rate identity; it proves exactly the restricted symbolic family needed for v4. No coprimality, diagonalizability, or pole-separation premise was used.

For the endpoint, I checked the exact formal identity `E4=L p0-N`. At the root, positivity of `L` gives `p=p0`, and the definitions then give `q=q0` and `w=U`. Under these substitutions the `y^3` residual is `E3`, hence `phi=0`; `D1=[y^2]R` after setting `phi=0`, and the remaining `y` residual is `E1`, hence `D2=0`. This establishes the asserted **same** endpoint matrix, with its two vanishing feedback entries, not a limiting or independent profile.

## 4. Uniform interval signs, including both endpoints

The checker used the larger rational interval `I=[7/9,820421/10^6]`, containing the whole `z` box and hence `[7/9,z_*]`, and the whole `U,V` rate box. For each expression below it expanded its exact polynomial after multiplying by `L` where appropriate and subtracting the displayed floor:

\[
L-1,\ Lp-7,\ Lq-9,\ Lw-2,\ LB-3,\ LC-2,\ LD_1-3,\ LD_3-2,
\ -\partial_z(L\phi)-6,\ -\partial_z(LD_2)-9/10.
\]

It converted each polynomial in `z` to its complete Bernstein basis on `I`. Its 30 exact coefficients have degrees `1,1,2,1,1,2,3,4,2,3`, respectively. Each coefficient is a polynomial in `U,V`; expanding at the exact rate center and subtracting the sum of absolute nonconstant coefficient contributions over radius `r` gave a **strictly positive rational lower bound for every one of the 30**. These full lower bounds and the exact contraction/residual bounds are in the pinned output, not rounded approximations. Bernstein nonnegativity and the box estimates therefore prove all ten uniform inequalities claimed at LF120–122, not only a finite set of sampled rates or z values.

In particular `L>1`; `p,q,w,B,C,D1,D3>0` and the entire rate box has `U,V>0`. With fixed root rates, the strict derivatives `partial_z(L phi)<-6` and `partial_z(L D2)<-9/10`, together with `L phi=L D2=0` at `z_*`, imply `phi,D2>0` for `7/9<=z<z_*` and exactly zero at `z=z_*`. Division by `L` is justified everywhere. This proves Metzler nonnegativity on the **closed** interval without dividing by either feedback or assuming it is positive at the endpoint.

## 5. Every PH tie and dimensional scaling

For `d=1`, choose any `c>0`, let `K=D_z(c)>0` and `Q_c=c^2+pc+q>0`, and define `h` exactly as LF128–133. The first three recurrence equations give

\[
h_1=1/Q_c,\ h_2=(c+U)h_1,\ h_3=(c+U)h_2,\ h_4=(c+U)h_3.
\]

`h7`, then `h6`, then `h5` are strictly positive by the displayed positive denominators and nonnegative feedbacks; `K>0` makes `h7>0` even when both endpoint feedbacks vanish. My free-parameter symbolic calculation checked six noncentral rows of `(cI-G)h=K e7` directly, as well as `beta h=1`. For the center row it checked the exact identity

\[
((c+w)h_4-h_5)\,Q_c(c+U)(c+V)^2
=\det(cI-G)-KQ_c.
\]

By (1) and the coefficient identity, the right-hand side is `D_z(c)Q_c-KQ_c=0`. Every multiplier on the left is strictly positive, so the seventh row also holds. This gives an actual vector `h>0`, not an unjustified appeal to a sign of an inverse.

Set `Delta=diag(h)`, `T=Delta^-1(G-cI)Delta`, `alpha=beta Delta`, `omega=Delta^-1 K e7`. The proven signs give `T` Metzler, `alpha>=0`, `alpha 1=beta h=1` and `omega>=0`. The actual seven rows give `-T1=omega`. The roots of `det(yI-G)` are `0`, the repeated pair `-1±i sqrt(z)`, and the roots of `Q`; real `p,q>0` place both roots of `Q` strictly in the left half-plane. Thus `G-cI` and its diagonal conjugate `T` are Hurwitz. By (1)–(2), the exact same `alpha,T,omega` have transfer `K/D_z(s+c)`, even at repeated/cancelled roots by polynomial identity.

For general physical `d>0`, first build this representation with `c0=c/d`, `z=b^2/d^2`; then replace `T,omega` by `dT,domega` and keep `alpha`. The transfer is the normalized transfer evaluated at `s/d`, namely

\[
\frac{c((c+d)^2+b^2)^2}{(s+c)((s+c+d)^2+b^2)^2}.
\]

This equals the registered target with `a=c+d`; `b` enters only through its square. The transformation and normalization remain valid at `z=z_*`.

## 6. Computational evidence, imports and unresolved gates

I authored two new bounded checkers in my own root; neither reads any author checker or certificate. They reuse only generic `esym`, `zero`, and Bernstein helpers from my earlier f18 reviewer-owned script. `SymPy 1.14.0` was loaded from an already-present local dependency directory; the author used the same library family, so this is independently constructed code, **not** an independent implementation/library, proof assistant or external-model review. All calculations are exact rational or polynomial symbolic operations; no floats, nonlinear numerical root, sampled-state evidence, or optimizer result is used in the verdict.

| Reviewer-owned artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-review-f50-ph7-endpoint-independent-check.py` | 150 | `5b8298af45ce3ec1f7c58905da9c95ea0f9eab75ca62dfd14100fef4600d575d` |
| `frontier-review-f50-ph7-endpoint-independent-check-v1.json` | 103 | `ea6014667cf160c5794eb1f6b27b592d4d8babae25e6112fd4f94ba0a4eeb2c0` |
| `frontier-review-f50-v3-root-check.py` | 29 | `9c2ad4a6c9c023d33012e8ea4a6c831956b925099a665c75671629fab52c0572` |
| `frontier-review-f50-v3-root-check-v1.json` | 11 | `c5a41bb68fe305547cb8fddda94d59f311b4b6ca189d4298a4a2c2b8d78749d8` |
| reused reviewer helper `frontier-review-f18-ph7-independent-check.py` | 180 | `0d1b35f603c45eb503436d1bdd5fa89f185af32d93adcdcec74051e1fc8f345d` |

The first actual command returned `PASS: SymPy 1.14.0; exact contraction <1/100 and center residual <radius/100; 10 uniform Bernstein-box bounds; endpoint identities; free 7x7 det/numerator/normalizer` before Wed Oct28 17:46:02 PDT. The second returned `PASS: old v3 cubic has unique root in cited interval; v3 upper < v4 lower` before 17:46:56 PDT. Their checks are exactly those described above; they do not establish any old lower bound or novelty claim.

Named unresolved conditional imports are: old PH6 lower `proof-unrestricted-six-state-barrier-v1.md`, SHA-256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, for exact minimum 7; and old direct upper overlap as qualified in `institute/runs/three-area-2026-10-23-96h/PH7-entire-rational-seven-ninths-band-parent-v1.md`, for the lower end `13/20`. Their historical process and scope qualifications remain. The old farther extension to `1/2<z` has additional named old upper/G7 imports and is **not** freshly reconstructed or included as a new conclusion here.

No author contact, independent-family/external-model assessment, formal verification, novel-priority search, or new claim at `8/9` was performed. Prior process findings, STOP/HOLD/ZERO boundaries and old-file immutability remain unaffected.

**END — f50 same-harness written review, exact upper construction only; exact order conditional on named old lower.**
