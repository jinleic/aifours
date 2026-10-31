# F764: common graph parity without the false odd-offset lemma

**NONBLIND GENERAL-AUTHOR WRITTEN RESULT; NOT ADOPTED.** Native clock observed before this creation: 2026-10-30T17:52:14-0700 PDT. At the exact same-object imports below I independently derive F747 (3.1), the common partial-Y parity (3.2), the E/O equality and the `4`, `3+1`, `2+1+1` contradictions. The derivation works also for the `2+2` partition through the parity and forcing steps; it does **not** independently establish F747 §6's subsequent `2+2` contradiction. The separate parent-adopted `1+1+1+1` theorem is an import, not a new proof. Therefore **this return does not establish `d_E >= 1` or the entire all-graph-D0 exclusion**. It supplies a repair of the parity bridge and exposes two false profile-level inferences in F747 §3, with explicit all-seven-profile examples. No parent acceptance or full-caller counterexample is implied.

## 1. Exact quantified interface

For every *one common* normalized rank-two physical object at the imported S4/S5/S6 interfaces, take `I=B=F_2^2`, quotient labels `(ell,i)`, and local coordinates `(ell,h,i,b)`. The physical mate toggles `h` and leaves `b` unchanged; graph sites are `(1,F_i,i,b)` with `sum_i F_i=1`. The same bent graph function and common phase give graph phase linear parts `lambda_i` with `sum_i lambda_i=0`. The SAME `x=U0`, `y=U3`, phase, `a`, general `g`, actual `T`, and original-DC transport `t` are retained. Set `X(c)=(-1)^(t.c)x(c)` and `Y(c)=(-1)^(t.c)y(c)`; this common modulation shifts both spectra and does not change the physical `a`, `g`, or transport. On the graph, `Y=-agX`. Use the local-H definition and counts in S5/S6: `D0=4`, `D3=18`, `Z2=6`, `Z4=1`, `Z0=17`, `sum X^2=56`, `sum Y^2=128`; all 64 U0 coefficients are divisible by 8 and capped by 8, with the SPECIFIC transported zero, `J=1`, and all 64 U3 coefficients capped by 12. S6's seven simultaneous profile equivalence and S4's graph-phase foundation are imported at their stated boundaries, not unrestricted independent-column choices.

Here `d_E=0`: all four D0 are graph mates. Write `D_i subset B`, `k_i=|D_i|`, and `B_D=sum_i sum_(b in D_i) b`. The named four partitions are `4`, `3+1`, `2+2`, and `2+1+1`. The total graph count for general `d_E` is instead `sum_i k_i=4-d_E`, with `d_E=0,1,2,3,4`; nothing here removes any `d_E>0` case. The one-per-row `1+1+1+1` subfamily is separately excluded by S4 only under S4's own full imports. Neither S4 nor this return proves whole rank two, full rank, V, the selected-T/original caller or NL242.

For `alpha in B*` let `chi_alpha(b)=(-1)^alpha(b)` and identify `B*` with `F_2^2` by the standard dot product. Write `Q(b_0,b_1)=(b_1,b_0)`. The same-X profiles are

`Z_(ell,i)(s,alpha) = (1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha(b))`.

For all eight quotient labels, `Z(0,0)=0`. EACH of the seven nonzero `(s,alpha)` columns is simultaneously either a single `+/-2`, or four `+/-1` entries on an affine 2-flat in the three quotient bits with product `-1`. In particular the odd-support vector is zero or a 4-point affine plane. Graph row notation: `S_i(b)=X(1,F_i,i,b)` is a sign and `d_i(b)=X(1,1+F_i,i,b)/2` is a sign on `D_i`, zero elsewhere. For unnormalized two-bit Walsh transforms,

`Z_(1,i)(s,alpha)=(-1)^(s F_i)[Shat_i(alpha)+2(-1)^s dhat_i(alpha)]/4`.  (2.1)

The row-zero equation is `sum S_i+2 sum d_i=0`, and the lambda entry is `Z_(1,i)(1,0)=-(-1)^F_i sum d_i`.

## 2. Complete local row analysis, including the singleton alternative

If `p_i` counts negative graph signs, the row-zero equation modulo 4 gives `p_i=k_i (mod 2)`. Thus for even `k_i`, `S_i=epsilon_i chi_xi_i` for an affine character, including `xi_i=0`; for odd `k_i`, `S_i=epsilon_i(2 1_(b=gamma_i)-1)`. All signs below are actual signs of the SAME array; descriptions of a pair do not make its columns independent.

* `k=0`: the row-zero equation requires `xi!=0`; lambda is zero. At nonzero alpha, both extensions are odd exactly at `alpha=xi`.
* `k=1`: the sole mate is at `u`, with `d(u)=epsilon`; lambda has magnitude 1. At nonzero alpha exactly one extension is odd, at `s=alpha(gamma+u)`.
* `k=2`, equal mate signs: row-zero makes `S` constant, and lambda is a graph singleton of magnitude 2; call this **active**. For distinct sites `u,v`, put `Delta=u+v!=0`, `a=Q Delta`; at nonzero alpha, both extensions are odd exactly at `alpha=a`.
* `k=2`, opposite mate signs: lambda is zero and `xi!=0`; call it **inactive**. In **N type**, `xi=a` and both extensions are odd at every nonzero alpha. In **O type**, `xi!=a`: at `alpha=xi` exactly one extension is a `+/-2` singleton, at `alpha=a` both are zero, and at `alpha=xi+a` both are odd. Indeed `dhat(alpha)=epsilon chi_alpha(u)(1-chi_alpha(Delta))`, while `Shat` is nonzero only at `xi`.
* `k=3`: the three mate signs have sum `epsilon`; two equal `epsilon`, one `-epsilon`. Let `u` be the OMITTED mate and `v` the minority-sign mate. Then `S=epsilon(2 1_gamma-1)`, lambda has magnitude 1, and for nonzero alpha one `+/-1` lies at `s=alpha(gamma+u)`. The opposite extension is zero except for a `+/-2` at the unique nonzero `alpha=Q(u+v)`. This follows from `Shat=2 epsilon chi_alpha(gamma)` and `dhat=-epsilon chi_alpha(u)-2 epsilon chi_alpha(v)`.
* `k=4`: row-zero leaves mate-sign sum 0 or `+/-2`. A nonzero sum makes `S` constant, lambda a graph singleton, and both extensions odd at every nonzero alpha. If the sum is zero then the four mate signs form a signed nonconstant character `chi_a`; `S` is a nonconstant `chi_xi`, and `xi!=a`, since otherwise (2.1) produces a forbidden magnitude 3. At alpha `a` BOTH extensions are graph `+/-2` singletons; at `xi` both graph entries are odd; at the third nonzero alpha they vanish.

Because `d_E=0`, ell0 X has exactly six `+/-2` Z2 sites, no support at physical `b=0`, and no X support on E-row blocks. Each ell0 row has an even number of sites by its zero profile; hence at most three ell0 quotient rows are occupied. For each such row and `s`, Fourier inversion at `b=0` gives

`sum_alpha Z_(0,i)(s,alpha)=0`.  (2.3)

Also, with `z_i=Z_(0,i)(1,0)`, `Z_(0,i)(0,alpha)+Z_(0,i)(1,alpha) == z_i (mod 2)`. If lambda is a singleton, all `z_i` are even and the two extension odd supports agree. Do NOT impose that conclusion for a lambda plane.

The lambda alternatives must be retained literally. In `4` an active row supplies a graph singleton; otherwise graph lambda is zero and the ell0 lambda must be a singleton `+/-2`, since a four-entry plane would require four occupied ell0 rows. In `2+2`, two active rows cannot coexist in one profile; one active row supplies the singleton, and if neither is active the singleton is on ell0. In `3+1` and `2+1+1`, the two odd graph lambda entries force a four-entry plane with two ell0 entries. In particular the `2+1+1` k=2 row is inactive, but may be N or O: N is NOT ruled out by the U0 profiles, as §4 explicitly demonstrates.

A separate **lambda-only** illustration of the ell0 singleton: put ell0 row A values `+2` at `(h,b)=(0,10),(0,11)` and `-2` at `(1,10),(1,11)`; row B values `+2,-2` at `(0,01),(0,10)`; all other ell0 X values zero. Lambda is `+2` at A and zero elsewhere. For a graph `2+2` choose opposite-sign D0 pairs `(00,+),(01,-)` and `S=chi_10` on each of the two k=2 rows; take `S=chi_10` on each k=0 row. All graph lambda entries vanish, and the row-zero equations and physical six-Z2/four-graph-D0 counts hold. This merely shows the allowed singleton alternative at the local/lambda boundary. It is NOT asserted to satisfy the other six profiles, any U3 condition, or a caller. S7 likewise reports only a parent-run local/lambda enumeration, not a full-seven-profile or U3 result.

## 3. Uniform replacement proof of (3.1)

Let `P_i=sum_(b:S_i(b)=-1) b`. The exact seven-profile condition yields a graph-only XOR identity without any odd-offset assumption. Fix nonzero alpha. Since each odd-support set is an affine plane in quotient `(ell,i)`, its intersection with the graph half `ell=1` has 0, 2, or 4 entries; a singleton `+/-2` has no odd entries. Thus the number of odd graph entries in the `(0,alpha)` profile is even.

By the row-zero equation and the fact that the nonzero alpha character is negative on exactly two b sites,

`Z_(1,i)(0,alpha) == 1 + alpha(P_i + sum_(b in D_i)b) (mod 2)`.

Indeed this quotient is `-1/2` times the sum of `S_i+2d_i` over that two-site half; the parity of each nonzero `d_i` is 1. Summing over four graph rows cancels the four constants. For both basis covectors alpha, the even-graph-odd-count condition gives

`sum_i P_i = B_D`.  (3.0)

For an even row `P_i=Q xi_i`: a nonconstant character has two negative sites whose XOR is `Q xi_i`, while a constant character has XOR zero. For an odd row `P_i=gamma_i`, whether its negative set has one or three elements, since the XOR of all four b points is zero. The SAME graph/phase relation gives the graph-Y forms

`G_i(b)=sigma_i (-1)^(b_0 b_1+theta_i(b))`, `theta_i=lambda_i+xi_i` for even rows;
`G_i(b)=sigma_i (-1)^kappa_i(b)`, `kappa_i=lambda_i+(1,1)+Q gamma_i` for odd rows.

In all four named partitions the number of odd rows is 0 or 2, and `sum_i lambda_i=0`. Applying Q to (3.0) therefore proves, for the same actual X and Y,

`sum_even theta_i + sum_odd kappa_i = Q B_D`.  (3.1)

This derivation covers **each** partition, including both singleton and plane lambda columns; it uses only a necessary consequence of each simultaneous profile, not independent selection of profile columns. It does not assert that unequal odd offsets are impossible. More explicitly, with `delta=gamma+u` for odd rows (where `u` is the omitted site for k=3), its four specializations are:

| graph occupancy | consequence of (3.0) |
|---|---|
| `4` | `B_D=0`, hence `sum_i xi_i=0` |
| `3+1` | `xi_C+xi_D=Q(delta_3+delta_1)` for the two k=0 rows |
| `2+2` | `sum_i xi_i=Q(Delta_A+Delta_B)=a_A+a_B` |
| `2+1+1` | `xi_2+xi_0=a_D+Q(delta_1+delta_1')` |

The final two offset terms in the `3+1` and `2+1+1` rows cannot simply be erased. The counterexamples next show this is a factual correction, not only an omitted justification.

### Direct check of the `2+2` N/O subcases

This detail is not needed for the uniform proof but checks F747's local `2+2` discussion, including ell0 lambda `+/-2`. Every graph profile has even odd-support cardinality. If A is active and B is N, the active covector `a_A` and the two k=0 covectors are the three different nonzero values. If A is active and B is O, all of A and the two k=0 rows avoid `xi_B` because B has a singleton in one extension. With `c_B=xi_B+a_B`, the numbers of those three covectors at `a_B,c_B` are respectively even, odd. The possibility `(0,3)` makes ell0 zero at `c_B` in both extensions and at `xi_B` in the singleton extension; ell0 lambda is also zero because A is active. Equation (2.3) then makes ell0 zero at `a_B` in that extension, where graph is already zero, contradicting the profile energy. Thus the counts are `(2,1)` and `a_A+xi_C+xi_D=c_B`.

For inactive N/N, (3.1) gives `xi_C=xi_D`. N/O is impossible because the N row is odd in the O singleton's column. For O/O with unequal `xi_A,xi_B`, each singleton forces the other O row's zero covector there: `a_A=xi_B`, `a_B=xi_A`; both k=0 covectors are the third nonzero one. If `xi_A=xi_B=xi`, the two singletons occur in opposite extensions, both k=0 covectors avoid `xi`, and (3.1) gives `xi_C+xi_D=(xi+a_A)+(xi+a_B)`. These deductions use actual row coefficients; they do not disallow the ell0 lambda singleton when both graph lambda entries vanish.

## 4. Two all-seven-profile counterexamples to F747 §3's intermediate assertions

These are fresh written **U0-level** examples. Each specifies one X, not independent profile columns. They do not assign a common full physical Y or prove J, all U3 caps, V or the original caller; hence they do not refute F747's final exclusion. They do refute the stated claim that the U0 profiles alone force the two odd offsets to agree, and the consequent claim that `2+1+1` N type is impossible. All arithmetic below is displayed for inspection; no program was run.

Use rows `A=00,B=10,C=01,D=11`, `F_A=F_B=F_C=0`, `F_D=1`. In each profile table `A+` means entry `+1` at that row, `A-` means `-1`, and `A(-2)` is a singleton. Entries not listed are zero. The columns headed graph and ell0 are both parts of the **same** profile vector.

### Example I: `3+1`, distinct odd offsets and distinct k=0 covectors

Graph data: A has `S=2 1_10-1` and mate D0 signs `d(10)=+1,d(01)=-1,d(11)=+1`; B has `S=2 1_00-1` and `d(11)=+1`; C has `S=-chi_01` and no D0; D has `S=-chi_11` and no D0. All other mate X values are zero. Ell0 has only these six X sites: A `(0,10,+2),(1,11,-2)`; B `(0,10,-2),(1,10,+2)`; C `(1,10,+2),(1,11,-2)`. Here a triple denotes `(h,b,X)`.

| `(s,alpha)` | graph entries | ell0 entries |
|---|---|---|
| `(1,00)` | A-, B- | A+, B- |
| `(0,10)` | A(-2) | none |
| `(1,10)` | A+, B+ | A-, B+ |
| `(0,01)` | A+, C- | A+, C+ |
| `(1,01)` | B+, C- | B-, C- |
| `(0,11)` | B+, D- | A-, C- |
| `(1,11)` | A-, D+ | B+, C+ |

Each four-entry support is an affine quotient plane and has product `-1`; the singleton has magnitude 2; every row-zero value is zero. The actual k=3 omitted site is `u_A=00` and `gamma_A=10`, so `delta_A=10`; the k=1 site is `u_B=11`, `gamma_B=00`, so `delta_B=11`. The k=0 covectors `01` and `11` differ. Thus both F747 §3 assertions of equality fail even with all seven profiles at once. Here `B_D=11`, and the corrected specialization holds: `01+11=10=Q(10+11)`.

### Example II: `2+1+1` with genuine N type

Graph data: A has `S=2 1_00-1` and sole mate `d(00)=+1`; B has the same S and sole mate `d(01)=+1`; C has `S=chi_10` and the opposite mate pair `d(00)=+1,d(01)=-1`; D has `S=-chi_10` and no D0. Ell0 has only A `(0,10,+2),(1,11,-2)`; B `(0,10,-2),(1,10,+2)`; C `(0,10,-2),(0,11,+2)`.

| `(s,alpha)` | graph entries | ell0 entries |
|---|---|---|
| `(1,00)` | A-, B- | A+, B- |
| `(0,10)` | A+, B+, C+, D- | none |
| `(1,10)` | C+, D+ | A-, B+ |
| `(0,01)` | A+, C+ | A+, C- |
| `(1,01)` | B+, C- | B-, C- |
| `(0,11)` | A+, C+ | A-, C+ |
| `(1,11)` | B+, C- | B+, C+ |

Again every support is an affine plane with product `-1` and row-zero values vanish. At C, `Delta=01`, `a=Q Delta=10=xi_C`, so it is exactly N type. The two odd offsets are `00` and `01`, and `xi_C+xi_D=0=a+Q(00+01)`. These examples have the required four graph D0 and six physical Z2 X sites, no ell0 X at `b=0`, and one common X of energy 56. They verify the literal seven-profile shapes by the displayed tables; they do NOT purport to reconstruct the remaining phase/Y/caller conditions.

## 5. Shared partial-Y parity, E/O forcing and three exclusions

For the SAME Y define

`A_ell(s,alpha,beta)=sum_(h,i,b)Y(ell,h,i,b)(-1)^(s h+alpha(b)+beta(i))`.

Let `n` count negative actual Y signs on the 12 nonzero graph mates. Let `m_alpha` count odd-row graph characters equal to alpha. A bent graph row has Walsh value `2 sigma_i (-1)^((alpha+theta_i)_0(alpha+theta_i)_1)`; an odd character row contributes `0` or a signed 4. The 12 actual mate values contribute signed 2. Counting negative summands modulo 2 gives, for a constant `c` independent of `s,alpha,beta`,

`A_1/4 == n+c+s+m_alpha+alpha(B_D+Q sum_even theta_i) (mod 2)`.  (3.2)

The beta exponent cancels because `sum_even i+sum_i(4-k_i)i=sum_i i=0`. The s exponent is `sum_even F_i+sum_odd(1+F_i)=sum_i F_i=1`; the XOR of the mate b sites is `B_D`. The even number of bent rows cancels the common `alpha_0 alpha_1` term, leaving `alpha(Q sum_even theta_i)`. This derivation depends on the actual shared phase and all actual mates, not frequencywise independent signs.

Set `v=B_D+Q sum_even theta_i`. From (3.1), `sum_odd kappa_i=Qv`. With no odd rows, `v=0`. With two, either their kappa coincide and again `v=0`, or they differ by `Qv`; the two are exactly a level set of `alpha(v)`, because `(Qv)(v)=0`. Hence `m_alpha+alpha(v)` is constant in alpha, including coincident characters. There is one slice `s_*` on which every `A_1/4` is even and the opposite slice on which every `A_1/4` is odd.

By S4/S5, the general g and `J=1` give every full Y coefficient `4 mod 8`. Parseval from `sum Y^2=128` and cap 12 gives exactly eight magnitude-4 coefficients and 56 magnitude-12 coefficients. The two full coefficients paired by the ell frequency are `A_0+A_1` and `A_0-A_1`; both partials are multiples of 4, with opposite quotient parities, and the two caps are equivalent to `|A_0|+|A_1|<=12`.

At `s_*`, let E be the number of the 16 `(alpha,beta)` with `|A_1|=8` (all other values there are 0). At `s_*+1`, let O count `|A_1|=4` (the rest have magnitude 12). Each E or O position consumes at least one distinct small full coefficient, so `E+O<=8`. The ell1 spatial energy is `16+12*4=64`; 5-bit Parseval gives `O=2+E/2`. If `e_i(b)` is the actual mate-Y sign at a non-D0 site, put `C=sum_mates G_i(b)e_i(b)`. Parseval at the first slice gives

`E=16+(-1)^s_* C >= 4`, since `|C|<=12`.

Consequently `E=O=4`, and equality forces at **each of the 12 individual mate sites** `e_i(b)=-(-1)^s_* G_i(b)`. At an O position the remaining cap and exhaustion of all eight small coefficients force `|A_0|=8` (if `A_0=0` it would use two small coefficients). At the other slice the SAME graph row becomes

`(-1)^((s_*+1)F_i) G_i(b)[3-2 1_(b in D_i)]`.  (4.2)

For any three distinct `i in F_2^2`, a single beta, with an overall sign, aligns any prescribed three nonzero real signs: every sign assignment on three points extends to an affine character. Thus the following are genuine single physical frequencies:

* `4`: the k=4 row contributes magnitude 2 and the other three bent rows each 6. Align the three 6s to get `|A_1|>=18-2=16`, contradiction.
* `3+1`: at the k=1 character, that row contributes 10, each k=0 bent row contributes 6, and the k=3 character row contributes at most 6. Align the 10,6,6 to obtain `|A_1|>=16`.
* `2+1+1`: a k=2 bent row contributes magnitude 2 or 6. Indeed the two deleted signed graph summands are equal or opposite; a bent row's four signs have product -1, yielding those two cases. If the two k=1 characters differ, take alpha equal to one, giving row magnitudes 10 and 2; align the 10, the k=0 row's 6 and the k=2 row's at least 2, then subtract 2: at least 16. If they coincide, align 10,10,6 and subtract the k=2 row's at most 6: at least 20.

All contradict `|A_1|<=12`. The arguments have arbitrary actual row signs, all admissible F/phase data and every placement within these partitions. They are implications under the specified full common-object imports, not existence assertions.

## 6. Disposition, remaining work and evidence

F747 §2's local formulas and N/O classification are reconstructed above. F747 §3's two U0-only odd-offset/k=0-equality and N-impossibility assertions are false by the two simultaneous-profile examples; the uniform graph-odd-support proof repairs the target identity without them. F747 §3's `2+2` parity conclusion and §4's residue/equality forcing are reconstructed at the stated imports, as are §5's three exclusions. This is a fresh written candidate/check, not adoption. F747 §6 was present in the complete packet but its `2+2` exclusion was not independently checked here. The remaining all-graph implication therefore requires a separate full §6 check or alternative proof; all general `d_E>0` cases and the physical U3/V/original-caller frontier remain open. No stronger target, novelty, independent-model-family, human, kernel/formal, or original-source identity claim is made.

**Coverage and pins.** After actual dispatch and direct PREBODY ACK to Main, the sole literal packet was displayed serially in exact RAW windows of at most 20 LF, in order through LF 728 and its ending, before research/comparison. The 22 distinct listed prebody controls, actual dispatch, manifest, freeze receipt, final binding and parent-live metadata were read through endings before ACK; their metadata and the packet hash/byte/LF observations matched the supplied bindings. The following S1–S7 full source bodies were read as literal packet blocks, not by following source links; source path hashes below are the parent-supplied complete-body pins, not separate live source rehashes. All paths use `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/` as prefix.

| source | complete path after prefix | LF | SHA-256 |
|---|---|---:|---|
| S1 | `parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json` | 11 | `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c` |
| S2 | `review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/parent-omitted-ell0-lambda-singleton-proof-gap-major-v1.md` | 7 | `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca` |
| S3 | `review-waves/f747-boolean-general-d0-occupancy-profile-frontier-author/author-candidate-v1.md` | 143 | `27fcb901518fdf2208f55553d647f5ef5d17960fc0c606f3f6fe3a02d33b7f85` |
| S4 | `dispositions/info-6-entire-four-distinct-d0-rank2-same-object-obstruction-parent-v1.md` | 31 | `ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928` |
| S5 | `parent-recovered-local-H-definition-and-general-g-foundation-v1.md` | 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |
| S6 | `dispositions/info-6-actual-rank2-seven-profile-and-four-distinct-d0-cross-fibre-parent-v1.md` | 37 | `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a` |
| S7 | `review-waves/f749-boolean-d0-occupancy-local-profile-exact-finite-author/parent-d0-occupancy-local-profile-v2-run-v1-receipt.json` | 456 | `44fc6d7c1f177a22eba29d295889220761f540a427bb84a7b7f9d9912cc52bf9` |

Wave metadata independently hashed: manifest `49bc81ebf741fad3e5f000a5d88119ab1062a56bc08afbcd6688e87c683f0b5f`; freeze `332b0b8311b003003763cd1bf5c99101eaa28599213802a45172a2eee995ce6f`; final binding `f61dc822149d94f5d5221c8822b6275d62d8f771dd6ae81574cb33bbc678e049`; metadata `b55d51c7e9cf091d55713d01e3afccb3cd8d5ac405d0791f64e165ab3b80f795`; actual dispatch `97724c1bc86221561946f710798248210a584fd50985b41031803f3aa0891cab`; packet `b00c3a145d4337ee744046eb921e7ad1d91be878130f9eb238ea748340b2f95d` (69,561 bytes, 728 LF). S7's described parent run is not a child run or a proof that all seven profiles hold. All genuine held episodes AND ALL proof/method/selection/planning/verification/reporting/confidence/downstream consumers were NONINPUT; status controls only were read. No held history, unspecified sibling, old code, or outgoing source link was read. **CHILD SCIENTIFIC EXECUTION NOT RUN**: no test, compiler, solver, CAS, finite checker, source execution, build, lint, formatter, external model or paid job. No finite source or parent GO is proposed here. Written identities and displayed example checks are not computational, human or independent-family verification. Any subsequent correction must be additive, with a fresh path and no backdating.
