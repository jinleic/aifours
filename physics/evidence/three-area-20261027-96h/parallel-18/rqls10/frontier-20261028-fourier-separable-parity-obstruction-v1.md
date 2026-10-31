# Fourier-separable arrays of order 2p cannot be maximal and resolvable

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` before writing: **Wed Oct 28 18:01:20 PDT 2026**. The theorem is an exact ALL-L obstruction for a natural Fourier-separable construction family, for every odd prime p. It does NOT assert that an arbitrary QLS can be put in this family, and is NOT an unrestricted order-10 no-go or a novelty claim.

## 1. Exact original-object theorem

Let p be an odd prime, n=2p, and zeta a primitive n-th root of unity. For an arbitrary function `mu: Z_n -> Z_n`, consider the n×n array of ACTUAL unit vectors in C^n

`psi_(r,c)(t) = zeta^(r t + c mu(t)) / sqrt(n)`,  r,c,t in Z_n.        (1)

Allow ANY common unitary, arbitrary per-cell phases, and arbitrary permutations of the row and column labels. **Theorem:** no array of this form is simultaneously

1. a QLS(n) with row and column ONBs;
2. of maximal cardinality n² (every two distinct cells nonparallel); and
3. 1-resolvable by ANY partition of its cells into disjoint transversal ONBs.

Indeed, under the QLS and maximal-cardinality assumptions it has **no orthogonal transversal at all**. For the original n=10 this excludes the whole Fourier-graph construction family over all Latin resolutions, not merely the even-cyclic resolution or one selected permutation. The conclusion remains restricted to (1); a general QLS may be nonuniform and non-Fourier-separable.

## 2. Row feasibility forces mu to be a permutation

Every vector in (1) has norm1. For fixed column c, varying r gives the standard complete character basis, so the column is an ONB for every mu. For fixed row r, the inner product between its c and c+b vectors is

`F(0,b)/n`, where `F(a,b)=sum_(t in Z_n) zeta^(a t+b mu(t))`.

If the row is an ONB, `F(0,b)=0` for every nonzero b. Let m_j count t with mu(t)=j. The discrete Fourier inversion identity on Z_n then yields m_j=1 for every j. Thus the QLS hypothesis itself forces mu to be a permutation; we do not silently assume bijectivity of a candidate function. The argument allows all cell and basis phases and does not require a particular L.

## 3. Maximal cardinality forces all F(p,b), b odd, to be nonzero

Assume mu is a permutation. If its parity is homogeneous, meaning `mu(t)≡t+k (mod2)` for one k∈{0,1}, then for EVERY r,c,t,

`psi_(r+p,c+p)(t) = (-1)^(t+mu(t)) psi_(r,c)(t)=(-1)^k psi_(r,c)(t)`.

The distinct cells `(r,c)` and `(r+p,c+p)` have the SAME ray. Therefore maximal cardinality implies mu is NOT parity-homogeneous.

We now prove `F(p,b)!=0` for every odd b whenever mu is not parity-homogeneous.

### 3a. The b=p case

`F(p,p)=sum_t (-1)^(t+mu(t))` is a sum of 2p signs. Their product is

`(-1)^(sum_t t + sum_t mu(t))=1`,

because mu is a permutation and the exponent is twice sum_t t. Thus the number of negative signs is EVEN. A zero sum of 2p signs would need exactly p negative signs, but p is ODD. Therefore `F(p,p)!=0` for EVERY permutation mu, with no parity assumption.

### 3b. All other odd b

Define `h_j=(-1)^(mu^(-1)(j))`. It is a sequence of p plus and p minus signs, so `sum_j h_j=0`. Since zeta^p=−1,

`F(p,1)=sum_(j=0)^(2p−1)h_j zeta^j = sum_(j=0)^(p−1)(h_j-h_(j+p)) zeta^j`.

Let `v_j=h_j-h_(j+p)`, each in {−2,0,2}. If F(p,1)=0, the integer polynomial `V(X)=sum_(j=0)^(p−1)v_j X^j` is divisible over Q by the irreducible degree-(p−1) cyclotomic polynomial

`Phi_(2p)(X)=1-X+X²-...+X^(p−1)`.

Since deg V<=p−1 and Phi is monic, `V=k Phi_(2p)` for k∈{−2,0,2}. If k=0, h_(j+p)=h_j for every j, so `sum h=2 sum_(j=0)^(p−1)h_j`, twice an ODD integer; it cannot be0. Thus k=±2, forcing `h_j=epsilon*(-1)^j` for every j, with epsilon=±1. Equivalently mu preserves parity everywhere or reverses parity everywhere. Therefore a maximal-cardinality array necessarily has **F(p,1)!=0**.

For any other odd b!=p, primality of p gives gcd(b,2p)=1. The cyclotomic automorphism `zeta -> zeta^b` sends F(p,1) to F(p,b), because `zeta^(pbt)=(-1)^t` when b is odd. An automorphism cannot send a nonzero number to zero, so **F(p,b)!=0 for EVERY odd b!=p**. Together with 3a, every odd b is covered.

Only the elementary irreducibility/automorphism property of cyclotomic fields is imported. This is an all-p symbolic proof, not a finite phase grid.

## 4. Every transversal would contradict parity

Assume there is an orthogonal transversal. Because it meets each row and column exactly once, it has the form `(r,pi(r))` for a permutation pi of Z_(2p). For each of the p disjoint opposite-row pairs r and r+p, orthogonality demands

`F(p, pi(r+p)-pi(r))=0`.

By §3, the column difference cannot be odd. Thus the two column values in EACH opposite-row pair have the SAME parity. These p disjoint pairs partition all2p columns. But there are exactly p even column values and p is odd; a union of monochromatic pairs cannot contain an odd number of even values. Contradiction.

This excludes ANY orthogonal transversal under maximal cardinality, hence ANY possible 1-resolution. It is stronger than ruling out the particular cyclic-transversal construction but remains a theorem only for the Fourier-separable family (1). A row/column relabelling merely relabels the permutation pi; common unitary and cell phases preserve all orthogonality/ray relations.

## 5. Independent bounded checks and exhaustive restricted-family scan

The checker `frontier-20261028-fourier-parity-check-v1.py`, SHA256 **a5ce4541726ad469ca61737cc837060f44f0a329cfb96918a5a67adef3ab657f**, independently constructs Phi_10 by exact integer polynomial division and checks all252 possible five-plus/five-minus h-patterns. Its actual output at18:00:59:

```text
5+ / 5- sign patterns 252 exact Fourier zeros 2 both parity-homogeneous: PASS
mu(0)=0 permutations 362880 parity-homogeneous 2880
F(5,5) exact nonzero histogram {-6: 14400, -2: 115200, 2: 172800, 6: 57600, 10: 2880}
pi(0)=0 permutations admitting five monochromatic opposite-row pairs 0
PASS finite corroboration; ALL-p theorem rests on independent written proof
```

The independent analytical proof is §§2–4; these finite checks are corroboration, not the proof for arbitrary p. `mu(0)=0` is a computational gauge: subtracting mu(0) multiplies each cell vector by a c-dependent unit phase, preserving all rays. Likewise `pi(0)=0` follows by translating all selected column labels and preserves its pair-difference constraints. The written theorem does not rely on either normalization.

An earlier separately written exact restricted-family search `frontier-20261028-fourier-graph-search-v1.cpp`, SHA **4f284e6c89d5ed691dd82bb817b8992454dd34f075b8b0a4c26c458c776e56cf**, evaluated all362880 normalized mu permutations, rejected2940 as already having a detected repeat and357460 with an empty necessary Fourier-zero difference row, then exhaustively backtracked the remaining2480 possible transversals with **zero truncated cases** and **no candidate**. Its complete result `frontier-20261028-fourier-graph-result-v1.json` SHA **edf5390ec19c4407aea018ba55273e645289bdc3b152d676c70747196aa8c1c3**. This exhaustive computation is restricted to (1) and is not a general QLS search; the parity proof above is independent of that enumeration.

Why one transversal suffices for this restricted search: its Gram inner products depend only on `(r-s,c-d)`, so translating an orthogonal transversal `(r,pi(r))` by every column shift yields ten disjoint transversal ONBs. The no-transversal theorem is stronger and does not require relying on this construction. A separate exact original-definition verifier `frontier-20261028-fourier-qls-verify-v1.py` SHA **8487ef00bb519b710fa4ace11ba54c1f94cd5abc66683701e951b721d8527e32** was prepared; because the search recorded no candidate, it truthfully reported “no candidate recorded; no QLS witness to verify.”

## 6. Remaining frontier

This rules out a whole *physical-vector construction family* for order10 and for every order2p with p odd prime. It neither rules out unrelated phase structures/Latin incidences in a different ansatz, nor shows that all maximal QLS are Fourier-separable. The validated13-ray Parker array and other nonuniform possibilities are not contradicted. A true original result still requires a100-ray actual array with all30 ONBs, or an obstruction over ALL complex arrays and ALL resolutions.

Cyclotomic identities, parity proof, code and scope need independent review before adoption. No claim of novelty, formal/kernel or external-model verification; no held historical result is a premise.

**END — all-resolution Fourier-separable parity obstruction, not unrestricted QLS10 closure.**
