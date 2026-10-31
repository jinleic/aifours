# Literal actual-block and raw-edge definition excerpts

These selected definitions do not import the historical theorem or its proof. The entire f111 adoption remains withdrawn; no former review credit is transferred.

## /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/correct-length-residual-cover-followon/proof-UNIFORM-RESIDUAL-PARTIAL-v1.md

Full-source SHA-256 `7192a3c1e0d6a94d2711802a413ecd5a717eb95478ed6338cf46a814b05802e2`; literal lines 219–231. The source is not adopted by this excerpt.

```text
## 7. Actual odd-reflection deletion effects — no assumed composition

Let o_F count ODD maximal CYCLIC CONSTANT reflection blocks, not ordinary reflection runs. The following elementary local count statement is used only where there are at leastp+1>=8 such blocks, so the cyclic single-block/two-neighbor-degeneracies cannot arise.

**Lemma7.1.** If one ACTUAL reflection letter is removed from an ODD maximal cyclic constant block, the resulting actual word has odd-block count o_F-1 or o_F-3, never larger.

**Proof.** If the odd block has lengthell>=3, its remaining lengthell-1 is even and at least2. It remains present with the same value; previous boundaries are unchanged because neighboring values at empty gaps were different by maximality. Its odd contribution is lost and no new fusion occurs: o_F drops1.

If the odd block is a singleton, remove it. Its two adjacent rotation gaps concatenate. If the resulting gap is nonempty, neighboring reflection blocks remain separated; odd count drops1. If that gap is empty, the neighboring reflection blocks become adjacent. When their values differ they stay distinct, again a drop1. When their values are equal they fuse. If their parity indicators are alpha,beta in{0,1}, the merged parity is alpha XORbeta, so the change is

    -1-alpha-beta+(alpha XORbeta)=-1-2alpha*beta.

Thus the drop is3 exactly when both neighbors are odd, otherwise1. These are DISTINCT neighboring maximal blocks in the stated high-o_F setting; no block is double-counted. No further fusion arises at the unchanged outside maximal boundaries. Every rotation occurrence/value is unchanged, although rotation runs may concatenate in the singleton case. All counts are of the ACTUAL new decomposition, not assumed inherited parameters. QED.
```

## /Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/consolidated-lower-band-v1.md

Full-source SHA-256 `1c8d863bfb63c9d651d600af9e534d1d404663ff378c3243bbfa21e98a0d313d`; literal lines 85–115. The source is not adopted by this excerpt.

```text
## 5. One rotation-independent raw graph, all values handled

After the PROVED Z1 and P calls, rotations are nonzero and actual reflection gaps have capacity at most one. The possible-switch cyclic graph on reflections is therefore especially literal: an edge is present when the raw endpoint reflection values differ OR its gap is occupied by a rotation. No dependence on a guessed selected K remains in this graph.

FC/EQ proves that the full all-K/all-cut **GS1 predicate** is equivalent to this raw graph having a matching of at least p-1. It does NOT equate that predicate with every possible identity2p selection. Every actual survivor outside GS therefore has raw matching number at most p-2.

The graph cannot be the full odd cycle, which already has a large matching. Otherwise its components after deleting absent edges are paths, including isolates. With F=3p-2 and o_M odd-size components,

    nu_M=(F-o_M)/2.

Thus nu_M<=p-2 forces o_M>=p+2 and at least p+2 absent/flat gaps. Now EVERY rotation is nonzero, so a flat gap is EXACTLY an EMPTY gap between equal neighboring reflection values. No occupied identity gap remains because those ORIGINAL words were actually solved by Z1, not because a zero occurrence was identified with an empty gap.

Let ell_i be the lengths of the ACTUAL maximal cyclic CONSTANT reflection blocks in the original surviving word. Define

    H=sum floor(ell_i/2),
    o_F=#ODD such blocks, e_F=#EVEN such blocks,
    k_F=o_F+e_F, kappa=p-1-H.

These are actual block statistics, NOT terminal-NF parameters. The number of empty equal-value gaps is exactlyF-k_F=2H-e_F, so

    F-k_F>=p+2,
    k_F<=2p-4,
    2kappa+e_F<=p-4.                                    (B)

This now holds for ALL original rotation alphabets after the explicit actual-word Z1 removal; it is not merely the earlier zero-free COROLLARY being silently imposed on the whole band.

At the separately retained old-trust residual floor o_F>=p+2, the actual identity o_F=p+2kappa gives

    1<=kappa<=floor((p-4)/2)=(p-5)/2.

The lower bound1 uses ONLY that named inherited floor and retains its S(p) secondary/Lev statement-level ancestry. Bound(B) and the new direct word selections themselves have no such extra imports.
```
