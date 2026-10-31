# f499 WRITTEN review: local-lift incompatibility with the named f263 caller

## Verdict

**SUPPORTED:** The additive erratum correctly proves that **every lift produced by the exact f468 recipe—eight inactive support-two blocks and sixteen empty inactive blocks—fails to satisfy the named f263 \(U_0\)-energy and \(U_3\)-zero-count requirements simultaneously**.

The recipe remains valid as a ternary, support-116, local-\(H=0\) construction with the prescribed two fibres. The incompatibility is not a five-span exclusion, does not invalidate the two-fibre Fourier equivalences, and does not establish or exclude an original Boolean caller.

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR at the reconstructed scope.** The original-caller conclusion is conditional on the explicitly supplied f263 residual, including its \(G3=1\Rightarrow \#\{U_3=0\}=23\) import and its displayed local meaning of \(H\).

## 1. Frozen inputs and review procedure

The reviewed wave is `f499-boolean-local-lift-incompatibility-original-f263-written-review`.

Identity pins, as supplied in the assignment and parent metadata:

- Manifest: `5a578154d357b41cc056ff8f37da9f6d757c064a78acee77169db9ab978f1091`
- Freeze receipt: `56a44c66484809ce91da977fc885cb7bcf533b33a28928c323eaf3c405392236`
- Literal packet: `48e7a4419fc36b4f2e33ca5219b3ea8a576799b2706edd473339079ef2a48c19`

Source coverage:

| Source | Material read | Declared whole-file SHA-256 |
|---|---|---|
| S1 | Complete f468 candidate, LF 1–76 | `642e16f3042fcfed6efd97ec84bd13b6aaa41cd2c0a470756d5a21ec611e56b1` |
| S2 | Complete additive incompatibility erratum, LF 1–35 | `9471cda09e4b8e15d9390b0ce4a7b9ddd354fdc6e82ba64283a8302ee4d13c08` |
| S3 | Explicitly selected f263 review LF 1–103, **not** its remaining LF 104–162 | `117149fa1734b863b21a37197217b4d8f111ac455194d445c25d0bc95d420de1` |
| S4 | Complete adopted actual-caller dichotomy, LF 1–37 | `2aa39512cf0ef6d1194cc8257dfe722cf9a58b62f637baf9056e08355b4423f0` |

The complete manifest, freeze receipt, ten status-only controls, and parent metadata supply were read before the administrative pre-body ACK. The ACK preceded the first mathematical packet read. All 253 packet LF were then read in order, raw, in windows \(1\!-\!20,\ldots,221\!-\!240,241\!-\!253\), including every supplied source ending, before derivation.

The hash observations above are **parent-supplied**, not independently recomputed by this reviewer. No reviewer-native clock observation is claimed. No scientific execution, code, CAS, enumeration, replay, new selected mathematical instance, linked-source follow, author-code inspection, sibling review, or held scientific payload was used. This full body is returned for parent materialization; no repository file was written.

## 2. Exact imports and labels

The four partial transforms are on the **same** physical block:
\[
U_s(c)=\sum_{w\in Q}u(c,w)\chi_s(w),
\qquad Q=\mathbb F_2^2.
\]
The named independent characters are \(\chi_1,\chi_2\), with
\(\chi_3=\chi_1\chi_2\); \(U_0\) is the ordinary block sum. These labels are distinct from the \(R\)-frequencies in \(A\) and from the graph variables \((j,b)\).

S3 LF 75–85 supplies the common inverse and unnormalized Fourier constants. In particular,
\[
\widehat U_s(r)=2k(r,s),\qquad
\sum_c U_s(c)^2=\frac1{16}\sum_r k(r,s)^2.
\]
Thus the named spectra give
\[
E_0=56,\qquad E_1=144,\qquad E_2=136,\qquad E_3=128.
\]
For example, the \(U_0\) fibre has eight zeros and 56 coefficients of magnitude \(4\) in \(k\), giving \(E_0=56\). For the nonzero fibres,
\[
E_s=\frac{4e_s+36(64-e_s)}{16}=144-2e_s,
\]
with \((e_1,e_2,e_3)=(0,4,8)\).

The additional requirement
\[
Z_3:=\#\{c:U_3(c)=0\}=23
\]
is the explicit \(G3=1\) import in S3 LF 99. Its underlying historical source is not separately supplied or re-opened here. The conclusion therefore retains precisely that named-residual dependency.

## 3. The two-fibre construction remains valid locally

### Canonical Fourier equivalences

The written equivalences in S1 LF 19–43 are supported at their stated normalized five-span scope, using S4 as the adopted actual-caller import.

For nonzero \(y\perp1\), the two full blocks give \(G_0(y)=12\). Every corresponding full \(g\)-coefficient is \(\pm12\), and its average over the eight \(z\)-frequencies is \(12\). Hence all eight equal \(12\), forcing the other partial rows to vanish. On each \(B\)-coset, quotient Fourier inversion then gives exactly one support point in each pair \(\{2j,2j+1\}\). This supplies the common graph function \(f(j,b)\).

For odd \(y=1+2v\), the displayed transform is
\[
\widehat g(y,z)
=3(-1)^{z\cdot1}W_{f+q}(v,w(z)).
\]
The map \(w(z)=(z\cdot3,z\cdot5)\) is onto the two-bit frequency space. Consequently the required odd-row magnitudes are equivalent to \(f+q\) being bent. The even and odd rows of \(\widehat a\) are, respectively, signed copies of \(W_r\) and \(W_{r+f}\), giving the stated common-phase condition.

This is a written reconstruction of the equivalences, **not** a reconstruction of the finite census in S1 LF 47–62.

### Physical local blocks

On a support block, the recipe sets
\[
u(w)=a\chi_1(w)\quad(w\ne w_0),\qquad u(w_0)=0.
\]
Character orthogonality gives
\[
U_1=3a,\qquad U_2=-a\chi_3(w_0).
\]
The required equation \(\chi_3(w_0)=-g/a\) has exactly two solutions because \(g/a=\pm1\). Also,
\[
U_0=-a\chi_1(w_0),\qquad U_3=-a\chi_2(w_0),
\]
so both have magnitude one, independently of the hole choice.

A full \(|U_2|=4\) block must be \(u=\pm\chi_2\), giving \(U_0=U_1=U_3=0\).

For a support-two \(|U_2|=2\) block, the recipe chooses points \(p,q\) in opposite \(\chi_3\)-classes and puts \(u=(g/2)\chi_2\) there. Exactly one of \(\chi_1,\chi_2\) changes sign between \(p\) and \(q\). Therefore its remaining magnitudes are exactly
\[
(|U_0|,|U_3|)=(2,0)\quad\text{or}\quad(0,2).
\]

Finally, let \(\delta=(1,1)\) in the fixed \(Q\)-basis. Then
\(\chi_1(\delta)=\chi_2(\delta)=-1\) and \(\chi_3(\delta)=1\). Equal signs \(\alpha=\pm1\) at \(p,p+\delta\) give
\[
U_1=U_2=0,\qquad U_0=2\alpha,\qquad
U_3=2\alpha\chi_3(p).
\]
Thus every filled inactive block has \(|U_0|=|U_3|=2\).

These identities verify S1 LF 66–70 without selecting an additional instance.

## 4. Reconstruction of all block counts

The \(U_1\) divisibility and range in S3 LF 83–87 give \(U_1\in\{0,\pm3\}\). Energy \(144\) therefore gives exactly **16 support-three blocks**.

For the other 48 blocks, \(U_1=0\). Their four-point transform is either all zero, a pair of magnitude-two entries, or one magnitude-four peak, as stated in S3 LF 87.

S3 LF 93–97 establishes 24 \(U_2\)-zero blocks. In its affine-rank-three case, the three independent relative character signs give \(t_2\) magnitudes \(0,2,4\) with multiplicities \(24,32,8\); the supplied congruence criterion identifies the 24 zeros with \(U_2=0\).

Hence \(U_2\) is nonzero on 40 blocks, 16 already being support-three blocks. If \(p\) and \(h\) count its even full and half blocks, then
\[
p+h=24,\qquad16+16p+4h=136.
\]
Thus \(p=2\) and \(h=22\). The remaining \(64-16-2-22=24\) blocks have \(U_1=U_2=0\).

The recipe’s support is consequently
\[
16\cdot3+2\cdot4+22\cdot2+8\cdot2=116.
\]
No block has a \(|U_0|=4\) peak, so its displayed **local** \(H\) is zero.

## 5. Universal incompatibility of the exact eight-halfblock recipe

Let \(k\) count the 22 support-two \(|U_2|=2\) blocks having \(|U_0|=2\). The complete recipe has the following census:

| Block type | Count | \(|U_0|\) | \(|U_3|\) |
|---|---:|---:|---:|
| \(U_1=\pm3\) | 16 | 1 | 1 |
| Full \(U_2\) peak | 2 | 0 | 0 |
| \(U_2\) halfblock using \(U_0\) | \(k\) | 2 | 0 |
| \(U_2\) halfblock using \(U_3\) | \(22-k\) | 0 | 2 |
| Filled inactive halfblock | 8 | 2 | 2 |
| Empty inactive block | 16 | 0 | 0 |

Therefore
\[
E_0=16+4k+8\cdot4=48+4k,
\qquad
Z_3=2+k+16=18+k.
\]

The named energy \(E_0=56\) forces \(k=2\), giving \(Z_3=20\), not 23. Conversely, \(Z_3=23\) forces \(k=5\), giving \(E_0=68\), not 56.

This proves S2 LF 17–29. It applies to **every admissible \((f,r)\)** to which the recipe applies, every support-hole choice, every permitted active pair, every choice of eight inactive blocks, and every local sign choice. The argument depends only on their forced block types and counts, not on a finite representative or the finite graph census.

## 6. Normalization preserves these obstructions, not necessarily balance

For the inherited \(R\)-coordinate operations, write
\[
u'(c,w)=\varepsilon\chi_\ell(c)\,u(Lc+t,w),
\]
where \(L\) is invertible. Each named partial transform obeys
\[
U_s'(c)=\varepsilon\chi_\ell(c)\,U_s(Lc+t).
\]
Consequently \(E_0\), \(Z_3\), support counts, and local peak counts are unchanged.

Balance is different: a nontrivial \(c\)-character modulation changes the ordinary sum of \(u\) into another Fourier coefficient. Its preservation does not follow.

This reasoning keeps the named \(Q\)-fibres fixed. It does not invoke arbitrary \(Q\)-character multiplication, which would permute the fibres. No such operation is needed for the inherited normalization. S2 LF 11 is therefore supported at the operations actually used.

## 7. The correct local census was already in f263

The same named conditions determine the earlier census without any new global construction.

The 23 \(U_3\)-zero blocks leave 41 nonzero blocks. After removing the 16 magnitude-one blocks, let \(p_3,h_3\) count full and half \(U_3\)-blocks:
\[
p_3+h_3=25,\qquad16+16p_3+4h_3=128.
\]
Thus \(p_3=1,h_3=24\).

Now let \(a,b,c\) count magnitude-two pairs in slots \((0,2),(0,3),(2,3)\), let \(d\) count full \(U_0\) peaks, and let \(o\) count empty blocks. Then
\[
a+b+4d=10,\qquad a+c=22,\qquad b+c=24,
\]
\[
a+b+c+d+o+2+1=48.
\]
Solving gives
\[
a=4-2d,\quad b=6-2d,\quad c=18+2d,\quad o=17+d.
\]
At the displayed local \(H=d=0\),
\[
(a,b,c,o)=(4,6,18,17),
\]
with two full \(U_2\) peaks and one full \(U_3\) peak.

In particular, the inactive 24 blocks are **six** \((U_0,U_3)\) halfblocks, **one** full \(U_3\) block, and **17** empty blocks. Their support contribution is \(6\cdot2+4=16\), equal to the eight-halfblock recipe’s contribution but with different energy and zero-count consequences.

These equations and their solution already appear in S3 LF 99–103. S2 LF 33 correctly credits them as prior within the run. They establish a necessary local census, not a globally compatible arrangement.

## 8. Per-claim disposition and limits

| Claim | Disposition |
|---|---|
| Conditional canonical two-fibre Fourier equivalences | **SUPPORTED**, S1 LF 19–43 with the declared S4 import |
| Ternarity, prescribed \(U_1,U_2\), support 116, and local \(H=0\) of the recipe | **SUPPORTED**, S1 LF 66–70 |
| Exact recipe satisfies both named \(E_0=56\) and \(Z_3=23\) | **REFUTED**, as correctly asserted by S2 LF 17–29 |
| Obstruction covers all admissible pairs and all recipe choices | **SUPPORTED** by the universal block calculation |
| Correct local census is already present in f263 | **SUPPORTED**, S3 LF 99–103 |
| Equivalence with an undisplayed historical \(H\) convention | **INCONCLUSIVE**; only the explicit local definition is used |
| Underlying historical derivation of the \(G3\)-to-zero-count rule | **NOT RECONSTRUCTED** beyond the expressly authorized S3 import |
| Finite enumeration counts and rank classification in S1 LF 47–62 | **NOT RECONSTRUCTED**; no code, output, or linked evidence was inspected |
| Exclusion of the whole five-span branch, either six-span branch, or NL242 | **NOT ESTABLISHED** |
| Original balanced caller, compatible \(V\), odd-fibre caps, rank/eight-zero/\(T\) completion | **NOT ESTABLISHED** |

The frozen S1 candidate is not rewritten by this review. S2 is a later additive correction: its stronger incompatibility statement must accompany subsequent use of the recipe. The earlier f478 review was not read or re-adjudicated here; its exact frozen scope is left untouched.

No novelty, priority, independent-family, human, kernel, original-target acceptance, or parent adoption is conferred.

**Overall correctness:** correct at the explicit conditional scope above.  
**Explanation:** The erratum’s energy/zero-count contradiction holds for every lift generated by the exact recipe, while preserving its valid two-fibre local construction. Its scope and prior-credit qualifications correctly prevent promotion to a whole-branch exclusion or a new census result.  
**Confidence:** 0.99.