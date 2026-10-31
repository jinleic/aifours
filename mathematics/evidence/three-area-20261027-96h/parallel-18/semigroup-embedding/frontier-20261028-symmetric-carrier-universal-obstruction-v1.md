# Arbitrary symmetric-band powers cannot host the 68-source

**Status: NEW AUTHOR WRITTEN ALL-ACTOR OBSTRUCTION for a specific band quasivariety; UNREVIEWED / UNADOPTED.** This is a genuine boundary of the new B_I model carrier. It does not obstruct all seminormal bands: the pinned six-/eight-/ten-band hosts of S68 remain faithful. The proof below uses no actor-transport theorem.

## 1. A universal band quasiidentity

Let Q be the band quasiidentity

`EF=F, FE=E, EB=E, FB=F, AE=AF  ⇒  E=F`.                 (Q)

Every symmetric band B_I from `frontier-20261028-symmetric-seminormal-band-family-v1.md`, SHA `0b384b98ef651be0f2105cfeec3e371b1cbfaf0c8ebfd091d42adae0c190b3e9`, satisfies Q. Indeed, a distinct R-related pair E,F must lie in the lower right-zero band `{x}∪{v_i}`; all upper u_i have singleton R-classes. If B=x or B is any lower v_j, right multiplication by B is constant, so EB=E and FB=F force E=F. Therefore a distinct pair requires B=u_j. In this case xB=v_j≠x, so E,F cannot be x; they are distinct v_i,v_k. But every A satisfies `A v_i=v_i`, `A v_k=v_k`, contradicting AE=AF. This proves Q for arbitrary finite or infinite I.

Every rectangular band also satisfies Q: an R-pair has the same row, and EB=E, FB=F make both columns equal the column of B. Universal quasiidentities are preserved by direct products and subsemigroups. Hence Q holds in every band in `SP({B_I}∪{rectangular bands})`, allowing arbitrary index sets, arbitrary products/subbands and arbitrary group actions preserving them.

## 2. A transport-free source criterion

Suppose a semigroup S has distinct idempotents e,f and source elements a,b with

`ef=f`, `fe=e`, `eb=e`, `fb=f`, `ae=af`.                  (1)

Then no homomorphism from S to a physical `P(C,D)` with C satisfying Q and D completely simple can separate e,f.

Proof. Let r be the actor map. The R-idempotent equations force r(e),r(f) to have the same Rees row. Equality r(a)r(e)=r(a)r(f) forces their columns to agree. As each cell has a unique idempotent, `r(e)=r(f)=d`. Let E,F,A,B be their band coefficients. Because d is idempotent, its self-weight is1, giving EF=F,FE=E.

The equations eb=e,fb=f use the SAME physical group weight w, since the left actors are identical. Put `B'=α_w(B)`; then EB'=E and FB'=F. The source equality ae=af also uses the same weight v for its two right factors, so `A α_v(E)=A α_v(F)`. Applying the inverse band automorphism α_(v⁻¹) gives `A' E=A' F` with `A'=α_(v⁻¹)(A)`. Q applied to E,F,A',B' forces E=F. Their actors coincide, so the two entire physical images coincide. □

No purity, finiteness, actor-image restriction, normal subgroup or coinduction assumption is hidden. In particular arbitrary nonabelian group actions on B_I powers cannot repair this source obstruction.

## 3. Exact original-source instance and scientific consequence

S68 satisfies (1) at `(a,b,e,f)=(0,25,37,61)` in its pinned source table. The exact checks in `frontier-20261028-quotient68-faithful-host-checker-v1.py`, SHA `694d037f52e02a0c9cf00eb426bdaa04043930bb035e3877f19a11e395807f25`, include those equations and e≠f; source-class verification additionally requires the mandatory full-natural-order erratum `frontier-20261028-natural-order-weu-audit-erratum-v1.md`, SHA `801f699bb640bd1e58eed095779c05b882e7d9eddd0ea1c470b522ecbc345c28`, and its full-order checker. Thus S68 has **no** faithful physical host over ANY CS actor whose band is a subband of any product of the symmetric B_I and rectangular bands.

The six-element SN band C in the already faithful C⁵ host violates Q at `(A,B,E,F)=(4,3,1,0)`. Hence the needed seminormal target class is strictly richer than this entire symmetric-carrier quasivariety. This forbids silently treating B_I or its powers as a universal model family for the one-sided original R/L task. The earlier nonabelian quotient experiment remains a finite test on its own declared inputs; it is not a universal separation strategy.

This is a band-class obstruction and a model-selection boundary, NOT an all-SN nonembedding or full Q1 answer. All mathematics remains author-written, unreviewed, nonformal and without novelty clearance.
