# f277 — plateaued-support XOR: review-v1

## Verdict

**0 FATAL / 1 MAJOR / 2 MINOR. Overall correctness: incorrect. Confidence: 0.99.**

The self-contained weight-16 support-XOR theorem and its conditional application establishing redundancy of (N1) are supported. However, the named imports also imply (N2) at the stated residual, contradicting the manuscript’s central claim that (N2) remains genuinely additional and its proposed surviving non-implication sentence. The generalization needs a local scope/amplitude correction; the opening base SHA is also malformed.

These are reviewer findings, not parent adoption decisions. No witness, exclusion, interface-completeness certification, or change to the residual’s status is supplied.

**Materialization:** The write tool refused the repository path. This is the complete review text for parent materialization as `review-v1.md`; the refusal receipt is recorded in §8.

## 1. Frozen bindings and scope

The manifest matched its supplied SHA-256, byte count and LF count before its body was opened. Every scientific input below likewise matched all three manifest fields before any scientific input body was opened.

### Paths

- **W**: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f277-nl242-plateaued-support-xor/`.
- **M**: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-owner-3/successor-20261029-info6-plateaued-support-xor-v1.md`.
- **C**: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-owner-3/checkpoint-20261029T2009-v1.json`.
- **I1**: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/successor-20261029-f255-boolean-local-normalization-correction-v1.md`.
- **I2**: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-obstruction-parent-v1.md`.
- **I3**: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-residual-10-cross-fibre-parent-v1.md`.

| Object | Observed SHA-256, equal to expected | Bytes | LF |
|---|---|---:|---:|
| W/manifest-v1.json | dee6551bbb6f1691852e6467f2d345a24bd7669bd60f6556012033edf5cfdacf | 4645 | 58 |
| M | 4d9dec9d937df3431be4f86858e1af46299d63f9f852aa44474dab5085dc1bf8 | 10605 | 82 |
| C | 6b1825ba97f285d2fa92f0002629b6cab9175ef756fddc19d67a0033e90b9074 | 2489 | 18 |
| I1 | e0c3f4807732d6cd70d47485f1692366c0f77abfd1c5169e7a5782114bfddcf4 | 12388 | 151 |
| I2 | 18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912 | 4246 | 24 |
| I3 | e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09 | 8344 | 31 |

I1–I3 are conditional imports at their explicitly displayed scopes. In particular, I3’s H means the explicit local U₀-peak count, not an independently certified identification with an undisplayed historical class table. Neither the excluded base/erratum nor any sibling review was opened. References within allowed inputs to other bodies did not authorize opening those bodies.

## 2. Findings

### M1 — Remove the claim that (N2) is an additional residual condition

- **Severity:** MAJOR; **priority:** P1; **confidence:** 1.00.
- **File:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-owner-3/successor-20261029-info6-plateaued-support-xor-v1.md`.
- **Location:** LF58–60; repeated at M LF3 and C LF8,16.
- **Exact quotes:** M LF58: “**the only new u-side condition is (N2)**”; M LF60: “That sentence **survives for (N2)** but **fails for (N1)**”.

At this very frozen residual, the displayed imports already force (N2): I1 gives a common ternary u with Walsh(u)=2k, balance, and even k on every nonzero fibre, so the P*-projection of the XOR of supp(u) is zero; I1 LF98–102 and I3’s explicit H=0 give even counts 4,6,18 of the three two-entry block types. Each two-entry type has a fixed support difference, so its total contribution to that projection cancels; full and empty blocks contribute zero, while every three-entry block contributes exactly its missing point z₀(c). Consequently the projection is precisely the claimed (N2) sum, and (N2) is already implied. The fact that the new plateaued theorem by itself does not constrain z₀ does not establish non-implication from the entire adopted system. Correct C2 and C3, and their summary/checkpoint repetitions, rather than retaining (N2) as a genuinely new condition. A complete all-variable derivation is in §3.4.

### m1 — State the weight restriction and correct amplitude in (C4)

- **Severity:** MINOR, local generalization repair; **priority:** P2; **confidence:** 1.00.
- **File:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-owner-3/successor-20261029-info6-plateaued-support-xor-v1.md`.
- **Location:** LF62.
- **Exact quotes:** “any perfect `{0,±1}` array `μ`”; “For `2^{n−t} ≡ 2 (mod 4)` or singleton supports the amplitude `2^{(n+t)/2}` is odd and the conclusion can fail”.

The first clause must explicitly restrict the perfect array’s weight: an unrestricted perfect array includes μ=δₐ with a≠0, whose support XOR is a, as the manuscript itself notes at LF50. The relevant even amplitude is the normalized dual’s flat amplitude √w=2^{(n−t)/2}, not the Boolean Walsh amplitude 2^{(n+t)/2}. For example, on F₂, σ(x)=(−1)ˣ has singleton support and Boolean Walsh amplitude 2, which is even, while its dual has amplitude 1. A support size congruent to 2 modulo 4 is impossible here: augmentation of μ∗μ=wδ₀ forces w to be an integer square. The intended divisible-by-4-support theorem is valid, but the literal general formulation and the purported exceptional-amplitude explanation need correction; the weight-16 theorem is unaffected.

### m2 — Repair the truncated base SHA in the opening provenance pin

- **Severity:** MINOR; **priority:** P3; **confidence:** 1.00.
- **File:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-owner-3/successor-20261029-info6-plateaued-support-xor-v1.md`.
- **Location:** LF3.
- **Exact quote:** “base `a1b7036f4b37738e3a5bb58527b46129eeaf3d5c733872a65b443cdc156a`”.

This purported SHA-256 has only 60 hexadecimal characters and therefore cannot identify a SHA-256-bound frozen base. M LF80 and C LF13 instead agree on the 64-character string `a1b7036f4b37738e3a5bb58527b46129eeaf3d5c733872a278a65b443cdc156a`. Make the opening pin internally consistent with that full-length identifier. The excluded base was not opened, so this finding establishes the malformed/internal-inconsistent pin, not a fresh verification of the base’s actual bytes.

## 3. Independent mathematical reconstruction

### 3.1 Fourier normalization and perfectness

Use the unnormalized transform on \(G=\mathbb F_2^6\), so double transformation multiplies by 64. For \(W_\sigma(c)\in\{0,\pm16\}\), Parseval gives
\[
|D|\cdot16^2=64^2,
\]
and hence \(|D|=16\). With \(\mu=W_\sigma/16\), double transformation gives \(\widehat\mu=4\sigma\). Thus the transform of \(\mu*\mu\) is identically 16 and inversion gives
\[
\mu*\mu=16\delta_0.
\]
This proves Proposition 0 with the stated normalization; no imported theorem is needed.

### 3.2 The integral u-basis engine

Set \(u_i=g_i-1\). The relations \(g_i^2=1\) give \(u_i^2=-2u_i\). The inverse substitution \(g_i=1+u_i\) establishes the displayed ring isomorphism. Expanding products of \(1+u_i\) is a triangular, diagonal-one change from the group basis to the square-free monomials \(u_S\), so these monomials are a genuine integral basis.

For subsets \(S,T\), every repeated index contributes \(-2u_i\) and no index disappears; therefore
\[
u_Su_T=(-2)^{|S\cap T|}u_{S\cup T}.
\]
For \(x=\sum_Sa_Su_S\) with \(x^2=16\), the constant coefficient gives \(a_\varnothing^2=16\) and thus \(a_\varnothing=\pm4\). This argument works directly for every perfect μ in the theorem, even before introducing any corresponding σ.

The only ordered pairs with \(S\cup T=\{i\}\) are \((\varnothing,\{i\})\), \((\{i\},\varnothing)\), and \((\{i\},\{i\})\). The \(u_i\) coefficient is consequently
\[
2a_\varnothing a_i-2a_i^2
=2a_i(a_\varnothing-a_i),
\]
which must vanish in \(\mathbb Z\). Thus \(a_i\) is either 0 or \(a_\varnothing\), in particular even. Finally the expansion of \(g^c\) gives
\[
a_i=\sum_c\mu(c)c_i.
\]
On D every μ(c) is odd, so \(a_i\) modulo 2 is the number of supported c with \(c_i=1\). Every coordinate of the support XOR vanishes. This supports the universal weight-16 theorem exactly as quantified.

The specific reduction discussed at M LF48 is also correct: in characteristic two the square reduces to the constant augmentation parity and supplies no support-XOR constraint for an even support. The further sentence “In particular no mod-2 argument can prove the theorem, and none was needed” is not a proved impossibility theorem about all conceivable arguments. Only the insufficiency of this particular reduced identity is supported; the broader methodological assertion is **INCONCLUSIVE** and is not used in any mathematical disposition below.

### 3.3 The conditional plateaued application and (N1)

I1 LF78,88 gives \(16U_1=3W_{\sigma_1}\), \(U_1\in\{0,\pm3\}\), and exactly 16 nonzero blocks. Therefore \(W_{\sigma_1}=(16/3)U_1\) takes values \(0,\pm16\), with the same support D. Apply the independently reconstructed theorem after choosing a basis of R and its dual. It follows that \(\bigoplus D=0\).

I2 supplies the frozen (0,4,8) block scope and the count 16; I3 fixes the residual and explicit local meaning of H. Thus (N1) redundancy is supported conditionally on precisely these named imports, without opening the excluded interface or re-adopting the undisplayed proofs behind the imports.

### 3.4 The same imports also imply (N2)

This derivation uses only displayed premises and applies to every common ternary array satisfying them; it is not a selected example or an existence argument.

Write the support as
\[
\mathcal S=\{(c,z):u(c,z)\ne0\}\subset R^*\oplus P^*,
\]
with \(P^*\) of dimension two. Let Z be the XOR of its z-coordinates. By I1 LF31–37 and LF53–66, balance gives \(\widehat u(0,0)=0\), and for every nonzero \(s\in P\),
\[
\widehat u(0,s)=2k(0,s),
\qquad k(0,s)\in\{\pm2,\pm6\}.
\]
Subtracting these two character sums gives
\[
\sum_{\substack{c,z\\s\cdot z=1}}u(c,z)
=-k(0,s)\in2\mathbb Z.
\]
Modulo two, each nonzero \(u(c,z)\) is 1. Therefore \(s\cdot Z=0\) for both independent s and hence \(Z=0\). Equivalently, this is the elementary first-moment consequence of the already displayed Walsh divisibility by four.

Now decompose Z by the block types already present in the imports:

1. There are 16 three-entry blocks, indexed by D, each with unique missing point \(z_0(c)\). The XOR of all four points of \(P^*\) is zero, so the support XOR of such a block is \(z_0(c)\).
2. Empty blocks and full four-entry blocks contribute zero.
3. A two-entry block at z and \(z+d\), \(d\ne0\), with values \(\alpha,\beta\in\{\pm1\}\), has transform at s equal to
   \[
   (-1)^{s\cdot z}\bigl[\alpha+\beta(-1)^{s\cdot d}\bigr].
   \]
   Its two nonzero transform positions p,q satisfy \((p+q)\cdot d=0\). In dimension two this determines the unique nonzero d from the unordered type \(\{p,q\}\). Thus every block of the same two-entry type contributes the same d, independent of its position and signs.

I1 LF98–102 gives the counts
\[
a=4-2d_0,\qquad b=6-2d_0,\qquad c=18+2d_0
\]
for the transform pairs (0,2), (0,3), (2,3), where \(d_0\) is the U₀-peak count. I3 LF3,17 expressly identifies the frozen H with this count and fixes H=0. Hence the counts are 4,6,18, all even, and all two-entry contributions cancel. Consequently
\[
Z=\bigoplus_{c\in D}z_0(c)=0.
\]

This is exactly the (N2) formula printed at M LF58. The argument does not use the new support-XOR theorem, any purported independence of gap placements, an excluded review, or an undisplayed historical class-table convention. It shows why failure of the new theorem alone to address gaps cannot justify C2/C3’s conclusion about the full imported system.

For completeness, the even-count equations can also be checked directly from the displayed local energies. Removing the 16 three-entry blocks leaves U₀,U₂,U₃ energies 40,120,112. The two U₂ peaks and one U₃ peak contribute 32 and 16, respectively. Thus
\[
a+b+4d_0=10,\qquad a+c=22,\qquad b+c=24,
\]
giving the displayed counts. No additional count-table assumption is being smuggled into the cancellation.

### 3.5 Sharpness and the weight-four illustration

For \(\mu=\pm\delta_a\), convolution is \(\delta_0\), the dual flat amplitude is 1, and the support XOR is a. Taking \(a\ne0\) is a valid hand counterexample to removing the even-dual-amplitude restriction. The corresponding linear Boolean function has Boolean Walsh amplitude \(2^n\), not amplitude 1.

For the stated four-point signs (+,+,+,−), the two unordered pairs for each nonzero difference have opposite sign products, so convolution vanishes there and equals 4 at zero. Also
\[
x=1+g_1+g_2-g_1g_2=2-u_1u_2,
\]
and \((u_1u_2)^2=4u_1u_2\), whence
\[
x^2=4-4u_1u_2+4u_1u_2=4.
\]
The augmentation is 2, the degree-one coefficients are zero, and the support XOR is zero. The illustration is correct.

### 3.6 Correct general divisible-by-four form

For a perfect integer signed array of weight w, augmentation gives \(a_\varnothing^2=w\), so \(m=\sqrt w\) is an integer. The identical degree-one calculation gives \(a_i\in\{0,a_\varnothing\}\). If w is divisible by four, m is even, and the parity bridge proves
\[
\bigoplus\operatorname{supp}\mu=0
\]
in every dimension.

For a Boolean plateaued function with Walsh amplitude \(A=2^{(n+t)/2}\) and support size \(w=2^{n-t}\), its normalized dual has transform
\[
(2^n/A)\sigma=\sqrt w\,\sigma
\]
and is perfect of weight w. The preceding argument proves the requested general divisible-by-four Walsh-support statement.

The parity parameter is \(\sqrt w=2^{(n-t)/2}\), not A. Singleton support has \(\sqrt w=1\) and \(A=2^n\), even for every positive n. A support size congruent to 2 modulo four cannot be the weight of such a perfect array because it cannot be an integer square. These observations provide the local corrections required by m1; they do not undermine the restricted theorem.

## 4. Per-claim dispositions

| Claim and manuscript location | Disposition | Basis / boundary |
|---|---|---|
| Parseval support size and inversion, LF7 | **SUPPORTED** | Direct unnormalized Fourier calculation, §3.1. |
| Proposition 0, LF9–13 | **SUPPORTED** | μ-hat=4σ and convolution inversion. |
| Integral ring isomorphism, basis, product rule, LF23–35 | **SUPPORTED** | Inverse substitutions and integral triangular basis change. |
| Degree-one constraint, a∅=±4, parity bridge, LF37–46 | **SUPPORTED** | Direct coefficient comparison, including the constant coefficient. |
| Universal weight-16 support-XOR theorem, LF17–21 | **SUPPORTED** | Self-contained, no named import required. |
| Particular mod-two reduction, LF48 | **SUPPORTED** | It is vacuous for even support. |
| Claim that no mod-two argument of any kind can prove the theorem, LF48 | **INCONCLUSIVE** | Only the insufficiency of the displayed reduced identity was established; no broader methodological impossibility is certified. |
| Weight-one sharpness and weight-four worked illustration, LF50–52 | **SUPPORTED** | Hand derivations in §3.5; amplitude understood as the dual flat amplitude. |
| Plateaued σ₁ and automatic (N1), C1 LF56 | **SUPPORTED, conditional imports I1/I2/I3** | Exact normalized transform and frozen scope in §3.3. |
| (N1) redundancy, first part of C2 LF58 | **SUPPORTED, conditional imports I1/I2/I3** | It follows from the imported plateaued structure. |
| (N2) remains genuinely additional, C2 LF58 and opening LF3 | **REFUTED, conditional imports I1/I3 at the I2 scope** | The same displayed system implies (N2), §3.4, finding M1. |
| Correction of non-implication for (N1), C3 LF60 | **SUPPORTED as a statement about the quoted claim** | Does not certify the excluded original Remark’s full text. |
| Non-implication survives for (N2), C3 LF60 | **REFUTED** | The opposite implication is proved in §3.4. |
| General divisible-by-four support theorem intended in C4 LF62 | **SUPPORTED with explicit weight restriction** | Self-contained general derivation, §3.6. |
| Unrestricted perfect-array wording and exceptional Walsh-amplitude explanation, C4 LF62 | **REFUTED as written** | Singleton counterexample and normalization distinction, finding m1. |
| Exact full (U)/(V) interface identities and their completeness | **INCONCLUSIVE** | Their base and erratum are excluded inputs; only the claims actually printed here were audited. |
| No witness/exclusion supplied; no broader conclusion follows, C5 LF64 | **SUPPORTED as this review’s result boundary** | Not a fresh census of all other research or a certification of their global status. |
| Import identities and displayed pins, LF68–74 | **SUPPORTED as conditional imports / verified bindings** | No re-adoption of undisplayed dependency proofs. |
| C LF8,16: theorem and (N1) repetition | **SUPPORTED** | Same mathematical scope as above. |
| C LF8,16: (N2) is the only new condition | **REFUTED** | Same issue as M1. |
| Opening base identifier, M LF3 | **REFUTED as a SHA-256 pin** | 60 characters; finding m2. |
| Author history, elapsed activity, unchanged excluded bodies, provenance/novelty assertions | **INCONCLUSIVE beyond the directly observed review actions and input bindings** | Excluded objects and historical execution were not inspected. |

## 5. Complete display coverage receipt

All listed initial displays were raw, without line elision, at most 15 LF per window. Every actual ending was displayed. Mandatory order was respected: complete manifest, complete manuscript, complete checkpoint, then complete I1, I2, I3. Mathematical consideration and mathematical note-taking began only after all these initial displays had completed, with the reconstruction-phase clock observation at 20:21:49−0700.

| Object | Initial raw display windows, in order | Ending included |
|---|---|---|
| W/manifest-v1.json | 1–15; 16–30; 31–45; 46–58 | LF58 |
| M | 1–15; 16–30; 31–45; 46–60; 61–75; 76–82 | LF82 |
| C | 1–15; 16–18 | LF18 |
| I1 | 1–15; 16–30; 31–45; 46–60; 61–75; 76–90; 91–105; 106–120; 121–135; 136–150; 151–151 | LF151 |
| I2 | 1–15; 16–24 | LF24 |
| I3 | 1–15; 16–30; 31–31 | LF31 |

After the bright line, four additional raw windows were displayed for exact finding anchors: **M 56–62; M 3–3; M 78–82; I1 96–104**. They were requested together as independent re-reads, not as a replacement for any initial coverage. These are all re-display windows.

The initial receipt covers **28 windows and 364 distinct LF including the manifest**, or **306 LF of scientific input bodies**. With the four re-displays there were **32 raw windows**. There were no status-only context inputs, no sibling-review displays, no author-script displays, and no unlisted scientific-body displays.

## 6. Controls, clocks, and deviations

### Observed native clocks

All entries below are literal native `/bin/date` observations, not reconstructed creation times or estimates. All are on 2026-10-29, offset −0700.

| Phase / observation | Native clock |
|---|---|
| First manifest-metadata phase observation | 20:19:24 |
| Input metadata / ordered-display phase, before metadata | 20:19:55 |
| Input metadata batch completed | 20:19:56 |
| All required displays already complete; reconstruction phase begins | 20:21:49 |
| Literal provenance-pin length check, before / after | 20:28:37 / 20:28:37 |
| Review drafting phase begins | 20:28:47 |
| Output materialization phase begins | 20:31:08 |

The metadata commands used `shasum` and `wc`, with a 120-second tool deadline, and completed without a tool error. The separate literal-string length pipeline returned **60** and **64** and explicitly reached **exit_status=0**. No scientific script, solver, build, test, finite enumeration, or author code was executed. No reviewer control script or execution-result artifact exists. The singleton counterexample and weight-four check above are written hand reconstructions, not claims of executed controls. There was no scientific timeout, unsuccessful scientific control, or negative test misreported as a pass.

### Additive process disclosure

Before the manifest body, higher-priority runtime instructions required reading the root memory summary and the procedural skills `aifours-written-math-acceptance-protocol` and `independent-snapshot-review`. The memory read preceded the first observed native clock and manifest verification; skill reads also preceded the manifest-body display. This is disclosed as a bounded departure from a literal manifest-first / listed-files-only reading of the review protocol. These were procedural policy reads, not additional scientific inputs; no mathematical consideration, mathematical notes, or inter-input comparison occurred before all permitted scientific displays were complete. The exact time of the preliminary policy reads was not observed and is not backdated.

The optional external-model procedure was not invoked. No sibling review, excluded base/erratum, held/withdrawn/ZERO/quarantined source, author script, unlisted prior-wave output body, or network resource was opened. No frozen input, manifest, disposition, ledger, or README was modified. No other process deviation is identified.

## 7. Assurance boundary

This is a **same-harness written mathematical review with metadata-only machine checks**. It is **not human review, independent-model-family verification, formal proof, kernel verification, a novelty audit, an original Boolean realization, or an exclusion certificate**. Conditional imports remain conditional at their displayed scopes. The reviewer makes no parent adoption decision. The new theorem is supported, but the submitted package needs the M1 correction and the two local repairs before it can accurately state its advertised consequences.

## 8. Additive materialization receipt

The complete review was submitted to the write tool at the assigned path:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f277-nl242-plateaued-support-xor/review-v1.md`

The tool refused that filesystem path, stating that it is limited to `xd://` device transport and `local://` session scratch and that other filesystem paths are refused. No repository review file was created by that attempt. A subsequent native `/bin/date` observation was **2026-10-29T20:33:59-0700**; this is an after-refusal observation, not an asserted exact refusal time.

The complete review is therefore returned in-channel under the manifest’s fallback rule. No persisted-review SHA-256 or successful materialization is claimed.
