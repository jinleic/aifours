# f23 — Bloch-radius gap and sharpened same-projector bound

Reviewer **PhysicsMOQLS8-2**, author **PhysicsDepol4-2**. Native observation before writing: **Wed Oct 28 17:26:54 PDT 2026**. Same-harness written proof reconstruction plus independent exact checks; not formal/kernel,human,configured-model-family or novelty acceptance.

## 1. Complete inputs,exact verdict and exposure

Read the COMPLETE assignment FIRST,then both candidate bodies in full through their endings. Live metadata pins:

|Input|LF|SHA256|
|---|---:|---|
|assignment-v1.json|27|59276ae3c9c3400a3e41ee196409c19df742c7a0d0566f8ec9cf91a7a79f8bf2|
|frontier-20261028-11-bloch-gap.md|61|dfebdc80d1d72523f26c3603ba04dbd14ac17cfe38d6f1b5288db67e72212245|
|frontier-20261028-14-sharpened-bloch-gap.md|48|36f297ea359a05efc93b862de7817f1b64866fab1d8f297e0f04d4cf3a5193de|

The original target is the registered ALL-density,physical-parameter output-majorization problem,with one actual complex rank3 projector for k3;its exact domain is stated in the earlier read `physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/intake-v1.md` LF20–34. Both papers' only mathematical dependencies are the source-defined channel,product reference,Schmidt/erasure/spin-flip identities and mirror,all RECONSTRUCTED here. The earlier `frontier-20261028-01-spectral-mirror.md` and `frontier-20261028-06-erasure-certificate.md` were read completely and live-pinned in my just-completed f5 scientific review;I rederive rather than assume their verdict.

Prior contact is substantive: same-track physics research, prior f5 complete proof review and the 512 matrix-unit mirror check. The present exact checker reuses my own independently authored,hash-pinned Gaussian-rational matrix primitives;it imports NO author program or author check output. This is not a blind or independent-model-family review. No author contact or quarantined mathematical premise is used.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR; NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPE.**

- S1/11: the displayed base inequality is supported for EVERY actual pure four-qubit input,complex rank3 P and physical p,including negative right-hand-side cases. Its sufficient radius region and fixed-cap closed-convex-hull extension follow exactly.
- S2/14: the retained-x sharpening,minimum term,piecewise threshold including equality at2/3,and corresponding fixed-cap closed-convex-hull extension are supported.
- Neither proves the unrestricted k3 inequality,or a criterion in terms only of the local radii of an arbitrary mixed density. No external-source/priority or global all-index acceptance follows.

## 2. Physical same-pair layer notation and reference

Let `Φ_p(X)=(1−p)X+(p/2)Tr(X)I`, `Λ_p=Φ_p^⊗4`. For `0≤p≤1` put q=1−p and define the commuting actual erasures

    E_i(X)=I_i/2 ⊗ Tr_i(X), restored to the same tensor order,
    T_m=Σ_(|S|=m) E_S(rho),    t_m=Tr(P T_m).

The channel identity on the SAME rho,P is

    Tr(PΛ_p(rho))=Σ_(m=0)^4 q^(4−m)p^m t_m.                    (E)

Each q^(4−m)p^m is nonnegative on this interval. At rho*=|0000><0000|,take P* onto `|0000>,|1000>,|0100>`. For each erasure set S of size m,its trace is `2^(−m)[1+1_(1∈S)+1_(2∈S)]`;summing gives the SAME fixed reference layer tuple

    (t_0*,t_1*,t_2*,t_3*,t_4*)=(1,3,3,5/4,3/16).

The pure product output eigenvalues are all products of `a=1−p/2` and `b=p/2`,a≥b on[0,1];P* selects the top1+2 eigenvalues including at ties. Thus its trace is exactly `R3=a⁴+2a³b`,not merely a chosen lower reference.

## 3. Every pure input: t1 and t3

Let rho=|ψ><ψ| be ANY pure four-qubit density,with local eigenvalues `(1±r_i)/2`,0≤r_i≤1,and R=Σ_i r_i. A Schmidt decomposition across i|bar-i gives two nonzero eigenvalues `(1±r_i)/2` for rho_bar_i. Therefore E_i(rho) has eigenvalues `(1+r_i)/4` twice,`(1−r_i)/4` twice,and zero otherwise. The sum of its three largest is `(3+r_i)/4` even at r_i=0 or1.

For an arbitrary rank3 orthogonal P,the trace against a Hermitian H is bounded by its three greatest eigenvalues: diagonalize H;the weights `<e_j,P e_j>` belong to[0,1] and sum3. Summing the four actual E_i inequalities yields

    t1≤Σ_i(3+r_i)/4=3+R/4.                                      (1)

Also

    T3=(1/8)Σ_i rho_i⊗I_(other sites).

The terms act on different sites and commute. If `r1≤r2≤r3≤r4` after reindexing,the three largest eigenvalues (with ties allowed) sum to

    (12+r1+r2+3r3+3r4)/16 ≤ (12+3R)/16 =: A.                (2)

Thus t3≤A for the SAME P. This coarse A may exceed the sharper universal5/4 bound;that does not invalidate its use as an upper bound.

## 4. Spin flip,t2 and the ACTUAL common overlap x

The exact one-qubit identity `σ_y X^T σ_y=Tr(X)I−X=2E_i(X)−X`,tensored across four sites, gives

    tilde-rho=Y rho^T Y=T0−2T1+4T2−8T3+16T4,
    Y=σ_y^⊗4.

T4=I16/16. Put `x=Tr(P rho)` and `y=Tr(P tilde-rho)`. Both are in[0,1],because rho and tilde-rho are actual density matrices and P is an actual orthogonal projector. Tracing the SAME operator identity with P gives

    4t2=y−x+2t1+8t3−3
        ≤1−x+2(3+R/4)+8(12+3R)/16−3
        =10−x+2R.                                                (3)

Hence the sharpened upper bound is `t2≤5/2−x/4+R/2`. Dropping the nonpositive `−x/4` yields the first paper's weaker `t2≤5/2+R/2`. No independent state,projector,local marginal or spin-flipped optimizer is selected.

## 5. Exact first and sharpened gap expansions

Subtract the ACTUAL trace (E) from the single reference in §2. Using t0=x,t4=3/16,(1)–(3),and only nonnegative q,p coefficients,

    R3(p)−Tr(PΛ_p(rho))
      ≥ q⁴(1−x) −(R/4)pq³
        +(1/2+x/4−R/2)p²q² +(1/2−3R/16)p³q
      = pq[8p−R(4−p²)]/16 + q⁴(1−x)+(p²q²/4)x.              (4)

The equality uses `4q²+8pq+3p²=4−p²` since p+q=1. This is a purely algebraic identity;individual terms may be negative when R is large,which does not reverse any inequality.

Since x∈[0,1],the last two terms are a convex combination of `q⁴` and `p²q²/4`,so they are at least their minimum. This proves the strengthened paper's statement for0≤p≤1. Dropping BOTH nonnegative x-terms gives the first paper's base bound. At R=0,the base is `p²q/2`,matching the previously reviewed one-uniform gap;the successor legitimately adds an independent nonnegative term,not an assertion that the earlier base was already sharp.

No coefficient is optimized with a different P,rho or p. No claim that the lower bound is nonnegative for all R is made.

## 6. Piecewise threshold, equality and all endpoints

For 0<p<1,the two nonnegative candidates in the minimum compare as

    q⁴−p²q²/4 = q²(q−p/2)(q+p/2).

Thus the minimum is p²q²/4 when p≤2/3,and q⁴ when p≥2/3. Divide the total bound by the strictly positive p q/16 ONLY inside0<p<1. Nonnegativity is exactly the claimed sufficient condition

    R ≤ 4p(3−p)/(4−p²)                         for 0<p≤2/3,
    R ≤ [8p+16(1−p)^3/p]/(4−p²)              for 2/3≤p<1.

At p=2/3 both equal7/4;strictly smaller R gives a strict displayed gap. If the bound is negative,it remains a valid lower bound and yields no decision. At p=0 the minimum and base both vanish;at p=1 they also vanish and Λ_1(rho)=I16/16 for every rho,so the actual k3 difference is exactly0. No division by p or q is made at these endpoints.

## 7. Exact physical mirror and fixed-cap mixtures

For every complex four-qubit operator X and physical p∈[1,4/3],the entrywise identity above yields

    Λ_p(X)=Y Λ_(2−p)(X)^T Y,
    Tr(PΛ_p(rho))=Tr((Y P^T Y)Λ_(2−p)(rho)).

`Y P^T Y` is again an actual rank3 orthogonal projector,and the input rho,its local radii and R are unchanged. The product-reference spectrum depends on |1−p| and so is the same at p and2−p. Set `s=min(p,2−p)`;the two formulas above apply for every p∈[0,4/3]. In particular p=4/3 maps to s=2/3 and is covered at the common7/4 threshold. No input conjugation or independently optimized P is substituted.

Fix p and R0. For EVERY pure rho_j with R(rho_j)≤R0,the slope of the base bound in R is `−s(1−s)(4−s²)/16≤0`,so the same lower bound with R0 holds for each. The extra minimum depends only on p. Apply it to every summand of any finite convex mixture using the SAME P;trace is affine. Continuity extends it to the closed convex hull. If the pure class is empty the hull assertion is vacuous.

This does NOT assert that a mixed state with `Σ_i r_i(rho)≤R0` has such a pure decomposition;indeed the sum of local radii and the convex-hull condition are different predicates. Neither bound asserts anything about general mixed inputs outside the named hull.

## 8. Independent exact symbolic and physical checks

Wrote and ran once:

    python3 -B frontier-review-f23-bloch-exact-check-v1.py \
      --output frontier-review-f23-bloch-exact-check-receipt-v1.json

Checker SHA256 **b6cfee53d2e89493fd430181f6601e42d5074e66cecacfbd12ec6a6b492bf05a**;receipt SHA256 **ec4d0a076795d7007f01fe8dd9b016b5acd63f2af8ca3b45168d780cc6e6eb7b**. It imports only my OWN earlier Gaussian-rational primitive file after checking SHA **5de969371efd72585a6ffddf39c26ebb78e6f2252e7d652394eb3c9c730f720e**;no author code is imported.

Actual `PASS_EXACT_BLOCH_GAP_SAMPLES_NOT_UNIVERSAL_PROOF` output:

1. Exact sparse multivariate polynomial dictionaries verified the full `(p,R,x)` identity (4),the low-threshold polynomial identity,and the crossover factorization. Arithmetic was `fractions.Fraction`,no symbolic CAS or floats.
2. One complex Hermitian idempotent trace3 P was checked exactly. Two actual pure states were checked idempotent/trace1:an unequal complex GHZ with R=28/25 and two unequal complex entangled pairs with R=8316/4225. Every local radius was computed exactly from its reduced2×2 density.
3. The SAME P was used to check x,y,all t_m bounds and the sharpened gap at seven rational p values `0,1/3,1/2,2/3,1,7/6,4/3` for both pure states. One actual mixture of the first state and a separately verified pure one-uniform state was checked with component cap R0=28/25,not its mixed local radius.
4. For the unequal GHZ at p=1/3,the base lower bound was **−19/810** while the added term was **1/81**:this confirms the code treats a negative lower bound honestly rather than reporting a violation. At p=1 all three actual traces and reference were **3/16**,with zero gap;at p=4/3 the GHZ actual trace was **3/16** and the reference **32/81**. Full exact outputs are in the receipt.

These sample checks are finite diagnostics,not the proof. The prior f5 independent checker verified the mirror on all256 matrix units at EACH of p=7/6 and4/3;that is exact for all operators at those two sample parameters,not all-p certification. The all-variable identities are proved above.

## 9. Final residual and trust boundary

The sufficient pure-state region is the stated R/noise threshold;its exact closed-convex-hull extension retains the cap on EACH generating pure state. General pure inputs above that threshold,arbitrary mixed inputs outside the named hull,including mixed locally uniform states not known to be in the hull,and the global t1/t2 sufficient certificate remain OPEN. At s=0 or1 the actual endpoint conclusion is separate and does not enlarge the positive interior region by division.

Both author claims are conventional written mathematical results at the scopes above;this review establishes no configured-independent-family/human/formal/kernel/novelty status and does not certify inherited old proof chains. No claim that an original global violation or full k3 solution has been found. Parent must actually read BOTH complete source candidates and this complete return before scoped adoption.
