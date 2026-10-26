# Written reconstruction — conditional four-qubit depolarizing regions

Observed immediately before writing: **2026-10-23T14:18:28-07:00**. Reviewer PhysicsPPT44, acting under `peer-review-wave-eighteen-v1.json`. This is the single assigned bounded peer review; it does not replace the reviewer's P44 problem.

## Snapshot and verdict

Source: `physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/proof-v1.md`.

SHA-256 actually observed using `shasum -a 256`: **`5e801b156b8f19ce4048dbe8a5ec3fb0f6499eba1ca42b2cdddcaa8d61a91b7e`**, matching the parent's pin. All223lines were read, along with the actual selection, inherited baseline README, and the primary Song–Wang–Tomamichel–Fang conjecture/parameter definitions in the retained2609.37240v1 source.

**Verdict: no substantive mathematical defect found in TheoremsA, B and CorollaryB1 under their displayed pure-state/convex-decomposition hypotheses.** No FATAL, MAJOR or MINOR finding is raised. This supports a **scoped in-harness written check**, not unrestricted four-qubit majorization, a globally closed new index, a novelty verdict, or parent acceptance.

## 1. Pauli identities reconstructed (source73–115)

Use the real coefficients `r_P=Tr(rho P)` for Hermitian Pauli strings, so `Tr(PQ)=16 delta_PQ`. With A_j the sum of their squared weight-j coefficients, purity gives `1+A1+A2+A3+A4=16` and A1=R.

For each triple I, `Tr(rho_I^2)=2^(-3)` times the sum of squared coefficients supported inside I. On summing the four triples, weights0,1,2,3 occur with multiplicities4,3,2,1. Thus their summed purities equal `(4+3R+2A2+A3)/8`. The four complementary one-qubit purities sum to `(4+R)/2`. Pure-state Schmidt spectra identify these two quantities. Consequently `A3=12+R-2A2`; combining with total purity gives `A4=3-2R+A2`.

Spin flip multiplies a Pauli string of weight j by `(-1)^j`, and for pure rho the overlap with its flipped rank-one projector is the squared spin-flip amplitude C. Hence

`16C=1-R+A2-A3+A4=4(A2-R-2)`.

It follows that `A2=R+2+4C`, `A3=8-R-8C`, `A4=5-R+4C`, agreeing with source99. This uses pure-state compatibility; it is not asserted for arbitrary mixed inputs.

For X2, the coefficient on a supported weight-j string is `binom(4-j,2-j)/4`, yielding `(3/2)I+(3/4)P1+(1/4)P2`. For X3 it is `binom(4-j,3-j)/8`, yielding `(1/2)I+(3/8)P1+(1/4)P2+(1/8)P3`. Pauli orthogonality therefore gives, independently of a sample state,

`Tr X2=24`, `Tr X2^2=36+9R+A2=38+10R+4C`,
`Tr X3=8`, `Tr X3^2=4+(9/4)R+A2+A3/4=8+3R+2C`.

## 2. Rank13 and the moment lemma reconstructed (source51–71,117–131)

For any2by2 operator Y, `sum_{a=x,y,z} sigma_a Y sigma_a=2Tr(Y)I-Y`; the same linear identity applies with an ancillary tensor factor. Summing over the four sites gives

`Z=2X3-4rho`, hence `X3=2rho+Z/2`.

For pure rho, each of the twelve summands defining Z is a positive rank-one projector. The support of X3 lies in the span of psi and those twelve Pauli-orbit vectors, so rankX3<=13. No eigenvalue ordering of Z and no old Z-majorization lemma is needed. This is an upper bound, not a statement that every input has rank exactly13.

For a positive operator of rank<=r, append zeros to length r. With S its leading k-sum, separate Cauchy–Schwarz on the first k and last r-k entries gives

`q >= t^2/r + [r/(k(r-k))](S-kt/r)^2`.

Sortedness puts S on the branch `S>=kt/r`. Therefore comparison with the same quadratic at any B>=kt/r implies S<=B. This establishes the source lemma without the invalid inference “smaller purity implies majorization”. Rank padding remains valid when the actual rank is smaller than r.

## 3. Central-index thresholds and the channel bridge (source133–159)

For a computational product input, each diagonal entry of T_s is `binom(z,s)` where z is its number of zero bits. Thus T2 has spectrum `6,3^4,1^6,0^5`; at k=6,...,10, `B=k+13`. With t=24 and r=16, the moment threshold simplifies to

`(k+13)^2/k+(11-k)^2/(16-k)=32+169/k+25/(16-k)`.

Subtracting38 gives `H_k=-6+169/k+25/(16-k)`, which reproduces **all five exact thresholds** printed at source29–33. Their R-only corollaries are `(H_k-4)/9`, reproducing that column too. The monotone-branch comparison B>24k/16 holds throughout this range. Since H_k decreases on this interval, k=10 is the controlling central threshold226/15.

For `q=min(p,2-p)`, all five expansion coefficients `(1-q)^s q^(4-s)2^(s-4)` are nonnegative. Here q lies in[0,1] for every physical p in[0,4/3]. Endpoints are understood by the continuous polynomial expression, without a problematic division.

X0=I and X4=rho are immediate. Diagonalizing the four single-qubit marginals expresses X1 as a convex combination of local bit-flip conjugates of T1; Ky-Fan convexity gives its required bounds. X3 is positive of trace8, while K_k(T3)=8 for k>=5. Thus at central k all other subset-size bounds are unconditional.

Every T_s is simultaneously diagonal and nonincreasing in the common number-of-zero-bits order, so their top-k sums add with the nonnegative coefficients. Ky-Fan subadditivity proves the asserted **same k**, all-q channel bound, not just an X2 inequality.

Finally, direct algebra gives `sigma_y D_p(X)^T sigma_y=D_(2-p)(X)` for every2by2 X. Tensoring is **global transpose followed by unitary conjugation**, not a nonpositive partial transpose of the input. It preserves the entire output spectrum. Therefore the p>1 extension is sound, including the product reference's reordered spectrum.

## 4. Complete-majorization region (source161–197)

Condition `3R+2C<=157/36` and C>=0 imply

`10R+4C<=(10/3)(157/36)=785/54`,

so `Tr X2^2<=2837/54`. The smallest of the listed k=2,...,10 reference thresholds is796/15, and

`796/15-2837/54=143/270>0`.

I reconstructed the table directly from B=9,12,15,18,19,20,21,22,23 and t=24; all entries agree. At k=1, X2<=6I termwise; at k>=11 the reference has reached trace24. Hence X2 majorization really holds at every index for this input region.

For X3, the same condition gives purity at most445/36. With r=13,t=8 the nontrivial thresholds are

`25/2+9/11=293/22`,
`36/3+4/10=62/5`,
`49/4+1/9=445/36`.

All exceed or equal445/36; the near-tight k=3 gap is exactly `62/5-445/36=7/180>0`. The branch condition B>=8k/13 holds for all three. The k=1 bound is X3<=4I termwise and k>=5 is its trace bound. Hence X3 also has every required partial-sum bound. The common-order expansion from the previous section now applies at all fifteen channel indices.

The source's mixed-state extension is precisely the valid convex-hull statement: each pure component must satisfy the displayed region condition. It does **not** infer membership in that convex hull from a general mixed state's small local Bloch vectors. Source45 and197 state the needed caveat explicitly.

## 5. Spin-flip compatibility and scope (source199–223)

Across any qubit versus its complement, write psi with Schmidt coefficients sqrt(mu),sqrt(1-mu). Local-unitary covariance preserves the modulus of the global spin-flip amplitude. The qubit flip is off-diagonal in this basis, leaving two cross terms of coefficient sqrt(mu(1-mu)), each with overlap modulus at most one. Thus `sqrt(C)<=2sqrt(mu(1-mu))`, equivalently `C<=1-|r_i|^2`. Summing establishes `R+4C<=4`. Consequently

`3R+2C<=2+(5/2)R<=157/36` when `R<=17/18`.

This verifies B1, including the R=0 pure-state region. Products have R=4,C=0 and are outside this sufficient region, despite saturating the actual majorization conjecture; so no unrestricted conclusion follows.

The artificial spectrum at source221 has trace24, squared norm `6*(10/3)^2+10*(2/5)^2=1024/15`, and K6=20>19. Its earlier-index sums obey the stated reference bounds. It illustrates failure of purity-only sufficiency; it is **not** represented as a compatible X2(rho) or a channel counterexample.

The inherited baseline README still leaves central indices globally open, and the primary2609.37240v1 Eq.(2) quantifies over arbitrary inputs and physical parameters. This manuscript adds conditional input regions, not global-index closure. The state-dependent theorem may be useful specialist progress, but originality or priority has not been established by this review.

## Evidence boundaries

- Actual work: complete source/selection read, observed source hash, independent written reconstruction of all load-bearing formulas, threshold arithmetic, rank argument and channel bridges.
- Shared inputs: the author's proof and the parent's focus; not a blind reconstruction or different-model-family guarantee.
- No scientific script, SDP, eigensolver, numerical spot check, executable certificate replay, build/test/formatter, nested agent or modelCLI was run.
- No formal/kernel or human review. No acceptance of source-wide claims outside the read scope. No novelty clearance.
- Parent full-check gate remains separate. The reviewer resumes its own P44 next construction obligation after returning this file.
