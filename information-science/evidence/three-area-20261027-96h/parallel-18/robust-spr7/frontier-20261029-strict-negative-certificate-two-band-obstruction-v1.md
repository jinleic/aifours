# Direct obstruction to strict negative-coordinate certificates

**Status: WRITTEN theorem candidate with WRITTEN-checked-in-kernel finite phase classification; not parent adoption.** This applies **directly** to the original strictly negative-coordinate atom certificate, rather than passing to a zero annihilator or assuming its support.

Let \(K\) be any compact independent coefficient box of monic Hurwitz septics. Consider a finite positive-weight collection of actual denominator/frequency pairing atoms, possibly including zero and compactified infinity. Suppose its aggregate coefficients on **all eight** numerator monomials \(b_0,\ldots,b_7\) are strictly negative. Merge all positive-frequency atoms at the same squared frequency by positive-weight averaging their actual denominators; the averaged denominator remains in the same stable box. Let the resulting distinct positive nodes be \(t_1<\cdots<t_m\).

1. Both sequences of actual parity evaluations \(E_{a_i}(t_i)\) and \(O_{a_i}(t_i)\) must contain the oriented sign subsequence **\(-,+,-,+\)**. In particular \(m\ge4\).
2. The global ordering of the actual even/odd root bands strengthens this to **\(m\ge5\)**, even if zero and infinity atoms are allowed.
3. If \(m=5\), the samples must have two reversed crossings, one in an odd root band and another in a later even root band. Their only possibilities are:

| Phase classes \((q_1,\ldots,q_5)\) | Forced nondegenerate node intervals inside global root bands |
|---|---|
| \((2,1,3,2,4)\) | \([t_1,t_2]\subseteq O_1\), \([t_3,t_4]\subseteq E_2\) |
| \((2,1,3,5,4)\) | \([t_1,t_2]\subseteq O_1\), \([t_4,t_5]\subseteq E_3\) |
| \((2,4,3,5,4)\) | \([t_2,t_3]\subseteq O_2\), \([t_4,t_5]\subseteq E_3\) |

Consequently no strictly negative certificate with five positive nodes can be supported on a grid with at most one node in each global parity-root band. These restrictions are necessary, not sufficient: no actual certificate or original verdict follows.

## Exact moment sign lemma

For merged node \(t_i\), let \(\mu_i>0\) be the uncompactified positive weight, and put
\(x_i=\mu_iE_{a_i}(t_i)\), \(y_i=\mu_i t_iO_{a_i}(t_i)\). Positive zero- and infinity-atom contributions, if present, enter only the \(b_0\) and \(b_7\) coordinates. Strict negativity of the eight coefficients implies, for **both** \(z=x\) and \(z=y\),
\[
\sum_i z_i<0,\quad \sum_i t_i z_i>0,\quad
\sum_i t_i^2z_i<0,\quad \sum_i t_i^3z_i>0.
\]
For example a zero atom only makes the first \(x\)-inequality stricter, and an infinity atom only makes the last \(y\)-inequality stricter.

We prove these four inequalities force an oriented \(-,+,-,+\) subsequence of the nonzero \(z_i\). If not, its ordered sign word fits inside four blocks \(+^* -^* +^* -^*\), with any blocks allowed empty. Choose three distinct positive numbers \(r_1<r_2<r_3\) in the corresponding gaps, including before the first node or after the last if needed. Then
\[
q(t)=\prod_{j=1}^3(r_j-t)=q_0-q_1t+q_2t^2-q_3t^3,\qquad q_k>0,
\]
has the same sign as every nonzero \(z_i\), so \(\sum_i z_iq(t_i)>0\). But expanding using the four moment signs makes every term strictly negative, a contradiction. This also rules out \(m<4\).

## Phase ordering and five-node classification

The independently selectable even and odd coefficient parts give six compact globally strictly separated root bands \(E_1<O_1<E_2<O_2<E_3<O_3\), as derived in `frontier-20261028-five-frequency-single-endpoint-exclusion-v1.md` (SHA-256 `e8aae88916a5275f0cbe4fe057dd6bcc2eea809f6ab1d3f8bb5a897d2db23f2a`). Each stable actual denominator has a strictly increasing unwrapped phase and classes
\[
q=0,1,2,3,4,5,6:\quad (++),(-+),(--),(+-),(++),(-+),(--).
\]
For any \(t_i<t_j\), any valid class choices satisfy \(q_i\le q_j+1\); if both parity signs reverse, \(q_j\ge q_i+2\). A parity-zero sample permits either adjacent class. A stable denominator never has both parities zero, so such a class can be chosen while retaining the four nonzero sign entries in each oriented subsequence.

With \(m=4\), the sign lemma forces both parity signs to be exactly \(-,+,-,+\), so the four samples have the sign sequence \((--),(++),(--),(++)\). The first class is at least 2 and the three double reversals advance at least 6, impossible because the final class is at most 6. Thus \(m\ge5\).

For \(m=5\), the independent integer enumeration considers all \(7^5\) class sequences, retaining exactly those satisfying both oriented subsequences and **every** pairwise ordering constraint. There are exactly the three sequences in the table; omitting phase order leaves 676 sequences, so the check is not vacuous. A backward class step \(r+1\to r\) between increasing frequencies forces the whole intervening node interval into the corresponding global parity-root band: the earlier actual root is at or before the first node, while the later actual root is at or after the second. This proves the stated band constraints, including root-side equality cases.

## Evidence and scope

Standalone finite phase checker `frontier-20261029-strict-certificate-five-node-phase-independent-kernel-v1.py`, SHA-256 `ac13abaad74ea3c110d86b0cfa2a309b3aa7d5b1fe733e58ca4273ac3219ec9a`; receipt `frontier-20261029-strict-certificate-five-node-phase-independent-result-v1.json`, SHA-256 `84fdaf7e1045bb746e491b8c46ea2ce8babb4900c7589ef7abeb5d51cfd85c44`. The oriented-sign lemma, frequency averaging, compact root-band and phase arguments are written mathematics; only the finite class classification is machine-checked, using integer arithmetic in one Python Eval host. This is not formal proof, cross-vendor review, novelty clearance, an exclusion of all \(m\ge6\) certificates, or an arbitrary-box existence verdict.
