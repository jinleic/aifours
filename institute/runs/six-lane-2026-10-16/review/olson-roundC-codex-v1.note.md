**Findings: 0 FATAL, 0 MAJOR, 1 MINOR documentation correction.** No mathematical counterexample or unresolved correctness gap was found under the declared imports.

- **MINOR — [SOURCE01:5–10,29](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-roundC-review-v1/snapshot/01-proof-INVstar-few-v1.md:29): stale dependency versions.** Adopt a citation erratum replacing REFL-few-odd r1 with **SOURCE04/r2**, and ROT-FEW-E v1 with **SOURCE02/v2**, including their supplied hashes. The latter incorporates the required even-block correction. This changes no theorem hypothesis, range, or conclusion.

The dispositions concern mathematical correctness under the supplied imports.

| Target | DISPOSITION |
|---|---|
| [SOURCE00 — OLSON-FEW](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-roundC-review-v1/snapshot/00-proof-OLSON-few-v1.md:13) | **ACCEPT**, conditional as stated |
| SOURCE01 — INV*-FEW | **ACCEPT-WITH-FIXES**, citation correction above |
| [SOURCE02 — ROT-FEW-E v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-roundC-review-v1/snapshot/02-proof-ROT-few-E-v2.md:20) | **ACCEPT**, conditional as stated; version-comparison limitation below |
| [SOURCE03 — KAPPA01 v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-roundC-review-v1/snapshot/03-proof-KAPPA01-v2.md:16) | **ACCEPT**, conditional as stated |
| [SOURCE04 — REFL-few-odd r2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-roundC-review-v1/snapshot/04-proof-REFL-fewodd-r2.md:53) | **ACCEPT**, using the accepted RED and small-\(k\) inputs |

**SOURCE00:19–31 — deletion, bookkeeping and lift pass.** Write \(\epsilon(a)=a\bmod2\). Fusion contributes
\[
\epsilon(a+b)-\epsilon(a)-\epsilon(b)\in\{0,-2\}.
\]
Deleting a rotation therefore cannot increase \(o_F\), including when its run disappears. Deleting a reflection from a surviving block changes its parity by \(\pm1\). Removing a singleton reflection removes one odd block; any subsequent fusion can only lower the count further. Empty neighboring runs, cyclic wraparound, and zero or one remaining reflection block obey the same bounds, counting each physical cyclic block once.

Consequently every deletion satisfies \(o_F(w')\le o_F(w)+1\). The stated hypotheses give respectively \(o_F(w')\le3\), \(o_F(w')\le4\) with \(p\ge7\), or \(5o_F(w')\le2p+4\).

The lift is valid despite the potentially different pairs attached to different deletions: a zero rotation or two nonopposite nonzero rotations provide a surviving obstruction in some deletion. A cyclically adjacent pair of different reflections also survives, still adjacent, after deleting elsewhere. Thus every deletion being RGR forces \(w\) to be RGR. SOURCE11:7 supplies RGR-LONG at exactly the required scope.

**SOURCE01:22–35 — maximal-block and REFL interfaces pass.** SOURCE12:7–9,29 and SOURCE13:7–11,30 support the rotation results for the original maximal constant blocks, without reflection-run constancy. The unaccepted \(p=5,o_F=4\) case is excluded correctly.

In part (b), the relevant REFL application occurs at the **\(\eta=1\) base case**, after expanding the final heavy. Expansion leaves every block odd and nonempty and preserves which rotation gaps are empty. Since every empty gap separates different values, the representation remains maximal and
\[
o_F(u^\circ(h))=k.
\]
Such an empty gap lies inside a nonconstant maximal cyclic reflection run, including across wraparound. REFL-few-odd therefore supplies exactly the contradiction needed by SHgen-E. Both this word and the final original word satisfy the required odd-block bound, since
\[
k\le o_F(w)\le(2p+4)/5\le p.
\]
No unrestricted REFL hypothesis remains hidden in this substitution.

**SOURCE02:20–29,33–53 — the even-block repair works.** The rotations-only case is excluded by two applications of EGZ at \(p\). For a surviving single even block, setting \(H=F/2\) gives
\[
R+H\le3p-2,\qquad R=4p-2-2H,
\]
hence \(H\ge p\); that block contains \(2p\) identical reflections. The alternative exclusion by accepted one-block K1 is also valid, since K1 forces \(F=2p-1\).

The all-odd continuation, recomputed parameters and transfer of the rotation multiset remain valid. FLEXa uses no nonempty-run assumption; expansion preserves the empty gaps throughout induction.

The correction matches SOURCE10:3–8 and the embedded diff at SOURCE02:65–94. **The literal assertion “NOTHING else changed” cannot be independently certified:** the actual v1 file is absent from this snapshot. The current mathematical proof passes; the embedded diff is not an independently checked version comparison.

**SOURCE03:16–66 — both slices pass at the revised range.** Normalization gives
\[
\widehat\kappa=\kappa(w)-(o-k)/2\ge0.
\]
Thus \(\kappa(w)=0\) forces \(k=o,\widehat\kappa=0\); \(\kappa(w)=1\) permits exactly the two cases stated.

For the triangle case, deleting two order-two terms leaves a zero-sum-free sequence with \(e=k-1\). MULT requires
\[
3e+2=3k-1\le2p,
\]
which follows exactly from the corrected \(3k\le2p+1\). Its remaining order-two term is \(pg\), forcing \(p\le e+1=k\), impossible in this range.

The star argument also passes: \(d\le k-1\le m'\) makes \(c_0g^d\) available, and the forbidden zero-sum lengths force \(d=1\), hence \(c_0=-g\). The resulting bounds \(E\le k-1\) in K0 and \(E\le k-2\) in K1 supply (H) and (K). Expanded-word REFL applications have \(o_F=k\le p\). The stronger ELT0-FEW conclusion is imported only where the original word has constant runs and its hypotheses hold.

**SOURCE04:53–71 — MON and the terminal contradiction pass.**

| Move | Effect on \(o_F\) |
|---|---|
| P1 | Adding/recolouring an even block preserves recipient parity; double fusion decreases the count by \(0\) or \(2\). |
| P2 | Removing an even block and appending its even length preserves parity; the merged rotation run stays nonempty. |
| P3 | The donor stays nonempty; filling a gap between different values changes no constant block. |
| P4 | Inserting two identical reflections preserves block parity; deleting the rotation run permits only parity-nonincreasing fusion. |

These arguments cover cyclic boundaries and degenerate mergers. Normalization preserves block lengths. RED’s accepted terminal word has all maximal constant blocks odd, so its **constant-block count** is \(k=o_F\le o_F(w_0)\le p\), contradicting SOURCE14:13. SOURCE16’s correction to P4’s \(\kappa\) bookkeeping does not affect this argument.

I independently checked the new reductions, interfaces, parameter bounds and MON argument above. GRX/PM*, one-block K1, Davenport, RGR-LONG, RED/K0*, the small-\(k\) result, and SOURCE05–09 remain imports at their supplied scopes. No finite census or experimental observation was used as a premise.

All **17 SHA256 pins match**. Only static reads and hashes inside the permitted snapshot were performed. No gate authority or novelty claim is asserted.