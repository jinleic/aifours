# K52W written review package v1 — full K5.2* exclusion [CANDIDATE_UNVERIFIED]

- Written: `/bin/date` read at 2026-10-19T16:53:43-0700 immediately before exclusive create. Owner SunM13MixedFibres.
- Candidate: K/K52-W-v1.md, sha256 c9c5ecbf106e7a9744558837b79567bd9ec3ad2988a562f5e15462b92a3a8e5d, 206 lines, 17,432 B.
- Scope: K/K52-W-SCOPE-v1.md, sha256 bec966875c716ede5bab5e4dc0b5f38544f5606cda781c2c0ac6e2672172e253. The parent sketch was disclosed BEFORE the worker freeze, so no
  preregistration independence is claimed. The old accepted class result, code and outputs are not premises.
- K = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k52-written; ROOT = /Users/jinleic/repos/aifours. Exact absolute paths and whole-file hashes are in the JSON manifest.

## 1. Exact claim, not a new class closure
K5.2* (README line94) is empty: seven pairwise disjoint left cosets, arbitrary group and finite-index subgroups; gcd6
inside C={s} cup O_4, |O_4|=4; gcd4 on d_1-d_2 and d_j-s; gcd2 on d_j-O_4; the stated prime-incidence hypotheses, every
exponent/cofactor and 2/3/5-marker placement. All new claims CANDIDATE_UNVERIFIED pending two-family review and parent.
This is a WRITTEN VERIFICATION REPLACEMENT for the K5.2* part of StageB, not KII or the larger K52 universe including
D2'. The parent retains the old computational proof and F-1 history. No full Sun(7), novelty, Lean or human-review claim.

## 2. Verbatim theorem and proof (candidate lines175-181)
```text
**Theorem K52-W.** No group with finite-index subgroups contains a configuration of class K5.2*, for all exponents,
cofactors and marker placements of the exact class.
*Proof.* R0 reduces an arbitrary-group configuration to finite G with the same indices and disjointness. Put
b=alpha_(d_1 d_2) and b*=alpha*_(d_1 d_2) for its ACTUAL inverted configuration. Lemma B1 applies to both configurations
(the same labelled tuple, SHAPE and marker data are preserved), so b,b*>=2. INV gives b+b*<=4; hence b=b*=2. This
contradicts Lemma B2 for the original configuration. Equivalently, B1/B2 leave b=b*=3, directly violating INV.
All cases, including a putative b=3, have now been covered. QED
```

## 3. Reading order and import boundary
Read transition's parent sketch; frozen scope (all pre-freeze exposure); candidate IN FULL; exact foundational input
extracts below. The proof supplies R0, multiplier bounds, actual INV, and FC24 in full. FC24 uses ONLY Sun(2) (re-proved)
and the accepted classical Sun(4) inside U_v. It uses every 2-/4-SUBset of an actual fibre set even when it has 5 or 6
pieces; it does not assume general LFC(c), Sun(3), Sun(5), Sun(6), VFC or a minimal-counterexample frame. The general
accepted LFC package DOES record computer-assisted Sun(5)/Sun(6) imports, deliberately shown in the extracts for contrast.
No arbitrary theorem from that package is transferred without a proof. No StageB implementation/certificate/output or
accepted K52 conclusion was read as evidence for this proof.

## 4. Written review questions
1. SHAPE (lines25-43): does dividing the raw indices by4,4,12,6,6,6,6 give exactly seven pairwise-coprime factors,
   3-free q_1,q_2 and odd r_o, and conversely exactly the README K5.2* class? No assumed common cofactor normalisation.
2. R0, A, INV (lines58-79): check the finite quotient, product formula and double-coset sum for the ACTUAL inverse.
3. FC24 (lines81-99): inspect every trace subgroup and every fibre count. Are ONLY Sun(2) and Sun(4) used, with strict
   gap from the missing own fibre? Do not assume actual fibre sets have at most4 elements.
4. Local gcds (lines101-128): retain the higher 2-part on d_2 OR s OR the apex; prove the d--s table for b=1,2 and
   a=1,2,3. Check higher3 on s, on a unique t in O_4, or absent, and arbitrary5 location/cofactor primes.
5. Uniform-sketch defect (lines139-142): {s,t,u,v} has pair gcd9 on s,t and3 elsewhere; the uniform weight sum4/3
   is invalid. Corrected E (lines144-152): t has weight0; any4 positive-weight vertices all have gcd3, so cannot occur;
   when d is present, O_4 is absent (coprime labels). Check ALL 24-admissible sets, including zero-weight vertices.
6. B1/B2 (lines154-173): hand-check objectives/case exhaustion; no scientific enumeration or LP answer is evidence.
   Then check the actual-inversion finish in lines175-181, including the putative b=3 case.
7. DAG/boundary (lines183-206): confirm no hidden Sun(5)/(6), StageB or parent-sketch premise, no KII extension.
Return FATAL/MAJOR/MINOR by group, exact file:line, smallest repair; an empty findings list is valid. Mathematical
correctness and the full-Sun(7) gate are separate. Approval is never a premise.

## 5. Exact excerpt sources (inclusive physical raw lines; whole-file sha256)
| source | sha256 | lines | role |
|---|---|---|---|
| K/K52-W-v1.md | c9c5ecbf106e7a9744558837b79567bd9ec3ad2988a562f5e15462b92a3a8e5d | 1-206 | NEW whole proof (SHAPE, R0/A/INV, FC24, exact gcds, repaired weights, B1/B2, full theorem, DAG) |
| K/K52-W-SCOPE-v1.md | bec966875c716ede5bab5e4dc0b5f38544f5606cda781c2c0ac6e2672172e253 | 1-42 | frozen scope and disclosure of parent/pre-freeze sketches |
| ROOT/institute/runs/six-lane-2026-10-18-96h/control/mathematics-slot-transition-sun-stageB-written-20261019-1639-v1.json | f189835cfd4e5e20cd4494e73b27851a07ba0576efc01551260ef5e38ad379cd | 1-12 | authority and UNVERIFIED parent weighting sketch; no theorem premise |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset7/README.md | 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1 | 11-29, 33-52, 85-96 | K5.2* definition, P0/P1 setting, R0, elementary facts, accepted Sun(4) import; no routing reduction used |
| ROOT/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md | 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35 | 16-24, 46, 58-60 | acceptance/notation/class scope and Sun(4) import; no K52 conclusion used |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-v1.md | 77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee | 9-17 | elementary multiplier notation and range |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-v1.md | 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c | 20-45, 54-71 | geometric fibre and actual-inversion origins only; general LFC(c) is not imported |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-erratum-v1.md | 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5 | 10-32, 47-65 | mandatory elementary/index, Sun(2), own-fibre and actual-inversion overlays E1-E3/E6-E7 |
| ROOT/institute/runs/six-lane-2026-10-18-96h/review/sun7-lfc-inv-parent-verdict-v1.md | 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 | 16-23, 31-33 | accepted geometric/INV scopes; computer-assisted general LFC provenance explicitly NOT carried into FC24 |

## 6. Packaging metadata
Manifest K/review-excerpts-K52W-v1.json, sha256 20d885030c5a55e1acca3bbf8a0df7e512da5c3aef837c9df934289fb89b9b32, 3,753 B. It lists 16 inclusive ranges from
9 sources as {path,sha256,start,end}. Raw selected bytes 41,716; package plus selected source 49,149 B
(<=100,000). Hash/range/byte metadata checked; no scientific computation or solver. This packet contains the FULL new
proof, with no mathematical node replaced by context-only claims.
