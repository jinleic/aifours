# Depolarizing asymptotic claim: scoped primary-source audit

Read-only scout CapacityClaimAudit. Preserved verbatim; proposed wording is advice, not automatically adopted.

**Summary**

1. **What arXiv:2609.39747v2 proves.** Theorem 6 says that, for a fixed excitation cutoff K, the coherent information of the M-qubit depolarizing channel converges to that of a single-mode Gaussian channel G_η. The error bound Δ_{M,K} is written out in full and goes to 0 as M grows. In the parts I read I found no error, so this is a sound-looking existence argument.
2. **What it does not prove.** The headline p_th ≥ 0.2029161 also needs Ic(ρ, G_η) > 0. The paper's only support is one number, Ic ≈ 10⁻¹², for a state whose amplitudes are not published. It gives no precision, error bound, interval certificate, code or data.
3. **Finite witness.** The paper gives no finite witness: no M and no state. Its own Δ bound would need M on the order of 10⁶⁶ to beat a 10⁻¹² margin [INFERENCE, my arithmetic].
4. **What our p = 1/5 result is.**
   - It is an explicit finite realization of a consequence of Ahmed's claim.
   - It is a rigor upgrade only for (0.194868, 1/5].
   - It is not a new threshold.
   - It does not use Theorem 6 or Ahmed's numbers.
   - It does depend on Ahmed's construction: the same mod-3 comb, the re-derived Theorem II.3/II.9 decomposition, and a witness found by Gaussian-limit optimization.
5. **The verdict wording needs fixing.** The phrase "not a breakthrough unless the asymptotic claim proves non-rigorous" is badly calibrated. The 10⁻¹² premise is already uncertified as published, and that still does not lift p = 1/5.
6. **Versions and artifacts, checked live.** v2 is still the newest version, and v1 has the same numbers. arXiv lists no ancillary files, and a targeted search found no erratum. The cited Agarwal repo's last commit (2026-07-03) predates the paper.

**Files** (paths relative to `/Users/jinleic/repos/aifours`; `S/` = `physics/evidence/six-lane-20261016/depolarizing/sources`, lane root = `physics/evidence/six-lane-20261016/depolarizing`)
- `S/2609.39747.txt`:
  - :285-293 Theorem 6
  - :340-384 numerics, conclusion and AI statement
  - :977-1186 Lemmas III.1–III.2
  - :1186-1770 Theorem IV.2, Lemmas IV.3–IV.4, the uniform bound ε_{M,K} (IV.32)
  - :1771-1997 Lemma IV.5, Theorem IV.6, Δ (IV.48)
- `S/2609.39747.pdf`: cross-check of the main-result paragraph; matches the txt.
- `S/2607.27449.txt:72-96, 291-294`: Mele et al. antidegradability formula and their certification standard.
- `S/2605.09138.txt:528-529`: Agarwal et al. accuracy statement.
- `S/2608.15870.txt:26-31`: KG's certified point.
- `S/2610.02176.txt:97-100`: Khanian–Leung–Smith (KLS) per-use limit.
- Lane `README.md:18,34-36,46-48`; `evidence/LOG.md:13-19,28-31,105-112`; `evidence/gauss/g3_eta0.73{2,3}.log`; `review/PROOFS_v5.md:19-30`.
- `institute/runs/six-lane-2026-10-16/review/depolarizing-parent-verdict.md:29,31`; `contract.json:8-11`.

**Architecture:** Our `cert.py` evaluates finite-M sectors using Ahmed's Theorem II.3/II.9 decomposition, re-derived in `PROOFS_v5 §1`. The witness was found by Ahmed's method: optimize for G_η, then move to Sym^M (`LOG.md:28-31`). The certificate itself never uses Theorems 5–6.

---

### 1. Conventions: total-error p vs replacement probability
All three papers write p for the total error. Ahmed's channel is D_η = ηρ + (1−η)·I/2, so 1−η = 4p/3 is the probability the state is replaced by I/2, and each Pauli has probability p/3. KG writes p_KG = p/3.

| Point | Total p | η = 1−4p/3 | Replacement prob. 1−η | Per-Pauli p/3 |
|---|---|---|---|---|
| KG certified | 0.194868 | 0.740176 | 0.259824 | 0.064956 |
| **Ours** | **1/5** | **11/15** | 4/15 | 1/15 |
| Our negative control | 201/1000 | 0.732 | 0.268 | 0.067 |
| Ahmed claim | 0.2029161 | 0.7294452 | 0.2705548 | 0.0676387 |
| Lane headroom assay | 0.20295 | 0.7294 | 0.2706 | 0.06765 |

The emergent channel G_η is a thermal attenuator with transmissivity η and N_E = 1/(2η). Using Mele's formula η_AD(ν) = (ν+½)/(ν+1), G_η is antidegradable only when η ≤ 1/√2, i.e. p ≥ 0.21967. So Ahmed's point is not ruled out by antidegradability [INFERENCE, my arithmetic].

### 2. Theorem delta table

| | Exact statement | Quantifiers | Finite witness | Status |
|---|---|---|---|---|
| KG 2608.15870v2 | Ic(A, D^⊗45) > 0 at p = 0.194868 | Explicit 45-qubit state | Yes; artifact on Zenodo returned HTTP 403 to us | Exact-rational certificate; not peer reviewed |
| Ahmed, Theorem 6 (analytic) | \|Ic(ρ, D_η^⊗M) − Ic(ρ, G_η)\| ≤ Δ_{M,K} → 0 | For fixed η and K, uniform over all ρ with excitations ≤ K. Δ is explicit (IV.48), valid once M passes explicit side conditions (supp. lines 1723-1727, 1883-1884, 1898) | Not applicable | Written proof; no flaw found in read scope; not peer reviewed |
| Ahmed, threshold claim | p_th ≥ 0.2029161 | "For all sufficiently large M"; no M given | None: amplitudes unpublished (only q, n ≤ 220, mean ≈ 56.47) | Depends on Theorem 6 plus an uncertified 10⁻¹² value |
| **Ours** | Ic(ρ⋆, N_{1/5}^⊗2000) ∈ [1.13738e-8, 1.14328e-8] bits | Explicit, hash-bound M = 2000 state | Yes | Computer-assisted (double-double + Arb), single implementation |

Status by range of p:

| Range | Before our certificate | After |
|---|---|---|
| ≤ 0.194868 | Certified (KG) | Certified |
| (0.194868, 1/5] | Claimed only: Theorem 6 + uncertified premise + monotonicity | **Certified (ours)** |
| (1/5, 0.2029161] | Claimed only | Claimed only |

### 3. What 2609.39747v2 establishes at p = 0.2029161
- **(a) Analytic part.** Theorem 6 and IV.6 hold uniformly over all states supported within K excitations. Every part of Δ is explicit: ε_{M,K} (IV.32), ε^att = 4√K·(2 log M/M)^{1/4} (IV.43), and the atypical-sector term 4(1+η)log(K+1)/(ηM). The logic is valid as an existence-by-convergence argument.
- **(b) Numerical part.** The paper reports Ic ≈ 10⁻¹² for the output truncated at D = 320 (a lower bound by data processing).
  - The amplitudes are optimized but not printed.
  - Precision, error and units are not stated; the supplement uses base-2 logs (:583-584).
  - The lane's own float exploration, which I have not checked, reports |Ic| ~ 1e-11 of both signs for combs with mean photon number about 56, at every η tried (`LOG.md:17-19`). Ahmed's state sits in that same regime (mean 56.47), so the sign at 10⁻¹² is not robust without error control [INFERENCE].
- **(c) Certificate.** None is given. The truncation method Ahmed cites [17] (Mele et al.) does include interval certification, and Mele et al. call their own 2.4e-9 float point uncertified. Agarwal et al., who share four authors with Ahmed, reported thresholds at Ic = 10⁻⁷ with "at least 10 decimal places" accuracy. Ahmed's 10⁻¹² is below that and comes with no accuracy statement.
- **(d) Finite witness.** None is published. Our p = 0.2 result is both:
  - an explicit finite realization within Ahmed's ansatz and construction route;
  - a rigor upgrade, but only on (0.194868, 1/5], not for Ahmed's headline value.

  It also shows that M = 2000 is enough at p = 1/5, compared with the ~10⁶⁶ implied by Ahmed's bound [INFERENCE]. That is modest added information, not a theorem about convergence rates.
- **KLS 2610.02176 does not conflict.** It limits the per-use rate of fully permutation-invariant inputs to the single-use value. LSD here uses inputs that are i.i.d. across blocks, and a fixed Ic > 0 per block means a per-use rate of order 1/M → 0, which is consistent [INFERENCE].

### 4. Quotes (≤40 words each)

| # | Quote | Local file:lines | Public source |
|---|---|---|---|
| Q1 | "Theorem 6. For every ρ ∈ L(SymM(C2)) supported within a fixed Dicke excitation cutoff (equivalently Fock cutoff) given by K, \|Ic(ρ,Dη⊗M) − Ic(ρ, A(1+η)/2η∘L2η²/(1+η))\| ≤ ∆M,K, where ∆M,K → 0 as M → ∞." (formula rendered) | `S/2609.39747.txt:285-293` | https://arxiv.org/abs/2609.39747v2 |
| Q2 | "Note that both εM,K and εatt M,K go to 0 as M → ∞, and hence we also have limM→∞ ∆M,K = 0." | :1996-1997 | same |
| Q3 | "we truncate the output of the Gaussian channel to a finite cutoff D and collapse all higher excitation levels to \|⊥⟩ … by data processing, we can lower-bound the coherent information of the full Gaussian output" | :340-346 | same |
| Q4 | "Both codewords have real amplitudes and are supported on n ≤ 220 with q ≈ 0.4506152. … The amplitudes of both codewords have a nearly Gaussian envelope, with mean photon number close to 56.47." | :359-366 | same |
| Q5 | "At η = 0.7294452 we obtain Ic(ρ, Gη) ≈ 10−12. Since Ic(ρ, Gη) > 0, Theorem 6 gives Ic(ρ, Dη⊗M) ≥ Ic(ρ, Gη) − ∆M,K > 0 for all sufficiently large M." | :367-370 | same; identical in https://arxiv.org/html/2609.39747v1 |
| Q6 | "We therefore conclude from our work that pth ≥ 0.2029161." versus the introduction's "producing a new improved lower bound pth ≳ 0.2029" | :375-376; :76 | same |
| Q7 | "The numerics for this work were conceived by the authors, implemented by AI and verified by the authors." | :382-384 | same |
| Q8 | "Fix η = 0.7294452, which corresponds to p = 0.2029161." … "η = (1 − 4p/3), the probability with which the input state is left unchanged and otherwise replaced by a maximally mixed state" | :348-349; :57-62 | same |
| Q9 | "Very small numerical improvements have been found by LLMs subsequently [14, 15]." ([15] is KG, which is certified) | :48-50 | same |
| Q10 | "Our certificates imply 0.75 ≤ ηc ≤ 0.7841 rigorously. A numerical search gives a stable positive value 2.4 × 10−9 at η = 0.7818, suggesting ηc ≲ 0.7818, but that point has not yet been rigorously certified." | `S/2607.27449.txt:291-294` | https://arxiv.org/abs/2607.27449 |
| Q11 | "the thermal attenuator is antidegradable, and hence has zero quantum capacity, for η ≤ ηAD(ν) [57], where ηAD(ν) := (ν + 1/2)/(ν + 1)" | :78-83 | same |
| Q12 | "Our coherent information computation is accurate upto at least 10 decimal places for the values of n that we have computed, and the reported lower bounds on thresholds correspond to a coherent information of 10−7." | `S/2605.09138.txt:528-529` | https://arxiv.org/abs/2605.09138 |
| Q13 | "with certified Ic > 0 at the exact rational p = 16239/250000 = 0.064956 (per-Pauli convention; total error rate 3p = 0.194868)" | `S/2608.15870.txt:28-31` | https://arxiv.org/abs/2608.15870v2 |
| Q14 | "Thus the asymptotic coherent-information optimization under full permutation invariance requires only a single channel use. Finite-block superadditivity remains possible, but its excess per use vanishes at a controlled rate." | `S/2610.02176.txt:97-100` | https://arxiv.org/abs/2610.02176 |

### 5. Rigorous vs uncertified
- **Sound-looking (no error found in what I read):**
  - the reduction "a finitely supported ρ with Ic(ρ, G_η) > 0 implies Q(D_η) > 0";
  - the exact decomposition, which the parent re-derived independently.
- **Uncertified:**
  - the sign of Ic(ρ, G_{0.7294452});
  - therefore the specific value 0.2029161.
- **Certified (computer-assisted, single implementation):** our M = 2000 block at p = 1/5.
- **Not a weak link:** Theorem 6 does not depend on the 10⁻¹² number for points just above 1/5. The lane's own uncertified float Gaussian-limit values are 8.89e-9 at p = 0.20025 and 1.68e-9 at p = 0.201 (`gauss/g3_eta0.733.log`, `g3_eta0.732.log`). Combined with Theorem 6, they already point above 1/5 [INFERENCE].

### 6. Auditing "not a breakthrough unless the asymptotic claim is non-rigorous"
The condition mixes up two different things: the analytic theorem and the numerical premise.
- If only the numerical premise fails (which is already its status as published), the threshold claim drops only slightly. The Theorem 6 route with larger margins still points above 1/5.
- Only a refutation of Theorem 6 itself would make 1/5 the best credible value. Even then the gain is +0.005132 over the best certified point, and meeting the contract's "consequential delta" would need its own argument.

**Recommended wording:**
> "Among audited primary sources, ρ⋆ is the first explicit finite witness with a certified sign at p ≥ 0.2 (total-error p; η = 11/15). It raises the best certified explicit point from 0.194868 (arXiv:2608.15870v2) to 1/5. It lies 0.0029161 below the claimed p_th ≥ 0.2029161 (arXiv:2609.39747v2). That claim combines an analytic convergence theorem (Theorem 6, explicit Δ_{M,K} → 0, no finite M; no error found in this audit) with an uncertified premise: Ic(ρ, G_η) ≈ 1e-12 for an unpublished state, with no stated precision, error bound or artifact. If the premise holds, it already implies Q > 0 at 1/5. Our certificate is independent of Theorem 6 and of those numerics, but uses that paper's mod-3 comb, its Theorem II.3/II.9 decomposition (re-derived) and its Gaussian-limit optimization route. It is a rigor upgrade on (0.194868, 1/5] and an explicit finite realization, not a new threshold. Not a breakthrough; modest specialist significance."

**FRONTIER line:** drop the "unless …" clause.

### 7. Real flaws found
1. **Ahmed et al.:** no mathematical flaw in what I read. The only issues are presentational: "≳ 0.2029" in the introduction vs "≥ 0.2029161" in the conclusion; "Ic(ρ, G_η)" written for what is the truncated lower bound; and KG's certified result described as "numerical improvements".
2. **Lane README:18** calls Ahmed's numerics "float64". The paper never states a precision; the label should say "precision, error bound and state not reported".
3. **Parent verdict:29 and :31** contain the conflation described in section 6.
4. **Lane README:46-48** lists "reproduce the Ahmed threshold ≈ 0.2029" as a required positive control. No completion is recorded, only the trend note in `LOG.md:17-19`, and it is missing from the deviations list. This does not affect the p = 1/5 certificate.

### 8. Unresolved checks
- Ahmed's 10⁻¹² premise cannot be checked: the state is not public and contacting the authors is out of scope.
- Not verified here:
  - Stam (1978) eqs. (2.6) and (4.1) as used in (IV.14) and (IV.21);
  - the cloner Kraus coefficients (IV.6)/(IV.18);
  - Ahmed's section II beyond the parent's re-derivation;
  - Winter's continuity bound with an infinite-dimensional output system.
- Priority against both papers rests on this read-only audit alone. The hostile review explicitly left it out (`depolarizing-v3-hostile-review.note.md:103`).
- The arXiv export API returned HTTP 429; the abstract pages loaded fine. I had no shell, so the host times of the live fetches were not recorded.

### 9. Primary read scope
- 2609.39747 txt lines 1–605 and 977–2000, plus a PDF cross-check. Section II proofs (605–976) were only skimmed.
- Live pages: the arXiv abstract pages for 2609.39747 and 2608.15870, the v1 HTML of 2609.39747, the Agarwal repo commits via the GitHub API, and one web search.
- The targeted line ranges from 2607.27449, 2605.09138, 2608.15870 and 2610.02176 listed above.
- Lane README, LOG, gauss logs, PROOFS_v5 §1, the parent verdict and the contract gate.

No arithmetic was rerun, no models or solvers were run, and no files were edited.
