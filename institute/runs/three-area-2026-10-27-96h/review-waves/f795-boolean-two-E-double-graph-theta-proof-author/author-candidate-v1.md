# F795 — same-X defect-row theta XOR, all three lambda alternatives

**Status: conditional written AUTHOR candidate; NOT parent-adopted or independently reviewed.** At the actual same-object interface below, for every prescribed transported character, odd graph F, physical location pair and actual sign assignment, the four graph-row covectors satisfy

\[
 \theta_{00}\oplus\theta_{01}\oplus\theta_{10}\oplus\theta_{11}=\kappa,
 \qquad 0\ne\kappa,\quad \kappa(\delta)=0,\quad \delta=p\oplus q\ne0.
\]

The notation in the display means that kappa is the **unique nonzero covector** annihilating delta; it does not mean the scalar kappa(delta) is nonzero. The conclusion follows already from the same-X zero column and simultaneous nonzero quotient profiles, not from any constructed Y. All three lambda types, both allowed allocations of the two E sites, every sign, and both values of every transform slice are retained. The extra exact tests and the E-plane refinements below are necessary restrictions on actual X, not claims that every row of the case table is realizable. The proof is a fresh written reconstruction after reading the complete packet, **nonblind** to S1, which already states this invariant and a larger unadopted common-Y obstruction. This return does not assess or adopt S1's common-Y proof.

## 1. Exact imports and actual quantities

Work at the named conditional rank-two five-span interface of packet S1, S4 and adopted-scope S6. Coordinates are `(ell,h,i,b)` with `ell,h in F2`, `i,b in F2^2`. There is one physical object and its fixed original-DC transported character `t`; put `X(c)=(-1)^t(c) x(c)` without choosing or changing t. The graph has sites `(1,F_i,i,b)` with `sum_i F_i=1`. Its same-b mate is `(1,1+F_i,i,b)`. All four graph values in each row are ±1. There are exactly two graph-mate D0 sites, in the same row `j` at distinct `p,q`; their X values are `2 epsilon_p, 2 epsilon_q`. Every other graph mate has X=0. Of the other two D0 sites, both are E sites at `ell=0,b=0,i!=0`; they occupy either the same E row (different h) or two distinct E rows. The six ell=0 Z2 sites have b!=0 and X=±2; all other ell=0 X values, including the two full sites, are zero. This is an X-side import, not a construction of the physical inverse or a common Y.

For `s in F2` and b-covector `alpha`, use the **same** X in every column

\[
 Z_{\ell,i}(s,\alpha)=\frac14\sum_{h,b}X(\ell,h,i,b)(-1)^{s h+\alpha(b)}.
\]

The eight `Z(0,0)` entries vanish. Each of the seven nonzero `(s,alpha)` columns is either a single ±2 or four ±1 on an affine two-flat of the quotient `(ell,i)`, with product of those four signs −1. `lambda=Z(1,0)`. These are imported necessary actual-X properties, not free independently selected columns. The original phase, ternary inverse, J, U3 and full-caller assertions are not inferred from them.

Put `delta=p+q` and let kappa be the unique nonzero covector with `kappa(delta)=0`; denote the other two nonzero covectors by `u,v`. They obey `u(delta)=v(delta)=1` and `u+v=kappa`. Addition is XOR. For signs write `chi_alpha(b)=(-1)^alpha(b)`.

## 2. Row zero and the complete lambda split

At any row without D0 mates, zero eta says the four graph signs sum to zero. Any balanced sign function on F2² is a signed nonconstant character: the two positive positions form an affine line and hence are a level set of a unique nonzero covector. Thus its graph values are `sigma_i chi_{theta_i}(b)`, with `theta_i` one of kappa,u,v and `sigma_i=±1`.

At row j the zero equation is

\[
 \sum_b X(1,F_j,j,b)+2\epsilon_p+2\epsilon_q=0.\tag{1}
\]

* If `epsilon_p=epsilon_q=epsilon`, the sum is `-4 epsilon`; all four graph signs are `-epsilon`, so `theta_j=0`, `sigma_j=-epsilon`, and `lambda_(1,j)=2(-1)^F_j sigma_j`. The lambda column is therefore **the graph singleton** at j. All ell=0 lambda entries vanish.
* If `epsilon_p=-epsilon_q`, the graph row is balanced, with `theta_j` nonzero, and every graph lambda entry is zero. The whole lambda profile is either **one ell=0 singleton ±2**, at any permitted quotient row, or **four ell=0 ±1 entries** with product −1. The latter four entries necessarily occupy all four ell=0 rows: the ell=0 half of the quotient is itself the only four-point affine plane contained there.

No E singleton has been discarded; S2/S5 explicitly flag the historical gap. This is exhaustive under the profile import, but is not an existence claim for any alternative with the physical inverse and Y conditions.

The actual ell=0 support also constrains the three alternatives. There are eight sites, and `lambda=0` at row i means that the signed X/2 sum in each h-cell is zero. A singleton ±2 at `(0,a)` means its h=0 and h=1 signed sums are ±2 and ∓2; all other h-cell sums are zero. Thus every cell in either singleton-lambda alternative has even occupancy. A four-site cell must be in a non-full row i!=0 and consume its physical E site. If q is the number of four-site ell=0 cells, the graph-singleton case has q=0,1,2 and `4-q` occupied cells. In the E-singleton case q is at most 1, so there are three or four occupied cells. Indeed q=2 would consume all eight sites in the two h-cells of the singleton row, each with a 3:1 sign split. At every nonzero alpha each such cell has Walsh sum ±2. For some s their combination gives an ell=0 entry ±2. Choosing alpha equal to the nonzero theta of any of the three untouched graph rows gives a simultaneous graph entry ±1 in that very column, impossible for a singleton. These are necessary restrictions, not a realization classification.

In the four-entry E-plane lambda case, each of the eight h-cells contains exactly one site: each of four lambda entries ±1 requires at least one site in each h-cell, and there are exactly eight sites. Write their b-coordinates as `P_i` at h=0 and `Q_i` at h=1 and their X/2 signs as `a_i,-a_i`. Then `a_i=±1`, `product_i a_i=-1`, `P_0,Q_0 != 0` at the full-site row, and exactly two of all `P_i,Q_i` in non-full rows are zero. The latter count is the actual two E D0 sites; it allows allocation 2 or 1+1 without asserting their existence in every subcase. Put `d_i=P_i+Q_i`. For all alpha,s,

\[
 Z_{0,i}(s,\alpha)=\frac{a_i}{2}\bigl(\chi_\alpha(P_i)-(-1)^s\chi_\alpha(Q_i)\bigr),\tag{2}
\]

which is zero unless `s+alpha(d_i)=1`, when it is `a_i chi_alpha(P_i)`. For each i and alpha exactly one s-slice is nonzero.

## 3. Every kappa/u/v graph entry and the XOR proof

For all rows write graph values as `sigma_i chi_{theta_i}(b)`, with the constant character allowed only for j in the equal-mate case. For i!=j and alpha!=0,

\[
 Z_{1,i}(s,\alpha)=(-1)^{sF_i}\sigma_i\,1_{\theta_i=\alpha}.
\]

Define `B_alpha=(epsilon_p chi_alpha(p)+epsilon_q chi_alpha(q))/2`. At j the actual physical entries are

\[
 Z_{1,j}(s,\alpha)=(-1)^{sF_j}
 \left(\sigma_j 1_{\theta_j=\alpha}-(-1)^s B_\alpha\right).\tag{3}
\]

Let `k_alpha` count the three nondefect rows with theta=alpha. If a column has only 0 or ±1 on its graph side, the number of nonzero graph entries is even: a graph ±1 excludes a ±2 singleton, and a four-point affine plane intersects the graph half `ell=1` in 0, 2 or 4 points. This observation is **not** applied when the graph side contains ±2.

* **Equal signs.** Here theta_j=0, `B_kappa=epsilon_p chi_kappa(p)=±1` and `B_u=B_v=0`. Therefore the graph counts are `1+k_kappa,k_u,k_v`, all even. Since the three k's sum to 3, the only multiplicity triples `(k_kappa,k_u,k_v)` are `(3,0,0)`, `(1,2,0)`, `(1,0,2)`. Their XOR contribution is kappa.
* **Opposite signs, theta_j=kappa.** `B_kappa=0`, whereas `B_u,B_v` are ±1. At all three characters row j contributes exactly ±1. All three k's must be odd; their sum is 3, so `(k_kappa,k_u,k_v)=(1,1,1)`. The other rows XOR to zero, and adding theta_j gives kappa.
* **Opposite signs, theta_j=u.** At alpha=u, formula (3) is 0 for one s and ±2 for the other. The ±2 column is the singleton at j, so every other graph entry there is zero and `k_u=0`. At kappa the j entry is zero, so `k_kappa` is even; at v it is ±1, so `k_v` is odd. Thus `(k_kappa,k_v)=(0,3)` or `(2,1)`, and the XOR is `u+v=kappa`. The `theta_j=v` case is identical with u and v exchanged.

This proves the displayed invariant for **every** actual F, p,q, sign and specified t at the stated same-X interface. The argument never assumes F in a chosen normal form, identifies t with zero, or assumes that separate X-profile choices come from one array.

## 4. Exact profile restrictions, including both s-slices

The previous parity argument can be read as the following exhaustive necessary graph-side table. Here `mixed` means a four-entry quotient plane with two graph and two ell=0 entries; `graph plane` means all four graph rows with no ell=0 entries; and `E-only` means the column is either an ell=0 ±2 singleton or all four ell=0 ±1 entries with sign product −1. The table states what an actual column must be; it does not claim every indicated possibility has an actual completion.

| Mate signs and defect theta | alpha=kappa | alpha=u | alpha=v |
|---|---|---|---|
| equal, theta_j=0 | mixed if k_kappa=1; graph plane if k_kappa=3 | E-only if k_u=0; mixed if k_u=2 | E-only if k_v=0; mixed if k_v=2 |
| opposite, theta_j=kappa | mixed | mixed | mixed |
| opposite, theta_j=u | E-only if k_kappa=0; mixed if k_kappa=2 | for one s graph singleton ±2 at j, for the other s E-only | mixed if k_v=1; graph plane if k_v=3 |
| opposite, theta_j=v | E-only if k_kappa=0; mixed if k_kappa=2 | mixed if k_u=1; graph plane if k_u=3 | for one s graph singleton ±2 at j, for the other s E-only |

The two rows with theta_j=u/v have the multiplicity constraints from §3, not independent entries in the table. In any graph-plane entry the product of the four graph signs must be −1 in **both** s-slices. In the equal/alpha=kappa case and the opposite/theta_j=u,alpha=v case (or its u/v swap), that product is `B_alpha product_(i!=j) sigma_i`: the s exponent is `sum_i F_i+1=0`. Thus it is not legitimate to require two opposite signs there.

For an exact per-column test, after computing the actual E-side values rather than choosing a profile independently: (i) a graph ±2 forces that value to be the whole singleton, so every E value and other graph value is zero; (ii) with exactly two graph ±1 values in rows r,r', exactly two E values ±1 must be in rows a,a' with `a+a'=r+r'` and the product of all four signs −1; (iii) with four graph values, all E values are zero and their graph-sign product is −1; (iv) with no graph values, the E-only singleton or whole E-plane condition applies. Together with (3), this is necessary **and sufficient for the declared profile shape for each of those six columns**. It is not sufficient for the physical inverse, full Fourier/caller constraints, or a Y witness. The same actual E values must be used for all six tests and lambda.

## 5. Further simultaneous restrictions if lambda is the E plane

The representation (2) gives information not visible from lambda alone.

**A. Opposite signs and theta_j=kappa.** Each of the kappa,u,v columns is mixed in each s-slice. Hence for every nonzero alpha exactly two `alpha(d_i)` are 0 and two are 1. Taking the two independent covectors u,v and their sum shows that the four `d_i` are all distinct. In particular `i -> d_i` is an affine bijection of F2²: the XOR of its four values is zero, so the value at the fourth input is determined by the other three. For the unique nondefect row `i_alpha` with `theta_i=alpha`, each E pair in that alpha column has difference `j+i_alpha`; equivalently `alpha(d_{i+j+i_alpha})=alpha(d_i)` for all i. Both s-slices' sign products must still satisfy the explicit test in §4. These conditions apply uniformly to all actual F and E allocations.

**B. Opposite signs and theta_j=u** (and symmetrically theta_j=v). Let `s_*` be the singleton slice determined by `(-1)^s_* B_u=-sigma_j`. Its E entries vanish, so (2) forces `u(d_i)=s_*` for every i. If `k_kappa=0,k_v=3`, the kappa column has no graph entry on either s-slice; because all E entries in (2) are 0 or ±1, each slice would require four E entries, contradicting the fact that each i appears in only one slice. Therefore the E-plane lambda case necessarily has `k_kappa=2,k_v=1`. Let D be the difference of the two graph rows in the kappa column; it is also the difference of the complementary graph pair in the v column. Each of those columns is mixed, so `kappa(d_i)` is balanced and constant on each pair `{i,i+D}`. Thus the four d values consist of two values, each twice, with common u-value `s_*`; the repeated pairs are exactly the D-pairs. The non-singleton u slice has all four E entries, whose required sign product −1 gives `u(sum_i P_i)=0`. All mixed-column sign-product conditions from §4 remain required.

These refinements do not omit the E-singleton lambda alternative; §3 and §4 already cover it without assuming the special one-site-per-cell representation (2). Nor do they prove that any particular permitted E-plane or singleton pattern has a physical or common-Y realization.

## 6. Evidence, process, and open scope

Main directly confirmed the actual f795 dispatch receipt before I opened it. Before any packet body, I read the actual dispatch receipt, the complete manifest, freeze receipt, final binding, prepared metadata and all 22 listed status/permission controls through their endings; then I sent Main a **direct PREBODY ACK** naming those controls and the one packet part's **928 LF**. I then read part 01 serially RAW in consecutive windows of at most 20 LF through LF 928 and its ending, including long lines, before mathematical work or comparison. The controls were used solely for status/permissions: the method-restoration and frontier-direction records; parent L1, privacy, core-Gram, AME-compression and PH-registration quarantines; f439, f444, f448, f508, f513, f586, f602, f596, f653, f654, f659, f660 and f662 quarantines; parent remaining-D0-occupancy omission; and prerun f746/f749 corrections. All genuine held episodes **and all consumers** remained NONINPUT. The task was nonblind to the target/manifest and, after the ACK, all packet bodies; no clean-cognition or independent-family claim is made. No unlisted source, old code, held history, sibling result, outgoing link or network was opened.

The packet manifest is `manifest-v1.json`, parent-supplied SHA-256 `58b8a4ccb6ddbae336b452ecc93233da471fb9df9a2e7ccb5667868ef93785cb`; its one complete part has 928 LF and parent-supplied SHA-256 `42a2438e7b6a8b24e56f8e11df65d153f61fbe415711dddff3b08680643cca05`. The freeze receipt reports source roundtrip/persisted-byte checks and final binding reports all hashes matching; these are **parent-reported administrative facts**, not independently recomputed hashes, mathematical proof or source-identity certification. The complete source bodies in that packet, with LF counts and SHA-256 pins supplied in the manifest, are as follows; paths are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`:

| ID | Complete source body; LF | Parent-supplied SHA-256 |
|---|---|---|
| S1 | `review-waves/f789-boolean-two-E-one-double-graph-author/author-candidate-v1.md`; 200 | `db6343f98e598ffbe8c480175bbef6d3aeaac4f1b69766c360e5841121679dd5` |
| S2 | `review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/parent-omitted-ell0-lambda-singleton-proof-gap-major-v1.md`; 7 | `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca` |
| S3 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-quotient-census-erratum-v1.md`; 9 | `90c4242e118be887f19b61ccba23f4af0c6062516142962b9a315557c0e03606` |
| S4 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-candidate-v1.md`; 121 | `e4e1c4a1812a03d0334dbee16dec50650d6a904e0e68b75dbcddae22e73aefa8` |
| S5 | `review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/author-candidate-v1-addendum-1.md`; 15 | `4dddaf7084e784b8c8d2b51b857320a26438a6a669b1ad9dee2f8d19268c4114` |
| S6 | `dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md`; 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S7 | `dispositions/info-6-entire-four-E-row-d0-actual-common-y-obstruction-parent-v1.md`; 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S8 | `review-waves/f755-boolean-remaining-D0-profile-and-U3-integer-finite-author/parent-u3-local-profile-v2-run-v1-receipt.json`; 256 | `d3cdcca328bf4c902c214ddbb9b5d42fccb41f56406147681c3baf2880f5aaf1` |
| S9 | `review-waves/f778-boolean-four-E-bent-parity-and-countermodels-finite-author/parent-v4-one-shot-run-v1-receipt.json`; 182 | `72ce3e26ffc187528890a9d0a808066ceb13b5d6fb9040644cf82f60b9871d08` |
| S10 | `parent-recovered-local-H-definition-and-general-g-foundation-v1.md`; 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |

S1 is an unadopted author proposal and explicitly gives the same target invariant, hence this is **nonblind reconstruction**, not independent discovery. S3 corrects S4's quotient census to eight, not four, transform values. S4 gives X-side omitted-singleton examples; S9 reports the parent's finite check at its own stated scope, not a complete Y or original caller. S6 adopts the named conditional lambda/census scope and S7 a different d_E=4 obstruction; neither is enlarged here. S8/S9 are read receipts, not source code or a new execution. S10 is the scoped local-H/general-g foundation; this X-side result neither rederives its original source nor requires a separate Y phase formula.

**Open / not claimed:** The same-X invariant and the conditional profile restrictions alone do not construct a full Y, establish S1's proposed Y contradiction, rule out all d_E=2 occupancies, settle d_E=0, V, the physical inverse/original selected-T/rank/eight-zero caller, global rank-two/five-span/NL242, or prove novelty. No separate human, family, kernel or parent review/adoption is asserted. The candidate's additional E-plane restrictions are written deductions needing scrutiny, not an executed exhaustive search. No source program is proposed. No scientific code, test, solver, CAS, build, lint, formatter, external-model CLI, network, Git, installation or deletion was run by this author. This file was created exclusively, then before return its opening display was corrected from the self-contradictory typo `0≠kappa(delta)=0` to `kappa≠0, kappa(delta)=0`; the prose and proof had already specified the latter. The native UTC clock observed before creation was `2026-10-31T01:27:14Z`; it is a lower bound on file creation, not a backdated creation timestamp.
