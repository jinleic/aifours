# Independent reverse/canonical CRT proof of the full d4 orbit identity

**PhysicsResearch96h-2 / physics-1.** Actual native clock at the completed hash observation: **Wed Oct 28 19:20:25 PDT 2026**. This is a second independently arranged **full exact rational** d4 source-orbit identity computation, not merely the earlier one-prime weighted diagnostic. The mathematical implication is conditional on the pinned code/data/runtime and the separately written height-bound and source-group proofs. It is not a human/other-model-family review, formal/Lean kernel, parent/f62 adoption, all-d theorem, operational distillability consequence, or novelty claim.

## 1. Actual complete result

`frontier-20261028-d4-reverse-independent-crt-check.py`, SHA256 `423e58d82a5be68486b8940199335b677f3d69cbb3ba33a37065e1bded42ebbc`, returned **PASS in 162.390 s** on one process with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`. The complete result is `frontier-20261028-d4-reverse-independent-crt-check-results.json`, SHA256 `3afc85cf5f47645314fa4ec369247f357c6e415a834707e273425253eea0ca19`.

- Every one of **424 distinct, trial-division-verified primes** gave zero residual on **all 4675 actual source orbit sums**: family counts 1142/2391/1142. All source denominators were checked coprime to each prime.
- The verifier independently recomputed the actual common denominator D (**6645 bits**) and an integer residual upper bound B (**6745 bits**). The exact product P of the tested primes has **6761 bits**, and the program's actual exact comparison verified `P>2B`.
- Therefore all 4675 rational source-orbit residuals are exactly zero, **conditional on** the written source/stabilizer and height-bound proof plus this implementation/runtime correctness: each scaled integer residual is divisible by P and has absolute value at most B<P/2.
- All **1570** actual physical row-pair occurrences were covered, forming **17** row-pattern groups; independently rebuilt cache contained 60 site maps,36 auxiliary maps and10 equality specifications. The lower map counts reflect a different equal-letter matching/deduplication, not omitted rows.
- In-memory +1 mutation of one aab coefficient at the first prime produced **1142 nonzero family31 and2391 nonzero family22** residuals, as expected for a comparator fault control; no physical C/state was sampled.

The progress file `frontier-20261028-d4-reverse-independent-crt-progress.json`, SHA256 `9bd405b4c3523ec41d5ac3e93cc6c20b825dd306e0090598cff77b86e3f8a822`, is a **historical 400-prime INCOMPLETE snapshot**: the program only updated progress at multiples of50. The separate final receipt above records all424 primes and is the complete terminal result. Do not mistake the intermediate snapshot for the final outcome or silently overwrite it.

## 2. What is genuinely different and what remains shared

The new full computation:

1. constructs source orbit labels by explicit **direct canonical minimization** over all left/right family stabilizers, the three-site permutations and inversion, rather than the prior union-find;
2. uses its own formal physical factor rule, deliberately matching the **last** available identical letter instead of the owner's first-match source rule, and verifies the factor multiset on every used row pair;
3. rebuilds site and auxiliary Gram maps from **explicit finite basis diagrams/indices**, equality maps from independent 3-replica partial-trace indices and integer compression, and the objective from cycle counts, rather than invoking the owner global local-map functions;
4. forms each Gram product in the opposite association `W_r (Z W_s^T)`, and applies `np.tensordot` to the four local axes in **reverse order**, rather than the owner's FLINT-integer forward-axis operation or the earlier modular forward-axis backend;
5. recomputes its own D and complete integer B from the actual corrected coefficients, W values and its own local-map maxima; the exact new B happened to equal the earlier independently audited B. The prior receipt supplies the **prime list**, not the residue values; this run rechecked primality, uniqueness, D coprimality, all residuals and the exact product itself.

The public source/corrected data, data-only parser, literal-reference helper implementations, same NumPy/Python runtime, standard tensor algebra and the mathematical B formula are still shared. The grouping-by-modules and row-major tensor convention implement the same source certificate. Thus this is **not** an independent human/model family, a separate proof assistant, or a proof free of all common-mode software or mathematical assumptions.

## 3. Why reverse matching and the height bound are sound

`frontier-20261028-d4-reverse-crt-conditional-proof-v1.md`, SHA256 `d63142eec546a9ba936d04bbb4c994559a19b0af1028434af376c7662c652294`, supplies the explicit index proof: if two valid ket/bra assignments differ by stabilizers sigma,tau of repeated source letters, then

`V_p[k_sigma;l_tau]=V_(sigma p tau^−1)[k;l]`.

The **same** sigma,tau act on all three physical site permutations and the auxiliary permutation, so they bijectively permute every source orbit. Opposite tie-breaking cannot change that orbit's functional sum. This does not require treating family moments as independent physical objects.

For each final integer-scaled residual R_o, the independently recomputed bound is

`|R_o| <= 24^4 [ Cblock·Zmax·Wmax²·Amax⁴
                 + Ceq·Lmax·Emax⁴ + Cobj·(D/2^31) ] = B`,

with actual-data `Cblock=278530617`, `Ceq=433`, `Wmax=771160`, independent local `Amax=256`, independent equality `Emax=24`, and independent cycle objective `Cobj=1438646272`. These are safe absolute bounds: each source word has no more than the explicit k²r²n² summands per type, and an orbit has no more than24⁴ words. The result file records the full exact D, B, P and all424 primes. Every NumPy int64 contracted axis, Gram rank and orbit sum is checked against signed-64-bit overflow before use; the computation uses no floating-point residual/tolerance.

## 4. Scientific implication and exact remaining gates

The new result removes a substantial **shared source-orbit, equal-letter assignment, local-map and arithmetic-order dependency** from the earlier global identity checks, while retaining the shared inputs/runtime qualifications above. It supplies a second full exact CRT route for the identity—not the merely two-weight diagnostic and not a physical positivity proof by itself.

The actual original complex rank<=2 lift, physical joint Gram blocks, five same-pair equalities and identical marginal compression modules, source commutant/group span, original trace-swap objective, and 1237 saved corrected PSD matrices remain necessary. Their complete fixed-d4 dependency chain is `frontier-20261028-d4-source-dependency-closure-v2.md`, SHA256 `124bd68bf23b52fe5b5b6db4173851b50f075c293d537dbb8fea7ed83680392b`; the owner local-map closure is `frontier-20261028-d4-owner-local-map-closure-v1.md`, SHA256 `24e9a465d057d92960f1211a9ddcd833ee67ca2aae120ef1b80cecee3bba79c7`.

This verifier and note were authored/run **after** Main actually read `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`, and explicitly allowed prospective primary work. The earlier 20/30-minute cadence deviations remain disclosed, with no retrospective continuous-supervision or causal inference. The earlier process-qualified one-prime/two-weight result was **not** an input to this verifier. f62's frozen review is not silently enlarged; Main must decide any prospective use.
