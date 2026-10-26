# Candidate v1 — local officer moments enlarge the four-active-value exclusion

Observed before creation: `2026-10-23T14:54:00-0700`. PhysicsAME46, physics-6. Continued OWN AME support research. Written only; no program, enumeration, solver, numerical tensor, compilation or model CLI.

## Scope and dependency

The main new consequence is a complete WRITTEN exclusion of every support48/e0 configuration having **exactly four active local values in each coordinate**, regardless of its initially proposed positive deficits. It reduces such a configuration to the newly excluded{3,3,3,3}⁴ profile.

Dependency: `profile3333-exclusion-v1.md`, SHA256 `5e1907bd1b0f60f19e32ac4d19287f7dc4b466de5dfff72cc81890c71a3cec27`, still an author candidate awaiting separate reconstruction. This addendum is therefore also CANDIDATE / PARTIAL, not accepted lower49 or a full support48 exclusion.

## 1. The local moment identity is an existing officer-placement consequence

Use T for officers, t=|T|, h=36−t, V_i={a:d_(i,a)>0}, v_i=|V_i| and c(x)=|{i:x_i∈V_i}|. For a fixed active value a of coordinate i, write d=d_(i,a) and S_i=Σ_(j!=i)v_j. Then

    |{x∈T:x_i=a}|=6−d,
    Σ_(x∈T:x_i=a) (c(x)−1)=S_i−3d.                  (L)

Indeed, for each partner j, exactly v_j−d of the active pair-lines(a,b), b∈V_j, carry an officer. Summing over the three partners counts the other active coordinates of the officers with x_i=a. This is exactly the historical officer-placement C3 fact in ENGINE_V3.r1.md LF49–57, summed locally. It is not claimed as a new underlying mechanism.

All these identities hold for arbitrary AME amplitudes and every e: they use only officer-code exclusivity and the exact six two-party pair-line norms, not equal-modulus or phase assumptions.

If all officers have c=2, equation(L) becomes

    S_i−3d=6−d,       d=(S_i−6)/2.                   (E2)

If all officers have c∈{2,3}, it instead gives

    6−d ≤ S_i−3d ≤ 2(6−d),
    S_i−12 ≤ d ≤ floor((S_i−6)/2).                  (E23)

These restrictions are on EVERY active value separately, not merely average deficits.

## 2. Complete corollary: active alphabet sizes(4,4,4,4) are impossible at support48/e0

Assume h=12,t=24 and v=(4,4,4,4). The existing global officer identities give

    κ1=Σ_Tc=6·16−48=48,
    κ2=Σ_T binom(c,2)=6·16−72=24.

Therefore Σ_T(c−1)(c−2)/2=κ2−κ1+t=0. Every summand is nonnegative for integer c, so every officer has c∈{1,2}. Its average isκ1/t=2, forcing **all officers to have c=2**.

For any i, S_i=12. Equation(E2) forces every positive deficit to be3. There are four such values in every coordinate, so the initially arbitrary profile is necessarily{3,3,3,3}⁴. The dependency's derived normal form/two-forced-lines contradiction excludes it at e=0.

**Candidate corollary.** No e=0 AME(4,6) with h=12 can have v_1=v_2=v_3=v_4=4. Equivalently the entire four-active-values-per-coordinate stratum at support48 is excluded, not just a hand-picked choice of its deficits. This remains a partial result towards the unrestricted numerical bound.

## 3. Two precisely narrowed residual strata, not additional exclusions

These computations identify actual remaining obligations. They are NOT claimed nonexistence results.

### Active alphabet sizes(4,4,4,5)

Here κ1=6·17−48=54 and κ2=108−72=36. Hence

    Σ_T(c−2)(c−3)/2=κ2−2κ1+3t=36−108+72=0.

Every officer has c∈{2,3}. In a four-active-value coordinate, S_i=13 and(E23) gives d≤3. Four positive deficits≥2 sum to12, forcing all four to be3. In the five-active-value coordinate, S_i=12 likewise gives d≤3. Five positive deficits sum to12, so they are exactly3,3,2,2,2.

Thus this whole active-size stratum can only have profile

    {3,3,3,3}³ {3,3,2,2,2}.

There are six c=3 officers and eighteen c=2 officers, from κ1=54 and t=24. This is a surviving three-/four-thick-axis obligation, not covered by the previous entirely-thin-axis theorem.

### Active alphabet sizes(3,5,5,5)

Here κ1=6·18−48=60 and κ2=120−72=48, so the same nonnegative sum is48−120+72=0. Again c∈{2,3}. For the three-value coordinate, S_i=15 and(E23) gives d≤4. Three positive deficits sum to12, forcing4,4,4. In a five-value coordinate S_i=13 gives d≤3, so its deficits are3,3,2,2,2.

Thus this whole stratum can only have profile

    {4,4,4} {3,3,2,2,2}³.

There are twelve officers of each active weight2 and3. This is likewise a narrowed residual profile, not excluded here.

## Verification boundary and next obligation

All displayed identities are symbolic written counts; no finite program or scientific arithmetic cell was run. The first corollary depends on the complete normal-form exclusion's still-pending correctness check. The two residual profiles require a new coherent-support/phase compatibility obstruction or an exact state, not a re-count of old48 certificates. Other active-size patterns and all required e>0 support48 cases remain outside this addendum. The unrestricted documented bound is unchanged48..60.
