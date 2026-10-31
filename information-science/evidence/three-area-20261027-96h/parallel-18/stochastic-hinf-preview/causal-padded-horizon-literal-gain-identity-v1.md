# Exact causal finite/infinite horizon identity for the same linear preview law

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:32:48 PDT 2026**. Admitted class-level literal-domain work, not diffusion-annihilating controller construction. Only supplied definitions/current exact controller class and ordinary strong linear-SDE uniqueness, causality and monotone norm limits are used. No new source or execution.

## 1. All-variable scope and explicit infinite-horizon admissibility interpretation

Fix arbitrary compatible real original matrices, positive dimensions, finite h>=0 and ONE deterministic stationary linear preview law with fixed K,L0,Lh,H as supplied. The SAME law/matrices/h are used for every horizon, zero initial state/history and zero extension of finite-window disturbances. No controller is retuned with the horizon.

For finite b>h, define G_b as the literal progressive-E2 gain with input interval [0,b-h] and original output interval [0,b], exactly as in the bound class. Gains may be extended-valued; this theorem does not import NR-GAIN or assume a finite operator bound merely from per-input E2 well-posedness.

For the infinite comparison, admit all canonical progressive inputs with finite expected squared energy on [0,infinity). Use the actual global LOCAL strong solution: restrict to each finite interval, apply permitted strong linear-SDE uniqueness/existence, and paste the consistent solutions. This law has no finite-time explosion and its control is E2 on every compact interval. NO global expected-control-L2, internal EMS or prescribed stability requirement is silently inferred. If an original infinite-horizon admissibility convention demands those additional properties, law eligibility under that convention remains a SEPARATE premise.

The original infinite output norm may be infinite. Define

`G_infinity=sup_(progressive E2 input, E||w||>0) E||z||_[0,infinity) / E||w||_[0,infinity)`.

The denominator is finite by Cauchy-Schwarz, with the actual expectation-of-path-norm convention. This is a precisely stated physical comparison domain, not certification of all unspecified book conventions.

**Theorem.** In the extended reals,

**G_infinity = sup_(b>h) G_b.**                               (H)

The proof must account for the current preview tap; directly replacing an infinite input by its cutoff at b-h does NOT preserve the original output up to b. A padded horizon is essential to the caller below.

## 2. Exact actual-input causality, all window and noise terms

If two progressive input processes coincide on [0,t], their original controller feedforward terms coincide there: every window argument at time s<=t is at most s, and both endpoints/kernel use no future beyond that time. The original closed-loop state equations have identical forcing through t. Strong uniqueness on this interval at the SAME Brownian motion and initial state gives identical actual states, controls and outputs through t.

This includes B0 control-noise coupling, A0 state noise, K feedback, the current/left taps and the entire supplied L2 kernel. It is not a statement about separate deterministic-input versions or conditioning on a future random input path. No stochastic independence or realization is needed.

## 3. Every finite-horizon actual caller embeds in the infinite comparison

Fix ANY b>h and an admitted finite-window input v. Extend it by zero to all later times. This extended input is progressive globally E2 with the same literal denominator. The infinite actual output agrees with the finite output through b by the preceding uniqueness argument, and its full path norm is at least the finite prefix norm. Therefore

`G_infinity >= E||z_v||_[0,b]/E||v||_[0,b-h]`.

Take the full finite input supremum and then b to get `G_infinity>=sup_b G_b`, including infinity. In particular if the right side is infinity, equality follows immediately and no infinity-times-zero argument is used.

## 4. The converse caller needs a padded horizon

Assume `g_*=sup_(b>h)G_b<infinity`, and fix ANY globally progressive E2 input w with positive literal norm. For each t>0 form the actual deterministic-time cutoff `w^t=w 1_[0,t]`, zero afterward. It is an admitted finite-window input for the finite problem with horizon **b=t+h**, because that problem's input interval is [0,t].

Its actual output through time t agrees with the infinite response to w, including any controller term using w(s) in the final preview window. The finite gain bound thus gives

`E||z(w)||_[0,t] = E||z(w^t)||_[0,t]`

`<= E||z(w^t)||_[0,t+h] <= G_(t+h) E||w||_[0,t] <= g_* E||w||_[0,t]`.

If the cutoff input is zero in expected norm, linearity/zero initial state gives zero output for that cutoff, so the inequality is also valid without dividing by zero.

As t increases, both path norms increase to their full-horizon norms. Monotone convergence applies to the NORMS themselves, not an RMS substitute, and gives

`E||z(w)||_[0,infinity) <= g_* E||w||_[0,infinity)`.

The input was arbitrary, so G_infinity<=g_*. This proves (H), with all matrix/h/kernel/zero-output cases included. No limit of controllers or horizon-dependent policy has been taken.

## 5. What the identity does and does not say about synthesis

For a fixed eligible law and prescribed gamma>0, infinite-horizon uniform-strict feasibility is equivalent to existence of ONE common finite-horizon margin:

`there exists kappa<gamma such that G_b<=kappa for EVERY b>h`.

It is NOT equivalent merely to `G_b<gamma for each b`, where margins can approach zero. Nor does `for every b there exists F_b` imply existence of one infinite-horizon law. Any controller quantifier must retain the SAME F and its separately verified infinite-horizon admissibility.

The completed tap family supplies an exact actual illustration: with h>0 and nonzero scalar taps, `G_b=||B_(ceil((b-h)/h))||<M=|j0|+|jh|` for every finite b, while `G_infinity=M`. Thus all finite problems meet a uniform-strict threshold gamma=M individually using the SAME law, but no common strict margin exists and infinite UNIFORM strictness fails. This is an author-only current-family import, not independent verification or a claim of another controller's impossibility. Its infinite POINTWISE strictness is separately proved; the two statements are not conflated.

In general, infinite pointwise strictness implies finite pointwise strictness by zero extension, while the reverse argument above only passes nonstrict limits. No general reverse pointwise assertion or physical counterexample to every such reverse assertion is supplied here. The exact padded gain identity does not resolve an endpoint attainment issue by itself.

## 6. Degeneracies, source boundary and imports

The proof covers h=0 (padding then adds zero), h>0, zero output/forcing matrices, all ranks/signs and extended infinite gains. Finite b>h preserves a nontrivial input domain; no value is defined for empty denominator intervals. Deterministic inputs can be treated analogously, but no equality of deterministic and progressive gains is inferred; the supported physical gap already rules out that blanket step.

Only the adopted local-control interpretation of the infinite comparison is asserted. Extra global-control-energy/stability requirements, arbitrary nonlinear full-information laws, nonzero initial homogeneous responses and the book's unformalized process-space choices remain separate. No scientific source/result/body outside the allowed inputs, stopped construction, old probability-buffer/realization guide or source-page method discussion is consumed.

The proof is written and all-variable, using actual strong linear-SDE uniqueness/linearity, the explicitly causal window formula, zero extension, prefix norm monotonicity and ordinary monotone convergence. It is independent of the pending NR-GAIN global-bound review. No scientific interpreter/calculator/CAS/program/enumeration/solver, selected state/control probe, model CLI or nested agent occurred. All old process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP and source/copyright qualifications persist; no peer/parent, formal/kernel, human/configured-family, executable or novelty acceptance is claimed.
