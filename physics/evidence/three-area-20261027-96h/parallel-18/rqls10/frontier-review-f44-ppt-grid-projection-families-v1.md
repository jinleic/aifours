# f44 — independent exact review of the grid-state projection families

Reviewer **PhysicsRQLS10-2**, physics-5. Native `/bin/date` immediately before writing: **Wed Oct 28 17:38:49 PDT 2026**. **Verdict: FATAL0 / MAJOR0 / MINOR0 — NO SUBSTANTIVE DEFECT AT EXACT CANDIDATE SCOPE.** The actual 4×5 state, its full partial-transpose certificate/SN3 argument, five computational projections and the ALL-complex-kernel-line family are reconstructed below. The observed source-polynomial identity error is correctly disclosed and repaired by the candidate; it is not a new defect in these two candidate files.

The conclusion is about one explicit 4×5 state and specified local maps. It does **not** show SN<=2 for arbitrary rank-four projections, arbitrary 4×4 PPT states, or the original 4×4 SN>=3 problem. Same-harness written review plus exact computer arithmetic is not a formal/kernel, human, configured-independent-model, source-novelty or original-target acceptance.

## 1. Actual inputs, prior contact and independent checks

Read `review-waves/f44-ppt-grid-projection-families/assignment-v1.json` ENTIRELY FIRST. Then read BOTH candidate files completely through their closing braces:

1. `frontier-20261028-grid-state-five-projections-v1.json`, **24 LF**, SHA256 **9863760e2ca2331164d12e62300f3ad7db5b6a17a3ef424e360d504d541004a9**.
2. `frontier-20261028-grid-all-two-column-compressions-v1.json`, **33 LF**, SHA256 **4076912f4e4197244483b47eaa7d6e5d09207386840929db1d04814332ff9406**.

Read the registered literal original `physics-3-ppt-sn3-definitions-v1.md`, **9 LF**, SHA256 **eecd40e6e864ac0e13212543ffb2916a9799f7457dc9cd7c35b6537316ceaceb**, and matched all three live hashes. Read the named primary Krebs–Gachechiladze [arXiv:2509.07086v1](https://arxiv.org/html/2509.07086v1), specifically its displayed range matrix (11), five polynomials (12), and immediately following polynomial identity. This confirms what the candidate calls the printed source identity; it is not a complete external source/novelty audit.

Prior contact: I reviewed an earlier physics-3 minimum-face union in w83 and had HELD w96 caps exposure, neither of which is a proof premise here. The current prospective owner direction permits independent work, not retroactive validation of earlier held material or a clean-cognition certificate. No target-author contact, old mixed/held body or author's checker/result was used as evidence; candidate-reported checks are separately identified as reports.

New independent checker `frontier-review-f44-grid-exact-check-v1.py`, SHA256 **0cb8520a9ee3ccd4ca291d3d443727b037a397fad2ec38f584dddea4cd905d10**, builds the actual state and all projected kets from scratch using pairs of `fractions.Fraction` for Gaussian rationals. Its symbolic range-minor step uses the separately written polynomial helper `frontier-review-f8-exact-check-v1.py`, SHA256 **5ae7a6ae0864dc439827e7ab6de2825f21fcfaafd006dd3530638ecf6157b6a0**, not an author script. It checks all400 original PT entries, all40 symbolic 3×3 minors for the listed five identities, all five projected ranks/traces, both j3/j4 complete 256-entry decompositions and all six stated Gaussian-rational K samples including all16 twirl kets' 3×3 minors and256 matrix entries.

Actual command: `python3 frontier-review-f44-grid-exact-check-v1.py`. The initial run failed at Python parsing because of a missing sample-list parenthesis; it performed NO checks. I corrected that local new checker and reran. Actual corrected-run output, **Wed Oct28 17:38:30 PDT 2026**:

```text
PASS 4x5 state trace=31 rank=9, PT=10 positive projectors entrywise, PT rank=10
PASS all five are actual 3x3 minors; corrected 2a^4 identity and primary residual exact
PASS five projections exact traces [23, 28, 23, 25, 25] ranks [8, 9, 8, 8, 8] PT ranks [9, 10, 9, 9, 9]
PASS j=0,1,2 direct rank<=2 and j=3,4 twirl rank/minor + full 256-entry decompositions
PASS large u (1,0) v (2,0): 16 rank2 twirl kets + nonnegative residuals + 256 exact entries
PASS large u (1,0) v (0,0): 16 rank2 twirl kets + nonnegative residuals + 256 exact entries
PASS large u (1,1) v (1,-1): 16 rank2 twirl kets + nonnegative residuals + 256 exact entries
PASS small u (0,0) v (1,0): 16 rank2 twirl kets + nonnegative residuals + 256 exact entries
PASS small u (1,0) v (2,0): 16 rank2 twirl kets + nonnegative residuals + 256 exact entries
PASS small u (0,1) v (3,0): 16 rank2 twirl kets + nonnegative residuals + 256 exact entries
PASS all six Gaussian-rational compression samples; no universal claim from sampling alone
```

Here a pair `(p,q)` means `p+i q`; the actual script prints each component as `Fraction`. These finite checks corroborate the stated samples. The ALL-complex claim below is instead established by exact rank/twirl/weight identities valid for arbitrary complex u,v.

## 2. The actual 4×5 state and PPT certificate

Write `[v]=|v><v|` and use the given fixed computational labels. Let

`A=|00>+|11>+|22>`, `B=|01>+|12>`, `D=|10>-|21>`,

`C=|02>+|34>`, `E=|20>+|33>`, `F=|23>`, `G=|30>`, `I=|32>`, `H=|04>`.

The SAME unnormalized state is

`R=[A]+[B]+[D]+3([C]+[E]+[F]+[G]+[I]+[H])`, `rho=R/31`.

Its nine generating vectors have pairwise disjoint nonempty computational supports, hence are orthogonal and linearly independent. Their norm-squared sum with the stated weights is31, so R>=0, trace31 and rank9. Its range is exactly the original matrix family

```text
[a  b  c  0  h]
[d  a  b  0  0]
[e -d  a  f  0]
[g  0  i  e  c]
```

for arbitrary complex a,b,c,d,e,f,g,i,h, not just real coefficients or a selected slice.

Partial transpose on Bob is exactly

```text
R^Gamma = [01+10]+[12+21]
          +(1/3)[3*02+11+20]+(2/3)[11-2*20]
          +3[04+32]+3[23+30]+[00]+[22]+3[33]+3[34].
```

Every displayed coefficient is nonnegative, so its right side is positive semidefinite. The independent exact code verified ALL400 entries of the equality and its rational rank10; no positivity of a partial transpose is assumed merely because R is positive. Therefore rho is an actual normalized PPT 4×5 state.

## 3. Exact complex range/minor SN3 argument and source correction

For the full nine-parameter range matrix, the following are actual 3×3 minors (row/column indices below are0-based):

- `g1=e(a²-bd)`, rows(0,1,3), columns(0,1,3);
- `g2=c(a²+bd)`, rows(1,2,3), columns(1,2,4);
- `g3=e(b²-ac)`, rows(0,1,3), columns(1,2,3);
- `g4=-c(d²+ae)`, rows(1,2,3), columns(0,1,4);
- `g5=a³+b²e-d²c-ace`, rows(0,1,2), columns(0,1,2).

The independent symbolic checker searched all40 actual minors and verified each identity and

`2a(g5-g3-g4)-c*g1-e*g2=2a^4`.

Hence if a range vector has complex Schmidt rank<=2, all five minors vanish and a=0. This is a polynomial implication over C, including arbitrary zero parameters; no numerical sampling or real-only restriction is used. But A belongs to range(R) with a=1. In any positive rank-one decomposition of R, each summand vector lies in range(R): for w in ker R, `0=<w|R|w>` is a sum of nonnegative squared overlaps, hence each summand is orthogonal to ker R. If R had an SR<=2 ensemble, its range would be contained in the hyperplane a=0, contradicting A. Thus SN(rho)>=3. The displayed defining sum has generators of rank at most3, so SN(rho)<=3 and **SN(rho)=3**.

The source's published line after Eq.(12) instead states `a(g5-g3-g4)-c*g1+e*g2=a^4`. Direct symbolic expansion gives its left-minus-right residual `a²ce+2bcde`; at the explicit tuple (a,b,c,d,e)=(1,0,1,0,1), left=2 and right=1. Therefore that particular printed identity is false as written. The candidate's corrected identity above is exact and proves the intended simultaneous-minor implication; the published existence theorem is NOT declared false merely because one displayed identity needs correction. This is a source-specific arithmetic finding, not a novelty or complete source audit.

## 4. Five computational projections, all original vectors retained

For j=0,...,4 let P_j remove Bob coordinate j and `R_j=(I tensor P_j)R(I tensor P_j)^*`, then identify the remaining four Bob coordinates in their original order. Positivity is immediate and PPT follows from the actual local-map formula

`R_j^Gamma=(I tensor conjugate(P_j)) R^Gamma (I tensor conjugate(P_j))^* >=0`.

For j=0,1,2, projected A has two nonzero terms, and every other originally listed generator has Schmidt rank<=2. Their SAME positive weighted sum therefore gives SN(R_j/tr R_j)<=2 directly. No claim of entanglement or exact SN for these three is made. Independent exact traces/ranks/PT ranks are respectively

```text
j=0: trace23, rank8, PT rank9
j=1: trace28, rank9, PT rank10
j=2: trace23, rank8, PT rank9.
```

For j=3, with original Bob labels retained before the final identification, set for z^4=1

`q_z=z A+B-z² D-z³|20>`.

After the projection, its Alice row2 is z times row1, while row3 is zero, so SR(q_z)<=2 for EVERY fourth root z. Summing the four phase projectors cancels all nontrivial characters:

`(1/4)sum_z[q_z]=[A]+[B]+[D]+[20]`.

The SAME projected R is

`R_3=(1/4)sum_z[q_z]+2[20]+3([C]+[30]+[32]+[04])`.

All terms are nonnegative and SR<=2; trace25, rank8, PT rank9. The explicit coefficient-row statement is at the post-j3 projection, not an assertion about the unprojected q.

For j=4, similarly

`q'_z=z A+z² B-D+z³|02>`.

After the projection, coefficient column2 is z times column1, column3 and Alice row3 of q' vanish; SR(q')<=2. The four-phase identity is

`(1/4)sum_z[q'_z]=[A]+[B]+[D]+[02]`,

and

`R_4=(1/4)sum_z[q'_z]+2[02]+3([E]+[23]+[30]+[32])`.

Again all terms are nonnegative SR<=2; trace25, rank8, PT rank9. The independent Fraction/Gaussian checker verifies every3×3 minor for each phase ket and all256 entries of EACH projected decomposition. The twirl is finite and exact, not a statement inferred from sampling random complex phases.

## 5. Both j3 and j4 are entangled — exact range witness

Project either R_3 or R_4 further onto Alice and Bob coordinates0,1,2. The SAME nonzero unnormalized 3×3 state is

`T=[A]+[B]+[D]+3([02]+[20])`,

whose range consists of the matrices

```text
[a  b  c]
[d  a  b]
[e -d  a].
```

A rank-one matrix has both 2×2 minors `a²-bd=0` and `a²+bd=0`, so 2a²=0 and a=0 over C. Yet A belongs to range(T) and has a=1. A positive separable decomposition would have all product vectors in range(T), forcing their span inside a=0 and excluding A, contradiction. T is therefore entangled. A local projection of a separable state is separable (possibly zero); here T is nonzero. Thus R_3 and R_4 are each entangled. Combining with their explicit SR<=2 decompositions gives **SN exactly2** for those two normalized projections. PPT was separately established; no NPT implication is being substituted.

## 6. ALL complex rank-four maps with kernel in the last-two-coordinate plane

Let K:C5->C4 have rank4 and ker K a line contained in span{|3>,|4>}. K is injective on span{|0>,|1>,|2>}, while the image of span{|3>,|4>} is a one-dimensional line independent of those three images. An invertible output basis change therefore writes `K=H K_(u,v)`, H invertible, where

`K_(u,v)|0,1,2>=|0,1,2>`, `K_(u,v)|3>=u|3>`, `K_(u,v)|4>=v|3>`, `(u,v)!=(0,0)`.

Invertible local congruence preserves PPT in both directions (`Gamma_B` replaces H by conjugate(H)) and preserves pure Schmidt rank and hence Schmidt number in both directions. Trace is positive after K since the state has nonzero surviving 3×3 core. Thus it suffices to prove the normal form; no noninvertible output reduction is confused with an equivalence.

Write primes for the SAME K_(u,v)-projected generators and `R_uv=(I tensor K_uv)R(I tensor K_uv)^*`. The ALL-pairs formulas are as follows.

### 6a. Exact finite local-unitary twirl

For `z,w in {1,i,-1,-i}`, let

`U_A=diag(1,z,z²,w)`, `U_B=diag(1,z^(-1),z^(-2),z²/w)`.

These are actual local unitaries on the4×4 output. For any q, define `T(q)=(1/16)sum_(z,w)[(U_A tensor U_B)q]`. By the character sums of the finite group `(Z/4)^2`, distinct characters are orthogonal and mixed terms vanish. The actual projected generators have characters

```text
A':1, B':z^-1, D':z, C':z², E':z²,
F':w^-1, G':w, I':w z², H':z²/w.
```

The only repeated character is C'/E'. Neither seed below contains BOTH, so its twirl equals precisely the sum of its individual weighted projectors. Local unitaries preserve Schmidt rank; proving the seed has rank2 proves this for every twirled ket.

### 6b. Case |v|<=2|u|, including v=0

Here u!=0 and p=v/u. The actual seed

`q_L=A'+B'-D'+C'+(3p/4)F'+(4/3)G'+(3/2)H'`

has coefficient matrix

```text
[ 1    1  1  3v/2 ]
[-1    1  1   0   ]
[ 0    1  1  3v/4 ]
[ 4/3  0  0    v  ].
```

Column2 equals column1, and column3 equals `(3v/4)(column0+column1)`. Columns0 and1 are independent for EVERY complex v (their first-two-row 2×2 determinant is2), so SR(q_L)=2, including v=0. Twirling and subtracting its nonnegative weights from the defining SAME R_uv gives the exact identity

`R_uv=T(q_L)+2[C']+3[E']+(3-9|p|²/16)[F']+(11/9)[G']+3[I']+(3/4)[H']`.

Since |p|<=2, the F' weight is at least3/4; all displayed residual weights are nonnegative and the residual projected generators have SR<=2. Thus this case has SN<=2, without assuming C',E' are orthogonal or ignoring their coincident twirl character.

### 6c. Case |u|<=|v|/2, including u=0

Here v!=0 and p=u/v. The actual seed

`q_S=A'+B'-D'-E'-2p G'+p I'+H'`

has coefficient matrix

```text
[ 1    1  0   v ]
[-1    1  1   0 ]
[-1    1  1   0 ]
[-2p   0  p  -u ].
```

Row2 equals row1, and row3 equals `-p row0+p row1` because u=pv. Rows0 and1 are independent for EVERY complex v, so SR(q_S)=2, including u=0. The exact same-object decomposition is

`R_uv=T(q_S)+3[C']+2[E']+3[F']+(3-4|p|²)[G']+(3-|p|²)[I']+2[H']`.

If |p|<=1/2, the G' and I' coefficients are respectively at least2 and11/4; all others are nonnegative. Every residual generator has SR<=2. This proves SN<=2 for this case.

Every nonzero complex (u,v) belongs to at least one case: if |v|<=2|u| use 6b, otherwise v!=0 and |u|<|v|/2 use 6c. The equality boundary is valid in BOTH; the two coordinate endpoints are explicitly covered. Independent exact replay checked the six author-stated samples including both boundary decompositions and genuinely complex values, but the ALL-complex conclusion rests on the symbolic matrix/character/weight proof just given.

## 7. PPT, normalization and entanglement for EVERY map in this family

For any complex K_uv, the actual PT satisfies

`R_uv^Gamma=(I tensor conjugate(K_uv)) R^Gamma (I tensor conjugate(K_uv))^* >=0`.

Both R_uv and its PT are positive. The trace is

`tr R_uv=19+6(|u|²+|v|²)>0`,

so normalization is legitimate for every nonzero pair (indeed the unnormalized expression is positive even at the excluded zero pair). Local projection onto Alice/Bob coordinates0,1,2 gives exactly the same nonzero entangled T of §5 for ALL u,v, since K_uv fixes the original Bob0,1,2 coordinates. If R_uv were separable, this local projection would be separable; contradiction. Hence **SN(R_uv/tr R_uv)=2** for the entire family. The final invertible H preserves both SN and PPT, so the statement holds for EVERY rank-four K with the specified kernel-line property, not only for the normal form or the six samples.

No statement is made about kernel directions outside span{|3>,|4>}, arbitrary local projections of other 4×5 states, any candidate 4×4 PPT/SN>=3 state, or global P44 closure. The result identifies a proper family of actual PPT entangled states of SN2.

## 8. Assurance and disposition

The source's displayed identity error is a genuine **source-specific** error but is explicitly identified and repaired by candidate1; it is not concealed or attributed to a false 4×5 theorem. The independent checker rederived all five minors and both the erroneous residual and corrected zero polynomial. It verified actual state/decomposition bytes and six stated exact samples, while the universal rank, twirl, positivity, projection and entanglement arguments are written in §§2–7.

No finite-sample check is promoted to an ALL-complex proof, no arbitrary-kernel reduction is assumed, no previous held outcome is a premise and no author contact occurred. Original 4×4 PPT/SN target, source priority/novelty and all stronger verification gates remain open. Actual earlier administrative/process records remain historical, not retrospectively changed.

**Final verdict: FATAL0 / MAJOR0 / MINOR0 — NO SUBSTANTIVE DEFECT at the exact stated source-state/projection-family scope.** Main must itself read both candidate bodies and this actual review before any adoption. I resume my own physics-5 research after returning this result.
