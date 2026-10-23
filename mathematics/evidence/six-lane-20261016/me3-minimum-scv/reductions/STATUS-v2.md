# reductions/ — STATUS v2

Written 2026-10-18 06:12 PDT (host clock) by `MathPhaseType3.ME3Reductions` for `MathPhaseType3`. This file supersedes
`STATUS.md`, which is kept (sha256 61776330…2c76). **Correctness only; no novelty, priority or "first" claim.** The D2
bound I_2 ≥ v_cos is not addressed here.

The v2 changes answer review `institute/runs/six-lane-2026-10-16/review/me3-reductions-codex-v1.note.md` (sha256
a6d34ecb9b0ea1c29646f6bb7d02a4ad73888af9bb7d7a826a4c778da94b1328; ACCEPT-WITH-FIXES, no fatal defect).

## 1. Claims after v2 (`proof/reductions-v2.md`)

| Item | Status |
|---|---|
| L1 (structure, dominant real exponent, converse realization) | Proved in text. |
| L2 (cone, ratio form, mixtures, extreme rays, inclusion bookkeeping) | Proved in text. **Fix (1):** §0.2 and Lemma 2.3 now require positive mass 0 < ∫f, and Remark 2.3a shows that every e.p. application satisfies it. |
| L3 (real exponents: SCV ≥ Δ3) | Proved in text. |
| L4 (Δ3 = s(x1) ∈ (1/4, 1/3), h(Δ3) = 0) | Proved in text, EXACT. v2 adds exact root isolation in (0, 1/2), (2, 3), (6, 7), plus s(x1) < 1/3 < 1/2 < s(x3). |
| Lemma 4.2: Δ3 > 553/2000 | EXACT, by h′ ≥ 149/3 on [1/4, 1/3] and h(553/2000) = −1293623/250000000 (run `exact-certs-v1`). This replaces the v1 Sturm run. |
| L5 (D1 cone, closed form, uniform bound, tails) | Proved in text. Tail constants are EXACT: 428/2125 for ω ≤ 1/4; 232498770764161/700733376734161 for ω ≥ 4. |
| Theorem 5.6 (attainment, upper separation) | EXACT. **Fix (3a):** ω = 1, cos φ = 35/37, sin φ = 12/37 give (m0, m1, m2) = (27, 62, 171)/74, so v_cos ≤ 773/3844 < 0.2014 < 11/50 = T, and 773/3844 < 553/2000 < Δ3. The Arb bound U (`ctl-c-v2`) is now a supplementary conditional computation. |
| Contract-band check | **Fix (2):** relabelled EXPLORATORY. It tests the Newton value, so it cannot give the lower band endpoint. Its "STOP" only prints; a failure reaches the exit code only through `all_pass`. |
| Theorem 5.8: v_cos ≥ 0.20090156350055 | **Fix (4): KEEP, OPTIONAL, COMPUTATIONAL (conditional); used by no proof.** Own audit `audit-bnb-v2` 27/27 and cap control `ctl-f-mut-cap-v1`, plus the independent parent certificate `RESULT-v1.json` (sha256 9a72e3e7…65e3, run `d1b-lower-worker-L`). |
| L6 (D2 cone, feasibility, θ1, moments) | Proved in text. |
| Cor 7.1 (inf over ME(≤3) = I_2 ≤ v_cos) | Proved in text. It uses only EXACT separations. |

**What the theorem uses:** the written lemmas and EXACT facts only. It does not use U, and it does not use the lower
bound of Theorem 5.8.

## 2. Runs added in v2 (launcher `code/run_v1.sh`, one process at a time)

| Run | Program | Exit | Result |
|---|---|---|---|
| `exact-certs-v1` | `code/exact_certs_v1.py` | 0 | 47/47 checks pass. No-float AST self-scan passed. The 5 wrong controls W1, W2, W4, W5, W6 all fail as required. |
| `audit-bnb-v1` | `code/audit_bnb_v1.py` | 1 | **Failed attempt, kept.** Check C4 wrongly expected a finite enclosure on the full middle box. The enclosure is NaN and therefore not certified, which is the correct behaviour. This was an audit-expectation error, not a defect of the audited program. The other 25 checks passed. |
| `audit-bnb-v2` | `code/audit_bnb_v2.py` | 0 | 27/27 checks pass: binding to sha 508b1488…, static acceptance logic, library semantics, run evidence. |
| `ctl-f-mut-cap-v1` | `code/ctl_f_d1bnb_v1.py 0.20090156350055 1/4 4 reject 1000` | 0 | Box cap hit: aborted, 6 boxes left on the stack, outcome **reject**. A cap is never reported as success. |

Exact certificate results:
* C1 moments 27/74, 31/37 (= 62/74), 171/74, giving SCV = 773/3844.
* C1 agrees with Lemma 5.3's algebraic form and with exact SymPy integration.
* C2: h(553/2000) = −1293623/250000000; h′ minimum on [1/4, 1/3] is 149/3; Q⁶h(s) ≡ 0 mod q.
* Exact bracket: Δ3 ∈ (478316921303906167/1729382256910270464, 1275511790143749779/4611686018427387904), i.e.
  0.276582530780945666….
* Controls:
  * W1 swapped cos/sin: SCV = 206/169, fails.
  * W2 h(2766/10000) = 4277637/3906250000 > 0, fails.
  * W4 point 1/5 outside the window, refused.
  * W5 (35/37, 13/37) has c² + s² = 1394/1369, refused.
  * W6 phase sign: SCV = 2549/7396, fails.
* Informational: h(552/2000) = −142803/3906250 < 0 certifies only the weaker, true bound Δ3 > 0.276.

## 3. Files (sha256)

New in v2:

| File | sha256 |
|---|---|
| `proof/reductions-v2.md` | see the final message (this STATUS file cites it, so its hash cannot appear here) |
| `code/exact_certs_v1.py` | 043920f78000949c9a05a9cd7ec88f3d6b9997a05e11cdfd7a3498f693fe255a |
| `runs/exact-certs-v1/exact_certs.json` | b18d51636d4c1998e19e3f7c44c08308660e8f3d1f4f8e0be56fbbc8f4e10a04 |
| `code/audit_bnb_v2.py` | 1eb5a0cf66a551fe201879abf0f85f1eb2c5801d3f108020a89ea6835eefbad5 |
| `runs/audit-bnb-v2/audit_bnb.json` | fbb9c28a2cc306a9a6c13819a0e266f18361f6da37f3282fa648a20f5a7ea8da |
| `code/audit_bnb_v1.py` (failed attempt) | ebf9a4d7b7618c925f9657038c781f431fcc7e1cc72c00a5f1bff252798e5acc |
| `runs/audit-bnb-v1/audit_bnb.json` (failed attempt) | 27534245356da37498d853042b077da956a654d4ce83ba4c194d66a2cd79ebcb |
| `runs/ctl-f-mut-cap-v1/ctl_f.json` | 007b7d9e21bb1b9ab8505f31a928c90dc86c906a4695814f955f3e66a0ade990 |

Pinned for the optional Theorem 5.8 (key files):

| File | sha256 |
|---|---|
| `code/ctl_f_d1bnb_v1.py` | 508b148870fc18e3cb32de6ada1c5245aca4271db92867b959597b4ba29341b7 |
| `code/ctl_f_gradsym_v1.py` | 2417f74037567dcf6ff0a1f74c9f5f33c47cebcc64c5c3ab13b03e4dca9994ec |
| `runs/ctl-f-main-v1/ctl_f.json` | 9a62b9f8e96a03389919e28f037ec8f2a5da53f959dce610982293655f4ea40f |
| `runs/ctl-f-gradsym-v1/ctl_f_gradsym.json` | c15beac679016f07ea8a802c371f98c0069c3cb8fd408048a85e1b7a00c3c774 |
| `receipts/ctl-f-main-v1-pre.json` | b9b6f4905dba821db3cd23ea5529d6281a02cf8e743622ce28be3ab68b6b7c3c |
| `receipts/ctl-f-main-v1-post.json` | 69becaaf14d2cc3d871580600e57f24951cf93656ae8ee06db1968a0646fea98 |
| `receipts/ctl-f-gradsym-v1-pre.json` | 1853275c69f4227af1e7eecf58932838d9f31774a4830da275889160e22bdbab |
| `receipts/ctl-f-gradsym-v1-post.json` | 701242e1bf5534c97ad53f5ab0a79a357d665554acf3c4ea9bd0e029cdf09791 |
| `proof/vcos-lower-bound-v1.md` | 01821b4ce4acbf3708fdda7acefb85e04a00773a5a9c36ab3923f9efa16a9e20 |

Receipts for the v2 runs:

| File | sha256 |
|---|---|
| `receipts/exact-certs-v1-pre.json` | af2aebc74752a5cd0454734c4614b096095b32e0e613f3bad2b258cfa3e3484f |
| `receipts/exact-certs-v1-post.json` | 4f2c98481240f63f078852d39b33d521fd8994eaaa7f9ef54a421892476c6ea3 |
| `receipts/audit-bnb-v2-pre.json` | 59e61c4225ed31ac2bf8a384af8c689b41ff13f9c70b37c3b0edee4d5a4181a6 |
| `receipts/audit-bnb-v2-post.json` | 454035ea81054615772c0ff817ccef77b5287ce9ea4267cdeb842e6cc6a2edeb |
| `receipts/ctl-f-mut-cap-v1-pre.json` | 3b3512f27f957db77c04621dc8f143b99605ce3d156cf13bbf9481d600e3f367 |
| `receipts/ctl-f-mut-cap-v1-post.json` | e83ac2f68435300f05cd3bd949c668eb06dc097b88898c0d9a87bc8a2dc88527 |

The v1 files are unchanged: `proof/reductions-v1.md` ad6c5091…5536 and `STATUS.md` 61776330…2c76.
