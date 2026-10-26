# All-reference obligation — sharp pair scalar and explicit Q-quotient pivots

Before-creation clock observed: **2026-10-23T16:59:52-07:00**. PhysicsResearch96h. Intermediate unreviewed written work, no new scientific execution. The universal four-block polynomial request is still pending a named decision. These are helper identities for the SAME all-reference target, not separate discoveries or a complete target claim.

## 1. Universal sharp bound on E_ij

For a pair split use u=q_i+q_j, v=q_k+q_l, z=u+v and

`E_ij=(z+uv)/[4(4+z)]`.

Checkpoint001 proved E<=1/4. The complementary lower bound is

**`E_ij>=1/12`.**

Let T=x_i+x_j, V=1-T. Convexity of x/(1-x) gives

`u>=u0=2T/(2-T)`, `v>=v0=2V/(1+T)`.

The expression2(u+v)+3uv increases in both nonnegative variables. Direct algebra gives

`2(u0+v0)+3u0 v0=4`.

Therefore

`E_ij-1/12=[2z+3uv-4]/[12(4+z)]>=0`.

References with equal probabilities within each of the two pairs attain1/12; this explains the earlier constant paired scalar without assuming it persists as equality at generic spectra. Rank-one endpoints use the regular E formula from checkpoint005 and continuity. No full kernel/equality classification is added.

In particular the positive opposite edge alpha=1/4+E in the generic four-dimensional upper form lies in[1/3,1/2]. Its first two leading principal minors are already universally positive:

`det M_[1]=1`, `det M_[2]=1-alpha^2>=3/4`.

The remaining four-block burden is its third and fourth leading minors, not positivity inferred from these two.

## 2. Independent positive-coefficient factor for the second homogeneous minor

Use the polynomial matrix P=L M from `all-reference-four-polynomial-reduction-v1.md`. Put

`Q=(p0+p2)(p1+p3)`, `R=4W3-S(2S^2+Q)`.

Then

`L-P12=Dab Dcd R`,

`L+P12=Dab Dcd[4W3+S(2S^2+Q)]`.

Thus `f2=(L-P12)(L+P12)`. The second bracket has positive coefficients. So does the cubic

`R=2S^3+8S e2-4e3-SQ`.

Its exact coefficient classes are:

- p_i^3:2;
- p_i^2 p_j, i!=j in opposite parts of{0,2}|{1,3}:13;
- p_i^2 p_j in the same part:14;
- p_i p_j p_k with three distinct indices:30.

These exhaust its20 degree-three monomials. They follow by counting contributions from S^3, S e2, e3 and SQ, not by fitting or evaluating reference points. Consequently f1=L and f2 have nonnegative raw coefficients with strict positive pure-last values under every ordered-gap substitution. The proposed program's first two minor families can therefore serve as independently written algebraic controls; checking them does not create a new physical result. No source algorithm or admission scope was changed.

## 3. Explicit diagonal form of the nonzero-weight Q quotient

For a fixed a!=b, put T=x_a+x_b, V=1-T and O={j,k}. Retain

`A=diag(tau_i)`, `tau_a=tau_b=1/2`, `tau_j=tau_k=1`,

`f=A c`, `d=d_ab=(2-T)/2`,

`D_QQ=A-f f^T/d`.

For0<T<1, an orthonormal basis of c-perp is

`u_A=(c_b e_a-c_a e_b)/sqrt(T)`,

`u_O=(c_k e_j-c_j e_k)/sqrt(V)`,

`u_C=sqrt(V)*(c_a e_a+c_b e_b)/sqrt(T)`

`     -sqrt(T)*(c_j e_j+c_k e_k)/sqrt(V)`.

In this basis the upper Q quotient is exactly diagonal:

**`diag(1/2,1,1/(2-T))`.**

The first two vectors have zero f overlap and lie in constant A blocks. On u_C the A expectation is(1+T)/2 and the squared f overlap is TV/4, so subtracting the actual TV/(4d) gives1/(2-T). Cross entries vanish directly. Therefore the nonzero Q spectrum is uniformly between1/2 and1 for every reference, independent of the imbalance inside either pair. The intrinsic endpoint spectrum follows by continuity or directly from A; the normalized basis itself is not evaluated at T=0 or1.

For the lower form, retain the reference K=c in the Q space. Its lower block is4d and its pairing to Q-perp is4f†u. The lower Schur complement on Q-perp is

`3A+f f^T/d-4f f^T/d=3D_QQ`.

Thus its explicit quotient pivots are exactly three times the upper ones. This is not a lower sign proof on the remaining coupled coordinates, but it rules out a spurious reference-mode or Q-pivot singularity as a hidden residual.

## 4. Literal remaining matrices

Universal all-reference domination is still NOT PROVED and no exact failure is known. The outstanding conditions are:

- generic four-block leading minors3 and4 (the lower form follows conditionally once its upper is proved);
- both seven-dimensional Schur remainders of the nonzero12-weight blocks;
- both zero-charge12-dimensional remainders.

All four nonnegative Schmidt coefficients, including every zero/repeated value, remain in scope. A polynomial coefficient attempt may be sufficient if fully checked, but negative coefficients or positive finite assays do not settle these matrix signs. No additional compute, root search, CLI or nested agent is authorized by this checkpoint.
