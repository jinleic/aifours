# RQLS10 v41 — EXACT two-field orthogonality bridge, and EVERY fifth-root ONB has dephasedF5 rank3or4

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 10:02:13 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite moment/congruence/Fourier/quadratic/Hermitian reasoning only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty or accepted finite-witness claim.

This is NOT a reversal of v40's warning that F16 orthogonality alone is too weak. It supplies the genuinely missing ADDITIONAL exact conditions, proves that they are JOINTLYSUFFICIENT, and sharply constrains the resulting context geometry. The original phase5 family remains OPEN; no100-word witness has been produced.

## 1. A necessary global phase-sum invariant, made zero by ONE common coordinate unitary

Use v40's literal phase5 vectors q_c(s)=zeta^f_s(c)/sqrt10, with zeta a primitive fifth root and f(c) inF5^10. Two actual orthogonal vectors have balanced difference counts2each, hence

    sum_s [f_s(c)-f_s(d)]=2*sum_(a inF5)a=0 inF5.

The row/column orthogonality graph of the actual10x10 cells is connected, so ALL hundred phase words have the SAME coordinate sum t. Adding a constant word a*1 is only a ray phase and changes the sum by10a=0; thus this sum is genuinely projectively invariant within the phase5 family.

Multiply all complex vectors by ONE common coordinate-phase unitary diag(zeta^h_s), with sum h_s=-t. This preserves all original conditions and the phase5 alphabet while making every phase word's sumZERO. Choose each ray's constant-shift representative so its first coordinate isZERO. The resulting representatives lie in

    S={x inF5^10: x_1=0, sum_s x_s=0},            dimS=8.

The standard bilinear form dot(x,y)=sum_s x_s y_s is NONDEGENERATE on S. Indeed, in the remaining9 coordinates the annihilator of the sumzero hyperplane is the all-ones line; such a vector lies in that hyperplane only if9a=4a=0, hence a0. Write Q(x)=dot(x,x).

The choice is ONE common coordinate change plus independent global RAY phases, not an independent ambient basis for each row. No arbitrary array outside the phase5 branch is declared WLOG.

## 2. Finite Hermitian orthogonality plus TWO moments is EXACT, not a relaxation

For two phase words f,g let n_j count their coordinate differences equal to j inF5; sum n_j=10. Let t inF16 be the order5 image of zeta modulo2. By the full proof inv40,

    sum_s t^(f_s-g_s)=0 IFF every n_j isEVEN.     (H16)

Also impose the two finite moments

    sum_j j*n_j=0,
    sum_j j^2*n_j=0 inF5.                        (MOM)

The first is already automatic for pairs in the globally normalized S; the second is Q(f-g)=0. If the rays are DISTINCT, conditions H16+MOM are JOINTLYEQUIVALENT to actual complex orthogonality.

Necessity follows from balanced counts2each. For sufficiency, H16 gives n_j=2m_j with nonnegative integers m_j summing5. Regard the m_j as a MULTISET of FIVE elements ofF5. MOM says its element sum and squared-element sum are BOTHZERO.

**Five-element lemma.** Such a multiset is either allfivecopiesofONE element, OR allfiveDISTINCT elements ofF5.

Proof: if any value is repeated, translate it to0; because the multiset length is5 and its first two moments vanish, both moments remain zero. It now has entries(0,0,a,b,c), with a+b+c=0 and a^2+b^2+c^2=0. If a0, then b+c0 and2b^2=0, so allzero. If a!=0, scale it to1 and write b/a=x,c/a=-1-x. The square equation becomes

    x^2+x+1=0.

Its discriminant is-3=2 inF5, a NONSQUARE (the squares are0,1,4), impossible. Thus a repeated value forces allfive equal. If there is no repeated value, the five values are exactlyF5. This proves the lemma without enumeration.

The all-equal case would make all ten phase differences equal, so the two complex rays would coincide, contrary to the distinctness hypothesis. Therefore m_j=1 for every j, giving n_j=2 each, EXACT actual complex orthogonality.

Thus, for distinct normalized phase classes in S,

    ACTUAL complex orthogonality
      IFF Q(f-g)=0 AND h(t^f,t^g)=0 overF16.     (EXACTBRIDGE)

Here h(x,y)=sum_s x_s y_s^4; its zero condition is H16 (switching the exponent sign only conjugates a zero). This is an exact sufficiency theorem at the stated phase-family scope, not just a necessary reduction.

## 3. Every original context lies in an affine totally singular3-or4-flat overF5

Take any actual10-ray context. Translate its ten S representatives by one of them, so it contains0. Pairwise complex orthogonality and EXACTBRIDGE imply Q(x)=0 for each translated point and Q(x-y)=0 for each pair. Since the characteristic is5,

    Q(x-y)=Q(x)+Q(y)-2dot(x,y)

forces dot(x,y)=0 for all pairs. Their linear span is therefore TOTALLYISOTROPIC in the nondegenerate8-space S, so its dimension is at most4. This is a finite geometric necessity, not an assumption that only four coordinates of the complex vectors are nonzero.

The affine dimension cannot be0or1 because a phase-class line overF5 has only5points, whereas the actual ONB has10 DISTINCT phase classes.

The affine dimension also CANNOT be2, by the exact Fourier argument in section4. Hence it is3or4. No assertion is made that both values are attained or that this rank determines a witness.

## 4. Complete rank2 exclusion, retaining ALL ten actual context rows

After the translation and constant-phase representative choice, let M be the10x10 dephased exponent matrix of that context. Its row rank equals the affine dimension above. Suppose that rank were2. Factor overF5

    M=R*C,

where R is10x2 and C is2x10 of full row rank. The ten row coefficient vectors r_a inF5^2 are DISTINCT: identical r_a would make identical exponent rows, impossible for orthogonal rays. The columns of C form a ten-element MULTISET p_s inF5^2.

For every row difference delta=r_a-r_b, actual orthogonality gives

    sum_s zeta^(delta dot p_s)=0.

Because its ten difference values are balanced2each, the same identity holds for EVERY nonzero scalar multiple of delta.

Now any set of10 points in the affine planeF5^2 has a difference in EVERY projective direction: a chosen direction partitions the plane into onlyFIVE parallel lines, so10 points force two on one of those lines. Thus the displayed Fourier sum vanishes for EVERY nonzero delta inF5^2, not just the differences one happened to list.

The finite Fourier transform of the integer multiplicity function of the ten p_s is therefore zero at all24 nonzero characters and equal10 at zero. Fourier inversion forces that function to be CONSTANT10/25=2/5 on all25 plane points. An integer multiplicity cannot equal2/5. Contradiction.

This excludes the ENTIRE rank2 possibility, not a linear-code ansatz on a selected subset. Together with section3, EVERY fifth-root10-dimensional ONB has dephased exponent rank exactly3or4 overF5.

## 5. Exact original phase5 master as a DOUBLE finite geometry

The whole phase5 maximal1-RQLS10 problem is now equivalently:

-100 DISTINCT phase classes, represented by100 points in the common8-space S after the stated legitimate global normalization;
- an ACTUAL10x10 placement and ANY full Latin resolution L;
- for every row,column and L-symbol context, all ten pair differences are Q-isotropic overF5 AND all ten phase-torus images t^f are mutually Hermitian-orthogonal overF16.

EXACTBRIDGE proves these two finite conditions are JOINTLYSUFFICIENT for every required COMPLEXONB, not just necessary. Distinctness of the F16 projective phase-torus images is equivalent to distinctness of the phase classes(v40's injectivity). Each context's affineF5 span automatically has dimension3or4, and its F16 linear span automatically has dimension5 by the full cyclotomic determinant-rank theorem inv40.

This supplies an exact finite bi-geometry—not an arbitrary pairing of independent point sets: BOTH images must come from the SAME phase words via f->t^f. A generic isotropicF5 configuration plus an unrelated F16 clique is not a witness. Context affine flats or Hermitian5-spaces may intersect in additional unselected points; no unproved intersection-dimension restrictions were added.

The global mixed OA and three GH-code partitions inv40 remain equivalent descriptions. The new bridge does not turn its finite Hermitian counterprofile(4,2,2,2,0) into a valid basis: that profile fails the required moment conditions, so the prior warning is intact.

## 6. Acceptance/import boundary and remaining task

An ENTIRE gate must reconstruct ALLsix sections/endings plus operativev40 phase/field/rank facts: global SUM invariance and ONE coordinate normalization; nondegenerate8-space; five-element repeated-value lemma; exclusion of same-ray exception; JOINTiff bridge; totally singular affine span; ALLrank2 Fourier directions/integer inversion; exact same-word coupling of the two finite geometries and original Latin placement. A single finite clique, moment or GH block is not the result.

Classical inputs are elementary finite-field arithmetic, finite additive-character Fourier inversion and v40's fully named cyclotomic/F16 facts. All operative arithmetic/identities are written, NOT machine-checked. No scientific interpreter, private approximate scout, executable finite-witness checker/control/vendor/priority gate or unprovided classifier output was used or called passed.

No actual100-point phase-word/Latin table or contradiction has been delivered. Phase5 and the original maximal100-ray1-RQLS10 remain OPEN. Other alphabets, the full TypeIV master and all arbitrary noncovariant intrinsic10/4+6/5+5 possibilities remain OPEN. No A5-WLOG, unrestrictedno-go, formal/kernel/family/human/current-openness/novelty/original-witness promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues the ACTUALcoupled finite geometry or another original construction, no early pending-review park.
