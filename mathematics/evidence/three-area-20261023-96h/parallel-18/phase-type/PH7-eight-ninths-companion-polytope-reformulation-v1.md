# PH7 at 8/9: observability split, companion-polytope form and the forced exit flag

The actual `/bin/date` returned before this manuscript was **Sun Oct 25 21:53:56 PDT 2026**. Owner: MathResearch96h-2, slot math-1.

Status: AUTHOR-WRITTEN CANDIDATE. It gives an exact REFORMULATION and NECESSARY structure only. It contains no PH7 witness, no empty-intersection proof, and no 8/9 decision. The minimum at 8/9 stays in {7,8}.

No interpreter, eval kernel, calculator, CAS, enumeration, solver, replay, native experiment, model CLI or nested agent was used. No scientific machine check is claimed. The derivation core was saved first in `checkpoint-056-companion-polytope-reformulation-v1.json`. That checkpoint also discloses that earlier private reasoning included approximate mental decimal evaluations. Those evaluations have ZERO credit, and nothing below uses them.

The method lineage is the classical cone and invariant-polytope characterization of positive realizations and PH representations (Ohta–Maeda–Kodama; O'Cinneide; Farina–Benvenuti). No novelty or priority is claimed.

## 1. Named imports and fixed notation

The named written imports are used at their existing assurance boundaries, not re-proved here:

- **B6**, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. No PH of order at most 6 exists for z>1/2.
- **The SCC/Perron-coordinate theorem**, `PH7-reducible-obstruction-and-Perron-coordinates-v1.md`, SHA256 `d0dea4e8ffdf8132dfa2460c7cc40a01e8834bcc47e981837f28410f605fd242`. Its parent disposition is `PH7-entire-reducible-SCC-parent-v1.md`, SHA256 `729e7e6c43c8d34f90ccb5f8975de74eb3c1848399b2c6c96021464ceab6051d`. It gives: every actual PH7 at 8/9 has exactly 7 states, its matrix G=T+cI is irreducible Metzler with spectral abscissa 0, and det(yI−G)=D_z(y)Q(y), where Q is monic and both roots of Q are strictly stable.

Fix the following:

- Normalize d=1 and put z=8/9, w=sqrt(z), s=1+z, y0=−1+iw.
- D_z(y)=y·chi(y), where chi(y)=(y²+2y+s)²=y⁴+4y³+(4+2s)y²+4s y+s².
- Write chi=y⁴+c3y³+c2y²+c1y+c0, so c3=4, c2=4+2s, c1=4s and c0=s².
- beta=alpha>=0 is the initial row and gamma=omega>=0 is the exit column.
- The scalar transfer is F(y)=beta(yI−G)^(−1)gamma=K/D_z(y), with K>0 and relative degree 5.

## 2. Lemma 1: the observability split

Let W be the span of the rows beta G^k, and Vc the span of the columns G^k gamma. The 7×7 Hankel matrix (beta G^(i+j) gamma) is the product of the observability rows and the reachability columns. Its rank is the McMillan degree 5 of F. By Sylvester's rank inequality and the product bound:

    5 >= dim W + dim Vc − 7,   dim W >= 5,   dim Vc >= 5.

So exactly one of the following holds:

- **Case I:** dim W = 5.
- **Case I\*:** dim Vc = 5.
- **Case II:** dim W = dim Vc = 6.

Actual PH time reversal maps W isomorphically onto Vc. The map is beta_rev T_rev^k = (T^k omega)^T V, with V the positive diagonal occupation matrix of the reversal (see Section 4 of `PH7-eight-ninths-two-complete-dominator-strata-v1.md`). Hence Case I\* is Case I for the actual reversed pair. No case is dropped.

## 3. Case I as a polytope

Let psi(tau)=beta exp(G tau) be the actual occupation row. In Case I, x→xG acts on the 5-dim space W. F(tau)=psi(tau)gamma has a simple pole at 0 and a double pole (requiring a Jordan block of size 2) at y0 and at its conjugate. So the action on W has characteristic polynomial exactly y·chi(y). Every psi_j therefore lies in the real 5-dim span V_F of

    1, e^(y0 tau), tau e^(y0 tau), and their conjugates.

G is irreducible with Perron root 0. Let pi be its left Perron vector. Then psi_j(tau)→kappa·pi_j>0. Put:

    psi~_j = psi_j/(kappa pi_j) = 1 + osc_j,
    G^_ij = pi_i G_ij / pi_j.

G^ is Metzler with zero column sums and has the same positive-edge graph as G. The occupation ODE gives the EXACT identity

    psi~_j' = sum_(i!=j) G^_ij (psi~_i − psi~_j).                      (INV)

Write v_j ∈ R⁴ for osc_j, and C for d/dtau on the 4-dim oscillating space. Then (INV) says C v_j = sum_(i≠j) G^_ij (v_i − v_j). So Pi=conv(v_1,...,v_7) is invariant under exp(C tau) for tau>=0.

Let l(v)=psi~_v(0) be the affine functional "value at time 0". Then l(v_j)=beta_j/(kappa pi_j)>=0. With theta_j=gamma_j kappa pi_j/A0 and A0=lim F, we get F/A0=sum theta_j psi~_j, a convex combination. So the normalized F-point v_F lies in Pi.

**All seven points are distinct vertices.** Let V' be the vertex set of Pi and suppose |V'|<=6. Each vertex v has C v in the tangent cone cone(v'−v : v'∈V'). That gives a Metzler M' with zero column sums and C v = sum M'_(v'v)(v'−v). For each vertex, f_v(tau):=l(exp(C tau)v) satisfies f' = f M'. Because l is affine and exp(C tau) is linear, f_v(tau)−f_u(tau)=l_lin(exp(C tau)(v−u)). Writing v_F as a convex combination of the vertices gives F=A0·sum theta'_v f_v.

Restrict to the states that can reach the support of theta' (no edge leaves that set's complement into it) and apply the positive resolvent normalization. This is an actual PH of order <=6 for the same F, which contradicts B6 at z>1/2.

The same construction shows that ANY exp(C tau)-invariant polytope with 7 vertices, lying in {l>=0} and containing v_F, gives an actual PH7. **So, at the named imports, Case-I PH7 exists if and only if such a 7-vertex polytope exists.**

## 4. Exact companion coordinates and the occupation transform

osc_F has nonzero tau e^(y0 tau) part (computed in 4.1), so it is a cyclic vector for C. Hence

    e_m = C^m v_F,  m = 0,1,2,3,

is a basis of R⁴. In this basis C is the companion matrix of chi: C e_m=e_(m+1) for m<3, and C e_3=−(c0e_0+c1e_1+c2e_2+c3e_3). Identify x=sum x_m e_m with the polynomial p_x(y)=x_0+x_1y+x_2y²+x_3y³. C then acts as multiplication by y modulo chi.

Relative degree 5 gives F^(m)(0)=0 for m<=3 and F^(4)(0)=K. With A0=K/s², this yields osc_F(0)=−1 and osc_F^(m)(0)=0 for m=1,2,3. Hence

    l(x) = 1 − x_0 = 1 − p_x(0).                                       (L)

Laplace transforms give L[osc_F]=(s²−chi)/(y chi). Also L[osc_(e_m)]=y^(m−1)s²/chi for m=1,2,3, using the vanishing initial derivatives. Collecting terms gives the exact occupation formula

    L[psi~_x](y) = l(x)/y + s² p_x(y)/(y chi(y)).                       (OCC)

For x=e_0 this returns s²/D_z=F/A0. The polynomial coordinates are related to the old complex coordinates by Q=p_x(y0) and P=p_x'(y0), and C becomes (P,Q)→(y0P+Q, y0Q).

### 4.1 Explicit v_F in the old complex coordinates

    v_F = ( −1 + i(1+3w²)/(2w³),  (1+w²)(1+iw)/(2w²) ).

The P-coordinate has real part −1. Re(y0P_F+Q_F) = 1−(1+3w²)/(2w²)+(1+w²)/(2w²) = 0 confirms F'(0)=0. These are written algebra only.

## 5. Distances, the exit lemma and the forced flag

Let d_j be the graph distance from supp(beta) to j. Then psi_j(tau) ~ (beta G^(d_j) e_j) tau^(d_j)/d_j!, with a positive coefficient. The m-th derivative of psi~_x at 0 equals −x_0(C^m x). The companion relations give:

- m=1: c0·x_3
- m=2: c0·x_2 − c0c3·x_3
- m=3: c0·x_1, when x_2=x_3=0

So distance d corresponds to exactly these strata:

- d=0: x_0<1.
- d=1: x_0=1 and x_3>0.
- d=2: x_0=1, x_3=0, x_2>0.
- d=3: x_0=1, x_2=x_3=0, x_1>0.
- d=4: x=e_0.

No state has d>4, because then its transform s²p/(y chi) would vanish identically.

**Exit lemma.** Suppose gamma_j>0 for some j with d_j<4. Then the coefficient of y^(4−d_j) in the numerator of sum gamma_j psi^_j receives only positive leading path terms, so the numerator is not constant. Therefore gamma lives on distance-4 states. Every distance-4 state sits at the single point e_0, and distinct states are distinct vertices, so there is EXACTLY ONE exit state, e. Conversely, any such support gives the constant numerator, so the transfer is K'/D_z automatically.

Distance-3 states lie on the open ray e_0+R_(>0)e_1. Three collinear points cannot all be vertices, so there is EXACTLY ONE distance-3 state, o.

Every forward edge raises distance by at most 1. Hence pred(e)={o} and pred(o) ⊂ D2∪{e}, where D_k is the set of distance-k states. From C v_e = t(v_o−v_e), with t=G^_(oe)>0:

    v_o = e_0 + e_1/t.                                                  (FLAG)

Column-sum zero at e gives t=−G_ee, the actual holding rate of e. Let k_1=|D1| and k_2=|D2|. Then (|I|,k_1,k_2) with |I|+k_1+k_2=5, each part >=1, is one of six sub-types: (3,1,1), (2,2,1), (2,1,2), (1,3,1), (1,2,2), (1,1,3).

All non-initial points lie on {x_0=1}. That hyperplane supports Pi by (L), and its face contains the affinely independent flag e_0, v_o, a D2 point and a D1 point. So it is a FACET. The graph is a forward chain I→D1→D2→o→e with arbitrary backward edges. This is the two-strata class A, now with its upstream block forced to this distance structure.

## 6. Exact cone identities

All rates below are the actual G^ entries (nonnegative).

**At o.** For D2 points v_j=e_0+a_je_1+b_je_2 with b_j>0:

    sum_(j∈D2) lambda_j b_j = 1/t,
    sum_(j∈D2) lambda_j a_j = 1 + (sum lambda_j + mu)/t,

where lambda_j=G^_(j o) and mu=G^_(e o).

**At s∈D2** with v_s=e_0+ae_1+be_2: C v_s = e_1+ae_2+be_3. Only D1 points have an e_3 coordinate, namely c_j>0. Hence

    sum_(j∈D1) G^_(j s) c_j = b > 0.

**At r∈D1** with v_r=e_0+ae_1+be_2+ce_3:

    C v_r = −c c0 e_0 + (1−c c1)e_1 + (a−c c2)e_2 + (b−c c3)e_3.

Only initial points have x_0≠1. The e_0 coefficient therefore gives

    sum_(i∈I) G^_(i r) l_i = c·s².                                     (D1)

**At i∈I:** −c0 x_(3,i) = sum_(j) G^_(j i)(l_i − l_j).

**Barycenter.** Let r>0 be the right Perron vector of G^. Then C(sum r_j v_j)=sum r_j C v_j=0 and C is invertible, so sum r_j p_j ≡ 0. Its constant term gives sum_(I) r_i l_i = sum_(all) r_j. Its y³ term gives sum_(D1) r_j c_j + sum_(I) r_i x_(3,i) = 0, so some initial point has x_3<0.

**Q-projection.** The map x→p_x(y0) is a quotient by the invariant eigenplane E_P=(y²+2y+s)·R[y]_(<=1). Its image polygon is invariant under multiplication by y0.

- Suppose that polygon were a triangle. Then a 3-state CTMC would have eigenvalue y0. For any centered 3×3 Metzler matrix, tr X²>=0 forces (Im)²<=(Re)²/3, but here z=8/9>1/3. So the polygon has at least 4 vertices.
- The same bound gives a P-slice Pi∩E_P with at least 4 vertices.

## 7. Case II: only six combinatorial types

In Case II, W adds one real hidden root −q (q>0; strictly stable by the SCC import). The normalized points lie in R⁵, and all 7 are vertices by the same B6 argument as in Section 3. Seven vertices of a 5-polytope have a 1-dimensional Gale diagram, given by the unique affine dependency z (sum z_j=0, sum z_j v_j=0).

From Lambda G^ = A~ Lambda, where Lambda has columns (1,v_j), we get G^ z = h' z, with h' the beta-unobservable hidden root. Let a=#{z>0}, b=#{z<0} and c=#{z=0}. The vertex condition forces a,b>=2. Then Pi is the c-fold pyramid over Delta_(a−1)⊕Delta_(b−1) (Grünbaum, d+2 vertices). With a<=b, the only types are

    (a,b,c) = (2,2,3), (2,3,2), (2,4,1), (2,5,0), (3,3,1), (3,4,0).

## 8. A necessary Jordan–CTMC condition

F has a double pole at y0, so G and the CTMC generator G^^T have a Jordan block of size >=2 at y0. Let L=G^^T, pi~ its stationary law, and Q and m right y0-eigenvectors of L and of its time reversal, with Q in range(L−y0). Then

    sum_j pi~_j m_j Q_j = 0.

Trace, moment, Newton and JLL tests see only spectra. So they cannot separate this condition from a semisimple double eigenvalue. Whether 7-state semisimple double spectra reach z=8/9 is NOT evaluated here.

## 9. Exact remaining gap

Case-I PH7 at 8/9 holds if and only if the companion system has a solution with:

- 7 vertices in {x_0<=1};
- the flag (FLAG);
- the cone identities of Section 6 for ALL rates;
- one of the six sub-types.

Case II reduces to six explicit 5-polytope types. Neither feasibility nor emptiness is proved here. This is a necessary/iff interface at the named imports, not a resolution. No formal, kernel, human, cross-vendor or novelty acceptance is claimed. HOLD, root, cutoff, deadline and cadence are unchanged.
