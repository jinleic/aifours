# All four D0 blocks cannot lie on graph mates: profile/phase obstruction

**Status: NONBLIND GENERAL-AUTHOR WRITTEN CANDIDATE, NOT ADOPTED.** This is a proposed proof for the exact common rank-two, five-span physical interface below. It is not an independent review, a finite pass, a full original-caller result, or an NL242 conclusion. In particular, the result does **not** assume or prove that the four D0 blocks all lie on graph mates. It shows that such an allocation is impossible under the stated caps, and hence, using the imported four-distinct result separately, that any surviving caller has at least one D0 in the six E-row blocks. The cases with E-row D0 remain open.

## 1. Exact claim and imports

Use the SAME physical ternary inverse, `x=U0`, `y=U3`, graph function `f`, phase `R`, `a`, `g`, local `H_loc=0`, counts, specified original-DC transport `t`, and all original interfaces in S1–S5. Explicitly, this is the rank-two polar branch with bent `f+q`, `q(b)=1+b0*b1`, and common bent phases `R,R+f`; D0=4, D3=18, Z2=6, Z4=1, Z0=17; `sum x^2=56`, `sum y^2=128`; all 64 `x` coefficients divisible by 8 and capped by 8; **the specific** `xhat(t)=0`; `J=1`; and all 64 `y` coefficients capped by 12. S2 gives the local-H definition and general g, S3 supplies the seven simultaneous U0 profiles at the stated imports, S4 the graph/bent interface, and S5 the physical counts and residue. S1's one-D0-per-graph-coset exclusion is an imported theorem, not proved anew here. No linked source, unassigned sibling proof, or old code is used.

**Proposed theorem.** Under exactly these imports and caps, none of the four graph-mate occupancies `(4)`, `(3+1)`, `(2+2)`, `(2+1+1)` can occur when all four D0 blocks are graph mates. With S1, the remaining graph-mate partition `(1+1+1+1)` is also excluded. Consequently `d_E >= 1`, where `d_E` counts D0 on the E row. This is a necessary condition only; it neither produces nor excludes a common caller with `d_E=1,2,3,4`.

The proof below uses no formula for a unique D0 exception in an even-occupancy row, no prior three-cell location conclusion, no assumed XOR of graph Y covectors, and no frequencywise independent sign choices. The structural assertions and exclusions are all at the written-candidate level until parent scrutiny.

## 2. Same-object coordinates and complete local equations

Write `I=B=F2^2`, `Q(v0,v1)=(v1,v0)`, and use the common radical coordinates of S3/S6: `(ell,h,i,b)`, physical mate direction `e` toggling `h`, graph `ell=1,h=F_i`, and `sum_i F_i=1`. Physical `b` is unchanged by this coordinate choice. Let `X(c)=(-1)^(t.c)x(c)` and `Y(c)=(-1)^(t.c)y(c)`. The same modulation translates both spectra and preserves all stated caps, the given zero, and `4 mod 8`; it does **not** replace the fixed physical `a,g` or claim that the inverse is itself being modulated.

In graph row `i`, let `D_i subset B` be the actual mate D0 locations, `k_i=|D_i|`, `S_i(b)=X(1,F_i,i,b) in {+1,-1}`, and `Dsgn_i(b)=X(1,1+F_i,i,b)/2`, equal to a sign on `D_i` and zero elsewhere. For `s in F2, alpha in B*` define the exact partial coefficient

`Z_(ell,i)(s,alpha)=(1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha(b))`.

The eight quotient labels are `(ell,i)`. For every `(ell,i)`, `Z(0,0)=0`. Each of the other seven columns, simultaneously for this **one** X, is either one entry `+/-2`, or four entries `+/-1` supported on an affine 2-flat of `F2^3` with sign product `-1`. This is the S3 equivalence at its full imported boundary. In particular the number of odd entries in its ell=1 half is always 0, 2, or 4.

With the unnormalized two-bit Walsh transform denoted by a hat, the exact row formula is

`Z_(1,i)(s,alpha)=(-1)^(s F_i) [Shat_i(alpha)+2(-1)^s Dsgnhat_i(alpha)]/4`.   (2.1)

The specified zero gives, row by row, `Shat_i(0)+2 Dsgnhat_i(0)=0`, not merely a global sum. If `p_i` is the number of negative `S_i` signs, then integrality, or directly this equation, yields `p_i == k_i (mod 2)`. Thus even `k_i` means `S_i` is a signed affine character, and odd `k_i` means `S_i=epsilon_i(2*1_(b=gamma_i)-1)` with one actual exceptional graph point. In the odd case the latter sign has graph sum `-2 epsilon_i`.

The common phase restrictions `R_i(b)` are affine, with row-linear parts `lambda_i` an affine bijection `I -> B*`; in particular `sum_i lambda_i=0`. The argument is the S6 graph/bent argument and is independent of D0 occupancy. For an even row write `S_i=epsilon_i(-1)^(xi_i(b))`. Then its graph Y row is bent and can be written `G_i(b)=sigma_i(-1)^(b0*b1+theta_i(b))`, `theta_i=lambda_i+xi_i`. For an odd row the graph Y row is a character with covector `kappa_i=lambda_i+(1,1)+Q gamma_i`. These statements use `Y=-a*g*X` on the SAME graph. The sign `sigma_i` absorbs the affine constants. Thus `(4)` and `(2+2)` have four bent graph Y rows, whereas `(3+1)` and `(2+1+1)` have two bent and two character rows.

The lambda-column graph entries simplify to

`Z_(1,i)(1,0)=-(-1)^F_i Dsgnhat_i(0)`.   (2.2)

A `k=0` row has `xi != 0` and lambda entry 0. A `k=1` row has lambda magnitude 1, its D0 mate sign equals `epsilon`, and its nonzero-alpha two entries have exactly one `+/-1`: it lies at extension `s=0` iff `alpha(gamma+u)=0`, otherwise at `s=1`, where `u` is the actual D0 b-coordinate. A `k=3` row also has lambda magnitude 1: its three D0 signs consist of two `epsilon` and one `-epsilon`; let `u` be the omitted mate and `v` the minority-sign D0 site. At each nonzero alpha it has one main `+/-1` at the same extension determined by `alpha(gamma+u)`, plus a possible opposite-extension `+/-2`. The latter occurs at exactly the unique nonzero `alpha=Q(u+v)`. This follows directly from (2.1): for nonzero alpha, `Shat=2 epsilon chi_alpha(gamma)` and `Dsgnhat=-epsilon chi_alpha(u)-2 epsilon chi_alpha(v)`.

A `k=2` row with the two D0 signs equal has constant `S`, lambda magnitude 2, and `xi=0`. With opposite D0 signs it has lambda 0 and nonzero `xi`. Write its two distinct locations `u,v`, `Delta=u+v !=0`, and `a_D=Q Delta`. For nonzero alpha its complete possibilities are:

* **active lambda:** at `alpha=a_D` both extensions have magnitude 1; at the other two they are zero;
* **inactive, N type:** `xi=a_D`; both extensions have magnitude 1 at all three nonzero alpha;
* **inactive, O type:** `xi!=a_D`; at `alpha=xi` exactly one extension has magnitude 2 and the other is zero, at `a_D` both are zero, and at `xi+a_D` both have magnitude 1.

These follow from the two-term transform of the actual signed D0 pair, not an exceptional-point formula. A `k=4` row has D0 sign sum 0 or `+/-2`, since the row-zero equation bounds it by 2. If the sum is `+/-2`, `S` is constant and lambda has magnitude 2; if it is 0, `S` is a nonconstant character and lambda is 0. The latter D0 sign function is itself a nonconstant signed character on all four b values.

For the present `d_E=0` proof, ell=0 X is supported on exactly six Z2 blocks, with `X=0` at physical b=0. Row-zero makes the number of those blocks in each ell=0 row even; hence at most three such rows are occupied. Also, for each ell=0 row and each s,

`sum_alpha Z_(0,i)(s,alpha)=0`.   (2.3)

If `z_i=Z_(0,i)(1,0)`, then for every alpha the parities of the two extension entries have XOR `z_i mod 2`; this is because their sum is the b-Walsh transform of the `h=0` ell=0 signs and its parity is independent of alpha. In particular, when the lambda column is a singleton `+/-2`, the odd-entry supports of the two columns at each nonzero alpha are identical. No such same-support statement is asserted for an arbitrary four-entry lambda plane.

## 3. Profile forcing of the common Y parity

Let `B_D=sum_(i,b in D_i) b`. For the four partitions in the theorem, the U0 profiles force

`sum_even theta_i + sum_odd kappa_i = Q B_D`.   (3.1)

Here and below all sums are XORs. This is a consequence, not an assumption. First, when there are two odd rows, their main odd entries must occur at the same extension for every nonzero alpha: elsewhere the even rows contribute equally to the two extension parities; at a `+/-2` singleton the other odd row must be in the other extension. Consequently their two offsets `gamma+u` are equal, with `u` the D0 site for k=1 and the **omitted** site for k=3.

For `(3+1)`, the two k=0 rows cannot use the special `+/-2` alpha of the k=3 row; at each other alpha their contributions must have even parity. Their nonzero character covectors are therefore equal. The XOR of the three D0 sites in the k=3 row equals its omitted `u`, so (3.1) follows from the common offset and `sum lambda_i=0`.

For `(2+1+1)`, lambda already has two odd graph entries, so the k=2 row is inactive. Its N type would contribute at both extensions for all three alpha and the only k=0 row could not match that parity at all three. Thus it is O type. Its `+/-2` alpha and its zero alpha cannot be the k=0 covector, so the latter is `xi_2+a_D`. Hence `xi_2+xi_0=a_D`, and the common odd-row offset gives (3.1).

For `(4)`, the XOR of its four D0 b positions is 0. If the k=4 row is active, it contributes odd entries at both extensions at each nonzero alpha; the three k=0 covectors must therefore be the three distinct nonzero values. If it is inactive, its balanced D0-sign character has nonzero covector `a`; its graph covector `xi` cannot equal `a`, since then (2.1) has a forbidden magnitude-3 entry. At alpha `a` both extensions are graph singletons, so the three k=0 covectors avoid `a`. At `xi` their multiplicity is odd, hence 1 or 3. Multiplicity 3 would make ell=0 vanish at `xi` and at `a`; at the third nonzero alpha the column still has energy 4 but (2.3) forces every ell=0 entry to vanish. Thus the multiplicity is 1 and the remaining two k=0 covectors coincide. In either case the four `xi` XOR to zero, giving (3.1).

For `(2+2)`, let A,B denote the k=2 rows, C,D the k=0 rows, and `a_A,a_B` their pair covectors. Lambda is a singleton: two active rows are impossible, and if both graph lambda entries are zero, a four-entry ell=0 lambda plane is impossible because at most three ell=0 rows are occupied. The table in section 2, even graph parity, identical odd supports of the two alpha extensions, and (2.3) give `sum_i xi_i=a_A+a_B` as follows.

* One active A and N-type B: `a_A,xi_C,xi_D` are the three distinct nonzero covectors; hence `xi_C+xi_D=a_A` and `xi_B=a_B`.
* One active A and O-type B: A,C,D avoid `xi_B`, and their counts at `a_B` and `c_B=xi_B+a_B` must be respectively even and odd. The counts 0 and 3 would make ell=0 zero at `c_B`, and in one extension also at `xi_B`; (2.3), with zero ell=0 lambda, would then force the nonzero column at `a_B` to vanish. Thus the counts are 2 and 1, giving `a_A+xi_C+xi_D=c_B`.
* Both inactive N: C,D have the same covector, giving the identity. N/O is impossible because the N row is odd in the singleton column of the O row.
* Both inactive O: if `xi_A != xi_B`, the singleton columns force `a_A=xi_B`, `a_B=xi_A`, and `xi_C=xi_D` equal to the third nonzero covector. If `xi_A=xi_B=xi`, the two singleton entries must be in opposite extensions, C,D avoid `xi`, and even parity at the two remaining alpha gives `xi_C+xi_D=(xi+a_A)+(xi+a_B)`. Both subcases give the identity.

Since `B_D=Delta_A+Delta_B` in `(2+2)`, this proves (3.1) there. No location theorem for one D0 per row was used.

Now define the actual ell partial Y transforms

`A_l(s,alpha,beta)=sum_(h,i,b) Y(l,h,i,b)(-1)^(s h+alpha(b)+beta(i))`.

Let `n` be the number of negative signs on the 12 nonzero graph mates, and let `m_alpha` count the odd-row graph characters equal to alpha. The graph contribution of each even row is twice a sign; its normalized bent dual has sign `sigma_i*(-1)^((alpha+theta_i)_0*(alpha+theta_i)_1)`. Multiplying these signs and the 12 actual mate-character signs yields, for a constant `c` independent of `s,alpha,beta`,

`A_1/4 == n+c+s+m_alpha+alpha(B_D+Q sum_even theta_i) (mod 2)`.   (3.2)

The beta exponent cancels because the XOR of all four i labels is zero. The s exponent is `sum_even F_i + sum_odd(1+F_i)=sum_i F_i=1`. The mate b exponent is `B_D`, since the XOR of the four b values in each complete row is zero. The even number of bent graph rows cancels the common dual quadratic term. Equation (3.1) makes the XOR of the odd-row kappa values equal to `Q v`, where `v=B_D+Q sum_even theta_i`. For the multiset of at most two odd-row characters, `m_alpha+alpha(v)` is constant: if the odd multiplicity set is empty then `v=0`; if it has two elements they differ by `Qv` and form a full level set of `alpha(v)`, since `(Qv)(v)=0`. Thus (3.2) has one parity for all alpha,beta at one h slice `s_*`, and the opposite parity at `s_*+1`. This establishes the required shared parity for every one of the four occupancies, without positing a global kappa XOR.

## 4. Shared energy forces all actual mate signs

`J=1`, the S2 general g and S5 physical residue give every full Y coefficient `4 mod 8`; its cap and energy 128 therefore force exactly eight magnitude-4 coefficients and 56 magnitude-12 coefficients. Since `A_0+A_1` and `A_0-A_1` are those two full coefficients, both partial transforms are multiples of 4, their quotients have opposite parity, and their pair of caps is equivalent to `|A_0|+|A_1|<=12`.

At `s_*`, let E count the 16 `(alpha,beta)` with `|A_1|=8`; the others have `A_1=0`. At `s_*+1`, let O count those with `|A_1|=4`; the others have magnitude 12. Every E or O position consumes at least one distinct magnitude-4 full coefficient, so `E+O<=8`. The ell=1 energy is exactly `16+12*4=64`; its 5-bit Parseval identity gives `O=2+E/2`. Put `C=sum_(actual 12 mates) G_i(b)e_i(b)`, where the mate value is `2 e_i(b)`. Parseval over `(i,b)` at `s_*` gives `E=16+(-1)^s_* C>=4`. Consequently `E=O=4`, and equality in `|C|<=12` forces, at **every one** of the 12 actual mate sites,

`e_i(b)=-(-1)^s_* G_i(b)`.   (4.1)

In addition, all four O positions must have `|A_0|=8`; otherwise an `A_0=0` position would contribute two small full coefficients in addition to the four already consumed by E. At `s_*+1`, (4.1) makes the h-transformed Y row equal to

`(-1)^((s_*+1)F_i) G_i(b) [3-2*1_(b in D_i)]`.   (4.2)

For any three distinct i in `F2^2`, some beta aligns their three real signed row contributions. This is the only beta choice in each following contradiction and is a genuine single physical frequency.

## 5. Three immediate occupancy exclusions

For `(4)`, one row has no mate Y and contributes a bent-row Walsh value of magnitude 2. The other three k=0 bent rows each contribute magnitude 6 by (4.2). Align those three: `|A_1|>=18-2=16`, impossible.

For `(3+1)`, at alpha equal to the k=1 graph character the k=1 row contributes magnitude 10; each k=0 bent row contributes 6; the k=3 character row contributes at most 6. Align the first three: `|A_1|>=10+6+6-6=16`.

For `(2+1+1)`, each k=2 bent-row contribution in (4.2) has magnitude 2 or 6: if the two deleted signed graph summands are equal, the other two summands are opposite because a bent row has sign product -1, and the resulting magnitude is 2; if they are opposite the magnitude is 6. If the two k=1 characters are distinct, take alpha equal to one: their row magnitudes are 10 and 2, the k=0 row has magnitude 6, and the k=2 row has magnitude at least 2. Align the 10, 6 and k=2 rows to obtain at least 16. If the two characters coincide, align the two magnitude-10 rows and the k=0 magnitude-6 row; subtracting the k=2 row of magnitude at most 6 still gives at least 20. Thus all three allocations fail.

## 6. The `(2+2)` exclusion, including the physical Z2 locations

Let the k=2 rows be A,B and their pairs be `(u_A,v_A)`, `(u_B,v_B)`. Set `Delta_i=u_i+v_i`, `P_i=G_i(u_i)G_i(v_i)`. At each alpha, row i has magnitude 2 precisely when `P_i*(-1)^alpha(Delta_i)=+1`, and otherwise magnitude 6. If their magnitudes differ, three rows have magnitude 6 and one has magnitude 2, so aligning the three gives at least 16. Hence both predicates agree for every alpha. Evaluating at alpha=0 and varying alpha gives

`Delta_A=Delta_B=Delta !=0`, and `P_A=P_B=P`.   (6.1)

By section 3, `sum_i theta_i=Q(Delta_A+Delta_B)=0`. The product of the four normalized bent-dual signs is therefore independent of alpha. Equation (4.1), the odd parity of each bent graph Y row, and removal of the four D0 sites give `(-1)^n=P_A P_B=1`. The product of the four signed row-dual signs at `s_*+1` is consequently `-1` (equivalently it is `-P_A P_B`). Thus for each of the two alpha satisfying `(-1)^alpha(Delta)=P`, the four beta values of `|A_1|` are `4,4,12,12`; for the other two alpha all four are 12. This follows by the four-point transform of an odd-sign vector with weights `(2,2,6,6)` or `(6,6,6,6)`.

Define the single ell=0 h-combination `B_i(b)=Y(0,0,i,b)+(-1)^(s_*+1)Y(0,1,i,b)`. At the two alpha outside the above level set, every beta has `A_0=0`. At each alpha inside it, exactly two beta have `A_0=+/-8` and the other two have `A_0=0`, by section 4. Therefore `Bhat_i(alpha)` is 0 or `+/-4` and is nonzero for exactly two i. The two allowed alpha differ by `a=Q Delta`; at b=0 the inverse gives `|B_i(0)|<=2`, while the physical F/E blocks make `B_i(0)` either 0 or `+/-4`. Hence `B_i(0)=B_i(Delta)=0`; the latter equality also follows from the Fourier level-set relation `B_i(b+Delta)=P B_i(b)`. The two Fourier entries in each row are negatives, so the same two rows, call them U,V, are the only nonzero B rows. If `p,q` are the two nonzero b values other than Delta, then `p+q=Delta` and, in each of U,V, `|B_i(p)|=|B_i(q)|=2`; all other B entries vanish.

This gives an exact *derived*, not assumed, physical Z2 arrangement. The unique Z4 cannot be at a zero B site, since `+/-4` plus at most one `+/-2` cannot cancel. It lies at one of the four `(U or V,p or q)` sites and has a Z2 in the other h slot. Each of the other three sites has exactly one Z2. The remaining two of the six Z2 must be an opposite-h cancelling pair at one other site. That pair cannot occupy a third i row: its X signs are opposite by row-zero, which would give an ell=0 lambda entry of magnitude 1, whereas the lambda profile here is a singleton `+/-2`. Hence the pair is in U or V; rename its row U. It cannot be at p or q, where one h slot is already occupied, so it is at Delta. Row V has only its p,q Z2, with opposite X signs in the same h. Row U has Z2 at both h over Delta, and one each over p,q in opposite h. Its lambda value is 0 or `+/-2`; when it is 0, the two X signs in each h are opposite, and when it is `+/-2` they are equal within each h.

The resulting U0 profile consequences are particularly restrictive. For every nonzero alpha other than `a=Q Delta`, `Z_(0,U)(0,alpha)` and `Z_(0,U)(1,alpha)` are both `+/-1`. Their ratio changes sign between those two alpha. This is direct: `alpha(Delta)=1`, while the characters of p and q are opposite, so exactly one of the two h-row transforms is nonzero; as alpha changes by a, that nonzero h swaps. If lambda at U is zero, at alpha a exactly one of these two entries is `+/-2` and the other zero. If lambda at U is `+/-2`, both entries at alpha a are zero. Row V, whenever its entries are nonzero, has a fixed extension ratio `(-1)^h_V` because its p,q sites have the same h.

An inactive O-type k=2 row would have a graph singleton `+/-2` at its `xi != a`, contradicting the two nonzero U entries there. Therefore every inactive k=2 row is N type. If one k=2 row were active, lambda at U would be 0; at alpha a the active and N graph rows both have `+/-1` entries in each extension, contradicting U's `+/-2` singleton. Thus both k=2 rows are inactive N type, and lambda at U is `+/-2`. The two k=0 rows must have a common character covector eta by even graph-support parity. If `eta != a`, their two entries and the two N-row entries fill the entire graph plane at eta, contradicting U's odd entries. Thus `eta=a`.

For each of the other two alpha, the profile is now the *same physical* four-entry affine plane consisting of graph rows A,B and ell=0 rows U,V. Its sign product is `-1` in each of the two h-extension columns. On each graph row the ratio `Z(1,alpha)/Z(0,alpha)` is `-(-1)^F_i`, independent of alpha, because only its signed D0-pair transform contributes. The V ratio is also independent of alpha; the U ratio flips between the two alpha. The ratio of the two required plane sign products would therefore flip from `+1` to `-1`, contradiction. This excludes `(2+2)` without assuming the one-D0 location theorem, a three-cell Z2 pattern, or a pre-existing kappa XOR.

## 7. Broader frontier and explicit nonclaims

The proof of sections 2–6 is ONLY for `d_E=0`; the four partitions treated sum to four graph D0. The imported S1 disposes of the fifth partition `(1+1+1+1)` at its own exact scope. The resulting candidate `d_E>=1` still permits `d_E=1,2,3,4`; those occupancies are neither witnesses nor excluded here. For general `d_E`, `sum_i k_i=4-d_E`, the graph X energy is `32-4*d_E` and the ell=0 X energy is `24+4*d_E`. Since the zero profile column vanishes, the corresponding seven-profile energies are respectively `16-2*d_E` and `12+2*d_E`. The d_E=0 assumptions that ell=0 X vanishes at b=0, that its nonzero rows contain only six Z2, and that ell=1 Y energy is 64 do not automatically carry to those cases. They are not reused there.

No single common surviving `f,R,x,y` is constructed; no V sign choice or all-odd-fibre cap is supplied; no full original selected-T/gauge/rank/eight-zero caller is reconstructed. There is no proof of whole rank-two, rank-four, five-span, six-span, m114, Boolean, or global NL242 closure. Original-source identity, novelty, worldwide priority, independent model family, human review, and kernel/formal verification are not established. All genuinely held episodes and **all** proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. Parent must independently read the entire candidate and imports, reconstruct the parity bridge and section-6 Z2/profile argument, and issue a separate disposition. The result is nonblind and same-harness.

## 8. Provenance, coverage, and NOTTESTED

After actual dispatch and direct PREBODYACK to Main, I read the single packet serially as RAW LF 1–335 in ordered ranges of at most 20 LF, through its ending before any comparison or mathematical research. Before ACK I read the full manifest, freeze receipt, final binding, prepared metadata, actual dispatch, and all 22 listed controls through their endings. I did not follow outgoing links or read the six source paths separately; their following SHA-256 values are the parent-supplied bindings for the complete literal source blocks, not independent rehashes of those source paths:

* S1, 31 LF: `ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928`.
* S2, 13 LF: `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef`.
* S3, 37 LF: `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a`.
* S4, 38 LF: `443d0a1a94384e237076cb7974b49845e6fa52edf3ca83f161259e79a369de1e`.
* S5, 51 LF: `fc7169410a6540a6d63ea033720a90207fd49e89e4cc048d9eb208639eb65e5c`.
* S6, 139 LF: `63cc4fa48e0dececec9a381b32ca75191eec31e22e2cb3fb4907d7275437e890`.

Post-body administrative SHA-256 observations: manifest `eef0b109d634c44f40ebc325c65956d9404b3a5d7438960328951c3392319814`; freeze `118612db6d41ab25cb4e8d6d1093bc2cc2a18b651cd4ade669c014e86da72680`; final binding `7e5978a94790b7bfe45c5c308a74d06f3b0df7a1e6a4de2d6a7acf67c02d5a69`; prepared metadata `64c70e19235d1fa94a6cdc5fa0c5aa64338e6e58a8e641dadc0255c3b50b72fe`; actual dispatch `ab5e6d3595351aedacf932269d49944189d5a5e1052f9abf635cf589c88067`; packet `af6c3bac44a033bba82427d6bb43ea5ab4fd05a70a2c5f66e10a6d0cd2c106f3`. The native clock observed before candidate creation was `2026-10-30T17:39:37-0700 PDT`, not an asserted exact write time.

**CHILD SCIENTIFIC EXECUTION NOT RUN.** No scientific program, solver, CAS, finite check, build, test, linter, formatter, external-model CLI, or linked source was run/read. Administrative metadata hashing is not a scientific test. There is no finite source or parent GO in this return, no computational pass, and no correction to an earlier candidate: this is the first exclusive final-bytes candidate for this wave. Any discovered flaw requires an additive correction with a fresh path, not an overwrite. Every mathematical claim above remains pending full independent parent review.
