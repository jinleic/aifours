# Olson RPdelta: SEG-k, initial-word transfer and B/B-prime exclusions

Recorded at 2026-10-19T13:04:25-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Written mathematics relative to [V5](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md) `13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547` with all bindings S1/m1-m7. **INV, TRANSFER and T1-T3 retain the conditional import base of accepted RED**, including its RGR imports (I1)-(I4) only at their stated exit scopes and K0*. None is enlarged to arbitrary genuine-empty-run words. Neither RP-LIFT nor RP-2NE is an input. REFL(p), REFL-HI(p), RES-HI(p), INV*(p) and full ordered Olson remain OPEN.

## Text of record and mandatory overlays

Use the eight exact texts K, K-e, T, B, B-e1, B-e2, BP, BP-e named in the [v2 package](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/review-package-RPdelta-v2.md) `38ab5e7d41a5a5cdb4c88d583690b2381b371da72357b3276832f975e5522ce4`, all pinned in the [v2 freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-claude-v2-deferred-freeze-v1.json) `2e4fb95f6ab459a999cd6b428e6ff26eb24aa2d052f20515c37f937729f078d9`. Their original errata stay mandatory. Apply [consolidated erratum E1-E5](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/erratum-1-RPdelta-consolidated-v1.md) `2450446d526305e561ee2c8c05b1946dd704363f31d95eef58df5797d73a2136`, then the [parent erratum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-parent-erratum-v1.md) `110338d856445866c91c42208bd900987f9761110ef47ef540104f91d70b65b4` last. The [v2 excerpt manifest](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/review-excerpts-RPdelta-v2.json) `ad52ef73d41059b64c29d49c6dfacb815a72f952991c649164f400920afb62ce` contains 30 ranges from 21 files; the parent verified every whole-file hash and range.

## Setting and accepted statements

For the all-odd statements: p>=5 prime; a cyclic word of length 4p-2 over D_(2p); rotations in one nonzero pair {rho_x,rho_-x}, normalized to x=1 and A>=B; every maximal cyclic constant reflection block odd; genuine empty runs. H=sum floor(l_i/2), kappa=p-1-H, k the number of constant reflection blocks and R=2p-k+2kappa. No run-purity or B<kappa hypothesis is added to SEG-k or B/B-prime. Residual-class consequences still require the actual residual hypotheses.

1. **SEG-k:** k>=4kappa+5 and k>=p+floor(R/2)+1 imply an increasing-index identity 2p-subword. This is a sufficient criterion, not a necessary condition. The R=0 case uses AR.
2. **INV:** along the accepted RED process on an initial REFL-violating avoider, D=A-B is constant, while B, kappa and g=kappa-B never increase. The terminal satisfies 1<=g_T<=g0, 0<=B_T<=B0, R_T=D0+2B_T>=p, k_T=2p-D0+2g_T and kappa_T=g_T+B_T>=2.
3. **TRANSFER:** for an initial avoider w0 (constant blocks may be even), normalize A0>=B0 and set D0=A0-B0, kappa0=p-1-sum floor(l_i/2), g0=kappa0-B0. If every integer cell 1<=g<=g0, 0<=b<=B0, g+b>=2 satisfies one of the six clauses below, every maximal cyclic reflection run of w0 is constant. An empty box gives the conclusion by contradiction with the RED terminal.
   Set kappa=g+b, R=D0+2b, k=2p-D0+2g, Delta=p+kappa-1-R. Clauses:
   - (a) k<=p (SMALLK, only on the hypothetical residual terminal).
   - (b) k>=2p+1 and k>=3kappa+3.
   - (c) k>=4kappa+5 and k>=p+floor(R/2)+1.
   - (d) p>=11, R=p, kappa>=(p+1)/4.
   - (e) R<p.
   - (f) b=0, R>=4kappa-4, and either Delta<=1 or p>=kappa+5Delta-5; CJ/EDGE at its accepted scope, with R>=2p covered separately by equal-rotation selection.
4. **T1:** |A0-B0|<=1 and o_F(w0)>=3kappa0+3 imply the reflection-run conclusion. **T2:** o_F(w0)>=4kappa0+5 and A0+floor(D0/2)<=p+1 imply it. **T3:** if o_F(w0)>=3kappa0+3, only box cells D0-p<2g<=D0 need checking against (c)-(f). Here o_F counts odd maximal cyclic CONSTANT reflection blocks, not reflection runs. These are initial-word statements at RED's conditional scope, not terminal numerical bands.
5. **B.1-B.3** at their printed scopes, with B.2 requiring 1<=delta<=(p-12)/3 and its (viii) range estimate read as sufficient. The capped-gain invariant and the G_need=0 case are mandatory as corrected.
6. **Theorem B:** for eps in {0,1}, kappa=(p-1)/2-eps and R=p+delta, the all-odd word has an identity 2p-subword whenever 1<=delta<=(2p-29+2eps)/7.
7. **Theorem B-prime:** under the same setting, the conclusion holds for 1<=delta<=min((p-12+4eps)/3,(2p-32+2eps)/3). Its validity conditions are rechecked, not imported by applying B.2 outside B.2's range. B-prime contains every nonempty Theorem-B range.
8. **B.4:** a remaining avoider in region B with 1<=delta<=(p-12)/3 must satisfy a=|AB|<=N_O and 2x<7delta-2p+29-2eps, where x=R-q. This is necessary word structure, **not another universal exclusion band**.

## Exact numerical increment relative to I.14

For delta>=1, retain the literal E1 definitions:

- J=[max(2,ceil((delta+1)/2)),p-1] over integers.
- A=[ceil((p+3delta+2)/4),floor((p-delta-4)/2)] union [ceil((p+delta+1)/2),p-delta-3]. An interval with lower>upper is empty.
- E contains (p+3delta+1)/4 exactly when delta>=2 is even, p+3delta is 3 modulo 4, and p>=5delta+11; otherwise E is empty.
- M_BP(p,eps)=min(floor((p-12+4eps)/3),floor((2p-32+2eps)/3)); N consists of (p-1)/2-eps for eps in {0,1} with 1<=delta<=M_BP(p,eps).

The numerical increment supplied here is exactly E union N, and the remaining values under these stated numerical tests are J minus (A union E union N). This compares fixed numerical bands, not all previously available structural arguments or realizable words. At delta=0, I.14 is unchanged. TRANSFER adds no independent terminal band and does not automatically import B/B-prime or the odd-delta SEG-num top cell into its six clauses.

## Reviews and parent checks

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-codex-v1.prompt.stdout.txt) `e11c4dcb4d57f9e665e892c40955c695c0b48ab605853171d21d47fe75b1759d`: gpt-6.1-sol/max/read-only, all four groups ACCEPT-WITH-FIXES, 0 FATAL/0 MAJOR/5 MINOR. All five disposed by consolidated E1-E5.
- [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-claude-v2.prompt.note.md) `a6bd0e096ecb62897638715909f37b016ca8f6354ac8463d8f6cf5487d8caaac`: claude-opus-5-5/max/no tools, independently re-derived all four groups and E1-E5; 0 FATAL/0 MAJOR/5 distinct MINOR (B-1/B-2 shared across B and BP). Disposed by the parent erratum without changing statements or ranges. The earlier capacity NO_VERDICT is not approval.
- Parent hand checks: k>=4kappa+5 gives R<=2p-2kappa-5; the sufficient TRANSFER inequality 2g-b>=2-B0 gives A0+floor(D0/2)<=p+1, without an attained-corner assertion; P0's positive odd-run count gives d>=1; G_need=0 requires no added segment units, so no negative gain bound is needed; at p=31,delta=4 the parity endpoint is 11 while the SEG-num interval is [12,11]. Read both full reviews and the source ranges affected by the parent erratum; no scientific computation performed.

## Remaining and trust boundary

The numerical complement above remains, subject to word-specific raw SEG, B=0 CJ/EDGE and B.4. I.14's uncovered R=p cells remain uncovered by this packet: (5,2), (5,3), (7,3), and 2<=kappa<ceil((p+1)/4) for p>=11; diversity-conditional FP-1 is not universal coverage. The reviewer's proposed separate (17,0,1) closure is not promoted. The accepted statements do not establish unrestricted reflection/rotation rigidity, full ordered Olson, existence of avoiders, a realizability census, novelty, priority, Lean verification or human review.
