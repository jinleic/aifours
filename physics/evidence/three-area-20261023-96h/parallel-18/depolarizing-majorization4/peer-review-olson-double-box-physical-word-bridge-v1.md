# v31-B — Olson double-box actual-word/parity/cyclic bridge review

Actual returned clock preceding this review: **Sun Oct 25 04:35:12 PDT 2026**. Reviewer **PhysicsDepol4-2**, different-domain supplied-proof applicability slice. This is WRITTEN reconstruction only, not blind, cross-vendor, human, formal/kernel or novelty acceptance. HOLD v2 and parent erratumv7 remain binding.

## 1. Snapshot, coverage and exposure

Assignment: `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v31.json`, v31-B, SHA256 `73cf8654ddca55870d137b3e447355274c54a733451fa9aa3d1d6a1dc3dcf5d8`.

Reviewed source: `mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/proof-FIXED-ROTATION-DOUBLE-BOX-BAND-CLOSURE-v1.md`, **LF1–220, complete**, SHA256 `26b39995d5a7816233fd992ef11b6f193d2e4615f5ede2a4a340b4155e32c86f`.

Mandatory literal packet: `peer-review-wave-v31-olson-double-box-physical-word-bridge-sources-part1-v1.md`, SHA256 `04eafa432d8bd5dace5636c60338f4b834479a778d304947ad87059188a3e762`. Its complete229-line body, containing every source LF1–220, was actually read in two ranged calls; no truncated source line was left unread. Both author-source and literal-packet hashes were observed by metadata-only shasum and match the frozen manifest. This is not a claim of a separately programmed literal-packet regeneration check.

Binding `parent-evidence-erratum-v7.md` was read completely, LF1–39, observed SHA256 `d5e1911bba6549684c93b2e910fac66eb44c353ae5dea2a8d1555516946e8d05`.

Exposure ACK was written before new reconstruction: `peer-review-olson-double-box-physical-word-bridge-ack-v1.json`. It discloses the parent assignment/headline, first source window, prior old-branch review filename and run-ledger exposure. I have NOT read the disjoint v31-A review, and no parent correctness conclusion was supplied or assumed. No scientific eval, interpreter, arithmetic/symbolic program, enumeration, certificate replay, solver, CLI or nested agent was used for this review. Metadata clocks/hashes only.

All line references below are to the pinned220-line AUTHOR SOURCE, not packet display line numbers.

## 2. Verdict and exact interface to the disjoint algebra slice

**Assigned applicability slice: 0 FATAL / 0 MAJOR / 0 MINOR findings.** The dihedral multiplication, actual-position parametrization, integer size/parity, empty-selection exception, one-r0 parity completion and cyclic restoration all reconstruct at the literal stated quantifiers.

**Theorem DB is NOT fully reconstructed by v31-B alone.** This review is conditional on the following polynomial interface being separately reconstructed by v31-A:

- **A-IND:** Q_K has exactly the Boolean indicator values claimed at LF114–118.
- **A-COEFF:** equations(6)–(7) at LF120–130 are valid at the exact boundary M=3(p−1), with the indicated absence of all lower-u-degree terms.
- **A-SECOND:** the ordinary polynomial G at LF155–164 has degree_z<=p−1 and the p-variable signed sum in(15) vanishes.

Those algebraic statements were read and inspected for their role in the applicability chain. Their full independent coefficient/signed-box reconstruction is **NOT_RECONSTRUCTED in this disjoint slice**, not PASS inferred from the candidate headline or a prior low-band theorem. Subject to that interface, the source's use of Boolean points refers to legitimate actual selections, the asserted pattern of Q_K/G values follows, and the resulting contradiction has exactly the claimed R,F-band consequence.

## 3. Literal group law and product coordinate

**Reconstructed: LF9–13, LF85–108.**

For an ordered selected list `(v_j,e_j)`, repeated use of the displayed multiplication gives second coordinate `product_j e_j` and first coordinate

`sum_j (product_(h<j) e_h) v_j`.

This follows inductively by adjoining the next selected factor; it does not commute any selected factors. Only selected reflections change the sign prefix. Rotations, including zero-valued rotations, have e=+1 and therefore leave it unchanged.

In gap t, the selected-reflection prefix parity is u_t. Hence a selected rotation of value x in that gap contributes `(-1)^u_t x=(1−2u_t)x` on Boolean points. The same prefix applies immediately before f_t because the intervening rotations have sign+1.

Reflection f_t is selected iff its endpoint colours differ. If the colours are0→1, its prefix sign is+1 and its contribution is+y_t. If1→0, its prefix sign is−1 and its contribution is−y_t. Equal colours omit it. These three cases are exactly `(u_(t+1)−u_t)y_t`, including the zero cases. Thus the reflection-coordinate summation by parts is

`sum_(t=1)^F (u_(t+1)−u_t)y_t`

` =sum_(t=2)^F (y_(t−1)−y_t)u_t`,

because u1=u_(F+1)=0 removes the two boundary terms. Adding the selected rotations yields precisely source(3), with its constant `sum_(r in K) x_r` and `−2x_r u_(g(r))` contribution for every actual selected rotation.

The total selected-reflection number is even, so the product's second coordinate is+1. Therefore it is the rotation rho_(V_K), not an arbitrary element whose sign coordinate has been forgotten. Identity is equivalent to V_K=0 in F_p once that parity has been established.

## 4. Actual cut, gaps, occurrence naming and completeness

**Reconstructed: LF52–71.**

The hypotheses give at least one rotation and at least one reflection for every prime p>=7. Around the ACTUAL cyclic word, the named occurrence r0 belongs to exactly one maximal gap of consecutive rotations between reflections. Cutting immediately after its preceding reflection places that gap at X1, ending at f1. This does not require r0 to be the first rotation in the gap or the gap to contain only r0.

There are exactly F named reflections f1,...,fF and exactly F rotation gaps. Empty gaps and several rotations in a gap are legitimate; g(r) records the gap of each named occurrence. The other p rotations remain p distinct occurrence variables even if some values or gap indices coincide. Selecting a subset of names never selects an occurrence twice.

For every u2,...,uF in{0,1}, the change rule selects one well-defined actual reflection subset. Starting at u1=0, the next colour is recovered uniquely from whether f_t is selected. Closure u_(F+1)=0 is exactly the condition that the total number of selected reflections be even. Consequently this parametrizes ALL even reflection subsets uniquely, not just a convenient family of alternating blocks. In particular, no selected reflections implies all colours equal the anchored zero colour, so u=0 is the unique empty-reflection configuration.

No rotation/reflection value needs to be nonzero or distinct. Empty gaps do not remove the corresponding reflection-colour variable. If repeated gap indices or values make two formal expressions coincide, the selections are still named actual occurrence subsets; the proof does not require distinct expressions or an injective map from values to subsets.

## 5. Integer selected size and the unique zero-size exception

**Reconstructed: LF75–83, LF136–149.**

For Boolean a,b, the integer `a+b−2ab` equals0 when a=b and1 otherwise. Therefore source(1) is EXACTLY `|K| + number of selected reflections`, not just a size congruence or an approximation. Boundary colours give its degree-two part exactly `−2 sum_(t=2)^(F−1) u_t u_(t+1)`; the initial and terminal adjacent products vanish.

K is used only when its cardinality is even. The selected reflection count is even, hence the actual total size is even. Every selected letter is one original occurrence, so the size lies in[0,N] with N=4p−1. As p is odd, the multiples of p in that interval are0,p,2p,3p; precisely2p is positive and even. Thus an indicated Boolean point with nonzero size has actual size2p, not p or3p and not an uncontrolled representative modulo p.

If nonempty even K is fixed, |K|>=2. There is then NO empty selection for any u. Under hypothetical absence of identity2p, the indicator Q_K must vanish at every Boolean point, giving(8).

For K empty, the total size vanishes iff no reflections are selected, and §4 showed that this occurs iff u=0. The product there is the empty product, hence identity. At every other indicated Boolean point, positivity and the parity/multiple argument give a forbidden actual identity2p. Therefore the exact delta-function pattern(9) follows, with no additional exceptional point from a zero reflection or rotation value.

In particular, a zero-valued rotation still contributes one to the integer selected SIZE. Its group value being identity does not turn a nonempty occurrence subset into the empty selection. This closes the possible zero-value loophole in the use of(8).

## 6. One actual r0 closes parity without changing highest-colour data

**Reconstructed: LF59, LF100–107, LF153–177; conditional use of A-COEFF.**

There are exactly p other named rotations r1,...,rp. Every actual subset A of them determines K(A) by source(12). If |A| is even, K=A is even; if |A| is odd, adjoining the DISTINCT actual occurrence r0 makes K even. K is empty iff A is empty. Every nonempty resulting K has at least two actual occurrences and has size at most p+1. In particular, selecting all p other rotations selects r0 as well because p is odd, and uses all p+1 available rotations legitimately.

Adding r0 changes the constant coordinate term by x0 and the integer size term by1. It does NOT change the reflection-selection map. Since r0 belongs to the anchored gap1 and u1=0, its purported linear-colour term `−2x0 u1` is identically zero. Its addition therefore changes neither L_K nor Z2. Other selected rotations in gap1 similarly have no colour-linear term; multiple rotations in that gap do not invalidate the assertion.

It follows DIRECTLY that `L_(K(A))(u)=L(1_A;u)` in(13), for every actual A, including repeated or zero x_i. No sum of selected rotations is being replaced by a virtual midpoint or a packet endpoint.

Crucially, the author does NOT substitute the Boolean parity function of A into V_K or Z_K before bounding the degree in z. V and Z have different constants for the two parity cases, and those actual changes are retained through the physical selection argument. Only AFTER A-COEFF removes dependence on the constant terms does the common highest-u coefficient identify G(1_A) with the appropriate signed Q_K sum. This is precisely the legitimate order of operations needed for the one-r0 bridge. No nonlinear parity polynomial is silently assigned degree one.

Under A-IND and A-COEFF, §§5–6 therefore force `G(0)=1` and `G(1_A)=0` for every nonempty A. If A-SECOND supplies the asserted strict-degree signed cancellation, the contradiction is applicable to the full word, not only to words satisfying a matching or gap-normal-form hypothesis.

## 7. Same selected positions return to original linear order

**Reconstructed: LF136, LF190–210.**

Write the original word as AB at the actual cut and the cut word as BA. The selected occurrences in A have a product P_A in their original internal order; similarly the selected occurrences in B give P_B. This definition also works if one selected portion is empty, taking its product to be identity.

The product of that SAME named selection in the cut order is P_B P_A. If it is identity, then

`P_A P_B=P_B^(-1)(P_B P_A)P_B=1`.

But P_A P_B is exactly the product of those selected named positions in increasing ORIGINAL index order. No new occurrence is selected, removed, revalued or permuted within either block. The cardinality remains exactly2p. The argument uses conjugation of the whole selected product, not an invalid assertion that arbitrary cyclic shifts preserve a nonidentity group element unchanged.

Thus the original-word failure hypothesis may indeed be transferred to the cut word in LF136, and any cut-word existence conclusion is restored to original order in §9. There is no cyclic-versus-linear selection gap.

## 8. Whole-source scope/import audit and exclusions

The complete source includes ALL actual words with R=p+1 and F=3p−2. The applicability reasoning uses no raw-matching bound, OLD/REF/SEL/IPGEN/GS/DS3 failure, nonempty residual assertion, inverse normal form, all-odd-block property, unique endpoint, or special type ordering. Those restrictions do not reappear covertly in the rotation names, cut, colour variables or K(A).

Accordingly, IF the disjoint algebra slice and parent composition settle the complete argument, the theorem applies to any lower residual word lying in this band simply by set inclusion. It does not require treating the correctness or completeness of every historical exclusion as an additional theorem. On a genuinely REF-avoiding word, an obtained selection cannot have K empty, because that would be an all-reflection identity2p selection. Its rotation count is therefore even and between2 andp+1, exactly as LF196 says.

This does NOT force a two-rotation selection. It does NOT put the selected subset into a maximum-matching packet family. The old L_MAX counterexample is therefore preserved rather than contradicted. An unrestricted actual identity-selection conclusion and failure of a narrower packet-lift mechanism can coexist.

The phrase “actual selector” at LF25/LF196 is supported here ONLY as existence of a legitimate actual occurrence subset. LF198 correctly disclaims a computational extraction procedure or complexity bound. This review supplies no algorithm and no certificate file containing a particular selected subset for each word.

Source LF214 attributes the colouring/summation/Fermat mechanism to an old proof, but the physical formulas needed for this slice are re-derived inside the pinned source and reconstructed above. The old proof's computation, sharpness and prime-power assertions are not premises here. I have not independently audited that attribution, the old proof's SHA provenance, global novelty, historical process claims or exact membership definitions of each named residual caller.

## 9. Explicit NOT_RECONSTRUCTED obligations

1. **Polynomial/algebra acceptance:** A-IND, A-COEFF and A-SECOND as listed in §2. In particular, no full proof of equations(6), (7), the degree_z bound and the final two-box algebra is certified by this applicability return. That is the separately frozen v31-A slice; no verdict is inherited from it.
2. **Full Theorem DB acceptance:** NOT_RECONSTRUCTED as a complete theorem by v31-B alone; requires the actual algebra return plus parent reading/composition.
3. **Algorithm/executable witness:** no selector algorithm, complexity guarantee, finite certificate or executable replay reconstructed or asserted.
4. **Other bands/general targets:** no other R band, unrestricted prime-dihedral ordered Olson theorem, prime-power extension or all-finite-group book theorem reconstructed.
5. **Packet lift:** no proof of packet-only L_RES and no repair/reversal of the false L_MAX assertion.
6. **Scientific/novelty assurance:** author historical arithmetic and no-execution statements are not independently attested by this review; no unadmitted arithmetic output is accepted; no human/formal/cross-vendor/novelty acceptance.

**Disposition:** no correction required in the assigned actual-word applicability slice at the pinned source bytes. Its bridges support the candidate's full declared R,F quantifiers CONDITIONALLY on the explicit polynomial interface. No broader PASS is implied.
