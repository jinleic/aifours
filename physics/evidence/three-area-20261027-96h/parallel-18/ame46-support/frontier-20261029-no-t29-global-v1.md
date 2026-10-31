# No AME(4,6) state has exactly 29 maximal coefficients, regardless of its total support

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 10:14:28 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified, or novelty-cleared. The exact-t29 exclusion below is self-contained and uses no no-OLS(6), small-excess unitary classification, no-Hamming-one, SAT, or prior author outcome. No held material was used.

## 1. Exact claim and optional composition

A normalized complex AME(4,6) state in any product basis cannot have exactly **t=29** coefficients of modulus1/6, regardless of its total support N.

Combining this candidate with the separately recorded [f113 t≤29 disposition](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-maximal-coefficients29-parent-v1.md), SHA-256 `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b`, would strengthen it to t≤28. That composition retains f113's no-OLS(6) and prior-t≤30 boundaries and is **not adopted here**. The exact-t29 exclusion itself has neither import.

The new step is the full pair partition's partner-degree identity (§3), which makes the former maximum-multiplicity-three argument unnecessary. No total residual-support count is assumed.

## 2. Maximal entries partition every pair system

For each 2|2 cut, `U=6ψ` is a36×36 unitary. A coefficient of modulus1/6 exhausts its row and column norms; it is the only nonzero entry there, in every cut. Distinct maximal P words therefore share no coordinate pair. The29 P words occupy29 singleton rows and columns; E, the other support, uses the remaining `n=7` pair values, each with at least two E extensions. Singleton residual rows would themselves be maximal.

Thus for every one of the six pair systems, all36 pair values partition into29 P-carried singletons and7 E-carried values. No pair is omitted or shared between P and E.

## 3. Partner degree is independent of the other party

Fix a local E symbol a at party i and let m_i(a) be the number of P words using a. For ANY j≠i, the m_i(a) corresponding P pairs have distinct j values by P injectivity. Every one of the other `6−m_i(a)` j values must be E-carried, by the full partition. Consequently

`d_i(a):=|π_j(E_a)|=6−m_i(a)`                                     (D)

is the same for all j≠i.

This number is at least2. If it were1, each of the other three coordinates would be constant on E_a, leaving at most one E word in that fiber; its pair row would be a singleton and hence maximal, contradiction. Since the E pair projection at i,j has7 values,

`Σ_{a∈π_i(E)} d_i(a)=7`, so `|π_i(E)|≤3`.

Each pair projection has7 values, so no local alphabet can have fewer than3 symbols when every partner has at most3: `2·3<7`. Therefore **all four E alphabets have size exactly3**. This conclusion did not bound any E-pair multiplicity or |E|.

## 4. Maximal-word activity contradiction

Call a coordinate of a P word active if its value belongs to the corresponding E alphabet, and write k(x) for the number of active coordinates of x. In a fixed pair system:

- there are18 pairs with its first coordinate active; exactly7 are E-carried, so exactly11 P words are active at each party;
- there are9 active/active pairs; exactly7 are E-carried, so exactly2 P words are active at each party pair.

Hence

`Σ_{x∈P} k(x)=4·11=44`,

`Σ_{x∈P} C(k(x),2)=6·2=12`.

But `k−C(k,2)` takes the values `0,1,1,0,−2` for k=0,1,2,3,4, always at most1. Thus

`32=Σ_{x∈P}[k(x)−C(k(x),2)]≤|P|=29`,

contradiction. This proves the stated exact-t29 candidate.

## 5. Original-target use and limits

The row count `N≥72−t` holds for every AME basis. If the t≤28 composition is independently accepted, it would imply N≥44, which is weaker than the already recorded45 support bound. This is an all-support structural improvement, not by itself a support-bound improvement.

It also simplifies specific near-threshold case splits: a support47 analysis no longer needs to analyze t29's seven-row/four-excess residual once this exact-t29 exclusion is accepted. The t27 support47 branch and all N45/N46/global bound compositions remain separate review and parent decisions.

The arithmetic44−12=32 and the five per-word values are the same exact counts used in earlier bounded controls. Those controls do not replace review of the new unconditional partner-degree step. No priority, exact minimum, human review, independent-model-family review or formal proof is claimed.
