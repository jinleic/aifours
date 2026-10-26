# Addendum 1: a written root-of-unity proof after the HOLD correction

Observed before creation: **Sun Oct 25 04:13:21 PDT 2026** (`/bin/date`). MathShor, math-5. **WRITTEN only.** No scientific eval/interpreter, enumeration, symbolic/numerical program, certificate replay or solver was run after the parent's corrective message. Metadata clocks/hashes only.

This is additive to `proof-HETEROGENEOUS-PURE-RUN-AND-ONE-GAP-v1.md`, SHA-256 `38328e19b46a88f524b7af2b51654b9d6bf8e7dcf62cba1bdfdd5ce2350cba7f`. That packet and its observed arithmetic JSON remain unchanged. The separate `parent-HOLD-correction-disclosure-v1.json` identifies all eight prior eval calls and withdraws the erroneous automatic-admission/verification implication. The erroneous permission originated with the parent; no retrospective GO is asserted.

The purpose here is mathematical rather than administrative: replace the five-term mask's dependence on the 36 evaluated polynomial remainders by a direct, finite, written proof. The result remains the SAME RESTRICTED endpoint-support obstruction, not unrestricted Shor noncompletion or an existence-changing discovery. No new support cutoff is proposed.

## 1. Exact claim and named classical algebra imports

Let

```text
P(z)=1+z^3+z^8+z^11+z^19.
```

**Claim.** P has no root of unity.

Only elementary cyclotomic-field facts are imported:

- a primitive m-th root has minimal polynomial `Phi_m` over Q and degree `phi(m)`;
- if `p^2 divides m`, then `Q(zeta_m)` has degree p over `Q(zeta_(m/p))`;
- if m is squarefree and `p divides m`, then `Phi_p` remains the degree-(p-1) minimal polynomial of a primitive p-th root over `Q(zeta_(m/p))`, since p and m/p are coprime.

These are named classical field-degree statements, not newly authenticated source theorems or formal proofs. Their standard degree ratios follow from the cyclotomic degree formula; no Szabo, Redei, code-realization or computational theorem is used.

Suppose for contradiction that zeta is primitive of order m and

```text
1+zeta^3+zeta^8+zeta^11+zeta^19=0.                (A)
```

We treat a minimal five-term relation and a decomposable relation separately. “Minimal” means no nonempty proper SUBSET of these five indexed terms sums to zero, retaining repeated values if powers happen to coincide.

## 2. A minimal five-term relation forces m to divide 30

First suppose `p^2 divides m`. Set `K=Q(zeta^p)`. The basis

```text
1,zeta,...,zeta^(p-1)
```

is linearly independent over K. Group the five terms in A by their exponents modulo p. Each group coefficient over K must be zero. Minimality therefore forces all five indexed terms into ONE residue class. Since exponent 0 occurs, every exponent would be divisible by p. But 3 and 8 are relatively prime. Contradiction. Thus m is squarefree.

Now suppose an odd prime `p>=7` divides this squarefree m. Put `K=Q(zeta_(m/p))` and write zeta as a product of a K-root of unity and a power of a primitive p-th root omega, with that power coprime to p. Group A by the omega exponent. It becomes

```text
A_0+A_1 omega+...+A_(p-1) omega^(p-1)=0,       A_j in K.
```

There are only five terms and p>=7, so at least one coefficient is an empty group, hence zero. The degree-(p-1) minimal polynomial of omega over K is `1+...+x^(p-1)`. Thus all the A_j must be equal; the empty one makes them all zero. Minimality again forces every original term into one group, so all exponent differences are divisible by p. The exponents include 0,3,8, which makes this impossible.

Consequently m is squarefree and has no prime divisor other than 2,3,5. Hence

```text
m in {1,2,3,5,6,10,15,30}.                     (B)
```

This is a written special-case proof of the needed small-conductor reduction; a general theorem about short vanishing sums is not assumed.

## 3. Eight explicit written reductions exclude the minimal case

For the orders in B, the following identities at a primitive zeta are immediate from the displayed cyclotomic relations. They are ordinary written algebra, not a replay of the earlier table.

- **m=1:** `P(1)=5`.
- **m=2:** `P(-1)=-1`.
- **m=3:** using `1+zeta+zeta^2=0`, the residues give `P(zeta)=2+zeta+2zeta^2=-zeta`, nonzero.
- **m=5:** the residue expression is `1+zeta+2zeta^3+zeta^4`. Subtracting `1+zeta+zeta^2+zeta^3+zeta^4=0` leaves `zeta^3-zeta^2=zeta^2(zeta-1)`, nonzero.
- **m=6:** `zeta^3=-1`, `zeta^5=1-zeta`, and `zeta^2=zeta-1`. Hence `P(zeta)=zeta^2+zeta^5+zeta=zeta`, nonzero.
- **m=10:** using `zeta^5=-1`, first obtain `P(zeta)=1+zeta-zeta^4`. The relation `Phi_10=z^4-z^3+z^2-z+1` reduces this to `2+zeta^2-zeta^3`. It is a nonzero polynomial of degree 3, smaller than the minimal degree 4, so cannot vanish.
- **m=15:** `zeta^10=-zeta^5-1`, hence `zeta^11=-zeta^6-zeta`. Also

  ```text
  Phi_15(z)=z^8-z^7+z^5-z^4+z^3-z+1.
  ```

  Reduce `zeta^19` to `zeta^4` and use these relations. The result is

  ```text
  P(zeta)=zeta^7-zeta^6-zeta^5+2zeta^4,
  ```

  a nonzero polynomial of degree 7, below the minimal degree 8.
- **m=30:** put `eta=-zeta`, which is primitive of order 15. Then

  ```text
  P(zeta)=1-eta^3+eta^8-eta^11-eta^4
         =eta^7+eta^6-eta^5-2eta^3+2eta.
  ```

  The second equality uses precisely the order-15 relations just displayed. Again the polynomial is nonzero of degree 7, below eta's minimal degree 8.

Thus A cannot be a minimal five-term relation.

## 4. A decomposable relation would be an impossible pair plus triangle

If A is not minimal, a proper zero subsum cannot have one term. A zero subsum of four terms would leave a single nonzero unit root summing to zero, impossible. A proper zero subsum of two or three terms therefore partitions A into an opposite pair and a zero-sum triple.

Three unit complex numbers sum to zero only when, after common scaling, they are the three cube roots of unity. One elementary proof: write `1+u+v=0` with both u,v of modulus 1; then `|1+u|=1` forces `Re(u)=-1/2`, giving the two primitive cube roots. Thus for a triple of exponents a,b,c, both `zeta^(b-a)` and `zeta^(c-a)` have order 3.

For completeness, the gcds of the two positive differences from the smallest member of each possible triple are:

| Triple | gcd of differences |
|---|---:|
| 0,3,8 | 1 |
| 0,3,11 | 1 |
| 0,3,19 | 1 |
| 0,8,11 | 1 |
| 0,8,19 | 1 |
| 0,11,19 | 1 |
| 3,8,11 | 1 |
| 3,8,19 | 1 |
| 3,11,19 | 8 |
| 8,11,19 | 1 |

If this gcd is 1, the order m divides 3 by the two order-three conditions. It cannot be 1, so it is 3. An order-three root has no power equal to -1, so the complementary pair cannot be opposite.

For the sole exceptional triple `{3,11,19}`, its successive difference is 8, so `zeta^8` must be a primitive cube root. The complementary pair has exponents `{0,8}` and would instead require `zeta^8=-1`. Contradiction.

Every partition is excluded. This proves that P has no root of unity, without any arithmetic interpreter or enumerated cyclotomic remainder certificate.

## 5. Written reconstruction of the restricted code obstruction

Retain the original packet's WRITTEN pure-run argument:

```text
L R+(1-z^n)H=S_n,
L R=S_n modulo z^n-1,
```

where L records pure-start a-exponents and R pure-end a-exponents, both with the empty endpoint 0. The code itself still contains no empty word. This derivation uses the accepted raw GP theorem and exact word-delay classification, not the prior scientific computations.

The small-end exclusion can also be read directly as literal word identities. For each `s in {1,2,4,6,7,12,13,14}`, the original packet displays actual `p_s,p_s a^s` in C. For each `i in {0,3,8,11}`, `a^i b` is in C. A proposed `a^(i+s)b^beta` contradicts UD via

```text
(p_s a^s)(a^i b)(b)^(beta-1) = (p_s)(a^(i+s)b^beta),
```

for EVERY beta>=1. The following handwritten witness choices cover every excluded exponent through 25:

```text
1=0+1,   2=0+2,   4=0+4,   5=3+2,   6=0+6,
7=0+7,   9=3+6,  10=3+7,  12=0+12, 13=0+13,
14=0+14,15=3+12, 16=3+13, 17=3+14, 18=11+7,
20=8+12,21=8+13, 22=8+14, 23=11+12,24=11+13,25=11+14.
```

The first summand is always an actual base exponent i; the second is a displayed actual residual s. If pure-end support were capped at25, the only possibilities for R would therefore be the four-term mask or P, just as in the original packet. The four-term case is excluded by its explicitly written signed-multiplier identity

```text
(1+z^3+z^8+z^11)(1-z^3+z^6)=1+z^8+z^9+z^17,
```

because the forced L residues13 and14 make the coefficient at22 at least2 instead of1.

For the five-term case, the new written proof in Sections1-4 makes P invertible in `Q[z]/(z^n-1)` for EVERY n. The unique solution of `L P=S_n` would be `L=S_n/5`, contradicting its 0/1 coefficients and constant coefficient1. Thus the restricted structural conclusion is now supported by this direct written chain:

```text
Every finite UD factor-complete extension contains
an actual a^ell b^beta with ell>=26, beta>=1.
```

No credit from the earlier 36 evaluated remainders is needed for this conclusion. The conclusion is still only a forced escape from the specified small pure-end support, not noncompletion at larger support.

## 6. Current assurance and exact open gap

The earlier arithmetic outputs remain preserved observations performed under erroneous parent permission, with no retroactive admission or independent verification credit. This new addendum supplies a WRITTEN replacement proof; its field-degree imports, minimal-subsum argument and handwritten reductions need independent written reconstruction. No such review or formal verification is claimed.

The unrestricted problem remains NOT_PROVED. No finite global M, universal multi-positive-gap invariant, or contradiction covering all larger endpoint supports has been obtained. PR and every HG_g still leave the real many-positive-gap coherence problem; the original packet's explicit K0 control remains a written warning against promoting those solved subsystems. No automatic critical-gap iteration, seed enlargement, native computation, source-only-to-science relabeling or deadline reset is authorized.
