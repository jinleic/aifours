# Sharp cross-objective overlap exponent for all first-order-near-optimal laws

**AUTHOR CANDIDATE — WRITTEN with exact rational exponent controls; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:58:20 PDT 2026`.

## 1. Original full-private laws and precise sharpness statement

For b=e^(-epsilon)->0 let F_b consist of ALL Borel probability laws obeying epsilon privacy for EVERY Borel event and EVERY h in the FULL CLOSED unit l1 diamond D. Let L(mu)=E||X||_1 and J(mu)=E||X||_2^2.

Take ANY pair of actually feasible laws mu_b^L,mu_b^J which are each first-order near-optimal for their OWN objective:

    L(mu_b^L)<=2^(1/3)b^(1/3)+o(b^(1/3)),
    J(mu_b^J)<=[2/sqrt(3pi)]b^(1/2)+o(b^(1/2)).                        (1)

The preceding source-independent candidate theorems supply the corresponding all-law lower bounds, so these conditions really mean first-order near-optimality; neither law is assumed unique, centered or radial.

**Uniform-over-sequences exponent:** every such pair satisfies

    1-TV(mu_b^L,mu_b^J) = o(b^(1/18)).                                  (2)

**Power sharpness:** there exist explicitly constructed exact-epsilon pairs satisfying (1) such that

    1-TV(mu_b^L,mu_b^J) >= (1-o(1)) b^(1/18)/log_2(1/b).               (3)

Consequently for EVERY eta>0, no uniform `O(b^(1/18+eta))` overlap bound holds over all such near-optimal sequences. The little-o in (2) is essential: (3) does NOT claim a positive limiting coefficient at b^(1/18). Both laws still converge weakly to delta_0 and have TV->1. This result concerns ACTUAL all-event/full-closed-D laws, not an assumed source optimizer, and sharpens the earlier b^(1/8) counterexample.

## 2. Named author inputs, not accepted source theorems

The proof uses the two still-UNREVIEWED, source-independent peak-floor candidates:

- first norm `frontier-20261028-peak-floor-first-norm-universal-v1.md`, SHA `fa39d7bdc125da7c8f7424d5976309227d8101a58b15efea919e8eb8376f04ea`: its peak-floor decomposition, scaled first-norm bathtub deficit Delta_b->0, and first-order optimum;
- squared Euclidean `frontier-20261028-peak-floor-low-privacy-universal-v1.md`, SHA `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43`: the actual Euclidean density peak bound `M_J sqrt(b)=O(1)`, explicit first-order disk-shell law, and all-law value.

Both were derived without LAW642, v241, MDA, PMLR or f68 research premises, but they remain AUTHOR-WRITTEN and require review. This successor imports their EXACT peak/deficit statements, not a generic assumption that TV convergence alone controls shrinking balls. No original Euclidean optimizer uniqueness or source-priority claim enters.

## 3. Upper bound using the actual mean-law deficit

Write `s=b^(1/3)`. The first-norm peak-floor proof decomposes the ACTUAL density of mu_b^L as

    p_L = ell_b 1_(x_b+D) + g_b,
    ell_b=O(s),

with a scaled bounded bathtub radius `t_b<=K` and an exact nonnegative deficit `Delta_b->0`. No rate for Delta_b is assumed. For any `r>=2K s`, the l1-cost sublevel comparison gives

    mu_b^L(B_2(r)^c)
       <= 2ell_b + integral_(|x|_2>r)g_b(x)dx
       <= O(s) + 2s Delta_b/r.                                          (4)

Indeed `||z||_1>=||z||_2`; on scaled `|z|_2>r/s`, the target bathtub density vanishes and the deficit integrand is at least `(r/s-t_b)g_b^#`, which is at least `(r/(2s))g_b^#`.

The squared-Euclidean peak-floor result gives a uniform-for-this-sequence density cap `M_J<=C b^(-1/2)` for all sufficiently small b. Therefore for ANY r>0,

    mu_b^J(B_2(r)) <= pi r^2 M_J <= C' b^(-1/2)r^2.                    (5)

For probability densities, overlap is `1-TV=integral min(p_L,p_J)`. Splitting at B_2(r) gives

    1-TV <= mu_b^J(B_2(r)) + mu_b^L(B_2(r)^c).                         (6)

Choose the ACTUAL sequence-dependent radius

    r_b=max{ b^(5/18) Delta_b^(1/3), 2K b^(1/3) }.

If Delta_b=0 the first term is 0; all formulas below then use the second radius. Applying (4)–(6) and `max(u,v)^2<=u^2+v^2` gives

    1-TV <= C''[ b^(1/18)Delta_b^(2/3) + b^(1/6)+b^(1/3) ]
          = o(b^(1/18)),                                                  (7)

because Delta_b->0. No unproved rate of L1/TV convergence, no optimizer uniqueness and no estimate of a moving source threshold is used. This proves (2).

## 4. An explicit almost-matching construction

Let L_b be the actual fully private first-norm shell law with centered core `2^(1/3)b^(1/3)D`; let E_b be the actual fully private Euclidean shell law with centered disk core radius `(4/(3pi))^(1/4)b^(1/4)`. The named bounds make them first-order near-optimal for L and J respectively.

Introduce a THIRD actual private centered diamond-shell law B_b with core

    q_b D,      q_b=b^(5/18).

Let

    w_b=b^(1/18)/log_2(1/b),
    P_b=(1-w_b)L_b+w_b B_b,       Q_b=E_b.                               (8)

For sufficiently small b, 0<w_b<1. Geometric-layer moments give `L(B_b)=O(q_b)`, because `q_b^3=b^(5/6)>>b` and the first shell is smaller order. Thus

    w_b L(B_b) = O(b^(1/3)/log_2(1/b))=o(b^(1/3)).

The named all-law lower/upper bounds imply P_b is first-order mean-near-optimal, and E_b is first-order Euclidean-near-optimal. Convex mixing preserves the FULL closed-D/every-event inequality. A common far positive-quadrant rectangle is outside all compact cores; there every density drops by exactly b on the SAME e1 shift. Hence P_b and Q_b also have EXACT privacy parameter epsilon.

Because `q_b/b^(1/4)=b^(1/36)->0`, the whole component core q_b D lies inside E_b's top Euclidean disk for small b. Their exact normalizers satisfy

    Z_B ~ 2q_b^2,       Z_E ~ A0 b^(1/2),
    A0=pi(4/(3pi))^(1/2)=2sqrt(pi/3).

Consequently on q_b D,

    w_b p_B ~ [1/(2log_2(1/b))] b^(-1/2)
             < p_E ~ A0^(-1)b^(-1/2)

for all sufficiently small b. Also p_P>=w_b p_B. The overlap integral on that actual core is therefore at least

    integral_(q_b D) min(p_P,p_E) >= w_b Q_B(q_b D)=w_b(1-o(1)),

since its top-core mass tends to one. This proves (3). The construction is not a finite-parameter optimality claim about B_b or P_b.

## 5. Actual exact exponent controls

A bounded Fraction-only cell evaluated the scaling identities for b=2^(-k), using the base-2 logarithm in (8):

```text
b=2^- 36 weight= 1/144 relative_mean_contamination= 1/36 weight_over_b^(1/6)= 4/9
b=2^- 72 weight= 1/1152 relative_mean_contamination= 1/72 weight_over_b^(1/6)= 32/9
b=2^- 144 weight= 1/36864 relative_mean_contamination= 1/144 weight_over_b^(1/6)= 4096/9
critical_power=1/18; component_radius_power=5/18; 1/18+5/18=1/3
```

These exact samples check exponent algebra only; the universal little-o and explicit overlap proof are §§3–4.

## 6. Review and limits

The theorem is conditional on the TWO named unreviewed source-independent peak-floor bodies. Request disjoint review of the sequence-dependent Delta/r choice, all-law peak cap, actual core density comparison and common exact-epsilon event. It does not imply that the older exact-optimizer b^(1/6) coefficient is wrong, or that a uniform constant exists at exponent 1/18. No original theorem/review gate, source priority, novelty, formal/kernel/human/configured-family acceptance or nonadditive-channel result is claimed.
