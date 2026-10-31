# Five-node zero certificates require two reversed root-band crossings

**Status: WRITTEN structural obstruction with WRITTEN-checked-in-kernel finite classification; author candidate, not parent adoption.** This sharpens the actual-box five-positive-frequency analysis in `frontier-20261028-five-frequency-single-endpoint-exclusion-v1.md` (SHA-256 `e8aae88916a5275f0cbe4fe057dd6bcc2eea809f6ab1d3f8bb5a897d2db23f2a`). It concerns exact **zero annihilators**, not arbitrary strictly-negative-coordinate atoms.

## Theorem and direct search consequences

Let \(K\) be a compact independent coefficient box of monic strictly Hurwitz septics, with parity-root bands \(E_1,O_1,E_2,O_2,E_3,O_3\) strictly ordered as in the named predecessor. Suppose a positive-weight annihilator of all eight numerator coordinates has **exactly five distinct positive** squared frequencies \(t_1<\cdots<t_5\), plus positive-weight zero and infinity endpoint atoms. Merge atoms at equal frequencies by averaging their actual denominators; denote the resulting actual denominator at \(t_i\) by \(a_i\). Then:

1. For some stable real cubic \(c\), each \(a_i(i\sqrt{t_i})/c(i\sqrt{t_i})\) is real, and its signs alternate **\(-,+,-,+,-\)**.
2. The five samples must contain two disjoint **backward** crossings, one across an odd-part root band and one across a later even-part root band. More precisely, their only possibilities are

| Class sequence | Backward node intervals and bands |
|---|---|
| \((2,1,3,2,4)\) | \([t_1,t_2]\subseteq O_1\), \([t_3,t_4]\subseteq E_2\) |
| \((2,1,3,5,4)\) | \([t_1,t_2]\subseteq O_1\), \([t_4,t_5]\subseteq E_3\) |
| \((2,4,3,5,4)\) | \([t_2,t_3]\subseteq O_2\), \([t_4,t_5]\subseteq E_3\) |

Here \(E_j,O_j\) denote the closed ranges of the corresponding root over **actual** members of \(K\), not arbitrary phase bins. Each contained node interval is nondegenerate. Thus a one-sample-per-root-band frequency grid cannot support such a five-node exact annihilator. Nor can one occur if both \(O_1,O_2\) are singleton bands, or if both \(E_2,E_3\) are singleton bands; in particular fixing either whole parity excludes it. These are genuine necessary restrictions on certificate geometry, not an unrestricted SPR conclusion. For seven positive coefficient widths the bands need not be singletons, so no original eligible case is thereby eliminated merely by fixing a parity.

## Derivation

Let \(H(t)=\prod_{i=1}^5(t-t_i)\), with \(H(0)<0\), and let \(\mu_i>0\) be the merged compactified positive weights converted to the uncompactified pairing. The predecessor's eight exact moment equations and Vandermonde interpolation give real \(\alpha,\beta\), with \(A=-\eta_0H(0)>0\) and \(\eta=\eta_\infty>0\), such that
\[
\mu_iE_{a_i}(t_i)=\frac{\alpha-A/t_i}{H'(t_i)},\qquad
\mu_i t_iO_{a_i}(t_i)=\frac{\beta+\eta t_i}{H'(t_i)}.
\]
Both scalar factors \(f(t)=\alpha-A/t\) and \(g(t)=\beta+\eta t\) are strictly increasing. Assign any zero factor the positive-side sign. Both factors cannot vanish at one sampled node: that would make the actual Hurwitz \(a_i\) have an imaginary-axis root. The signs of \(1/H'(t_i)\) are \(+,-,+,-,+\). Let \(k,l\in\{0,\ldots,5\}\) be the numbers of nodes at which \(f,g\), respectively, are assigned negative sign.

Each actual denominator has strictly increasing unwrapped phase and one of seven sign classes
\[
q=0,1,2,3,4,5,6:\quad (++),(-+),(--),(+-),(++),(-+),(--).
\]
For any samples at \(t_i<t_j\), the globally separated root bands give \(q_i\le q_j+1\); either adjacent class is valid at a parity zero. Exhausting the 36 monotone threshold pairs and these seven classes gives exactly
\[
(k,l;q_1,\ldots,q_5)=(1,3;2,1,3,2,4),\ (1,4;2,1,3,5,4),\ (2,4;2,4,3,5,4).
\]
The executable exact-integer enumeration below checks **all** pairs and **all** compatible class sequences, including root-side choices; removing phase ordering leaves 676 sequences, so the ordering condition is genuinely active. A downward class step \(r+1\to r\) between increasing frequencies forces the intervening interval into the corresponding global root band: the earlier sampled root is at or before the first node, while the later sampled root is at or after the second. This yields the table, even if one endpoint evaluation is zero.

All surviving pairs satisfy \(1\le k<l\le4\) and \(l\ge k+2\). Consequently \(f\) and \(g\) both cross zero, with
\[
0<\frac A\alpha<\frac{-\beta}{\eta},\qquad \alpha>0,\quad\beta<0,\quad\alpha(-\beta)>\eta A.
\]
Therefore \(c(s)=\eta s^3+\alpha s^2-\beta s+A\) is strictly Hurwitz by the cubic Routh criterion. Its parity parts are \(E_c=A-\alpha t=-tf(t)\) and \(O_c=-\beta-\eta t=-g(t)\). The moment equations give
\[
a_i(i\sqrt{t_i})=-\frac{c(i\sqrt{t_i})}{\mu_i t_i H'(t_i)},
\]
including at a zero of one factor, because the other is nonzero. This proves the alternating real-ratio signs.

## Evidence and scope

Checker `frontier-20261029-five-frequency-two-band-obstruction-independent-kernel-v1.py`, SHA-256 `d68b02a58a50a13986dff88d71b590440da7784c5545ed051d06d5a56f810416`; receipt `frontier-20261029-five-frequency-two-band-obstruction-independent-result-v1.json`, SHA-256 `ae9c32b3ff6a8c0d2f4fb705c3a5ee7eba50ed33658443b21cd7f170f30b01b6`. The cubic, parity-band, moment, root-continuity and phase arguments are written mathematics, importing the named predecessor; only the finite class classification is independently checked by exact integer computation. This is one author's work, not formal proof, cross-vendor review, novelty clearance, or a claimed existence/nonexistence of five-node annihilators. It does not assert that strict negative-coordinate certificates themselves have this support: a hypothetical original counterexample has an exact zero annihilator via the separate eight-atom alternative, and the present theorem constrains that annihilator only in the five-positive-node/both-endpoints case.
