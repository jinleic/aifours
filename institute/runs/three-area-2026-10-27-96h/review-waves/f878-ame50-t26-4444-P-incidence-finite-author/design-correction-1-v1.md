# F878 design correction 1: unrun source v1 superseded by v2

**Additive author note; not a run receipt, review, or acceptance.** It concerns `finite-ame50-4444-p-incidence-v1.py`, for which the parent supplied metadata only: SHA-256 `fd7e5c3daafc1cc6eb0185447b2b193eb77c6794cdc795a8f22c94350c4b6cd3`, 25168 bytes, 628 LF. v1 was never executed, and no GO was requested or issued for it. Its bytes are preserved unchanged.

## Defect

In `r1_abstract_triples`, v1 enumerates the 512 abstract configurations given by `hs ∈ {0,1,2,3}^3` and three outside bits. It correctly treats a configuration as eligible when at least two triple words have `h` symbol `b_h=0`, and it correctly requires each eligible configuration to fail on an actual pair collision. Its hard-coded total, `(eligible, rejected) == (320, 320)`, was wrong. With exactly two zeros there are 3 positions for the nonzero entry and 3 nonzero values; with three zeros there is 1 choice. There are 8 outside-bit choices in each case, so the correct total is `(3·3+1)·2^3 = 80`.

[INFERENCE, not observed] Had v1 been run, it would have stopped at that stage with a check failure. That would have been a checker-expectation failure, not evidence against the r=1 argument. The parent classified this as one pre-run expectation **DESIGN MINOR**: not an observed failed run and not a proof falsity.

## Successor

`finite-ame50-4444-p-incidence-v2.py` is a complete, separately written source and the only operative candidate source. Its mathematical changes relative to v1 are:

1. The r=1 expected total is `(80, 80)`. The comment shows its derivation.
2. In a type-B row, it adds three forced-map assertions: `f(c)=1-b_j`, `f(1-b_j)=b_j`, and `{f(b_j),f(t)}={2,3}`.

Its other changes are non-mathematical:

- The internal limit is 39 s, measured from process start rather than from when the alarm is armed.
- The docstring states that the source needs Python 3.10 or newer, because it uses `int.bit_count`. v1 used the same method without stating the requirement.
- Some fixtures and controls are written as loops.
- Some functions are renamed.
- The star-enumeration loop runs its deadline check by iteration count.

v2 is also UNRUN. Before any execution, the parent must read every source byte and the complete narrative and errata, and issue a separate one-shot GO.

No code execution, test, compilation, subprocess, network, external model, deletion, Git, or edit of an existing file was used to produce this note.
