# PH7: every seven-state realization is irreducible for z>1/2

**NEW WRITTEN THEOREM CANDIDATE, topology-independent, with exact symbolic identities. Independent review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1; actual observed clock before writing Wed Oct28 17:48:25 PDT2026. This is not an existence/exclusion decision at 8/9. No held source is a premise.

## Theorem

Fix any c,d>0 and b>0; put a=c+d and z=b^2/d^2. Let

    H(s)=c(a^2+b^2)^2 / [(s+c)((s+a)^2+b^2)^2].

If `z>1/2` and a PH representation `(alpha,T,omega=-T1)` of H uses **at most seven states**, then it has exactly seven states, every state is reachable from alpha, and the directed graph of T is **strongly connected**. In particular an 8/9 witness, if any, must be an actual irreducible seven-state generator. Equivalently, there is no reducible or lower-state PH representation in this regime.

The lower-state consequence reproduces the known unrestricted PH6 barrier at this cut; it is not claimed as a new theorem. The additional SCC conclusion is stated separately, and no claim of global mathematical novelty is made. No fixed 3+3 chain, hidden-root sign pattern, real diagonalizability, or specific beta/exit support is assumed.

## 1. Trimming and spectral placement from the actual PH transfer

Delete states unreachable from the support of alpha. This preserves the represented transfer and its PH row ties because the reachable set is forward closed; the initial probability still sums to1. In a Hurwitz transient generator, every remaining state can reach some positive exit: `(-T)^(-1)omega=1`, and a state without an exit path would have zero on the left. Let m be the retained number of states, so m<=7.

The denominator of H in lowest terms is degree5: poles -c simple, `-a +/- ib` each double. Consequently all three occur, with at least these algebraic multiplicities, in the characteristic polynomial of the retained T, even if its two additional eigenvalues are repeated, nonreal, or coincide with target poles.

Every irreducible communication block of T has Perron rate at most `-c`. Here is the actual positivity argument. For any such block B, reachability and exit reachability give fixed t0>0 with positive entrance and exit vectors on it. By nonnegative semigroup path expansion, the target density at time `t+2t0` dominates their bilinear form in `exp(tB)`. Perron theory for an irreducible Metzler matrix gives a positive constant times `exp(rho(B)t)` for all sufficiently large t. But partial fractions of the actual H give `f(t)=O(exp(-ct))`: the other terms are polynomials of degree at most1 times `exp(-at)` times sines/cosines. Thus `rho(B)<=-c`. Since -c itself is a pole and hence an eigenvalue, the full spectral bound is exactly -c.

Write

    G=(T+cI)/d.

Every SCC block of G is Metzler with Perron rate <=0. G has the visible real eigenvalue0 and the conjugate pair `-1 +/- i sqrt(z)`, each with algebraic multiplicity at least2.

## 2. No SCC with at most three states contains a visible nonreal eigenvalue

An irreducible Metzler block of order1 or2 has only real eigenvalues; for order2 the discriminant is `(x11-x22)^2+4 x12 x21>=0`. Suppose an irreducible 3-by3 Metzler block contains `-1 +/- i sqrt(z)`. Its remaining eigenvalue is the real Perron root `-r`; Perron simplicity and strict spectral dominance give `0<=r<1`.

For any real Metzler A, `tr A^2 >= (tr A)^2/n`: indeed `tr A^2=sum A_ii^2+2 sum_{i<j} A_ij A_ji` and Cauchy bounds the diagonal squares. Applying it at n=3 yields exactly

    3[r^2+2(1-z)]-(r+2)^2
      =2[(1-r)^2-3z] >=0.

But `(1-r)^2<=1<3z` when z>1/2. Contradiction. Thus every SCC containing either visible complex eigenvalue has at least four states.

Since there are two algebraic copies of each conjugate visible eigenvalue and m<=7, they cannot be contributed by two distinct SCCs: each such block would need at least four states. Their full visible multiplicity is therefore in ONE SCC. Irreducibility of that block forces a real Perron eigenvalue in addition to the four nonreal eigenvalues, so its size is at least5. This argument still applies if hidden roots coincide with visible ones: total multiplicity can be larger, never smaller.

## 3. The common SCC cannot have five states

Its spectrum would be the visible pair twice plus the real Perron eigenvalue `-r`, where again `0<=r<1`. The same trace-square bound at n=5 gives

    5[r^2+4(1-z)]-(r+4)^2
      =4[(1-r)^2-5z] >=0,

impossible for z>1/2. This conclusion does not require any statement about the hidden quadratic or chosen input/output vectors.

## 4. A standalone six-state Metzler spectral lemma

**Lemma.** No real 6-by6 Metzler matrix with spectrum

    0, -u, -1 +/- i sqrt(Z) each twice,

where u>=0, can exist when `Z>1/2`. Reducibility is allowed in the lemma; no transfer realization is assumed.

*Proof.* Put `a=4+u`, `h=a/6`, and `X=M+hI`. Then `tr X=0`. Newton sums with algebraic multiplicity, without diagonalizability, give

    tau2=tr X^2=(5u^2-8u+8-24Z)/6,
    tau3=tr X^3=-(u-2)(5u^2-2u+18Z+2)/9.     (6TRACE)

For real Metzler X, `tau2>=0`. To control tau3, form real symmetric S with `S_ii=X_ii` and `S_ij=sqrt(X_ij X_ji)`. Then `tr S=0`, `tr S^2=tau2`, and `tr X^3>=tr S^3`: diagonals and two-state terms agree, while AM-GM compares the two orientations of every distinct-index 3-cycle.

For any real symmetric traceless six-by-six S,

    tr S^3 >= -(4/sqrt(30)) (tr S^2)^(3/2).     (6EXT)

This follows by compact minimization of the six real eigenvalues at fixed square sum and zero sum: at an extremum they have at most two distinct values, and the most negative ratio is attained for multiplicities1 and5, namely `(-5t,t,t,t,t,t)`. The zero-square case is trivial. Consequently, whenever tau3<0 the necessary inequality is

    (8/15) tau2^3 - tau3^2 >=0.                 (6NEC)

For Z>1/2, `tau2<0` throughout `0<=u<=2`: its numerator is a convex quadratic in u, negative at both endpoints. Thus u>2. Set `s=u-2>0` and `delta=Z-1/2>0`. The exact identities(6TRACE) become

    tau2=tau20-4 delta,    tau20=s(5s+12)/6 >0,
    tau3=tau30-2s delta,   tau30=-s(5s^2+18s+27)/9 <0.

Since tau2>=0, both `tau2^3<=tau20^3` and `tau3^2>=tau30^2`. Direct expansion yields

    (8/15)tau20^3-tau30^2
       = -s^2(30s^2+116s+135)/15 <0,

contradicting(6NEC). This proves the lemma. Exact symbolic verification of every displayed polynomial identity is pinned in §6. □

## 5. The common SCC cannot have six states, hence all seven are connected

Suppose the single SCC containing both visible pairs has size6. Its two remaining eigenvalues are real: an irreducible real Metzler matrix has a real Perron eigenvalue, and a lone remaining nonreal eigenvalue cannot occur without its conjugate. Let them be `-r` (the Perron root) and `-u`. Perron dominance and the overall spectral bound give

    0<=r<1,    u>=r.

Shift this SCC by rI and scale by `1/(1-r)`. The resulting six-by-six Metzler spectrum is

    0, -(u-r)/(1-r), -1 +/- i sqrt(z)/(1-r) each twice.

Its u-parameter is nonnegative and its new squared frequency is `z/(1-r)^2 >= z>1/2`, contradicting the standalone lemma. Coincident hidden/visible roots do not create an exception: the Perron root must be real and all algebraic multiplicities were counted.

The common SCC must therefore have size at least7. But m<=7. Hence m=7 and this SCC is the entire retained graph: G, and therefore T, is irreducible. Since m equals the original at-most-seven count, no original state was trimmed and the original input reaches every state. This proves the theorem. □

## 6. Exact checks, imports and nonclaims

Actual completed execution:

    python3 frontier-20261028-ph7-irreducibility-identities-check.py
    SymPy 1.14.0 exact 3/5/6 state SCC barrier identities PASS

The checker uses symbolic rational polynomial arithmetic, not floating arithmetic. It verifies the n=3/n=5 trace-square identities; all n=6 centered trace-square and trace-cube identities; their positive-delta monotonic decompositions; and the strict negative delta-zero polynomial identity. It does NOT check Perron semigroup arguments, AM-GM, SCC decomposition, the compact eigenvalue extremum, or the theorem as a formal proof.

Checker `frontier-20261028-ph7-irreducibility-identities-check.py`, 26LF/1512B, SHA256 `41c37488c7e9313d812916078ea7861d7ed9007e649d1f6b9f501ce0b98ef7c6`. Certificate `frontier-20261028-ph7-irreducibility-identities-certificate.json`, 9LF/416B, SHA256 `b856870dbfabf42dd002148f0cb8e5f726960ba9a7bb5ef8a6c340f63089a92a`.

Named ordinary mathematical imports are finite directed SCC decomposition/characteristic factorization; positive Metzler semigroups and irreducible Perron spectral dominance; Cauchy and AM-GM; the elementary compact Lagrange-multiplier eigenvalue extremum; rational polynomial arithmetic. The same six-state centered-trace idea appears in the already-adopted v121 complete equivalence source and PH6 lower proof; the above proof reconstructs its spectral lemma rather than asserting discovery of it. The SCC application was not found by the author's focused search of the named v121 author and parent source; that is not an exhaustive literature or prior-art search.

The theorem says nothing about whether an irreducible seven-state realization exists at 8/9, whether the critical minimum is7 or8, which hidden roots occur, or whether the family maximum equals any candidate endpoint. The exact trace-two/three inequalities for unrestricted SEVEN-state spectra alone are insufficient to decide the target; see the separate `frontier-20261028-ph7-trace23-obstruction-limit-v1.md`, which is NOT a PH witness.

Prior held outputs remain nonpremises and all historic process findings survive. Same18/exclusive owner root; no external-model campaign, publication, secret exposure, deletion, Git push or infrastructure mutation. Independent written/math/dependency and stronger verification gates are not conferred.

END — all actual PH7 representations at z>1/2 must have a single strongly connected seven-state graph; original existence/exclusion at8/9 remains open.
