# A one-auxiliary defect inequality and a seven-dimensional syndrome-cylinder obstruction

## Required inputs and status

Read the four historical corrections first: `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md`; `frontier-20261028-mixed-plane-symmetry-erratum-v1.md`; `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md`; `frontier-20261029-primal-checker-subset-coverage-erratum-v1.json`. Their complete bodies precede this manuscript in the prospective small proof packet.

**WRITTEN candidate mathematics; one 1008-row integer identity independently implemented and checked in the existing owner eval kernel.** The component/fiber application below awaits scientific review. No formal proof, novelty clearance, unrestricted guessing-number bound or adoption is claimed. The 1,811,001-row affine-plane archive is immutable and was NOT replayed. No affine-plane entropy theorem, two-syndrome theorem, held f161/f162 consumer, reviewer return, DFZ inequality or copy program is an input.

## 1. Literal graph and alphabet-free inequality

Let V={1,...,10}, with neighborhoods

```
1: 2,3,4,5,6,7       2: 1,3,7,9,10
3: 1,2,4,8,9         4: 1,3,5,8,10
5: 1,4,6,9,10        6: 1,5,7,8,9
7: 1,2,6,8,10        8: 3,4,6,7,9,10
9: 2,3,5,6,8        10: 2,4,5,7,8
```

This is the literal 26-edge R-minus graph transcribed from Fig.2, printed p570, of the Gurpinar 2024 publisher PDF, SHA256 `373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8`. Edge3-4 is present and9-10 absent. The inequality itself is about the displayed sets, regardless of this graph-name identification.

For ANY finite variables X1,...,X10,U, define

```
Delta = H(X_V) - (2/3) sum_v H(X_v)
F_v = H(X_v | X_(N(v)))
D_6 = H(X_6 | X_{5,7,8,9}, U)
D_7 = H(X_7 | X_{2,6,8,10}, U)
E_9 = H(U | X_{2,3,5,6,8})
E_10 = H(U | X_{2,4,5,7,8}).
```

**Lemma (unconditional ordinary-Shannon inequality).**

```
18 Delta <= 6 sum_(v notin {6,7}) F_v + 5(F_6+F_7)
            + D_6 + D_7 + E_9 + E_10.                  (A)
```

No FD, binary variable, cardinality cap, linearity or component representation is assumed in (A). In particular, for an original-neighbor FD law,

```
18 Delta <= D_6+D_7+E_9+E_10.                          (B)
```

**Exact proof of (A).** On the 2047 nonempty entropy coordinates of the eleven variables (U is bit10), the supplied certificate gives

```
113 * [RHS(A) - 18 Delta]
     = sum_r lambda_r I_r,
```

where the 1008 strictly positive integer lambda_r and every literal row vector are included. There are1006 ordinary CMIs and2 conditional entropies. Each I_r is nonnegative. The independent checker rebuilds every row from its CE/CMI descriptor and separately rebuilds RHS(A)-18Delta from the displayed sets; all2047 coefficients agree exactly. It imports no producer, old checker, scientific library or theorem. It rejects changed target, flipped multiplier, altered literal row vector, deleted graph edge and dropped row controls. Thus the mathematical import is only ordinary finite-variable Shannon nonnegativity and the complete integer identity, not an author's PASS flag.

The originating discovery projected a fresh four-state certificate to one auxiliary and averaged a vertex swap. That discovery history is NOT a logical dependency: the new integer certificate is independently checkable for arbitrary U.

## 2. Actual triangle encoding over a finite abelian group

Let G be a finite abelian group of size d>=2. Use the ordered triangle factors

```
T1=123, T2=145, T3=167, T4=239, T5=2-7-10,
T6=389, T7=4-5-10, T8=4-8-10, T9=569, T10=678.
```

There is one G-valued component x_v^t at each triangle occurrence. Each X_v is its three incident components, so the alphabet is G^3, size d^3. Define sigma_t=sum_(v in Tt) x_v^t in G. Let the law obey the ORIGINAL graph FDs H(X_v|X_N(v))=0.

No smaller-neighborhood FD is inferred from those graph FDs. Every smaller local decoder below is established by solving the actual group-sum equation for its missing component.

Put C=(x_1^3,x_6^3,x_7^3), the COMPLETE tuple of factor3, and let Y_v be X_v with its factor3 component omitted if v belongs to T3. In a positive-probability C-fiber, omitted components are constants. Therefore the Y law still has the original graph FDs: supply those constants to the original decoders.

Take U=(sigma_5,sigma_9,sigma_10) in that fiber. Knowing U and Y_{5,7,8,9} solves the two remaining components at vertex6 (factors9 and10). Hence D6=0 for the Y law. Knowing U and Y_{2,6,8,10} solves vertex7's factors5 and10, hence D7=0.

The original-neighbor tuple at vertex9 recovers Y9 and already contains the other components of factor9. It therefore determines sigma9. Similarly the original-neighbor tuple at vertex10 determines sigma5. Consequently

```
E9 <= H(sigma5,sigma10 | sigma9,C)
E10 <= H(sigma9,sigma10 | sigma5,C)
```

after averaging the fiber inequalities. Applying (B) proves

```
18 Delta(Y | C)
 <= H(sigma5,sigma10 | sigma9,C)
    + H(sigma9,sigma10 | sigma5,C).                     (C)
```

Here Delta(Y|C) means H(Y_V|C)-(2/3)sum_v H(Y_v|C). No assumption that the full syndrome is determined by U is made; six other factor parities are unrestricted.

## 3. Fixed-factor lifting and quantitative conclusion

Assume sigma3 is constant. Every pair of components of C determines the third. Three pairwise entropy subadditivity inequalities give

```
3 H(C) <= 2 [H(x_1^3)+H(x_6^3)+H(x_7^3)].
```

Write C_v for the factor3 component at vertices1,6,7 and a constant at the other vertices. Since X_v=(C_v,Y_v),

```
H(X_V) = H(C)+H(Y_V|C)
H(X_v) = H(C_v)+H(Y_v|C_v)
       >= H(C_v)+H(Y_v|C).
```

Therefore Delta(X)<=Delta(C_vertex_blocks)+Delta(Y|C)<=Delta(Y|C). Combining with (C) proves the following candidate quantitative theorem:

**If sigma3 is constant, then every actual component FD law satisfies**

```
18 Delta(X)
 <= H(sigma5,sigma10 | sigma9,C)
    + H(sigma9,sigma10 | sigma5,C).                     (D)
```

In particular Delta(X)<=0 whenever BOTH conditional entropies on the right vanish. This permits conditional nonlinear relationships depending on C; it is not merely a claim about an affine syndrome support.

## 4. A d^7-syndrome cylinder, including128 binary syndromes

An immediately checkable sufficient hypothesis for the zero-defect case is that, for fixed group constants gamma,alpha,beta,

```
sigma3 = gamma,
sigma5 - sigma9 = alpha,
sigma10 - sigma9 = beta.                              (E)
```

Then both right sides in (D) vanish, without restricting any other syndrome coordinate. Thus every such arbitrary FD law obeys

```
H(X_V) <= (2/3) sum_v H(X_v).                           (F)
```

There are d^7 allowed syndrome vectors in (E): sigma9 and the six coordinates1,2,4,6,7,8 are free. For G=F2, (E) is an affine subspace of F2^10 of dimension7, containing128 syndromes, not an affine plane of at most4 syndromes. The law can use any subset with arbitrary probabilities and correlations. A uniform FD support in this class has size at most d^20. Fixed-parity triangle codes attain d^20, so the restricted-class bound is sharp.

The factor-preserving graph permutation (8,9,3,4,10,7,6,1,2,5) exchanges factors3 and10 and preserves the set{5,9}. It transports (E) to the second cylinder with sigma10 constant and sigma3,sigma5,sigma9 mutually equal up to fixed group offsets. This transport can also be checked literally from the triangle list; no graph permutation that fails to preserve the factor list is used.

Neither cylinder covers arbitrary syndrome supports. Nothing here establishes the unrestricted balance conjecture or improves the unreviewed numerical global upper bound. The new content is the alphabet-free auxiliary-defect representation, its quantitative actual-component consequence, and these much larger restricted syndrome classes.

## 5. Exact evidence and review boundary

- Integer certificate `frontier-20261029-one-auxiliary-defect-certificate-v1.json`, SHA256 `7c1b7b6f8b5bfe286411b5d3ba92dc6dd351e7003402102f9c4480038a220e82`, includes all1008 literal row vectors and positive integer multipliers.
- Independent standalone checker `frontier-20261029-one-auxiliary-defect-check-v1.py`, SHA256 `4f6b3fd88713ca18335db09368179834b3f7bb4c86651822cfd99dc63bf8429e`.
- Receipt `frontier-20261029-one-auxiliary-defect-check-result-v1.json` records the actual bounded integer check inside the existing eval kernel and the five negative controls. It is execution evidence, not an independent scientific verdict.

Every scientific claim in this manuscript remains a candidate pending independent semantic/caller review. The general entropy inequality can be reviewed without any prior affine-plane theorem or originating four-state certificate. The common-syndrome corollary depends on actual component inversion and the explicitly written fixed-factor entropy lift, not a stronger graph-FD assumption. No novel-result or publication claim is made.
