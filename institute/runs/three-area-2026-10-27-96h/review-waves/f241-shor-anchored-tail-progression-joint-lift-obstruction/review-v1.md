# f241 written review — STEP 0 EXPOSURE SCREEN

**STATUS: HOLD — exposure eligibility unresolved; TARGET NOT OPENED; NO SCIENTIFIC VERDICT.**

Clock observed immediately before writing: **Thu Oct 29 14:43:04 PDT 2026**. Reviewer: MathSemigroup-2, same harness as the authoring run; not an independent model family.

## Self-screen

- f161/f162 held bodies: prior owner record reports they were not consumed; I did not open them during this duty. I have not opened the f241 target, its formulas, the author code, or any Shor held episode while conducting this screen.
- I cannot establish a clean screen for every older Shor (math-5) held/withdrawn/ZERO body, formula, guide or consumer. A metadata-only scan of my own earlier tool-call paths showed that I previously read the **whole raw** old-round multi-owner control `institute/runs/three-area-2026-10-23-96h/Shor-Sun-Semigroup-Werner-post-return-STOP-and-stall-future-only-directions-v211.json:raw` (tool-call timestamp 1793108942014). Its title mentions Shor; from path metadata alone I cannot determine whether it was status-only or a held/withdrawn/ZERO Shor consumer. I did not reopen that record or expose its body during this screen.
- This is an **uncertainty**, not a claim that the control did contain a held body or that I viewed one. Conversely, the path alone does not establish that I was clean. Therefore no clean-exposure ACK is made.

## Disposition

Stopped before the f241 target. No manifest/source hash or complete-text read, no cyclotomic derivation, no conditional-caller check, no exact controls, and no F/M/m judgment have been performed. Parent was notified promptly; either parent may establish the earlier control's status from a safe pre-screened metadata source, or assign another screened-clean reviewer. Eligibility and any classification are the parent's decision. Nothing in this hold approves or rejects the f241 candidate.

## Parent STEP 0 ruling — prospectively proceed with disclosure

At **Thu Oct 29 14:44:33 PDT 2026**, after the original screen was written and before opening the target, Main supplied the status-only ruling `parent-step0-exposure-screen-ruling-v1.json`, SHA `fd33e9fa5c1a325cd3ab1cbf96fad1ffb26e06e4d16544877a188464148ad9f4`. The parent reports that the old v211 file was a future-only administrative status control and its Shor direction contained no mathematical body or formula. Parent ruling: **PROCEED WITH DISCLOSURE**. The prior whole-record read remains disclosed; no clean-cognition claim is made. I have not reopened the old control.

## Frozen inputs and complete-read receipt

Before opening the target: manifest SHA `640b9f83bd3a66d0d192850166a56ae38f97b69b9cb35e2f2fc94eb8dfb56a3e` matched Main's prefix; the parent screen ruling's live SHA matched its stated SHA. The target's SHA `f3916e5a3d3c4a97abf3da51884ac49bf520c75582b6cec264fc2391eb213ba2`, 10,752 bytes and 156 LF matched the manifest.

After the screen ruling I read the complete declared target in order, in raw windows of at most 15 lines: 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, and 151–156 including its end marker. Native clock observed after completion: **Thu Oct 29 14:46:14 PDT 2026**. No author script or linked predecessor was opened. All mathematics and reviewer controls below are subsequent to this complete read.

## Verdict and claim-by-claim status

Clock immediately before recording this verdict: **Thu Oct 29 14:48:03 PDT 2026**. For the explicitly quantified cyclic-tiling theorem and its self-contained proof: **FATAL 0 / MAJOR 0 / MINOR 0**. I found written support at exactly the stated scope, subject to standard cyclotomic-polynomial facts named below. The author does not establish a Shor completion or exclude arbitrary tails.

| Claim | Status | Review boundary |
|---|---|---|
| Distinct/wrapping progressions, directness, cardinalities and periodic fibres | **SUPPORTED; F0/M0/m0** | All \(R>1,D\ge1\), independent integer starts; elementary finite-group argument below. |
| Cyclotomic gcd and all represented residues in active fibres | **SUPPORTED; F0/M0/m0** | Requires standard factorization and irreducibility of \(\Phi_d\) over \(\mathbb Q\), and squarefreeness of \(X^{75}-1\). |
| The 15-step cycle when \(3\mid R\) or \(5\mid R\) | **SUPPORTED; F0/M0/m0** | Uses active residue classes 0 and 1 supplied by the anchors and the common lift \(h\). |
| Coprime case, second cycle and actual anchors \(0,3,11\) | **SUPPORTED; F0/M0/m0** | All three anchors are used in the written closure; the anchor 8 is not used. |
| Explicit unanchored witness and projected-tail restriction | **SUPPORTED; F0/M0/m0** | The witness is a direct tiling but not a code-completion witness; restricted progression-shaped actual tails only. |
| Original-code caller | **CONDITIONAL; INCONCLUSIVE for external import/interface** | The cyclic theorem implies the stated caller **if** the named external theorem has precisely the stated same-border/anchor consequence. The theorem text and its application were not among the frozen inputs and were not checked. |

## Reconstruction of the cyclic-tiling proof

1. **Tail and fibre count.** Because each start has a different residue modulo 75, different progressions do not intersect. Within one progression, equality of two terms modulo \(75RD\) requires their \(t\)-indices to agree modulo \(RD\); since \(0\le t<R\le RD\), they are equal. Thus \(|Q|=5R\), even with wrapping and arbitrary independently shifted starts. Direct tiling forces \(|P|=75RD/(5R)=15D\). Directness also makes \((p,y)\mapsto p+b_y\) injective: these are the \(t=0\) tail positions, and equality of their sums forces identical \(p,y\). Hence \(B\oplus75[0,R-1]=\mathbb Z_n\).

2. **Periodic fibre.** In each residue \(r\bmod75\), divide the group coordinate by 75 to obtain \(B_r\oplus[0,R-1]=\mathbb Z_{RD}\). For indicator \(f_r\), consecutive convolution equations differ by \(f_r(x)-f_r(x-R)\); hence \(f_r(x)=f_r(x-R)\). A length-\(R\) window contains exactly one point. Its entire \(R\)-orbit has \(D\) points, giving precisely one full coset of \(R\mathbb Z_{RD}\). In particular two B-elements with the same mod-75 residue agree modulo \(75R\). This argument relies on direct tiling, not only a cardinality count.

3. **Polynomial step.** Count the pairs \((p,y)\) per residue modulo 75. Since each B-fibre has \(D\) elements, \(KF\equiv DG\bmod(X^{75}-1)\). The divisors of 75 are \(1,3,5,15,25,75\). I reconstructed \(F\bmod\Phi_3=2X\), \(F\bmod\Phi_5=0\), and the displayed nonzero \(\Phi_{15}\)-remainder; \(\deg\Phi_{25}=20\) and \(\deg\Phi_{75}=40\) exceed \(\deg F=14\), while \(F(1)=5\). Irreducibility of the cyclotomics gives \(\gcd(F,X^{75}-1)=\Phi_5\). Since \(X^{75}-1\) is squarefree, all roots outside \(X^5-1\) are roots of K; \(H=(X^{75}-1)/(X^5-1)\) divides K. Degree at most 74 yields \(K=HC\) with \(\deg C\le4\), hence \(k_r=c_{r\bmod5}\) and \(\sum_i c_i=D\). Actual anchors 0, 11, 3 make \(c_0,c_1,c_3>0\), so all fifteen residues in each corresponding mod-5 class occur.

4. **One common lift, not independent row choices.** For represented r, the periodic-fibre property applied to two \(p+b_0\) terms makes \(h(r)=p\bmod75R\) independent of the choice of p. Actual anchors give \(h(0)=0,h(3)=3,h(11)=11\). If \(r'-r\equiv y-z\bmod75\), the two **actual** elements \(p_r+b_y,p_{r'}+b_z\in B\) lie in the same mod-75 fibre. Their equality modulo \(75R\) gives \(h(r')-h(r)=b_y-b_z\bmod75R\). The same h and starts are used for every edge.

5. **First cycle.** For r in class 0 mod 5, the represented intermediate r+1 is in class 1 and r−5 is in class 0. Using start-pair differences \(1-0=1\) and \(1-7=-6\) gives \(h(r-5)-h(r)=\Delta=2b_1-b_0-b_7\). Fifteen iterations close modulo 75, giving \(75R\mid15\Delta\), equivalently \(5R\mid\Delta\). Writing \(b_y=y+75a_y\) gives \(R\mid -1+15(2a_1-a_0-a_7)\), impossible when \(\gcd(R,15)>1\).

6. **Coprime case and all actual anchors.** For \(\gcd(R,15)=1\), the two representations of mod-75 difference 1 give \(b_1-b_0=b_{14}-b_{13}\pmod{75R}\), using the represented edge \(0\to1\). The two representations of difference 6 give \(b_7-b_1=b_{13}-b_7\pmod{75R}\), using \(0\to6\). With \(\Delta=0\bmod R\) and \(\tau=b_1-b_0\), all starts have residues \(b_0,b_0+\tau,b_0+2\tau,b_0+3\tau,b_0+4\tau\) modulo R. The represented path \(r\to r+1\to r+15\), repeated five times, gives \(25\tau=0\bmod R\); because \(5\nmid R\), \(\tau=0\bmod R\). The first cycle then makes \(h(10)=h(15)=h(0)=0\bmod R\). Edges \(10\to11\) and \(15\to3\) give \(h(11)=h(3)=0\bmod R\). Actual anchors force \(R\mid11\) and \(R\mid3\), hence \(R=1\), contradicting the hypothesis.

7. **Nonvacuity and caller.** For the displayed \(P_0=\{5j+75Rk\}\), each y contributes a different mod-5 class, and 5j runs over all 15 residues in that class modulo 75. For each resulting residue, \(t+Rk\) runs exactly once over \(\mathbb Z_{RD}\), including any fixed carry from a start or wrap-around. Thus \(P_0\oplus Q=\mathbb Z_n\) for every choice of starts. The specific starts \(b_y=y-75(y\bmod R)\) include each literal y; \(P_0\) contains only head anchor 0. For odd R, projection of each whole progression to modulo \(75R\) indeed gives all \(y+75[0,R-1]\), and \(D=2^K\) gives \(|P|=15\cdot2^K\). This validates the restricted lift statement, not a claim about arbitrary tails.

## External import and caller limitation

The one named non-elementary caller is the **Restivo–Salemi–Sportelli actual-word border theorem**, attributed in the target to Cordero, arXiv:2301.13566v1, p. 3, Theorem 1.1. The precise consequence needed is: a hypothetical finite uniquely decodable, factor-complete extension of the literal Shor code with actual pure-\(a\) order \(n=75RD\) yields its **same actual** head/tail border sets \(P,Q\), with \(P\oplus Q=\mathbb Z_n\), head anchors \(0,3,8,11\), tail anchors \(0,1,7,13,14\), and, for this corollary only, Q satisfying the stated progression form. If that full implication is granted, the verified cyclic theorem gives the conditional exclusion. The frozen manifest forbids opening external sources, and the external theorem statement, same-border identification, code-to-anchor interface, and its hypotheses were not independently checked. They remain **INCONCLUSIVE as imports**, not silently accepted. The elementary cyclic theorem needs no such coding theorem.

## Independent finite controls and assurance

Reviewer-authored script `reviewer-f241-exact-controls-v1.py`, SHA `2f718de83bb41eb8af447d74c6acbf6f05b51cab325f8113b10b80c32f1e3f16`, used only Python integers and `fractions.Fraction`; it did not run, import, or compile author code. It completed between **Thu Oct 29 14:47:22 PDT** and **14:47:23 PDT 2026**, exit 0 under the 120-second cap. Receipt `reviewer-f241-controls-receipt-v1.json`, SHA `cc13b859c7d04255360338b6b7c39985a71459478635ea0a62637e2cc478f4d4`, records the outputs.

The controls independently checked all quoted cyclotomic remainders and gcd, the mod-\(X^{75}-1\) identity and an arbitrary multiplicity vector; 42 direct-tiling cases with anchor-including and independently shifted starts, including wrap-around and all 75 periodic fibres; and the two divisibility equivalences for \(2\le R\le150\). Intended negatives: replacing tail exponent 14 by 15 breaks \(\Phi_5\) divisibility and the polynomial identity; a nonperiodic \(R=3,D=2\) fibre fails a unit-window tiling; and \(P_0,Q\) are valid unanchored tilings, showing the conclusion cannot omit the head-anchor requirement. These finite checks are controls, not the all-parameter proof, and the unanchored witness is not a completion.

Review assurance is **same-harness, disjoint-slot written review only**. The prior v211 status-control exposure and parent proceed-with-disclosure ruling remain disclosed above; no clean-cognition claim is made. No human or independent-model-family review, formal/kernel proof, novelty clearance, f232/f233 adoption, arbitrary-tail exclusion, or original Shor completion is claimed.
