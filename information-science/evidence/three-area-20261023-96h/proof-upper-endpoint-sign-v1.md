# Exact sign of the sharp upper endpoint under the two positive causal premises

**Status: CANDIDATE / NOVELTY_UNCLEAR.** A written consequence inside the frozen bounded-real model. No scientific program or new target is introduced. This supplies the natural upper-endpoint counterpart to the main lower-endpoint threshold, including its degenerate equality cases. Binary special cases are prior work; a classical-corollary outcome remains possible.

## 1. Statement

Retain the main theorem's complete arbitrary-law model and notation. Assume the data are compatible and the two average causal premises of the surrogate paradox are positive:

    h=q-p>0,   gamma>0.

Let U be the sharp attainable upper endpoint for delta. Then

    U>=0.                                                   (1)

More precisely, U>0 if and only if at least one of the following holds:

**A.** mu_0([0,1))>0.

**B.** mu_0 is concentrated at 1, and simultaneously

    q<1,  mu_1([0,1))>0,  gamma<m_1.                       (2)

In every other compatible case satisfying the two positive premises, U=0. Thus such data can never force a strictly harmful treatment effect for every compatible law, although they can allow harmful effects, can force beneficial effects by the main threshold, or can exclude every strictly beneficial effect in the equality cases above.

Concentration of the subprobability mu_0 at 1 means mu_0({1})=p_0. Because h>0, p_0>0. In case B, gamma>0 and compatibility imply m_1>0 and hence p>0, so no empty-stratum exception is hidden in the conditions.

## 2. Elementary lower-tail fact

For a nonzero subprobability measure mu of mass P on [0,1], its lower-tail integral ell(x), 0<x<=P, satisfies

    ell(x)<x iff mu([0,1))>0.                              (3)

If mu is concentrated at 1, every selected mass x has integral x. Conversely, if mu has positive mass below 1, select an amount of that mass up to x and complete the remainder arbitrarily; its integral is strictly smaller than x. The minimizing tail therefore also has integral <x. This proves (3), including atoms and full-mass selection.

Also ell_s(x)<=m_s, since a nonnegative selected submeasure cannot have a larger first moment than the whole measure.

## 3. A positive law unless the control S_0=0 stratum is at the outcome ceiling

From the missing-outcome normalization,

    eta=gamma+m_0+p-m_1>m_0,                               (4)

because gamma>0 and m_1<=p. Choose switch masses r=h and t=0, which are feasible because h>0 and q<=1. The upper formula of the main theorem reduces to

    G_eta(h)=min(eta,h)-ell_0(h).                           (5)

Both eta and h are at least ell_0(h), by (4) and the tail bound ell_0(h)<=h. Thus (5) is nonnegative and U>=G_eta(h)>=0, proving (1).

If mu_0([0,1))>0, equation (3) gives ell_0(h)<h. Equation (4) also gives ell_0(h)<eta. Hence G_eta(h)>0, proving sufficiency of A by an actual attaining law from the main theorem. No additional causal assumption is used: r=h,t=0 is merely one permitted coupling in the unrestricted model.

## 4. Exact optimization when mu_0 is concentrated at 1

Now suppose mu_0 is concentrated at 1. Then m_0=p_0 and ell_0(r)=r for every feasible r. Compatibility's upper bound is

    gamma<=g_min+1=m_1,

so set

    kappa=m_1-gamma>=0.

The budget becomes

    eta=gamma+1-m_1=1-kappa.

Since m_1<=p and gamma>0, equation (4) gives eta>p_0>=r for every feasible r. Thus min(eta,r)=r. The main upper objective simplifies **exactly** to

    G_eta(r)
      =t+min(eta,r)-(t+eta-1)_+-ell_0(r)-ell_1(t)
      =t-(t-kappa)_+-ell_1(t)
      =min(t,kappa)-ell_1(t).                              (6)

As r ranges over I, t=r-h ranges over

    0<=t<=t_max=min(p,1-q).                                (7)

Therefore in this entire ceiling-stratum case,

    U=max_(0<=t<=t_max) [min(t,kappa)-ell_1(t)].             (8)

This includes all endpoint and zero-mass possibilities.

If q=1, then t_max=0 and U=0. If gamma=m_1, then kappa=0 and the objective is -ell_1(t)<=0, with value 0 at t=0; again U=0. If mu_1 is concentrated at 1, then ell_1(t)=t, so the objective min(t,kappa)-t<=0 and U=0.

These are exactly the failures of the three conditions in B. Conversely, if all conditions in B hold, then p>0, t_max>0 and kappa>0. Choose any t with

    0<t<=min(t_max,kappa).

Equation (3) gives ell_1(t)<t. Formula (6) then gives G_eta(h+t)=t-ell_1(t)>0. Thus U>0. This proves necessity and sufficiency of B, completing the theorem. QED.

## 5. Interpretation and boundary

The theorem does not deny the surrogate paradox: the sharp lower endpoint may be strictly negative, including in the main manuscript's explicit uniform example at gamma=2/5. It says that under the same coarse data interface and unrestricted latent dependence, the two positive causal premises always leave at least one nonharmful compatible law. Universal strict harm cannot be identified from those premises and the supplied information alone.

The exact exceptions to a **strictly beneficial** compatible law occur when the untreated S_0=0 factual outcomes are already at the known upper support bound, together with one of the additional restrictions identified in Section 4. Outcome support bounds therefore matter essentially; replacing [0,1] by an unbounded domain changes the problem and is not done here.

For binary factual data, write a,b,c,d as in the standalone reduction. Condition A is c>0; if c=0, condition B is q<1, d>0 and gamma<b. Thus U=0 exactly when c=0 and at least one of q=1, d=0 or gamma=b holds. This can also be read from the existing seven upper expressions, so the all-binary case is not a new result.

No clinical inference, finite-sample procedure, non-strong-surrogate theory, continuous-surrogate theorem or novelty clearance is claimed. This new written proposition still needs parent/independent checking; its status does not automatically inherit the main manuscript's earlier WRITTEN_CHECKED label. The Kuroki 2013 full-text gate remains ACCESS_BLOCKED.
