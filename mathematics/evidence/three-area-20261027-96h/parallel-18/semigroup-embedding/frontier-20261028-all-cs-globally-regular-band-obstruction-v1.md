# A finite original-class source has no globally regular-band-by-CS host

**NEW AUTHOR WRITTEN CANDIDATE with exact finite source check; UNREVIEWED and UNADOPTED.** Native check-start observation **Wed Oct 28 18:38:22 PDT 2026**. This is an unrestricted-CS-actor obstruction only for the **narrower target whose band is globally regular**. It is NOT an obstruction for all locally regular bands, not a solution to the original full target, not a printed-question equivalence or novelty claim. The general argument imports the standard regular-band left/right decomposition and standard Rees representation/coordinate facts at the explicitly stated points. Disjoint review and independent witness verification are essential before adoption.

## 1. Exact statement

There exists a 45-element regular, weakly E-unitary, locally r-orthodox semigroup S for which **no** injective homomorphism exists into any physical band-by-completely-simple product `P(B,D)` with B a globally regular band, for ANY completely simple D and ANY permitted group action on B.

More concretely, its actual syntactic actor q has18 elements and has two distinct same-q R-related idempotents e,f. Every band coefficient model over this SAME q with globally regular B necessarily has `β(e)=β(f)`. The latter is proved by a universal band identity argument, not a bounded host search. Section 5 justifies the extension from actual q to **arbitrary** CS actors for this finite source. If the actor-restriction/transport payment there fails review, retain only the independently proved same-q obstruction; do not infer the arbitrary-actor statement.

The original registered band variety is locally regular. A band can be locally regular without this note establishing that it is globally regular; the argument below does not apply to arbitrary bands in that larger permitted scope. Thus no negative answer to the original Q1 or Q2 follows.

## 2. Literal source and the actual R pair

Let A be the five-element monoid

```text
0 1 2 3 0
3 2 1 0 1
0 1 2 3 2
3 2 1 0 3
0 1 2 3 4
```

where 4 is the identity, and let `θ=(0,1,0,1,0):A→C2`. Equivalently A is `(R⋊C2)^1`, where the two-point right-zero R is swapped by the group. Let I=Λ={0,1,2} and

`P=((4,4,4),(4,1,3),(4,4,1))`.

Set `S=M[A;I,Λ;P]`, with product `(i,a,λ)(j,b,μ)=(i,a P_(λ,j) b,μ)`. Every P row and column contains the unit4, so regularity follows from a mutual inverse of a; E(A)={0,2,4} is a regular band. The entries 1 and3 have the same nonidentity θ-value and both satisfy `a p a=a` for every a in their inverse group fibre. The actor `r(i,a,λ)=(i,θ(a),λ)` is therefore onto and pure; the local-corner embedding into A shows S locally r-orthodox, and purity into a completely simple actor gives weak E-unitarity. These source assertions are also checked directly in §6.

Its group sandwich matrix is

`Q=((0,0,0),(0,1,1),(0,0,1))` over C2.

Because Q has first row/column zero and all rows and columns are distinct, a Rees-context K-array determines the group value from K_(0,0), the actor row from K_(ν,0), and the actor column from K_(0,k). Thus D=M[C2;3,3;Q] has equality as its syntactic congruence, and the pure map r is the actual q_τ. The exact source verifier exhausts all 46² actual/absent contexts per source element and confirms this conclusion rather than relying solely on the matrix criterion.

Put

`e=(1,1,1)`, `f=(1,3,1)`,
`a=(1,4,0)`, `b=(2,4,0)`, `z=(0,4,1)`, `s=(1,4,1)`.

Then e and f are DISTINCT idempotents with the SAME actor `(1,1,1)` and `ef=f`, `fe=e` (so e R f). Further,

`ab=a`, `ba=b`, `s(az)=e`, `s(bz)=f`.                    (1)

Both products in the last display use action weight the nonidentity element of C2. The source is globally nonorthodox and not locally inverse; it is not merely a repetition of an earlier orthodox/local-inverse target.

## 3. A regular-band four-term lemma

**Lemma.** Let B be a globally regular band. If `uv=u`, `vu=v`, and `E=xuy`, `F=xvy` satisfy `EF=F`, `FE=E`, then E=F.

Use the classical theorem of Kimura that every regular band embeds as the spined product of a left regular band L (`xyx=xy`) and a right regular band R (`xyx=yx`). Its full scope and these precise identities are stated in T. Quinn-Gregson, *Homogeneous Bands*, Advances in Mathematics 331 (2018), §2 and Definition 3.3, [DOI 10.1016/j.aim.2018.02.005](https://doi.org/10.1016/j.aim.2018.02.005); [accepted text](https://eprints.whiterose.ac.uk/id/eprint/129045/1/Homogeneous_bands.pdf). This is a **named classical import**, not independently proved here. Only the two coordinate projections and their joint injectivity are used; the automorphisms of B need NOT preserve the chosen projections for the argument.

In the R-coordinate, uv=u and vu=v force u=v: the right-regular identity gives `(uv)u=vu`, whose left side is u and right side is v. Hence E and F have the same R-coordinate. In the L-coordinate, EF=F and FE=E force E=F: the left-regular identity gives `(EF)E=EF`, whose left side is E and right side is F. Both coordinates agree, and the spined-product embedding is injective. This proves the lemma for finite or infinite B.

## 4. Every globally regular-band model over the actual q collapses e,f

Take any physical q-model with band B and its C2 action α. Write U=β(a), V=β(b), Z=β(z), X=β(s). Since ab=a and ba=b and the corresponding actor self-weights are the identity, the mixed product relations give

`UV=U`, `VU=V`.

Likewise both az and bz have identity action weight, so β(az)=UZ and β(bz)=VZ. Equation (1) and the common nontrivial action weight give

`β(e)=X α_1(U) α_1(Z)`,
`β(f)=X α_1(V) α_1(Z)`.

The automorphism α_1 preserves the two displayed left-zero equations. Since e and f have the SAME idempotent q-value, their actor self-weight is the identity; ef=f and fe=e therefore give

`β(e)β(f)=β(f)`, `β(f)β(e)=β(e)`.

The lemma in §3, with `u=α_1(U)`, `v=α_1(V)`, `x=X` and `y=α_1(Z)`, forces β(e)=β(f). Their actor coordinates also agree and e≠f. Therefore no such model is injective. This applies to EVERY globally regular B, every C2 action, infinite bands included, and every model satisfying the actual physical source relations. No enumeration of candidate bands is used in the universal conclusion.

## 5. Why an arbitrary CS actor cannot evade this finite-source obstruction

Suppose, for contradiction, that S embeds into `P(B,D0)` for an arbitrary CS semigroup D0 and globally regular band B. Let `t:S→D0` be the actor projection and T=t(S). T is finite. It is also completely simple, as follows.

View D0 in Rees coordinates. Each occupied T cell is a finite subsemigroup of the corresponding ambient H-class group, hence a subgroup and contains that cell's ambient group identity. All row/column cross-cells occur because products combine the left factor's row with the right factor's column. Given a∈T_(i,λ), b∈T_(j,μ), choose x and y to be the occupied-cell idempotents in T_(i,μ) and T_(j,λ). Then xby lies in the subgroup T_(i,λ); with its inverse z in that subgroup, `x b y z a=a`. Thus T is simple. Its idempotents are primitive because any idempotent order relation in T is one in D0, whose idempotent natural order is equality. The standard Rees–Suschkewitsch characterization now makes T completely simple.

The actor map t:S→T is onto and pure: over an idempotent CS coordinate the physical product has identity self-weight, so any band coordinate gives an idempotent; injectivity of the original embedding reflects this to S.

There are TWO distinct gauge/transport steps; neither may be omitted:

1. **Restrict the ambient actor to T without changing the regular band.** Choose Rees coordinates `T=M[H;J,M;Q]`, `D0=M[K;I,Λ;P0]`. The inclusion has ordinary Rees homomorphism coordinates

   `ι(j,h,μ)=(a(j),u_j φ(h) v_μ,b(μ))`,
   `v_μ P0_(b(μ),a(k)) u_k=φ(Q_(μ,k))`.

   Here φ:H→K is an injective group homomorphism. Let the T action be `α^T_h=α_(φ(h))`, and for s with t(s) in row j define the new coefficient `β_T(s)=α_(u_j^(-1))(β_0(s))`. The ambient product weight for source factors in rows j,k is `u_j φ(h Q_(μ,k)) u_k^(-1)`. Applying α_(u_j^(-1)) to the original host equation gives the T-host equation exactly. Equality of transformed coefficients and T actors gives equality of original coefficients/actors (the common T row fixes u_j), so this T-host remains faithful. B itself is unchanged and still globally regular. The Rees coordinate formula is the standard elementary factorization reconstructed in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md` §3; its derivation does not require the map to be onto.

2. **Push the pure onto T actor to the ACTUAL q.** Since t is onto and pure, `τ_S=t^(-1)(τ_T)` by lifting actual contexts and reflecting idempotence. The onto map `T→T/τ_T` is pure and between CS semigroups. The explicit gauge pushforward reconstructed in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, transports the faithful T-host to a faithful actual-q host with band `(J×M)×B`. Its group map is an isomorphism on local groups. A rectangular band and the product of two globally regular bands are globally regular; thus the new band is globally regular.

Section 4 rules out that actual-q host. This contradiction proves the any-CS-actor statement at the declared globally-regular-band scope, conditional only on the named classical and actor-transport inputs. It does NOT rule out a locally-regular-but-not-globally-regular band. The finite-image argument is essential here; no claim is made that an arbitrary nonregular or infinite subsemigroup of a CS semigroup is CS.

## 6. Exact source verification and standing gap

`frontier-20261028-ambiguous-regular-band-obstruction-checker-v1.py`, SHA `96bf6200eae58ce0a49db6f3496c1771ebc7ed0e83c2ad15de15d8707ab07601`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 18:38:22 PDT 2026**, exit0:

```text
source=45 idempotents=24 actual_actor=18
PASS associativity, regularity, weak-E, local r-orthodox, nonorthodox, non-locally-inverse
PASS purity and actual tau via 46^2 contexts/source
same-q R-idempotents e,f= (1, 1, 1) (1, 3, 1) ; ef,fe= (1, 3, 1) (1, 1, 1)
left-zero source a,b= (1, 4, 0) (2, 4, 0) ; e=s(az), f=s(bz), equal action weight=1
```

The program checks a literal table and all finite source identities only; it does NOT enumerate all regular bands and is not a proof of the infinite-target obstruction. That obstruction is the written universal §3–5 argument, with the named Kimura/Rees imports. The unrelated earlier bounded solver exploration `frontier-20261028-ambiguous-row-regular-band-search-v1.py` used a DIFFERENT P and is not evidence for this source; no UNSAT solver verdict is used here.

This finite source lies beyond the previous row-coded theorem: its second row contains distinct entries 1 and3 with the same θ-value. The previously proved row-coded family and eight-band example therefore remain compatible with this obstruction. No conclusion about the original locally-regular target, all-source canonical R/L, the printed Q1/Q2, source novelty or independent certification is asserted.
