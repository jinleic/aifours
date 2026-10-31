# Candidate composition: no AME(4,6) state has support 48, hence conditional global support at least 49

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 12:31:19 PDT 2026`. **WRITTEN composition of separately pinned author candidates and recorded dispositions.** Every own component is unreviewed; this is not a parent adoption, formal proof, independent-family review or novelty clearance. No held, withdrawn or quarantined material is an input, and no earlier stopped support-48/49/50 route is recovered: the t=24 and t=28 branches use the new six-word lemma and pair-partition CNF certificates written today.

## 1. Claim

Every normalized complex AME(4,6) state, in every product basis, has support N≠48. Combined with the separate candidates for N≤47 (§4), every such state would have **N≥49**, so with the checked 60-term tensor `49≤m≤60`.

## 2. Case split by the number t of maximal coefficients

For each cut U=6ψ is unitary; the t modulus-1/6 entries are singleton rows and columns; the remaining n=36−t pair values per system are E-carried with multiplicity at least two. Hence N≥72−t, i.e. t≥24 at N=48, and the residual excess is e=|E|−2n=t−24 in every cut.

| t | n | e | outcome at N=48 | source (SHA-256) |
|---:|---:|---:|---|---|
| ≤23 | | | impossible: N≥72−t | row count above |
| 24 | 12 | 0 | every residual profile excluded, §3 | §3 |
| 25 | 11 | 1 | no unitary support with excess one | recorded f141 disposition `physics-6-n46-unitary-bridge-t27-t29-parent-v1.md` (`b1d3face7eb8a06faec59031e62971c3054dbd99b9426087d73d882af3f30e40`) |
| 26 | 10 | 2 | excess two forces one eight-entry 3×3 block plus full 2×2 blocks, so n would be odd | `frontier-20261028-unitary-two-excess-classification-v1.md` (`4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0`), also reconstructed in f141 |
| 27 | 9 | 3 | full heavy-core overload | `frontier-20261029-n48-t27-full-heavy-core-v1.md` (`cb62c730d4d72f4662b1778bba2b14fe6bf07919d42dc7b02f7c59d45d5985a7`) |
| 28 | 8 | 4 | five cases, pair-partition CNF with P code, LRAT-checked; no imports | `frontier-20261029-n48-t28-exclusion-v1.md` (`d910803eece60e5bfd3bedee268e0cac9efee129d124cbb8a06093d32f7a141e`) |
| 29 | 7 | 5 | no state has exactly29 maximal coefficients, any N | `frontier-20261029-no-t29-global-v1.md` (`eaa2c9f93b782720527eb0117434a2663954735038330c09b1943bc99831dbe5`) |
| ≥30 | | | t≤29 | recorded f113 disposition `physics-6-maximal-coefficients29-parent-v1.md` (`86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b`; no-OLS(6) and prior-t≤30 boundaries) |

## 3. The zero-excess branch t=24

Residual alphabets: no size6 (`frontier-20261029-n48-t24-no-six-symbol-party-v1.md`, `f54782be3d7f95f461a9507cd0ae1c696e1cbad4b0ae12b38618d8a042f0d4f1`, conditional on the n12 no-Hamming-one candidate `frontier-20261029-n48-t24-noh1-and-six-alphabets-v1.md`, `6bbe85a8b1bec38ef5984d32408c52479ec58edeb3502398d87ab1f7e04a7c96`, which carries no-OLS(6)). A size2 alphabet would force every partner to size6 (2r≥12). Pair products are at least12, so at most one size3 alphabet. The nine profiles and their exclusions:

| profile | exclusion | source (SHA-256) |
|---|---|---|
| 3444, 3445 | activity residue Σr_ir_j−6Σr<0 (−6, −1) | no-six bridge §7 |
| 3455 | activity refinement at the size-5 parties, no import | no-six bridge §7 |
| 4444 | degree normal form plus integer cross-cut phase certificates; identity support via no-OLS(6) | `frontier-20261029-n48-t24-4444-phase-exclusion-v1.md` (`f3d90e07304746c57c7a985893255b03e678e230713f6d6a8a4fb1643ad673b9`) |
| 4445 | ordered-pair antisymmetry contradiction | `frontier-20261029-n48-t24-4445-antisymmetry-v1.md` (`4154df91ee4e8dc91feb724b0174e37643d9a70c66e4b40e237d7ac337c15970`) |
| 3555, 4455, 4555, 5555 | all87 ordered degree cases UNSAT under no-Hamming-one + six-word lemma, LRAT-checked | `frontier-20261029-n48-t24-remaining-profiles-six-word-sweep-v1.md` (`2732770e8377ffa2610138e22f6a3787a4a15a51aff1d3e469a1a5f6c185b315`), lemma `3e8e5a4fc9fbc58b5b6e0a3c6a16bc246fdccd78b2bbbcf6f9e1014b26172f07` |

The 4444, 4445, six-word sweep and no-six results all depend on the n12 no-Hamming-one candidate. A corroborating CNF sweep of the five profiles in the first four rows, with the same flags, is running and is not a premise.

## 4. Conditional global consequence

`frontier-20261028-global-ame46-support-lower47-v1.md` (`dbb3769da37c9fe4861efd98e4c098343a5bdddce08c15480754fe0374b951ee`) is the earlier candidate N≥47, conditional on its pinned chain. `frontier-20261029-n47-residual-reduction-v1.md` (`9d727efb08543532eba75fd26dd647033743e74d0f67f2c9ec58face34c35681`) reduces N=47 to t=27, and `frontier-20261029-n47-heavy-core-written-exclusion-v1.md` (`7fbfc5ce1255e1575b64d3d0b73c612afb2af2c93d8e682f16c8031ff6fa2fea`) excludes that branch. With §§2–3 this would give N≥49. The parent has recorded N≥45 (`physics-6-ame46-global-support-lower45-parent-v1.md`, `28ffc96f2b7295dd62c7efcfe39d066ac1a77449fbf0804a67c86cbce8c8a8cc`); nothing above that is adopted.

## 5. Imports and review boundary

Classical import: no-OLS(6) (Tarry), through f113, the n12 no-Hamming-one candidate and the 4444 identity step. Recorded dispositions: f113 and f141. Everything else is new elementary mathematics plus exact finite certificates (CaDiCaL LRAT, independent RUP checker; exact-CNF scope). Review should re-derive each row, the profile/degree coverage conventions, and audit the encoders. No 48-term or 49-term witness is claimed, and the minimum remains open in 49..60.
