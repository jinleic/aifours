DISPOSITION: ACCEPT-WITH-FIXES

- **MINOR — `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r1.md:72`: stale open-status statement.** Correct statement: “The assembly alone leaves R4 unresolved; the subsequent Lemma R4 in `proof-R4-closure.md` excludes avoider data in R4 and completes MIX_low(p) and PAR(p) for every prime \(p\ge5\).” This is a status inconsistency, not a gap in Theorems M or P.

- **MINOR — `inverse-parity/mixdef-low/c2/proof-Rstar-r3.md:178`: realizability is conflated with avoidance.** Physical normalized data are realizable as an RGR word: put \(u_t=d_t-\phi_t\pmod p\); their sum is zero modulo \(p\), so reflection values can be reconstructed. Correct statement: “Membership does not establish that the resulting RGR word is an avoider, or provide an ordered-product counterexample.”

- **MINOR — `inverse-parity/mixdef-low/c2/README.md:99`: the historical ‘Theorem PF’ entry lacks the later qualification.** Correct statement: “This superseded finite claim was conditional on unreviewed census code; the current assembly labels it Statement PF [W+F, conditional].” The universal written proof subsequently supplies these prime cases independently.

No FATAL or MAJOR mathematical finding.

All four target SHA-256 values match the manifest exactly. I also recomputed every other manifest hash: all match. All file reads stayed within the pinned directory. No claimant code was imported, executed, or compiled; no writes, network, solvers, or delegation were used.

Below, T1–T4 denote the targets in the question.

**1. Completeness and exact chain**

From the stated reviewed imports, the written proofs of MIX_low(p) and PAR(p) are complete for every prime \(p\ge5\).

First take a hypothetical MIX_low avoider. If \(A\ge2p\), select \(\rho_1^{2p}\). Otherwise apply M0 repeatedly. If \(B\) becomes zero, use S1′, A1′, or the trivial cut according to the remaining rotation length. Otherwise obtain normalized MIX_low data and apply Lemma S.

The remaining elimination order is:

| Remaining case | Elimination |
|---|---|
| Outside R*: \(\Phi(Z_0)\ge2g+2\) or \(|Y_{\rm al}|+a_Z\ge3\) | MIX-R |
| \(B\ge g+1\) | W |
| Some \(d_t\ge2p-B\) | B1 |
| In R*, some \(bh_t\ge B+1\) | A |
| After these restrictions, \(g=1\) | G1 |
| Every run cheap | AC |
| Otherwise \(2X+\alpha\le2g+s+S_Z-1\) | KS |
| In R***, \(c(Z_0^+)\ge g+1\) | ZP |
| In R***, some \(bh_t\ge s+1\) | C |
| The residual R4 | R4 |

After A and B1, Fact F(d) supplies \(d_t\le2g+B-2\), hence \(\phi_t\le g-1\). This also supplies C’s exceptional-run bound, as checked below.

Every branch produces an identity \(2p\)-subword, contradicting the hypothetical avoider. This proves M. The PAR assembly in item 6 then proves P. I found no mathematical gap in this chain.

**2. M0, independently**

For every pattern \(P\), deleting one rotation of each sign decreases **both** \(E^+(P)\) and \(E^-(P)\) by exactly one, irrespective of whether the modified run belongs to \(P\).

Inserting two identical reflections increases \(h(P)\) by exactly one:
\[
\left\lfloor\frac{l_j+2-f_j}{2}\right\rfloor
=
\left\lfloor\frac{l_j-f_j}{2}\right\rfloor+1.
\]
The boundary pattern, \(m(P)\), and \(\beta(P)\) remain unchanged. This includes \(P=\varnothing,[k]\).

Consequently,
\[
g'_P(E-1)
=\min\!\left(p-m,\ E+m+h-p,\ \left\lfloor\frac{E-1}{2}\right\rfloor\right)
\le g_P(E).
\]
The first two terms are unchanged; the third cannot increase. Therefore the new integer window is contained in the old one. Taking residues preserves containment. Empty windows remain empty; full residue windows cause no exception to the implication.

The restriction \(r_t\ge3\) ensures that the modified rotation run remains nonempty. No run disappears or merges; \(F'=F+2\ge1\) and \(R'=R-2\ge1\).

The bookkeeping is correct:
\[
(A',B',R',H',\kappa')=(A-1,B-1,R-2,H+1,\kappa-1).
\]
The quantities \(k,d_t\), both kinds of run parity, and reflection values \(y_j\) are unchanged. Thus the **modular** half-jumps of HW, \(\theta_t/2\), are unchanged. This does not assert invariance of T2’s integer \(\phi_t=d_t-x_t\).

Iteration terminates because \(B\) decreases. Each terminal rotation run is pure or a \((1,1)\)-pair. No inherited inequality is required.

At its MIX_low uses:

- \(k\le p\) and odd reflection runs persist.
- \(A-B\) and \(g=\kappa-B\ge1\) persist.
- \(A'\ge B'\), \(A'\le2p-1\), and \(\kappa'\le k-1\) persist.
- If \(B'>0\), then \(B'<\kappa'\), giving every normalized MIX_low hypothesis.
- If \(B'=0\), all rotations are \(\rho_1\), \(\kappa'=g\ge1\), and
  \[
  R'=2p-k+2g.
  \]
  S1′ applies for \(R'\le2p-2\), A1′ for \(R'=2p-1\), and the trivial cut for \(R'\ge2p\).

Neither \((P)\) nor \((D0)\) is silently reused after M0.

**3. ZP, C, and the R4 consequences**

ZP supplies every KL hypothesis:

- \(c(Z_0^+)\ge g+1\) makes \(Z_0^+\) nonempty.
- \(Y\ne\varnothing\), since \(\sum bh=k-2g=B+s+1>0\); therefore \(Z_0^+\) is proper.
- Free runs are cheap, hence \(\phi_t\le g-1\).
- \(BH(Z_0^+)\le0\le B\).

For C, \(k\ge2g+B+1\ge4\), so \([k]\setminus\{t_0\}\) is a proper nonempty cyclic interval with \(m=1\). Its displayed \(c\) and \(BH\) bounds are correct. Wherever C is used inside R**,
\[
\phi_{t_0}\le g-1\le p-k+g,
\]
using \(k\le p\). Thus its exceptional-run hypothesis is available.

All listed R4 consequences are correct:

- \(s\ge1\), because some \(bh_t>0\) while every \(bh_t\le s\).
- \(Z_0^+\ne\varnothing\): otherwise \(X=\alpha=0\), contradicting the R*** inequality.
- Combining \(X+m(Z_0^+)\le g\) with R*** gives
  \[
  \alpha\ge2m(Z_0^+)+s+S_Z.
  \]
- Since \(\alpha\le B\le g\),
  \[
  s\le\alpha-2\le B-2\le g-2.
  \]
- Writing \(|Z_0|=n_d+\alpha+\beta+\pi_0\), the stated bound
  \(\delta\ge2g+s-n_d\) gives
  \[
  exc=|Z_0|+\delta-2g\ge\alpha+\beta+\pi_0+s.
  \]
- Substitution into R1 gives
  \[
  \text{anti mass in }Z_0\ge s+S_Z+2m(Z_0).
  \]

T1 uses nonemptiness, the \(X,\alpha,s\) bounds, and the resulting \(\delta^+\) estimate. The final \(exc\) and anti-mass inequalities are not used in its closure argument.

**4. R4, line by line**

Facts (i)–(iii) are justified by R**, Fact F(c), and the preceding consequences.

For fact (iv), every aligned run in \(Z_0\) is free and has integer \(\phi_t\ge1\). Other free runs have nonnegative \(\phi_t\). Hence
\[
n_d\le X\le g-1.
\]
The exact accounting is
\[
\delta^+=2X-S_Z-n_d+\text{free anti mass}.
\]
Free anti mass is at least \(\alpha\), so R*** gives
\[
\delta^+\ge2g+s-n_d\ge g+s+1.
\]
Also \(\delta\ge\delta^+\), because the remaining \(Z_0\)-runs have nonpositive \(bh\).

Step 1 is valid. \(Y\) is a proper subset of the cycle, so its cyclic components are paths. Taking one alternating class from each component produces an independent union in the **cycle**. Component ends, wrap-around, and paths of one or two vertices create no missing edge. Actual R4 parameters already force \(k\ge11\).

Moreover,
\[
BH(Y)=s+1+B+\delta\ge2s+3.
\]
Thus the heavier classes satisfy \(BH(Q)>s+1\). Greedily adding weights in \([1,s]\) gives
\[
s+1\le BH(N)\le2s,\qquad |N|\ge2.
\]

In branch 2(a), independence gives
\[
m([k]\setminus N)=|N|.
\]
The complement is proper and nonempty, and
\[
c([k]\setminus N)\ge g+1,\qquad BH([k]\setminus N)\le B.
\]
Its individual \(\phi\)-bounds come from fact (i). KL applies.

In branch 2(b), integrality gives
\[
\phi(N)\ge p-k+g+|N|\ge g+2.
\]
For \(S=Z_0^+\cup N\),
\[
BH(S)\le-(g+s+1)+2s=s-g-1\le-3.
\]
The last inequality **does use** \(s\le g-2\), already established in T2. Since \(BH([k])=B+s+1>0\), \(S\) is proper; it is nonempty because \(N\ne\varnothing\). Therefore \(m(S)\ge1\), and
\[
c(S)\ge X+\phi(N)+1\ge g+3.
\]
Again every KL hypothesis holds.

I found no configuration satisfying the applicable arithmetic hypotheses where either construction fails.

**5. Coverage, definitions, and direction of implication**

The eliminations cover every normalized MIX_low avoider. The definitions of R*, R**, R***, R4 and all quantities named in the question agree across the targets and r2 import. In particular, the evenness of \(\Phi\) makes r2’s residual condition equivalent to T2’s R1.

I regenerated the parent diff using LF splitting and obtained an exact match. Sec. 1–6 changes consist of the listed fixes and specified additions; no additional reviewed statement was changed.

Every kill is used in the correct direction: **actual avoider ⇒ lift data ⇒ identity subword ⇒ contradiction**. Neither M nor P requires proving that the relaxed interval-feasible R4 system is empty.

**6. PAR assembly and hypothesis matching**

Normalize \(A\ge B\) by the stated automorphism. Avoidance gives \(A,B\le2p-1\) and \(B\le\kappa\). The inherited conditions give
\[
\kappa\ge0\quad\text{(Pairs)},\qquad
\kappa\le o_F-1\quad\text{(V)},\qquad o_F\le k\le p.
\]

The cases are exhaustive:

- **\(\kappa=0\), some even run:** K0 applies. Its required \((P),(V),k\le p\) hold.
- **\(\kappa=1\):** \(B=0\) or \(1\). K1 and K1′ apply respectively; K1′ receives \((D0)\) from the original inherited word.
- **\(\kappa\ge2,B=0\):** OR gives odd reflection runs and all rotations \(\rho_1\); S1′/A1′/the trivial cut apply by rotation length.
- **\(B=\kappa\ge1\):** KB receives \((V)\), \(o_F\le p\), and original-word \((D0)\) in its capped case.
- **\(1\le B<\kappa\):** OR preserves \(A,B,H,\kappa\), produces odd reflection runs, and gives
  \[
  k(\widetilde w)=o_F\le p,\qquad \kappa\le o_F-1.
  \]
  These are exactly the MIX_low hypotheses.

OR need not preserve \((P)\) or \((D0)\): the subsequent mixed-case theorem does not require them. The exceptional uses of \((D0)\) in K1′ and KB concern the original word. Condition \((E)\) is not needed by this assembly.

Thus K+ eliminates every parity in its range, while K0 eliminates the remaining parity violators. This proves the stated PAR(p).

**7. Census dependence**

For the audited targets, the output-dependent assertions are:

| Location | Assertions dependent on census/replay output |
|---|---|
| T1:60–62 | p=11 configuration/applicability counts, prefix success, C never applicable, and observed census emptiness of R4 |
| T1:63–67 | Synthetic success and mutation-rejection counts |
| T1:68–69 | Earlier synthetic success and mutation counts |
| T2:216–217 | Configuration counts, R* counts, and reported finite emptiness |
| T2:218–230 | p=17 census completeness/counts, classifications, replay success, and consequent finite emptiness |
| T2:231–236 | Construction replay statistics and mutation results |
| T2:237–241 | Relaxed-search counts, observed emptiness, and stopped-search status |
| T2:242–246 | Cross-check sample counts and zero mismatches |
| T3:21–22, 45–51 | PF’s finite conclusions and supporting census/replay assertions |
| T3:52–53, 68 | Reported sampled cross-check provenance/results |

The pruning inequalities explained in T2 are mathematical arguments; correspondence to the implemented census and completeness of its execution remain code-dependent.

M, P, PA, P5, and M0 depend on none of these outputs. Current PF statements and their T2 reference explicitly say conditional. The historical README exception is the third MINOR finding.

**8. Claims and status**

P5 follows from written arguments: at \(p=5\), \(g=1\), \(B\in\{1,2\}\); W handles \(B=2\), and MIX-R/A/B1/Fact F/G1 handle \(B=1\), with normalization supplied by the assembly.

T1’s scope is correct. PAR plus RUNS would give INV_Res and the RGR length-\(4p-1\) conclusion through DR-Res. Extending to all dihedral words additionally requires INV*. The packet does not establish RUNS, unrestricted INV, INV*, or ordered Olson for all primes.

The “unreviewed” labels correctly describe status at freezing. The earlier open-status text should now be qualified as historical.

**9. Independent finite checks**

All checks used my own in-memory, single-threaded `python3 -B -c` code. Successful test processes peaked below 13 MiB RSS and used under three CPU seconds each. An initial virtual-address-limit setup attempt exited before testing.

For M0, seed `2026101701`, random compositions and rotation signs, \(k\le8\):

| \(p\) | M0 steps | Pattern comparisons | Raw ordered-product DP checks |
|---:|---:|---:|---:|
| 5 | 1,000 | 11,336 | 200 |
| 7 | 1,000 | 30,450 | 200 |
| 11 | 1,000 | 46,796 | 200 |

Every endpoint and residue-containment check passed, including empty/full **patterns**. The samples contained 60,922 full residue windows and no empty integer windows. Another 100 complete normalizations per prime reached the stated terminal forms.

No original M0-applicable avoider was sampled. One resulting \(p=5\) word was an avoider; an additional raw DP replay confirmed it. Three known critical avoiders, one per prime, also passed independent HW/DP negative controls. Preservation on an originally avoiding, M0-applicable sample: **NOT RUN—none found**.

For R4, seed `2026101702`:

- 10,500 structured random arithmetic instances at \(p=17,23,31,47,61,79,101\), including pairs and nonfree antis.
- 4,000 targeted instances at \(p=23,31,47,61\).
- Combined: **14,418 branch-(a) and 82 branch-(b) constructions**, all satisfying KL and the direct integer window test.
- 8,166 proper cycle subsets at \(2\le k\le12\) checked path splitting, independence, half-weight, and complement block counts, including 77 singleton-\(Z_0\) cases.
- Two mutation controls detected the expected failures: removing \(bh\le s\) allowed \(|N|=1\); removing \(\phi\le g-1\) left the constructed set violating KL’s individual bound.

The request that *every* hypothesis be necessary is stronger than true: for example, branch (b) only needs
\[
\delta^+\ge2s-B
\]
for its BH budget; then \(BH(S)\le B<BH([k])\) also proves properness. The stronger bound in T1 is valid but not necessary. Other individual hypothesis-deletion mutations: **NOT RUN**.

The final exhaustive normalized HW checks were:

| \(p\) | Labelled run vectors | Zero-sum residue assignments covered¹ | Interval-feasible labelled assignments | HW avoiders |
|---:|---:|---:|---:|---:|
| 5 | 1,601 | 902,625 | 0 | 0 |
| 7 | 298,965 | 30,653,653,779 | 104 | 0 |

¹ Coverage uses full-window and singleton exclusions; these assignments were not all individually iterated. After singleton exclusions, 0 and 1,763 assignments respectively required further testing.

The 104 interval-feasible \(p=7\) assignments form 15 rotation classes. **All 104 were realized as actual words and replayed by raw ordered-product DP; every replay found an identity subword.** Odd reflection-length distributions were collapsed using HW’s dependence on \(H\). Cases \(A\ge2p\) were discharged analytically.

These finite checks support the audit; the universal conclusions rest on the written arguments.

### Established

M0, ZP, C, the R4 consequences and R4 are correct in their stated scopes. From the reviewed imports, MIX_low(p), PAR(p), PA and P5 follow as claimed.

### Open

General RUNS(p), unrestricted INV and INV*. Emptiness of the relaxed R4 system is neither established nor needed.

### UNKNOWN

Claimant census/replay code fidelity and the reported larger-prime census counts. Exhaustive MIX_low checks for \(p\ge11\): **NOT RUN**.