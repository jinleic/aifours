# v33-A serial written review: the new small-phase decomposition closes the x1111 upper bound

Actual returned `/bin/date` before writing: **Sun Oct 25 04:53:05 PDT 2026**. MathResearch96h-2, SAME reviewer as v30-B. Strictly WRITTEN reconstruction; metadata clocks/hashes/source reading only. No scientific eval/interpreter/arithmetic program, enumeration, certificate replay, symbolic program, solver, model CLI or nested agent. Parent erratum v7 and HOLD remain binding.

## 1. Binding, exposure, full coverage and verdict

Exposure was frozen before the new body read in `peer-review-ppt-small-phase-SN2-ack-v1.json`. Prior v30-B findings are preserved, not transferred automatically to this successor.

Read the complete462-LF literal packet `peer-review-wave-v33-ppt-small-phase-SN2-sources-v1.md`, SHA256 `319c86df0576a554970abfd6fe37a7279321267a9c79ad4792a8f7539c752624`. Both declared full source ranges were read: new ADDENDUM LF1–207 and original markdown LF1–241. The sole truncated line, packet LF233/original LF13, was explicitly reread RAW. Fresh metadata source hashes match the manifest:

- **NEW** = `rational-x1111-SN2-ADDENDUM-1-small-phase-decomposition.md`, SHA256 `1044856f43b167bd56acf49a56a261bfece8e7ebf9394380ca3e0d6a8f578097`.
- **OLD** = `rational-x1111-schmidt-two-certificate-v1.md`, SHA256 `2d38c9947d4c4ef87149f694dbc277e915eb0e706ec83656f6c626d7c6c76e56`.

Source references below use ORIGINAL LFs in NEW/OLD, not packet LFs.

**Overall verdict:0 FATAL /0 MAJOR /0 MINOR at the complete NEW written-proof scope.** The new37-term identity has a full written reconstruction below, with NO unmet load-bearing identity. Together with the exact same-input PPT/entanglement argument it supports **SN(rho)=2 for the literal x1111 state ONLY**.

The old21-pair weighted identity remains **NOT_RECONSTRUCTED** and receives no verification/admission credit. It is NOT a premise of the new proof, so its historical gate is bypassed by a new identity, not retroactively passed. All process findings and v30-B's original non-acceptance remain true at their historical snapshot. Parent disposition of this successor is still required. This is same-harness written checking, not executable, formal/kernel, configured dual-family, cross-vendor, human or novelty acceptance.

## 2. B0 — identical literal state, normalization and PPT:0F/0M/0m

NEW LF17–40; OLD LF19–47. The a,b,c,d,e,f,g,h,j definitions and all nine weights are unchanged from the actual frozen x1111 input reconstructed in v30-B. In particular d=02+|3>x, h=|0>x, x=(1,1,1,1), and rho=R/49. The positive Gram sum has trace

`3+2+2+3(5+2+1+1+4+1)=49`.

The displayed positive partial-transpose Gram also remains exactly the same. To rebind its proof rather than rely solely on an old verdict: the partial transpose of P(a)+P(b)+P(c) has core diagonals00,11,22,01,12,10,21 and cross pairs01/10,02/20,12/21,02/11,-11/20. The first six stated Gram projectors reproduce this plus3P02+3P20. The non-core partial transpose supplies those extra diagonals and the remaining four Gram groups, since the d cross02/3r moves to0r/32 and e cross20/33 moves to23/30. With l=|3>x this gives exactly3P(32+h)+3P(30+23)+3P(l)+3P33. Thus rho is PPT by a literal positive Gram identity, with no historical solver/rank/LDL observation needed.

## 3. B1 — inherited eight-vector assembly freshly rebound:0F/0M/0m

NEW LF44–78; OLD LF51–99.

For delta=2i/3 the stated gamma has gamma²=-5i/12 and |gamma|²=5/12; the opposite delta conjugates it. Independent beta,chi signs preserve beta²+chi²=delta+delta^(-1). In each actual coefficient matrix, row index3 is delta times row index1, the upper3-by3 determinant vanishes, and the upper-left2-by2 minor is nonzero since |beta chi|=5/12<1. Each psi therefore has complex Schmidt rank exactly2.

Writing psi as

`a+beta b+chi c+delta v+delta chi f+delta beta g`, `v=d-e-f-g`,

the independent signs eliminate every mixed covariance except potentially b/g and c/f. Those are(5/12)E(conj(delta))=0; the a/v covariance is E(delta)=0. The surviving diagonal variances are1,5/12,5/12,4/9,5/27,5/27 in these six coefficient groups. This proves the complete A identity. No old21-pair premise or unadmitted arithmetic enters it.

Subtracting A from the defining R therefore leaves exactly(7/12)[P(b)+P(c)] plus F M F*, where F=(d,e,f,g,h,j) and

`M=3I6-(4/9)q q^T-(5/27)(E_ff+E_gg)`,

`q=(1,-1,-1,-1,0,0)^T`.

## 4. B2 — all16 literal phase vectors have two products:0F/0M/0m

NEW LF82–97.

For arbitrary z,w in the SPECIFIED nonzero set Z4={1,i,-1,-i}, expanding the first product gives

`(z|0>+|3>) tensor (x+z^(-1)|2>)`

`=z h+02+|3>x+z^(-1)32=d+z h+z^(-1)g`.

Expanding the second gives

`(|2>+w^(-1)|3>) tensor (|0>+w|3>)`

`=20+w23+w^(-1)30+33=e+w j+w^(-1)f`.

Their sum is precisely the actual chi_(z,w), not merely a vector in a similar support. Thus every one of the sixteen specified vectors has Schmidt rank≤2. The formula has no unverified division by a zero coordinate; z,w are nonzero by their definition.

## 5. B3 — full finite-character operator identity:0F/0M/0m

NEW LF99–112.

Group chi_(z,w) into five coefficient vectors:

`(d+e)*1 + h*z + g*z^(-1) + j*w + f*w^(-1)`.

For an integer k, averaging z^k over Z4 is1 when4 divides k and0 otherwise, by the finite geometric series; averaging independently over(z,w) multiplies the two such factors. The five exponent pairs are(0,0),(1,0),(3,0),(0,1),(0,3), all distinct modulo4 in both coordinates jointly. Therefore every off-group covariance vanishes. This includes z versus z^(-1): their exponent difference is2, whose average is0, not1.

The only retained internal cross pair is d/e, which share the SAME constant character. Thus the complete operator identity is

`(1/16)sum_(z,w in Z4) P(chi_(z,w))`

`=P(d+e)+P(f)+P(g)+P(h)+P(j)=B`.

This proves ALL coefficient entries at once by character orthogonality. The sixteen-point sum DEFINES a finite Fourier identity; no program enumeration, numerical sampling or inference from a tested subset was performed.

## 6. B4 — all five pair projectors and singles:0F/0M/0m

NEW LF116–124.

k1=d+f and k2=d+g have Alice support contained in span{|0>,|3>}; hence their coefficient matrices have at most two nonzero Alice rows. k3=e-f and k4=e-g have Alice support in span{|2>,|3>}. k5=f-g is the product |3> tensor(|0>-|2>). Therefore every pair projector is on a rank≤2 ket over C. The singles d,e each are sums of two products; f,g,h,j are products. Also b and c are sums of two products.

This support proof does not require k1,...,k5 to obey the earlier simultaneous-Veronese sufficient conditions. Not belonging to that older restricted cone would not invalidate any of these actual rank certificates.

## 7. B5 — complete residual identity, all21 coefficient entries:0F/0M/0m

NEW LF126–171. Put lambda=4/9. Work in the SIX-DIMENSIONAL COEFFICIENT space with independent formal coordinates(d,e,f,g,h,j), then apply F. From Section5, lambda B has diagonal lambda at every coordinate, and its sole nonzero upper off-diagonal is(d,e)=lambda.

The five pair projectors have coefficient vectors

`(1,0,1,0,0,0)`, `(1,0,0,1,0,0)`,

`(0,1,-1,0,0,0)`, `(0,1,0,-1,0,0)`,

`(0,0,1,-1,0,0)`.

Their lambda-weighted diagonal counts are(2lambda,2lambda,3lambda,3lambda,0,0). Adding the singleton terms gives ALL SIX target diagonals:

|Coordinate|Complete total|Value in M|
|---|---|---:|
|d|lambda+2lambda+11/9|23/9|
|e|lambda+2lambda+11/9|23/9|
|f|lambda+3lambda+16/27|64/27|
|g|lambda+3lambda+16/27|64/27|
|h|lambda+23/9|3|
|j|lambda+23/9|3|

Here3lambda+11/9=(12+11)/9,4lambda+16/27=(48+16)/27, and lambda+23/9=(4+23)/9. These are exactly3-lambda on d,e,3-lambda-5/27 on f,g, and3 on h,j.

For clarity the COMPLETE FIFTEEN upper off-diagonal entries, including every zero, are:

|Pair|RHS coefficient|Target -lambda q_i q_j|
|---|---:|---:|
|d,e|+lambda from B|+lambda|
|d,f|+lambda from k1|+lambda|
|d,g|+lambda from k2|+lambda|
|d,h|0|0|
|d,j|0|0|
|e,f|-lambda from k3|-lambda|
|e,g|-lambda from k4|-lambda|
|e,h|0|0|
|e,j|0|0|
|f,g|-lambda from k5|-lambda|
|f,h|0|0|
|f,j|0|0|
|g,h|0|0|
|g,j|0|0|
|h,j|0|0|

There are no hidden h/j covariances: character orthogonality removed them in B, and no pair or singleton has any h/j cross coefficient. Lower entries are the Hermitian conjugates. Thus all36 actual matrix entries agree. This is the missing written residual proof, with small rational coefficients, not a checksum or an appeal to historical booleans.

Applying the linear congruence by the ACTUAL F gives exactly NEW(9). Overlaps between physical source kets do not cause extra conditions: equality was proved before congruence. No independence or orthogonality of F's physical columns is assumed.

## 8. B6 — literal37-term decomposition and normalization:0F/0M/0m

NEW LF173–189.

Substitute the new residual identity into the independently rebound R-A identity, and expand B using the sixteen-phase identity. The phase-projector coefficient is lambda/16=(4/9)/16=1/36. The complete positive coefficients are then

`1/8` on each of8 psi terms;

`7/12` on b,c;

`1/36` on each of16 chi_(z,w) terms;

`4/9` on each of5 k terms;

`11/9` on d,e; `16/27` on f,g; `23/9` on h,j.

This is exactly NEW(10), with8+2+16+5+6=37 terms before any merging. All are rank≤2 kets by Sections3,4,6. All displayed scalar coefficients are positive. Unlike the old conjugate-pair table there is NO additional half-weight convention: the sixteen-phase average has already supplied its factor1/16.

Divide the exact operator identity by49. Normalizing each nonzero ket u changes its scalar coefficient c to c||u||²/49. These weights are nonnegative and sum to1 by tracing the proved identity and Tr(R)=49. Therefore the literal x1111 state has a complete convex rank≤2 decomposition, proving SN(rho)≤2 in WRITING without the old21-pair sum.

## 9. B7 — matching lower bound and exact input scope:0F/0M/0m

NEW LF191–199; OLD LF182–198.

The projected range matrices are unchanged. If the Bob3 column(H,0,J)^T is nonzero in a rank-one coefficient matrix, the middle Alice component vanishes, so its entire middle row and A vanish. If that column is zero, H=J=0 and the two core minors force A²-BC=A²+BC=0, so A=0 over C. Thus every product ket in that projected range has11 coefficient zero.

Every pure positive summand of a separable operator lies in its range, since a kernel vector has zero expectation in every nonnegative summand. Such a projected separable state would therefore have11 diagonal entry0. The actual entry is1 from P(a). The projection is entangled, and local projection cannot create entanglement from a separable rho. Hence SN(rho)≥2. Together with Section8 this proves the precise literal-input statement **SN(rho)=2**.

No all-filter or all-state statement is obtained. The unchanged generic-x qualitative barrier in OLD was read completely but is not needed for this exact input proof.

## 10. Serial resolution and exclusions

**New load-bearing identities NOT_RECONSTRUCTED: NONE.** The new two-product factorization, complete character average, all five support certificates, all six diagonal/fifteen off-diagonal identities, positive weights, full37-term assembly and normalization have explicit written reconstructions above. The same-input inherited ingredients were rebound rather than accepted by verdict transfer.

**Old21-pair weighted identity: still NOT_RECONSTRUCTED.** Neither its literal JSON coefficients nor any historical unadmitted computation is validated or made admissible by this successor. The old MAJOR gate remains in v30-B's immutable history; it is no longer load-bearing for the new upper-bound route.

At the stated written level, the successor establishes that this particular x1111 PPT input is Schmidt-two and cannot be detected negatively by a universally two-block-positive witness. Parent may disposition this mathematical result as retiring that input from an SN3 search. It does NOT recover a historical N4 solver result or child exit: those remain UNKNOWN/unestablished. No retry, new native launch or GO. Unrestricted P44, a different PPT/SN3 example or an all-state theorem remains open. No formal/kernel/finite-replay/cross-vendor/human/novelty acceptance is claimed.
