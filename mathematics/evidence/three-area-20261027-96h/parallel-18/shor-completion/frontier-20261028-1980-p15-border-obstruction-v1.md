# Shor completion: forced gcd396 excludes the 15-head border at order 1980

Owner **MathShor-2**, math-5. Actual clock of independent finite replay: **Wed Oct 28 19:45:32 PDT 2026**.
**Conditional necessary-border reduction plus two independently implemented exact finite checks. No n=1980 exclusion, original-problem solution, formal/peer/cross-family verification or novelty claim.**

## 1. Exact branch and arithmetic

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order1980 and same-D direct border factors P,Q with the old anchors

    A={0,3,8,11} subset P,      Y={0,1,7,13,14} subset Q.

The actual-word border factorization and the necessary Sands gcd-class disjointness criterion are classical and were independently reconstructed in earlier pinned packets. This packet excludes only `|P|=15, |Q|=132` by showing that **each side must contain a nonzero difference of gcd396**, forbidden by Sands.

Here `1980=2^2*3^2*5*11`. P's size15 and Q's size132 force:

* P uniform modulo5, with3 elements in each class, since Q's size is coprime to5.
* Q uniform modulo4, with33 elements in each class, since P's size is odd and therefore both `Phi_2` and `Phi_4` divide Q.
* Q uniform modulo11, with12 elements in each class, since P's size is coprime to11.

The old P-difference classes are `{3,4,5,11}` and old Q-difference classes are `{1,2,6,12}`.

## 2. P must use gcd396

Assume P avoids gcd396 as well as the old-Q gcd classes. Retain only old-anchor-compatible P-candidates in mod5 classes0,1,2,4; there are56. These four classes each require3 P-elements and include the actual old anchors0 and11. This drops class3 and every other condition, so it is a relaxation.

An exhaustive bitset quota search on the56 candidates returns UNSAT in73 nodes with36 quota prunes. An independently written set-based search with different branching returns UNSAT in79 nodes with40 prunes. Consequently any actual P must use gcd396.

## 3. Q must also use gcd396

Assume Q avoids gcd396 and the old-P gcd classes. Retain only old-anchor-compatible Q-candidates in mod4 classes1,2,3 OR mod11 classes1,2,7; there are298. The retained actual old anchors are1,7,13,14. The six required quotas are

    mod4 classes1,2,3: 33 each;
    mod11 classes1,2,7: 12 each.

All other Q-elements, the remaining quota classes, and the full factorization are deliberately ignored, so this too is a relaxation. The bitset search returns UNSAT in147 nodes with74 quota prunes; the independently written set-based search returns UNSAT in173 nodes with87 prunes. Any actual Q must therefore use gcd396, contradicting §2 and Sands disjointness.

The primary checker also directly validates an explicit P relaxation witness and an explicit Q relaxation witness after **only the extra gcd396 ban is removed**. Both witnesses contain gcd396 differences. These are positive controls for the finite search, not direct border tilings or complete codes.

## 4. Evidence pins and limits

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-1980-p15-forced-396-check.py` | 45145db5ac14a71bf9be15866d0c84b39c290e798d67ec005fff460ab6a25f8b | 56 / 3282 |
| `frontier-20261028-1980-p15-forced-396-replay.py` | 0647b7a00362e6e9932971fe8cba359b07b575a387843bc4614132b56939edf1 | 38 / 1892 |

The original generic Z3 run on this branch timed out and is NOT a premise. These searches establish only the stated finite necessary-border obstruction, subject to disjoint scientific review. The 1980 branches P=12 and36 have separate unreviewed packets; other sizes remain open. The original finite UD factor-completion problem remains OPEN.

**END OF ORDER-1980 P15 BORDER OBSTRUCTION.**
