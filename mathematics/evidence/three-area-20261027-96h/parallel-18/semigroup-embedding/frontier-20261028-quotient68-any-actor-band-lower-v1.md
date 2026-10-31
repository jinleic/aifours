# A six-element band lower bound for every CS actor

**Status: NEW AUTHOR WRITTEN universal lower bound; UNREVIEWED / UNADOPTED.** For the pinned 68-source S, every faithful physical band-by-CS host, with arbitrary CS actor and arbitrary action, has band size at least 6. This complements the exact **10-element minimum over the actual actor q** in `frontier-20261028-quotient68-exact-q-band-optimum-v1.md`, SHA `d9eed1b521d76da32a096b42d34f3cf66a05dc53b007613295976e73627a6174`. It does not prove the all-actor minimum is 6 or 10.

## 1. A six-distinct-elements band lemma

Let B be any band, and suppose

`EF=F`, `FE=E`, `AE=AF`, `E=VT`, `F=VQ=UT`, `T=PQ`, `E≠F`.     (1)

Then the six elements `E,F,A,T,V,Q` are pairwise distinct. No regular-band or seminormal identity is needed.

Because T is idempotent, `ET=E` and `FT=F`. A differs from E and F: if A=E then AE=E, AF=F; if A=F then AE=E, AF=F. T differs from E and F: if T=E then FT=FE=E, while if T=F then ET=EF=F. If A=T, multiply AE=AF on the left by E: `(ET)E=E` but `(ET)F=F`. Thus E,F,A,T are four distinct elements.

V differs from F because V=F would give `E=VT=FT=F`; it differs from T because V=T gives E=T. If V=A then `AE=A(VT)=AT=E` and `AF=A(VQ)=AQ=F`. If V=E, the equality `E=EPQ` implies `EQ=(EPQ)Q=E`, so `F=VQ=E`. Each case contradicts E≠F; hence V is a fifth distinct element.

Q differs from F: if Q=F, the expression `E=VPF` gives EF=E, but EF=F. If Q=E, `F=VE` gives FE=F, but FE=E. If Q=T, `F=VQ=VT=E`. If Q=V, `F=VV=V`, already excluded. Finally, if Q=A then the expressions for E,F end in A, so EA=E and FA=F; multiplying AE=AF on the left by E gives E=EF=F. Thus Q is different from all five prior elements, proving |B|≥6. □

## 2. Every actor must realize the lemma

Use the source relations and notation of the direct arbitrary-actor proof `frontier-20261028-quotient68-all-cs-direct-obstruction-v1.md`, SHA `9092df28a55693c396ee5797b2687eb457265b139087d1119d69eb0f36e35043`: distinct idempotents e,f satisfy `ef=f`, `fe=e`, `ae=af`, `e=stv`, `f=sv=utv`. In ANY CS actor, the R relations force the actor rows of e and f equal and `ae=af` forces their columns equal, so their idempotent actor values coincide. In a faithful host their band coordinates E,F are distinct and satisfy EF=F, FE=E.

The Rees group-coordinate comparison in the cited proof aligns the action weights and gives `E=VPQ`, `F=VQ=UPQ` for suitable V,P,Q,U∈B. Finally, `ae=af` gives `c_a α_h(E)=c_a α_h(F)` for the common weight h; applying the inverse band automorphism gives `AE=AF` with `A=α_h⁻¹(c_a)`. Therefore (1) holds in every faithful host, so its band has at least six elements. This argument does not depend on the all-actor transport theorem.

The six-element SN band C used in the earlier faithful C⁵ host realizes the six-distinct configuration: `(E,F,A,T,V,Q)=(1,0,4,3,5,2)`, with `P=3`, `U=0`, and `T=PQ=3`. Its literal table verifies every equality. Thus the abstract six-element lower bound is sharp for the **displayed configuration**. It does not follow that the entire 68-source embeds with a six-element band over any actor.

## 3. Quantifier boundary

The literal ten-band host over q establishes an all-actor upper bound of 10 because q is one allowed CS actor. Thus the currently proved author-candidate bounds for the minimum band size over all actors are **6≤min≤10**. The stronger exact value 10 is certified only with actor fixed to q; no inference is made that the larger class of arbitrary actors has the same minimum. The source tables, checks and unreviewed finite-witness status are those of the cited predecessors. No general Q1 resolution or novelty is claimed.
