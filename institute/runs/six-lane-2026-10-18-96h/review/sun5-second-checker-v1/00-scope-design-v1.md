# Sun5 second independent checker v1 — scope and design (frozen before code)

- Written: 2026-10-19T17:10:55-0700 (host /bin/date). Owner: worker Sun5SecondChecker. Write scope: this directory only (`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun5-second-checker-v1`), every file created with exclusive mode `x`; corrections only as new numbered versions.
- Authority: parent source scope `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/sun5-sun6-second-checker-source-scope-v1.json` (6cc055bcd254dc4405b2876f67ae6d494534b844605dccb0f6c924662c49659a), full-gate ruling `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/sun7-full-result-computation-gate-ruling-v1.json` (4818f1ca96c99e012d758e165982ec0844228eae07ff3f38b95dc2b7a3a5eada), run contract `contract-v1.json` (55baff0c…ffcaa), worker contract (ef76faef…5f83).
- Status: SOURCE-ONLY. Nothing in this directory has been executed, compiled, tested or linted. No runtime GO is requested or implied by authoring. Parent source review + separate item GO + fresh stability check + five-part release are required before any run; the shared supervisor owns process lifecycle.
- Purpose: a second, independently written exact checker for the accepted computer-assisted Sun k=5 import (Core(5) finite pattern bridge). Verification support only; no new theorem, novelty or priority claim.

## 1. What is checked (finite statement)

Universe 𝓛 = all labelled triples (α, E2, E3): α: E(K5) → {1,2,3} (rules-v1 L0.3), E2, E3 ∈ {0,1,2,3,4, none} (E2 = E3 allowed; rules-v1 §0). |𝓛| = 3^10·6^2, recomputed by the checker from the definition, never taken from old counts.

Claim C5-BRIDGE: the pinned extract has one record per S5-orbit of 𝓛 (orbits pairwise disjoint, union exactly 𝓛); every record except the survivor carries a certificate that the checker re-verifies exactly against rules-v1 + cumulative erratum v3 + proof-v4 §4 semantics; the set of labelled triples covered by SURVIVE records is exactly the S5-orbit of the written-excluded pattern S-D of proof-v4 §6. The S-D exclusion itself is written mathematics (proof-v4 §5–6) and is NOT checked by this program; it is reported as a separate accounted class, never as a computational PASS.

Bridge to the theorem (proof-v4 §4 M1/M2, §7): each rule is a predicate of (α,E2,E3) alone, sound for every admissible τ and every pairwise-coprime r with that marker status. The checker evaluates r-dependence symbolically through marker status (T, K, PB) and through unbounded 2-/3-adic exponents (FH2), never by representative-number simulation.

## 2. Independent representation (deliberately not a canonical-form cube)

- Colourings as edge-colour masks: (A1, A2) 10-bit masks of the α=1 and α=2 edges (A3 = complement). Markers as one-hot 5-bit masks (0 = none).
- Universe constructed by subset decomposition: A1 over all subsets of E, A2 over all submasks of E∖A1. Each colouring gets a sequential rank; a direct-address table maps (A1,A2) to rank and detects any repeat.
- S5 constructed as the closure of the generators (0 1) and (0 1 2 3 4) under composition; the checker verifies 120 distinct bijections (hence all of S5). Induced edge permutations act on masks via precomputed 1024-entry tables.
- Orbits by forward expansion from each record (apply all 120 group elements), with orbit-stabiliser consistency |orbit|·|stab| = 120 checked per record.
- Coverage: an owner array over the dense index rank·36 + marker index. Every labelled triple must be owned by exactly one record: duplicate keys, overlapping orbits, missing triples and out-of-universe images are separate failure reasons.
- Independent cross-check (not load-bearing): Burnside count (1/120)·Σ_π 3^{edge cycles}·(1+fixed vertices)^2 must equal the number of records accepted as distinct orbits.
- No lexicographic canonical form, no canonical-key comparison, no old counts.

## 3. Certificates (strict, exact)

Input: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-core5-certificates-run1-parent-extract.tsv`, sha256 e9bd7c54d9d9c85228f071973763c186d9a064f1269faffd70d43d53e18b5bb2, 635388 bytes, 21150 lines (equals gunzip of producer `engine-v1-run1/certificates.tsv.gz` 1c7e8008a35ac1bd5dbc6be2b3ec886a36b62765a62ef2a15a5ff8f0f541be85, observed by hash). Untrusted.

Line grammar (byte-level regex, no json module): `KEY \t RULE \t WITNESS \n`, KEY = 10 digits in {1,2,3} for edges 01,02,03,04,12,13,14,23,24,34 then `/` E2 E3 with E2,E3 ∈ {0..4,-} ('-' = none). RULE ∈ {T,K,PB,N2,FH2,SURVIVE}; any other rule (incl. the rules-v1 P-pair/F-H1 names, whose serialization is uncited and absent from run1) is rejected.

- T `[[a,b,c],τmin,τmax]`: a<b<c; recompute τmin = lcm_e α_e/gcd(α_e, r_opp(e)) via marker status, τmax = min vertex product; require equality with both serialized integers and τmin > τmax.
- K `[v,[S],"q"]`: S strictly increasing, v∉S, 2≤|S|≤4; every pair {i,j}⊆S has τmin(v,i,j) = α_vi·α_vj (K1 link at v, M1); Σ_{i∈S} α_iv ≥ 4 (L3 violated); q canonical rational equal to Σα_iv/4.
- PB `[v,[S],"q"]`: same index rules; x_j = α_vj/4, u = 1/(4·gcd(r_v,α_jk)) by marker status, hi = largest multiple of u ≤ min(x_j,x_k), lowered by u when the containment forced by equality is barred by K2 (both K2 conditions when x_j = x_k); value = Σ(1−x_j) − Σ_pairs(1−x_j−x_k+hi_jk) ≥ 1; q canonical and equal to value.
- N2 `[]`: all ten α = 2 (rules-v1 L5).
- FH2 `[[a,b],[V2],n_i,n_ii]`: a<b, α_ab = 1, V2 = {v∉{a,b}: α_va = α_vb = 2} ≠ ∅ recomputed and equal; BOTH H2 alternatives for the SAME (a,b): (i) m=4, t_a=t_b=1, t_v=2 on V2; (ii) m=2, t=1 on {a,b}∪V2; other t_l ∈ 1..m; all met-coset sets with |M_l| = t_l, M_a = {0}; λ_l = 4 r_l t_l/m with gcds computed as sup over all instances (2-/3-adic, marker vertex exponent unbounded, primes ≥5 never shared); reject iff F3 fails at a t=1 vertex or some coset with s≥2 has every pairwise gcd < s. Every assignment of both cases must be rejected and n_i, n_ii must equal the exact enumerated counts.
- SURVIVE `-`: allowed only if its orbit is exactly the orbit of S-D (α01=α02=1, α03=α04=2, other six α=3, E2=1, E3=0; proof-v4 §6). Any other SURVIVE is an unexcluded survivor → FAIL.

## 4. Interface (fail closed)

CLI: `--input PATH --expected-sha256 HEX --output-dir NEWDIR --deadline-epoch INT [--cancel-file PATH]`. Bytes read once, hashed, parsed from the same buffer; mismatch → no verification, status INPUT_PIN_MISMATCH. SIGTERM/SIGINT set a cancel flag; the cancel file and deadline are polled during every phase. Output dir created with mkdir (must not exist); RESULT.json and records.tsv written with mode x, flushed, fsynced, re-read and hashed; a final COMPLETE marker binds their hashes. Status values: PASS_MODULO_WRITTEN_SD, FAIL, INCOMPLETE_DEADLINE, INCOMPLETE_CANCELLED, INCOMPLETE_ERROR, INPUT_PIN_MISMATCH. Exit 0 only for PASS_MODULO_WRITTEN_SD after successful publication before the deadline; any publication error → nonzero exit and no COMPLETE marker. Per-record accounting: VERIFIED / FAILED(reasons) / UNVERIFIED / WRITTEN_SD; per-labelled-triple accounting likewise. No asserts; `python -O` cannot change behaviour.

## 5. Independence and reads

Never read: math16/sun-coset5/code/*, any bridge/indep/labelled verifier, engine, check_v2, controls implementation, or any other checker. Allowed: mathematical texts (proof-v4, rules-v1, erratum v3, README, addendum v4), verdict prose for routes/pins, producer output DATA (extract, run.json, survivors.json, controls.json as data). Every read is logged with sha256 in the read log. Disclosure so far: a targeted grep of old AUDIT-v1.md exposed its line 147 (old canonical-form approach) and 149 (old labelled counts); neither is used; this design avoids canonical forms and old counts by construction.

## 6. Deliverables (this directory)

scope (this file), checker source `code/sun5_second_checker_v1.py`, proof-to-code map, scalar schema, read log + independence declaration, frozen controls plan (+ fixtures with hashes, created after the plan), input/resource plan, full-body source review packet, manifest of all SHAs, checkpoints. Nothing self-accepted.
