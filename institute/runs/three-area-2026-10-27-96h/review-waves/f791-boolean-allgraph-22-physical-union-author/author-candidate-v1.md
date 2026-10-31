# F791: actual 2200 physical obstruction and conditional all-graph union

**Status: NONBLIND GENERAL-AUTHOR WRITTEN CANDIDATE, NOT ADOPTED.** I reconstruct the complete 2200 argument below, including its actual partial-Y inversion and physical site forcing. I find no mathematical counterexample or gap in that reconstruction at the stated imports. This is not an independent-family or constrained-WRITTEN review, and it is not parent acceptance, a human or kernel verification, a global witness, or a novelty result. The other four all-graph occupancy exclusions remain the *named imports* quantified in §8; in particular the 4000/3100/2110 candidates are not promoted here into previously adopted theorems. The d_E=2-only statement is a conditional union of those imports and the 2200 candidate, not an unconditional new disposition.

Native UTC clock observed before creation: `2026-10-31T01:23:22Z`. This is a pre-creation observation, not a purported creation timestamp.

## 1. Explicit common-object hypotheses and conclusion

Fix **one** actual normalized rank-two five-span m116 object with its same physical f, R, a, general g, ternary u, x=U0 and y=U3, its graph/phase and physical inverse, and local `H_loc=0`. Here `H_loc` counts U1-zero blocks with a single |U0|=4 peak; it is not the radical plane. Import the actual normalization, graph, local-type/count, profile and phase interfaces at their stated scope in S9–S12, not converses to the original caller. Require the *specified* original-DC transport t, xhat(t)=0, all 64 U0 coefficients divisible by 8 and of magnitude at most 8, J=1 and all 64 U3 coefficients of magnitude at most 12. The actual counts are D0=4, D3=18, Z2=6, Z4=1, Z0=17, with sum x²=56 and sum y²=128. The general-g bridge gives every full y coefficient congruent to 4 mod 8. All these conditions and the assumptions below refer to the **same** physical object; there is no replacement by free, separately chosen spectra or profiles.

Let `I=B=F_2²`, write `chi_alpha(b)=(-1)^(alpha·b)`, and let `Q(b0,b1)=(b1,b0)`. Coordinates are `(ell,h,i,b)` with ell,h in F_2 and i,b in F_2². The graph has ell=1 and h=F_i, with sum_i F_i=1; the actual physical mate changes h and keeps **the same b**. Put X(c)=(-1)^(t·c)x(c), Y(c)=(-1)^(t·c)y(c). This common modulation translates the two spectra together and does not change a, g, t, or the physical mate.

For the theorem in §§2–7 impose d_E=0 and graph occupancy 2200: distinct graph rows A,B each have two D0 mates D_A,D_B, and graph rows C,D have none. On graph row i, `S_i(b)=X(1,F_i,i,b)` and `G_i(b)=Y(1,F_i,i,b)` are signs. At the four D0 mates, X=±2 and Y=0; at the other twelve graph mates, X=0 and Y=2e_i(b), e_i(b)=±1. On ell=0,b=0, X is zero, the two actual F sites have Y=0 and the six E sites have Y=±2. On ell=0,b≠0, exactly six Z2 sites have X,Y=±2, one distinct Z4 site has X=0,Y=±4, and all remaining sites are Z0. Thus the ell=1 Y energy is 16+12·4=64.

For each quotient point `(ell,i)` and `(s,alpha) in F_2 x F_2²`, use the **same-X** profiles

`Z_(ell,i)(s,alpha) = (1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha·b)`.

The zero column Z(0,0) vanishes at all eight quotient points. Each other column is either one ±2 or four ±1 on a single affine two-flat in `(ell,i)`, with sign product -1. In particular its number of odd entries on ell=1 is even. These are necessary simultaneous conditions on X, not seven independently selected columns. The graph phase relation is `Y=-agX`; for the even rows of 2200 it yields

`S_i=epsilon_i chi_xi_i`, `G_i(b)=sigma_i(-1)^(b0 b1+theta_i·b)`, `theta_i=lambda_i+xi_i`, `sum_i lambda_i=0`.

All signs and covectors are the actual ones. The four graph Y signs have product -1 on each row. **Claim, subject to separate scrutiny of these inputs and the written proof:** no such common object exists in the 2200 case. It is an implication from necessary actual-object hypotheses, not an existence or original-caller equivalence claim.

## 2. Same-X graph parity and the common actual-Y slice

Put `d_i(b)=X(1,1+F_i,i,b)/2`; it is a sign on D_i and zero elsewhere, and set `B_D=sum_i sum_(b in D_i) b`. The zero profile says

`sum_b S_i(b)+2 sum_b d_i(b)=0`,

`Z_(1,i)(s,alpha)=(-1)^(s F_i)[Shat_i(alpha)+2(-1)^s dhat_i(alpha)]/4`.

For k_i=|D_i| even, the first equation says the number of negative graph signs is even, so S_i is indeed a signed character, including a constant. Let M_i be the XOR of the negative-S locations. For nonzero alpha, the zero-row equation gives

`Z_(1,i)(0,alpha) = -(1/2) sum_(b:alpha·b=1) (S_i(b)+2d_i(b))`
`                  ≡ 1+alpha·(M_i+sum_(b in D_i)b) (mod 2)`.

The number of odd graph entries in this column is even, so the four congruences imply `sum_i M_i=B_D`. For a signed character, M_i=Q xi_i, also when xi_i=0. Consequently

`sum_i xi_i=Q B_D` and `sum_i theta_i=Q B_D`.                 (1)

This proof does not use F747's false odd-offset equality, its false N-type exclusion, or a choice between a lambda singleton and plane.

Define partial Fourier transforms of the *actual Y*, using unnormalized sums:

`A_ell(s,alpha,beta)=sum_(h,i,b)Y(ell,h,i,b)(-1)^(s h+alpha·b+beta·i)`.

The two full coefficients at a fixed `(s,alpha,beta)` are A0+A1 and A0-A1, and their common cap is equivalent to `|A0|+|A1|≤12`. Each graph-row b transform is `2 sigma_i(-1)^q(alpha+theta_i)` with q(z)=z0 z1. Thus A1 is twice the sum of sixteen signs: four graph-row Walsh signs and twelve actual mate signs. Its quotient A1/4 is integral; its parity is the negative-sign parity of those sixteen signs. In their product the beta exponent is `sum_i(5-k_i)i=sum_i i=0`, the s exponent is `sum_i F_i=1`, and the alpha exponent is `alpha·(B_D+Q sum_i theta_i)=0` by (1). Four copies of q(alpha) also cancel. Therefore one **common** s=s_* has every A1/4 even, and s'=s_*+1 has every A1/4 odd, simultaneously for all 16 alpha,beta, including alpha=0.

By residue and cap each full coefficient has magnitude 4 or 12; Parseval, `sum Y²=128`, gives exactly eight magnitude-4 coefficients. Let E count positions on s_* with |A1|=8, and O count positions on s' with |A1|=4. The other positions on the respective slices have A1=0 and |A1|=12. Each E or O position consumes at least one distinct magnitude-4 full coefficient, hence E+O≤8. Five-bit Parseval for ell=1 gives

`64E+16O+144(16-O)=32·64`, so `O=2+E/2`.              (2)

Let `C=sum_(12 actual D3 mates) G_i(b)e_i(b)`. Four-bit Parseval on the s_* h-combination gives

`64E=16[64+4(-1)^s_* C]`, hence `E=16+(-1)^s_*C≥4`.    (3)

Equations (2)–(3) force E=O=4 and equality in |C|≤12. Therefore **at every one of the twelve physical sites**, not merely after a Fourier choice,

`e_i(b)=-(-1)^s_*G_i(b)`.                                  (4)

Each E position uses exactly one small full coefficient. At an O position A0 is 0 or ±8: A0=0 would use two small coefficients. Since E+O=8 already exhausts all eight, `|A0|=8` at every O position. At all |A1|=12 positions the cap forces A0=0. At s' the actual contribution of row i is

`R_i(alpha)=(-1)^(s'F_i) sum_b G_i(b)chi_alpha(b)[3-2 1_(b in D_i)]`,
`A1(s',alpha,beta)=sum_i chi_beta(i) R_i(alpha)`.             (5)

Any prescribed signs on three distinct rows can be aligned by one beta up to an overall sign, since three distinct points of F_2² are affinely independent. This is one physical frequency, not three separately chosen frequencies.

## 3. Both pair products, alpha=0, and inversion of one physical B

For i=A,B write D_i={u_i,v_i}, `Delta_i=u_i+v_i≠0`, and `P_i=G_i(u_i)G_i(v_i)`. The four signs `G_i(b)chi_alpha(b)` have product -1 and sum ±2. If the two signs deleted by the coefficient in (5) agree, the other two are opposite and the modified sum has magnitude 2; if the deleted signs disagree, it has magnitude 6. In either case its sign is the sign of the original bent Walsh sum. Thus

`|R_i(alpha)|=2 iff P_i chi_alpha(Delta_i)=+1`; otherwise it is 6.    (6)

The C,D row magnitudes are always 6. If the A,B predicates differed at any alpha, a single beta aligns the three sixes and leaves magnitude at least 18-2=16, contradicting the cap. Hence the predicates agree **at all four alpha**. At alpha=0 they imply `P_A=P_B=P`; then the nondegenerate characters imply `Delta_A=Delta_B=Delta≠0`. Put `a=Q Delta`. The two alpha with magnitude pattern `(2,2,6,6)` are exactly

`L_P={alpha:chi_alpha(Delta)=P}={gamma,gamma+a}`.             (7)

For P=+1 this is `{0,a}`, explicitly including alpha=0; for P=-1 it is the other two nonzero alpha. No b-translation, P sign, or selected covector is assumed.

At s', A1/4 is odd. The sum of the positive row magnitudes divided by four is even for either `(2,2,6,6)` or `(6,6,6,6)`; flipping any row sign changes that parity. Hence the product of the four row signs is -1. Beta characters preserve the product and run, modulo a common overall sign, through all four odd-product sign patterns. Consequently the four absolute A1 values are `4,4,12,12` for every alpha in L_P, and `12,12,12,12` for every other alpha. In conjunction with §2, A0(s',alpha,beta) is therefore ±8 at exactly two beta for each alpha in L_P, and is zero everywhere else.

Now define the **single actual spatial array**

`B_i(b)=Y(0,0,i,b)+(-1)^s'Y(0,1,i,b)`.

For fixed alpha, beta inversion of its actual transform A0 says `Bhat_i(alpha)=(1/4)sum_beta A0(s',alpha,beta)chi_beta(i)`. The two distinct nonzero beta terms ±8 give Bhat values 0 or ±4, with exactly two nonzero i. At the two selected covectors, b inversion at 0 gives

`|B_i(0)|=|Bhat_i(gamma)+Bhat_i(gamma+a)|/4≤2`.

Physical F/E locations instead force each B_i(0) to be 0 or ±4 (and it is 0 in the F row), so it is 0. Thus the two Bhat vectors are negatives and have the same two nonzero rows, say U,V. Full b inversion gives, for **every** i and b,

`B_i(b)=Bhat_i(gamma) chi_gamma(b)[1-chi_a(b)]/4`.          (8)

This formula remains valid when gamma=0. Since ker(a)={0,Delta}, let p be either point outside that kernel and q=p+Delta. For each i=U,V, (8) says B_i(0)=B_i(Delta)=0, `|B_i(p)|=|B_i(q)|=2` and `B_i(q)=P B_i(p)`; all other rows vanish. This is an inversion of the common actual Y, not a free choice of Bhat columns.

## 4. Z4/Z2 placement follows from the physical inverse

There are exactly four `(i,b)` h-pairs with nonzero B: U,V crossed with p,q. At all other pairs B is zero. The unique Z4 cannot be in a zero-B pair, since its sole opposite-h partner is at most Z2 and cannot cancel magnitude 4. Nor is Z4 at b=0, which consists of the actual F/E blocks. Therefore it occupies one of the four support pairs and its opposite-h partner is a Z2 with the weighted opposite sign, leaving magnitude 2. In each of the other three support pairs there is **exactly one** Z2: zero would give B=0, while two give magnitude 0 or 4. Thus four of the six Z2 sites are already used.

The remaining two cannot occupy free slots in the support pairs, because doing so changes magnitude 2 to 0 or 4, and the Z4 pair is already full. A lone Z2 at a zero-B pair cannot cancel. The remaining two must therefore be the two opposite-h sites in **one** further `(i,b)` pair, with their weighted Y values cancelling; this b is not 0. These are deductions from actual physical site magnitudes, not an assumed three-cell or B-support fixture.

Each ell0 quotient row has an even number of Z2 sites because its zero-profile X sum is zero, and six Z2 sites occupy at most three ell0 rows. The lambda profile means Z(1,0), not the phase covectors lambda_i. A k=2 graph row with equal D0 signs contributes ±2 there (active); two active rows exceed the profile energy 4. If one is active the profile is that graph singleton. If neither is active, all graph entries vanish, and an ell0 four-point plane would require four occupied ell0 rows. Hence the profile is a **singleton** in either alternative, and every lambda-profile entry is 0 or ±2.

If the extra cancelling Z2 pair lay outside U,V, its row would contain exactly two X sites at opposite h. Its zero row sum makes their X signs opposite, giving a lambda-profile entry of magnitude 1, impossible. Thus it belongs to U or V; relabel it U. Its b must be Delta because b=0 and p,q are already occupied as above. V has just two Z2 sites, one over p and one over q, with opposite X signs. If their h values differed, V's lambda entry would have magnitude 1; hence both are in a common h=h_V.

U has Z2 sites over `(0,Delta),(1,Delta)` and one each over p,q. Since the U zero row and its allowed lambda values imply an even signed X sum in each h cell, the p,q sites have opposite h. Interchange p and q if needed and denote the four X values at `(0,Delta),(1,Delta),(0,p),(1,q)` by `2r,2t,2z,2w`, with r,t,z,w signs. Zero row and singleton lambda give

`r+t+z+w=0`, `lambda_U=r+z in {0,±2}`.

All possibilities are: if lambda_U=0, `z=-r,w=-t`; if lambda_U=±2, `z=r,t=w=-r`. For either nonzero alpha≠a, chi_alpha(Delta)=-1 and chi_alpha(q)=-chi_alpha(p). Substitution shows both `Z_(0,U)(0,alpha)` and `Z_(0,U)(1,alpha)` are ±1, and their extension ratio flips between the two such alpha. At alpha=a, if lambda_U=0 exactly one extension is ±2 and the other zero; if lambda_U=±2 both are zero. For V, its opposite X signs and common h give two ±1 entries for each alpha≠0,a, with extension ratio `(-1)^h_V` independent of alpha; at alpha=a its entries are zero. These statements retain both singleton locations until they are actually eliminated below.

## 5. Complete active/N/O elimination and same-flat sign contradiction

For each A/B pair let `xi_i` be its actual graph-X character covector. The possible row types, directly from the row-zero equation and its displayed transform, are:

* **active:** equal D0 X signs, xi_i=0, graph lambda entry ±2; at alpha=a it is odd in both extensions;
* **N:** opposite D0 X signs and xi_i=a; at every nonzero alpha it is odd in both extensions. For alpha≠0,a the extension ratio is the constant `(-1)^(F_i+1)`;
* **O:** opposite D0 X signs and xi_i≠a; at alpha=xi_i≠a one extension is a ±2 graph singleton, at alpha=a both are zero, and at the remaining nonzero alpha both extensions are odd.

These are exhaustive, including all signs and coincidences. An O row is impossible: its singleton at xi_i meets the physical U row, which is odd in both extensions there. Two active rows were already ruled out by lambda energy. If exactly one is active, the other must be N. The graph singleton forces lambda_U=0; at alpha=a, U has a ±2 singleton in one extension, while both the active and N graph rows are odd in **both** extensions. This is impossible. Consequently both A and B are N; graph lambda vanishes, V's lambda vanishes, and the E-side singleton is at U, with lambda_U=±2.

For every nonzero alpha, A and B already contribute two odd graph entries in each extension. Even graph-odd-support parity forces the nonzero character covectors of C and D to occur with even multiplicity, so they are equal; call the common value eta. If eta≠a, at alpha=eta all four graph rows and both U,V rows are odd in each extension, exceeding the four entries available to a profile. Thus eta=a.

For each of the two nonzero alpha≠a and each of its two extensions, the four odd entries are exactly at `(1,A),(1,B),(0,U),(0,V)`, each ±1. If these points do not form one affine flat, the profile condition already fails. If they do, each of the four relevant profile sign products must equal -1. The ratio of its s=1 product to its s=0 product is the product of the four extension ratios. The two N ratios are the constants `(-1)^(F_A+1)` and `(-1)^(F_B+1)`; the V ratio is `(-1)^h_V`; the U ratio flips between the two alpha. Hence the two product ratios are opposite, whereas each must be (-1)/(-1)=+1. Contradiction. This completes the 2200 written implication at §1's full common-object hypotheses, for both signs P and both lambda-singleton placements.

## 6. What the earlier finite records actually say

S7 is the actual F766 v2 receipt: process exit 0 but overall JSON status **PARTIAL_COOPERATIVE_DEADLINE**. Its same-X 4000, 3100 and 2200 stages completed at their stated scope; 2110 did not (361,394 of 774,144 canonical graph tuples finished). Its complete derived-22 stage was explicitly conditional on an already supplied fixture and did not derive the B support, the physical forcing, a common all-capped Y or an original caller. Partial 2110 observations must not be extrapolated into a complete census or a global PASS.

S8 is the F781 receipt, COMPLETE_FINITE_LOCAL_SCOPES_ONLY: the three literal X countermodels, one-row patterns, affine-flat parity and the **conditional** 22 B-support physical-site checks have their recorded local scopes. F781 assumes the B support for its 22 stage; it does not derive that support from common U3, construct f/R or a common all-capped Y, finish a global 2110 census, or establish this union. Its packet-display recovery is separately recorded as one PROCESS MINOR. These are parent-run receipt reports, not new runs by this author, and are not substituted for §§2–5.

S2 retains **one F747 author MATH MAJOR** for its two false U0-level intermediate assertions: equal odd offsets/3100 k0 covectors and the resulting exclusion of N type in 2110. Their falsity does not by itself refute the final all-graph assertion. Neither false inference enters the proof here or any allowed union import.

## 7. Imports and exact frontier of the proposed union

The following are separately quantified hypotheses/results, **not proved or newly adopted by §§2–5**:

1. **Odd-E parity, S10:** for every actual normalized same-X object at its named count, transported-balance and seven-profile imports, `d_E` is even. Directly, ell0 has 6+d_E X sites of magnitude 2, each quotient row has signed sum zero, and each row therefore has an even number of sites. This is an adopted necessary parity result at its own scope, without a U3 cap requirement.
2. **Four-E exclusion, S11:** for every same actual normalized object at the full listed f/R/g, H_loc, physical inverse/counts, specified t, seven profiles, J=1, residue and all common-Y U3-cap imports, d_E=4 is impossible. Its disposition explicitly covers both ell0 lambda singleton and four-entry plane. It remains an imported adopted conditional obstruction, not a result of the arithmetic census alone.
3. **4000, 3100, 2110 exclusions, S3/S5 (also S4):** for *every* same actual d_E=0 object with respectively these graph-mate occupancy multisets and the full §1 physical/same-X/phase/J=1/common-Y residue and all-cap hypotheses, no object exists. S5 is a nonblind written author reconstruction, **not an adopted theorem**. Its 2110 claim explicitly includes both N and O; its reasoning uses the repaired parity and the same actual Y, not either F747 false inference. F766's partial receipt is not a substitute. These are three separately named candidate imports here.
4. **1111 exclusion, S9:** for every same actual object at its named normalization, graph/phase, physical counts, H_loc, specified t, all-U0 and same-X profile, J=1 and all common-Y U3-cap imports, one D0 in each graph row is impossible. This is the separately adopted conditional four-distinct theorem, including its actual location/physical bridge; it is not inferred from an arbitrary free signed array. It is an import, not newly reproved here.

The branch interfaces in these statements refer to the same t, physical mate, actual f/R/a/g/x/y and the same cap/residue, rather than changing witnesses between branches. In particular the S9 location theorem remains an actual-interface import; the 2200 proof does not silently assume it. Subject to these precisely stated imports and independent scrutiny of §§2–5, the five and only five partitions of four graph mates are 4000, 3100, 2200, 2110 and 1111; each is excluded when d_E=0. S10 removes d_E=1,3 and S11 removes d_E=4. Thus the proposed logical consequence is **d_E=2**. This is a necessary condition, not a constructed object or proof of feasibility.

At d_E=2, `sum_i k_i=2`: graph allocations are `2` in one row or `1+1` in two rows. The two E-row D0 sites are either both h sites in one E row or one site in each of two distinct E rows. The four cross-combinations remain, subject to all actual same-X/phase/Y/physical constraints. The d_E=2 graph-2 lambda alternatives include graph singleton, E singleton and four-entry E plane; graph-1+1 has two graph and two E odd entries on the same admissible flat. No lambda alternative is assumed realizable merely by this list.

**Unresolved:** independent checking and parent disposition of the written 2200 proof and the unadopted three-shape imports; the complete d_E=2 actual common-Y frontier; the original selected-T/rank/atom/caller interfaces, V signs, any global rank-two/five-span exclusion or NL242 claim, and novelty. Parent adoption of one scoped import does not automatically adopt this composition. Neither the conditional union nor either finite receipt establishes an all-capped witness.

## 8. Coverage, bindings, and process facts

After Main's direct confirmation of the **actual dispatch receipt**, I read that receipt, the entire manifest, freeze receipt, final pre-dispatch binding, prepared metadata and all **23** manifest-listed status/permission controls through their endings, then sent Main a direct PREBODY ACK naming 23 controls and ordered part lengths 596 and 1062 LF. Only after ACK I read packet part 01 LF 1–596 followed by part 02 LF 1–1062, serially in contiguous RAW windows of at most 20 LF, through both endings, before mathematical comparison or work. Total packet coverage: **1,658 LF**. No packet-line truncation was observed.

Presentation disclosure: the initial administrative manifest display summarized/elided nested blocks; before ACK I recovered the entire manifest verbatim in RAW LF 1–300 and 301–324. I omitted this administrative recovery from the ACK and reported it directly to Main after recognizing the omission. This is an observed presentation/notice fact, not a claim of mathematical falsity or a retroactive clean first display. No packet body was read before ACK; the subsequent packet sequence above was not interrupted by this recovery.

The 23 controls, in manifest order, were: prospective method restoration (15 LF), owner addendum 2 (14), L1 quarantine (23), privacy auxiliary quarantine (11), core-gram auxiliary quarantine (9), AME compression quarantine (8), held-PH reporting quarantine (49), f439 (23), f444 (16), f448 (20), f508 (22), f513 (22), f586 (23), f602 (23), f596 (24), f653 (11), f654 (11), f659 (11), f660 (11), f662 (11), E-row omission (11), f746/f749 pre-run corrections (28), and f781 display recovery (5). Their complete paths, per-control hashes and bindings are in the frozen manifest and prepared metadata below. These controls were used for **status and permissions only**. All genuine held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. No outgoing source, old code, held history, unspecified sibling result or source link was read. This is not a private-cognition certificate.

The following whole-file administrative SHA-256 observations were made **after** packet reading; for these seven own-wave artifacts only, I independently ran metadata hashing. They are not scientific verification:

| artifact | SHA-256 |
|---|---|
| actual dispatch receipt | `6a11bb2f03c3629026101852b9e015979e4091b92b15ceaf6ae444d2f9a0773d` |
| manifest | `34d73ba9b5b9b3cf69b41784bea8b631d18e15781dfecf3607bee5f3dea82a2f` |
| freeze receipt | `245b7a673a94fd4af444f8585f0d74c6fe7725e4aefb37cc2cec1decbc8c2746` |
| final pre-dispatch binding | `607747c712c2c47fe039f82dfe47483a1c25f56868e0ea4689d848b47a2d606a` |
| prepared metadata | `1a371b947abb18d935a066d7100d69e0448bb48d1a24749aa05b63f9440c0b04` |
| packet part 01, 596 LF, 86,717 bytes | `1384590763eeeb2fb55a3e048a034dd91640f8007214e358cb539dac452b1004` |
| packet part 02, 1062 LF, 87,205 bytes | `f4b3ffe9ff2d6f2d992850331b6e539fa0554a9dda49eb77f67896b1a36f4888` |

The freeze receipt reports complete-body roundtrip and persisted packet equality; the final pre-dispatch binding reports all expected/live pins matching. Those are parent administrative reports, not independently rerendered source identities. The twelve complete source blocks were read only in the packet; their following whole-source SHA-256s and paths are **parent-supplied pins**, not separately opened or live-rehashed source files. Prefix P is `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`.

| ID | complete source after P | LF | parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `parent-boolean-all-graph-D0-and-two-E-only-union-candidate-v1.md` | 13 | `904612998ea53b43690af8c20716c473f7b8b4d95b4eb55e135d5eb295719819` |
| S2 | `review-waves/f747-boolean-general-d0-occupancy-profile-frontier-author/parent-false-offset-and-N-type-profile-inferences-math-major-v1.md` | 9 | `bfd61d0b27a29c43ad9757b6eb62300fec62b4953b2aca106f74c3836a3e6424` |
| S3 | `review-waves/f764-boolean-all-graph-D0-common-parity-proof-author/author-candidate-v1.md` | 166 | `5af6d01a1d5d3820ddc086b596ce6064390d1e30acdd9c1396465b76fee2864d` |
| S4 | `review-waves/f765-boolean-22-physical-Z2-and-allgraph-proof-author/author-candidate-v1.md` | 195 | `c54f235a86907ac14f769d504f0c589bfdc458155da6c6191d32a80b265a7779` |
| S5 | `review-waves/f779-boolean-graph-D0-repaired-parity-and-three-shapes-author/author-candidate-v1.md` | 191 | `a53943119e135540456f8e464422a5ca418f698239650d05b5c912b7b2f840c5` |
| S6 | `review-waves/f780-boolean-graph-D0-22-physical-forcing-author/author-candidate-v1.md` | 159 | `244c790c8735125287ede9cebb7a9144847bf685dc63dc371300f81746d1bb4b` |
| S7 | `review-waves/f766-boolean-allgraph-D0-profile-parity-exact-finite-author/parent-allgraph-profile-parity-v2-run-v1-receipt.json` | 582 | `f48e7d2eb424d900198cbea89d12155c7974c5bceb3606ce63fda2151db224b6` |
| S8 | `review-waves/f781-boolean-repaired-graph-D0-exact-local-countermodel-author/parent-repaired-local-v1-run-v1-receipt.json` | 164 | `a85083add99f01d9815a9651cfa66db0d4bd16806f6e62758f72acf7fd03c42c` |
| S9 | `dispositions/info-6-entire-four-distinct-d0-rank2-same-object-obstruction-parent-v1.md` | 31 | `ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928` |
| S10 | `dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md` | 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S11 | `dispositions/info-6-entire-four-E-row-d0-actual-common-y-obstruction-parent-v1.md` | 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S12 | `parent-recovered-local-H-definition-and-general-g-foundation-v1.md` | 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |

**CHILD SCIENTIFIC EXECUTION NOT RUN:** no scientific program, finite source, old source, solver, CAS, test, build, compiler, formatter, external-model CLI, installation or paid/heavy action was run. This author result is a nonblind written reconstruction, not a disjoint check, independent-family/human/kernel review or parent acceptance. No source or prior finding was overwritten. Any later repair must be an additive new artifact, with no backdating.
