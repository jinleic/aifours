# f180 — PH7 exclusion at and above 83/100: independent same-harness review

**Reviewer:** ReviewF180PH7Above083. **Disposition:** scientifically ACCEPT the new Lemma 6, Lemma C3 and their exact z3 certificate; ACCEPT the all-topology PH7 exclusion for every z >= 83/100 conditional on the explicit adopted imports below. **Findings: 0 FATAL / 0 MAJOR / 2 MINOR** (one expository, one reviewer-process display deviation; neither is a mathematical blocker). Author diagnostics and historical run chronology are separately INCONCLUSIVE, non-premises.

This is a same-harness scientific review, not human review, independent-model-family review, formal/kernel verification, novelty/priority clearance, or proof that the imported caller/band is correct. I did not use an external model or execute/import either author Python program. An exact finite computation is evidence for the stated polynomial cover, not a claim of formal verification.

## 1. Freeze, source order and exact dependencies

The first opened source was `manifest-v1.json`. Its SHA-256 was **2acd4ca02d2b6555221c71a6d7d53005407090d39939123b8b6af45712e50658**, matching the task. All nine full input SHA-256/byte/LF triples were checked before substantive reading. I then read every input in this exact declared order, completely, before mathematical interpretation:

1. `frontier-20261029-ph7-closed-endpoint-and-f50-erratum-v1.md` — 2013 B / 14 LF; `a1cfbd816d04e03655b7461850e95df91e13b0e6fb081801f306bc1b4a719d8c`.
2. `frontier-20261029-ph7-f159-f160-minor-fixes-addendum-v1.md` — 6767 B / 39 LF; `a447c10752b9c876b8eaa9754ce5246bda11e40778f26bf98fa5c4fd345ac4d1`.
3. `frontier-20261029-ph7-eight-ninths-impossibility-v1.md` — 10157 B / 86 LF; `599feaa589a6281316786cdd4d19050a88ba2945a12ce253d5f04678e862b2d4`.
4. `frontier-20261029-ph7-shift-monotonicity-corollary-v1.md` — 3746 B / 37 LF; `dde16615ea1cfcc0dcac77ca5f3329cc947e58287e4c126b13979468b7a390e1`.
5. `frontier-20261029-ph7-impossibility-above-0p85-v1.md` — 7453 B / 75 LF; `a624b358c71e838963c8250bfb82af2e54b06f3bc886332abcc3891a3e24f133`.
6. `frontier-20261029-ph7-impossibility-above-0p83-v1.md` — 8991 B / 82 LF; `f9e9847de445dc8887c54ec29b72d34e579268b079dc8e146c1b357f7d6c67a5`.
7. `frontier-20261029-ph7-threshold-z3-check.py` — 19488 B / 323 LF; `802dfcdb686c85ab24166ffda1c8119f032536d4ff146dcf995bfdbf0fc34440` — read only, never run/imported.
8. `frontier-20261029-ph7-threshold-z3-certificate-v1.json` — **2072339 B / 213732 LF**; `b1946079fc0a380e77cdfd1e04dd9e88a6fac6e5379bf8dce65e0ef3acad6d10` — fully consumed by my own `json.loads`, without rendering the full JSON. See m2 for bounded extracted display.
9. `frontier-20261029-ph7-threshold-z3-integer-replay.py` — 18089 B / 301 LF; `3ccb226fa299de1307d6db51525035bb5783ba5df338fd9938a9053581d269c1` — read only, never run/imported.

All live input hashes/bytes/LF were subsequently rebound unchanged in `reviewer-f180-evidence-inventory-v1.json` (SHA-256 **cd066e02a35d19c28882c39fb2388ca73bb0377480861c5bd5c07b3589245cb9**). Its input paths are the exact absolute paths from the manifest; its artifact list gives every pre-report output name, size and hash.

### Conditional imports, precisely

- **Caller:** `frontier-20261028-ph7-global-irreducibility-v1.md`, SHA-256 **729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49**. Adopted, not an input and not opened/re-reviewed. For z > 1/2, it converts a PH representation with <=7 states to an irreducible 7-by-7 Metzler G with s(G)=0 and characteristic polynomial `y[(y+1)^2+z]^2(y^2+p y+q)`, p,q>0.
- **f159 Lemmas 1–4**, in input 3 with input 2's corrections: positive definiteness of `𝒜=-S` (using irreducibility and a non-real eigenvalue), geometric-symmetrization extra-cycle cover identity, coefficient identities through y^3, and Ky Fan. These are reviewed context, not renewed whole-file review targets.
- **Lemma S**, input 4 with input 2's supremum convention: the Perron-projector shift and rescaling preserves irreducible Metzler spectral realizability and lowers z. It is not an assertion of downward-closed PH realizability.
- **Lemma 5**, input 5: y^2 relation and its interlacing consequence `Y2b>=0`. Its older C2/certificate is not a finite-certificate dependency of this new proof.
- The new work checked here is **Lemma 6 + C3 + the z3 cover**, including independent reconstructions of inherited cases (a),(d) and crude contradictions in (b),(c). No unlisted no-two-cycle core, girth-four certificate, f161/f162, held/zero payload, sibling review or author regression file was opened. Their correctness is not silently imported to replace these reconstructions.
- Only the **lower endpoint** of a realizability-supremum bracket uses the adopted band/f50 assertion in mandatory input 1. The band itself was not supplied and was not re-verified. No PH8 construction is needed for the present exclusion theorem.

## 2. Claim-level verdicts

| Claim | Verdict | Exact dependencies / qualification |
|---|---|---|
| C1: Lemma 6, `E1=a3+b2+c1+W6-P33` and `Y1+>=0` | ACCEPT; 0F/0M | f159 Lemmas 1–4, coefficient extraction, interlacing; written reconstruction below, symbolic identities, exact regression control. |
| C2: C3's four-case reduction and NB/MC selector logic | ACCEPT; m1 exposition | Definitions below, Lemma 5 for Y2b, C1 for Y1+, elementary symmetric inequalities; no inaccessible core premise. |
| C3: all five z3 covers / all 26 rebuilt polynomials | ACCEPT; 0F/0M | Full JSON parse; independently defined rules; own direct per-leaf exact Bernstein/affine calculation; prefix/Kraft coverage; intended-reason negatives. |
| C4: no PH representation with <=7 states for any z>=83/100, all topologies | ACCEPT CONDITIONAL | Caller + f159 Lemmas 1–4 + Lemma S + Lemma 5 + C1–C3. No topology restriction introduced. |
| C5: supremum <=83/100 and closed-right bracket | ACCEPT type/upper bound; lower endpoint CONDITIONAL | C4 gives `sup Z7<=83/100`, not `<83/100`. Input 1 supersedes old lower-end wording, giving `[z_*,83/100]` if its adopted-band statement is imported. |
| C6: author execution chronology and §6 floating/kernel diagnostics | INCONCLUSIVE, non-load-bearing | I did not run author programs or inspect unlisted diagnostics. Matching counts/digests below do not authenticate their historical run times, numerical searches, novelty or priority. |

## 3. Written reconstruction of Lemma 6

Write `Wk=sum_{|C|=k} omega_C`, with the nonnegative extra-cycle weights of the adopted cover identity, and `v1<=...<=v7` the positive eigenvalues of `𝒜=-S`. Let `e_k=e_k(v1,...,v7)`. A principal submatrix `𝒜_U` has positive eigenvalues, because 𝒜 is positive definite.

The coefficient of y in `det(yI+𝒜_U)` is `e_{|U|-1}(𝒜_U)`. Consequently the cover's empty set contributes e6; one 3-, 4-, 5-, or 6-cycle contributes respectively `-omega e3(𝒜_U)`, `-omega e2(𝒜_U)`, `-omega tr(𝒜_U)`, or `-omega`. A pair can affect y only when it consists of two disjoint 3-cycles: its complement has one vertex and its contribution to y is `+omega_C omega_C'`. A 3+4 pair contributes only a constant; any larger pair, or three extra cycles, cannot contribute to y on seven vertices. Thus, defining `a_j=sum_{|C|=3}omega_C e_j(𝒜_U)`, `b_j=sum_{|C|=4}omega_C e_j(𝒜_U)`, and `c1=sum_{|C|=5}omega_C tr(𝒜_U)`,

`[y]det(yI-G)=e6-a3-b2-c1-W6+P33`.

The target y coefficient is `(1+z)^2 q`, so

`E1:=e6-(1+z)^2 q = a3+b2+c1+W6-P33`.

Here P33 sums unordered vertex-disjoint pairs of 3-cycles. All weights are nonnegative, so

`0<=P33 <= sum_{C<C'}omega_C omega_C' = (W3^2-sum_C omega_C^2)/2 <= W3^2/2`.

Cauchy interlacing for a size-m principal submatrix gives `v_i<=mu_i<=v_{i+7-m}`. Elementary symmetric functions are coordinatewise increasing on positive arguments. Therefore

- `a3>=W3 e3(v1,...,v4)` and `a2<=W3 e2(v4,...,v7)`;
- `b2>=W4 e2(v1,v2,v3)` and `b1<=W4(v5+v6+v7)`;
- `c1>=W5(v1+v2)`; also `W6>=0`.

The y^2 cover coefficient has no pair term (two cycles leave degree at most one), hence Lemma 5 gives **the equality** `E2=a2+b1+W5`. With `s12=v1+v2>0`,

`W5>=E2-W3 e2(v4,...,v7)-W4(v5+v6+v7)`.

Multiplying by s12 preserves this inequality even if the right side is negative. Substitution into E1 yields

`E1 >= s12 E2 + W3 alpha + W4 beta - W3^2/2`,

where

`alpha=e3(v1,...,v4)-s12 e2(v4,...,v7)`,

`beta=e2(v1,v2,v3)-s12(v5+v6+v7)`.

The y^3 equality is `E3=a1+W4`; interlacing/Ky Fan gives `a1>=W3 S4`, where `S4=v1+...+v4`. Thus `0<=W4<=E3-W3 S4=:K`. The sign needed for replacing W4 is strict:

`-beta=s12(v5-v3)+s12 v7+(s12 v6-v1v2)>0`,

because the first term is nonnegative and `s12 v6-v1v2=v1v6+v2(v6-v1)>0`. Hence `W4 beta>=K beta`, and rearranging proves

`Y1+ := E1-s12 E2-W3 alpha-K beta+W3^2/2 >= 0`.

This proves the lemma; no numerical eigenvalue approximation is used in this argument. At fixed six rates `x=v7`, E1/E2/W3 are affine in x, alpha/beta are affine in x, and K is affine in x. Consequently Y1+ is at most quadratic; my symbolic polynomial arithmetic confirms degree exactly two and the supplied coefficient definitions.

## 4. Definitions rebuilt, and written reconstruction of C3

Let `x=v7`, `f_k=e_k(v1,...,v6)`, `F=f1-4`. Matching the target coefficients independently gives

`p=e1-4`, `q=e2-4e1+10-2z`,

`E4=e3-[(4+4z)+(6+2z)p+4q]`,

`E3=e4-[(1+z)^2+(4+4z)p+(6+2z)q]`,

`E2=e5-[(1+z)^2p+(4+4z)q]`, `E1=e6-(1+z)^2q`.

The six-variable quantities, all rebuilt rather than read from stored coefficient arrays, are

`A=f2-4f1+10-2z`,

`B=f3-4f2+(10-2z)f1+12z-20`,

`h1=f3-(6+2z)f1+20+4z`,

`h0=f4-(6+2z)f2+(20+4z)f1+3z^2+6z-45`,

`D=h1-A S4`, `E=h0-B S4`, `Q0=A^2-F B`, `H0=-(h0 A-h1 B)`.

The identities `q=A+xF`, `W3=E4=Ax+B`, `E3=h0+xh1`, `K=E+xD` and `EA-BD=h0A-h1B` hold symbolically in z. `Qpol` and `Hpol` in the compact covers are positive integer multiples of Q0 and H0 (scales 2500 and 500000 at z3).

For Lemma 5 put `S3=v1+v2+v3`, `m2=e2(v1,...,v4)`, `L4=v4+v5+v6+x` and `Y2b=E2-E4 m2-S3(E3-E4 L4)`. Its leading x coefficient is exactly `c2=S3 A`. Write `Y2b=c2 x^2+c1 x+c0`, `Y1+=d2 x^2+d1 x+d0`.

### Case (a): f1<4

Let `r=4-f1>0`. Since p>0, x>r. Since q>0, A>rx>r^2. But the exact identity `5 f1^2-12 f2=sum_{i<j<=6}(v_i-v_j)^2>=0` gives

`A-r^2=f2+4f1-f1^2-6-2z <= -7f1^2/12+4f1-6-2z`

`=6/7-2z-(7/12)(f1-24/7)^2<0`

at z3=83/100>3/7. Contradiction.

### Case (b): f1>=4, A<=0

q>0 forces F>0. If A=0, W3=B>=0 implies Q0=-FB<=0. If A<0, the crude feasible interval is

`x_q=-A/F < x <= x_E=-B/A`.

It is empty unless `Q0<0`, because `F(x_E-x_q)=Q0/A`. In either subcase Q0>0 contradicts the crude hypotheses. QO proves Q0>0 outside N^6, where `N=[11/21,37/27]`.

Inside N^6, the sorted NB cover is exhaustive. An unsorted leaf (`lo_i>hi_j` for some i<j) contains no sorted point. F, A and Q leaves immediately contradict f1>=4, A<=0 or Q0<=0. Every other selector requires A<0, so c2=S3 A<0 and Y2b is strictly concave:

- **E4v6:** E4(v6)<0 and A<0 imply E4(x)<=E4(v6)<0 for x>=v6.
- **Y2v6:** Y2b(v6)<0 and Y2b'(v6)<=0 imply Y2b(x)<0 for x>=v6.
- **Disc:** discriminant `c1^2-4c2c0<0` with c2<0 implies Y2b<0 for all real x.
- **Y2tan:** let `GQ=F^2Y2b(x_q)=c2 A^2-c1AF+c0F^2`, `GPQ=F Y2b'(x_q)=-2c2A+c1F`. The second certified polynomial is `T2=A GQ+GPQ Q0=A F^2[Y2b(x_q)+Y2b'(x_q)(x_E-x_q)]`. Since A<0 and F>0, `-GQ>0,T2>0` make the tangent at x_q negative at both endpoints. A concave quadratic lies below its tangent; the tangent is negative throughout the interval. Thus Y2b<0 there. An empty crude interval is already contradictory.
- **Y2E:** `-A^2Y2b(x_E)>0` and `mDE=2c2B-c1A=-A Y2b'(x_E)>=0` imply Y2b(x_E)<0 and Y2b'(x_E)>=0. Concavity gives Y2b'(x)>=0 for x<=x_E, whence Y2b(x)<=Y2b(x_E)<0 on the allowed region.

Every selector contradicts one of W3>=0 or Y2b>=0. This explicitly covers A=0 and f1=4 boundary possibilities; they cannot hide in a leaf requiring strict A<0 or F>0.

### Case (c): f1>=4, A>0, D<=0

The identity H0=-(EA-BD) supplies the crude contradiction. If D=0, K>=0 implies E>=0, so EA-BD>=0. If D<0, W3>=0 and K>=0 imply

`-B/A <= x <= -E/D`.

Nonempty interval implies BD<=EA after multiplying the endpoint comparison by -AD>0. Thus H0<=0 in both subcases. HO proves H0>0 outside `M^6`, `M=[7/9,5/3]`.

Inside M^6, the sorted MC cover has no applicable unsorted leaf. mA, D and H contradict respectively A>0, D<=0 and H0<=0. A **Y1end** leaf certifies A>0, D<0, d2>0 and the strict positivity of

`-[d2 B^2-d1AB+d0A^2]=-A^2Y1+(-B/A)`,

`-[d2 E^2-d1DE+d0D^2]=-D^2Y1+(-E/D)`.

Thus Y1+ is convex and negative at both crude endpoints. It is negative on their entire segment, contradicting Lemma 6. Empty segments already contradict feasibility; D=0 cannot occur in a Y1end leaf.

### Case (d): f1>=4, A>0, D>0 — residual reduction reconstructed here

Put `al_j=e_j(v1,...,v4)`, `be1=v5+v6`, y=al1. The identities

`K1=al3-al1 al2+4al1^2-16al1+20+4z`,

`K2=al2-al1^2+4al1-6-2z`, `D=K1+be1 K2`,

`Abar=al2-4al1+10-2z+be1(al1-4)+be1^2/4`,

`Dbar=4al1^2-16al1+20+4z-(5/6)al1 al2+be1 K2`

give `Abar-A=(v5-v6)^2/4>=0` and `Dbar-D=al1 al2/6-al3>=0`. For completeness the latter bound is the exact nonnegative identity

`al1 al2-6al3=(1/2) sum_{i<j<k<=4}[v_i(v_j-v_k)^2+v_j(v_i-v_k)^2+v_k(v_i-v_j)^2]`.

Also `3al1^2-8al2=sum_{i<j<=4}(v_i-v_j)^2>=0`, so define `tau=al2/((3/8)y^2)` in [0,1]. Sortedness gives `be1>=2v4>=y/2`, so `gam=be1-y/2>=0`. Therefore `al2=(3/8)tau y^2`, `be1=y/2+gam`, `f1=y+be1`, with y>0, gam>=0. Abar>0 and Dbar>0 follow from case (d).

The residual polynomials rebuilt from these displayed definitions are positive multiples of Abar, Dbar and f1-4: first 144,144,2 and then the integerization LCMs 25,25,1. On the chart `y=s/(1-s)`, `gam=g/(1-g)`, ordinary tau in [0,1], the exact residual cover puts every point into a leaf proving Abar<=0, Dbar<=0, or f1-4<0. Each contradicts this case. Thus (a)–(d) exhaust all possibilities.

## 5. Independent finite replay: method, completeness and results

My code is `reviewer-f180-lib.py`, `reviewer-f180-defs.py`, `reviewer-f180-replay.py` and `reviewer-f180-merge.py`, not either author program. Python 3.14.3 / NumPy 2.4.3 were used; NumPy arrays are `dtype=object` containing exact arbitrary-precision integers. Sparse polynomial coefficients use int/Fraction. No floating arithmetic appears in any acceptance calculation. All **26** certified polynomials were reconstructed from the definitions above: 2 compact, 13 NB, 8 MC, 3 residual. Their integerization LCMs/digests agree with every recorded certificate value (residual polynomials have their own digest convention after the displayed 144/144/2 scaling).

### Direct per-leaf method, not author-style de Casteljau

A path is mapped independently to intervals `[n_i/2^ell_i,(n_i+1)/2^ell_i]`, char t splitting axis t mod 6 (mod 3 residual), 0 lower, 1 upper.

For an ordinary degree-d axis, substitution `s=(n+t)/2^ell` gives the integer Taylor-shift matrix

`U[j,k]=C(k,j)n^(k-j) 2^(ell(d-k))` for j<=k.

The monomial-to-Bernstein matrix is `V[m,j]=L C(m,j)/C(d,j)` for j<=m, with `L=lcm_j C(d,j)`. Their product gives the leaf Bernstein coefficients up to a **positive** factor. Sorted polynomials are first expanded exactly under `v=lo+(hi-lo)s` and integerized.

For compact degree-2 axes I instead use the exact quadratic blossom. With N=2^ell, rows corresponding to endpoint pairs (n,n), (n,n+1), (n+1,n+1), the column for `x^k(1-x)^(2-k)` is

`[2(N-a)(N-b), a(N-b)+b(N-a), 2ab]`,

an integer Bernstein row scaled by 2N^2. This acts directly on the original monomial coefficients in u. Residual y/gam axes use the general compactification expansion `x^i(1-x)^(d-i)` followed by the ordinary leaf matrix; tau is ordinary Bernstein. Degree-zero axes have identity action.

Tensor products of these per-axis matrices compute every required leaf tensor directly from the global polynomial. A trie grouped by complete interval on axis 0, then axis 1, etc. shares identical partial mode products; it does **not** subdivide parent-box Bernstein tensors. Separate no-trie controls reproduced 760/760 sampled recorded leaves.

### Coverage and strictness proofs

For every cover I checked unique binary paths, no leaf prefix of another, and exactly `sum_leaf 2^(-depth)=1` using integers at the maximum depth. A finite prefix-free set with Kraft sum one exhausts all binary cylinders: otherwise a missing cylinder has positive mass. Thus the associated closed dyadic boxes cover the cube (midpoint ties may choose either bit). Shard unions were checked for exact decided-set equality and no duplicate verdicts.

For QO/HO, R boxes were checked inside their closed excluded cube. A pos box has depth>=6, all Bernstein coefficients>=0, and every box corner inside `(0,1)^6` has coefficient>0. Every axis was split at least once, so a box interval cannot span both global endpoints 0 and 1. At any point of the box in the global open cube, choose an interior-domain corner on the point's minimal box face; its Bernstein basis function is positive. This proves strict positivity there, including internal subdivision faces. The compactification factor `prod(1-x_i)^2` is positive at all finite positive rates. No positivity on zero-rate boundary faces is assumed.

For sorted covers I independently used the packet's rule table, not certificate-supplied rules as authority; the tables were additionally compared exactly. All required tensor coefficients were >0 except mD6/mDE allowed >=0; in fact those recorded minima were strictly positive too. All 5897 unsorted leaves were checked by exact rational interval inequalities.

Residual all-coefficients<=0 / <0 rules are valid on the closed compactified boxes and hence on the actual finite-rate chart. Exactly four Dbar leaves have maximum coefficient 0 (paths 101101, 101111, 111101, 1111111); this is **allowed**, since Dbar>0 was needed in case (d). They are not silently treated as strict negatives.

### All 53372 leaves replayed

| Cover | Total leaves | Replayed label counts | Max depth |
|---|---:|---|---:|
| QO | 25674 | pos 21673; R 4001 | 36 |
| HO | 9473 | pos 9345; R 128 | 32 |
| NB | 14034 | Q 4728; Y2tan 3472; unsorted 4838; Y2v6 67; E4v6 888; Disc 36; Y2E 5 | 37 |
| MC | 2046 | H 601; Y1end 386; unsorted 1059 | 23 |
| residual | 2145 | Abar<=0 1051; Dbar<=0 1026; f1-4<0 68 | 22 |

NB required **20680** per-polynomial leaf tensors; MC required **2531**. QO/HO required 31018 positive tensors plus 4129 excluded-box checks. All five covers pass prefix/Kraft completeness and every leaf rule. The excluded compact cubes map exactly to the affine boxes: `[11/32,37/64]/(1-[11/32,37/64])=[11/21,37/27]`, and `[7/16,5/8]` maps to `[7/9,5/3]`. The mappings are increasing, so closed endpoints and complements agree.

## 6. Actual bounded controls and receipts

Each one-shot executable was capped at **120 s**. Both 36-job replay batches had that cap **per child**; no cap/timeout occurred. A cap would have meant UNKNOWN, never acceptance. Native start/end clock observations, per-job exits/stdout/output hashes and the full artifact hashes are in the evidence inventory and `reviewer-f180-receipts-*.json`.

| Control | Observed local clock interval (2026-10-29, -0700) | Exit / actual result |
|---|---|---|
| main direct replay, 36 jobs | 08:53:38–08:54:20 | every child exit 0; max child wall 21.18 s |
| symbolic identities / 26 polynomial bindings / coverage | 08:55:01–08:55:24 | exit 0; **170/170 PASS** |
| main merge | 08:55:54–08:55:55 | exit 0; every leaf accepted |
| positive + intended-reason negatives | 08:58:07–08:58:31 | exit 0; **49/49 behave as intended** |
| wrong-z full replay at 41/50 | 08:58:37–08:59:14 | all 36 child exits 0; max 19.36 s; **merge exit 1, 17501 leaf sign/rule failures**, intended |
| Lemma 6 coefficient regression | 08:59:52–08:59:52 | exit 0; **11/11 exact** y^6…y^1 identities; separate floating inequality diagnostic 11/11 |
| engine vs exact rational evaluation | 09:01:53–09:02:50 | exit 0; **16/16 positive/negative** controls behave as intended |
| trie vs direct no-trie sample | 09:10:54–09:11:24 | exit 0; **760/760** agree; sibling-box negative changes 97/140 records |
| wrong-z digest binding | 09:16:04–09:16:12 | exit 0; correct z 26/26 match; at 41/50 and 21/25 only the 3 z-free polynomials match |

The 49 controls include: for each cover, unmodified positive coverage; dropping first/middle/last leaves (Kraft sum <1 for the intended reason); duplicate leaves (duplicate-path rejection); overlapping child leaves (prefix rejection). Relabelled controls fail for their mathematical conditions: 40 Q leaves labelled A fail A positivity, 40 Q leaves labelled unsorted fail the strict interval test, 40 Y2tan leaves labelled Disc fail discriminant positivity, 40 H leaves labelled Y1end fail at least one endpoint/convexity tensor, QO pos leaves labelled R fail cube inclusion, HO R leaves labelled pos fail positivity, and residual Dbar leaves labelled Abar fail the Abar sign. Wrong-sign -T2, +E4(v6), +D^2Y1+(-E/D), -Qpol and -Abar fail on their intended sign test (40/40 each).

Wrong-z=41/50 was not rejected because of missing files, malformed JSON, a crash or coverage gaps: the same covers remain prefix-free/Kraft-complete and every child exits 0. Failures are exact polynomial sign failures: QO 9234 pos leaves, HO 1758 pos leaves; NB Q 4433, Y2tan 1426, E4v6 66, Y2v6 21 leaves; MC H 442, Y1end 67 leaves; residual Abar 41 and Dbar 13 leaves. These total 17501 distinct failing leaves. At the digest level z=41/50 or 21/25 preserves only NB:F, NB:Fm and residual:f1minus4, all z-free; all 23 z-dependent bindings change.

The engine positive controls compare exact Bernstein evaluation to direct rational polynomial evaluation at interior points: their ratio is one positive constant per leaf. Perturbing P to P+1 breaks that ratio as intended. This checks the positive scaling/mapping independently of the sign rules. The Lemma 6 regression separately enumerates one-way/virtual cycles of 11 seeded rational Metzler matrices (including nonzero disjoint-3-cycle pair terms), computes principal minors exactly, and verifies the coefficient relations. Its floating eigvalsh diagnostic is explicitly not an acceptance premise; the written interlacing proof is the premise.

Key evidence hashes:

- `reviewer-f180-lib.py`: `fb4d4e0bb18581442cbb634f8429c54f568abe27e53ba049c916cd47145c89b8`.
- `reviewer-f180-defs.py`: `3f33ab0aab885448def98a35fa2e29e04e08b933bfdc60363730c6a1b85c29ea`.
- `reviewer-f180-replay.py`: `27299b4547df12c9fde45d29241f6735aff8035aa1c1c2382eb076e6e97bf00e`.
- `reviewer-f180-receipts-main.json`: `923044daa873248eab5814d0fc447228cf4c9950ba85b53109b900c4cc81c7ea`.
- `reviewer-f180-merge-main-stdout.txt`: `7358d2413b691441f73e617a0270436e28edc28f2af92bb91d98b04563e5d6e3`.
- `reviewer-f180-identities-stdout.txt`: `fb7b5ca564d54847eb9d3857c45a57cfc3cdb5f23f00caba86ad28ef45764969`.
- `reviewer-f180-negatives-stdout.txt`: `56c87c7067837fa9de305a5ae7118a0ecda35fd62a3bbd4d33590749d1ec667a`.
- `reviewer-f180-receipts-z41over50.json`: `5dce233856f0fc5082522dd8242397f4a0a32b14e5e0958745d96dfad64a23ed`.
- `reviewer-f180-merge-z41over50-stdout.txt`: `ff5d5edcd03b076364ad18a018053394b3c12cadb881f2fa2a8a4b0524e1d991`.

## 7. Theorem propagation and closed endpoints

If a PH representation with <=7 states existed at z>=z3, the adopted caller applies because z3>1/2. Lemma S with `t=sqrt(z/z3)-1>=0` and rescaling by 1+t moves its double non-real pair to `-1±i sqrt(z3)` while preserving irreducible Metzler structure and Perron root zero. The two remaining non-Perron roots retain negative real parts after the shift/rescaling, so the new real quadratic still has p,q>0. The adopted symmetrization lemmas, Lemma 5 and new Lemma 6 then give all six C3 inequalities at z3, a contradiction. This uses no special topology or detailed-balance assumption.

Excluding every z>=z3 yields **sup Z7<=z3** only: realizable ratios could approach z3 from below. The target §1 uses `[41/50,83/100]` and `[z_*,0.83]`, and its END uses `[41/50,0.83]`: all right endpoints are closed. Mandatory input 1 supersedes its older v4 status/lower-end statements and the older half-open bracket in the f160 context. Under the addendum's adopted f50-band import the updated bracket is **[z_*,83/100]**, with `820420341/10^9 < z_* < 820420541/10^9`. That lower-band statement is an explicitly conditional import here, not a reconstruction of an unlisted construction. No PH7 downward-closure claim is inferred from spectral shift monotonicity.

## 8. Findings, deviations and non-claims

### m1 — MINOR, exposition/self-containedness

Target §4 says cases (a),(d) are “as before” / “the three-parameter residual,” and §2 names several quantities “as in the core,” but the cited core is not a declared input. The bundle contains enough formulas in its generator/replay/addendum to reconstruct them, and I supplied the complete case (a),(d), Q0/H0 contradictions and residual chart proofs in §4 above. Thus this is not a mathematical gap after reconstruction. A written theorem packet should state these formulas and short inequalities in prose rather than require a reader to recover them from implementation text or an inaccessible citation. No frozen author bytes were edited.

### m2 — MINOR, reviewer-process display deviation

The instruction said the certificate was to be parsed fully but never displayed. I did not dump/render the 2 MB JSON, but my own parse/controls printed a structural metadata/count summary, the three residual expression strings, and bounded leaf identifiers in coverage-negative/zero-boundary failure receipts. This is the exact display deviation; it did not involve unlisted/held material and none of those extracted claims substitutes for the full parse or independent replay. It is disclosed rather than silently described as zero display. It has no mathematical effect but is counted separately as a review-process MINOR.

Other execution disclosures: exploratory reviewer residual/HO runs at 08:50:33–08:50:34 and 08:51:43–08:51:52 exited 0; their own output JSON filenames were overwritten by the final main batch and only final-batch hashes are evidence here. Preliminary kernel digest/coverage/timing experiments were superseded by the recorded bounded scripts. Some local shell invocations used directory listings/paging and mechanical job-list construction rather than the preferred specialized tool route; this did not open additional scientific inputs or alter author files. All writes were review-v1.md or reviewer-prefixed artifacts within this wave directory. No Git, deletion command, publication, external-model call, author contact, infrastructure change, sibling review or held material access occurred. No author program was imported/executed. No timeout is being promoted to a pass.

**No FATAL or MAJOR mathematical defect was found in the frozen candidate.** The same-harness result does not by itself clear novelty, human review, independent-model-family review or formal/kernel validation.

## 9. Created artifacts and detached review digest

Exact pre-report filenames/sizes/hashes are in `reviewer-f180-evidence-inventory-v1.json`. Created executable/library artifacts are `reviewer-f180-lib.py`, `reviewer-f180-defs.py`, `reviewer-f180-replay.py`, `reviewer-f180-runner.py`, `reviewer-f180-identities.py`, `reviewer-f180-merge.py`, `reviewer-f180-negatives.py`, `reviewer-f180-lemma6-regression.py`, `reviewer-f180-engine-check.py`, `reviewer-f180-trie-crosscheck.py`, `reviewer-f180-wrongz-digests.py`; job lists `reviewer-f180-jobs-main.txt`, `reviewer-f180-jobs-z41over50.txt`; seven `reviewer-f180-*-stdout.txt` files; main/wrong-z batch receipts; 72 per-shard `reviewer-f180-out-*.json` files. The two output families have 36 files each, the wrong-z family carrying `-z41over50` in its filenames. Nothing outside this wave directory was written.

This report's SHA-256 cannot be embedded into its own unchanged bytes without self-reference. It is recorded immediately after creation in **`reviewer-f180-review-receipt-v1.json`** and in the final handoff; that receipt also lists the exact complete created-file census including this report and the evidence inventory. The detached receipt itself is outside its own hash census by construction.
