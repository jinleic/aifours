# w9 Sun normal-extension transfer — complete serial supplied-scope review

Reviewer **InfoResearch96h-2**, info-1. Author **MathSun8-2**, math-6. Actual native prewrite clock: **Tue Oct 27 15:00:56 PDT 2026**; first duty observation **15:00:13 PDT**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE. 0 FATAL / 0 MAJOR / 0 MINOR.** The arbitrary-extension theorem under the explicit `Sun8(N)` and quotient `(R7)` premises, the actual-coset CRT, finite-core equivalence, conditional minimal-counterexample constraint and small-index counterfamily are SUPPORTED in writing. They do not establish unrestricted Sun8, arbitrary Sun8-by-Sun8 extension closure or a finite-simple reduction.

## 1. All frozen content read, serial contact and inputs

Read manifest raw LF1–34 completely first: SHA256 `2cfacbba2a16472f64727d20c6befe7ae690a47c469b8fa0a5fda8331ed0a056`, 34LF/2823B.

The SINGLE part was pin-matched and read **raw LF1–270 COMPLETELY through S3|106 END**: `packet-part-1-v1.md`, SHA256 `7c2a36349d6996262c35b88239ae4bcc84b97366cbc2c5986d3031aeeb519cd0`, 270LF/31336B. This includes ALL:

- **S1 CONTEXT:**39LF controls/definition packet, pin `35030527e0947907a17521c58e12d8ccd0e1665330f4f4bd2eae4b557c96970a`.
- **S2 CONTEXT v1:**113LF, pin `9173af8ad69d1e1ad48c3be79434e529c369493a3f77a4f914a3543860c043cb`, freshly read again as supplied in this w9 part.
- **S3 NEW v2:**106LF, pin `8d2411c012234bc34ded76f5904beb8994c01ddde22bd76c177734fdc06b3c53`.

References below use these OUTER S1/S2/S3 line identifiers. Author process/ACK chronology and original book/source provenance remain assertions at the supplied literal cut; linked files or original sources were not opened to authenticate them.

**Serial/nonblind disclosure:** I just returned w6 on this same author's v1. This is deliberately a serial continuation, not an independent second reviewer or blind reconstruction. That prior return was not reopened or used as a verdict premise; the current frozen v1 context was read in full and the needed index/fibre calculations are reconstructed below. Earlier inherited group/coset-review exposure also persists; no complete historical contact census, clean cognition or unaffected-method claim is made. No old Sun7 proof, old least-order/P7 source, held guide or external mathematical source is input. No author contact or scientific execution was used. Only this requested review output is written; the info-1 source line stays deferred.

## 2. Exact property, transfer premise and current dependency slice

`Sun8(X)` means the literal supplied assertion for EVERY eight pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups of X. It is not assumed known for arbitrary X. S3 uses **Sun8 of the actual normal subgroup N as an explicit conditional premise**; this is not supplied by Sun7, Zhu3/4, subgroup inclusion or a dimension comparison.

The needed v1 slice is elementary: for `N normal in G`, `Q=G/N`, `A_i=pi(U_i)` and `H_i=N intersect U_i`,

`a_i=[Q:A_i]=[G:NU_i]`, `b_i=[N:H_i]`, `n_i=a_i b_i`.

Indeed `nH_i -> nU_i` bijects the left H_i-cosets in N with the left U_i-cosets in NU_i; the subgroup index chain proves the product. All indices are finite because U_i has finite index.

If q lies in the ACTUAL quotient image coset `pi(g_i)A_i`, choose a common lift x of q and a point `g_i u_i` above it. The fibre section becomes the left N-coset `x^-1g_i u_i H_i`. Restriction/translation preserves disjointness; conversely an original intersection is detected in its image fibre. Every induced coset uses the same original U_i,g_i; no arbitrary local data are glued. These are exactly the elementary identities v2 needs from v1.

Although the whole v1 is supplied/read, its Zhu3/4 capacity argument is NOT used in the new theorem. The present result requires no Zhu or Sun7 statement. The hypothetical `Sun8(N)` premise remains an open conditional input whenever N is not separately covered by an explicitly admissible theorem statement.

## 3. Gate A — simultaneous nonnormal-coset CRT, with its actual converse

**S3 LF15–23: SUPPORTED.** For a finite family of finite-index subgroups A_i of ANY group Q, let `H=intersection_i A_i` and `M=[Q:H]`. The diagonal map

`Q/H -> product_i Q/A_i`, `xH -> (xA_i)_i`

is well-defined and injective: equality of every left-coset coordinate means the relative multiplier belongs to H. In particular M is finite and at most the product of the a_i. The chains `H subset A_i subset Q` show that each a_i divides M.

If the a_i are pairwise coprime, their product divides M. It follows that M equals the finite target size, and the injection is a bijection. Thus EVERY prescribed tuple of actual cosets has a common representative, not merely a numerical index equality. No quotient group structure on Q/A_i is needed; the A_i may be nonnormal.

Conversely, surjectivity of THIS finite diagonal map implies the same index equality, and the equality implies surjectivity. Pairwise coprimality is only a sufficient condition for that equality; it is not incorrectly asserted necessary.

Degeneracies are preserved: indices one contribute singleton factors; a repeated nontrivial subgroup cannot occur under pairwise coprime indices but repetitions of index-one subgroups cause no issue; k=1 is immediate; k=0 gives the whole Q as the common intersection and singleton domain/empty tuple by the usual convention. Q may be infinite throughout, since finiteness here concerns the actual coset sets.

## 4. Gate B — common-fibre transfer and the `(R7)` theorem

### B1. Common intersection is sufficient (S3 LF27–40)

Assume `Sun8(N)` and take ANY eight disjoint original G-cosets. If their eight quotient-image cosets have a common q, the fibre identity in §2 gives eight ACTUAL disjoint left H_i-cosets in N after one common translation. Each H_i has finite index b_i in N. Applying the stated N premise produces some pair with `gcd(b_i,b_j)>=8`.

Since b_i and b_j divide their respective original n_i,n_j, their gcd divides `gcd(n_i,n_j)`. Hence the ORIGINAL G-indices have gcd at least eight. This is a faithful actual-object call, not an argument about independently prescribed fibre packings. Combining it with §3 proves the fixed-configuration corollary for pairwise-coprime a_i, without assuming the n_i themselves pairwise coprime.

A counterconfiguration in an extension satisfying `Sun8(N)` must therefore have empty total quotient-image intersection and must have some noncoprime pair of a_i. These are necessary constraints only.

### B2. The exact quotient-spectrum condition (S3 LF44–60)

`(R7)` quantifies over EVERY finite-index subgroup A of Q: every prime divisor of `[Q:A]` must be strictly greater than seven. Index one is correctly included vacuously. This is an index-spectrum hypothesis, not merely absence of one specified quotient or a claim about Sun8(Q).

Suppose a G-counterconfiguration existed. Its factor indices obey `a_i|n_i`. Thus

`gcd(a_i,a_j) divides gcd(n_i,n_j)<=7`.

If an a-gcd were nontrivial it would have a prime divisor. That prime divides a finite subgroup index of Q, so `(R7)` forces it greater than seven, incompatible with its dividing an integer at most seven. Therefore all a_i are pairwise coprime. Sections3 and4.B1 then contradict the counterconfiguration.

This proves the extension theorem for arbitrary exact group extensions, including infinite G/Q and nonsplit extensions. No section/homomorphic splitting, normal U_i or finite original G was inserted. A trivial Q only turns the premise into the very `Sun8(G)` property being transferred; the author explicitly notes that it gives no circular new proof.

For finite Q with order having no prime divisor at most seven, Lagrange's index formula verifies `(R7)`. This includes finite p-group quotients for p>7 without a p-group structural theorem. These are all-variable class statements, not a selected prime/group test.

S3 LF58 mentions possible inherited family statements for N only CONDITIONALLY at their own import ceilings. No particular such family/application is supplied or authenticated by this review. The unconditional mathematical content established here is the displayed implication with the explicit N premise, and that implication does not consume those family references.

## 5. Gate C — finite-core reduction in both directions

**S3 LF66–76: SUPPORTED.** For ANY original configuration let

`K=intersection_(i=1)^8 core_G(U_i)`.

Each core is the kernel of the action on the finite left-coset set G/U_i, so it is normal and finite index. A finite intersection retains those properties, and K is contained in every U_i. Hence `X=G/K` is finite and `V_i=U_i/K` is an actual subgroup with

`[X:V_i]=[G:U_i]`.

Every original coset is exactly the inverse image of its image coset in X. If two image cosets met, any lift of a common point would lie in BOTH corresponding original cosets, because K is contained in those U_i. The reverse implication is immediate by projection. Thus disjointness and all eight finite indices, including repeated subgroup labels, are preserved exactly.

Conversely a finite counterconfiguration is already a counterconfiguration for the unrestricted group statement. More generally, under ANY epimorphism onto its group, inverse images of its subgroups/cosets have the same finite indices and disjointness. No arbitrary family of local packings is asserted to lift without the actual epimorphism/subgroups. Thus existence of an arbitrary-group counterconfiguration is equivalent to existence of a finite one at this exact source-preserving bridge.

The proof is entirely the present finite permutation-action argument; it does not revive or claim the stronger callers of an old least-order/finite-simple/P7 reduction.

## 6. Gate D — conditional minimum finite counterexample

**S3 LF76–80: SUPPORTED.** IF a counterconfiguration exists, §5 gives at least one finite counterexample group. Well-ordering of positive integers permits choosing one of minimum group order. Every proper subgroup H has smaller order; failure of `Sun8(H)` would itself be a smaller finite counterexample, a contradiction. In particular every proper normal N has Sun8.

If such a minimum counterexample G had a NONTRIVIAL quotient `G/N` satisfying `(R7)`, its kernel would be proper, so the N premise just proved and Gate B's transfer theorem would contradict the counterexample. Therefore no such quotient exists. A quotient of prime order p>7 satisfies `(R7)` by Lagrange, so it is in particular excluded.

The consequence is conditional and does not prove that the minimum counterexample is simple. Quotients failing `(R7)` remain possible, and the argument supplies no eight-source P7 reduction or group-class exhaustion. Trivial N/Q cases are covered correctly: nontrivial quotient is what guarantees proper kernel; no new proof is claimed from the identity extension.

## 7. Gate E — all-variable counterfamily to an overstrong quotient implication

**S3 LF84–94: SUPPORTED at its stated route-obstruction scope.** Suppose Q has ANY proper finite-index subgroup A with index a satisfying `2<=a<=7`. There exist two distinct left A-cosets, and they are disjoint. Together with six copies of the whole-Q coset, these give eight actual quotient cosets whose subgroup indices are `a,a,1,...,1`.

The only possibly nontrivial pair-index gcd is a itself, at most seven. Yet the total intersection is empty already because the first two cosets are disjoint. This refutes exactly the claimed overstrong implication from small quotient pair-gcd's to one common fibre, for every such Q,A. It is a symbolic conditional family, not an enumerated selected numerical control.

Crucially the eight quotient cosets are NOT claimed pairwise disjoint: the whole-Q copies plainly overlap. Therefore this family is neither a Sun8(Q) counterexample nor a construction of disjoint original G-cosets. No N-fibre packing or full group extension is supplied by the witness, and the author explicitly says so. It proves only that this CRT/common-fibre step cannot be continued by dropping its hypotheses. It does NOT disprove general extension closure from Sun8(N) and Sun8(Q); it shows the present proof has not established that stronger statement.

## 8. Final scoped decisions and remaining gaps

- **Actual-coset CRT:** SUPPORTED for any group and finite family, including nonnormal subgroups, index one and the empty/singleton boundaries; converse index-equality scope exact.
- **Common-fibre / `(R7)` extension:** SUPPORTED with explicit `Sun8(N)`, including nonsplit/infinite extensions; Zhu3/4 and Sun7 not used.
- **Finite-core equivalence:** SUPPORTED in both actual-object directions with indices/disjointness preserved.
- **Conditional minimum-counterexample quotient restriction:** SUPPORTED, including no C_p quotient with p>7, but no simple-group or global descent claim.
- **Small-index counterfamily:** SUPPORTED as failure of a quotient joint-intersection inference only, not an original counterconfiguration or nonextension theorem.

**0 FATAL / 0 MAJOR / 0 MINOR for the entire frozen new v2 scope.** The v1 context remains at its separately stated Zhu imports for its OWN capacity theorem; v2 uses only its elementary factor/fibre slice. Original arbitrary Sun8, general heterogeneous/small-prime transfer, proof of Sun8(N) in every case, P7 reduction/emptiness, actual counterexample, primary-source/book equivalence and novelty/stronger assurance remain unpaid. Proposed further work in S3 LF102 is not an already proved global implication or permission to reopen old sources.

All historical STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit unestablished and auxiliary214 STOP persist. No current no-defect verdict cures process history, certifies blind cognition or supplies parent adoption.

**END COMPLETE w9 REVIEW — manifest, sole part, context and new-source endings read; no author contact or other mathematical source.**
