# Actual 4444 same-P profiles: complete middle exclusion and one first-profile class

**Prospective GENERAL AUTHOR candidate, nonblind and same-harness; parent disposition and independent review remain separate.** The assertions below are for one actual complex tensor, its one set of P words and its one set of E words in one product basis, with arbitrary nonzero complex E amplitudes. The two exclusions use no cut-classification lemma, q=5 assertion, phase ansatz, separate pair completions, global t bound, or global N=50 conclusion. The argument, including the binary obstruction, is written out below.

## 0. Exact hypotheses and conclusions

Let each local alphabet `X_i` have six symbols, `i∈I={1,2,3,4}`, and let `U: X_1×X_2×X_3×X_4→C` have all three balanced 36-by-36 flattenings unitary. Suppose that its support has exactly 50 words, that exactly 26 supported entries have modulus one, and that the other 24 supported entries use exactly four symbols at each party. These hypotheses hold in the stated fixed-basis AME branch after setting `U=6ψ`: balanced maximal mixing gives the three unitary flattenings. Write `P` for the 26 modulus-one words, `E` for the other 24, `Q_i` for the actual E-used alphabet at i, and `O_i=X_i\Q_i`. Thus `|Q_i|=4`, `|O_i|=2`, and `E⊂∏Q_i`.

For `k=0,…,4`, let `n_k` count the **same actual P words** with exactly k coordinates in their respective `Q_i`. Then the only moment-possible profiles are

```
r=n_4=0: (n_0,n_1,n_2,n_3,n_4)=(0,2,18,6,0),
r=n_4=1: (n_0,n_1,n_2,n_3,n_4)=(0,1,21,3,1),
r=n_4=2: (n_0,n_1,n_2,n_3,n_4)=(0,0,24,0,2).
```

Under the hypotheses, **the entire r=1 profile is impossible**. Also impossible is every r=0 configuration in which the two singleton-inside P words have their inside coordinate at the same party and use its two different degree-two E symbols. Both statements quantify over all placements and phases compatible with their stated conditions. They do not claim to exclude any other r=0 case, r=2, the whole t=26 branch, or support 50 globally.

## 1. Actual physical-pair incidence

For any unordered pair `ij`, use the corresponding pair of parties as a row index of the appropriate balanced flattening. Every row has norm one. If a P entry is in that row, it exhausts the row; its column is likewise exhausted. Therefore the 26 P pair values are distinct, are disjoint from all E pair values, and their complement consists of exactly ten E pair values. Conversely every pair value is occupied, because a zero row would violate unitarity. Each of the ten E pair values has at least two E extensions: a unique nonzero entry in that row would have modulus one and hence be in P, not E. These facts apply to each of the six physical pairs, always for the same P and E.

For `a∈Q_i` let `d_ij(a)` be the number of E neighbors of a in `Q_j`, and let `p_i(a)` be the number of P words containing a. Of the six values `(a,y)`, precisely `d_ij(a)` are E pair values and the rest are distinct P values. Thus

```
p_i(a)=6-d_ij(a),      d_ij(a)=:d_i(a) independently of j,
Σ_{a∈Q_i} d_i(a)=10.                                         (1)
```

If `d_i(a)=1`, then in each of the other three parties a has only one E neighbor, so at most one distinct E word contains a. Its occupied pair value would have only one E extension, a contradiction. Hence `d_i(a)≥2`. The four positive integral degrees sum to ten and each is at most four, so at each party the degree multiset is exactly `2224` or `2233`.

For completeness, if `s_i(a)` is the number of E words containing a and `h_i(a)=s_i(a)-2d_i(a)`, then the two-extension property gives `h_i(a)≥0`, and

```
Σ_{a∈Q_i} h_i(a)=24-2·10=4.                                (2)
```

No sharper local surplus or residual-cut classification is needed below.

## 2. Same-P moments and party and symbol identities

For a physical pair `ij`, all ten E pair values lie in `Q_i×Q_j`; hence its P cell counts in `(Q_i×Q_j, Q_i×O_j, O_i×Q_j, O_i×O_j)` are `(6,8,8,4)`. A party occurs inside in 14 P words. Double-counting inside coordinates and inside pairs gives

```
Σ_k n_k=26,        Σ_k k n_k=56,        Σ_k C(k,2)n_k=36.    (3)
```

Solving these three equations yields

```
n_1=2-3n_0-n_4,   n_2=18+3n_0+3n_4,   n_3=6-n_0-3n_4.
```

Nonnegativity of `n_1` forces `n_0=0` and `r=n_4∈{0,1,2}`, giving precisely the three displayed profiles. These are moment possibilities, not asserted realizations.

Adopt the notation correction in S1 **before** using S2: `v_i` always denotes a triple-word count, never a symbol. Let `u_i` count the P words whose unique inside coordinate is i, and let `v_i` count the P words whose unique outside coordinate is i. Write `p_ij` for the number whose inside set is exactly `{i,j}`. If `{i,j,k,l}=I`, pair incidence gives

```
p_ij=6-r-v_k-v_l,       Σ_i u_i=2-r,       Σ_i v_i=6-3r.   (4)
```

The 14 P words inside at i satisfy

```
14=u_i+Σ_{j≠i}p_ij+Σ_{j≠i}v_j+r
  =u_i+18-2r-Σ_{j≠i}v_j,
```

which, using `Σ_i v_i=6-3r`, is exactly

```
u_i+v_i=2-r  for each i.                                    (5)
```

For `a∈Q_i`, let `z_m(a)` count P words containing a and having exactly m inside coordinates, `m=1,2,3,4`. The number of P words at a is `6-d_i(a)`. For each `j≠i`, exactly `4-d_i(a)` of the Q_j values form a P pair with a. Counting these three sets of pairs using the same P words yields

```
Σ_{m=1}^4 z_m(a)=6-d_i(a),
z_2(a)+2z_3(a)+3z_4(a)=3(4-d_i(a)),
z_1(a)-z_3(a)-2z_4(a)=2(d_i(a)-3),
z_2(a)=d_i(a)-2z_1(a)+z_4(a).                              (6)
```

For degree four the first two displayed lines imply `z_1=2` and `z_2=z_3=z_4=0`. Conversely, in r=0, if both singleton words use the same actual symbol a, then `z_1(a)=2`; degree two would give `z_3=4,z_2=-2`, and degree three would give `z_3=2,z_2=-1`. Thus in r=0 degree four occurs **if and only if** both singleton words use the same symbol at the same party. In particular no second party has degree four. If the singleton words are at distinct parties, or at different symbols of one party, all parties have degree multiset `2233`.

## 3. Entire middle-profile contradiction

Assume `r=1`. There is exactly one singleton P word. A degree-four symbol would require two, so all parties have degree multiset `2233`. Let `w*` be the unique all-inside P word. At any i, if `w*_i` had degree three, then `z_4(w*_i)=1` and (6) would give `z_1(w*_i)=z_3(w*_i)+2≥2`, impossible. Thus `w*_i` has degree two. Write `b_i` for the **other degree-two symbol** at i; it is not the count `v_i`.

Let H be the unique inside party of the singleton. Equation (5) gives `v_H=0` and `v_j=1` for every `j≠H`. Consequently there are exactly three triple-inside words `T_j`, one for each `j≠H`, with `T_j` missing j. For each `j≠H`, the symbol `b_j` is neither in the singleton nor in `w*`. Equation (6) for its degree two gives `z_3(b_j)=2`. Exactly two of the three T words contain j, so both use `b_j` at j.

At H, `b_H` is not in `w*`; its degree-two instance of (6) gives `z_3(b_H)=2+z_1(b_H)≥2`, irrespective of which H symbol the singleton uses. Choose two distinct triple words `T_j,T_k` containing `b_H`; here `j,k≠H`. Let l be the fourth party, different from H, j and k. Both selected words contain l and, by the previous paragraph, both use `b_l` at l. Thus they have the same `(H,l)` pair value `(b_H,b_l)`, contradicting P-pair injectivity. This covers every r=1 placement, including either singleton-symbol boundary; no E phase or additional assumption enters.

## 4. First-profile class: the same closed binary tensor

Assume `r=0`, both singleton P words have unique inside party H, and their H symbols are the two **different degree-two** symbols `a_0,a_1`. Equation (5) gives `v_H=0` and `v_j=2` for `j≠H`: all six triple words contain H, and exactly two miss each other party. Because the singleton symbols are different, §2 shows that all parties have degree multiset `2233`.

For every `j≠H`, let `D_j` be the two degree-two symbols in `Q_j`, and let `T_j=Q_j\D_j` be the two degree-three symbols. (These `T_j` are alphabet sets, not the triple words of §3.) No singleton has its inside coordinate at j, and `r=0`. Equation (6) therefore gives `z_3=2` for every symbol in `D_j` and `z_3=0` for every symbol in `T_j`. In particular **every triple word containing j uses D_j**.

Fix `b∈{0,1}`. Since `z_1(a_b)=1`, `z_4(a_b)=0` and `d_H(a_b)=2`, equation (6) gives

```
z_3(a_b)=3,    z_2(a_b)=0.                                  (7)
```

Every one of these three triple words misses one of the three parties other than H. Fix one such j. Exactly `4-d_H(a_b)=2` inside/inside P pair values have H symbol `a_b` and j symbol in `Q_j`; pair injectivity therefore permits at most two of the three triple words to contain j. At least one misses j. This holds for each of the three j, and there are only three misses in total, so exactly one triple misses each j. The other two both contain j, have distinct `(H,j)` P values, and use symbols in `D_j`. Hence they use **both** symbols of `D_j`. Since a degree-two H symbol has exactly two E neighbors at j and the P and E pair values are disjoint, its E-neighbor set at j is exactly

```
N_E(a_b;j)=T_j     for b=0,1 and every j≠H.                (8)
```

Set `A={a_0,a_1}` and define one and the same `2×2×2×2` array

```
B = U restricted to A × ∏_{j≠H} T_j,
```

with indices in physical-party order. Zeros are allowed inside B. For any fixed j≠H, the four physical pair values in `A×T_j` are E pair values by (8), so their four rows in the `Hj|kl` flattening are mutually orthonormal and contain no P entry. By (8) at k and l, all entries in these rows lie in the four columns `T_k×T_l`. Thus the corresponding 4-by-4 flattening `B_{Hj|kl}` satisfies

```
B_{Hj|kl} B_{Hj|kl}†=I_4,  hence also B_{Hj|kl}† B_{Hj|kl}=I_4.
```

The latter identity saturates each of those full-flattening columns, so this is a **closed** block, not a hypothetical independent cut completion. Doing this for all three j uses the same B and all three balanced cuts. Its squared norm is four; `φ=B/2` is a normalized pure four-qubit state with every two-qubit reduced density matrix `I_4/4`. We now prove that such a state cannot exist.

### Binary obstruction, including all phases

Let `ρ=|φ⟩⟨φ|`. In the Pauli basis put `r_α=tr(ρ σ_α)` for `α∈{0,x,y,z}^4`, and let `A_s` be the sum of `r_α²` over strings of weight s. The two-qubit marginals being `I_4/4` imply `A_1=A_2=0`. The complement of each one-qubit subsystem has the same nonzero reduced-density spectrum, so every three-qubit marginal has purity `1/2`. Summing their four Pauli-purity identities gives

```
16 = 4 + 3A_1 + 2A_2 + A_3,   hence A_3=12.
```

Global purity gives `16=1+A_1+A_2+A_3+A_4`, so `A_4=3`. Let `Y=σ_y` and define the spin flip `ρ̃=Y^{⊗4} ρ* Y^{⊗4}` in the same local binary bases. It is positive semidefinite, and `Y σ_μ* Y=-σ_μ` for `μ=x,y,z`. Orthogonality of Pauli strings yields

```
tr(ρρ̃)=(1-A_1+A_2-A_3+A_4)/16
       =(1-12+3)/16=-1/2 < 0.
```

But `tr(ρρ̃)=⟨φ|ρ̃|φ⟩≥0`, a contradiction. Hence no B, and therefore no original U in this entire specified singleton/degree class, exists. The argument does not assume real entries or nonzero entries at all 16 positions of B.

## 5. Boundary and exact residual

For `r=2`, there are no singleton or triple words. Equation (6) gives `z_4(a)=3-d_i(a)`. Thus all parties have degrees `2233`, each degree-two symbol occurs once among the two all-inside P words, and each degree-three symbol occurs zero times there; the two all-inside words differ at every party. This is only a necessary same-P statement, not an exclusion or a construction.

After the r=0 class proved above is removed, the remaining singleton placements are, **as necessary cases, not existence claims**:

1. Both singleton words at the same H and same symbol: that symbol is degree four, H has degree multiset `2224`, and every other party has `2233`.
2. Both at the same H but at different symbols, not both degree two: the selected degrees are `2+3` or `3+3`, and all parties have `2233`.
3. The singleton words have different inside parties: all parties have `2233`; each selected symbol has degree two or three.

For these cases and for r=2, the unresolved load-bearing step is to rule out or construct one actual P/E support and one common choice of E amplitudes and phases satisfying all three physical unitary flattenings. The identities here do not assert that the listed cases are feasible. No result in this note imports the q=5 conclusions in S3, any unadopted cut assumption, or a global t26/N50 result. There is no missing load-bearing source-body import for the scoped proof above: the stated flattening-unitarity hypothesis, elementary finite-dimensional linear algebra and the displayed Pauli calculation are the complete inputs. The source citations in the packet do not authorize opening linked bodies. No independent-family, formal/kernel, human, publication, novelty, priority, or parent-acceptance claim is made.

## 6. Complete read, provenance and process declaration

Before mathematical body reading or mathematical reasoning I read the complete frozen manifest, freeze receipt, final pre-dispatch binding, live metadata supply, actual dispatch receipt, and all 22 manifest-listed status-only controls. Initial ordinary views of four administrative JSONs had collapsed blocks; complete raw displays recovered them before the prebody acknowledgment. Controls were used for status and permissions only, not as mathematical inputs. I wrote `prebody-ack-v1.md` and sent its direct acknowledgment to Main before opening the packet. The assignment's target descriptions, administrative metadata, memory summary and written-math skill were already exposed; no prior-history or private-cognition certificate is claimed.

The sole literal part was then read completely and serially in raw inclusive windows `1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–248`, including the ending. Every display was below 30,000 bytes; I observed no packet clipping requiring recovery. The part renders all of S1 LF 1–3, S2 LF 1–172, S3 LF 1–22, and S4 LF 1–33. Its parent-supplied SHA-256 is `09b46473ab0743a1cba2578e16716adc88e70441d976ac9682bd3a1f1aba413a`; the four complete paths, source pins and administrative hashes are in the manifest/receipt. Those are supplied metadata, not hashes independently recomputed by me or a source-identity certification. S1 corrects notation; S2 is a nonblind prior author candidate, not an automatic acceptance. S3 and S4 were read in full as packet context, but no q=5 or other out-of-scope conclusion from them is a premise above.

No linked or unlisted mathematical source, held episode, held proof/method/planning/selection/verification/reporting/confidence/downstream consumer, sibling science, network, external model, scientific evaluation, code execution, tests, solver, compilation, child subprocess, Git or deletion was used. No code or verifier was prepared, so there is no code hash and no computational verification. The output names were absent in directory listings before their respective writes; the available write interface does not expose an OS-level exclusive-create flag, so atomic exclusivity against an external race is not claimed. No existing candidate or frozen source was edited.
