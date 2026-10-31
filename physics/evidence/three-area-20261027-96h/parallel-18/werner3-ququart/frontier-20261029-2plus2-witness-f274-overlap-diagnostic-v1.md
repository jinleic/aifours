# Additive symbolic diagnostic: one both-square-nonnormal subfamily is already f274-certified

**WRITTEN, owner candidate, UNREVIEWED.** This discloses a fresh post-packet diagnostic, not a physical q-value, a numerical instance, a new T2 theorem, or an edit to `frontier-20261029-d4-t2-arbitrary-2plus2-blocks-v1.md` (SHA-256 bb09c6bf442b9d497241297c57f9da678b559b5d13ee56cc871de4a6fc7f1473). It uses symbolic `t>0`, elementary matrix identities, and f274's written compound criterion. The whole 2+2 class remains the candidate's scope. The certificate membership of other members is not decided.

## Claim and scope

Set `A(t)=B(t)=(t I2+E12)⊕(−t I2)` for arbitrary real `t>0`, `X=A⊗I+I⊗B`, `L=2+8t²`, and `H=X†X`. Then **in the displayed reducing product basis itself**, the f274 modulus compound satisfies

`ρ(|H^[2]|)<2L=4+16t²`.

Thus this specific symbolic both-square-nonnormal family is ALREADY inside f274's strict sufficient region; it is not evidence that the new 2+2 theorem reaches outside that region. No assertion about all parameter choices of the manuscript's larger `α,c,β,d` family or about `η` necessity follows.

## Decomposition

The four 4-dimensional sectors of `X` are

`X11=2t I4+E12⊗I2+I2⊗E12`, `X12=E12⊗I2`, `X21=I2⊗E12`, `X22=−2t I4`.

In the natural basis of the first sector,

```
H11 = [[4t²,   2t,   2t,       0],
       [ 2t, 1+4t²,  1,      2t],
       [ 2t,   1,  1+4t²,     2t],
       [  0,   2t,   2t,  2+4t²]].
```

The other three `H` sectors are diagonal, with diagonal values among `0,1,4t²`. The support graph of `H` therefore has one four-vertex component `H11` and twelve singletons. The second compound decomposes into: (i) two-particle pairs inside `H11`; (ii) one vertex in `H11` and one singleton; and (iii) pairs of singletons. In (ii), after a signed basis permutation, `|H^[2]|` is `H11+h I4`, because `H11` is entrywise nonnegative and `h≥0`; its Perron value is `ρ(H11)+h`. In (iii) the value is a diagonal sum of singleton weights.

Let `g=max(1,4t²)`. The maximum row sum gives `ρ(H11)≤2+4t²+4t`. Both possible singleton maxima are strictly safe, since

`4+16t²−(3+4t²+4t) = 12(t−1/6)²+2/3 > 0`,

`4+16t²−(2+8t²+4t) = 8(t−1/4)²+3/2 > 0`.

Thus every mixed component has Perron value `<2L`. Two singleton weights sum to at most `2g<4+16t²` as well.

## The six-dimensional same-component compound

Order the pair basis by `12,13,14,23,24,34`. The off-diagonal support is invariant under swapping `12↔13` and simultaneously `24↔34`; `14` and `23` have identical couplings to the symmetric states. Since `t>0`, the nonnegative modulus compound is irreducible and its Perron vector is invariant under these swaps. On the symmetric subspace, after removing the common diagonal `8t² I`, its Perron value is the largest eigenvalue of

```
M = [[ 2, 4t,  0],
     [4t,  2, 4t],
     [ 0, 4t,  4]].
```

Put `λ=4+8t²`. Sylvester's criterion for `λI−M` applies because its leading principal minors are

`2+8t²`, `4+16t²+64t⁴`, `512t⁶`,

all strictly positive. Hence `λmax(M)<4+8t²`, and the full six-dimensional compound block has Perron value `<8t²+(4+8t²)=2L`. This and the mixed/singleton cases prove the claim.

## Boundaries

This is a manually derived symbolic diagnostic, disclosed because it bears directly on the requested f274-complement comparison. It does not prove the entire new class is certificate-covered or certificate-uncovered, and it does not settle the original T2 complement, T3, Z2, q3, source correctness, novelty, or any held process. It does not use the false f198 arbitrary-T estimate or any code, selected physical q-value, numerical search, or withdrawn guidance.
