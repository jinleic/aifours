DISPOSITION: ACCEPT-WITH-FIXES
ASSEMBLY (Q1-Q4, Q8, Q9): VALID conditional assembly; wording fixes below.
NEW-IMPORTS (Q5): FULLY VERIFIED at the stated scopes, relative to their named imports.
USES (Q6): Hypotheses match; no substantive defect found.
FOUNDATIONS (Q7): GR/WAS verified; deletion arguments checked; Q7 INCOMPLETE at upstream filter proofs absent from the snapshot.
INV*-SEPARATE: YES

Both required hashes match. All 29 manifest-listed files also match their recorded hashes. All citations below are relative to S and use LF line numbers. No computation, network access, writes or delegation was used beyond permitted file reading and hashing.

## FATAL

none

## MAJOR

none

## MINOR

1. **`olson-runs-assembly-proof-v2.md:43` — qualify the assertion that only one direction of HW is used.**

   That describes direct window certificates, but not the full imported proof chain. OR and M0 require the equivalence:

   \[
   w\text{ avoids}\Longrightarrow\text{all old windows avoided}
   \Longrightarrow\text{all reduced windows avoided}
   \Longrightarrow w_{\rm reduced}\text{ avoids}.
   \]

   The last implication uses the converse of the one-pattern implication. See `olson/inverse-parity/proof-PAR-Kplus-partial-r2.md:30` and `olson/inverse-run-count/proof-RUNS.md:408`.

   **Correction:** “Direct window certificates use only the one-pattern implication; the avoidance transfers OR and M0 use the full HW/H equivalence.” That equivalence is available and correct, so this does not invalidate a transfer.

2. **`olson-runs-assembly-proof-v2.md:149` — the corollary heading is misleading.**

   “And kappa > B for every RGR word” can read as a universal inequality. The formal statement at line 150 correctly asserts solvability **in the regime** \(1\le B<\kappa\).

   **Correction:** “MIX_DEF(p), and solvability for arbitrary reflection parities when \(1\le B<\kappa\).”

   The literal universal inequality is false: for every odd prime,
   \[
   w=\rho_1^{\,2p-1}\sigma_0^{\,2p-1}
   \]
   has \(B=\kappa=0\). It is even an avoider: an identity selection must use an even number of reflections, hence an even number \(q\in\{2,4,\ldots,2p-2\}\) of rotations. Its product is \(\rho_q\ne1\), since the only intervening multiple of odd \(p\) is odd. This counterexample concerns the heading’s literal reading, not the correctly quantified corollary.

## Q1. RUNS coverage and hypotheses

The six branches are exhaustive. After normalization, Fact Z gives
\[
0\le B\le\kappa.
\]
Thus \(B=0\) gives C1/C2; \(B\ge1\) gives equality or strict inequality with \(\kappa\), followed by the exhaustive integer split \(o_F\le p\) or \(o_F\ge p+1\). See `olson-runs-assembly-proof-v2.md:155`.

The common original word \(w'\) has length \(4p-2\), \(F,R\ge1\), all five inherited conditions, and normalized \(A\ge B\). Reflection parity is unrestricted. OR preserves \(F,R,A,B,H,\kappa\), produces nonempty runs, and gives \(\widetilde k=o_F\) with all reflection runs odd.

| Branch | Hypothesis check |
|---|---|
| **C1: \(B=0<\kappa\)** | OR is available because \(o_F\ge1\). The merged word has only \(\rho_1\) rotations. For \(\widetilde k\le p\), S1′ applies when \(R\le2p-2\), A1′ when \(R=2p-1\), and the cut when \(R\ge2p\). For \(\widetilde k\ge p+1\), C0-B′/A1/cut apply. None requires inherited inequalities of \(\widetilde w\). Sources: `olson/inverse-parity/proof-PAR-Kplus-partial-r2.md:164`, `:207`; `olson/inverse-run-count/proof-RUNS.md:318`, `:348`, `:377`. |
| **C2: \(B=\kappa=0\)** | Applied to the **original** \(w'\). Here \(R=2p-o_F\), \(R\ge k\ge p+1\), so \(1\le o_F\le p-1<k\): an even reflection run exists. Also \(R\ge p+1\ge6\). Original (P) supplies \(e_R\le e_F\); (V), or Fact Z, supplies \(o_F\ge1\). No merging occurs. Source: `olson/inverse-parity/proof-PAR-K0.md:98`. |
| **C3: \(B=\kappa\ge1,\ o_F\le p\)** | KB requires \(F,R\ge1\), normalization, equality \(B=\kappa\), (V), and \(o_F\le p\), with arbitrary original \(k\) and parities. All hold. Its exceptional capped case uses **(D0) of \(w'\)**. Source: `olson/inverse-parity/proof-PAR-Kplus-partial-r2.md:238`. |
| **C4: \(B=\kappa\ge1,\ o_F\ge p+1\)** | These are exactly KBH’s hypotheses, together with the common length, \(F,R\ge1\), and normalization. KBH requires neither all-oddness nor inherited conditions. Source: `olson/inverse-run-count/kappaB-high/proof-KBH.md:10`. |
| **C5: \(1\le B<\kappa,\ o_F\le p\)** | The merged word is all-odd, \(\widetilde k=o_F\le p\), \(A\ge B\ge1\), and \(B<\kappa\). Moreover Fact Z gives \(\kappa\le\widetilde k-2\), stronger than M’s \(\kappa\le\widetilde k-1\). No (P) or (D0) is needed on it. Sources: `olson/inverse-parity/mixdef-low/c2/obligations-after-PAR.md:40`; `olson/inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:61`. |
| **C6: \(1\le B<\kappa,\ o_F\ge p+1\)** | The original word directly satisfies MIX_DEF_HIGH’s length, \(F,R\), normalization, minority-count and odd-run-count hypotheses. Theorem B supplies its reductions. |

**K0 extension:** every actual use of \(k\le p\) is replaced correctly. At `olson/inverse-parity/proof-PAR-K0.md:102`, the required consequence is \(R\ge p\); here \(R\ge p+1\). At line 141, it is \(o_F\le p\); here \(o_F\le p-1\). The remaining partition and BC arguments impose no upper bound on \(k\). Consequently the extension at `olson/inverse-run-count/proof-RUNS.md:383` is valid.

Indeed, for \(k\ge p\), (P) is already automatic:
\[
F+\sum_i\lfloor r_i/2\rfloor
\le F+\sum_i(r_i-1)=4p-2-k\le3p-2.
\]

Remark (2) is correct: C1 and C3–C6 exclude every normalized inherited avoider with \(\kappa>0\), independently of the assumed \(k\ge p+1\). Hence every inherited avoider has \(B=\kappa=0\). C2 then supplies the run-count exclusion.

## Q2. Facts Z, T, K and transfers

**Fact Z is valid**, including automatic (V). The empty-pattern certificate gives \(B\le\kappa\), while avoidance gives \(A\le2p-1\). Therefore
\[
2p-o_F+2\kappa=A+B\le2p-1+B,
\]
so
\[
o_F\ge2\kappa-B+1\ge\kappa+1\ge1.
\]
Thus \(\kappa\le o_F-1\), exactly (V). If \(B\le\kappa-1\), this strengthens to \(o_F\ge\kappa+2\). Source: `olson-runs-assembly-proof-v2.md:68`.

**Fact K is valid:**
\[
A=2p-k+2\kappa-B\le2p-1
\quad\Longrightarrow\quad
2\kappa-B\le k-1.
\]
Since \(B\le\kappa-1\), this gives \(\kappa\le k-2\). Source: `olson-runs-assembly-proof-v2.md:89`.

**The transfer cautions are real.** For example, at \(p=5\), take \(b_i=0\) and

- \(r=(1,1,1,1,3)\), \(l=(2,1,2,1,5)\). All five inherited inequalities hold. OR produces \(\widetilde r=(2,2,3)\), \(\widetilde l=(3,3,5)\). The left side of (P) changes from \(11+1=12\) to \(11+3=14>13\).
- \(r=(3,3,3)\), \(l=(2,2,5)\). Again the inherited inequalities hold, but OR merges the rotations into one run of nine \(\rho_1\)’s, violating (D0).

These illustrate loss of inherited conditions; they are not claimed avoiders.

For M0, the left side of (P) increases by exactly
\[
2+\lfloor(r_t-2)/2\rfloor-\lfloor r_t/2\rfloor=1.
\]
Its window calculation is nevertheless correct:
\[
g'_P(E-1)
=\min\{p-m,\ E+m+h-p,\ \lfloor(E-1)/2\rfloor\}
\le g_P(E).
\]
Sources: `olson/inverse-parity/proof-PAR-Kplus-partial-r2.md:24`; `olson/inverse-run-count/proof-RUNS.md:402`.

No prohibited transfer is used:

- KB’s capped case returns to the **original word** before invoking (D0).
- B0, RL and the MIX_DEF_HIGH reduction invoke results whose hypotheses concern preserved parameters, or which explicitly require no inherited conditions.
- C0-B′’s removal of inherited hypotheses is justified below.

Thus the target’s audit at `olson-runs-assembly-proof-v2.md:206` is correct when “after OR or M0” means **on the reduced word**. (E) is unused; (P) is available on the original word in C2; (D0) is used only on the original word in C3.

## Q3. Theorem B

The reduction is valid. See `olson-runs-assembly-proof-v2.md:139` and `olson/inverse-run-count/mixdef-high/README.md:18`.

1. The \(A\ge2p\) cut selects \(2p\) copies of \(\rho_1\).
2. Otherwise OR gives an avoiding all-odd word with
   \[
   p+1\le\widetilde k=o_F\le2p-1.
   \]
   At the upper endpoint all runs are singletons, so ALT applies.
3. For \(\widetilde k\le2p-2\), each M0 operation leaves the affected rotation run nonempty, preserves reflection parities and \(\phi\), and decreases \(B\) by one. Therefore iteration terminates with pure runs or \((1,1)\)-pairs.
4. Throughout,
   \[
   \widehat\kappa-\widehat B=\kappa-B\ge1,\qquad
   \widehat A-\widehat B=A-B\ge0,\qquad
   \widehat A\le A\le2p-1.
   \]
5. If \(\widehat B\ge1\), every NMH hypothesis holds, including the full range \(p+1\le\widehat k\le2p-2\).
6. If \(\widehat B=0\), then \(\widehat\kappa=\kappa-B\ge1\). C0-B′ handles \(\widehat R\le2p-2\), and A1 handles \(\widehat R=2p-1\). The listed \(\widehat R\ge2p\) cut is valid, although unreachable after the preliminary \(A\le2p-1\) restriction.

No inherited inequality is invoked on \(\widehat w\).

## Q4. Theorem A and the exact GC scope

The FW+ application matches all hypotheses of `olson/inverse-run-count/mixdef-high/c2/proof-C2.md:119`:

- all-odd;
- \(k\ge p+1\);
- pure/\((1,1)\) runs;
- \(A,B\le2p-1\);
- \(\min(A,B)=B\le\kappa-1\).

Its cases match separately:

- \(R=2p-2\): R2 permits arbitrary rotation letters and arbitrary \(B\).
- \(R=2p-1\): FWH(a) needs only \(k\ge3\).
- \(R=2p\): FWH(b) needs \(k\ge6\), supplied by \(k\ge p+1\).
- \(R\ge2p+1\): with \(W=2p-k+1\), the integer complement of \(|d_u|\le W\) for every run is \(|d_u|\ge W+1=2p-k+2\) for some run. This is exactly BR’s threshold.

For \(R\le2p-3\), the word class at `olson/inverse-run-count/mixdef-high/c3/proof-C-r1.md:19` matches the target exactly. Its later hypothesis (H) belongs to that file’s own theorem; **NMH-iii does not impose (H)**. The assumed theorem at `olson/inverse-run-count/mixdef-high/c6/proof-GC.md:109` explicitly covers the whole initial NMH setting, including \(k=p+1\).

Also,
\[
\Delta_0=2p-R\ge3,\qquad
k=2\kappa+\Delta_0
\ge2(B+1)+3\ge7.
\]
Thus there is no missing \(k=p+1\), small-\(k\), region or positive-excess restriction in the application of (GC). I have treated its proof as a hypothesis, as authorized.

## Q5. Full-source checks of the new imports

**Every requested Q5 item is verified at its stated target scope.** The following gives the principal hand checks.

**FWH — verified.**  
Source: `olson/inverse-run-count/mixdef-high/proof-MH.md:54`.

For \(R=2p-1\), \(m=m^*=\lfloor\kappa/2\rfloor+1\) and \(\kappa\le x,R-x\) make both floor terms active. Their sum is \(p-1\).

For \(R\ge2p\), put \(y=R-x\). The nine pairwise sums between the three terms defining \(g_m(x)\) and \(g_m(y)\) reduce, by symmetry, to these six checks:
\[
\begin{aligned}
2(p-m)&\ge p-1,\\
(p-m)+(y+m-1-\kappa)&\ge p-1,\\
(p-m)+\lfloor y/2\rfloor&\ge p-1,\\
R+2m-2-2\kappa&=2p-k+2m-2\ge p-1,\\
(x+m-1-\kappa)+\lfloor y/2\rfloor
&\ge\frac{x+2m-3-2\kappa+R}{2}\ge p-1,\\
\lfloor x/2\rfloor+\lfloor y/2\rfloor&\ge(R-2)/2\ge p-1.
\end{aligned}
\]
The defining bounds on \(m\), \(x,y\ge\kappa\), and \(\kappa\le p-1\) supply each inequality.

The missing-looking interval check also holds:
\[
m_{\rm lo}\le
\left\lceil\frac{\kappa+1}{2}\right\rceil
=\lfloor\kappa/2\rfloor+1=m^*
\]
because \(k\le2\kappa\). The coloured-cut path to the complement exists. Its step bounds in (a), (b), (c) are respectively \(W-1,W,W\); skipping an interval containing \(W\) integers requires a step at least \(W+1\). Hence all three clauses follow.

**ALT, TL and KW — verified.**  
Sources: `olson/inverse-run-count/proof-RUNS.md:34`, `:65`, `:87`.

ALT’s vacancy rotation swaps the alternating arc colours and preserves \(p+1\) boundaries. Since \(d_t=\pm1\), the odd quantity \(E^+-E^-\) changes by \(\pm2\) and goes to its negative. It therefore reaches \(\pm1\), giving \(\{E^+,E^-\}=\{p-1,p\}\) and FW’s full window.

TL’s empty/full windows are nonempty under its length-\(4p-2\) hypotheses; their unique allowed representatives are \(0,p\). Telescoping gives \(\sum x_t=p\). KW follows by substituting
\[
X_P=\frac{D_P+|P|-e(P)}2
\]
into the three upper and three lower half-window bounds. Negative endpoints do not change the equivalences.

**S1 Steps 0–2, Split, Depth, C0-B and C0-B′ — verified.**  
Sources: `olson/inverse-run-count/proof-RUNS.md:188`, `:250`, `:318`.

The essential generalized parameter bounds are
\[
k\ge2\kappa+2,\qquad R\ge p,\qquad k\le R\le2p-2.
\]
The chain/singleton comparison yields canonical defect lifts and
\[
\delta_t\le2\kappa-2-r_t,\qquad
\Phi(Z)\ge2\kappa+2.
\]

Crucially, C0-B′ legitimately removes the inherited ND invocation:
\[
Z=\varnothing\Longrightarrow
2p-R=\sum bh_t\ge k
\Longrightarrow\kappa\le0,
\]
contrary to its hypothesis. No (D0) is needed here.

If \(\kappa=1\), the shallow-defect bound is already impossible. Otherwise \(\kappa\ge2\), hence \(k\ge6\), providing room for the Depth construction. For its chosen \(m\), \(3m\le k-2\). The three cases for its maximum give
\[
\rho+r_t+2m\le
5+R-k,\quad
2R-2p+3-r_t,\quad
3R-4p+4,
\]
respectively; each is at most \(2p-2\) in the extended range. The other floor-activation bounds remain valid.

Split is a direct interval argument: its two inequalities place the sum of the two lifts in \([-L_Q,p+U_Q]\); avoidance leaves exactly the central gap. In the Depth application, its second inequality has lower bound
\[
L_P+L^t+U_{P+t}\ge R-1\ge p-2.
\]
The resulting bound is
\[
\delta_t\le2p-R-2.
\]

At the first greedy crossing,
\[
\delta_P\le k-i^*-2\le R-1,\qquad
\Phi(P)\le k+r_t+1\le R+2\le2p.
\]
These give K4, K3 and K6. For K5,
\[
\delta_P+\rho_P-2m
=\Phi(P)-4m
\le k+r_t-3
\le R-2
\le2R-2\kappa-2.
\]
K1 and the parity condition K2 hold as stated. This checks the load-bearing C0-B′ chain without transferring inherited inequalities.

**A1 and B0 — verified.**  
Sources: `olson/inverse-run-count/proof-RUNS.md:348`, `:377`.

A1 is the constant-rotation version of the FWH(a) calculation. Its coloured-cut path has a vacancy because \(k=2\kappa+1\ge2m^*+1\). Its steps are at most \(2p-k\), smaller than the target interval’s \(2p-k+1\) integers. B0 then follows by OR and the exhaustive three-way split in \(R\).

**RL — fully verified as a citation proof.**  
Source: `olson/inverse-parity/mixdef-low/c2/obligations-after-PAR.md:38`.

The full RL proof covers more than C5: B0/K0 remove the zero cases; KB handles \(B=\kappa\) on the original inherited word; M handles \(B<\kappa\) on the merged all-odd word. Its capped-case (D0) is not transferred to the merged word.

**K0 extension and NMH ⇒ MIX_DEF_HIGH — verified.**  
Sources: `olson/inverse-run-count/proof-RUNS.md:383`; `olson/inverse-run-count/mixdef-high/README.md:18`.

Their complete hypothesis checks are given under Q1 and Q3. No additional inherited condition or finite certificate is concealed in either reduction.

## Q6. Previously reviewed imports

Every use matches its stated hypotheses:

- **R2/BR/FW+:** checked under Q4, including the exact integer oversized-run threshold.
- **KBH:** applied to the original word with \(B=\kappa\), \(o_F\ge p+1\), normalization and \(F,R\ge1\); no purity or inherited assumption is smuggled in.
- **OR/S1′/A1′/KB:** OR is invoked only with \(o_F\ge1\); low-\(k\) statements receive \(\widetilde k=o_F\le p\). KB’s capped argument explicitly returns to the original word at `olson/inverse-parity/proof-PAR-Kplus-partial-r2.md:277`.
- **H/BC/K0:** the corrected empty-pattern bound \(A,B\le2p-1\) is always supplied by avoidance and persists under OR/M0. BC imposes no bound \(k\le p\).
- **HW:** its half-window formula, including empty/full patterns with \(m=0\), is correct. From `olson/inverse-run-count/README.md:24`,
  \[
  C_{\max}=2m+2h,\qquad
  \left\lceil L/2\right\rceil=-g_P(E^-),\quad
  \left\lfloor U/2\right\rfloor=g_P(E^+).
  \]
  Dividing attainable even integers by two is valid modulo odd \(p\).

I found no substantive defect in these applications.

## Q7. Foundations and audit boundary

**GR and WAS are fully verified.** See `olson/proof-GR.md:38` and `olson/repr-WAS.md:16`.

For fixed zone signs, reflection counts realize precisely the even integers \(C\in[\Phi,C_{\max}]\). Eliminating \(C\) from the rotation-count constraints gives exactly the displayed Ach interval. Also
\[
\tau(z_P)=\tfrac12\sum_i z_i\theta_i
=\sum_{i\in P}\theta_i,
\]
because \(\sum_i\theta_i=0\). This proves WAS and then H/HW. Cyclic rotation preserves identity products by conjugation, so no rearrangement of selected letters is introduced.

The **DR/DR-Res deletion logic and DR′ membership argument check out**:

- An in-run deletion removes no run and changes none of the five inherited quantities upwards.
- RUNS first gives the common \(k\le p\); PAR then supplies the parities for deletions from \(X,Y\).
- Two long runs give contradictory parities. With one long run,
  \[
  |X|=4p-2k\ge2p,
  \]
  giving the stated reflection solution or the quoted Doubling application.
- DR′ preserves a forbidden rotation value/pair, or adjacent unequal reflections, by deleting an unrelated letter.

Sources: `olson/proof-INV-reduction.md:27`, `:44`; `olson/proof-DR.md:25`, `:47`.

**Q7 INCOMPLETE:** the upstream proofs of the earlier gap-bound Theorem P, Davenport-alpha and Doubling are not included in the manifest. Their quoted uses and the subsequent reductions were checked; their full proofs were not. Here the earlier “Theorem P” is the gap-bound import, not the later PAR theorem.

## Q8–Q9. INV*, circularity and finite evidence

INV* remains separate. None of the audited RUNS/NMH/MIX statements establishes membership in RGR for arbitrary avoiders. GR/WAS assume the rigid rotations and constant reflection runs; they do not derive either property. The partial-results summary likewise leaves both general obligations unresolved: `olson/inverse-parity/mixdef-low/c2/invstar/results.md:69`.

Consequently neither half (a) nor half (b) is discharged by this assembly. Substituting DR-Res’s RGR-long conclusion into DR′ is valid, but still requires INV*. The target correctly does not claim ordered Olson.

There is no RUNS–PAR circularity. RUNS uses **MIX_low/Theorem M**, whose proof does not require PAR; PAR is applied after RUNS. See `olson/inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md:65` and `olson-runs-assembly-proof-v2.md:179`.

No finite census, replay or certificate table is used as a mathematical premise. No solution of a relaxed window system is treated as a group counterexample.

## FULLY CHECKED:

- Target Facts Z, T, K; assembly deductions A–D and the conditional deduction E.
- FWH(a)–(c).
- ALT and its FW certificate; TL and KW in the target length-\(4p-2\) scope.
- S1 Steps 0–2; Split; Depth; C0-B; C0-B′; A1; B0.
- The K0 extension and NMH ⇒ MIX_DEF_HIGH reduction.
- RL’s complete citation proof.
- H/HW, BC, K0, OR and M0; S1′/A1′ and KB.
- GR and WAS.
- The deletion/parity/membership arguments of DR, DR-Res and DR′, relative to their quoted upstream imports.

## HYPOTHESIS-MATCHED ONLY:

- R2, BR, FW+ and KBH as already reviewed theorem imports; no renewed full-proof certification is asserted here.
- Accepted Theorems M and P and their transitive MIX_low proof packet.
- Assumed NMH-iii: its complete word-class scope was matched; its GC/seed proof was not re-reviewed.
- The external gap-bound Theorem P, Davenport-alpha, Doubling and EGZ used by the foundational reductions; their upstream proofs were not audited here.

Conditional on **(GC)**, the accepted **M/P** chain, and the foundational imports just identified, I endorse **NMH, MIX_DEF_HIGH, MIX_DEF, RUNS, INV_Res**, the normalized inherited-avoider conclusion **\(B=\kappa=0\)**, and solvability of every word in **RGR\(_{4p-1}(p)\)**. Both halves of INV* remain open in this argument; unrestricted ordered Olson does not follow.

This is a correctness assessment of the conditional RGR assembly. Its significance must be distinguished from the unrestricted ordered-Olson problem, which still needs INV*. No novelty search was performed, and no firstness claim is endorsed.