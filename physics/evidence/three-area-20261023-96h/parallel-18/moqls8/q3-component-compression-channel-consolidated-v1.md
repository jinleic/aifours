# MOQLS8 q3: component, compression and channel manuscript — consolidated v1

Owner PhysicsMOQLS8-2, physics-4. Observed precreation clock: **2026-10-25T05:00:18-0700 PDT**. This is the ONE consolidated next attack requested after v32-B, not a fourth incremental addendum. It leaves all pinned originals and the v28/v31 review sources unchanged.

**Status: AUTHOR-WRITTEN CANDIDATE AT NAMED IMPORTS.** New material: the zero-slack six-space theorem in §5, with its complete written proof. Earlier component/compression candidates are consolidated here with their assurance correction, not granted a new acceptance label. No scientific interpreter, eval, enumeration program, symbolic/numerical computation, solver, certificate replay, CLI or nested agent was used for this manuscript. Metadata clocks/hashes and written reasoning only. Parent erratum v7 and scientific HOLD v2 remain binding.

## 1. Exact theorem claimed and exact result NOT claimed

All five members are ordinary MOQLS(8): every entry is a full unit vector of C^8, all actual rows/columns are ONBs, and EVERY pair's ALL64 same-cell products form an ONB of C^8 tensor C^8. In q3 exactly three members are nonclassical and two are actual classical mates. No real, phase-alphabet, affine-net, support-catalogue or projected-mate restriction is imposed.

Let a_s be real projector-span dimension; f_s the COMPLETE global exact-multiplicity8-ray count; r_s=8-f_s; b_s=a_s-f_s. The claims of this manuscript are:

1. The previously written exclusions f4/r4/b9,b10 and f5/r3/b8,b9, and the all-three-a12 exclusion, follow from §6 at their named imports.
2. **NEW:** a globally irreducible six-dimensional component cannot have local projector span11 in a full physical five-MOQLS8 family (§5). This statement is not restricted to q3 or to finite phases.
3. Consequently the last f5/r3/b7 q3 residual is ALSO excluded (§7). Thus all f5/r3/b7..9 and f4/r4/b9,b10 are excluded at this AUTHOR-WRITTEN boundary.
4. Every q3 family must still have an UNEXCLUDED f4/r4/b8 member. The ENTIRE remaining necessary joint parameter frontier, up to permutation, is:

| Three pairs (a,f) | leftover-projection rank d | triple-fixed count c |
|---|---:|---:|
| (14,1),(12,4),(12,4) | 0 | 0 |
| (14,2),(12,4),(12,4) | 0 | 0 |
| (13,3),(13,3),(12,4) | 0 | 0 |
| (13,3),(12,4),(12,4) | 1 | 1 |

These are necessary patterns, NOT realizability claims or supplied physical arrays. None is excluded here. In particular this is NOT q3 closure, unrestricted classicality, a nonclassical witness, completion of A10/A11 or Boolean UNSAT for an old GB formula. q1/q2 remain open.

## 2. Provenance, imports and withdrawn-computation boundary

The direct proof interfaces consumed are those recorded in:

- `proof-q3-component-span-reduction-v1.md`, SHA256 `8fbd48630a85b4976ccb841924d429a96f5e091b61c7aaacdd5b87087f2897da`, at the accepted whole-q3 parent disposition. In particular: actual coordinate components; singleton=fixed-ray equivalence; general ONB span bound; local dimensions3/4/5 bounds; two-sided degree3/S3; MATCH/ISOLATE2; uniform a>=12 and surplus<=14.
- `proof-global-gram-defect-v1.md`, SHA256 `3b54a3e46ceb9ffa9edccab28664e13e322f5b47707fdffb77a51beba9a608d8`, WITH `proof-global-gram-defect-v1-erratum-1.md`, SHA256 `ef32720fe1b7c64a8539d6ae8cf5d94a0605e10a002aeb8483a5a2ac8eeb5d59`: covariance Gram ranges and rank budget, not a presumption that covariance contractions are projections.
- `proof-C4NET-heavy-support-v1.md` WITH its mandatory adjoint-orientation addendum, as named in the component packet and the v16 parent section. Actual transition rows are actual target-cell supports; both real and imaginary Hermitian constraints are retained.

The earlier new claims, STILL not assumed accepted merely because they were written, are `joint-residual-transversal-mechanism-v1-addendum-1.md`, SHA256 `dadd68e7e460f1d1d348a61e36f38197336fef21475cfd77d4fdd383ce51c8e7`, its mandatory assurance `...-addendum-2.md`, SHA256 `b3c63853723eac5ccaaa98a5e95fc883982181e386bd3b625f03ae9a768281a9`, and purely written `...-addendum-3.md`, SHA256 `85b542f1b191442ea9f4fde710e74600c6b54dd3f211f6c4ec3408fe3314e2f2`.

Seven scientific eval cells were run earlier under checkpoint026's erroneous blanket permission. Their actual operations are preserved in `resumption-arithmetic-permission-withdrawal-v1.json`. Parent v7 attributes that permission error to the parent and grants NO executable/finite-certificate/retroactive-admission credit. Their108-parameter output is NOT a premise here. The written case proofs below replace any temptation to cite that output as verification. No further scientific computation followed withdrawal. This manuscript is not independent reconstruction of the author's own earlier work.

No K12/K3, 1/39/2165 catalogue, native refutation, GA/GB symmetry, unretained proof stream, arbitrary Boolean realization or real-form assumption is imported to prove the new partial claims.

## 3. Physical notation and the channel lemma, now for four channels

### 3.1 Actual identities and components

For selected vectors q_x and a full mate t, put P_x=|q_x><q_x| and P_(t,x)=|Q_t(x)><Q_t(x)|. The full physical equations give, for distinct x,y,

`<q_x,q_y><Q_t(x),Q_t(y)>=0`,

and for EVERY unit w,

`sum_x |<w,q_x>|^2 P_(t,x)=I8`.                         (E)

All mate vectors in (E) are FULL C^8 vectors. Fix an ACTUAL row ONB E of the selected member. Each actual cell has at most3 nonzero coordinates in E, and the same holds in EVERY other actual row/column frame. The complete S3 blocks are singleton, full2, full3, one-zero3, zero-matching4.

The support graph of ALL cells splits the selected space into global coordinate components. Every actual row/column restricts to an ONB on each component. Projector spans add over these components. Singleton components are exactly the full multiplicity8-ray set; two-dimensional nonclassical components are prohibited by ISOLATE2.

Write MATCH for the supported physical fact: two distinct ray matchings on the same m rows/columns which are ONBs of the SAME m-dimensional space in EACH of the other FOUR full mates force m>=6. Those same-space ONBs are always derived below, never assumed from projected vectors.

### 3.2 A finite-channel lemma; the number three was not essential

Let B be a coordinate two-space, with its actual E-coordinate ray pair beta0. Let c_j be distinct orthogonal coordinate rays in B-perp and assign to each ONE noncoordinate B-ray b_j. Suppose EVERY actual selected cell is B-pure, B-perp, or genuinely mixed in ONE plane span(b_j,c_j), and at least one mixed cell occurs. Then the physical five-family is impossible. This proof applies in particular to FOUR channels, needed for a six-component; it is not inferred merely by changing a bound in an earlier statement.

Give each B-active cell its unordered B-ray pair beta={b,b-perp}. Selected vectors from different beta classes have NONZERO cross overlap. Their B factors have nonzero overlap, and they cannot share an outside c_j since that axis has only one assigned B-ray. Thus no outside cancellation occurs. An actual row's B-active vectors all have the SAME beta; the same is true for a column. Let n_beta count its rows.

For any full mate, the actual spans V_beta on different classes are perpendicular. Choose w in B nonorthogonal to every occurring B-direction. Equation (E) is a sum of positive operators with those mutually orthogonal supports, so each class sum is the identity on V_beta. Its trace is n_beta: each class row resolves I_B. Therefore dim V_beta=n_beta in EVERY mate. Column traces give the same column count.

The actual reference class beta0 contains NO mixed channels, since all b_j are noncoordinate. Its two pure B-rays occur once per class row and column. Their actual matchings are ONBs of V_beta0 in all four mates; MATCH gives n_beta0>=6.

Choose an occurring channel j, with beta=beta_j. Restrict (E), now w=b_j, to V_beta. Only pure-b_j cells and channels whose B-ray is parallel to b_j contribute. The full mate spans of these categories are perpendicular: the selected factors have a common nonzero B-direction and distinct outside axes. Their weighted operators sum to the identity on V_beta.

Every row using a channel contains exactly TWO genuinely mixed vectors forming an ONB of its fixed plane. The B-to-c_j row-resolution entry cannot be canceled by a different channel, so one mixed vector is impossible; more than two orthogonal vectors in the same plane is impossible. Split these rows by their unordered orthonormal ray-pair in that plane. Different pair classes have all cross selected overlaps nonzero and hence perpendicular full mate spans. A class on ell rows contributes trace ell in the b_j expectation. The positive-operator saturation consequently makes its actual mate span ell-dimensional. Its two repeated rays yield ell-cell matchings, ONBs of that SAME space in every mate. MATCH gives ell>=6 and hence n_beta>=6.

But beta!=beta0, and sum_beta n_beta=8. Contradiction. The proof used only finitely many channels, not m<=3. Arbitrary B-perp vectors, outside-edge activity and all four unrestricted mates remain allowed.

## 4. Sparse-block uncertainty and zero slack

### 4.1 One-zero3 geometry

For a one-zero3 block on B+c, B is the coordinate pair supporting the actual two-support basis ray w. The other two basis vectors form a genuine mixed ONB in span(b,c), where b is the B-ray perpendicular to w. Both coordinates of b and w are nonzero. Its real off-diagonal plane is the direct sum of ONE pure B-edge direction and ONE fixed real b-to-c cross direction. In particular its only nonzero PURE-edge directions are on B. The B-coordinate columns of that transition have degree3; the c column has degree2.

This follows directly by taking the off-diagonal parts of the three projectors: the two mixed cross parts are opposite, and P_w+P_b is the diagonal projection onto B. Complex phases are not normalized away. Likewise, a nonzero intersection of planes on two different triples can occur only on their common coordinate pair; existence of that pure-edge direction makes both blocks one-zero at their respective extra coordinates.

### 4.2 Z4: a zero-matching4 block is globally isolated

Align the zero-matching block on A so U_ii=0 and all other entries are nonzero. A vector in A with one E-coordinate has three F-coordinates. A vector with exactly two E-coordinates i,j has nonzero F coefficients i,j. For the complementary indices k,l, the restrictions of F_k,F_l to {i,j} are nonzero orthogonal two-vectors: their full inner product has no terms at k,l because of the matching zeros. Thus both remaining F coefficients cannot vanish simultaneously. A two-E-coordinate vector in A has at least three F-coordinates as well.

Any actual selected vector crossing A would have only one or two E-coordinates in A, since its total E support is at most3. Its A part would already occupy at least three F-coordinates, and its nonzero A-perp part adds another. This contradicts the physical degree3 bound. Hence A is a GLOBAL four-component. This is a complex argument, independent of a projector-span bound.

### 4.3 F3: a full3 block cannot belong to an irreducible component of dimension>=5

Suppose E-to-F has a full3 block on A and the containing global component has dimension>=5. Some actual vector v crosses A. Its A part cannot have one E-coordinate, which alone has three F-coordinates. Thus v has two A coordinates and one outside axis e. The A part has at least two F-coordinates (otherwise it would be an F-ray with only two E-coordinates, contradicting full3). Therefore e must be an F singleton, or v would have F degree>=4.

Take an ACTUAL line basis G containing v. Its E-to-G component is a3-block or a zero-matching4 block. The latter is globally isolated by Z4 and would force the whole component containing A to have dimension4. Hence G has a3-block on B+e, where B is the two-coordinate part of A used by v. The remaining A coordinate c cannot mix outside A in another G vector: it would again have three F-coordinates plus an outside coefficient. Thus c is a G singleton.

Both F,G preserve A+Ce. Their transition there is connected: the G c-axis overlaps all three F A-rays, and a mixed G vector joins the F e-axis to those rays. S3 forces a zero-matching4 block, which Z4 makes globally isolated. Contradiction. Thus dimensions>=5 have only singleton, full2 and one-zero3 blocks in EVERY pair of actual frames.

### 4.4 NEW zero-slack lemma for a minimal component

Let an irreducible component have dimension d and local projector span EXACTLY 2d-1. Let S be that real span and E its reference diagonal basis. Every collection U of ONBs whose projectors lie in S and which includes E has

`dim span(U)=2d-c(U)`,                                    (ZS)

where c(U) is its coordinate-component count.

Proof: the general ONB component lemma gives the lower bound 2d-c(U). Continue adding all actual line bases. The incremental proof of that same lemma, starting with U, pays at least c(U)-1 additional dimensions to make the final graph connected. Thus the final span2d-1 is at least dim span(U)+c(U)-1. Both bounds force equality. No actual degree bound is applied to an artificial frame.

This permits selecting individual actual transition blocks: keep that block's basis and use E-axes elsewhere. Their projectors lie in S. It also permits an artificial two-basis completion of any actual two-support ray v: on its pair the orthogonal-ray projector is Pi_pair-P_v, again in S. Consequently adding a new block or such an edge INSIDE an already connected partial support may not increase its off-diagonal span. This is an exact span statement, not an assumption that arbitrary S-projectors are actual cells.

## 5. NEW theorem: the irreducible six-space b11 is impossible

Suppose for contradiction d=6, b=11. Its real off-diagonal space L has dimension5. F3/Z4 imply that all actual transition blocks are singleton/full2/one-zero3. The local LIGHT input supplies at least one heavy3 block. Fix the reference E throughout this proof. A heavy support means the coordinate triple of an actual one-zero3 transition block.

### 5.1 Two heavy triples cannot intersect in exactly one coordinate

Suppose A=B+c and T=D+c, with B,D disjoint pairs. Their union has five coordinates; call the sixth e. Each block must have its zero at c. Indeed a heavy vector of T has one A-coordinate c and nonzero outside-A part. If the A block's c column had degree3, it would have degree>=4 in the actual A-block frame. Thus c has degree2 there, precisely the one-zero location. The reverse argument gives the same conclusion for T.

Their off-diagonal planes are therefore:

- one B-edge and one fixed noncoordinate b-to-c channel;
- one D-edge and one fixed noncoordinate d-to-c channel.

They are independent, spanning a four-space L0 on those five coordinates. Because the full six-component is connected, L has a nonzero e-to-core image. Since dim L=5, that image is exactly ONE REAL dimension and the kernel is exactly L0.

Every actual vector genuinely crossing e/core therefore has its core part parallel to ONE fixed ray u. It lies in span(u,e). In any actual row containing one such vector, the e-to-core off-diagonal resolution forces a second genuinely mixed vector; orthogonality allows at most two in that plane. They form an ONB of the plane. Their projector sum is P_u+P_e, so P_u belongs to S and Off(P_u) belongs to L0.

Since a mixed vector has E support<=3, u has one or two core coordinates. If it has one, it can only be c: either B coordinate has degree3 in the actual A-block frame, and either D coordinate has degree3 in the actual T-block frame; mixing one with e would give degree>=4. If u has two coordinates, Off(P_u) is a pure-edge direction of L0, so its support is B or D by §4.1. In that case it has both coordinates nonzero.

Subtracting the old P_u off-diagonal part from a mixed projector shows that L is L0 plus ONE PURE cross direction between e and u. Thus choose B as the channel two-space. If u=c or u is in D, all new activity is B-perp; B has its original single channel to c. If u is in B, it adds one fixed noncoordinate B-channel to e. In either case EVERY B-active actual vector is B-pure or in one of those channels. There are no B-to-D coherences; and an active noncoordinate B part already uses two E coordinates, so at most one outside coordinate is possible at degree3.

The finite-channel lemma of §3.2 contradicts this full physical configuration. Therefore no two heavy triples have intersection1.

### 5.2 If heavy triples do not overlap in two coordinates, a channel is already global

Now distinct heavy triples have intersections only0 or2. First suppose none intersects another in2. They are disjoint (at most two on six coordinates). Choose A=B+c. All actual blocks on the SAME A have the same off-diagonal plane by (ZS): the first such block already connects A and spans its required two dimensions.

There is no actual two-support ray on a B-coordinate and an outside-A coordinate: in the actual A-block frame its B-coordinate expands to degree3, plus the nonzero outside part. There is also no actual two-support ray on a B-coordinate and c: its pure edge is not in the one-zero3 plane, and its artificial two-basis completion would add a new direction inside the already connected A, contradicting (ZS).

Any B-active weight3 cell lies in a heavy block, necessarily on A because all the other heavy triples are disjoint. Thus every B-active mixed cell is in the ONE fixed b-to-c channel. Arbitrary B-perp cells are harmless. The channel lemma gives a contradiction.

### 5.3 If two heavy triples share a pair, all heavy activity has that common pair

Take A=B+c and T=B+d. By (ZS), their off-diagonal planes span exactly3 dimensions on the four connected coordinates. Their intersection is a nonzero pure B-edge line, so both blocks are one-zero at c,d. Their sum is the B-edge plus fixed noncoordinate channels from B to c and d.

A third heavy triple INSIDE those four coordinates but different from A,T would contain c,d. Its heavy projector has nonzero c-d coherence, absent from the old three-space. Adding that plane without changing the partial coordinate component would violate (ZS). Hence no such triple occurs.

Let the two remaining coordinates be e,f. Any heavy triple outside those four must intersect BOTH A,T in0 or2, never1 by §5.1. An elementary support case split now forces it to be B+e or B+f: a triple with exactly one B coordinate meets one of A,T in1 unless it lies inside the old four; a triple with no B coordinates contains c or d and meets the corresponding old triple in1. A triple disjoint from both cannot fit in only {e,f}.

For each occurring B+j, (ZS) forces its two-plane to meet the already connected B-edge in one real dimension. Thus it is one-zero at j, with ONE fixed noncoordinate B factor b_j. Multiple blocks on the same support cannot add another direction or B factor, again by (ZS).

No actual two-support ray touches a B-coordinate and an outside axis. For c the old A plane and (ZS) exclude its pure edge; for any outside-A axis the degree3 expansion in the actual A-block frame excludes it directly. Hence every B-active cell is B-pure or genuinely mixed in one of the at-most-FOUR planes span(b_j,j), j among c,d,e,f. Every assigned b_j is noncoordinate, and there is only one per outside axis. All outside-edge activity is B-perp. The four-channel lemma gives the contradiction.

The three cases exhaust all possible families of heavy supports. Therefore an irreducible six-component of span11 is impossible. QED.

**Boundary:** this theorem does NOT exclude a six-component of span12, a seven-component of span13, or five-/four-components one dimension above their earlier minimal bounds. Its proof depends on the exact zero-slack equality b=2d-1. The single-overlap core argument uses a SINGLE sixth coordinate and is not extrapolated to dimension7.

## 6. Consolidated q3 fixed-cell compression theorem

This section supplies the earlier four-stratum/all-a12 results by written proof, not the unadmitted parameter enumeration.

### 6.1 Fixed matching incidence and actual range projections

The two classical mates, rows and columns form an actual four-net. Every selected global fixed-ray matching M_(s,i) meets each net line once. For another member t, its FULL vectors on M_(s,i) form an ONB of C^8. Such a basis must contain every global fixed ray of t exactly once. Therefore any two fixed matchings from different quantum members meet in EXACTLY one actual cell.

Let p=J/64 and E4=I-sum_(four net classes)R_i+3p, an orthogonal projection of rank35. Let T_s=H_s/8-p be the three quantum covariance contractions, and Q_s their ORTHOGONAL RANGE PROJECTIONS. They have perpendicular ranges inside E4 and rank a_s-1. Thus

`L=E4-Q_1-Q_2-Q_3`

is an orthogonal projection of rank d=38-sum a_s, in {0,1,2}. This L is not a covariance contraction assumed idempotent.

For fixed cells x,y of member s,

`Q_s[x,y]=(1/8)1_(same fixed ray)-1/64`.

On the c cells fixed in all three members, L has diagonal7/32 and off-diagonal3/32 or -1/32, according as the two cells share none or one of the seven available lines. Any principal matrix of size<=3 is positive definite (multiply by32: diagonal7, off-diagonal absolute value<=3). Therefore c<=d.

If f_s are the fixed-ray counts, the number of cells fixed ONLY in s is

`N_(1,s)=f_s(8-f_t-f_u)+c >=0`.                          (COUNT)

In particular any pair summing above8 forces at least f_s triple cells for the third member. For f=(4,4,4), c=1 would yield exactly3 single-fixed cells. Each of the four net lines through the triple point needs another odd-fixed point, because each net line has12 fixed incidences. Those four points must be distinct. Thus c=1 is impossible in that case.

### 6.2 Exact six-class matrix and known constant

Let A_s be the orthogonal Gram-range projection of the selected RESIDUAL projectors, supported on its 8r_s residual cells Z_s. Its rank is b_s and it contains the normalized constant `1_Z/sqrt(8r_s)`. A_s is perpendicular to L. On the n=f_t f_u-c cells D_s which are fixed in t,u but residual in s, the compression of the projection A_s+L, of rank m=b_s+d, is EXACTLY the matrix K with

`K_xx=11/32`,

`K_xy=-1/32` for a common line among the four net classes and the two other fixed-ray classes,

`K_xy=3/32` otherwise.

This follows by substituting the two actual fixed-block formulas into E4-Q_t-Q_u+p. Distinct cells share at most one of those six lines.

With e the ORDERED line-sharing pairs,

`tau=tr K=11n/32`,

`sigma=tr K^2=[121n+9n(n-1)-8e]/1024`.

For n=8w+v, 0<=v<8, set `g8(n)=(8-v)w(w-1)+v w(w+1)`. Balanced integer occupancies minimize ordered pairs among eight lines. Deleting c points from the f_t-by-f_u intersection grid removes at most 2c(f_t+f_u-2) ordered pairs. Hence

`e>=e_min=(f_t f_u-2c)(f_t+f_u-2)+4g8(n)`.

Finally let mu=n/(8r_s). In an orthonormal basis for range(A_s+L) starting with the known residual constant, the matrix of restriction to D_s has first diagonal entry mu, trace tau and squared trace sigma. Splitting off this first coordinate and applying Cauchy–Schwarz to the remaining block gives

`sigma>=mu^2+(tau-mu)^2/(m-1)`.                          (CONST)

The compression need not be a projection. The simpler rank bound is rank K>=tau^2/sigma.

### 6.3 Complete old four-stratum cases

Imported component bounds and uniform12 give allowed f-values: a12 has f4/5; a13 has f2..5; a14 has f1..5. f0 costs at least15, f1 at least14, f2/3 at least13; f6/7 cannot be nonclassical after taking ALL fixed rays.

**Selected a14/f4 or f5.** The other spans are12,12, so d=c=0 and their f>=4. COUNT prohibits any pair with sum>8; f5 is impossible. For f4 all f-values must be4. Then n16, e_min160, tau11/2, sigma<=11/4 imply rank K>=11, contradicting b10. This excludes f4/b10 and f5/b9.

**Selected a13/f4 or f5; other spans12,12.** Here d=1. Any f5 forces c>=4>1, so all f4. c1 is excluded by the four-net parity argument. For c0 the same rank>=11 contradicts b+d=9+1=10.

**Selected a13/f4 or f5; other spans13,12.** Here c=d=0. f5 is impossible because the a12 member has f>=4. For selected f4, that member must have f4. The other a13 fixed count is2,3 or4:

- f4 gives the sixteen-point rank contradiction;
- f3 gives n12, e_min92, tau33/8, sigma<=119/64, so rank>=1089/119>9;
- f2: select THAT member, with r6,b11,m11,n16. CONST would require `(1/3)^2+[(11/2)-(1/3)]^2/10=1001/360>990/360=11/4`. Contradiction.

This exhausts the a13 cases and excludes f4/b9 and f5/b8. The same sixteen-point CONST also excludes a14/f3, since r5,b11,m11 gives `2761/1000>2750/1000=11/4`.

### 6.4 All three spans12 are impossible

Now d2 and all f>=4. An f5 forces c>=4>2, so all f4. At c0 the rank>=11 contradicts b+d=8+2=10. At c1 the parity argument applies. At c2, n14 and e_min120 yield tau77/16 and sigma<=593/256. But m10,mu7/16 in CONST give

`(7/16)^2+[(77/16)-(7/16)]^2/9=5341/2304>5337/2304=593/256`.

The strict difference is1/576 by the displayed integer numerators. Thus this span triple is excluded. No interpreter is invoked for these written identities.

## 7. NEW consequence: the remaining f5/b7 stratum is excluded

A selected f5/b7 has a12. It cannot have another a12 member: together their f-values sum to at least9. If the third span is14, c=d=0, contrary to COUNT and positive third f. If the third span is13, d1 but its f>=2 forces c>=2. If the third span is12, d2 but the third f>=4 forces c>=4. Thus both other spans are13 and c=d=0.

By the a13 exclusions their f-values are2 or3. If both are3, the selected nine-point compression has tau99/32 and sigma<=1385/1024; hence rank>=9801/1385>7 because `9801>7*1385=9695`. That contradicts b7.

In either remaining choice (2,2) or (2,3), an a13/f2 member has residual dimension6 and span11. It cannot split into3+3, since the two imported local bounds give span at least6+6=12. Two-components are impossible. It is therefore an IRREDUCIBLE six-component of span11, prohibited by §5. This excludes the entire remaining f5/r3/b7 stratum, without a three-space real-form assumption or a full-array enumeration. QED at the named physical imports and the NEW written six-space theorem.

## 8. Deriving and honestly retaining the four remaining q3 patterns

All nonclassical spans lie in12..14 and sum<=38. The possibilities are (14,12,12), (13,13,12), (13,12,12), (12,12,12).

- For a12, f is4 or5, and §7 removes5, so f4.
- For a13, f2 would be the prohibited six-space, while f4/5 were excluded by §6. Thus f3 only.
- For a14, f3/4/5 were excluded by §6, leaving f1 or2.
- The all-a12 triple is excluded.
- In (14,12,12) and (13,13,12), d=c=0.
- In (13,12,12), the f-values are3,4,4. Here d1. c0 is excluded by selecting the a13/f3 member: its b10 plus d1 gives m11, n16, mu2/5, and the same `2761/1000>11/4` contradiction. Thus c1.

This proves exactly the four necessary rows in §1 by written cases. Every q3 family still has an f4/r4/b8 member, but NONE of those four rows has been ruled out or constructed here.

Precise geometry still missing:

1. **(14,1)** contains an irreducible seven-space of span13: splitting3+4 would already cost6+8=14. Its zero-slack problem has TWO outside coordinates beyond a five-coordinate single-overlap core. The one-dimensional outer-coherence step of §5.1 does not extend automatically.
2. **(14,2)** has residual span12 in dimension6. It can be irreducible6 or split3+3. The exact zero-slack equality used in §5 fails in the irreducible case; a new internal coherence direction is not excluded. The split case is not silently treated as one six-space.
3. **(13,3),(13,3),(12,4)** contains two irreducible five-spaces of span10. Their off-diagonal spaces have one surplus direction over the minimal connected lower bound. Z4/F3 prohibit full3/zero4 blocks there, but do not prove unique channel coverage.
4. **(13,3),(12,4),(12,4), c=d=1** adds a rank-one leftover projection to that five-space/six-class coupling. The c1 incidence cannot be replaced with the c0 parity/rank argument. Its unknown full-cell equations remain.

The ONE next attack representation is therefore **one-surplus-direction channel collision**, encompassing the irreducible6/b12 and5/b10 rows and the rank-one-L row, with seven-space exact-zero-slack treated as its separate literal branch. No proof of that representation's global unique-factor conclusion is supplied. In particular two different B factors at the same outside axis or an extra coherence inside an already connected partial support cannot be dismissed when zero slack fails.

## 9. Acceptance, review and unchanged historical gates

This manuscript consolidates the existing three addenda and one substantive NEW six-space theorem; it does not claim that the v31 review of the older packet reviewed §5 or §7. Required reconstruction includes:

- the full corrected covariance/range distinction and six-class constant bound;
- Z4/F3's actual-frame support arguments;
- (ZS) for artificial ONBs whose projectors lie in S, without applying physical degree bounds to those frames;
- §5.1's one-dimensional outer coherence and actual-row two-vector saturation;
- §5.2/5.3's exhaustive heavy-support alternatives and all actual two-support rays;
- the finite-channel proof for four axes and all full mates;
- the new f5/b7 consequence and exact four-row frontier.

All are AUTHOR-WRITTEN until actually reconstructed. Earlier unadmitted eval results supply no executable or independent verification. Same-harness written support would not be proof-kernel/human/cross-vendor/novelty acceptance.

A10 remains UNSATISFIED at GB15/18: P1-B2.M2, P1-B2.M4, P1-B3.M2 remain UNKNOWN. Physical exclusions do not imply UNSAT of Boolean necessary-condition overapproximations. A11 remains UNSATISFIED/OPEN: this does not finish q3, q1/q2, global classicality or final adoption of any conditional legacy route. The detailed source/read/polarity assessment remains `A10-A11-written-barrier-v2.md`. No original input, proof stream, runtime qualification, child-exit attestation or permission error is repaired here.

All outputs stay in this owned root. No author/shared/pinned file is edited, no scientific GO exists, and the original October27 deadline is unchanged.
