# K62-M13 parent provenance and exposition erratum v1

Recorded at 2026-10-19T12:42:17-0700. Read after the frozen M13 files A `77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d`, B `455c58f9d35cc165f666eeaec9462e6b6ab6286196450532e619d6c0b9810058`, C `13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12`, D `d5fabd614afd1ef626d206df01f165db25883e54668c5ceab1e8ca69b7462194` and the worker overlay K62-M13-erratum-v1 `a4c476c10aede99ed77420413eec21549988c93926ce5d5fc081f4feefc346d9` (applied first). Disposes Claude `53c3a6de375b2c69e8b5d1ea2572f8c0908b5f89f871f2cde44666324f72333a` (ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 3 MINOR, all provenance or exposition). Codex `c8c4184bb4c71df3a34f04dcf1f03424b76df60ea9b229216eea6e89c14ef17d` M1 is already disposed by the worker overlay, which the Claude v2 snapshot reviewed. No statement, centre, orientation or strictness changes. Each Old span occurs exactly once in its source.

## m1 premise narrowing (C:16-17)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-C-v1.md

Old:
````text
  - CAP-62 (C1), with the hypothesis x_(d i*) = 1 (used for x = alpha only); Lemma RC, item CD3 of the CAP/DT overlay
    (sha256 996f924c731f0bfb1bf2a336d50d6ac0be50e55fb4ce134fa4b3cec2a1e2466d). Uses of these are CONDITIONAL ON CAP/DT VERDICT.
````

New:
````text
  - CAP-62 (C1), with the hypothesis x_(d i*) = 1 (used for x = alpha only), and RC-i* at f* = 1, each only at the interface
    discharged by parent CAP-DT verdict 84061c6f; the fresh light-fibre row count of the K62-M13-erratum-v1 (a4c476c1) New
    block; and the inline light-set derivation at C:74-76. No general Lemma RC, item CD3, or VFC-form rule is imported.
````

## m2 definitions of Phi^y and tight (C:66-67)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-C-v1.md

Old:
````text
Let y be either family, y' its opposite, v in O unmarked and a != b in O minus {v}. In the Phi^y-configuration at v put
X^v_j := Phi^y_v Phi^y_j.
````

New:
````text
Let y be either family, y' its opposite, v in O unmarked and a != b in O minus {v}. Here Phi^alpha = (U_j) in Gamma and
Phi^(alpha*) = (U*_j) in Gamma*; an edge vj is tight when y_vj + y'_vj = g_vj, i.e. X^v_j and D'_j partition G. In the
Phi^y-configuration at v put
X^v_j := Phi^y_v Phi^y_j.
````

## m2 reason for y_ab = 1 (C:93)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-C-v1.md

Old:
````text
(In particular y_ab = 1 forces this, and so do y_ab = 2, tau = 8 and y_ab = 4, tau = 16.)
````

New:
````text
(In particular y_ab = 1 forces this, because 4 divides tau and tau <= x_1 x_2 = 4, so tau = 4 = 4 y_ab; and so do y_ab = 2,
tau = 8 and y_ab = 4, tau = 16.)
````

## m3 premise pointer (D:11)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-D-v1.md

Old:
````text
- **Candidate premise:** the global 5/6 bound for both rows at every unmarked v, M13-C section 2 (sha256 13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12),
````

New:
````text
- **Premise:** the global 5/6 bound for both rows at every unmarked v, M13-C section 2 as replaced by the New block of
  K62-M13-erratum-v1 (sha256 a4c476c10aede99ed77420413eec21549988c93926ce5d5fc081f4feefc346d9); the frozen C file
  (sha256 13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12) still carries the superseded general-RC text at C:58-63,
````

## Status tags (Claude m1 tag part and notes)

Every "CONDITIONAL ON CAP/DT VERDICT" or "candidate" tag in A-D (A:117-118; B:1, 10-12, 61, 73, 80; C:1, 15-17, 52, 65, 99; D:1, 12, 99-100) is read as follows: the CAP C1 and RC-i* imports are discharged by parent verdict 84061c6f at their stated interfaces; the new M13 claims are accepted only by the parent M13 verdict and only at its stated scope. DT-C remains outside this packet.

## Notes recorded without text change

- D:29-32 lists only odd z; even z shares no odd prime and nothing depends on it.
- SCOPE:3 timing wording is superseded by checkpoint-017:39-42; exploratory derivation preceded the scope freeze, so no preregistration claim is made.
