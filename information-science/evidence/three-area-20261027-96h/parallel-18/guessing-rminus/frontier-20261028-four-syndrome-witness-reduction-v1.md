# The four-varying-syndrome case reduces to six 12-bit witness problems

**Status: WRITTEN with independently checked exact factor-cover orbits; conditional on the pinned graph-FD inequality; scientific review pending.** Suppose a q=8 original-neighbour FD law with positive balance gap exists and exactly four of the ten triangle syndrome bits are nonconstant. Then a positive-gap original-FD law exists on a **12-bit mixed alphabet**: eight graph vertices receive one bit each and two adjacent vertices receive two bits each. Up to the factor-preserving graph automorphisms, it is enough to search these six four-factor covers:

```text
{2,3,5,6}   {1,3,6,7}   {3,4,6,7}
{3,5,6,7}   {2,5,6,9}   {3,4,7,10}
```

Conversely, any positive-gap FD law on one of these six mixed alphabets embeds into q=8 vertex symbols by setting the six unused factor components to constants. The earlier entropy-balancing/type-class reduction `frontier-20261028-entropy-balance-equivalence-v1.md` SHA-256 `4013d40004f9e6576973517b5a36e634e294f6713f75ff44273d4266d920090e` would then convert it to a strict unrestricted guessing-number gain. This statement does **not** reduce laws with five or more varying syndrome bits, and does not claim that any of the six cases has a witness.

## Why the reduction is exact

The syndrome-cover theorem `frontier-20261028-syndrome-cover-entropy-gate-v1.md` SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b` requires the four varying factors to cover all vertices. Process the other six fixed-syndrome factors first, and condition on their entire component tuples. The fixed factors individually have nonpositive balance contribution under conditioning. The same chain-rule/conditioning argument shows that the original positive gap is at most the **average** balance gap of the last four-factor block. At least one positive-probability fiber therefore has positive gap. Its reduced vertex components still obey the original graph FDs with the conditioned components supplied to the decoders.

There are exactly 19 four-factor vertex covers. Every one has factor-incidence multiplicities `2,2,1,1,1,1,1,1,1,1`, and the two multiplicity-two vertices are adjacent. The graph automorphisms preserving the ten-factor set form a group of order 4, with six cover orbits of sizes `4,4,4,4,2,1`. The six displayed sets contain one member of each orbit. Relabeling factors and graph vertices transports the reduced FD and entropy problem.

## Finite weighted witness form

For each representative, let `W` be a set of the at most `2^12=4096` mixed-alphabet words satisfying the original-neighbour pair-consistency condition. A positive-gap law on `W` exists if and only if there are nonnegative integer weights `t[i,a]`, not all zero in any row, such that

\[
\left(\sum_{w\in W}\prod_i t[i,w_i]^2\right)^3
>\prod_i\left(\sum_a t[i,a]^3\right)^2.
\]

The Gibbs variational and rational-approximation proof is the same as in `frontier-20261028-balance-polynomial-equivalence-v1.md` SHA-256 `70e90a3236d735d74dbd71f68577f97f778e98eafdc49137e30aa4fe36178ec1`, with vertex-specific alphabet sizes 2 or 4. This is an exact existence criterion, not an assertion that a witness has been found.

A pure cardinality search cannot settle this weighted case. For each four-factor cover, a graph-independent triple containing one two-bit vertex has four component bits total; the FD makes projection to its complement injective, so any uniform mixed support has at most `2^8=256` words. The bounded uniform MIP runs found size 256 and timed out; the weighted runs also timed out without a strict integer witness. These statuses are not nonexistence proofs, and a positive **nonuniform** mixed law could have at most 256 support words.

## Evidence

`frontier-20261028-mincover-orbits-check.py` SHA-256 `f07aafc507eaca1d3070da500a7c755cd89077001fabee995ae314f821c649a0`, receipt SHA-256 `b27391385dfadb3c3715e3ed49b998c14800dc6da9e8024cc4d50d5dc633f9f2`; separately written `frontier-20261028-mincover-orbits-independent.py` SHA-256 `8a5632466ad4eda93ca0f8c226611faceef715fa9c7de12212d20c6a803139c9`, receipt SHA-256 `76e88564705548ae7089f4c7a4fe41d65db7c9eb9a3d486cd026be7fa2fc1a81`, checks all 210 four-factor sets, the 19 covers, four factor-preserving permutations and the six displayed representatives. The six independent triples covering all ten graph vertices are pinned in `frontier-20261028-syndrome-hyperplane-check-result.json` SHA-256 `ddc3c58d179f9602fa9284ca87efbf3bb14ce1a9193c47c4645638064b949a57`.

The uniform proposal receipt is SHA-256 `9d75c2dd9144ea082906f3ac164ecdb99492782b6b11f8aa1da3a63c70c1c864`; the weighted proposal receipt is SHA-256 `75ab960ffad770fb491c9d6f531b878a02f342125c4b00508ded5f616544abba`. The probabilistic conditioning/embedding argument remains written mathematics, not proof-assistant formalization or independent scientific review.
