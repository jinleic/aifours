DISPOSITION: ACCEPT-WITH-FIXES
FILE inverse-parity/mixdef-low/c2/proof-Rstar-r4.md: DELTA-ACCEPT-WITH-NOTES
FILE inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md: DELTA-ACCEPT-WITH-NOTES
FILE inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md: DELTA-ACCEPT-WITH-NOTES

No FATAL or MAJOR mathematical defect found. The avoider-based closure is valid from the stated imports. The remaining fixes concern change declarations, status wording, and references.

All paths below are relative to `inputs/`; line numbers count LF-separated lines.

**Findings**

- **MINOR — inaccurate change declaration.** `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:301`, also `:8`: “No mathematical statement of Sec. 1-6 changed” is inaccurate. Section 6 corrects realizability and normalized scope and adds Corollary R4-av. Correct statement: “The imported kill lemmas retain their statements; Section 6 contains the listed scope and realizability corrections, additional justification, and the newly named avoider corollary.”

- **MINOR — stale current-status wording.** `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:31` still calls M0 “not independently reviewed,” contrary to the supplied closure reviews and the updated assembly. Correct statement: “M0 was independently re-derived in both closure reviews; the remainder of proof-RUNS.md was not thereby reviewed.” At `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:231`, correct the heading to “Residual of the preceding eliminations, closed for avoiders; evidence [F],” or explicitly restrict “open” to interval-feasible-data emptiness.

- **MINOR — nonresolving relative references.** `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:14` names `c2/proof-MIX-low-partial-r2.md`, although the referenced file is in the same directory. Correct to `proof-MIX-low-partial-r2.md`; likewise remove the extra `c2/` at `:15` and `:17`. The same defect occurs at `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:61`, `:97`, `:99`, and `:100`. At `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:189`, the literal relative reference should be `../../../repr-WAS.md`.

- **MINOR — overbroad unchanged-step claim.** `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:140` should say “The theorem targets and underlying kill constructions are unchanged; normalization, dependency and scope arguments have been made explicit.” The revision adds the explicit normalization endpoint bound, the completed P5 route, and a redundancy observation.

- **NOTE — additional mathematical annotations are correct but incompletely itemized.** `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:41` adds the valid bound
  \[
  BH(Y)\ge 3s+g+4,
  \]
  `:43` adds the valid coarse bound \(k\ge11\), and `:56` adds a weakening observation. For that observation, the precise sufficient statement is: \(\delta^+\ge2s-B\) gives \(BH(S)\le B<BH([k])\); with \(|N|\ge1\), branch (b) gives \(c(S)\ge g+2\), sufficient for KL. The stronger displayed \(g+3\) still uses \(|N|\ge2\). Record these additions in the change log.

- **NOTE — unchanged imports remain literally stale.** `inverse-parity/proof-PAR-K0.md:4` should record the supplied Codex acceptance. `inverse-parity/proof-PAR-Kplus-partial-r2.md:133` should say: “For the PAR application with original \(k\le p\), the remaining range is covered by OR and Theorem M; this does not settle unrestricted MIX_DEF.” Recording these corrections in the new assembly adequately repairs the chain, while leaving the source lines unchanged.

**1. Snapshot, diff fidelity, and declared scope**

Verified: the eight required hashes matched first. Subsequently, all **25 manifest entries** matched their SHA-256 values.

Verified: regenerating each diff with `text.split('\n')`, `n=3`, `lineterm=''`, the stated header labels, and the final serialization LF gave an exact match. Applying each pinned diff in memory reconstructed its new file exactly.

Here, **a** means a named repair, **b** means declared support/status/history, and **c** means an edit not specifically itemized in the fix maps. A merged hunk can contain several classes.

| Exact hunk location | Classification |
|---|---|
| `_parent-derived/diff-Rstar-r3-to-r4.diff:3` — `@@ -1,16 +1,25 @@` | **b**: header, history and status updates. |
| `_parent-derived/diff-Rstar-r3-to-r4.diff:36` — `@@ -173,10 +182,14 @@` | **a**: normalized-avoider qualification and realizability correction/proof. |
| `_parent-derived/diff-Rstar-r3-to-r4.diff:55` — `@@ -189,15 +202,28 @@` | **a+b**: normalized scope, nonemptiness, R4-av support, normalized P5 remark. |
| `_parent-derived/diff-Rstar-r3-to-r4.diff:87` — `@@ -206,7 +232,10 @@` | **b**: universal-proof/status pointer and census separation. |
| `_parent-derived/diff-Rstar-r3-to-r4.diff:99` — `@@ -257,3 +286,17 @@` | **b**: change log. |
| `_parent-derived/diff-R4-closure-r0-to-r1.diff:3` — `@@ -1,70 +1,137 @@` | **a+b+c**: named repairs, expanded proof/status, plus incompletely itemized mathematical annotations at new `:41`, `:43`, `:56`; also deletion of old `proof-R4-closure.md:62`, an evidence-only sentence about census emptiness of R4. |
| `_parent-derived/diff-PAR-assembly-r1-to-r2.diff:3` — `@@ -1,44 +1,76 @@` | **a+b+c**: named scope/P5/status repairs; the correct mathematical dependency observation at new `:54`—K1/K1′ redundancy—is not specifically itemized. |
| `_parent-derived/diff-PAR-assembly-r1-to-r2.diff:112` — `@@ -59,16 +91,51 @@` | **a+b**: import status, scoped corrections to unchanged imports, replacement open-status text, change log. |

The **c** edits introduce correct supporting bounds or dependency observations, or delete evidence text. They change no theorem target or kill construction. The Rstar unchanged-statement claims and assembly unchanged-step claim nevertheless need the qualifications stated above. The closure header and log describe the principal repairs accurately, but do not itemize every added observation or the deleted census sentence.

**2. Map of all 15 requested repairs**

“ADEQUATE—chain” distinguishes a correction recorded in the new chain from an edit to an unchanged import.

| Item | Requested repair | Implementing location(s) | Assessment |
|---|---|---|---|
| Codex MINOR-1 | Replace stale universal-PAR open status | `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:119–125`, also `:36–37` | **ADEQUATE** |
| Codex MINOR-2 | Separate realizability from avoidance | `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:187–192` | **ADEQUATE** |
| Codex MINOR-3 | Qualify historical “Theorem PF” log | `inverse-parity/mixdef-low/c2/README.md:109–112`; `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:42–44` | **ADEQUATE** |
| Claude MINOR-1 | Use avoider-data exclusion, not interval-feasible emptiness | `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:65–80`; `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:215–221` | **ADEQUATE** |
| Claude MINOR-2 | Justify BH budget and properness before counting blocks | `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:51–54` | **ADEQUATE** |
| Claude MINOR-3 | Prove \(Z_0^+\ne\varnothing\) before using \(m\ge1\) | `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:208–211`; `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:31–34` | **ADEQUATE** |
| Claude MINOR-4 | Restrict residual assertions to normalized avoiders | `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:185–186`, `:205–206` | **ADEQUATE** |
| Claude MINOR-5 | Supply normalization and \(B'=0\) handling for P5 | `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:67–68`; `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:223–226` | **ADEQUATE** |
| Claude MINOR-6 | Supersede assembly open status and qualify Kplus:133 | `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:107–112`, `:119–123` | **ADEQUATE—chain**; import unchanged |
| Claude MINOR-7 | State \(F,R\ge1\) in P | `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:84–91` | **ADEQUATE** |
| Claude MINOR-8 | State consequence through DR-Res + DR′ | `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:96–99`; `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:124–125` | **ADEQUATE** |
| Claude MINOR-9 | Define \(X,\delta^+\) locally; describe replay weakening | `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:21–22`, `:107–112` | **ADEQUATE** |
| Claude MINOR-10 | Mark historical PF log superseded and conditional | `inverse-parity/mixdef-low/c2/README.md:109–113` | **ADEQUATE** |
| Claude MINOR-11 | Correct K0 review status | `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:94`, `:105–106`; `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:28–30` | **ADEQUATE—chain**; import unchanged |
| Priority scout | Define inherited by all five conditions; spell out rigid family | `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:22–32`; `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:63–64`, `:84–91` | **ADEQUATE** |

The outside-scope corrections are sufficient for this chain because no proof uses the obsolete status assertions. They are not literal repairs of the import files. The Kplus correction appropriately preserves the distinction between MIX_low and unrestricted MIX_DEF.

**3. Corollary R4-av**

Its exact statement at `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:215–216` is:

> Every normalized MIX_low avoider (after Lemma M0, with B >= 1 and A <= 2p-1) has lift data (r2 Lemma S) in R4.

I re-derived the elimination chain, checking the imported hypotheses:

1. **MIX-R:** the normalized setting and avoidance supply S-lifts; outside R*, one of MIX-R’s two thresholds holds.
2. **W:** requires \(B\ge g+1\), with no R* assumption. Survival gives \(B\le g\).
3. **B1:** requires some \(d_t\ge2p-B\), with no R* assumption. Survival excludes those masses.
4. **A:** now operates inside R*. Survival gives every \(bh_t\le B\).
5. **Fact F:** the preceding mass and BH restrictions force every \(d_t\le2g+B-2\), hence every \(\phi_t\le g-1\).
6. **AC:** applies inside R* if every run is cheap.
7. **KS:** now has its required “not every run cheap” hypothesis. Surviving its integer threshold gives \(2\phi(Z_0^+)+\alpha\ge2g+s+S_Z\).
8. **ZP:** survival gives \(c(Z_0^+)\le g\).
9. **C:** all other runs satisfy its \(\phi\)-bound; its exceptional run satisfies
   \[
   \phi_{t_0}\le g-1\le p-k+g
   \]
   because \(k\le p\). Survival gives every \(bh_t\le s\).

These surviving restrictions are exactly R4 as defined at `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:207`.

Omitting G1 is harmless. None of these applications needs \(g\ge2\), and the eventual R4 restrictions themselves imply \(g\ge B\ge s+2\ge3\). Lemma R4 does not need an additional G1 invocation.

The conclusion is precisely the avoider-data hypothesis excluded by `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:26–27`. R4-av is a new named corollary and explicit proof packaging of the implication already asserted at `inverse-parity/mixdef-low/c2/proof-Rstar-r3.md:192`, with the required qualifiers.

**4. Lemma R4**

The lemma’s scope, construction, dichotomy and conclusion are unchanged. Revision r1 supplies missing justification and puts properness before the block-count lower bound.

I re-derived the following:

- **(iii):** If \(Z_0^+=\varnothing\), then \(X=\alpha=0\), contradicting
  \[
  2X+\alpha\ge2g+s+S_Z>0.
  \]
  The free set is proper because its BH is nonpositive whereas \(BH([k])=B+s+1>0\). Thus \(m(Z_0^+)\ge1\), \(X\le g-1\), and
  \[
  \alpha\ge2m(Z_0^+)+s+S_Z\ge s+2,\qquad
  B\ge\alpha,\qquad s\le B-2\le g-2.
  \]

- **(iv):** Every aligned defect is free and contributes at least one to \(X\); defect pairs are free. Consequently
  \[
  D(Z_0^+)=S_Z+n_d-\text{free-anti mass},
  \]
  \[
  \delta^+\ge2X+\alpha-S_Z-n_d\ge2g+s-n_d
  \ge g+s+1.
  \]

- **Step 1:** \(Y\ne\varnothing\), since total BH is positive, and \(Y\ne[k]\), since \(Z_0^+\ne\varnothing\). Its components are paths. Combining \(B\ge s+2\) with the delta bound gives
  \[
  BH(Y)\ge3s+g+4.
  \]
  Taking the heavier parity class in each component produces an independent union in the cycle. Here \(s\ge1\), \(B,g\ge3\), so \(k=2g+B+s+1\ge11\). Greedy accumulation of positive weights at most \(s\) gives
  \[
  s+1\le BH(N)\le2s,\qquad |N|\ge2.
  \]

- **Step 2(a):** The complement \(S'\) is nonempty and proper. Independence gives exactly \(m(S')=|N|\), so the stated branch inequality yields \(c(S')\ge g+1\), while \(BH(S')\le B\). KL applies.

- **Step 2(b):**
  \[
  BH(S)\le2s-\delta^+\le s-g-1\le B-g-3<B.
  \]
  Since \(BH([k])=B+s+1>B\), \(S\) is proper. Only then is \(m(S)\ge1\) used to obtain
  \[
  c(S)\ge X+\phi(N)+1\ge g+3.
  \]
  KL applies.

Every required fact is available before use, including properness of the free set from positive total BH. The remark at `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:56–57` is correct as a statement about sufficient KL conditions; the weaker \(g+2\) conclusion explained in the finding is enough.

**5. Theorem M**

The statement equals the frozen MIX_low target. Its explicit rigid-family gloss agrees with RGR_N in the supplied definitions. The definition
\[
\kappa=p-1-H
\]
is at `inverse-parity/mixdef-low/README.md:10`; \(H=\sum_j\lfloor l_j/2\rfloor\) is also explicitly given in the new assembly at `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:25`. Theorem M imports this notation rather than repeating the definition.

The proof is valid entirely on avoider data:

- **Step 0:** \(A\ge2p\) supplies \(2p\) equal rotations. Otherwise
  \[
  A=2p-k+2g+B\le2p-1
  \iff 2g+B\le k-1.
  \]

- **Step 1:** I re-derived M0’s window monotonicity. Removing opposite rotations decreases each effective count \(E^\pm\) by one. Adding two equal reflections preserves boundary parities and phase and raises the reflection-pair contribution by one. Each half-window therefore shrinks, including empty/full-pattern windows. Length, \(k,d_t,\theta\), and reflection parities persist; \(A,B,\kappa\) each decrease by one, so \(g\) persists. No run vanishes. Avoidance transfers in the required direction. Decreasing nonnegative integer \(B\) ensures termination at pure runs or (1,1)-pairs.

- **Step 2:** If \(B'=0\), all rotations are \(\rho_1\), all reflection runs remain odd, \(k\le p\), and \(\kappa'=g\ge1\). Using the **original** \(B\ge1\),
  \[
  k\ge2g+B+1\ge2g+2,\qquad
  R'=A-B=2p-k+2g\le2p-2.
  \]
  These are exactly S1′’s required hypotheses. A1′ and a further trivial cut are unnecessary here.

- **Step 3:** If \(B'\ge1\), all normalized MIX_low hypotheses persist: odd reflection runs, \(k\le p\), \(A'>B'\), \(B'<\kappa'\le k-1\), \(A'\le2p-1\), and pure/pair rotation runs. Lemma S, R4-av and Lemma R4 apply successively.

No inherited inequality is improperly reused after M0. Neither Corollary′, Theorem PA’s hypothesis, nor census output is used.

**6. Theorem P and the PAR assembly**

The five conditions at `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:88–89` and `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:27–28` correctly copy (E), (P), (V), (Pairs), and (D0). With \(F,R\ge1\), the statement is exactly PAR at `proof-INV-reduction.md:41–42`.

Hypothesis matching checks:

- Sign normalization preserves the inherited conditions and avoidance.
- Avoidance first gives \(A,B\le2p-1\); only then is Lemma H’s simplified zero condition used to obtain \(B\le\kappa\).
- (Pairs) gives \(\kappa\ge0\); (V) gives \(\kappa\le o_F-1\).
- At \(\kappa=0\), an assumed even run permits K0, with its required (P), (V), \(F,R\ge1\), and \(k\le p\).
- At \(\kappa\ge1\), \(o_F\ge2\), so OR is applicable. It gives \(k(\widetilde w)=o_F\le k\le p\), all reflection runs odd, and unchanged \(A,B,\kappa\).
- S1′/A1′ do not require the possibly lost (P) or (D0).
- KB is applied with (V), \(o_F\le p\), and original-word (D0) in its capped case.
- If separately used, K1′ likewise has original-word (D0).

The cases
\[
\kappa=0;\qquad
\kappa\ge1,\ B=0;\qquad
B=\kappa\ge1;\qquad
1\le B<\kappa
\]
are exhaustive because \(0\le B\le\kappa\). K1 and K1′ are redundant: at \(\kappa=1\), \(B\) is either zero or \(\kappa\).

For the **general B=0 route**, S1′ and A1′ cover distinct possible ranges after OR. The trivial \(R\ge2p\) cut completes the unrestricted range classification. However, in this particular contradiction proof it has already been discharged by \(A\le2p-1\): with \(B=0\), \(R=A\). Thus all three are **not separate reachable post-OR cases**. This redundancy is harmless. Unlike Theorem M’s endpoint, the general PAR route does not force \(R\le2p-2\), so A1′ remains relevant.

The cross-file references do not create a mathematical cycle: M is proved independently; the PAR assembly then invokes M.

**7. Consequence wording**

Correct:
\[
\text{INV*}(p)+\text{PAR}(p)+\text{RUNS}(p)
\Longrightarrow \text{ordered Olson for }D_{2p}.
\]

PAR + RUNS gives INV_Res and therefore DR-Res’s RGR length-\(4p-1\) conclusion. DR′’s proof first obtains RGR membership using INV*, then needs precisely that conclusion; it does not otherwise use unrestricted INV.

The statements at `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:96–99` and `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:123–125` are therefore correct. None of the three new files claims to prove RUNS, INV, INV*, or ordered Olson.

**8. Realizability**

The repaired argument is correct. Using integer representatives before reduction modulo \(p\),
\[
\sum_t(d_t-\phi_t)
=D-(p-k+2g)=p.
\]
Thus \(\theta_t=2(d_t-\phi_t)\pmod p\) has zero sum. The reconstruction in `repr-WAS.md:11–12` supplies reflection values \(y\), consistently with \(u_Q=2^{-1}\sum_Q\theta_t\).

The normalized \(d\)-data determine nonempty pure rotation runs or (1,1)-pairs. Since
\[
H=p-1-\kappa\ge0,
\]
one can assign odd reflection lengths totaling \(F=k+2H\). Moreover,
\[
R=2p-k+2\kappa,\qquad R+F=4p-2.
\]

The remark explicitly declines to infer non-interval avoidance or an ordered-product counterexample. That repairs the original conflation.

**9. Census and replay labeling**

The operative PF statement is historical, [W+F], conditional on unreviewed census code, and superseded by M/P. The README correction is adequate.

Those three labels are **not literally repeated at every cross-reference**: for example, `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:237–238` says only “conditional evidence.” The surrounding qualifications prevent a substantive unqualified theorem claim.

The census/replay assertions in the three files are:

| File and lines | Assertions dependent on reported computation |
|---|---|
| `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:245–246` | Counts at \(p=5,7,11,13\), R* sizes, reported finite emptiness. |
| `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:247–259` | Claimed complete \(p=17\) census, 150 configurations, their parameters, successful kills, reported emptiness. The accompanying pruning argument is mathematical; its correspondence to the unpinned code is unchecked. |
| `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:260–265` | Replay counts, zero failures, hypothesis checks, mutation rejections. |
| `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:266–270` | Relaxed-search counts, emptiness observations, CPU-limit outcomes. |
| `inverse-parity/mixdef-low/c2/proof-Rstar-r4.md:271–275` | Cross-check samples, solution counts, zero mismatches. |
| `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:103–106` | Replay provenance and \(p=11\) applicability/success claims. |
| `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:107–112` | Synthetic success counts and mutation rejections. |
| `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:113–114` | Earlier synthetic counts and mutation rejections. |
| `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:42–44` | Historical conditional PF assertion for the four listed primes. |
| `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:75–86` | Census completeness, configuration counts, certificates, emptiness, and sampled cross-check descriptions. |
| `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:101` | Reported sampled cross-check with zero mismatches. |

The evidence/status wrappers and historical references also occur at Rstar `:19–20`, `:233–244`, `:285–286`; closure `:101`, `:115`, `:127–128`; assembly `:15`, `:71–73`, `:113–115`, `:136–137`. These are descriptions or qualifications of the evidence, not additional numerical premises.

**None of M, P, PA, or P5 depends on census or replay output.**

**10. Residual staleness and reference consistency**

Besides the findings:

- `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:98` should describe the **v2 portions within** r3/r4 Sections 1–6, rather than suggesting that those entire sections equal v2. Later additions are separately identified at `:99`.
- Bare root-document references at `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:17`, `:22`, and `inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:97` need `../../../` if intended as literal relative paths.
- `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r2.md:50` needs `../../proof-PAR-K0.md`.
- Extra `c2/` prefixes also occur in historical/evidence references at Rstar `:243`; closure `:103–104`; assembly `:81`, `:84–85`, `:113`. Correct local paths remove that prefix.
- Assembly `:123` uses the original closure filename for an active conclusion. Its mathematics is the same, but the current reference should be `proof-R4-closure-r1.md`.
- Rstar `:234`’s r1 assembly reference and assembly `:81`’s r3 reference are explicitly historical. They are not evidence that the current proof accidentally uses obsolete mathematics.
- Rstar `:15` and `:287` retain “unreviewed” inside explicitly historical r3 descriptions; those differ from the stale current M0 status at `:31`.

In the unchanged imports, the principal stale lines remain K0 `:4` and Kplus `:133`. Related historical open-status text remains at `inverse-parity/proof-PAR-K0.md:157–162` and `inverse-parity/proof-PAR-Kplus-partial-r2.md:10`, `:122`, `:138–141`, `:313–314`. Read these as the earlier file-local state, superseded for the PAR/MIX_low application. The broader MIX_DEF scope is not thereby closed.

**11. Additional mathematical content**

Beyond the named R4-av and realizability proof, the revisions make additional mathematical assertions explicit:

- \(BH(Y)\ge3s+g+4\);
- \(k\ge11\);
- branch (b)’s weaker sufficient delta bound and unnecessary \(|N|\ge2\);
- K1/K1′ redundancy;
- the stronger specialization that S1′ always handles \(B'=0\) after MIX_low normalization.

I re-derived these assertions; they are correct. Several were already observations in the supplied reviews. They add supporting arithmetic and dependency clarification, without changing the target theorem scopes beyond the requested corrections. No additional independent lemma or strengthened theorem was silently introduced.

Computed: **25 SHA-256 checks, three exact diff regenerations, and three in-memory diff reconstructions**. The proof checks above were static algebraic reasoning. No arithmetic sampling or enumeration campaign was performed.

**Established**

From the stated imports: Lemma R4 excludes normalized avoider data in R4; R4-av supplies exactly those data; M proves MIX_low(p), and P proves PAR(p), for every prime \(p\ge5\). PA remains a valid conditional, and P5 has a written-proof route. M0 monotonicity and realizability arithmetic were independently re-derived.

**Open**

This packet does not establish RUNS(p), unrestricted INV(p), INV*(p), or ordered Olson for all primes. It does not establish unrestricted MIX_DEF or emptiness of interval-feasible R4 data; the latter is unnecessary for M/P. The \(p=3\) case is outside scope.

**UNKNOWN**

Claimant code fidelity, reported census/replay counts, runtime claims and mutation results were not independently checked. Claimant-file import/execution/compilation, censuses, replays, solvers, network, delegation and explicit file writes: **NOT RUN**.