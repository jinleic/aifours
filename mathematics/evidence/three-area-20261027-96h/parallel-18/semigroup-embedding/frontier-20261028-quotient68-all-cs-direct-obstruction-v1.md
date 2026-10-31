# A direct all-CS-actor regular-band obstruction for the 68-source

**Status: NEW AUTHOR WRITTEN PROOF; UNREVIEWED / UNADOPTED.** This removes the actor-transport dependency from `frontier-20261028-quotient68-global-regular-obstruction-v1.md`, SHA `db8e2f41a747f59a4c25bed83bd4c6b89232e3fb6a31c88c38a9c7d1a13b2335`. It rules out globally regular bands only. The same source has the explicit seminormal/locally-regular-band host in `frontier-20261028-quotient68-sixband-host-and-obstruction-v1.md`, SHA `b24ce079030e75e6f1d5dfaa2a88696f4531eb53963f507c0876d4b0ad9f599c`, so this is NOT a counterexample to original Q1.

## 1. An arbitrary-actor criterion

Let S contain distinct idempotents e,f and elements a,s,t,v,u satisfying

`ef=f`, `fe=e`, `ae=af`, `e=stv`, `f=sv=utv`.          (1)

Then **no** homomorphism of S into any physical `P(B,D)` with globally regular band B and completely simple D can separate e,f. This statement is independent of finiteness, source regularity, purity, the syntactic actor, and actor-transport theorems.

Proof. Write D as `M[G;I,Λ;P]`, and let r be the actor projection of an arbitrary physical homomorphism. Since `r(e)r(f)=r(f)` and both actors are idempotents, their Rees rows agree. Since `r(a)r(e)=r(a)r(f)`, their Rees columns agree. A CS Rees cell contains only one idempotent, so

`r(e)=r(f)=d∈E(D)`.                                      (2)

Write `r(x)=(i_x,g_x,λ_x)` for x=s,t,v,u. Put

`A=g_s P_(λ_s,i_t)`,  `K=g_t P_(λ_t,i_v)`,
`C=g_s P_(λ_s,i_v)`,  `W=g_u P_(λ_u,i_t)`.

Because `r(stv)=r(sv)` and `r(utv)=r(sv)` by (1), compare their Rees group coordinates and cancel the common `g_v` on the right. This gives

`A K=C=W K`, hence `A=W`.                               (3)

Let `c_x` be the band coordinate of the image of x and write α for the G action. Physical multiplication, (3), and (1) give

`c_e = c_s · α_A(c_t) · α_C(c_v)`,
`c_f = c_s · α_C(c_v) = c_u · α_A(c_t) · α_C(c_v)`.

Set `V=c_s`, `P₀=α_A(c_t)`, `Q₀=α_C(c_v)`, `U=c_u`, `E=c_e`, `F=c_f`. Then

`E=V P₀ Q₀`, `F=V Q₀=U P₀ Q₀`.                       (4)

Since fe=e and both actor coordinates are the same idempotent d, its self-action weight is the identity; hence `F E=E`.

In a regular band, substituting `x=Q₀,y=V,z=P₀` into `xyxzx=xyzx` and multiplying by V on the left yields

`(V Q₀)(P₀ Q₀)=(V Q₀)(V P₀ Q₀)`.

The left side equals F because `F=U(P₀Q₀)` and `(P₀Q₀)²=P₀Q₀`; the right side is FE=E. Thus E=F. Together with (2), the physical images of e and f agree. □

No actor restriction, subgroup gauge, coinduction or comparison with actual q was used. In particular the statement applies to infinite B and D and arbitrary actions.

## 2. Exact source application and limitations

The pinned 68-source satisfies (1) with indices

`(a,s,t,v,u,e,f)=(0,8,24,53,60,37,61)`.

Its 68×68 table and actual actor map are in `frontier-20261028-quotient68-faithful-host-data-v1.json`, SHA `64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf`. The independent-from-Z3 checker `frontier-20261028-quotient68-faithful-host-checker-v1.py`, SHA `694d037f52e02a0c9cf00eb426bdaa04043930bb035e3877f19a11e395807f25`, checks the source quotient and (1), original WEU/local-r hypotheses, and the distinct same-q idempotents. The additional checker `frontier-20261028-quotient68-regular-collapse-checker-v1.py`, SHA `aa209250b31c29b8eede4bd2dfe6d2b497674206ded5763872f1466e7d09806f`, checks the four factor equations and both R products directly. These are same-author controls, not independent acceptance.

The six-element SN band from the positive host has `(V,P₀,Q₀,U,E,F)=(5,3,2,0,1,0)` satisfying (4), FE=E and E≠F; its direct table and seminormal checks are in the cited artifacts. The regular-band step is therefore genuinely unavailable in the larger printed/registered band variety. This all-actor obstruction applies only to the stricter globally-regular-band target, and does not solve the original Q1 or infer novelty, formal verification, or cross-model/human review.
