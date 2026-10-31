# Common local information: two nonuniform syndrome obstructions

## 0. Source-first entry and claim boundary

Read these complete erratum bodies FIRST: `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md`; `frontier-20261028-mixed-plane-symmetry-erratum-v1.md`; `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md`; `frontier-20261029-primal-checker-subset-coverage-erratum-v1.json`.

**Status: WRITTEN candidate mathematics. Two small integer coefficient identities have separately implemented, exact in-kernel checks; the component/fiber arguments below still require independent scientific review.** No formal proof, novelty clearance, scientific adoption or unrestricted guessing-number improvement is claimed. These two uses share one common-local-information mechanism; they are not counted as independent discoveries.

This manuscript consolidates the one-auxiliary cylinder result and a new arbitrary-function hierarchy result. It imports NO affine-plane entropy theorem, two-syndrome theorem, copy program, DFZ inequality, reviewer return, f161/f162 held consumer or bulk-archive PASS. The frozen67,393,983-byte affine-plane archive remains unchanged and was NOT scientifically replayed. The new checks concern only1008 ordinary-Shannon rows and478 Shannon plus53 declared zero-FD rows, respectively.

## 1. Literal setting and shared lifting lemma

The graph neighborhoods are

```
1:2,3,4,5,6,7   2:1,3,7,9,10   3:1,2,4,8,9
4:1,3,5,8,10    5:1,4,6,9,10   6:1,5,7,8,9
7:1,2,6,8,10    8:3,4,6,7,9,10
9:2,3,5,6,8    10:2,4,5,7,8.
```

This is the literal26-edge R-minus transcription from Fig.2, printed p570, of the Gurpinar2024 publisher PDF SHA256 `373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8`. Edge3-4 is present;9-10 is absent. The mathematical statements below are about these displayed sets.

Let G be a finite abelian group of size d>=2. Use ten triangle factors

```
T1=123, T2=145, T3=167, T4=239, T5=2-7-10,
T6=389, T7=4-5-10, T8=4-8-10, T9=569, T10=678.
```

A word has one G-component x_v^t at each triangle occurrence; every X_v has three components, alphabet G^3. Write sigma_t=sum_(v in Tt)x_v^t. A law obeys the ORIGINAL graph FDs H(X_v|X_N(v))=0. For any ten variables, Delta=H(X_V)-(2/3)sum_v H(X_v).

**Shared fixed-factor lemma.** Suppose sigma_t is constant for one triangle t. Let C be that factor's COMPLETE triple and Y_v the remaining components at v. On each positive-probability C-fiber, the Y variables still obey the original graph FDs: the deleted components are supplied as constants to the original decoders. No smaller-neighborhood FD follows merely from this observation.

Every pair of components of C determines its third. Pairwise entropy subadditivity, summed over the three pairs, gives3H(C)<=2sum_v H(C_v), with C_v constant off that triangle. Also

```
H(X_V)=H(C)+H(Y_V|C),
H(X_v)=H(C_v)+H(Y_v|C_v)>=H(C_v)+H(Y_v|C).
```

Thus Delta(X)<=Delta(Y|C). Any nonpositive-gap result on all conditional Y-fibers lifts to the original arbitrary law. No independence or uniformity is assumed.

## 2. First exact lemma: an arbitrary-auxiliary defect inequality

For ANY finite X1,...,X10,U, put

```
F_v=H(X_v|X_N(v)),
D6=H(X6|X_{5,7,8,9},U), D7=H(X7|X_{2,6,8,10},U),
E9=H(U|X_N(9)), E10=H(U|X_N(10)).
```

The following is an unconditional ordinary-Shannon inequality:

```
18 Delta <= 6 sum_(v notin {6,7}) F_v +5(F6+F7)+D6+D7+E9+E10.   (1)
```

No graph FD, binary variable, finite-field structure or cardinality cap is assumed in(1). Its supplied integer certificate is

```
113*[RHS(1)-18Delta] = sum_r lambda_r I_r,
```

with1008 strictly positive integer coefficients:1006 ordinary CMIs and2 conditional entropies. Every row's complete sparse coefficient vector is supplied. The independent implementation reconstructs both every CE/CMI and the displayed target, and compares all2047 nonempty entropy coordinates exactly. Thus Shannon nonnegativity proves(1). For a graph-FD law, its first ten defects vanish.

### Actual component consequence A

Let C be factor3's complete tuple and U=(sigma5,sigma9,sigma10). Within each C-fiber:

- Knowing U and Y_{5,7,8,9} solves vertex6's two remaining components by the factor9 and10 equations.
- Knowing U and Y_{2,6,8,10} similarly solves vertex7's factors5 and10 components.
- The original-neighbor tuple at9 recovers Y9 and hence sigma9. The tuple at10 recovers Y10 and hence sigma5.

These are ACTUAL component inversions, not stronger abstract graph FDs. Applying(1), then weakening conditioning in its last two defects, gives

```
18 Delta(Y|C)
 <= H(sigma5,sigma10|sigma9,C)+H(sigma9,sigma10|sigma5,C).          (2)
```

If sigma3 is constant, the shared lifting lemma yields the candidate quantitative theorem

```
18 Delta(X)
 <= H(sigma5,sigma10|sigma9,C)+H(sigma9,sigma10|sigma5,C).          (3)
```

Therefore Delta(X)<=0 if both right-hand conditional entropies vanish. An elementary sufficient condition is, for fixed group constants gamma,alpha,beta,

```
sigma3=gamma, sigma5-sigma9=alpha, sigma10-sigma9=beta.            (4)
```

All six other syndromes are unrestricted. The allowed cylinder has d^7 syndrome vectors. In the binary q=8 encoding it is an affine dimension7 subspace, up to offset, with128 syndromes, NOT another affine plane with at most4 syndromes. Probabilities, correlations and the used subset are arbitrary. Every uniform FD support in this class has at most d^20 words; fixed-parity triangle codes attain d^20.

The factor-preserving graph permutation(8,9,3,4,10,7,6,1,2,5) exchanges factors3 and10 and swaps5 with9. It gives a second cylinder: sigma10 constant and sigma3,sigma5,sigma9 equal up to fixed group offsets. No permutation that fails to preserve the factor list is used for this component transport.

## 3. Second exact lemma: an intermediate information hierarchy

Now use thirteen finite variables Y1,...,Y10,A,B,T, with S meaning the PAIR(A,B), not a new independent variable. Assume the two functional relations

```
H(A|T)=0, H(T|A,B)=0.                                          (5)
```

Let J={1,2,3,4,5,6,8,9,10}, and L_J(v) be the other vertices of these selected triangles through v. Define the following actual information variables:

|v|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|Z_v|S|T|T|B|S|A|A|S|T|S|

Besides all original graph FDs, assume only the following FD rows used by the supplied certificate:

- H(Z_v|Y_N(v))=0 for v in{1,2,5,6,7,8,9,10}.
- H(Y_v|Y_L_J(v),Z_v)=0 for v in{1,2,3,5,6,7,8,9,10}.
- H(Y_v|Y_L_J(v),S)=0 for v in{2,6,7,9}.
- H(B|Y_{1,4,5})=0 and H(B|Y_{4,8,10})=0.

**Conditional Shannon/FD lemma.** These finite-variable premises imply Delta(Y)<=0, with no binary or cardinality hypothesis.

The second supplied integer certificate says

```
8*(-3Delta(Y))
 = sum_478 positive_integer * ordinary_Shannon_row
   + sum_53 signed_integer * declared_zero_FD_row.               (6)
```

The478 Shannon rows are458 CMIs and20 conditional entropies. The53 FD rows comprise the33 listed physical FD rows and20 conditionings of the two base relations(5). Every row has its full literal coefficient vector on the8191 nonempty subsets of the thirteen variables. A separate checker rebuilds the ordinary Shannon vectors, derives the local sets from J and the triangle list, reconstructs the functional/physical FD rows, and verifies the complete integer coefficient identity. It imports no producing code, old checker, source model, scientific library or review return. The scientific validity of the actual-component instantiation below remains a written review obligation.

One way to understand the reduction is that an intermediate variable T can retain A while revealing only a function of B. For A=f(T), information-order and refinement rows are ordinary CE/CMI rows plus conditionings of H(A|T)=0. For T=f(A,B), the analogous rows use H(T|A,B)=0. The certificate contains those conditioned FD rows explicitly; no informal substitution of a three-state variable for a binary one is required.

### Actual component consequence B: arbitrary nonlinear phi

Suppose sigma7 is constant, and for arbitrary fixed group offsets a_t,b_t there exist G-valued A,B with

```
sigma_t=A+a_t for t in{1,3,5,6,9,10},
sigma_t=B+b_t for t in{2,8},
sigma4=phi(A,B),                                               (7)
```

where phi:GxG->G is ANY fixed function, not assumed additive, injective or balanced. A,B need not be independent or uniform. Then the candidate theorem is Delta(X)<=0.

**Proof.** Condition on the COMPLETE tuple of factor7 and delete just its components. Put O=phi(A,B), S=(A,B) and T=(A,O), so(5) holds. A and B are actual syndrome functions (recover them by subtracting fixed offsets). At vertices1,5,8,10 the incident selected parities reveal both A and B. At2,3,9 they reveal A and O, hence T. At6,7 they reveal A; at4 they reveal B. The original graph FD plus the other two components of each incident triangle therefore gives every required neighborhood-information FD.

Conversely, Z_v determines all selected parities at that vertex: S determines A,B,O; T determines A,O; the single A or B handles homogeneous vertices. Given Y_L_J(v), solve every missing component by its group-sum equation. This supplies the listed local Z_v FDs. S determines all selected parities and supplies the redundant local-S rows too. The complete factor2 and8 triangles determine B by their parity equations. Thus every declared physical FD in(6) holds on every fiber. Apply(6) and the shared fixed-factor lift to get Delta(X)<=0.

The allowed syndrome set has d^2 values, indexed injectively by(A,B), but phi can be arbitrarily nonlinear. For G=F2, the original fresh rank-three pattern is phi(A,B)=A*(1-B); all Boolean functions are covered, not merely that literal one-hot table. This does NOT cover arbitrary four-syndrome sets: the repeated-coordinate pattern(7) and fixed factor7 are essential premises.

## 4. Evidence, failure dependencies and limits

The complete two new certificates/checkers/receipts are:

- `frontier-20261029-one-auxiliary-defect-certificate-v1.json`, SHA256 `7c1b7b6f8b5bfe286411b5d3ba92dc6dd351e7003402102f9c4480038a220e82`.
- `frontier-20261029-one-auxiliary-defect-check-v1.py`, SHA256 `4f6b3fd88713ca18335db09368179834b3f7bb4c86651822cfd99dc63bf8429e`.
- `frontier-20261029-one-auxiliary-defect-check-result-v1.json`.
- `frontier-20261029-functional-syndrome-DAG-certificate-v1.json`, SHA256 `17fe38c9792b96a9f0af21e71084793ac6e193dedf927f586fd513a760b1e2f0`.
- `frontier-20261029-functional-syndrome-DAG-check-v1.py`, SHA256 `a2c889fe88957c9bd42342731bd9f796f6629ecd9b7775b6ce5b1de16dd3ce22`.
- `frontier-20261029-functional-syndrome-DAG-check-result-v1.json`.

Both checks used finite integer arithmetic inside the existing owner kernel, with declared small row bounds, and rejected five targeted mutations each. These are same-harness exact coefficient/row checks, NOT formal proof or independent referee acceptance. Receipts and cardinalities alone are not proof; all literal coefficient bodies and semantic input formats must accompany any prospective review.

If the first integer identity fails, consequence A is unsupported, but B does not import it. If the second identity or any of its functional/component premises fails, consequence B is unsupported; A does not import it. If the shared fixed-factor lift fails, both group-law applications fail even if the raw identities remain valid. Removing the fixed-factor premise, the deterministic-phi premise in(7), or the common-information conditions in(3) is NOT licensed by these statements.

The unrestricted R-minus entropy-balance and guessing-number problems remain open here. These restricted nonuniform obstructions are neither an actual strict-gain law nor a global negative answer. No novelty or publishability claim has been cleared.
