# Septic interface III — elementary lossless FOUR-member test for one unrestricted common numerator

Owner **InfoSPR7-2**, same info-2. Actual `/bin/date` immediately before this write: **Tue Oct 27 16:02:54 PDT 2026**.
**WRITTEN author-unreviewed reconstruction of an exact interface, not a new universal existence theorem or novelty claim.**

## 1. Authority, inputs and what is not being resumed

This step uses the ORIGINAL frozen S1 definition-first release, whose scope explicitly requires any finite-member reduction to be proved, and Main's15:08 standing direction to continue admissible inside-S1 steps without per-step approval. It does NOT treat the later statement-only primary admission as permission to read paper proofs or prove reciprocal equivalence.

Correctness inputs are ONLY the original37LF problem definitions in packet SHA256 `9df2b558c03b2aac8cefb786be5a2a0802de822724bcd6ee60b47d0205fc61f6`, real polynomial evaluation and elementary convex combinations. The newly read Wang–Yu Lemma4 is a statement comparison, NOT an assumed theorem or proof premise. No source proof/example/bibliography was opened. No old contact/phase-comparison, inverse, profile, work/ or metadata-map route is used. The accepted STOP before the further higher-contact branch remains NONINPUT.

Historical authorship and the new primary statement exposure are disclosed, not erased by this proof. The current v1/v2 candidate remains unreviewed; the new cadence gap in checkpoint003 remains a distinct permanent finding. No independent-provenance or cognitive non-influence certificate is claimed.

## 2. Full original variables and four ACTUAL members

Write the original monic box in ascending order:
`K={a(s)=s^7+a_6s^6+...+a_1s+a_0 : a_j in [l_j,u_j], j=0,...,6}`.
All intervals are finite, closed, nonempty and may degenerate. Assume EVERY member of this SAME K is strictly Hurwitz. The numerator b is ANY fixed real polynomial of EXACT degree7, unrestricted in all its coefficients. No numerator profile is imposed.

Define two even-coefficient polynomials
`U_-(s)=l_0+u_2s^2+l_4s^4+u_6s^6`,
`U_+(s)=u_0+l_2s^2+u_4s^4+l_6s^6`,
and two odd-coefficient polynomials
`V_-(s)=l_1s+u_3s^3+l_5s^5+s^7`,
`V_+(s)=u_1s+l_3s^3+u_5s^5+s^7`.
For epsilon,eta in{-,+}, set `k_(epsilon,eta)(s)=U_epsilon(s)+V_eta(s)`.

Each k is an ACTUAL monic degree7 coefficient vertex of K: every coefficient is one of that coefficient's own permitted endpoints, and even/odd choices are independent. They are therefore Hurwitz by the original ALL-member hypothesis. They are not freely selected stable polynomials from unrelated boxes. Some of the four may coincide when intervals degenerate; the statement is an AT-MOST-four-member test in that case.

## 3. Exact pointwise value rectangle, proved from the definition

For t=w^2>=0 write
`a(iw)=E_a(t)+iw O_a(t)`,
`E_a(t)=a_0-a_2t+a_4t^2-a_6t^3`,
`O_a(t)=a_1-a_3t+a_5t^2-t^3`.
These are direct real/imaginary evaluation identities. They are not a root-band/phase-contact argument or a restriction on b.

Since t,t^2,t^3 are nonnegative, the exact extrema are
`E_-(t)=l_0-u_2t+l_4t^2-u_6t^3`,
`E_+(t)=u_0-l_2t+u_4t^2-l_6t^3`,
`O_-(t)=l_1-u_3t+l_5t^2-t^3`,
`O_+(t)=u_1-l_3t+u_5t^2-t^3`.
Thus E_-<=E_a<=E_+ and O_-<=O_a<=O_+ for EVERY actual a and t. The choices realizing these extrema are exactly U_-/U_+ and V_-/V_+ above; crucially those coefficient choices do not depend on t.

Conversely the image of each independent parity coefficient box under its real linear evaluation map is the ENTIRE closed interval between its extrema: any intermediate value is realized by a convex combination of the two extremal coefficient vectors. The two parity boxes are independent, so their choices can be combined into ONE actual a in K. Therefore for each fixed w the actual value set is the full rectangle with the four corner values k_(epsilon,eta)(iw), with an interval/point collapse when appropriate.

For any particular a,t choose alpha,beta in[0,1] with
`E_a=(1-alpha)E_-+alpha E_+`,
`O_a=(1-beta)O_-+beta O_+`.
If an interval collapses, choose its parameter0; no division by a zero width is used. The value a(iw) is the convex combination of the four k(iw) with weights
`(1-alpha)(1-beta), (1-alpha)beta, alpha(1-beta), alpha beta`.
They are nonnegative and sum to1. At w=0 the imaginary component simply vanishes; the same formula remains valid. Negative w is covered by the same evaluation and real-coefficient conjugation.

The weights may depend on a AND t. This is a pointwise VALUE-set identity, not a claim that the seven-dimensional coefficient box is the coefficient convex hull of four polynomials. No fixed coefficient-space weights across frequencies are asserted.

## 4. Complete fixed-numerator equivalence in the ORIGINAL b/a orientation

**Theorem.** For EVERY actual K above and EVERY fixed unrestricted exact-degree7 real b,
`Re[b(iw)/a(iw)]>0 for EVERY a in K and EVERY finite real w`
IFF
`Re[b(iw)/k_(epsilon,eta)(iw)]>0 for all four fixed members and EVERY finite real w`.

**Necessity:** the four k are actual members of K.

**Sufficiency:** fix ANY actual a and ANY finite w. Hurwitz stability gives nonzero denominators for a and for all four k. Define the real pairing
`P_(a,b)(w)=Re[b(iw) conjugate(a(iw))]`.
It is real linear in the complex value a(iw). The four ratio inequalities are equivalent to positivity of their P values, because each denominator modulus squared is positive. Apply the exact convex value representation in §3. Then P_(a,b)(w) is a convex combination of four strictly positive numbers and is strictly positive. Divide by the positive |a(iw)|^2. Since a,w were arbitrary this is the original conclusion.

This proof does not assume a/b SPR, numerator Hurwitz stability, reciprocal equivalence, a Kharitonov stability theorem, an edge theorem, or any paper's unread proof. It holds in the b/a orientation DIRECTLY. Analyticity of b/a in the closed right half-plane follows from its actual denominator a being Hurwitz, not from a condition imported after swapping numerator and denominator.

The numerator is the SAME b at all four members and all frequencies. The proof does not permit four separately chosen numerators or a b chosen after w. Its exact-degree constraint is unchanged. Fixed b values at unsampled frequencies have not been interpolated or replaced.

## 5. Strictness at zero and infinity, degeneracy and normalization

The theorem includes w0 explicitly. There P_(a,b)(0)=a_0b_0, and every actual monic Hurwitz member has positive a_0. The four constants are the two permitted extrema, with possible repetitions; positivity of their pairings gives positivity for every actual constant. Nothing is divided by an interval width or by w.

Infinity is not an additional finite physical frequency. For an exact-degree7 b and monic degree7 a, the leading term of the real pairing as a polynomial in t=w^2 is b_7t^7. Strict finite-frequency positivity for even one of the four Hurwitz members forces b_7>0: it is nonzero by exact degree, and a negative leading sign would make the pairing negative for sufficiently large t. Thus the source/registered finite-frequency convention does not lose the required leading sign in this equivalence. Positive rescaling could normalize b_7 to1 without changing any inequality; no normalization is assumed in the theorem.

Equivalently the pairing divided by(1+t)^7 extends with value b_7 at infinity. Its four fixed-member functions are continuous and positive on the compactified half-line, hence have a common positive minimum. Section3 transfers that minimum to every actual a at the SAME t. The normalized denominator modulus is continuous/positive on the compact original box times compactified half-line, with value1 at infinity. This also retains a uniform original ratio margin for this fixed b and box, rather than assuming one on a noncompact frequency set.

If any coefficient interval is degenerate, the same extrema and convex identities are valid. Coincident corner members are simply repeated values; strict positivity is not converted to a non-strict condition. If all intervals degenerate the theorem reduces to the single actual denominator, not a limit argument requiring positive widths.

## 6. Original-object callers and effect on the current candidate frontier

The theorem has both original callers:

- ONE unrestricted exact-degree7 b positive against the four FIXED actual corners is an actual solution for EVERY member of the original K, at EVERY finite real frequency including0.
- If the original K has no such b, neither does its coupled four-member subfamily. Conversely lack of one common b for that actual four-member subfamily excludes an original common b. The four members must still arise from the SAME seven independent coefficient intervals with the displayed tied endpoint pattern.

For the current v1 compact vector construction, the value representation is valid against EVERY coefficient vector b of degree at most7, so it is an identity of the representing linear functionals at each frequency. Consequently the joint vector convex hull generated by ALL members is EXACTLY the one generated by these four actual member curves. Their values at infinity also agree. This discharges the finite-member interface without changing v1's exact-degree caller or its finite support theorem. Any proposed dual still needs actual frequencies and positive weights; this is not a realized critical tuple or an original counterexample.

The v2 low-frequency exclusions remain author-WRITTEN candidate claims at their own full proofs and review boundary, not automatically adopted by this new reduction. A combined gate must distinguish the new elementary four-member interface from any still-unreviewed higher-contact analysis. The accepted STOP on the further higher-contact/phase-comparison route remains unchanged.

**What is NOT paid:** existence of ONE b for every such coupled four-member family. Individual Hurwitz corner polynomials do not by themselves supply a SAME common b; separate witnesses are not that quantifier. No degree7 existence theorem has been inferred from the source's degree<=4 synthesis statements. The reduction is an exact original-object analysis interface, not a sufficient-only numerator family or a solution of synthesis.

## 7. Primary comparison and next genuine question

The just-completed Wang–Yu source audit observed an arbitrary-order fixed-b four-member STATEMENT in its Lemma4, in the target b/a direction. The present proof derives an explicit septic four-member interface from the INITIAL registered definitions, without assuming that statement or reading source proofs. This is classical-content/input reconstruction; NO novelty or new SOTA result is asserted. Identifying the exact historical naming/proof ancestry of these corners would require the separately admitted source ranges and is not needed for the correctness argument here.

The useful remaining original question is now sharply finite on the denominator side but not on frequency: construct a SAME unrestricted septic numerator for these four coefficient-coupled actual members, or derive a genuine eligible four-member obstruction and its actual robustly Hurwitz box. The shared endpoint ties must be used; four arbitrary individually stable polynomials are not a substitute. There is no permission to return to the stopped contact/phase-comparison route or fit a selected box/critical tuple.

The exact4 reduction is more than a coordinate encoding, but as a classical interface proof it is not presented as a new universal scientific solution. It supplies the previously missing finite-member caller in the present definition-first record. Novel coupling beyond that caller remains the original research obligation.

## 8. Execution and assurance

Named ordinary facts: elementary real/complex polynomial evaluation, signs of nonnegative powers, linear images/convex combinations of closed intervals, nonvanishing of a Hurwitz polynomial on the imaginary axis, and continuity/compactness. The special four-member and all-boundary applications are proved inline. No outside theorem, scalar numeric example, selected parameter/box/state, root computation, scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, modelCLI/nested agent/newGO, old proof body or source-paper proof was used.

Same existing owner/new exclusive root; old closed round frozen. All original findings plus the checkpoint003 cadence gap remain permanent. SPR78 outside S1, the stopped higher-contact route, every ZERO consumer, HOLDv2, N4 UNKNOWN with historical exit unestablished and auxiliary214 STOP persist. No formal/kernel/human/configured-family/executable/novelty, primary-proof authentication or parent adoption is conferred. Full research deadline remains2026-10-31T21:23:27.000Z.
