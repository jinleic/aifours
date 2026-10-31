# Original-order selectors from ANY actual reflection run and adaptive rotations

Owner **MathOlson-2-2**, original math-2. Native clock before write: **Wed Oct 28 17:37:05 PDT 2026**.
**Written candidate with a bounded producer-only check; independent checker NOT YET RUN.**

## 1. Uniform conditional theorem

Let p be any odd prime. In an ACTUAL D_(2p) word of length4p−1 suppose `2p−2≤R≤3p−2` rotations, `t=R−(2p−2)`, and a contiguous ORIGINAL run H of at least two reflections.
Let `D_H={y_j−y_i : i<j are actual reflections in H}⊆F_p`.
Let C be the maximum number of pairwise disjoint pairs of actual rotation positions with DIFFERENT exponents. Put `s=min(C,t,p−1)`.

If

`min(p,s+1)+|D_H|>p`,

then the word has an original-order identity selector of exactly2p actual occurrences, comprising2p−2 rotations and two reflections from H.

This is a proper actual-word condition. It does NOT claim every word satisfies it, any original counterexample exists, the entire dihedral problem is solved, or the theorem is novel.

## 2. Full original-order proof

Choose any s disjoint unequal rotation pairs. Because `s≤t≤p` and s≤p−1≤2p−2, there are at least t−s unpaired rotations available: `R−2s≥t−s` since `R−t=2p−2≥s`.
Fix t−s omissions among those unpaired positions, then omit exactly ONE actual position from each chosen pair. This omits exactly t rotations and retains2p−2.

Each independent pair choice changes the omitted exponent sum by a nonzero F_p increment. For any nonempty proper A⊊F_p and δ≠0, `A∪(A+δ)` has at least |A|+1 elements because translation by δ generates all F_p. Thus the attainable selected rotation-sum set Σ has size at least `min(p,s+1)`.

For ANY two reflections i<j in the SAME contiguous original reflection run H, no rotation occurs between them. Ignoring unselected reflections, the actual chronological product of those reflections and a chosen rotation set is

`r^( S+y_i−y_j )`,

where S is the sum of the actual retained rotation exponents. The order of the remaining rotations before/after the pair does not change their sign: the two selected reflections are consecutive with respect to rotations.
The support inequality gives `|Σ|+|D_H|>p`; therefore Σ∩D_H is nonempty. Choose actual omission choices giving S and an actual ordered reflection pair giving `y_j−y_i=S`. Their ORIGINAL ordered union has exactly2p occurrences and product1. No virtual coefficient, rearranged reflection, gap-independence or unproved global selector is used.

## 3. Easily checked lower bound for the directed-difference set

If H has h distinct reflection exponents and `eps=1` when some exponent repeats in H (else0), then

`|D_H|≥h−1+eps`.

Every distinct exponent besides the FIRST run value occurs later and gives a different nonzero directed difference from that first value. A repeated value adds0.
Thus the explicit sufficient condition

`min(p,s+1)+h−1+eps>p`

also pays the theorem. In particular, when s=p−1, ANY actual contiguous pair of reflections suffices; no run of length p+1 is required.
The exact directed-difference support condition can be stronger. No bound here is asserted necessary.

The usual maximum matching identity `C=min(floor(R/2),R−M)` for M the largest rotation-exponent multiplicity gives an exact way to read C: pair each minority with a majority if one class exceeds half; otherwise pair two largest classes and induct. This is a statement about actual positions, not a preassigned matching.

## 4. Proper word class outside earlier sufficient certificates

For ANY prime p≥5 take the FULL actual word

`(r)^(2p−2), s,s, (r²,s)^(p−1), s`,

with repeated factors denoting distinct original occurrences. It has R=3p−3,F=p+2,length4p−1; every rotation exponent is nonzero.
There are p−1 disjoint unequal rotation pairs joining p−1 initial r positions to the p−1 later r² positions. The first `s,s` is a contiguous run with `D_H={0}`; s=t=p−1, so the condition holds.
An explicit valid selector chooses the first2p−4 initial r's, those first two adjacent s's, and TWO of the later r²'s. Its total rotation exponent is `(2p−4)+4=2p`, and the adjacent selected s's multiply to1. It uses exactly2p original positions.

No two distinct rotation exponents occur within ANY reflection gap, so the earlier same-gap-pair theorem does not apply. For the earlier fixed I of the first2p−2 rotations, S=−2≠0 and all reflection potentials coincide; its exact two-reflection equation has no solution. The quotient run pattern has2p−3 odd runs, so the earlier saturated-separated-pair criterion also fails for p≥5. This does NOT rule out any other certificate or imply an avoiding word.

## 5. Bounded run actually performed; independent checker still due

`frontier-20261028-dihedral-short-run-experiment.py`, SHA256 `a2669f75a2a8a0e405385bf8b8a2e185e6c828a8d13f904359652e52e335b7e6`, was run once with seed2026102806,40 random full words per `(p,R)` for p=3,5,7,11 and all R in the displayed band.
It reported `PASS_BOUNDED_SHORT_RUN`: **1,200** actual random words, **659** meeting its exact support condition and producing direct-checked original selectors, plus four structured family instances. Saved full result SHA256 `d5f8392f4adcfa056202bcc581385dc07d4ca9bef96d83e13da03300c2cd0a6d`.

This is a producer-only run; **no independent checker, proof assistant or peer review has yet validated this new theorem or its finite outputs**. It is being pinned at the transition to the assigned priority review. A later independent checker must not rerun/overwrite the producer or misstate this record's earlier scope.

## 6. Boundaries

The full all-finite-group/dihedral original problem and the remainder of the intermediate count band remain open at the available evidence scope. No actual avoiding word, all-word selector, formal/human/configured-family acceptance or priority claim follows.
The current owner direction prospectively permits bounded scientific checks; historical quarantined outcomes are not accepted as premises. Only elementary group/prime-field counting is used here; no external model/paid API, secret, deletion, Git push, publication or infrastructure mutation.

**END — short contiguous reflection run candidate.**
