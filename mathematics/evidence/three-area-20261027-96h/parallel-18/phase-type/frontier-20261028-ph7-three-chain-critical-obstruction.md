# PH7 at 8/9: the supported two-chain family cannot reach the critical ratio

**MathResearch96h-2 / original math-1. New WRITTEN candidate with exact rational checks, not independent review or novelty acceptance.** Native observation before drafting: **Wed Oct 28 17:04:59 PDT2026**. This is a mathematically scoped obstruction to ONE explicit construction family, not an all-topology PH7 exclusion or a decision of the original seven-versus-eight question.

## 1. Why this is the relevant remaining problem

The superseding owner direction permits bounded scientific calculations and prospective source work. The existing final-report/source record says the unrestricted PH6 boundary has already been written-supported: PH order at most six iff `z=beta^2<=1/2`. Hence there is no new PH6 region to discover within this same registered family without revisiting that result. Main explicitly agreed to redirect this slot to the actual PH7 gap.

The complete earlier ordinary-written parent `PH7-entire-rational-seven-ninths-band-parent-v1.md` records an ACTUAL seven-state family on a closed interval through7/9 and some algebraic continuation, but leaves `z=8/9` open. Its same-matrix family is explicitly defined in `PH7-u-deformation-actual-family-v1.md` (201LF; SHA256 `9f9b048bd4113b5008bdebf56f1e5d903e06e0b6ffe1f8eed78dbcd7ebb1a01e`) §2–3, and specialized/rationally verified in `PH7-rational-uniform-band-seven-ninths-v1.md` (364LF; SHA256 `ef6df980b2fbb5545a42ed7f3c72f17cea6f26f7148065670c104838f9a0c0f7`) §2–3. Its independent positive diagonal normalization and original row ties are part of the family; no use is made of withdrawn controls or held guidance as an accepted premise.

**Question tested:** can the same THREE-upstream / one-center / THREE-downstream construction, allowing its entire free positive upstream rate u, be made physically valid at `z=8/9` merely by choosing a different u? The finite grid alone cannot answer this. The exact theorem below answers it for ALL real u>0.

## 2. The exact family and complete physical antecedents

Normalize d=1 and write `y=s+c`, c>0,

    D_z(y)=y[(y+1)^2+z]^2,       K=D_z(c).

The family's raw matrix G has upstream Jordan chain J_u, downstream J_1, a center with holding w, upstream-to-center and center-to-downstream unit links, backward entries D_1,D_2,D_3 and last-to-center feedback phi:

    J_u=[-u,1,0; 0,-u,1; 0,0,-u],
    G=[ J_u   e_3   0
        0      -w  e_1^T
        D       f   J_1 ],
    D=[(D_1,0,0);(D_2,0,0);(D_3,0,0)],  f=(0,0,phi)^T,
    beta=(C,B,1,0,0,0,0),  gamma=K e_7.

The physical realization is the POSITIVE diagonal similarity of `G-cI`: with h>0 satisfying `(G-cI)h=-gamma`, set `T=diag(h)^(-1)(G-cI)diag(h)`, `alpha=beta diag(h)`, `omega=diag(h)^(-1)gamma`. Literal PH feasibility requires alpha>=0 and T Metzler. In particular `B>=0`, `C>=0` and `phi>=0`, because positive diagonal similarity cannot change the sign of an off-diagonal entry. Zero coefficients are allowed in these necessary conditions.

The same-matrix coefficient equations use

    a=3u+3,  b=3u^2+9u+3,
    c3=u^3+9u^2+9u+1,  e4=3u^3+9u^2+3u,
    h0=b+4a-a^2-6,  L=b-4a+10-2z,
    N=4h0+4-c3-b(4-a)-4z,
    L p=N,
    q=(a-4)p+h0-2z,  w=p+4-a,
    B=p-2u,  C=q-up+u^2,
    phi=e4+c3*w-[(6+2z)q+(4+4z)p+(1+z)^2].

The letters a,b in this coefficient list are SIX-rate symmetric-polynomial names, not the original pole parameters. The algebraic identity `Q(y)=(y+u)^2+B(y+u)+C=y^2+p y+q` follows immediately. No independent hidden polynomial or separately chosen input is substituted.

## 3. Theorem at the entire critical-ratio family

**Theorem.** For `z=8/9`, no u>0 in the entire above family admits `B>=0`, `C>=0` and `phi>=0` simultaneously. This holds even before requiring nonnegativity of D_1,D_2,D_3, the normalizing vector h or the remaining PH conditions. At `L=0` the same coefficient equations have no solution p. Thus no positive diagonal normalization of this specified chain is a critical-ratio PH7 realization.

At z=8/9 the coefficient identities reduce to

    L(u)=3u^2-3u-7/9,
    N(u)=8u^3-9u^2+3u-32/9,
    q L=Q_*(u),
    -243 L phi=P_*(u),

where

    Q_*(u)=6u^4-8u^3+(25/3)u^2-(32/3)u+400/81,
    P_*(u)=243u^6-729u^5+2025u^4-5859u^3
             +9360u^2-7776u+3184.

The complete algebraic substitutions were checked coefficientwise over rational numbers by the independent checker in §6. Section4 below gives a finite exact sign certificate proving BOTH `Q_*(u)>0` and `P_*(u)>0` for every u>=0.

Suppose L!=0 and physical input nonnegativity B,C>=0 held. Since u>0,

    q=u^2+uB+C>0.

But `q L=Q_*(u)>0`; therefore L>0. The second identity then gives

    phi=-P_*(u)/(243 L)<0,

contradicting the necessary Metzler condition phi>=0. This uses no assumption that a hidden quadratic is independently Hurwitz: q>0 follows from the actual input coefficients and u>0.

At L=0, degree-four matching requires N=0 as well. Exact division gives

    N(u)=((8u-1)/3)L(u)+(110u-103)/27.

Simultaneous L=N=0 would force u=103/110, which lies in(0,1), but there `L=3u(u-1)-7/9<0`. Thus even the singular coefficient-matching boundary supplies no omitted p. The proof includes all zero B/C and all positive u; no finite-grid inference is used for this conclusion.

## 4. Explicit positivity certificate — no root oracle

For a polynomial P of degree m on an interval `[a,b]`, put `u=a+(b-a)t`, `0<=t<=1`. Its Bernstein representation is

    P(u)=sum_(j=0)^m B_j binom(m,j)t^j(1-t)^(m-j).

If all B_j>0 then P>0 throughout the closed interval, including endpoints. Exact coefficients for P_* are:

|u interval|degree-6 Bernstein coefficients, in order|
|---|---|
|[0,1/2]|`3184, 2536, 2044, 267421/160, 111197/80, 75277/64, 64717/64`|
|[1/2,1]|`64717/64, 54157/64, 58397/80, 102973/160, 2864/5, 508, 448`|
|[1,3/2]|`448, 388, 1664/5, 8999/32, 19241/80, 14731/64, 18529/64`|
|[3/2,2]|`18529/64, 22327/64, 38231/80, 114547/160, 11221/10, 1783, 2824`|

All are strictly positive. For the remaining ray write u=2+t, t>=0:

    P_*(2+t)=2824+12492t+22806t^2+20061t^3
                  +9315t^4+2187t^5+243t^6>0.

Exact degree-4 Bernstein coefficients for Q_* are:

|u interval|degree-4 Bernstein coefficients, in order|
|---|---|
|[0,1/2]|`400/81, 292/81, 1697/648, 1121/648, 689/648`|
|[1/2,3/4]|`689/648, 473/648, 293/648, 1273/5184, 1547/10368`|
|[3/4,1]|`1547/10368, 137/2592, 173/2592, 149/648, 49/81`|

For u=1+t, t>=0,

    Q_*(1+t)=49/81+6t+(61/3)t^2+16t^3+6t^4>0.

These closed intervals plus rays cover all u>=0. Every coefficient shown is strictly positive; the certificate is independently reproducible by exact polynomial coefficient conversion, not by numerical root fitting or a sign grid.

## 5. A non-effective open neighborhood, still only for this family

The same obstruction persists on SOME open z-neighborhood of8/9, uniformly over u>=0. This does NOT give a numerical endpoint.

Define `Q_z(u)=L(u,z)q(u,z)` and `P_z(u)=-243 L(u,z)phi(u,z)` by clearing L algebraically in the §2 equations. They are polynomials jointly continuous in(z,u), with degree4 and6 in u and leading coefficients6 and243 respectively, independent of z. Compactify the u-ray by `t=u/(1+u)` and form

    qhat(z,t)=(1-t)^4 Q_z(t/(1-t)),
    phat(z,t)=(1-t)^6 P_z(t/(1-t)),

extended at t=1 by those positive leading coefficients. These are continuous on a compact z-by-t rectangle. At z=8/9 they are strictly positive for all t∈[0,1] by §4, including t=1. Their minima are therefore positive, and uniform continuity supplies an actual open neighborhood of8/9 on which both remain positive for ALL u>=0.

The singular L=N=0 boundary is also absent in some neighborhood. Here `L(u,z)=3u^2-3u+1-2z`; for z near8/9 its constant term is negative, so it has exactly one positive root `u_+(z)`, continuously depending on z. At8/9 that root exceeds1, while N modulo L is `(110u-103)/27`, hence N is strictly positive at u_+. By continuity N stays nonzero at the unique positive root for sufficiently nearby z. Thus the matching system has no singular positive-u solution in that neighborhood either.

On this COMMON neighborhood, any physical B,C>=0 again force q>0 and hence L>0, so phi<0. This is an existence proof of a positive-width obstruction band for the SAME fixed-chain/diagonal-normalization family. Its width is NOT evaluated and no explicit numeric endpoint is claimed. It does not compare the unknown neighborhood with the earlier z_star or prove any gap of the full PH7 feasibility set.

## 6. What was actually executed and independently checkable artifacts

All scripts below are NEW under the exclusive owner root. No frozen source was edited. Executed checks:

1. `python3 frontier-20261028-ph7-chain-search.py` — 4001 exact Fraction grid points u∈[1/2,5/2] at z=8/9; **0 hits** requiring p,q,w,B,C,phi,D1,D2,D3>=0. Its best observed minimum is `-337576152226472643643/434004129000000000000` at `u=1551/1000`. This is a FINITE exploratory observation only, not the all-u theorem. Result JSON SHA256 `d65f8e377cdf83cd2e3067e190f720fe217cc75bbfaaf8dade5225945927350c`; script SHA256 `6c9346aaa7e21b078f6650af21b5e11d759294fedd9263d51ae82f71b14522d3`.
2. `python3 frontier-20261028-ph7-phi-sturm.py` — exact Fraction polynomial/Sturm analysis of the stated family. Reported zero positive roots of the critical phi numerator and zero positive roots of q numerator. This is a cross-check of symbolic signs, NOT independent PH feasibility or formal proof. JSON SHA256 `c1f2d5ddab4c63825c5433b1f16d06a01d724f956f6d1fc32da1db1f6203ead0`; script SHA256 `935c962112f25cf17e15177877e74f985a56de8f4fcd5090c05275d27a8c5767`.
3. `python3 frontier-20261028-chain-obstruction-check.py` — EXACT `fractions.Fraction` verification of coefficient identities, singular remainder, every Bernstein coefficient in §4 and shifted-tail coefficients. It completed successfully and wrote `frontier-20261028-chain-obstruction-certificate.json` SHA256 `0ce1f4df9ef2f0de461f676b324ceff9e8be86eb14d4e6ba82774bc9ef2cf0bc`; checker SHA256 `6044b0e702548c19c2b493f369d690732326b0b9dc783b6a61e427cf5c72d268`.

The last checker verifies exactly the stated algebra/sign certificates. It does not verify the source's entire earlier seven-state construction, establish a PH7 global lower bound, reprove the historical PH6 theorem, or constitute independent-family/formal/kernel review. The remaining compactness/continuity paragraph is written mathematics; no numerical interval margin is claimed.

## 7. Honest residual and next useful scientific step

**Falsified design premise:** tuning the single upstream rate u in the published 3+3 chain cannot reach z=8/9 while retaining its actual nonnegative input and last-to-center feedback. The singular matching case cannot rescue it. A small whole-u obstruction neighborhood follows, but only for this particular coefficient family.

**Still open:** a PH7 realization with other topology, nonuniform internal rates, other feedback supports or another actual input/exit; a topology-unrestricted PH7 exclusion; exact original minimum at8/9 and the full minimum-order function. We have not shown that the supported A-or-B equivalence reduces to this chain. A useful NEXT step must genuinely enlarge or replace the chain's internal degrees of freedom and enforce the SAME actual input, output, characteristic and nonnegative generator ties; it cannot infer global impossibility from this chart barrier.

Prior quarantines remain historical/unvalidated, not correctness inputs. The new direction permits fresh independent calculations but does not retroactively convert any prior held result or process finding to success. No claimed literature priority, independent external-model review, formal/kernel acceptance, numerical-witness PH7 or publication follows. Same exclusive NEWroot; no Git/push/deletion/publication/secret access or external model API; original2026-10-31T21:23:27Z deadline remains.

**END — exact ALL-u obstruction at z=8/9 and some unevaluated uniform neighborhood, restricted to the specified actual PH7 chain family.**
