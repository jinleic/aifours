# Universal residue obstruction for balanced nine-variable NL242

**Result: reviewed necessary conditions and one excluded residue type, not a solution.** Existence of a balanced nine-variable Boolean function with nonlinearity 242 remains open. All reviews below are model reviews, not human peer review or formal verification. The methods are prior art and novelty is unestablished.

## Statements

1. **Pair theorem.** Let `g,h` be odd-weight eight-variable Boolean functions with Walsh spectra satisfying `|G|+|H|<=28` everywhere. The quadratic

   ```
   D = (G^2-4)/32 + (H^2-4)/32 mod2
   ```

   satisfies `40 wt(D) >= 6656 - 512*2^r`, where `2r` is its polar rank. Hence `wt(D)>=112`, and only nine rank/weight pairs survive. [`SHARPER.md`](SHARPER.md) has the proof; the earlier, independently reviewed `wt(D)>=96` argument is [`PROOF.md`](PROOF.md).
2. **Balanced corollary.** A balanced nine-variable function with Walsh peak at most 28 has nonzero support XOR `s` (classical quadratic/Parseval argument, Wang–Lou–Wang Proposition 1). On the eight-dimensional space `s-perp`, the function `Q(a)=W_f(a)/8 mod2` is quadratic and is identified with `D`. Therefore at least 112 of those 256 frequencies have `|W_f| in {8,24}`. `Q` must belong to one of eight affine-equivalence types: rank2/weight192; rank4/weight128 or160; rank6/weight112,128 or144; rank8/weight120 or136.
3. **Type (rank4,weight128) excluded (model-reviewed).** [`zero-geometry/`](zero-geometry/README.md) proves that no balanced nine-variable peak<=28 function has intrinsic residue type (polar rank 4, weight 128). The proof assumes the Opus-reviewed zero-set/magnitude and next-bit lemmas. A fresh Codex `gpt-6.1-sol` review returned ACCEPT with no fixes, and the parent replay passed.
4. **One-to-three-zero corollary (same review).** A nine-variable function with exactly 1, 2 or 3 Walsh zeros has NL<=240. This rests only on the reviewed first zero moments. Priority is unresolved.
5. **Seven types remain:** (2,192), (4,160), (6,112), (6,128), (6,144), (8,120), (8,136). [`remaining-types/`](remaining-types/README.md) holds **unreviewed** partial results: new necessary conditions, a (6,144) sub-case, (2,192) coset lemmas and explicit stopping-point witnesses. No further type is excluded.

## Verification

| Gate | Result |
|---|---|
| Opus 5.5 hostile review of distance96 | correct; five exposition fixes applied ([`independent-review.json`](independent-review.json)) |
| Codex `gpt-6.1-sol` review of the corrected distance96 proof | ACCEPT, no fixes ([review](../../../../institute/review/continuation-20261015/quadratic-distance-codex-review.md)) |
| Codex `gpt-6.1-sol` review of the sharper112 theorem | ACCEPT, no fixes ([review](../../../../institute/review/continuation-20261015/quadratic-distance-sharper-codex-review.md)) |
| `python3 audit.py` | PASS: complete cap-28 pointwise domain, quadratic normal forms, energy constants and a capacity-essential control |
| `python3 sharper_audit.py` | PASS: complete pointwise domain, rank/weight table, and exact transform identities on real odd halves at cap32 |
| Corrupted inequalities | `--corrupt-majorant` and `--corrupt-r-bound` both exit 1 at genuine extremal pairs |
| Count relaxation over the nine types | exploratory only: it excludes only rank0/weight256, already excluded by `Q(0)=0` ([`type-count-explore.json`](type-count-explore.json)) |
| Codex `gpt-6.1-sol` review of the (4,128) exclusion and the 1–3-zero corollary | ACCEPT, no fixes ([review](../../../../institute/review/continuation-20261015/info-zero-exclusion-codex-review.md)); parent replay of `zero-geometry/code/audit.py` PASS |
| `remaining-types/code/audit.py` | PASS in the parent replay; results unreviewed, no exclusion claimed |

No formal verification or human peer review has been performed. Finite controls support the arithmetic; they do not replace the universal proofs.

## Attribution and scope

The quadratic residue, canonical-sign normalization and paired-half capacity identity are prior art (Wang–Lou–Wang, [arXiv:2610.17871v1](https://arxiv.org/abs/2610.17871); Lou–Xu–Wang, [arXiv:2610.17897v1](https://arxiv.org/abs/2610.17897)). The correlation step follows Lou–Xu–Wang's rank argument. Only this specific combined necessary condition is a candidate contribution, and its novelty is unestablished.

Seven types remain after the (4,128) exclusion. They are not small finite cases. Excluding them would require new mathematics or a proof-producing representation, not longer runs of earlier searches. The restricted 252-class corpus exclusion is separate: [`../README.md`](../README.md).
