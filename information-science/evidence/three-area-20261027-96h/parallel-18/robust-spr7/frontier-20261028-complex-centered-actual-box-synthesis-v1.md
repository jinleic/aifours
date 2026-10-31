# Exact common numerator for a different, complex-root-centered septic box

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This is a constructive result for one explicit all-member-stable interval box and its nested subboxes, not a universal SPR theorem or a negative certificate.

Let
\[
a_0(s)=(s+1)((s+1)^2+4)((s+1)^2+16)((s+1)^2+64),
\qquad r_*={4145923}/{67108864}.
\]
Its ascending coefficients are \((5525,8555,4893,2219,455,105,7,1)\). Let \(K_r\) have independent intervals \([a_{0,j}(1-r),a_{0,j}(1+r)]\) for \(j=0,\ldots,6\), and leading coefficient one.

At \(r=r_*\), every member of \(K_{r_*}\) is strictly Hurwitz and the following monic numerator works for all members and all real frequencies:
\[
(b_0,\ldots,b_7)=\left(\frac1{5000},\frac{7875271743}{5000},
\frac{8004469927}{5000},\frac{4087786311}{5000},\frac{1275580841}{5000},
\frac{134030769}{5000},\frac{48675703}{10000},1\right).
\]
More precisely, with \(t=\omega^2\), the compactified pairing \(P_{a,b}(t)/(1+t)^7\) is at least
\[
\delta=\frac{39406433438245031889}{39406496739491840000}>0
\]
for all \(a\in K_{r_*}\), \(t\ge0\). With \(S=1+\sum_{j=0}^6u_j=1550500019197/67108864\), the ratio itself satisfies
\[
\operatorname{Re}\frac{b(i\omega)}{a(i\omega)}\ge
\frac{\delta}{S^2}=
\frac{39406433438245031889}{21035440208386601974592078750}>0.
\]
The same numerator and stability statement hold for every nested \(K_r\), \(0\le r\le r_*\).

The midpoint numerator \(b=a_0\) does not work for this box: at actual corner \((E_-,O_+)\) and \(t=241/15\), its pairing is exactly
\(-94364663437436899057/89579520000000\). The example therefore requires a different numerator from that natural choice; it does **not** exclude other numerator choices.

At \(r^+=2081153/33554432\), the actual corner \((E_-,O_+)\) has sixth Hurwitz determinant
\[
-\frac{3144140301663432159380594098522442147523795988195321038125}
{1427247692705959881058285969449495136382746624}<0.
\]
Consequently every \(K_r\) with \(r\ge r^+\) contains that fixed non-Hurwitz polynomial and is ineligible. The interval \((r_*,r^+)\), of width \(16383/67108864\), is not disposed by this result.

## Exact evidence

The frozen certificate `frontier-20261028-complex-box-common-numerator-frozen-v1.json` has SHA-256 `1c07fc4f8f6a8c5714d4ad6b1cae0957400b8ad8b7ee4097f6789dc22cb9996e`. It contains the exact endpoint vectors, four parity cubics, 12 rational root brackets, the reference Routh column, four pairing polynomials and complete Bernstein leaves. The root brackets yield six strictly separated even/odd bands; the same connected-box/no-imaginary-crossing argument as in the three-gap packet establishes all-member stability. At each frequency, the minimum pairing over the independent coefficient box is the minimum of these four actual corner pairings. Their exact positive Bernstein leaves cover \([0,1]\) in the compact variable \(x=t/(1+t)\); the respective leaf counts are 6, 5, 7 and 5.

The standalone independently written replay `frontier-20261028-complex-box-independent-replay-kernel-v1.py` (SHA-256 `d7b62465fa685c09b83abf3119332613c7b5df26e428c2ffb288c717f85b3722`) reconstructs all 28 rational corner Hurwitz minors, the 12 root brackets and six bands, the reference Routh column, pairing polynomials, every Bernstein coefficient by direct affine power substitution, both margins, and the midpoint failure. It rejects a corrupted leaf and a reversed root bracket. Its receipt `frontier-20261028-complex-box-independent-replay-result-v1.json` has SHA-256 `01b728750cffc6210b197ed31b9d4c23e2ec3ef5de697ca9e6fe557d9ec86197`.

The upper-endpoint determinant was computed independently by rational Gaussian elimination and integer Bareiss, with matching scaling; see `frontier-20261028-complex-box-upper-instability-addendum-v1.json`, SHA-256 `b70a138d8549b5f4ad38c15d7b03776659f05a3f26857256ffc06b9eb7d97d35`. The numerator was found by an exact Bernstein inner-cone search and rounded exactly, not by treating a finite-grid dual as a full certificate; producer hashes are `efed43b02651c487638e55e50faf4b019187f8c08bb8e95a6df7a73a0b3655e6` and `a63da35c98a02387655451073c3652fe73f1ffb31dfd8f787f2d3b6a9eadfc67`.

Imports are elementary parity/interlacing, root continuity and exact Bernstein positivity on an interval. Computation uses integer and `fractions.Fraction` arithmetic in one Python Eval host. It is not formal verification, a cross-vendor review, novelty clearance, or a result for arbitrary boxes.
