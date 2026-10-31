# Independent same-harness review: circular Tuscan regular obstruction

Native `/bin/date` observed before writing: **2026-10-28T19:15:38-0700 PDT**.

## Scope, pin, and verdict

Binding assignment: `manifest-v1.json`; no higher manifest version was present when checked. The sole input, `information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/frontier-20261028-circular-regular-obstruction-v1.md`, had the manifest's SHA-256 `72af4fbaec5ac9bfd019327373ce0a7ced5e8d36f4c6dcba23feec1c92e76026`, 4,905 bytes and 25 LF. I hash-checked it before reading and read LF 1–25 completely, in order, in a raw window. **Input pin mismatches: 0.** Citations below are to that pinned candidate, not to an amended version.

**Candidate verdict: FATAL 1, MAJOR 1, MINOR 0.** The literal all-odd-n statement is false at n=1, and its proof misstates a load-bearing group theorem. The n=11 circular-to-linear implication and n=11 prime-order restriction have no identified mathematical defect. The regular obstruction is independently supported for **odd n≥3**, with the repaired group argument below; this is not acceptance of the frozen all-odd-n claim. There is also the separately disclosed source-access process deviation below, not counted as a mathematical finding.

## Findings

### FATAL 1 — n=1 violates the stated universal obstruction (candidate LF 7, 9–11, 13, 19)

Under the candidate's explicit definition at LF 7, take n=1, symbols Z/2, and the sole directed cyclic row `(0,1)`. At distance 1 the two ordered pairs of distinct symbols `(0,1)` and `(1,0)` each occur once. At distance 2 the events are `(0,0)` and `(1,1)`, so every ordered pair of **distinct** symbols occurs zero times, satisfying the given at-most-once condition. The regular C2 action by addition sends `(0,1)` to the rotation `(1,0)`, so it preserves the row. This is a literal counterexample to LF 19's “for every odd n” conclusion.

The counting step at LF 7 implicitly treats all distance-2 events as pairs of distinct symbols, and hence the analogous distance-2 exact-cover step at LF 13 fails when N=2. For N≥3 those events do have distinct endpoints. A repair is to state the counting lemma for n≥2 and the odd-n obstruction for **n≥3**. If an independently specified convention excludes n=1, this becomes a missing explicit domain qualification rather than a counterexample under that different convention; no such restriction is present in the pinned definition. The n=11 application is unaffected.

### MAJOR 1 — the normal-complement import is misstated (candidate LF 15)

The parenthetical claims that a cyclic Sylow p-subgroup entails an abelian normalizer and a normal p-complement. As a statement for general p this is false: for H=S3 and p=3, P=A3 is cyclic, `N_H(P)=S3` is nonabelian, and no subgroup of order 2 is normal, so there is no normal 3-complement. The alleged abelianness of the normalizer can fail even for the intended p=2: `H=C2 × (C7 ⋊ C3)` with the C3 generator acting by multiplication by 2 on C7 has central Sylow P=C2, but `N_H(P)=H` is nonabelian. The checker explicitly verifies both finite examples.

This is a defect in the cited load-bearing justification, **not** a counterexample to the intended p=2 conclusion. Correct it by stating the actual sufficient hypothesis `P≤Z(N_H(P))` for the normal-complement theorem and proving that hypothesis for cyclic P of 2-power order; alternatively use the self-contained transfer derivation below. Merely asserting that the normalizer is abelian does not establish it. The general Burnside theorem as quoted is not used as an import in this review.

## Independent reconstruction of the repaired obstruction

Assume odd n≥3 and N=n+1. Since N≥4, distance-1 and distance-2 endpoints are distinct. There are N(N−1) events at each distance and N(N−1) possible distinct ordered pairs, so at-most-once gives an exact cover at each distance.

For an H-orbit of directed cyclic rows let S be one row's stabilizer and let `s=[H:S]`. S embeds in the cyclic rotation group, hence is cyclic. Its rotations are by multiples of s, so the left differences `δ_i=x_i^(-1)x_(i+1)` and `ε_i=x_i^(-1)x_(i+2)=δ_iδ_(i+1)` are s-periodic. For each i modulo s, the corresponding starting points in the base row form `S x_i`. The s row translates indexed by left cosets `gS` give disjoint sets `gS x_i` which partition H. Thus the i-th period difference contributes every ordered arc with that left difference exactly once. Exact cover consequently requires, across row orbits, both period-difference multisets to equal `H\{e}`.

The orbit sizes sum to odd n. Some s is odd; its cyclic stabilizer S therefore contains a Sylow 2-subgroup P of H, and P is cyclic. Write `|H|=2^k m`, m odd. The following proves the special group fact needed, without relying on the erroneous general-p parenthetical.

1. The conjugation image `N_H(P)/C_H(P)` has order dividing `|Aut(C_(2^k))|=2^(k−1)`. It also has odd order because P lies in its centralizer and `[N_H(P):P]` is odd. It is therefore trivial: `N_H(P)=C_H(P)`. This says **P is central in its normalizer**, not that the normalizer is abelian.
2. Let T be representatives for the right coset space `P\H`. For h in H let `t_h` represent `Pth` and define `V(h)=∏_(t in T) t h t_h^(-1)` in P. Every factor is in P, which is abelian; reindexing by the right action on `P\H` gives `V(hh')=V(h)V(h')`.
3. Let x generate P. The right action of x on `P\H` has an odd number of fixed cosets, because the total `m` is odd and all other orbits have even length. A fixed coset representative t has `t x t^(-1)` a generator of P, so t normalizes P and hence centralizes it; that orbit contributes x to V(x). An orbit of even length ℓ contributes `t x^ℓ t^(-1)` in P, whose order divides `2^(k−1)`, hence lies in P². Thus `V(x)≡x (mod P²)`, so V(x) generates P. V is onto P; its kernel is a normal subgroup of order m, and `H/ker(V)≅C_(2^k)`.

Let `φ:H→Z/(2^k)` be this quotient map. Its nonidentity-element sum is

`∑_(h≠e) φ(h) = m ∑_(j=0)^(2^k−1) j ≡ 2^(k−1) (mod 2^k)`,

since m is odd. On each period the shifted δ list is the same list, so `∑φ(ε_i)=2∑φ(δ_i)`. If both exact covers held, the same ε sum would be both `2·2^(k−1)=0` and `2^(k−1)` modulo `2^k`, a contradiction. This establishes the **repaired** odd-n≥3 assertion, including n=11; the exact-checker evidence below is supplementary and is not the proof of the all-variable claim.

For completeness on the order-12 parenthesis at LF 19: Sylow counting gives either one or four Sylow-3 subgroups. If one, H is a semidirect product of its normal C3 with a Sylow-2 subgroup C4 or V4, with trivial or nontrivial action into Aut(C3)=C2: the resulting types are C12, C6×C2, Dic3, and D12 (order 12). If four, the eight nonidentity order-3 elements leave a unique normal Sylow-2 subgroup; it must be V4 and the nontrivial C3 action gives A4. Thus the listed five isomorphism types are covered; the noncyclic Sylow-2 types already fail the odd-orbit argument.

## Own exact small-instance verification

`review-check-v1.py` is my independent standard-library checker, not an author replay. It enumerates every directed circular row through 0 for C4, all row orbits under regular translation, and all ordered arcs in each orbit. Its complete result is in `review-check-v1.out`; execution exited 0. The three C4 orbits are:

| representative | orbit size | period D1 | period D2 | projected sums mod 4 |
|---|---:|---|---|---|
| `(0,1,2,3)` | 1 | `[1]` | `[2]` | 1, 2 |
| `(0,1,3,2)` | 4 | `[1,2,3,2]` | `[3,1,1,3]` | 0, 0 |
| `(0,3,2,1)` | 1 | `[3]` | `[2]` | 3, 2 |

The checker verifies the D2=D1-plus-shift identity on every period and the full-arc multiplicities, not just their aggregate counts. Hypothetically a D1 exact cover would give sum `1+2+3=2 (mod 4)`; doubling forces the D2 sum to 0, while a D2 exact cover would require 2. In fact these particular C4 orbits have no union of three rows at all, so this is explicitly a conditional verification of the difference-sum contradiction, not a claimed example of a D1-covering three-row array.

As a noncommutative control, the checker enumerates all 120 directed six-symbol rows in S3, their 26 orbits (3 of size 2, 8 of size 3, 15 of size 6), and checks the product identity, per-arc multiplicities and projected sums in every orbit. It also computes the elementary transfer homomorphism for C4, S3, the 42-element group above, and Dic3 of order 12; in Dic3 the Sylow C4 has a normal transfer kernel of order 3 and the nonidentity image sum is 2 mod 4. The checker directly verifies the n=1 edge case and the S3/H42 counterexamples in the findings.

Checker SHA-256: `f34aede8705b53027185242064da575adacc8c293a183719948959568f85bc3a`. Receipt SHA-256: `7600411080ccf0df11e8c10350f4e921e29093e5f1d3a995eca8f7d6127bb3cd`.

## Remaining n=11 claims

* **Circular ⇒ linear (LF 7):** after deleting ∗, each linear row contains each of the other 11 symbols exactly once; every linear event at either distance is a corresponding circular event. The at-most-once property survives deletion. This supports the implication, not existence of its premise or a claim of necessity.
* **Prime-order symmetry (LF 23):** a nontrivial symbol permutation fixing a directed cyclic row acts as a nonzero rotation, hence has no fixed symbol. If a prime-order symmetry fixes any symbol, it fixes no row, so its row orbits all have size p and p divides 11. For p=11 there is one fixed symbol ∞ and the rows form one orbit. Identify the remaining symbols with Z11; in a base row, its ten arcs not incident to ∞ must have ten different nonzero differences, else their 11 translates repeat an ordered arc. They are all of Z11\{0}, whose sum is 0. But their sum telescopes to the difference of the distinct endpoints of that 10-edge chain, which is nonzero. Hence no prime-order symmetry fixes a symbol. A fixed-point-free prime-order permutation of 12 points has p∈{2,3}. The count of fixed rows is congruent to 11 modulo p. These statements do not establish that either remaining type exists.

## Process, imports, and non-claims

**Source-access deviation:** I directly fetched `https://en.wikipedia.org/wiki/Cyclic_group`, a secondary source, contrary to this assignment's primary-sources-only restriction. It is not used as evidence for any statement above. A separate attempted read of `https://en.wikipedia.org/wiki/Burnside%27s_normal_p-complement_theorem` returned HTTP 404 and provided no theorem text. Main was notified and recorded this as a process/source-scope deviation, not a mathematical finding or an external-model transmission. No held, withdrawn, or quarantined body was read for this review.

The candidate's named Burnside normal-p-complement theorem is **not independently sourced in its general form** and, as stated there for cyclic Sylow p-subgroups, is false. The needed p=2 instance was instead derived above from an explicit transfer map; standard elementary group facts used include Sylow's theorem, Lagrange/orbit-stabilizer, cyclic-group automorphisms and the first isomorphism theorem. No primary-source prior-art/novelty audit was made. No SAT solver or SAT artifact was inspected or run: **no SAT, UNSAT, timeout, completion, or other SAT status is asserted**, including for the bounded order-3 checks mentioned at LF 25. This review does not decide T2(11), construct an 11-square or circular array, rule out asymmetric or nonregular arrays, prove existence of the remaining symmetry types, or claim necessity of circularity. It is same-harness review, not an external-family, human, formal, or novelty verification.

**Output-creation note:** The initial exclusive-create reserved `review-v1.md` as a zero-byte file, but template formatting raised `KeyError` before any content was written. After confirming the reservation remained empty, the review body was populated once with a fresh native clock; no previously frozen review content was edited.
