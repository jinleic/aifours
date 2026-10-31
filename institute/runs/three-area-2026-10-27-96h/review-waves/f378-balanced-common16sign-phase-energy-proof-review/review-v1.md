## Body for `review-v1.md`

# f378 — Written review of the common 16-sign phase code, energy ceiling, and phase-template exclusions

**Reviewer:** ReviewF378BoolPhase  
**Role:** WRITTEN_ONLY; same-harness review.  
**Disposition:** **SUPPORTED at the exact conditional actual-U/V caller scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**

This review reconstructs the mathematical claims in f365. It does not authenticate the original book/source, adopt author chronology assertions, establish novelty, supply an actual U realizer or capped complement, or close any original target.

### 1. Frozen inputs and read coverage

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f378-balanced-common16sign-phase-energy-proof-review/`

Bindings:

- Manifest SHA-256: `4be3a144d452985ff390d9656969fb9bdd5ffd11715ca6edabd5607e3976598b`
- Freeze-receipt SHA-256: `8acdbb33436b1ee4337edf12536c7d889d512e664996bd25fa1cb71580506326`
- Literal-packet SHA-256: `38b88bfff7182874e980371089450069eb9481e96d6a741d0ed2509fc26c2635`

The matching live hashes, byte counts and LF counts are **parent-supplied observations**, recorded in `parent-live-metadata-supply-v1.json` at **2026-10-30T09:54:48-0700 PDT**. They are not reviewer-executed hashes or reviewer-native start/completion times.

The complete manifest, receipt and all seven listed status/permission controls were read before the administrative pre-body ACK was delivered to Main. The complete ordered packet was then read raw in successive windows of at most 20 lines: packet lines 1–560 in 28 windows, followed by 561–563. This included S1’s final logical line 477 and the final packet line `S4|34`. No displayed elision remained. Mathematical reconstruction began only after that read completed.

The source identifiers below refer to the **current f378 packet**, not f365’s earlier local source numbering.

| ID | Complete frozen source | SHA-256 | Coverage |
|---|---|---|---|
| S1 | `review-waves/f365-balanced-original-u-v-after-coset-exclusion/review-v1.md` | `2355e1c4acfeccba991c2ddd2dd5e6d61aa44625920f1564364a6c12db6b8b9f` | Logical lines 1–477; 476 LF |
| S2 | `dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-residual-10-cross-fibre-parent-v1.md` | `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09` | Lines 1–31 |
| S3 | `dispositions/info-6-nl242-uv-caller-interface-and-unconditional-congruences-parent-v1.md` | `b1834337754499fbfdc5f0c1165dff8a1f44bcc5ff0420c1264f4624082afede` | Lines 1–19 |
| S4 | `dispositions/info-6-fixed-real-u-complement-autocorrelation-equivalence-parent-v1.md` | `cd34fb17911723cc3c96ef36f749553370a9cecefe738585d18a680989da5f11` | Lines 1–34 |

These paths are relative to:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`

No linked historical proof/reviewer body, sibling outcome, author code or held scientific payload was opened.

### 2. Exact imports and caller boundary

**SUPPORTED AS IMPORTED — exact conditional scope.**

The load-bearing imports are:

1. **S2 lines 3 and 13:** the actual balanced Boolean caller, Walsh cap, rank-two/eight-zero/\(m=116\)/\((0,4,8)\) hypotheses, common coordinates, block normalization, flat \(|k_1|=6\) fibre, and exactly sixteen \(U_1=\pm3\) blocks. The residual’s \(H\) is the explicit local count of single-\(|U_0|=4\)-peak blocks, not an inferred identity with an undisplayed historical convention; see S2 line 17.
2. **S3 lines 7–10 and 12–15:** the corrected complementary real-ternary U/V interface, global odd cap, balance/parity conditions, 116 u-points and 140 v-points, and the requirement to retain the full pointwise system. The standalone converse lacking pointwise complementarity is expressly not imported.
3. **S4 lines 7–11:** actual real ternary \(u\), full dual character coverage, real \(z\), the inverse normalization, original Walsh halves \(4k\) and \(4z\), and the distinction between a relaxed real spectrum and the original capped caller.

Thus the argument concerns **actual** real ternary functions \(u,v\) on \(R^*\times Q^*\), where
\[
R=\mathbb F_2^6,\qquad Q=\mathbb F_2^2,
\]
with
\[
u^2+v^2=1,\qquad |\operatorname{supp}u|=116,\qquad
|\operatorname{supp}v|=140.
\]
All original balance, even-half cap/structure, odd-half cap/parity and residual requirements remain imposed. In particular,
\[
\widehat U_s=2k_s,\qquad \widehat Z_s=2z_s,\qquad
z_s(r)\in\{\pm1,\pm3,\pm5,\pm7\}.
\]

Neither necessary support geometry nor arbitrary labelled magnitude data supplies an actual \(u\). The AC equivalence in S4 is not used as a replacement for the proofs below.

### 3. Sixteen triple-support blocks and their common local signing

**SUPPORTED — S1 lines 86–128.**

Let
\[
S=\{c:U_1(c)\ne0\},\qquad a=U_1/3.
\]
The imported actual-object facts give \(|S|=16\), with \(a=\pm1\) on \(S\) and zero elsewhere.

For \(c\in S\), the four terms \(u(c,w)\chi_1(w)\) belong to \(\{0,\pm1\}\) and sum to \(3a(c)\). Their nonzero count must be odd, and a count of one cannot give magnitude three. Consequently exactly three terms are nonzero and all three equal \(a(c)\).

There is a unique hole \(w_0(c)\), and
\[
u(c,w)=a(c)\chi_1(w)\quad(w\ne w_0(c)),\qquad
u(c,w_0(c))=0.
\]
For \(j\ne1\), character orthogonality gives
\[
U_j(c)
=a(c)\sum_{w\ne w_0(c)}\chi_{j+1}(w)
=-a(c)\chi_{j+1}(w_0(c)).
\]

Actual pointwise complementarity then gives one sign \(b(c)\), not four independent signs:
\[
v(c,w)=b(c)\mathbf1_{\{w=w_0(c)\}},\qquad
Z_s(c)=b(c)\chi_s(w_0(c)).
\]
Therefore
\[
\theta(c)=a(c)b(c)
\]
is common to all four projected fibres. This deduction depends on actual local complementarity; formal support placements alone do not suffice.

### 4. Fourier normalization, common code, local converse and cardinality

**SUPPORTED — S1 lines 99–104 and 132–203.**

The transforms are unnormalized 64-point transforms, so Fourier involution multiplies by 64. From \(U_1=3a\) and \(k_1=6\sigma\),
\[
\widehat a=4\sigma,\qquad \widehat\sigma=16a.
\]
Likewise, \(\widehat Z_s=2z_s\) gives
\[
\widehat z_s=32Z_s.
\]

For
\[
C_s=\sigma*z_s,\qquad
(f*g)(t)=\sum_r f(r)g(r+t),
\]
the convolution theorem therefore yields
\[
\widehat C_s=(16a)(32Z_s)=512aZ_s,
\]
and inversion gives
\[
C_s=8\widehat{aZ_s}.
\]
On the sixteen blocks,
\[
aZ_s=\theta\,\chi_s(w_0),
\]
and the product vanishes off \(S\). Hence
\[
C_s(t)=8\sum_{c\in S}
\theta(c)\chi_s(w_0(c))(-1)^{t\cdot c}.
\]

The factors **16, 32, 512 and 8** are consistent.

#### Local converse

Fix an actual \(u\). For a real full-dual array \(z\), define \(Z_s\) by the same inverse normalization. If the displayed code equation holds for one common \(\theta\), Fourier comparison gives, on \(S\),
\[
a(c)Z_s(c)=\theta(c)\chi_s(w_0(c)),
\]
and thus
\[
Z_s(c)=a(c)\theta(c)\chi_s(w_0(c)).
\]
Four-point inversion gives
\[
v(c,w)=a(c)\theta(c)\mathbf1_{\{w=w_0(c)\}}.
\]

Conversely, such local singleton signs give the code equation because \(a\) vanishes off \(S\). This establishes exactly the claimed equivalence **on these sixteen blocks**.

It imposes no sufficient condition on the other 48 blocks and does not establish the global odd cap or original-caller realizability.

#### Ambient code size

For fixed actual \(u\), each of the \(2^{16}\) fields \(\theta\) defines a quadruple. These quadruples are distinct because
\[
\widehat C_0=512\,\theta\,\mathbf1_S
\]
recovers every value of \(\theta\).

Thus the **ambient code** has exactly \(2^{16}\) elements. Globally admissible odd-capped complements can realize only a subset, possibly empty. No globally feasible lift is supplied for each codeword.

#### Divisibility, coordinate bound and norm

Each code coordinate is eight times a sum of sixteen signs. The sum is even, so
\[
C_s(t)\in16\mathbb Z,\qquad |C_s(t)|\le128.
\]
Writing \(q_s=aZ_s\), one has \(\sum_c q_s(c)^2=16\). Parseval gives
\[
\sum_t C_s(t)^2
=8^2\cdot64\cdot16
=65536.
\]

### 5. Cross-fibre and self-convolution constants

**SUPPORTED — S1 lines 205–244.**

For \(s\ne t\), on \(S\),
\[
q_s q_t=\chi_{s+t}(w_0)
=-aU_{s+t+1},
\]
because \(s+t+1\ne1\). Both sides vanish off \(S\).

For unnormalized transforms on a 64-element group,
\[
\widehat f*\widehat g=64\,\widehat{fg}.
\]
Consequently,
\[
C_s*C_t=8^2\cdot64\,\widehat{q_sq_t}
=4096\,\widehat{q_sq_t}.
\]
Also,
\[
\sigma*k_j
=\frac{16\cdot32}{64}\widehat{aU_j}
=8\widehat{aU_j}.
\]
It follows that
\[
C_s*C_t=-512\,\sigma*k_{s+t+1}\qquad(s\ne t).
\]

The displayed index pairings are correct:
\[
\begin{aligned}
C_0*C_1=C_2*C_3&=-512\,\sigma*k_0,\\
C_0*C_2=C_1*C_3&=-512\,\sigma*k_3,\\
C_0*C_3=C_1*C_2&=-512\,\sigma*k_2.
\end{aligned}
\]

For the self-convolution, \(q_s^2=a^2=\mathbf1_S\), while
\[
\sigma*\sigma
=\frac{16^2}{64}\widehat{a^2}
=4\widehat{a^2}.
\]
Therefore
\[
C_s*C_s=4096\widehat{a^2}
=1024(\sigma*\sigma).
\]

The factors **512 and 1024** are correct. These are derived consequences, not independent existence gates.

### 6. Linked four-fibre bound

**SUPPORTED — S1 lines 248–279.**

For every \(c\in S\),
\[
\prod_{s\in Q}q_s(c)
=\theta(c)^4\chi_{\sum_s s}(w_0(c))=1.
\]
If
\[
\sum_s t_s=0,\qquad \prod_s\epsilon_s=-1,
\]
then
\[
\eta_s(c)=\epsilon_s q_s(c)(-1)^{t_s\cdot c}
\]
satisfies \(\prod_s\eta_s(c)=-1\). Four signs of product \(-1\) sum to \(2\) or \(-2\). Therefore
\[
\left|\sum_s\epsilon_s C_s(t_s)\right|
\le8\cdot16\cdot2=256.
\]

The source-provided formal tuple in S1 lines 275–279 correctly distinguishes this inequality from four coordinate bounds alone: its stated signed sum is 512. The source explicitly does **not** present that tuple as an actual or capped spectrum. Auditing that supplied illustration does not establish caller feasibility.

### 7. Energy arithmetic, exclusions of 196 and 192, and total 560

**SUPPORTED — S1 lines 283–344.**

Define
\[
E_s=\sum_c Z_s(c)^2.
\]
From \(\widehat Z_s=2z_s\),
\[
\sum_r z_s(r)^2=16E_s.
\]
The global pointwise cap gives
\[
16E_s\le64\cdot49,\qquad E_s\le196.
\]

On \(S\), \(Z_s^2=1\), giving a total contribution of 16. Off \(S\), \(U_1=0\) forces the local support of \(u\) to have even size. Its actual complementary v-support also has even size, so every \(Z_s(c)\) there is even. Thus
\[
E_s\in4\mathbb Z.
\]

#### Exclusion of \(E_s=196\)

Equality in the cap bound forces \(z_s=7\rho\) with \(\rho=\pm1\). Fourier inversion gives
\[
32Z_s=7\widehat\rho.
\]
Both \(Z_s\) and \(\widehat\rho\) are integral. Since 7 is coprime to 32, every \(Z_s(c)\) would be divisible by 7, contradicting \(Z_s=\pm1\) on \(S\).

#### Exclusion of \(E_s=192\)

The deficit from \(64\cdot49\) is
\[
64\cdot49-16\cdot192=64.
\]
Counting the allowed magnitudes gives
\[
48n_1+40n_3+24n_5=64,
\]
or
\[
6n_1+5n_3+3n_5=8.
\]
Its unique nonnegative solution is
\[
n_1=0,\qquad n_3=n_5=1.
\]
Indeed, \(n_1=1\) leaves an impossible remainder 2; with \(n_1=0\), the only possible \(n_3\) values are 0 and 1, and only \(n_3=1\) leaves a multiple of 3.

For the distinct positions of magnitudes 3 and 5,
\[
z_s=7\rho-4\rho(i)\delta_i-2\rho(j)\delta_j.
\]
At every \(c\in S\),
\[
32Z_s(c)
=7\widehat\rho(c)-4\rho(i)\chi_i(c)-2\rho(j)\chi_j(c).
\]
Modulo 7, the left side lies in \(\{3,4\}\), while the correction terms on the right lie in \(\{1,2,5,6\}\). This is a contradiction.

Since \(E_s\) is a multiple of 4, excluding 196 and 192 proves
\[
\boxed{E_s\le188.}
\]

This is an **energy ceiling**, not a smaller pointwise cap. Neither attainability nor optimality of 188 is proved.

Finally, actual complementarity gives \(|\operatorname{supp}v|=256-116=140\). Four-point Parseval in each block gives
\[
\boxed{\sum_sE_s=4\cdot140=560.}
\]

### 8. Weighted magnitude and phase-distance inequalities

**SUPPORTED — S1 lines 349–380.**

For a translated/flipped template, let \(h_s\) count phase disagreements, \(A_s=\sum_r|z_s(r)|\), and \(D_s\) be the magnitude sum over disagreements.

The convolution convention is compatible with the disagreement definition because changing variables gives
\[
C_s(t)=\sum_r z_s(r)\sigma(r+t).
\]
Consequently,
\[
\epsilon C_s(t)=A_s-2D_s,\qquad D_s\le7h_s.
\]
Every sign is defined because all original z-coefficients are odd and nonzero.

For every allowed magnitude \(d\),
\[
d^2-8d+7=(d-1)(d-7)\le0.
\]
Summing over 64 coefficients gives
\[
16E_s\le8A_s-448,
\]
hence
\[
A_s\ge2E_s+56.
\]
Combining this with
\[
A_s=\epsilon C_s(t)+2D_s\le128+14h_s
\]
proves
\[
\boxed{E_s\le36+7h_s(t,\epsilon).}
\]

### 9. Independent-template distances 16, 38 and 60

**SUPPORTED — S1 lines 382–421.**

For any \(m\)-element set \(J\) of fibres, with independently chosen translations and flips,
\[
\sum_{s\in J}E_s
\ge560-188(4-m)=188m-192.
\]
Summing the preceding phase inequality gives
\[
7\sum_{s\in J}h_s\ge152m-192.
\]

The required roundings are correct:

| Fibres | Numerator | Minimum integer total distance |
|---|---:|---:|
| Any two | \(112\) | \(\lceil112/7\rceil=16\) |
| Any three | \(264\) | \(\lceil264/7\rceil=38\) |
| All four | \(416\) | \(\lceil416/7\rceil=60\) |

Thus the respective total-Hamming-radius 15, 37 and 59 neighborhoods are excluded, uniformly over actual callers and independent template choices.

Also, \(\sum_sE_s=560\) ensures that at least one fixed fibre has \(E_s\ge140\). For that fibre, the inequality holds for every template, so
\[
h_s(t,\epsilon)\ge
\left\lceil\frac{140-36}{7}\right\rceil=15
\]
for every translation and flip. The quantifier order in this ancillary statement is valid.

### 10. Linked-template distance 78

**SUPPORTED — S1 lines 423–451.**

Summing the magnitude bounds gives
\[
\sum_sA_s\ge2\cdot560+4\cdot56=1344.
\]
For linked templates satisfying
\[
\sum_st_s=0,\qquad \prod_s\epsilon_s=-1,
\]
the bound from Section 6 gives
\[
\sum_sD_s
=\frac{\sum_sA_s-\sum_s\epsilon_sC_s(t_s)}2
\ge\frac{1344-256}{2}=544.
\]
Since \(\sum_sD_s\le7\sum_sh_s\),
\[
\boxed{\sum_sh_s\ge\lceil544/7\rceil=78.}
\]
The entire radius-77 neighborhood of every such linked template is therefore excluded. No endpoint realization or optimality follows.

### 11. Remaining claims, limitations and unpaid gates

**SUPPORTED — scope qualifications in S1 lines 455–477.**

The restrictions are explicitly phase-coupled necessary consequences of the actual caller. Their proofs do not substitute a coset obstruction, occupancy ledger, N1/N2 claim or AC restatement for the local argument.

The following remain **INCONCLUSIVE / UNPROVED**:

- Existence of an actual U realizer in the assigned residual.
- Existence of a globally odd-capped V complement satisfying the other 48 blocks and all original equations.
- Nonemptiness of the globally admissible subset of the \(2^{16}\)-element ambient code.
- Attainment or optimality of the energy or distance bounds.
- Exclusion of the entire \((G_3,H)=(1,0)\) residual or \((0,4,8)\) case.
- Other fibre patterns, \(m=114\), other class-count pairs, rank two generally, or the complete balanced nine-variable NL242 target.
- Any balanced NL242 witness or global no-go.
- Novelty, priority, original-book/source authenticity, independent-family, human or kernel acceptance.

**INCONCLUSIVE — author historical assertions.** S1 lines 26–49 contain author chronology, reading and execution-status assertions. This review does not independently authenticate those assertions. Likewise, the historical literature-source statement at S1 line 475 refers to an earlier source not included as a separate current input. It is not independently verified here and is not used in any reconstructed theorem.

No scientific claim above requires those historical assertions. No REFUTED mathematical claim was found at the frozen conditional scope.

### 12. Verdict

**overall_correctness:** correct

**explanation:** The common-code theorem and local converse, convolution constants, linked bound, energy ceiling and all stated phase-distance exclusions reconstruct correctly under the full actual real-U/V caller and global odd cap. This supports the conditional written results only; realizability, global feasibility, whole-target exclusion, novelty and witness acceptance remain unpaid.

**confidence:** 0.98

---

## Body for `reviewer-process-v1.md`

# f378 reviewer process and materialization record

**Reviewer:** ReviewF378BoolPhase  
**Duty:** Exact frozen WRITTEN_ONLY review of f365 under the f378 manifest.

### Input and control sequence

Before reading the mathematical packet, the reviewer read:

1. The complete f378 manifest.
2. The complete freeze receipt.
3. Every listed status/permission control:
   - `contract-addendum-2-frontier-first-owner-direction-v1.json`
   - `parent-L1-selected-diagnostic-release-quarantine-v1.json`
   - `parent-written-duty-execution-and-reporting-deviations-20261030-v1.json`
   - `prospective-author-method-scope-restoration-20261030-v1.json`
   - `parent-ame-held-compression-claim-consumer-quarantine-v1.json`
   - `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`
   - `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`
4. `parent-live-metadata-supply-v1.json`.

Generic memory/skill process guidance was also read; it was not used as a mathematical premise.

An administrative pre-body ACK was then sent through `agent://Main`, and the tool reported delivery. That ACK preceded mathematical packet reading and derivation.

The complete ordered packet was read raw in 28 successive 20-line windows covering 1–560, followed by 561–563. All source endings were read, including S1 logical line 477 and S4 line 34. No display elision remained. Derivation began afterward.

The reviewer subsequently read the own-wave parent dispatch receipt and re-read the manifest’s closing requirements. No additional scientific source was opened.

### Methods and exclusions

- No scientific executable, interpreter, CAS, solver, enumeration, finite replay or source-code check was run.
- No mathematical phase, function, parameter or other instance was independently selected for a sanity probe.
- The formal illustration already present in S1 was audited only as a source-provided claim.
- No author code, sibling outcome or linked historical reviewer/proof body was opened.
- All genuine held outputs and their proof, method, selection and confidence consumers remained NONINPUT.
- Earlier general-author examples were treated as permitted author research, not retrospectively classified as violations.
- No external-model CLI, paid/heavy/remote job, installation, deletion, credential/provider change, commit, push, publication or infrastructure mutation occurred.
- No build, lint, formatter or test was run.
- No reviewer-native hash/date execution occurred.

### Clock attribution and checkpoint

The parent supplied **2026-10-30T09:54:48-0700 PDT** with matching live manifest, receipt, packet, control and source metadata. This is a parent observation, not the reviewer’s native start, derivation or completion time.

A substantive checkpoint was sent to Main after the complete packet read and reconstruction. It reported the checked local/code/convolution/energy/distance claims, the absence of a mathematical defect at the conditional scope, the remaining caller-feasibility limits, and the lack of scientific execution or selected probes. The tool reported delivery.

No child-native execution/start/completion timestamp or independently measured cadence is invented. No clean-cognition or historical-provenance certificate is asserted.

### File-writing and fallback

The available write tool exposes session scratch/device writes and agent messaging, not writes to the assigned wave filesystem. No wave-file write, alternate-filesystem workaround or shell write was attempted.

Accordingly, the full bodies for:

- `review-v1.md`
- `reviewer-process-v1.md`

are returned directly for parent materialization in the assigned wave. No persisted reviewer file or reviewer-file hash is claimed.

### Scientific settlement

The complete conditional mathematical review is returned with **0 FATAL / 0 MAJOR / 0 MINOR** findings. No scientific execution occurred. Actual-U existence, globally admissible complement feasibility, endpoint attainment, optimality, whole-target acceptance and novelty remain unproved.