DISPOSITION: ACCEPT-WITH-FIXES

There are no FATAL or MAJOR findings. I re-derived every universal argument in Sec. 0–6 by hand, line by line. All findings are MINOR: they concern statement precision and bookkeeping. I assert no counterexample and replayed nothing. All controls below are hand arithmetic, not executions.

## Findings

**MINOR-1. The residual and its Corollary are worded imprecisely** (`proof-Rstar-partial-v2.md:163-165`).
- "The open part is exactly R***" is only true as "the residual of these arguments".
- The Corollary's hypothesis ("no *avoider* configuration lies in R***") is, given Sec. 1–6, equivalent to MIX_low(p) itself. In that form no census can discharge it.
- Replace with:
  > The normalized interval-feasible data not handled by Theorem MIX-R and Sec. 2–6 are exactly those in R***. Hence every MIX_low avoider, if one exists, has lift data in R***.
  >
  > R*** is cut out by necessary conditions only: interval windows, (R1), (R2) and the Sec. 6 inequalities. Membership in R*** does not imply:
  > - realisability by an RGR word,
  > - survival of the non-interval windows u_P ∉ I(P), or
  > - an ordered-product counterexample.
  >
  > **Corollary.** If no interval-feasible normalized MIX_low data at p lie in R***, then MIX_low(p).

**MINOR-2. Same logical slip at L128.** "MIX_low(p) holds for every avoider configuration outside R**" should read "no normalized MIX_low avoider has lift data outside R**".

**MINOR-3. L52 overstates the anti mass.** "total mass B" should read "total anti mass B − n_P ≤ B".

**MINOR-4. L109 has an unjustified step.** After "otherwise B_Y ≥ 1", add: "(T is then a pair or an anti run; bh_T ≥ 2 puts it in Y, where it contributes ≥ 1 to B_Y)."

**MINOR-5. Import status is inconsistent, and a path is missing.**
- L13 calls Lemma H "reviewed".
- `proof-PAR-K0.md:4` still says "[W], not yet hostile-reviewed"; only its L24–31 correction cites a review.
- One of these status lines needs fixing. Per the brief, I treated Lemma H as reviewed.
- Also give a relative path for `proof-RUNS.md`.

**MINOR-6. Bookkeeping for the finite-evidence section** (L172–191).
- **(a)** L181 together with the Corollary would yield a computer-assisted MIX_low(p) for 7 ≤ p ≤ 17. Say explicitly at L181 that this is not claimed.
- **(b)** The p = 17 DFS prunes on "a partial lower bound for phi(Z0)+m". But m is a *cyclic* block count. A linear prefix overcounts by 1 when runs 1 and k both end in Z0. The code must allow for this, or the "complete" claim is unsupported. This cannot be checked from the packet.
- **(c)** "B2 restriction" (L190) is undefined in this file.

**Observation (not a defect).** The written proofs plus imports already give MIX_low(5):
- At p = 5, 2g + B ≤ 4 forces g = 1.
- B = 2 is handled by Lemma W.
- For B = 1, the cases are:
  - outside R*: Theorem MIX-R;
  - some bh ≥ 2: Theorem A;
  - otherwise, by Fact F(a),(d), all d ≤ 1 = 2g + B − 2, and Lemma G1 contradicts (R1).
- So L7's "nothing proves MIX_low(p)" is an allowed under-claim at p = 5. It can be added as a remark.

## Verification record (focus items)

**Lemma S in phi-form, Fact F (L25–39).**
- With m = 1, β = 0 and κ = g + B, r2:44 gives x(Q) ≥ G_1(D_Q) + 1. The identity at L27 holds.
- F(a) is r2:90–92 and uses only 2g + B ≤ k − 1.
- F(b)–(d) are correct.
- The chain cheap ⇒ d ≤ 2g + B ⇒ φ ≤ g − 1 is correct, and fillers are aligned.

**Lemma KL (L45–54).**
- Non-monotone c is harmless. The first prefix reaching g + 1 has a predecessor with c ≤ g, and each step adds φ_t + Δm ≤ g. Here Δm ∈ {−1, 0, 1} because P ∪ {t} ⊆ S ≠ [k].
- The bh ≤ 0-first ordering gives BH(P) ≤ B in both cases.
- D_P ≥ −B holds, and m ≥ 1 (needed for Cor. (vi)).
- Φ(P) = 2c(P) lies in [2g + 2, 4g], inside the Corollary's range.
- Every application in v2 uses an independent S with φ ≥ 0, so each step is w_t ∈ [1, g] anyway.

**Lemma W (L58–72).**
- Step 1: the runs split into {cheap} ⊔ {φ ≥ 0, bh ≥ 2} ⊔ {φ ≤ −1}.
  - The middle class is aligned with w ≤ d/2.
  - The aligned mass is A − n_P ≤ 2p − 1.
  - Hence W(cheap) ≥ 2g + 1, using neither B ≥ g + 1 nor R*.
- Step 2, some run non-cheap: the cheap runs form arcs. Taking the heavier parity class of each arc gives an independent union with weight ≥ W(cheap)/2 > g.
- Step 2, all runs cheap: the deletion of t0 is justified.
  - Its weight is w_{t0} = φ_{t0} + 1 ≤ g, so the path [k]∖{t0} has weight ≥ p + g.
  - The heavier class has weight ≥ (p + g)/2 ≥ g + 1, since p ≥ k ≥ 2g + B + 1.
  - The path ends are at cyclic distance 2, as k ≥ 4.
  - Control: this branch needs p + 2g ≤ gk ≤ gp, so it occurs only for g ≥ 2.
- Step 3: all weights are ≥ 1, so |S| ≤ g + 1 ≤ B. This is the only use of B ≥ g + 1.

**Lemma B1 (L76–87).**
- a' ∈ [1, B − 1], which forces B ≥ 2.
- gam(d_T) = d_T − p, φ(R') ≥ a' − B, and W(R') ≥ 2g + a' + s.
- The pigeonhole between the two parity classes stays valid with negative weights.
- Dropping runs with φ ≤ −1 only raises W.
- BH(S) ≤ Σ_S d ≤ a' because φ ≥ 0 on S.

**Theorem A (L97–114).**
- Classes (i)–(iv) are exhaustive:
  - aligned runs are cheap ⇔ bh ≤ 1;
  - pairs are cheap ⇔ bh ≤ 0;
  - antis are cheap ⇔ bh ≤ −c;
  - (iv) forces c ≥ 2.
- Re-derived: Σ#(i–iv) ≤ 2B_Z + B_Y − S_Z − 2m − bh_T + 1. The #anti_{Z0} term inside L_Z and #(iv) are jointly paid by the anti mass of Z0.
- Hence #cheap ≥ 2g + s + 2m + S_Z + (bh_T − 1 − B) + (B − B_Z) ≥ 2g + 2, using m ≥ 1 (Z0 is nonempty and proper).
- Signs check out:
  - pairs in Y have bh ≥ 2 and are charged to exc;
  - antis in Y are charged to B_Y;
  - T is excluded from (i)–(iv).
- BH(cheap) ≤ 2B + 1 holds in both cases: T aligned gives |Y_al∖{T}| ≤ 2B + 1, and T a pair or anti gives B_Y ≥ 1.
- Balancing by cardinality is enough. Since w ≥ 1 on cheap runs, both U and V get c ≥ g + 1, and only BH(U) + BH(V) ≤ 2B + 1 is used.

**Lemma G1 (L118–124).** Correct; the final contradiction is 2 + 2m ≤ 0. It uses (R1) and 2p − k ≥ k.

**Assembly (L128–131).** Correct. The range in F(d) together with d ≥ 2p − B covers [2g + B − 1, ∞).

**Lemma KS (L132–151).**
- L142–145 re-derived exactly, using φ(Z0) ≤ φ(Z0+) − β, B_Y ≥ n_apY and exc_ap ≥ 0.
- The tight case is correct: B_Y = S_Z = 0 and L_Z = 2B_Z force no pairs, with every anti in Z0 having c = 1 and bh ≤ −1, hence cheap.
- Uses (R2) only.

**Lemma AC (L153–161).** Correct, including the boundary B = 1, s = 0, where k = 2g + 2 is even and the cycle's two parity classes have BH sum 2. Uses (R2) only.

**Residual (L163–171).** The complement is computed correctly. The consequence at L171 re-derives from (R1): 2φ(Z0+) ≤ 2g − 2m + 2Σ_(iv)|φ|.

**Hypothesis matching.**
- Lemma H is used only in the direction "u_P ∈ I(P) for some proper P ⇒ identity subword", with β = 0.
- r2's V_0 and V_k use the corrected form: A ≤ 2p − 1 and B < κ.
- The K-Corollary needs 2g + B ≤ p − 1 and D ≥ p + 2g; both follow from k ≤ p and A ≤ 2p − 1.

## Hypothesis essential to any k > p transfer

The essential hypothesis is the low-run condition **k ≤ p**, equivalently D = 2p − k + 2g ≥ p + 2g. Together with A ≤ 2p − 1 it gives 2g + B ≤ p − 1. It is consumed in three places:

- **r2 Sec. 1, existence and uniqueness of the interval-chain lift** (r2:33–36, 56–57, 61–62). Without it, x, φ, bh and w are not well defined.
- **r2's Corollary of Lemma K** (r2:77–82): items (i) and (iv) need 4g + 2B + 1 ≤ 2p, and (v)/(vi) are proved via D ≥ p + 2g. This is the kill step of every KL application.
- **Local uses in v2**: F(c) at L34, B1 at L79, W Step 2 at L69, G1 at L123.

Several pieces survive k > p if lifts exist: F(a), the identity Σw = p + 2g, and Step 1 of Lemma W. Lemma M0's hypotheses are not in the packet, so its status for k > p is unverified here.

## Hand controls

- L27 identity: (D, B) = (10, 3) gives 3 = 3, and (9, 3) gives 2 = 2.
- K-Corollary (i) at the extreme 2g + B = p − 1, Φ = 4g, BH = B gives Φ + 2BH = 2p − 2 ≤ 2p.
- Theorem A's bound at g = B = B_Z = 2, s = 0, m = 1, bh_T = 3 gives exactly 6 = 2g + 2. It has no slack there, so no rounding hides an error.
