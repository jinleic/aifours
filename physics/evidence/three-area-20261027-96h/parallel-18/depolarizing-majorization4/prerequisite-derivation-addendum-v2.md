# physics-2 — global one-body budget, all-projector variance strengthening, and an exact trace-only ceiling obstruction

Actual `/bin/date` before this NEW additive write: **Tue Oct 27 15:04:50 PDT 2026**. Owner PhysicsDepol4-2, SAME narrow S1 release/new exclusive root. This does NOT edit `prerequisite-derivation-v1.md` (194LF/22276B, SHA256 `399da1ebefb71d352bb4f473dc390c49c704066e6831c689402e246a741f6720`).

**NEW WRITTEN ordinary-input candidate; not reviewed/adopted/novelty-cleared/formal/kernel/executable.** No scientific arithmetic program, calculator, selected state/noise/boundary/decimal probe or new source read. No original majorization result or physical violating witness is asserted. All old NONINPUT/STOP/HOLD/ZERO/exposure limits remain. The stated proof inputs are the PRIMARY-confirmed channel and ordinary finite-dimensional spectral/operator facts, not any old candidate or private method guide. No clean-cognition/noninfluence claim.

This is a genuine ALL-rank3 strengthening of the previous cycle's two-equality-class constraint, not a promotion of that proper class to the whole Grassmannian. It also pays an exact universal failed step: the resulting trace/purity-to-largest-eigenvalue estimate remains strictly above the original product-reference ceiling throughout every nondegenerate parameter, so that particular scalar inference cannot close k3. No noise value is selected to establish this obstruction.

## 1. Inputs and unchanged original convention

S1 controls/release/packet pins and actual prebody ACK are as recorded in v1. PRIMARY admitted and read ONLY for its abstract/Introduction definition: Song–Wang–Tomamichel–Fang, [arXiv:2609.37240v1](https://arxiv.org/html/2609.37240v1), Eq.(1) `D_(p,d)(X)=(1-p)X+(p/d)Tr(X)I`, `0<=p<=d²/(d²-1)`, and Eq.(2) arbitrary output spectrum majorized by product-reference output. d2/n4 gives exactly the registered physical0<=p<=4/3. The comparison is not reversed. No primary proof was read or used.

Keep EVERY density rho (pure or mixed), EVERY actual complex rank3 orthogonal P on H=(C2)^tensor4, and EVERY physical p. Let E_i be normalized one-qubit partial trace as in v1, and define the basis-independent local conditional defect

`L_i(P)=Tr[(P-E_i(P))²]`, `E(P)=sum_i L_i(P)`.

The symbols here are freshly defined finite-dimensional quantities, not imported old ENERGY/moment/source-route claims. The preceding v1 only proved E(P)>=4 under TWO local saturation hypotheses; it did NOT prove a global bound4. That stronger global assertion is not used below and remains unproved in this work.

Ordinary facts: Hermitian spectral theorem, Pauli trace orthogonality, local SU2 rotations/permutations preserving tensor-weight spaces, finite Ky-Fan variational principle, Hilbert–Schmidt orthogonal projections, Cauchy–Schwarz, and exact polynomial inequalities. No catalogue, tested tuple, physical ansatz or research import is invoked.

## 2. Sharp universal one-body budget and its ENTIRE equality set

For each site i let the REAL Bloch trace vector be `b_i=(Tr(P sigma_x^i),Tr(P sigma_y^i),Tr(P sigma_z^i))`, and let s_i=||b_i||. These are defined from the SAME P; no independent marginal assignment is permitted.

**Theorem4.** EVERY actual complex rank3 P satisfies

`sum_i ||b_i||² <=20`.                              (B1)

Equality holds IFF, after physical-site permutation, P has the form

`P=|a,b><a,b| tensor [I_(kl)-|c,d><c,d|]`,            (B2)

where a,b,c,d are ARBITRARY single-qubit unit vectors. This is the COMPLETE equality classification, not a chosen four-vector test. No member is instantiated or used in an original-channel comparison.

**Full bound proof, including zero/tied marginals.** Independently choose each local axis along b_i if nonzero; if zero choose any axis. Relabel sites so s1>=s2>=s3>=s4>=0. The Hermitian operator

`H=sum_i s_i sigma_(n_i)^i`

has mutually commuting local terms, and `Tr(PH)=sum_i s_i²`. Its eigenvalues are the signed sums of the s_i. The three largest, COUNTING multiplicity, have total

`3(s1+s2+s3+s4)-2s4-2s3=3s1+3s2+s3+s4`.             (B3)

To see completeness without an enumeration: the maximum uses no sign flips; the two smallest distinct nonempty flip costs are s4 and s3. A subset containing any other index costs at least s3, and a subset containing both smallest costs at least s3. Ties/zeros merely repeat eigenvalues with their correct multiplicities; the same total remains valid. Ky-Fan's variational principle for the actual rank3 P therefore gives

`sum_i s_i² <= 3s1+3s2+s3+s4`
` <=sqrt(3²+3²+1²+1²) sqrt(sum_i s_i²)`.

If all s_i vanish the result is immediate; otherwise divide by their positive Euclidean norm to obtain(B1). No physical state or parameter was selected, and this elementary Ky-Fan use on the commuting H does NOT assume the unproved channel-majorization target.

**All equality cases, necessity.** If the left side is20, equality in both inequalities forces `(s1,s2,s3,s4)=(3,3,1,1)` and P to be the top-three spectral projection of H. At these FORCED equality coefficients the top-three space is precisely the first two local plus directions tensor the two-qubit space excluding the last two local minus directions together. The third/fourth eigenvalue gap is strict: the one-smallest-flip costs are1,1 and the next cost is2. Thus there is no omitted degenerate spectral mixing. This gives exactly(B2), with relabelled local unit vectors.

**All equality cases, sufficiency.** For ANY a,b,c,d, the bracket in(B2) is a genuine rank3 projection and the fixed first-two factor has rank1, so P is an actual rank3 projection. Its first-two Bloch trace lengths are3,3, and each of the remaining two has length1 (the trace of a local Pauli against I4 vanishes and the omitted rank1 product has unit local Bloch vector). Their squared lengths sum to20. This proves the converse for ALL complex choices, not just real bases.

## 3. A global ALL-projector conditional-defect bound

Expand P in the standard four-qubit Pauli tensor basis:

`P=(1/16)sum_s c_s sigma_s`, `c_s=Tr(P sigma_s)`.

For weight w let `A_w=(1/16)sum_(|s|=w)c_s²`. Orthogonality and P²=P give

`A_0=9/16`, `sum_(w>=1) A_w=39/16`,
`A_1=(1/16)sum_i ||b_i||²<=20/16`.                  (B4)

All A_w are nonnegative. E_i removes exactly the terms nonidentity on site i, so

`E(P)=sum_(w=1)^4 w A_w`
` >= A_1+2(39/16-A_1) >=29/8`.                      (B5)

In fact the inequality is STRICT for EVERY rank3 P. Equality in(B5) would require both A1=20/16 and A3=A4=0. But in the complete equality class(B2), in locally aligned axes the two fixed pure factors have Pauli action+1 on Range(P), while either remaining one-body trace has absolute value1. Their product is a NONZERO weight3 Pauli trace. Local rotations preserve each Pauli-weight subspace and its total squared norm, so A3>0 also in the original basis. Contradiction. Thus

`E(P)>29/8 for EVERY actual complex rank3 P`.         (B6)

This is not claimed to be the optimum, a computed margin, a uniform numeric refinement beyond29/8, or the unproved bound4. The proof gives no new epsilon cutoff or original-channel comparison. It is a global constraint on actual rank3 P; the earlier local-equality theorem alone was not substituted for this proof.

## 4. Universal full-channel purity bound, retaining all physical parameters

Let t=1-p and x=t². Throughout the confirmed physical range,0<=x<=1. The channel multiplies each Pauli tensor of weight w by t^w, so for the SAME `B=Lambda_p(P)` one has

`Tr(B²)=9/16+sum_(w>=1) x^w A_w`.

For EVERY w>=2, x^w<=x². Using the ALL-projector budget(B4),

`Tr(B²)<=9/16+x A_1+x²(39/16-A_1)`
` <=(9+20x+19x²)/16`.                               (B7)

For0<x<1 the bound is STRICT: equality would require the same impossible simultaneous conditions A1=20/16 and A3=A4=0. At x0, all nonconstant Pauli tensors vanish and B=(3/16)I; at x1 the channel in the physical interval is the identity and Tr(P²)=3. These are all forced degenerate cases of the universal formula, not selected endpoint probes. Nothing is divided by x or1-x.

Equivalently, since trace B=3,

`Tr(B-B²)>=(1-x)(39+19x)/16`,                        (B8)

strict for0<x<1. This is a trace statement for the actual SAME-P full channel, not a uniform lower bound against every input rho. v1's exact trace-to-state inference obstruction remains applicable; no such invalid promotion is made.

## 5. Exact obstruction to closing original k3 from THIS trace/purity estimate

For ANY positive effect B on dimension16 with trace3, let z be its largest eigenvalue. Cauchy–Schwarz on the other15 eigenvalues gives

`Tr(B²)>=z²+(3-z)²/15`
` =9/16+(16/15)(z-3/16)²`.

Combining with(B7), and also B<=I for the physical unital channel, yields the valid ALL-rho bound

`G=Tr(rho B)<=min(1,U(tau))`,
`U(tau)=[3+tau sqrt(300+285tau²)]/16`,
`tau=|1-p| in[0,1]`.                                (B9)

This step uses only actual B; no independently fabricated spectrum is asserted to be physically realizable.

The original product reference has ordered local eigenvalues a=(1+tau)/2 and b=(1-tau)/2. Its largest output eigenvalue is a^4; the next four are a³b, so its TOP THREE sum is

`R3(tau)=a^4+2a³b=(1+tau)^3(3-tau)/16`
` =[3+8tau+6tau²-tau^4]/16`.                         (B10)

This includes all degeneracies and both p<=1/p>=1 conventions. It is derived directly from the confirmed channel on the reference, not borrowed from a legacy candidate.

For EVERY0<tau<=1,

`sqrt(300+285tau²)>=sqrt(300)>14`,
`8+6tau-tau³<=14`.

Therefore U(tau)>R3(tau) throughout that ENTIRE interval. For0<tau<1, R3(tau)<1 because the reference is strictly positive and thirteen eigenvalues remain outside its top-three sum. Hence **even the capped bound min(1,U) is strictly ABOVE the required ceiling on the whole nondegenerate interval**. At tau0 both formulas are3/16 and the channel is completely depolarizing; at tau1 the cap1 matches the trivial identity-channel ceiling. No particular tau or decimal has been tested.

Thus(B7) is a genuine universal actual-projector constraint, but **the specific Cauchy trace/purity-to-largest-eigenvalue inference(B9) does NOT prove original k3 at any nondegenerate parameter**. This is a full analytic failed-step result, not a selected numeric margin, relaxed witness or claim that original majorization is false. It also does NOT establish impossibility of every future argument using purity together with additional actual-object constraints. A stronger SAME-state/operator coupling is still needed; no all-route exhaustion is claimed.

## 6. Actual-object caller, exact remaining prerequisite and next control

Every original rho,p,complex rank3 P supplies(B1)–(B9). Conversely(B2) is a complete GENUINE rank3 equality family, not an arbitrary list of spectra; its universal converse was proved without choosing a member. v1 already supplies the exact original variational equivalence: a strict trace violation for an actual rho,P,p implies original Ky-Fan3 violation, and any original k3 violation supplies such a maximizing P, including degeneracy. NOTHING in this addendum exhibits such a violation or closes the missing ceiling.

The material new ALL-projector step beyond v1 is(B1)–(B8), not another proper state region. The exact barrier is(B9)–(B10): an input-conditioned/operator-level implication stronger than this total-purity control is necessary for this route to reach the original conclusion. The global rank3 bound E>=4 remains UNPROVED; its validity or failure has not been probed with selected projectors. Parent-adopted biseparable/regional/parity/central/k2/k4 claims are neither expanded nor needed as correctness premises for this derivation.

All mathematics is WRITTEN, elementary, unreviewed and not asserted novel. No old proposed source or protected guide was opened; prior exposure is NOT denied and clean-cognition/noninfluence is NOT certified. This additive file preserves v1 unchanged. Next admitted work must target the actual SAME-state gap rather than append a renamed scalar trace bound or revisit the excluded histories. If an essential source/input-separation premise is unavailable, report that precise prerequisite; do not silently replace the physical problem by an enlarged one. Main full-source/full-review read is still required before adoption.

Same18/new OWN only/old roots read-only/HOLDv2/N4UNKNOWN historical exit unestablished/aux214STOP/ALLprocessfindings and ENTIREZERO consumers. No scientific computation/selected-control-state-noise-boundary-decimalprobe/nestedagent/modelCLI/newGO/Git/delete/publication/contact/infrastructure. Science ends2026-10-31T21:23:27.000Z; continuous work requested not certified; substantive actual-clock cycle evidence only, no heartbeat/ACK/timer fiction.
