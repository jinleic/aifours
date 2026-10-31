# F779: common graph parity and three occupancy contradictions

**NONBLIND GENERAL-AUTHOR WRITTEN RECONSTRUCTION; NOT ADOPTED.** Native clock observed before this exclusive creation: 2026-10-30T18:11:57-0700 PDT. Under the exact common-object hypotheses in §1, I reconstruct the replacement graph parity (3.0)/(3.1), the common partial-Y residue for every frequency, the E/O equality forcing, and the contradictions for graph occupancies 4000, 3100 and 2110. I also give two completely specified same-X seven-profile countermodels to the false U0 intermediates. The 2200 obstruction is **not checked or accepted here**. Nothing here automatically proves d_E≥1, the full all-graph claim, a full-caller counterexample, or V/NL242.

## 1. Exact interface and notation

Work with ONE actual normalized rank-two five-span object at the supplied S5–S8 imports: the same physical f,R,a,g,u,x=U0,y=U3, graph/phase, local H_loc=0, and the *given* original-DC transport t. Require D0=4, D3=18, Z2=6, Z4=1, Z0=17, x-energy 56, y-energy 128, every U0 coefficient divisible by 8 and at most 8 in magnitude, the particular carried balance xhat(t)=0, J=1, and every U3 coefficient at most 12. The common transported arrays X(c)=(-1)^(t·c)x(c), Y(c)=(-1)^(t·c)y(c) translate both spectra by the same t; this is not permission to select a new zero or alter a or g. The general-g residue gives every full Y coefficient congruent to 4 mod 8. The same-X seven profiles and the graph/phase structure below are imported at their actual necessary boundaries, not as independent per-frequency choices or a converse to an original caller.

Let I=B=F₂², with standard dot product, χ_α(b)=(-1)^(α·b), and Q(b₀,b₁)=(b₁,b₀). Label coordinates (ell,h,i,b). The graph has ell=1, h=F_i, with Σ_i F_i=1; its physical mate has h=1+F_i and **the same b**. The graph phase has row-linear covectors λ_i with Σ_i λ_i=0. On the graph Y=-agX. Write S_i(b)=X(1,F_i,i,b)∈{±1}; D_i is the set of actual D0 mates, k_i=|D_i|; d_i(b)=X(1,1+F_i,i,b)/2 is ±1 on D_i and zero otherwise. All sums of bit vectors/covectors are XORs. Set B_D=Σ_i Σ_(b∈D_i)b.

**Throughout the new proof impose d_E=0:** all four D0 are graph mates, Σk_i=4; the six E-row blocks are D3. The ell=1 Y array has 16 graph signs, 12 actual nonzero mate values 2e_i(b), and four D0-mate zeros. Thus its spatial energy is 16+12·4=64. The six Z2 X sites lie at ell=0,b≠0, and all ell=0,b=0 X values vanish. The five partitions of four graph mates are 4000,3100,2200,2110,1111. The separately adopted 1111 theorem S5 is only an import at its own full physical/Y hypotheses. No conclusion for 2200 is taken from S3 §6. In the unrestricted problem Σk_i=4-d_E, and S6's separately adopted even-d_E result leaves d_E=0,2,4 at its exact assumptions; this proof does not exclude d_E=2 or 4.

The common profile at each quotient (ell,i) is

    Z_(ell,i)(s,α) = (1/4) Σ_(h,b) X(ell,h,i,b)(-1)^(s h+α·b).

For the SAME X, all eight Z(0,0) entries vanish. Each of the seven other columns is either one ±2 or four ±1 on an affine two-flat in (ell,i), with product -1. In particular, **each column has an even number of odd entries on ell=1**, since an affine plane is entirely inside, entirely outside, or intersects a half-space in two points; a singleton has no odd entries. The actual graph transform and row-zero equation are

    Z_(1,i)(s,α) = (-1)^(sF_i)[Shat_i(α)+2(-1)^s dhat_i(α)]/4,
    Σ_b S_i(b)+2Σ_b d_i(b)=0.                                      (1)

No false equality of odd-row offsets, k=0 covectors, or exclusion of N type is assumed.

## 2. Replacement (3.0)/(3.1) directly from graph odd support

Let p_i be the number of negative entries of S_i and P_i the XOR of their b positions. From (1), p_i≡k_i mod 2. An even row is a signed affine character S_i=ε_iχ_ξi, including the constant case ξ_i=0, and P_i=Qξ_i: for a nonconstant character its two negative positions XOR to Qξ_i, while both constant characters give XOR 0. An odd row is S_i=ε_i(2·1_(b=γ_i)-1), and P_i=γ_i whether the negative set has one or three points, because the XOR of all four b values is 0.

Fix any nonzero α and put H_α={b:α·b=1}. Using row zero in (1),

    Z_(1,i)(0,α) = -(1/2) Σ_(b∈H_α)[S_i(b)+2d_i(b)]
                 ≡ 1 + α·(P_i+Σ_(b∈D_i)b)  (mod 2).              (2)

Here |H_α|=2, and each nonzero d_i is odd. Summing (2) over the four graph rows and using the even graph-odd-support count gives α·(ΣP_i+B_D)=0 for both basis covectors. Therefore

    Σ_i P_i = B_D.                                                  (3.0)

This uses the full actual graph D0-site XOR, not an odd-offset lemma. It also holds in the 2200 and 1111 shapes, independently of the lambda column being a singleton or a plane.

For the same graph Y, the general graph phase is a common sign times (-1)^(b₀b₁+λ_i·b). Hence even rows are bent

    G_i(b)=Y(1,F_i,i,b)=σ_i(-1)^(b₀b₁+θ_i·b),  θ_i=λ_i+ξ_i,

and odd rows are signed characters G_i(b)=σ_iχ_κi(b), where

    κ_i=λ_i+(1,1)+Qγ_i.

The latter identity follows by expanding 2·1_(b=γ)-1: its quadratic term is b₀b₁ and its linear term is (1,1)+Qγ; the two quadratic terms cancel in Y. Since Σk_i=4, the number of odd k_i is even. Applying Q to (3.0), and using Σλ_i=0 and the cancellation of the even number of (1,1) terms, gives

    Σ_(even i) θ_i + Σ_(odd i) κ_i = Q B_D.                        (3.1)

This is a single same-object identity, with no choice of separate profile columns. For the relevant four shapes it specializes, with Δ the XOR of a k=2 pair and δ=γ+u for an odd row (u omitted when k=3 and present when k=1), to:

* 4000: Σ_i ξ_i=0, since all four b values XOR to 0.
* 3100: ξ_C+ξ_D=Q(δ_3+δ_1), where C,D are the k=0 rows.
* 2200: Σ_i ξ_i=Q(Δ_A+Δ_B), regardless of active/N/O type.
* 2110: ξ_2+ξ_0=QΔ+Q(δ_1+δ'_1), including N and O.

The offset terms in the last two odd-row cases do not generally vanish. The 2200 specialization is only the parity identity, not its full physical contradiction.

## 3. One common A₁ residue for all s, α and β

Use the actual Y throughout and define its ell-partials

    A_ell(s,α,β)=Σ_(h,i,b)Y(ell,h,i,b)(-1)^(s h+α·b+β·i).

Let E_r be the set of even-k graph rows, N=12+|E_r|, n the parity of the number of negative **actual** non-D0 mate signs e_i(b), and m_α the number of odd-row κ_i equal to α. The unnormalized b-Walsh transform of a bent row is

    Σ_b G_i(b)χ_α(b)=2σ_i(-1)^q(α+θ_i),  q(z)=z₀z₁,

while an odd-row transform is 4σ_i·1_(α=κ_i). There are an even number of bent rows, so N is even. In the sum of the N signed terms of magnitude 2, half the sum modulo 2 equals N/2 plus the number of negative signs. Odd-row magnitude-4 terms each contribute 1 modulo 2 regardless of their actual signs. Consequently A₁/4 is integral, and with a frequency-independent c∈F₂,

    A₁(s,α,β)/4 ≡ n+c+s+m_α+α·(B_D+QΣ_(even i)θ_i) (mod 2).   (3.2)

For a fully explicit constant one may take c=N/2+Σ_even 1_(σ_i=-1)+Σ_even q(θ_i), modulo 2. The phase bookkeeping is as follows:

* The β exponent is Σ_even i+Σ_i(4-k_i)i=Σ_all i=0. The β-independent odd-row terms are already accounted for by m_α.
* The s exponent is Σ_even F_i+Σ_i(4-k_i)(1+F_i)=Σ_even F_i+Σ_odd(1+F_i)=Σ_iF_i=1, because there are an even number of odd rows.
* The XOR of the b labels of the twelve **actual** non-D0 mates is B_D: the XOR of all four b values on each row is 0. Thus their α exponent is α·B_D.
* Expanding q(α+θ_i) gives q(α)+q(θ_i)+α·Qθ_i. The even number of bent rows cancels q(α), leaving α·QΣ_even θ_i. The remaining q(θ_i) and σ_i enter only c.

All equalities above are in F₂. This explicitly covers α=0 as well as every nonzero α, all four β, both s, arbitrary row signs, both F bits on every row, and all allowed actual mate placements.

Put v=B_D+QΣ_even θ_i. Equation (3.1) gives Σ_odd κ_i=Qv. In each of 4000,3100,2110 there are zero or two odd rows. With zero odd rows v=0. With two equal κ values, v=0 and m_α is even everywhere. With two distinct κ values, their XOR is Qv≠0; they form exactly one of the two levels of α·v because (Qv)·v=0. Thus m_α+α·v is constant in α in every case, including α=0. There is therefore ONE common slice s_* on which every A₁/4 is even and the other slice s'=s_*+1 on which every A₁/4 is odd.

## 4. E/O forcing from the same physical Y

The full coefficients are A₀±A₁. Their 4 mod 8 residue makes A₀,A₁ multiples of 4 with opposite quotient parities, and the two caps are equivalent to |A₀|+|A₁|≤12. The full energy 128, Parseval, and possible magnitudes 4 or 12 give exactly eight small (magnitude-4) full coefficients: 16n+144(64-n)=64·128 implies n=8.

At s_* let E count the 16 positions (α,β) with |A₁|=8; the rest have A₁=0. At s' let O count those with |A₁|=4; the rest have |A₁|=12. Every E position uses exactly one small full coefficient, and every O position uses at least one; hence E+O≤8. Five-bit Parseval for ell=1 gives

    64E + 16O + 144(16-O) = 32·64,     O=2+E/2.                  (4)

Let C=Σ_(12 non-D0 mates) G_i(b)e_i(b). On the s_* slice, the spatial h-combination is (-1)^(s_*F_i)[G_i(b)+2(-1)^s_*e_i(b)] at a non-D0 mate and (-1)^(s_*F_i)G_i(b) at a D0 mate. Four-bit Parseval yields

    64E=16[64+4(-1)^s_*C],   E=16+(-1)^s_*C≥4.                   (5)

Equations (4), (5) and E+O≤8 force E=O=4. Equality in |C|≤12 forces the sign **at each of the twelve individual physical mate sites**:

    e_i(b)=-(-1)^s_*G_i(b).                                        (6)

The eight E/O positions already consume all eight small full coefficients. At each O position A₀ cannot be 0, which would consume two small coefficients; its parity and cap then force |A₀|=8. The opposite slice s' has the actual row contribution

    R_i(α)=(-1)^(s'F_i) Σ_b G_i(b)χ_α(b)[3-2·1_(b∈D_i)].           (7)

One β multiplies row i by (-1)^(β·i). Any three distinct i∈F₂² are affinely independent, so a single β and an overall sign can align any three nonzero row contributions. This alignment uses one real physical frequency, not different β values for different rows.

## 5. The three shape contradictions

In every case the cap gives |A₁(s',α,β)|≤12. A k=0 row is bent with magnitude 6 in (7); a k=4 row is bent with magnitude 2. A k=1 row is a character with magnitude 10 at its κ and 2 elsewhere; a k=3 row is a character with magnitude 6 at its κ and 2 elsewhere. The latter two statements follow from summing the four character signs with the single exceptional b weighted 1 instead of 3, or vice versa.

* **4000.** At any α, align the three k=0 magnitudes 6; the k=4 row can cancel at most 2. Thus |A₁|≥18-2=16.
* **3100.** At α=κ of the k=1 row, align its 10 and the two k=0 sixes; the k=3 row can cancel at most 6. Thus |A₁|≥10+6+6-6=16.
* **2110.** The k=2 row is bent, and its magnitude is either 2 or 6: put t_b=G_i(b)χ_α(b), whose four signs have product -1 and sum ±2. If the two deleted signs are equal, the other two are opposite and 3Σt_b-2Σ_deleted t_b=±2; if they are opposite, their sum is 0 and the result is ±6. If the two k=1 κ differ, choose α equal to one; align its 10, the k=0 six, and the k=2 magnitude at least 2, subtracting at most 2 from the other odd row: |A₁|≥16. If their κ agree, align 10,10,6 and subtract at most 6: |A₁|≥20.

Each contradicts the same cap. The k=2 argument includes inactive N, inactive O and any admissible placement/sign; it does not import the false N-impossibility assertion. These are written implications from §1, not parent adoption.

## 6. Complete same-X profile countermodels to the false intermediates

These are literal spatial X arrays, not independently assembled columns. Use bit labels A=00, B=10, C=01, D=11 and F_A=F_B=F_C=0, F_D=1. The graph site is (1,F_i,i,b); a listed d_i(b) is half the X value on its actual same-b mate. All omitted graph-mate values are zero. A triple (h,b,value) in an ell=0 row specifies its only nonzero X entries. The seven profiles below list *all* nonzero entries; a subscript g or e indicates ell=1 or ell=0. Their signs are the actual numerical Z entries.

### 6a. 3100: unequal odd offsets and unequal k=0 covectors

Graph data:

| row | S_i(b) | nonzero d_i(b) |
|---|---|---|
| A | 2·1_(b=10)-1 | d(10)=+1, d(01)=-1, d(11)=+1 |
| B | 2·1_(b=00)-1 | d(11)=+1 |
| C | -χ_01 | none |
| D | -χ_11 | none |

At ell=0 take A: (0,10,+2),(1,11,-2); B: (0,10,-2),(1,10,+2); C: (1,10,+2),(1,11,-2); D: no sites. Substitution into the definition of Z gives:

| (s,α) | ell=1 | ell=0 |
|---|---|---|
| (1,00) | A_g:-1, B_g:-1 | A_e:+1, B_e:-1 |
| (0,10) | A_g:-2 | none |
| (1,10) | A_g:+1, B_g:+1 | A_e:-1, B_e:+1 |
| (0,01) | A_g:+1, C_g:-1 | A_e:+1, C_e:+1 |
| (1,01) | B_g:+1, C_g:-1 | B_e:-1, C_e:-1 |
| (0,11) | B_g:+1, D_g:-1 | A_e:-1, C_e:-1 |
| (1,11) | A_g:-1, D_g:+1 | B_e:+1, C_e:+1 |

A's omitted mate is u_A=00 and γ_A=10, so δ_A=10; B's actual mate is u_B=11 and γ_B=00, so δ_B=11. Their offsets differ, as do ξ_C=01 and ξ_D=11. The corrected relation is ξ_C+ξ_D=10=Q(10+11). Thus the two claimed equalities do not follow even from all seven simultaneous profiles.

### 6b. 2110: a genuine N row

Use the same F and locations. Set A: S=2·1_(00)-1,d(00)=+1; B: S=2·1_(00)-1,d(01)=+1; C: S=χ_10,d(00)=+1,d(01)=-1; D: S=-χ_10, no mates. At ell=0 take the same A and B triples as in 6a, C: (0,10,-2),(0,11,+2), and D empty. The full seven profiles are:

| (s,α) | ell=1 | ell=0 |
|---|---|---|
| (1,00) | A_g:-1, B_g:-1 | A_e:+1, B_e:-1 |
| (0,10) | A_g:+1, B_g:+1, C_g:+1, D_g:-1 | none |
| (1,10) | C_g:+1, D_g:+1 | A_e:-1, B_e:+1 |
| (0,01) | A_g:+1, C_g:+1 | A_e:+1, C_e:-1 |
| (1,01) | B_g:+1, C_g:-1 | B_e:-1, C_e:-1 |
| (0,11) | A_g:+1, C_g:+1 | A_e:-1, C_e:+1 |
| (1,11) | B_g:+1, C_g:-1 | B_e:+1, C_e:+1 |

At C the D0 pair has Δ=01 and a=QΔ=10=ξ_C, with opposite mate signs: this is precisely N type. The two odd offsets are 00 and 01. The corrected identity reads ξ_C+ξ_D=0=10+Q01. Thus N is not excluded by the U0 profiles alone.

In both tables every four-point support has XOR zero in the three quotient bits and four distinct points, hence is an affine two-flat; its displayed sign product is -1. The one singleton in 6a is -2. Every row sum is zero. Each array has four actual graph D0 sites, six ell=0 Z2 sites at b≠0, and X-energy 16+4·4+6·4=56. In both, the X-zero site (ell,h,i,b)=(0,0,D,01) can be designated the Z4 location, leaving the other 17 X-zero ell0/b≠0 sites Z0. The simultaneous profile equivalence gives the claimed U0 cap/divisibility and carried zero for these X arrays: the quotient Walsh transform of each singleton or odd-product flat has magnitude 2, then the definition contributes the factor 4.

**Boundary:** these constructions specify X and physical site locations only. They do not construct a compatible common physical Y, verify general-g/J=1 or all U3 caps, establish an original f/R/u/T/atom caller, or refute the final all-graph no-go. The S1 record retains **ONE** f747 author MATH MAJOR for both false intermediate issues, not two findings and not final-theorem falsity. F764/F765's replacement argument is distinct from the frozen f747 bytes.

## 7. Parent-run evidence and exact unpaid frontier

S4 is the actual parent f766v2 receipt: one 44.02774725 s run, process exit 0, JSON status **PARTIAL_COOPERATIVE_DEADLINE**, not a complete pass. At the stated same-X checker scope, 4000, 3100 and 2200 completed, whereas 2110 finished 361,394 of 774,144 canonical graph tuples and had started tuple 361,395. Its 240,720 observed 2110 same-X arrays include 128,848 N-type and 214,928 unequal-offset discriminator leaves; these are partial counts, not complete-domain totals. The completed 3100 stage reports 119,808 arrays and 92,160 discriminators for each of unequal offsets and unequal k=0 covectors. The 2200 and 4000 completed stages report 78,336 and 3,840 same-X arrays. The receipt reports no (3.1) obligation failures on the examined leaves, not proof of unexamined 2110 cases. Its separately complete local-A1 and derived-22 stages have their own recorded conditional/representative scopes; they do not turn the overall JSON into PASS or construct a common Y/U3 caller. F766v1 was superseded and NEVER RUN. I did not run or open its old source.

The new written argument covers exactly 4000,3100,2110 under §1 and is nonblind to S2/S3. S5's 1111 obstruction is a separate adopted import. The full actual 2200 physical obstruction remains **unpaid for this return**, including all linkage between its local, equality-forced Y and physical ell0 conditions. Its S3 presentation has been read but not independently reconstructed or accepted here. No union of these scopes may be relabeled a proof of d_E≥1 without a separate complete 2200 check and exact interface composition. Independently, S6 excludes odd d_E at its own adopted same-X scope; d_E=2,4 and any still-unpaid d_E=0 case remain open. J/U3 compatibility outside the three conditional contradictions, common f/R/u/T/rank/atom restoration, V signs, original caller, NL242 and novelty remain open. Parent full read, any independently scoped checks and eventual disposition are separate decisions; there is no requested source/GO in this return.

## 8. Coverage, bindings, corrections and NOTTESTED

Before the direct PREBODY ACK to Main I read the actual dispatch, complete manifest, freeze receipt, final binding, prepared parent metadata and all **22** manifest-listed controls through their endings; controls were permissions/status only. Only after that ACK I read both packet parts serially, in contiguous RAW windows of at most 20 LF: part 1 LF 1–1005 followed by part 2 LF 1–116, through both endings, before comparison or science. Total: **1,121 packet LF**, eight complete source blocks totaling **1,085 source LF**. No outgoing links, old source code, held payload/history or unspecified sibling proof was opened. All held episodes **and all** their method/selection/planning/proof/verification/reporting/confidence/downstream consumers remain NONINPUT. This is not a cognition certificate.

The following are parent-supplied complete-body source pins, read through the literal packet, not separately opened or live-rehashed at their original paths. Prefix P=`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`:

| source | path after P | LF | SHA-256 |
|---|---|---:|---|
| S1 | review-waves/f747-boolean-general-d0-occupancy-profile-frontier-author/parent-false-offset-and-N-type-profile-inferences-math-major-v1.md | 1–9 | bfd61d0b27a29c43ad9757b6eb62300fec62b4953b2aca106f74c3836a3e6424 |
| S2 | review-waves/f764-boolean-all-graph-D0-common-parity-proof-author/author-candidate-v1.md | 1–166 | 5af6d01a1d5d3820ddc086b596ce6064390d1e30acdd9c1396465b76fee2864d |
| S3 | review-waves/f765-boolean-22-physical-Z2-and-allgraph-proof-author/author-candidate-v1.md | 1–195 | c54f235a86907ac14f769d504f0c589bfdc458155da6c6191d32a80b265a7779 |
| S4 | review-waves/f766-boolean-allgraph-D0-profile-parity-exact-finite-author/parent-allgraph-profile-parity-v2-run-v1-receipt.json | 1–582 | f48e7d2eb424d900198cbea89d12155c7974c5bceb3606ce63fda2151db224b6 |
| S5 | dispositions/info-6-entire-four-distinct-d0-rank2-same-object-obstruction-parent-v1.md | 1–31 | ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928 |
| S6 | dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md | 1–52 | f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2 |
| S7 | parent-recovered-local-H-definition-and-general-g-foundation-v1.md | 1–13 | a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef |
| S8 | dispositions/info-6-actual-rank2-seven-profile-and-four-distinct-d0-cross-fibre-parent-v1.md | 1–37 | 44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a |

After completing both packet reads, I independently observed the following whole-file administrative hashes and LF counts: manifest `8ae98dff732562346471525017c2b75bf5f1a771671dd7c493ef61ed7af99b3c`/336; freeze receipt `71af4d8dc0e948ee3f77887e3433d10a804c5fe1a89ce01ed27a375cec6e14ba`/176; final binding `be5b868f41bf67a7d6b88bd51696125ec181fed43957774d87e68167c9f4d6ba`/228; prepared metadata `55538d86cd6ffd2a973fbbe35b90e39a611c0eacacce7c11c7ca0264b7793c7c`/296; actual dispatch `189c5426c5b89b9d443ce3df05b8e3a9b2765d75531292a684b89eb16caf4542`/32; part 1 `9a42fb87217a5329a049c4f6eaf8df74529e09b2688de5d10db274cf2dc8f3af`/1005; part 2 `df479fd422c3c49bece50987d0aaed9d058301fa5efa7f5f63a03e0ca3c6e703`/116. These packet/metadata observations are not source rehashes or scientific executions.

**Corrections and assurance:** the correction is the displayed replacement reasoning and two U0-only countermodels; no frozen source was edited. Any later correction requires a new additive artifact, never overwrite or backdate. **CHILD SCIENTIFIC EXECUTION NOT RUN:** no source/checker execution, interpreter arithmetic, compiler, test, solver, CAS, build, lint, formatter, external-model CLI, install, paid job, or child GO. The profile tables and derivations are written claims, not a computational pass. No independent-model-family, prior constrained-WRITTEN gate, human, kernel/formal verification, parent adoption, original-source identity or novelty claim is made.
