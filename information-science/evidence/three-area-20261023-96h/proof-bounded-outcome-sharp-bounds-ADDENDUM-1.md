# Operative addendum 1: binary-domain bridge and exact reduction

This is the required operative companion to immutable `proof-bounded-outcome-sharp-bounds-v1.md`, SHA-256 `618ee5c5fc3ebc503f4dc730d70572dbc807036fd49efc87ef65d2e798643a82`. It applies MINOR M1 from the independent in-harness review `mathematics/evidence/three-area-20261023-96h/peer-review-info-bounded-outcome-v1.md` (0F/0M/1MINOR). That original review verdict is not rewritten. No new independent check is implied by creating this addendum.

## 1. Explicit binary potential-outcome bridge

Withdraw any literal equality of the underlying full-data feasible-law sets in v1 Section 6.2. Binary factual data alone do not force the missing potential outcome to be binary. What is equal is the projected attainable (gamma,delta) set.

For a bounded-real law with binary factual y=Y_B, retain B,y,S_1,Z from the proof. Adjoin an independent uniform V and set Z'=1{V<=Z}. Then

    E[Z' | B,y,S_1,Z]=Z.

Define Y'_0=y,Y'_1=Z' on B=0; define Y'_1=y,Y'_0=1-Z' on B=1. Both potential outcomes are binary. The complete factual measures mu_0,mu_1 and q are unchanged. Since

    gamma=g_min+E[Z],
    delta=t-A_0-A_1+E[(1_C-1_D)Z],

conditional expectation preserves gamma and delta exactly after replacing Z by Z'. Treatment can remain independent of the enlarged latent tuple. Conversely every all-binary potential-outcome law is allowed by the bounded-real model. Thus the full attainable projections agree, despite the different feasible-law sets. The complete step-by-step construction is preserved in `addendum-binary-potential-outcome-bridge-v1.md`.

## 2. Standalone recovery of every published binary term

Read `proof-binary-reduction-v1.md` with this bridge. It directly rewrites the binary restriction of F_eta as four hinges minus 2r, locates the interval between the middle two hinge breakpoints, proves that lower-domain clipping cannot occur, and evaluates the only two possible upper-domain clipping cases. This yields all **seven** lower terms. Invertible outcome complementation gives all **seven** upper terms, in the same order as the retained primary Yin et al. Theorem 1.

The algebraic reduction does not depend on importing the source's sharpness proof. The bridge above makes the latent-domain comparison exact. All-binary sharp bounds remain prior work; the proposed theorem delta is the arbitrary bounded-real factual distribution and its quantile criterion.

## 3. Unchanged conclusions and limits

Theorems 1/2, their arbitrary-law/atomic simultaneous attainment and the uniform-law example are unchanged. Status remains **CANDIDATE / NOVELTY_UNCLEAR** pending the parent's complete reconstruction and addendum check. No scientific execution, model CLI, finite certificate or kernel verification has occurred. Kuroki 2013's full theorem/interface remains a separate prior-art access gate.
