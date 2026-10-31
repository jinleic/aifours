# Rank-free three-source Gram/Farey bound for every direct finite-simple P7 family

Owner: MathSun8-2. Actual observation: `Mon Oct 26 08:40:29 PDT 2026`.
Status: **NEW WRITTEN; not reviewed or adopted.** All calculations below are displayed written integer/fraction identities, not interpreter, calculator, program, enumeration, scientific replay or kernel checks. No special classification, Sun3/Sun4/R4, NC7/F7, Jordan, subgroup-table, McLaughlin or Parker input is used in the direct theorem.

## 1. Exact direct hypotheses, conclusions, and what is not concluded

Let G be finite. Suppose three actual nonempty LEFT cosets of actual subgroups M,R,H are pairwise disjoint, with

`[G:M]=7t, [G:R]=7r, [G:H]=7u`, where `t,r,u` are positive pairwise coprime integers.

No restriction excludes a private factor divisible by 7. The three cosets can be ANY three members of the original eight-coset P7 family. No coset is replaced by an abstract set, no subgroup is enlarged, and no original index or private factor is removed.

**Theorem A, full rank-free representation conclusion.** The complex permutation module X on the actual LEFT-coset set G/M contains a NONTRIVIAL irreducible constituent W of dimension `d<=1728`. More specifically, W can be chosen in the largest-positive-eigenvalue eigenspace of the centred incidence Gram operator built below from the actual R-orbit of M. There is NO assertion that W is the entire nonconstant orbital module, that X contains W with multiplicity one, or that the other incidence Gram operator preserves this chosen copy.

**Theorem B, full finite-simple order and index conclusion.** If G is finite NONABELIAN SIMPLE, this W is faithful and

`|G| < B := 169^5971968`.

Consequently, for ANY direct original eight-coset P7 family in such G, EVERY original index `7r_l` is `<B`. Every actual subgroup index, including `[G:N_G(U_l)]` and every actual outer index `7t`, is also `<B`. This covers the ENTIRE direct finite-simple branch, INCLUDING the case with no alpha-six source anywhere. It is not restricted to two-orbit sources, the mixed 6+1/5+2 branch, elementary normalizer quotients, or any source-isotypic predicate.

The theorem supplies a finite order bound, NOT exclusion of the groups below it, a completed finite assay, an actual eight-coset witness, a numerical value of R8, or full Sun8. For nonsimple G the small constituent may be nonfaithful: no bound on the order of such G follows. The old least-GROUP-ORDER existence descent to simple G and general Sun8-to-P7/Sun7 ancestry are SEPARATE named research inputs, not silently proved here; see §9.

## 2. Every needed intersection factor, including all conjugates

For any two of M,R,H, write their private factors as a,b. Their subgroup intersection has index divisible by both 7a and 7b, hence by `7ab`, because gcd(a,b)=1. Therefore

`[G:A intersect B] = 7ab delta`, with integer delta >=1.

The product-set formula gives `|AB|/|G| = delta/7`, so delta<=7. If delta=7, then AB=G and EVERY left A-coset meets EVERY left B-coset: `x^-1 y in AB` supplies an element of `xA intersect yB`. This contradicts the given disjoint pair. Thus the original factor is at most six.

We require more than this original-pair observation. R acts NONTRANSITIVELY on G/H: transitivity would imply RH=G and contradict the actual disjoint R- and H-cosets. The stabilizers at all points gH are `R intersect gHg^-1`. An orbit of size `[G:H]=7u` would itself be the whole G/H, making the action transitive. Hence, for EVERY g,

`[G:R intersect gHg^-1]=7ru delta_g`, with `1<=delta_g<=6`.

The upper bound is valid for ALL g, not an assumption that every delta_g equals the original delta. The lower divisibility still uses gcd(r,u)=1 and the conjugate subgroup's unchanged index.

Let Omega=G/M. Its base R-orbit is the ACTUAL set `T_R=R.M`, of size

`[R:R intersect M] = kt`, where `1<=k<=6`.

The upper bound follows from the disjoint M/R pair just proved. Similarly the actual base H-orbit `T_H=H.M` has size `ell*t`, where `1<=ell<=6`. Both are nonempty proper invariant sets. They need not be complements of single orbits; the R- and H-actions may each have arbitrarily many orbits allowed by the degree. No rank-one hypothesis has entered.

## 3. The actual denominator-six grid for every translated intersection

For a,b in G consider `aT_R intersect bT_H`. It is invariant under

`A = aRa^-1 intersect bHb^-1`.

Its index is `7ru delta` with `1<=delta<=6`, by §2 after conjugation. If an A-orbit on Omega has size w, then its point stabilizer lies in a conjugate of M. Thus

`7t divides [G:A]w = 7ru delta w`.

Since gcd(t,ru)=1, `t divides delta w`. With `g=gcd(t,delta)`, EVERY such w is a multiple of `t/g`. The entire intersection, being a union of A-orbits, also has cardinality a multiple of `t/g`. Therefore

`z(aR,bH) := |aT_R intersect bT_H|/t = n/g`, with integers `n>=0, 1<=g<=6`.

In particular every z belongs to the rational grid of denominator at most six (in its actual bounded range `0<=z<=min(k,ell)`). Its denominator can vary from entry to entry. We have not enumerated a group or assigned independently chosen intersections to different cells.

## 4. Incidence operators and the rank-free positive-trace bound

Let I_R be the 0/1 incidence matrix whose rows are the actual points of Omega and whose columns are the actual LEFT cosets aR, with entry one exactly when the row lies in `aT_R`. It is well-defined because T_R is R-invariant. Every column has kt ones; G-transitivity on Omega gives every row exactly kr ones. Similarly I_H has column sum `ell*t` and row sum `ell*u`. Both matrices are G-equivariant.

Put `P=I_R I_R*`, `Q=I_H I_H*`, where * means conjugate transpose, and let E_0 be orthogonal projection onto the constant line in X. The operators are positive Hermitian and G-equivariant. Their constant eigenvalues and traces are

`P.1 = k^2 tr .1`, `trace(P)=7ktr`,

`Q.1 = ell^2 tu .1`, `trace(Q)=7ell*tu`.

Here `tr` means the product `t*r`, NOT a trace function; only the explicit word `trace` denotes trace. Define

`P_0=P-k^2 tr E_0`, `Q_0=Q-ell^2 tu E_0`.

These vanish on constants and are positive Hermitian on `X_0=1^perp`. Their traces are

`trace(P_0)=k(7-k)tr>0`, `trace(Q_0)=ell(7-ell)tu>0`.

Let lambda>0 be the largest eigenvalue of P_0. Its eigenspace lies in X_0 and is G-invariant, since P_0 commutes with the G-action. A finite-dimensional complex unitary G-module is an orthogonal sum of irreducibles (average an inner product and take invariant orthogonal complements). Choose ANY irreducible W in this eigenspace and put d=dim(W). It is NONTRIVIAL because a transitive permutation module has only the constant invariant line. Its contribution to trace(P_0) is lambda*d, so

`lambda <= trace(P_0)/d`.

Since `0<=P_0<=lambda I` on X_0 and Q_0 is positive,

`trace(P_0 Q_0) <= lambda trace(Q_0) <= trace(P_0)trace(Q_0)/d`.

For clarity, the first inequality follows by taking the trace of `Q_0^(1/2) P_0 Q_0^(1/2) <= lambda Q_0`; it does NOT require P_0 and Q_0 to commute. W need not be multiplicity-one in X, and Q_0 need NOT preserve this copy or be scalar on it. This is precisely the rank-free replacement for the earlier one-isotypic covariance argument.

## 5. Full cross mean and variance over the same actual coefficients

Average Z=z(aR,bH) uniformly over ALL `(7r)(7u)=49ru` actual column pairs. The sum of the entries of `I_R* I_H` is the inner product of the two row-sum vectors, hence `7t*k*ell*ru`. Therefore

`E[Z]=mu=k*ell/7`.

The sum of their squared entries is `trace(PQ)`. The constant terms and the centred terms are orthogonal, so

`trace(PQ)=k^2 ell^2 t^2 ru + trace(P_0 Q_0)`

`<= [k^2 ell^2 + k(7-k)ell(7-ell)/d]t^2 ru`.

After division by `49ru*t^2` and subtraction of `mu^2=k^2 ell^2/49`,

`Var(Z) <= k(7-k)ell(7-ell)/(49d)`.

Every mean, square, trace and grid restriction uses the SAME actual entries and the SAME uniform distribution. No separately selected fibre data, phases, eigenvectors of Q_0, or per-entry supports enter this inequality.

## 6. The complete Farey-gap lower bound and exact dimension constant

The following elementary identity supplies all required grid gaps. If `a/b<c/d`, with `bc-ad=1`, and a rational `n/g` is strictly between them, the positive integers `bn-ag` and `cg-dn` obey

`g = d(bn-ag)+b(cg-dn) >= b+d`.

Thus each of the neighbor pairs

`0/1,1/6`; `1/4,1/3`; `2/5,1/2`

has NO rational of denominator at most six strictly between its endpoints: each determinant is one and each denominator sum is seven. They bracket respectively `1/7,2/7,3/7`. Reflection `x->1-x` brackets `6/7,5/7,4/7`; adding an integer changes no denominator. These six gaps exhaust the six possible nonzero residues below.

Because 7 is prime and `1<=k,ell<=6`, `mu=k*ell/7` is not an integer. Write its fractional part as j/7, `j in {1,2,3,4,5,6}`. Choose the corresponding translated/reflected gap `[a,b]`. Every actual value Z has denominator at most six by §3, so `(Z-a)(Z-b)>=0`. Taking expectations gives

`Var(Z) >= (mu-a)(b-mu)`.

For j=1,2,3 the exact products are respectively

`(1/7)(1/6-1/7)=1/294`,

`(2/7-1/4)(1/3-2/7)=(1/28)(1/21)=1/588`,

`(3/7-2/5)(1/2-3/7)=(1/35)(1/14)=1/490`.

Reflection gives the identical products for j=6,5,4. Thus in ALL cases `Var(Z)>=1/588`. Also `k(7-k)<=12` and `ell(7-ell)<=12`: the six integer products are `6,10,12,12,10,6`. Combining with §5,

`1/588 <= 144/(49d)`, hence `d<=144*588/49=144*12=1728`.

This proves Theorem A. It is a universal written six-residue identity, not a numeric parameter trial, numerical magnitude scout, enumeration of subgroups or scientific certificate replay. It does not assert that the full cyclic module generated by T_R has dimension at most 1728; only the chosen irreducible W is bounded.

## 7. Full faithful-unitary packing proof for the finite-simple order bound

Now assume G finite NONABELIAN SIMPLE. The kernel of its nontrivial irreducible W is a proper normal subgroup, so it is trivial. Average an inner product to make this faithful representation rho unitary of degree d<=1728.

Let `delta=min_{g!=1} ||rho(g)-I||_op>0`. Suppose delta<1/2 and choose a minimizer g. Every conjugate matrix of rho(g) has the same distance delta. For any two such conjugate matrices A,B,

`||ABA^-1 B^-1-I||_op = ||AB-BA||_op`

`= ||(A-I)(B-I)-(B-I)(A-I)||_op <= 2delta^2 < delta`.

By minimality and faithfulness this commutator is the identity. Thus ALL conjugates of g commute pairwise. They generate a nontrivial ABELIAN NORMAL subgroup, contradicting nonabelian simplicity. Therefore `delta>=1/2`.

For distinct group elements, their unitary matrices have operator-norm separation at least 1/2, hence Frobenius-norm separation at least 1/2. Their open Frobenius balls of radius 1/4 are disjoint in the real vector space of complex d-by-d matrices, of dimension `2d^2`. Every unitary matrix has Frobenius norm sqrt(d), so all these balls lie in the ball of radius `sqrt(d)+1/4` about zero. Comparing ordinary Euclidean volumes yields

`|G| <= (4sqrt(d)+1)^(2d^2)`.

Since `d<=1728<42^2=1764`, the base is strictly less than 169. Also

`2*1728^2=2*(2890000+95200+784)=2*2985984=5971968`.

It follows that `|G|<169^5971968`, proving Theorem B. This argument needs no Jordan theorem, finite-simple classification, character table or external minimum-degree estimate. The displayed integer power is NOT evaluated or used to launch a search.

## 8. ALL original sources and finite-core transfer; no lost index or fibre

For an original direct P7 family of EIGHT actual cosets `g_l U_l`, with ALL `[G:U_l]=7r_l` and pairwise coprime private r_l, choose ANY three distinct indices i,j,k and use `M=U_i,R=U_j,H=U_k`. Pairwise disjointness provides exactly every hypothesis in §§2–3. The other FIVE subgroups, cosets, original indices and private factors remain in the family unchanged. The theorem does not enlarge a subgroup or discard a hidden neighbour; it uses a consequence of this literal subfamily to bound the SAME ambient G when simple. Each original `7r_l<=|G|<B`, and every actual normalizer/outer subgroup index has the same bound. No inference replaces original indices by only their 2-ranks or by selected initial vertices.

For possibly infinite G with these finite indices, take C to be the intersection of the cores of ALL EIGHT original U_l. It is normal of finite index, is contained in every U_l, and is obtained from the kernels of their finite permutation actions. The quotient F=G/C is finite; original subgroup indices, the eight private factors, and all left-coset intersections/disjointness are preserved because each U_l is the full preimage of U_l/C. Thus the representation conclusion applies to F. It does NOT bound the order of infinite G, or automatically make F simple.

Normalizers are also preserved if later needed: an element normalizes U_l/C iff its conjugate has the same FULL preimage U_l in G. Hence `N_F(U_l/C)=N_G(U_l)/C`, with actual indices preserved. No normality of N_G(U_l) in G is required or claimed. This observation is not used as a replacement for the elementary three-source proof.

If G itself is an abstract NONABELIAN SIMPLE group with a proper subgroup of finite index, its action on that finite coset set has a proper normal kernel and is nontrivial; simplicity makes it faithful, so G is already finite. The stated simple-group bound therefore also covers that conditional case. It does not reduce arbitrary G to this case.

## 9. Source, process and exact remaining gap

All load-bearing mathematics for Theorems A/B and their DIRECT eight-source/finite-core applications is reconstructed in §§2–8. No prior special research packet or positive reviewer label is a correctness premise. The standard finite-dimensional spectral theorem, averaged unitary inner product/invariant orthogonal complements, subgroup index and orbit-stabilizer identities, positive-matrix trace inequality and Euclidean ball-volume scaling are the ordinary tools displayed in the proof. No supplied publication, classification theorem, frozen historical computation or accepted numerical bound is invoked.

The earlier full standalone `sun8-one-six-source-proper-orbit-Farey-finite-branch-v1.md` (168 LF, SHA256 `264477981654bf2a078808a7a1debcc17f181f0ea63dae33df3e5ee096e7f95a`) is a NEW narrower predecessor, not an accepted premise. Its unique-source dimension bound 720 is sharper in that case; the present bound 1728 removes EVERY source-rank, source-partition and alpha-six restriction by the maximum-eigenvalue trace argument. Earlier 200/142 source-block, private-owner, small-Q, single-isotypic, classical-family and actual-enlargement conclusions retain their original separate hypotheses; this bound does not supply their stronger geometric structures to arbitrary sources.

The current parent `sun-two-five-plus-two-and-mixed235-entire-parent-v1.md` (70 LF, SHA256 `a90790d172f33a32c92fb64ef074f4aaaafc677a7239dc4d338d41b9bc1ccafc`) adopts its older full source gates at selected 7-FREE/ASSUMED-simple cuts. Its NR-NS least-GROUP-ORDER existence descent source ranges and 63-LF composition were UNSUPPLIED in that freeze and remain NAMED_NOT_RECONSTRUCTED there. That is not a defect or premise of the direct conditional theorem here, and this new paper does not retroactively authenticate that ancestry or general Sun8-to-P7/global Sun7. Any attempted unconditional use of that reduction must supply its actual proof and preserve its exact existence quantifiers.

**Exact residual:** below the explicit universal B there remains NO written exclusion of ALL finite nonabelian simple direct P7 families, no actual witness, and no completed finite enumeration or authorized executable assay. The simple-existence descent and general Sun8/P7 ancestry still require their exact named source boundaries. For nonsimple or infinite groups a small nonfaithful constituent alone does not bound the ambient group or justify a source-preserving enlargement. Thus unrestricted Sun8 is OPEN in this work. Alpha-six absence is no longer an unbounded SIMPLE-case loophole IF this NEW proof is accepted, but it remains an unexcluded existence possibility below B; no new source-forcing or fibre-transport exclusion is claimed.

Permanent OWN057/047/078/COUNT/M1/v26/v31-two-findings/v33 and all received parent/reviewer finding histories remain, with all withdrawn historical trial guidance ENTIRELY ZERO. This paper was developed only in the separately acknowledged/released primary period after actual v123-C RETURN. Both scientific Eval kernels stay dead; no calculator/program/CAS/enumeration/solver/replay/CLI/nested agent/new scientific GO was used. New proof is WRITTEN only, not formal, kernel-checked, human/configured-family accepted, novelty/priority cleared or a public refutation. The original arbitrary-group research and exact remaining gap continue; this paper is not an early final park or round closeout.
