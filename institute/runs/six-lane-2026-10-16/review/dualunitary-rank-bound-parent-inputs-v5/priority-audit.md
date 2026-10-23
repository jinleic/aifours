# Sharp two-qutrit dual-unitary bound: bounded priority audit

Recorded 2026-10-17 PT. Read-only scout `QutritSharpPriority` (completed after 26 min), plus a parent reading of the locally pinned thesis chapter. **Verdict: no prior proof found in a bounded search.** A search miss is not novelty, and this audit does not vouch for the proof.

## Claim audited

(a) Every two-qutrit dual unitary that is not 2-unitary has e_p ≤ 15/16; the same entangling-power bound holds for T-dual gates through U ↦ US. The stronger sufficient structural claim is (b): for dual U, rank U^Γ ≤ 6 unless U^Γ is unitary; for T-dual V, the corresponding bound is rank V^R ≤ 6 unless V^R is unitary. Claim (b) implies (a), but the reverse implication is not asserted.

## Where the question is stated as open

| Source | Statement (verbatim) | Checked by |
|---|---|---|
| S. A. Rather, PhD thesis, IIT Madras 2023 (hdl 10603/547745), ch. 3, §3.3.1.2, printed p. 85 (chapter PDF page 17); lane copy `physics/evidence/six-lane-20261016/dualunitary-ep15-16/sources/rather-thesis-2023/07_chapter3.pdf`, SHA-256 `98598d45…22e7` | "Conjecture 3.3.2. There are no two-qutrit d² = 9 dual-unitary or, equivalently, T-dual gates with entangling power in the range 15/16 < e_p(U) < 1." Followed by: "A possible reason for the discontinuity in the entangling power may be due to the non-existence of two-qutrit dual-unitary gates whose partial transpose has rank 7 and 8" | Parent, from the lane's local layout text (lines 738–751). The scout could not reach the repository copy (anti-bot page). Page number corrected from 84 to 85 using the chapter's page-by-page extraction; p. 84 contains eq. (3.36). |
| Rajchel-Mieldzioć et al., arXiv:2508.04777v3 (25 Jun 2026), Rep. Prog. Phys. 89 057601, p. 9 | "The dual unitary U_s(2π/3) is an orthogonal matrix with entangling power 15/16 = 0.9375 which is likely to be the highest possible value for dual unitaries that are not 2-unitary"; the gap's "rigorous existence of which is yet to be established" | Scout, arXiv PDF text; same passage in v1 (6 Aug 2025) and v2 (30 Dec 2025) |
| Aravinda–Rather–Lakshminarayan, arXiv:2101.04580v2 (PRR 3 043034, 2021), p. 20 | for q = 3, "e_p(U) = 1 appears to be isolated… a gap whose left extreme… is otherwise not yet known" | Scout |
| Jonnadula et al., arXiv:1909.08139 (PRR 2 043126, 2020), p. 9 | "numerics suggest that the set of dual unitary matrices of size N² = 9 is not connected" | Scout |

## Matched prior results (none implies the claim)

- Rather–Ramadas–Kodiyalam–Lakshminarayan, arXiv:2212.06737v2 (PRA 108 032412, 2023), Thm 1: one LU class of order-9 2-unitaries. Its product-to-product normal form is the first step of the candidate proof; their argument assumes T-duality, the candidate's does not.
- Thesis ch. 3 (lane copy): bound 15/16 on the restricted class of T-dual gates with U^{Γ1} = U (maximal Schmidt rank 6); explicit family U(θ) attaining 15/16 at θ = 2π/3.
- Tyson (2003) Thm 10; Müller-Hermes–Nechita (1612.07616) Thm 1.3: plain unitaries on C³⊗C³ realise every Schmidt number 1–9, so (b) is specific to dual gates.
- Deschamps–Nechita–Pellegrini (1509.06543): characterisation via unital channels; qubit analogue only.
- Pahari, arXiv:2607.00210 (30 Jun 2026): Clifford dual gates over F_q, a finite subclass.
- Krishnan–Sunder / Clarisse et al.: permutation gates at d = 3 (72 maximal; next value 8/9).
- King–Ruskai (quant-ph/9911079) and Ruskai–Szarek–Werner (quant-ph/0101003): the unital qubit-channel normal form behind Fact K.

## Proof map against the literature

Normal form: prior (Chen et al. 2008; Rather et al. 2023). Fact K: classical. Theorem A (Cauchy–Schwarz on the spectrum of U^Γ U^Γ†): elementary. Lemmas N1, T, S, Propositions G, A*, B* and the assembly: no source found.

## Access holes

The thesis repository copy (anti-bot page) was unreachable for the scout; the parent read the lane's earlier-fetched local chapter copy instead. Journal bodies (PRL, Rep. Prog. Phys.) were not compared beyond arXiv. Rather's announced follow-up paper is not available.
