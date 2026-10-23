**DISPOSITION: ACCEPT-WITH-FIXES.** Audit date: **2026-10-18**.

| Theorem | Verdict | Exact scope supported |
|---|---|---|
| **K0\*** | **ACCEPT-WITH-FIXES** | Reflection-run constancy for rigid-rotation avoiders with \(\kappa=0\). |
| **RED** | **ACCEPT-WITH-FIXES**, conditional on (I1)–(I4) | Reduction of conditional REFL to nonexistence of residual avoiders in \(\mathrm{RES}_{<}(p)\) with \(\kappa\ge2\). |

**FATAL: 0. MAJOR: 0. MINOR: 5**, detailed below. One displayed FUS inclusion is literally false; its correction is local, and the corrected statement supports every subsequent application.

All **13 snapshot SHA-256 hashes match** the supplied pins. Only static snapshot reads and hashes were used. No interpreter, scientific computation, writes, network, delegation, or finite-result premise was used.

References below use the supplied source numbers: **00** is `00-proof-K0star-r1.md`; **01** is `01-proof-RED-r1.md`. Line references are 1-based LF lines.

**Required corrections**

1. **MINOR — incorrect reversed FUS formula.**  
   [00:78–83](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-reduction-review-v1/snapshot/00-proof-K0star-r1.md:78).

   The second inclusion must read
   \[
   \operatorname{Spec}(\sigma_u^{\,l'+l})
   \subseteq
   \operatorname{Spec}(\sigma_v^{\,l'}\sigma_u^l),
   \qquad l'\text{ even},
   \]
   with **\(u\)** on the left.

   The printed version fails for \(l=1,l'=2,u\ne v\): its required size-three product is \(\sigma_v\), whereas the source’s only size-three selection has product
   \(\sigma_v^2\sigma_u=\sigma_u\).

   The correction follows directly by taking the same counts as in the first-form proof, with the even number of \(\sigma_v\) letters selected first. Thus recolouring the **even** block to its neighbour’s value is valid in either orientation. That is the operation subsequently used. I classify this as minor because the intended operation is explicit at 00:84 and its repair requires no new hypothesis or unresolved argument.

2. **MINOR — PM0 omits \(k\ge2\).**  
   [00:97–103](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-reduction-review-v1/snapshot/00-proof-K0star-r1.md:97).

   Add **“Let \(k\ge2\)”**. At \(k=1\), \(R_j=R_{j+1}\) and \(S_j=S_{j+1}\), so the stated deletion/merger is not defined as intended. The actual imported PM* explicitly has this hypothesis at **09:31**.

   Every application in K0* and RED satisfies it. Import acceptance does not cover the malformed \(k=1\) statement.

3. **MINOR — the all-reflection constant-word exception needs exclusion from the maximal-decomposition bookkeeping.**  
   [00:15–20](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-reduction-review-v1/snapshot/00-proof-K0star-r1.md:15), also 00:84–87.

   For \(R=0,k=1\), the sole run is empty but \(\theta_1=0\). Thus “every maximal empty run is genuine” and “RGR iff \(g=0\)” are not literally valid throughout the stated \(R\ge0\) domain.

   Restrict those maximal-decomposition assertions and fusion bookkeeping to **\(R\ge1\)**, treating \(R=0\) separately by AR. Keep GR0/H0 valid for arbitrary representations. Both main proofs already eliminate \(R=0\) before using this bookkeeping.

4. **MINOR — SING’s cardinality needs truncation at zero.**  
   [01:36–44](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-reduction-review-v1/snapshot/01-proof-RED-r1.md:36).

   Put \(q=\kappa-B+\beta_t\). The number of remaining nonzero residues is
   \[
   \boxed{\max(0,q-1)},
   \]
   rather than \(q-1\) without qualification. At \(q=0\), the allowed set is empty, not a set of cardinality \(-1\).

   The consequential statements—solvability for \(q\le1\), and \(u_t=-1\) for \(q=2\)—are correct. CAP uses the former correctly.

5. **MINOR — F3 needs its full domain and empty/full-pattern qualification.**  
   [01:178–181](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-reflection-reduction-review-v1/snapshot/01-proof-RED-r1.md:178).

   Besides the supplied author correction **\(H\ge1\)**, the construction produces an RGR word only when **\(g=1\)**.

   There is another endpoint issue. For a hypothetical residual avoider with \(H\ge1\) and \(A=2p-1\), filling the gap raises \(A\) to \(2p\). The empty-pattern intervals change from
   \[
   I_\varnothing(w)=[1-p,\ B-\kappa-1]
   \quad\text{to}\quad
   I_\varnothing(w^\circ)=[-p,\ B-\kappa-1].
   \]
   The newly admitted \(-p\equiv0\) already certifies solvability: \(w^\circ\) contains \(2p\) copies of \(\rho_1\).

   Consequently, (I1) does **not force a proper-pattern boundary witness** in this branch. Either restrict that conclusion to \(A\le2p-2\), or explicitly include the empty/full certificate. If “patterns” here intentionally includes the full pattern, specify the \(m=0\) convention and acknowledge that its witness can simply be \(u_{[k]}=p\equiv0\). This issue is non-load-bearing for RED.

**Q1 — GR0/H0: accepted after independent algebraic checking.**

At **00:34–59**, the group-law sign is correct. With the literal product formula normalized by \(z_1=+1\),
\[
\sum_{f_i=1}z_i y_i
=\frac12\sum_i z_i(y_i-y_{i-1})
=-\tau(z),
\]
so the product coordinate is \(t-\tau(z)\). Global sign reversal preserves the identity condition.

Here is the elimination underlying the new H0 algebra. Write \(t=2h\), \(C=2c'\), \(q=p-c'\), and \(c=C_{\max}/2\). Feasibility is exactly
\[
\max(p-c,h,-h)
\le q\le
\min(p-\Phi/2,E_+-h,E_-+h).
\]
Eliminating \(q\) gives precisely the displayed half-window bounds. For proper \(P\),
\[
c=H+m-\beta,\qquad E_+=D_P+B,
\]
which yields the stated \(\lambda(P)\). Empty and full patterns give \(I(\varnothing)\) and its negative.

This remains exact for empty runs, arbitrary rotation order, negative endpoints, empty intervals, \(k=1\), and arbitrary lengths. No \(r_i\ge1\) or \(N=4p-2\) assumption enters this algebra.

The accepted **GRX/PM*** overlay is legitimate import acceptance at its stated scope (**12:7–8, 29–30**). It does not itself accept the new H0 derivation; that derivation was checked above.

**Q2 — segment moves: correct with the FUS and PM0 corrections.**

At **00:74–103**:

- **SPEC** is a one-way avoidance transfer. The selection replacement preserves both length and ordered product.
- **FUS** is one-way. Single fusion preserves \(H\); double fusion raises \(H\) exactly when the two outer blocks are odd.
- **SL** gives genuine spectrum equality in both directions. All four product/parity classes and their size maxima are correct, including \(a=3\).
- **TR** gives exact solvability equivalence: each moved balanced pair contributes one available rotation of each effective sign in every zone.
- **PM0** is one-way. Its patterns are exactly the old patterns constant across the merged runs. Boundary parity, telescoped \(u_P\), and the empty-pattern condition agree.

Arbitrary order inside a rotation run causes no additional obstruction: those letters commute and have one zone sign. Representation-based arguments remain valid when the representation is nonmaximal; maximal \(H,\kappa,k,g\) must then be recomputed. The later proofs make this distinction correctly.

Wrapping segments are handled by choosing a cyclic frame and returning identity selections by conjugation.

**Q3 — BC′ and CH: accepted.**

At **00:107–128**, the boost introduces only the residue \(0\), or leaves the interval empty. Its boost condition excludes that residue. This remains valid when either lambda is negative.

The representative-selection argument covers both cases:

- \(l+l'\ge1\): the outer interval contains at least \(p\) consecutive integers;
- \(l+l'\le0\): the central interval itself contains at least \(p+1\).

The two induction inclusions follow exactly from BC′(b). The final sum lies in \([p+1,2p-1]\), contradicting divisibility by \(p\). For \(s=2\), the induction conditions are vacuous and the endpoint argument remains valid.

At **00:130–141**, CH correctly handles zero-rotation parts. Every union of at least two parts has positive rotation count. Two deficient complementary unions would force \(R\le4\); hence the upper sum is at least \(R+1\ge p+1\). The lower inequality and final complement condition also hold. The boundary **\(p=5,R=p\)** is covered.

**Q4 — K0*: the last-step classification and all partitions are complete.**

At **00:150–194**, corrected FUS decreases \(g\). An odd–odd double fusion would produce \(\kappa=-1\), contradicting Pairs.

If the fusion process stopped with an empty run, all remaining even blocks could be removed by PM0 across nonempty neighbours. This would leave \(e_F=0<e_R\), contradicting P0. Therefore a last fusion exists and removes either one gap or the two gaps of the stated double-fusion configuration.

After the PM0 normalization,
\[
g\le e_R\le e_F,\qquad e_R\equiv e_F\pmod2.
\]
Also \(k-g\le R\) and \(e_F\ge g\) imply \(o_F\le p\), hence \(R\ge p\).

The case arithmetic is:

| Case | \((e_F,e_R)\) | Number of parts | Zero-rotation parts | \(\sum\lambda'\) |
|---|---:|---:|---:|---:|
| C1a | \((1,1)\) | \(k\) | 1 | \(p+1\) |
| C1b | \((2,2)\) | \(k-1\) | 0 | \(p+1\) |
| C2a, either mirror | \((2,2)\) | \(k-1\) | 1 | \(p+1\) |
| C2b | \((3,3)\) | \(k-2\) | 0 | \(p+1\) |

Every partition has at least two nonempty proper parts. The smallest cases \(k=2,3,3,4\), respectively, and wrapping grouped parts remain valid. Every retained zero-rotation part is a genuine singleton with \(\beta=1\). Thus CH supplies precisely BC′(b),(c), and the displayed sums supply (a).

No RGR classification theorem, RGR-LONG result, or INV* premise is used in K0*.

**Q5 — RED’s new lemmas: load-bearing extensions are valid.**

- **SING, 01:36–44:** endpoint algebra and residue restrictions are correct, subject to the cardinality correction.
- **KB\*, 01:48–65:** the argument genuinely extends to empty runs. Its estimates use \(d_Q\ge-B_Q\), \(D\ge p\), \(B\le k-1\), and disjoint/overlapping pattern sums—not \(r_i\ge1\). All capped and uncapped branches of BC’s inequalities are covered. At \(k=2\), the intermediate conditions are vacuous.
- **CAP, 01:66–69:** the equality chain correctly forces \(A=2p-1\), \(B=\kappa=k-1\), and all positive letters into the capped run. SING with \(\beta=0\) gives the contradiction. **D0 is not used.**
- **KBH\*, 01:70–79:** comparison with **04:39–108** confirms that empty segments do not invalidate the greedy construction. The original nonempty-run counting supplied \(D\ge1\); the new argument supplies \(D\ge0\) and handles the missing boundary correctly. More directly, when \(D=0\), every segment-interval has \(D_Q\le A=B\), so \(\operatorname{lo}(D_Q)=0\). Taking all greedy theta values zero satisfies both bounds. ZS still uses a proper pattern because \(o_F\ge p+1\).
- **K1\*, 01:85–92:** \(g\le e_R\le2\) and \(k-g\le R\) yield \(k\le p+2\), \(R\ge p\). Singleton boosts, parity, the possible zero-rotation union, and all BC′ inequalities are correct.
- **TII, 01:96–102:** this uses KB’s **uncapped** implication at **03:238–273**. It does not apply KB’s capped conclusion without D0. Once a capped segment is necessary, elementary equality and nonemptiness of the actual RGR segments give the type-(II) shape. Nonemptiness is used here only after reaching RGR.
- **QQ, 01:103–120:** both recolourings preserve avoidance and the relevant window data. SING gives \(v-u=2\). The two residues are therefore distinct and differ by \(1\). The stated \(l_1,l_2\) formulas are correct. If \(a'\le p-1\), every listed choice of active minima gives \(l_1+l_2\ge p\); if \(a'\ge p\), then \(a''\le p-1\), and the mirrored pattern gives the same contradiction. All caps, floor parities, and \(\kappa\le p-3\) bounds check out.

Thus these are valid extensions or new arguments, not imports obtained merely by renaming empty runs.

**Q6 — P1–P4 preserve the required properties and exhaust the exits.**

At **01:130–157**, all moves preserve length and the rigid rotation alphabet. Their maximal-decomposition changes are:

| Move | \((\Delta A,\Delta B)\) | \((\Delta H,\Delta\kappa)\) | \((\Delta k,\Delta g)\) |
|---|---:|---:|---:|
| P1, single fusion | \((0,0)\) | \((0,0)\) | \((-1,-1)\) |
| P1, double fusion | \((0,0)\) | \((\delta,-\delta)\) | \((-2,-2)\) |
| P2 | \((0,0)\) | \((0,0)\) | \((-1,0)\) |
| P3 | \((0,0)\) | \((0,0)\) | \((0,-1)\) |
| P4 | \((-1,-1)\) | \((1+\epsilon,-1-\epsilon)\) | \((-\epsilon,1-\epsilon)\) |

Here \(\delta=1\) exactly for an odd–odd double fusion. At P4, \(\epsilon=1\) exactly when the newly adjacent equal-valued blocks fuse.

The **first-applicable priority is essential bookkeeping**: before P3 or P4, neither P1 nor P2 applies, so every block is odd. Consequently the additional P4 fusion really does increase \(H\) by one more. Without that priority, equal values alone would not suffice.

P4’s avoidance argument is valid for the representation with the newly empty run: the first two lambda terms remain unchanged and the floor term decreases or stays fixed; \(I(\varnothing)\) also shrinks. Subsequent maximal fusion changes the representation, not the already-established avoidance. P4 changes \((R,F)\) by \((-2,+2)\); the other moves preserve both.

Pairs bounds \(\kappa\) below, so the lexicographic descent terminates. A hypothetical all-reflection output is excluded by AR. Existing genuine empty boundaries survive P2 and P4; hence only P1 or P3 can reach \(g=0\).

Both exits are excluded:

- **P3:** (I1) forces \(B=\kappa\); TII then contradicts the surviving mixed run.
- **P1:** C1/C2 are exhaustive. The \(\kappa_{\rm end}=0\) branch contradicts (I3). For positive terminal kappa, TII supplies \(A=2p-1\), and all SING hypotheses hold. The C2 residues give the stated \(-2\ne0\) contradiction; C1 is excluded by SING or QQ.

At a terminal state with \(g\ge1\), every block is odd and every rotation run is pure or empty. K0*, Corollary B=K, and K1* eliminate \(\kappa=0\), \(B=\kappa\), and \(\kappa=1\). **No terminal class is lost.**

**Q7 — audit coverage, imports, and unresolved scope.**

Fully audited here: GR0’s specialization and H0 algebra; SPEC, corrected FUS, SL, TR, corrected-domain PM0; BC′ and CH; every K0* case; SING, KB*, CAP, KBH*, K1*, TII, QQ; P1–P4, termination, both exits, terminal completeness, and RED’s converse. The necessary residual relations at **01:161–163** also check.

Imported at their supplied accepted scopes: classical EGZ and the Davenport constant; gap Theorem P and Davenport-alpha; RGR statements (I1)–(I4), including OR and the stated all-positive results. Their application hypotheses were checked. The absent original `proof-RUNS.md` and underlying MIX_DEF proofs were used through the exact accepted statements in sources **10–11**, not claimed as freshly audited. KB’s uncapped argument and KBH’s greedy argument were examined specifically for the new extensions.

No circular REFL/INV* assumption or finite premise was found. The finite aids and censuses were not validated or used.

Subject to the corrections above, the supported equivalence is exactly
\[
\boxed{\text{conditional REFL}(p)
\iff
\text{no avoider in }\mathrm{RES}_{<}(p)\text{ with }\kappa\ge2.}
\]
**Nonexistence of that residual class remains open. Full REFL, INV*, and ordered Olson are not established by these proofs.**