# f19 — independent review of the d=4 three-copy certificate chain

**VERDICT: 0 FATAL / 0 MAJOR / 1 MINOR, at the exact d=4 scope below.** The MINOR is an overstatement about two BASE-matrix checks, not a mathematical counterexample: the prior Schur routine tests PSD, not strict positive definiteness. I separately checked strict positive pivots on all 1237 base matrices, so the actual PD fact is supported prospectively. All 1237 CORRECTED matrices passed a newly written, independently implemented exact Fraction-Schur replay, and the independent-of-public-author identity checker was rerun on the same pinned corrected data with all 4675 residuals zero. A one-coefficient in-memory mutation was rejected by the identity checker for the expected reason.

The reconstructed mathematical consequence is CONDITIONAL on the exact computation, program-to-map correspondence, and the standard Schur–Weyl import: the certificate implies the original all-complex rank<=2 q3 inequality at d=4. This is substantial computer-assisted/same-harness evidence, NOT formal/kernel/human/configured-family acceptance, an independent model-family review, a general-d theorem, a new discovery, or a final parent disposition. The public paper already claims the target.

Reviewer: InfoResearch96h-2. Actual native pre-write observation: `Wed Oct 28 17:26:50 PDT 2026`.

## 1. Scope, complete reads, input identity

I read the complete frozen f19 assignment first and the complete added-scope record before opening the added candidate. I read ALL three assigned documents and the complete 315-LF global identity script, plus the named source-level walkthrough and the load-bearing base/auxiliary helpers. The 129-LF physical bridge arrived in the additive scope and was read in its entirety. Live SHA-256 values matched all supplied pins:

| Input | Extent | Live SHA-256 |
|---|---:|---|
| `frontier-20261028-d4-source-data-audit-v1.md` | 89 LF | `1240320c5357e34d75c1206056aa072b3758e461c948398fe4e6264b1b1aa566` |
| `frontier-20261028-d4-corrected-certificate-replay-v1.md` | 52 LF | `985e6da6389b893da3a182ddf5015bd73c62410f462d20dafe4611d1255098a5` |
| `frontier-20261028-independent-d4-global-identity-check.py` | 315 LF | `b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d` |
| `frontier-20261028-d4-certificate-bridge-and-independent-identity-v1.md` | 129 LF | `cc9a354a16b9d3abf6ac1ef8ff6fcc6e2041a88d435216b9d9b326a85f348a66` |
| `frontier-20261028-d4-global-aggregation-source-walkthrough-v1.md` | complete | `a8e81561b71e18b30b7e52ce082d7ffad2e90673cec39088ab2fe9a63af01185` |
| `frontier-20261028-independent-d4-base-check.py` | through full structural checks and main | `bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec` |
| `frontier-20261028-independent-d4-aux-equality-objective-check.py` | full used helpers and main | `0949e4945fa5cd20bac6a5d4e976c6756f97a16de2fb5c6b20c759f60798e99c` |

The author-root prefix for those files is `physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/`. I also read the actual results for the base, site, auxiliary/equality/objective, source-orbit, corrected replay, global identity and trace-swap checks. Their reported results are distinguished from my own executions below.

The public primary paper, retained at `institute/runs/three-area-2026-10-27-96h/public-sources/tomar-werner-copies-zenodo23682914-v3.pdf`, live SHA-256 `fe272e67d880a67c3ae2103e4e486753541accc8f64586182df06c279545a4e5`, was inspected for the original statement and complete §§3.1–3.6 validity bridge. To avoid relying on garbled text extraction, I rendered and visually opened PDF pages 3–5 at 110 DPI:

- `frontier-20261028-f19-paper-page-03.png`, SHA `763ad6010c509862a3e364a36d658efe98f49926384dd8bbd7604858bf8d8b93`;
- `frontier-20261028-f19-paper-page-04.png`, SHA `d28f614e18aa47efad9faa77e6aecc1d1c2f89e8178b76bf93b73395fc12539d`;
- `frontier-20261028-f19-paper-page-05.png`, SHA `462ea3eacb21025c8bfdfd1a607399201214fd95f627b3c3622c95c44b566159`.

This is NOT a complete paper or worldwide-source review. I previously reviewed a separate physics-1 rank-two interface in this same harness; I am not the source-code author, but this is not a blind or independent-vendor review. Historical quarantined findings/results were not accepted as premises. No author contact occurred.

## 2. MINOR M1 — strict-base-PD wording overstates what one test measured

Source-data audit **line 48** says “1237/1237 positive definite by both tests.” Its own preceding line 46 and `frontier-20261028-independent-d4-base-check.py:49–65,177–201` show that `exact_schur_psd` returns only a BOOLEAN PSD result and explicitly ACCEPTS an all-zero remaining Schur block. It does not report the absence of zero pivots. The characteristic-polynomial test does establish strict positivity from PSD plus positive determinant, and the independent Schur pass corroborates PSD; the recorded two algorithms did not each independently report PD.

This is a documentary/assurance MINOR, not a failure of the 1237 base matrices or of the corrected certificate. As a prospective independent repair to the EVIDENCE, I ran a fresh strict-pivot upper-triangular Fraction elimination on ALL base matrices from the archive: all 1237 had positive pivots and exact symmetry; a positive control passed and a singular rank-one matrix was correctly rejected. See §8. Recommend an ADDITIVE correction saying “characteristic polynomial established PD and the earlier Schur test independently established PSD; a later strict-pivot audit also established PD.” Do not silently rewrite the historical receipt or treat this additional test as having happened at the earlier clock.

**Additional coverage note, not a second finding against these pinned data:** the base structural helper checks the first four fields of each equality-local signature (side, slot, order, kind), but not cross-part compression-key sequence equality. A deliberately reordered ONE-side `aab` key list in a deep in-memory copy produced zero structural-check errors. For the actual hash-pinned archive I separately compared all four factor-key sequences in both `aab` and `abb`, and they match exactly. Thus the actual equalities are paid, but this metadata helper alone is not a general assertion that arbitrary input's two common-marginal compressions coincide. See §8; no claimed actual-input defect.

## 3. Original physical domain and normalization

Let `H=(C^4)^tensor3` and C:H->H be ANY complex linear operator of rank at most 2, including 0 and 1. No normality, Hermiticity, positivity, reality or product-support assumption is made. All partial traces are unnormalized:

    q3(C)=||C||_HS^2 -(1/2) sum_i ||Tr_i C||_HS^2
          +(1/4) sum_(i<j)||Tr_ij C||_HS^2 -(1/8)|Tr C|^2.

This is precisely EP3(4), not an arbitrary independently varied list of trace moments. Rank 0 is immediate. For nonzero C scale by a positive scalar to `||C||_HS^2=1/2`; q3 is homogeneous in the squared modulus of the scalar. Choose an isometry A:C^2->H containing ran C, including an arbitrary orthonormal completion in rank 1, and put B=2C†A. Then `C=AB†/2`, `||A||_HS^2=||B||_HS^2=2`.

Define `a=vec(A)/sqrt(2)`, `b=vec(B)/sqrt(2)` in H⊗C^2. Both have norm 1 and a's C^2 marginal is I/2. Their same ancilla contraction is exactly C. Conversely, any unit physical pair with that a-marginal reconstructs an isometry A, arbitrary B, a rank<=2 C and squared norm 1/2. Thus this is not an improper enlargement/narrowing of the normalized original complex domain.

For each of the eight site subsets S, direct index contraction gives

    ||Tr_S C||_HS^2 = <a⊗b, F_Q F_S(a⊗b)>.

The complete owner-side coefficient checker reportedly compares 131072 formal term occurrences and all eight subsets with zero mismatch. I additionally independently evaluated both sides on an actual sparse COMPLEX, non-Hermitian rank-2 factorization; every one of the eight values agreed exactly (§8). That single example tests conventions, not the universal inequality.

## 4. Physical moments, source span, valid PSD/equality caller

The source uses one SAME physical pair to form `Y31=|aaab><aaab|`, `Y22=|aabb><aabb|`, `Y13=|bbba><bbba|` on FOUR full H⊗C^2 replicas. Twirling local site unitaries and a common auxiliary unitary, site permutations, and complex conjugation preserves q3; multiplying by positive `L=(2*4^3)^4=2^28` only normalizes the source moments X_f. On source words the objective has the additional 2^3 factor and denominator `2^31=2147483648`. The paper's displayed objective and checker integer numerator have the same factors; the first/last replicas implement F_Q times `product_i(I-F_i/2)`, with the other two unit a replicas traced out.

**Named ordinary import — Schur–Weyl:** the commutant of four copies of U(n) is spanned by the 24 replica permutation operators, including n=2 on the auxiliary factor. Applied locally it puts each twirled moment in the span of four-factor words. The repeated-letter stabilizer acts simultaneously on left and right, site permutations permute the first three word factors, and complex conjugation plus Hermiticity gives the inversion symmetry. Averaging ANY real word representation over these finite actions yields coefficients constant on orbits. Word linear independence is NOT needed. Thus the actual physical tuple lies in the real source span of orbit sums.

**PSD blocks:** for a single row, partial transpose of WHOLE replicas of a pure product projector is another pure projector with those replica factors conjugated; twirling preserves PSD. For the used two-row coupled block, vectors `u=a⊗a⊗b⊗bar(a)` and `v=b⊗b⊗a⊗bar(b)` give the whole PSD Gram outer product of `u⊕v`, including both off-diagonal entries. The local-unitary action, conjugated on the same whole replica, acts consistently on both rows; averaging preserves the block's PSD. The pinned d4 metadata have 1126 single-row and 111 two-row coupled blocks, no gram2. Any fixed integer/real congruence K keeps `K†M(X)K` PSD, regardless of rank/completeness of K.

**Five equality groups:** the three Stiefel contrasts use a-replicas and vanish from `Tr_H |a><a|=I_Q/2` and unit trace. The aab and abb common-marginal equalities arise by tracing the appropriate unit a/b replica; the latter uses the explicitly different survivor order. Partial trace, common twirl and fixed matching compression preserve them. Actual `aab`/`abb` compression-key lists are equal between paired parts on EACH of the four factors, verified independently in §8; the generic structural checker does not itself enforce that fact.

With symmetric PSD Z_t, each `Tr[Z_t K_t†M_t(X)K_t]` is the squared Hilbert–Schmidt norm of `M_t(X)^(1/2) K_t Z_t^(1/2)` and hence nonnegative. Every equality term is zero on the physical X. This logical part is written reconstruction plus the named commutant/finite-dimensional PSD facts, not a kernel-checked theorem.

## 5. Exact computational predicates and what they share

1. **Input identity.** Live public archive SHA `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`; inner compressed d4 certificate SHA `0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f`; exported corrected data SHA `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`. The data-only unpickler forbids global/class loading. Corrected-data hash, target dimension and source member are checked before either of my full replays. Hashes bind bytes, not their scientific meaning.
2. **Base matrices.** The prior exact FLINT characteristic-polynomial sign/determinant check and Fraction-Schur PSD check report zero failures on 1237 symmetric dyadic BASE multipliers. The `e_t` scaling is strictly positive. The later independent strict-pivot test (§8) found all positive definite. Base PD is not a margin proof for the rational correction.
3. **Actual used local maps.** The prior source-bound comparator tested 81552 literal sparse-site diagram pair/permutation entries, the same 81552 in fixed-dimension mode, 1224 auxiliary entries, 648 specified equality compression/permutation entries, and all 331776 objective words, reporting zero mismatches. Site comparisons use an independent literal-index reference and four AST-isolated public-author pure functions; auxiliary/equality comparison imports the public core for comparison and also uses independent explicit reference functions. These are owner-reported prior executions whose actual receipts and relevant source I read; I did not re-execute those individual checks.
4. **Orbit partition.** Independent union-find generates both left and right stabilizer actions, adjacent physical-site transpositions and inversion on ALL `24^4=331776` words in EACH family. Both-direction comparison to public-author labels reported no partition disagreements: 1142/2391/1142 orbits. My subsequent full identity replay regenerated the same counts. This is a partition on source words, not an assertion that the operator orbit sums are linearly independent.
5. **Author correction.** The public verifier was actually run by the owner, with a restricted data loader and AST capture before its return. It reports 2634 exact correction coordinates, a maximal denominator of 6609 bits, 329 corrected equality entries, no nonzero residual out of 4675 and no PSD failure among 1237. Its local source-derived construction/correction/orbit residual are NOT independently implemented merely because it is a different runtime execution. The approximate pre-correction `9.728e-34` diagnostic is floating point and is not used as exact evidence. A correct final identity plus PSD does not depend on trusting the author's CRT construction path.
6. **Corrected PSD — new independent reviewer run.** `frontier-20261028-f19-independent-psd-replay-v1.py`, SHA `9998264bc45b35c736a86189f587e288390e2e88b8d6bf5c3cbef62467cd3e60`, is my separate in-place UPPER-triangular Fraction Schur implementation. It reads the saved rational JSON directly, validates every shape and symmetry, and handles zero pivots by requiring the remaining row to vanish. It ran on ALL 1237 corrected matrices, with all passed and no failures; 329 equality entries were present. Positive, singular-PSD, negative-pivot, zero-pivot/nonzero-row, and nonsymmetric controls all produced their intended outcomes. Actual elapsed 123.415 s / 123.49 s wall. Own-root receipt `frontier-20261028-f19-independent-psd-replay-result-v1.json` SHA `9e7c532904f6e0d19e3e627597229c0c3cd6d9891eed2b5e38da81044052346c`. This is independent code/algorithm structure, not an independent math library or proof assistant.
7. **Complete corrected source identity — reviewer rerun.** I reran the pinned independently rebuilt literal-map/global-aggregation script, one worker/thread, redirecting its OUTPUT OBJECT to my exclusive root rather than overwriting the author's result. It read the same archive/corrected bytes, rebuilt all 17 row-pattern groups and orbits, and found 0/0/0 nonzero residuals for 13/22/31, respectively; 4675 total, common denominator 6645 bits. Actual reported elapsed 65.190 s / 65.42 s wall. Own-root result `frontier-20261028-f19-identity-replay-results-v1.json`, SHA `2b590d26f5f4b87193ebecfdee9a1dc30c9835710d764fe0c35c44033891ce44`. This is a fresh execution of the SAME checker code the lane author wrote, not a third global implementation.

The global script does not import public `ep3core.py`/`verify_perd.py`, but it DOES share the lane author's restricted parser, auxiliary/equality literal helper, corrected-data file, Python/numpy/FLINT arithmetic and underlying structural conventions with other checks. It directly groups all corrected row pairs, contracts local factors in exact integer arithmetic and sums each full word's coefficient into its independently union-found orbit. No rounding is used in that terminal identity. The PSD replay and identity replay consume the same ordered matrices from the same pinned corrected file, so their binding does not require trusting that the correction came from any particular solver.

## 6. Identity implication and original target

For each source family, the independent checker forms the objective minus ALL 1237 `Tr(Z_t K_t†M_t K_t)` contributions and ALL five equality-group contributions. Exact zero on EVERY one of the 4675 orbit sums makes that linear functional zero on their real span, including all physical moments. The 17 grouping buckets are an implementation organization, not an assumption that different physical inputs can be chosen per block.

Together with §4, the checked identity gives, conditionally on the named program/standard-math imports,

    q3(C)=c(X)=sum_t Tr[Z_t K_t†M_t(X)K_t]+sum_e lambda_e E_e(X) >= 0

for every normalized nonzero original rank<=2 complex C; zero and scaling give the exact full original d4 domain. Corrected PSD and identity BOTH matter; neither the base PSD nor the approximate float residual is enough by itself. The separately reconstructed swap caller preserves the unnormalized partial-trace convention and all physical subset coefficients 1,−1/2,+1/4,−1/8.

This conditional reasoning does not independently prove Schur–Weyl, a formal semantic correspondence of every Python/FLINT instruction, a Lean build/axiom audit, Costa Rico's physical distillability criterion, any d>4 result, or a globally new theorem. The source's broader claim and prior status remain separate from this d4 certificate review.

## 7. Actual rerun commands and targeted mutation

The exact isolated identity replay command was (single worker/thread; `-B` prevents bytecode writes):

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B -c 'import runpy,pathlib,sys; p=pathlib.Path("/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-independent-d4-global-identity-check.py"); o=pathlib.Path("/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-f19-identity-replay-results-v1.json"); assert not o.exists(), "refuse overwrite"; d=runpy.run_path(str(p),run_name="f19_readonly_replay"); f=d["main"]; f.__globals__["OUT"]=o; print("f19 output",o,flush=True); raise SystemExit(f())'
```

Observed terminal result: `common denominator bits 6645`, groups `1 of 17` through `17 of 17`, `independent_orbit_counts={13:1142,22:2391,31:1142}`, `nonzero_residual_counts={13:0,22:0,31:0}`, `corrected_multiplier_count=1237`, `corrected_equality_count=329`, `verdict=PASS`.

The actual independent PSD replay command was

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-f19-independent-psd-replay-v1.py
```

Its observed stdout and five controls are preserved verbatim in the own-root JSON receipt named above.

**Targeted identity sensitivity:** after checking the real input hashes, I changed ONLY the numerator of corrected equality `aab` at index `[0,0,0,0]` by adding its denominator (i.e. coefficient +1) IN MEMORY; no input bytes were changed. The first wrapper attempt stopped with `NameError: original is not defined` before loading/evaluating the identity or writing an output. I corrected the wrapper's function-global binding and reran the failed step. The complete 64.297-second identity recomputation then returned expected `FAIL`, with nonzero orbit counts `{13:0,22:2391,31:1142}` and `EXPECTED_IDENTITY_FAILURE True`. The negative-control output `frontier-20261028-f19-identity-single-equality-mutation-v1.json`, SHA `b6ab9842f270465fb54428815bf61ba33d42f4a3bdfeccf9f5dfc56728adf08b`, reports the ORIGINAL source-data hash because those original bytes were loaded and verified before the wrapper modified one in-memory coefficient; it is expressly a MUTATION result, not an original-certificate failure. One mutation is not exhaustive software verification.

## 8. Independent smaller exact checks and actual outputs

### Base strict pivots and equality compression compatibility

Using the SHA-pinned archive and the existing restricted data-only parser, I independently applied an upper-triangular exact Fraction elimination requiring EVERY pivot to be strictly positive. Actual output:

```text
fresh strict-pivot base audit: matrices= 1237 nonpositive_or_nonsymmetric= []
strict control accepts positive/denies singular: True True
```

This uses a fresh predicate beyond the older Schur routine: zero pivots are rejected, rather than treated as legal PSD. It consumes the public archive's BASE matrices, not the corrected data.

For the actual paired common-marginal equality specifications, a direct comparison of the four factor-wise ordered compression-key lists gave TRUE for BOTH `aab` and `abb`. In an independent deep in-memory copy, swapping two key entries on ONLY one `aab` part changed that compatibility test to FALSE, while the earlier `structural_checks` returned zero errors. Actual output:

```text
mutated one side module-list order: semantic_same_compressions= False
base structural checker number of errors= 0
original pinned data: aab and abb compression key sequences match= True
```

This demonstrates precisely the helper's coverage limit; it does not itself establish the mutated global certificate identity or a false physical inequality. The actual pinned input is not the mutated one.

I also parsed the pinned archive with the data-only unpickler for each per-dimension file; actual `(declared dimension, type count)` values were `{3:(3,715),4:(4,1237),5:(5,1347),6:(6,1347),7:(7,1347),8:(8,1347)}`. The cited paper's V17 wording says “every one of the 1347 multipliers” for d=3,...,8, while Section4 explicitly gives 715 and1237 for d3/d4. That separate documentary source-count discrepancy was already disclosed in the candidate and is not a new mathematical finding about the d4 certificate.

### Independent complex physical swap sample

The following local Python Eval cell uses exact Gaussian-integer pairs and `Fraction`, independently expands a sparse U,V factorization and all eight actual partial traces and swaps. Columns of U and V have disjoint nonempty supports, so C=UV† has rank exactly 2; C is non-Hermitian. It tests a caller convention only.

```python
from fractions import Fraction as F

def addc(a,b): return (a[0]+b[0],a[1]+b[1])
def mulc(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def sq(a): return a[0]*a[0]+a[1]*a[1]
Z=(0,0)
U={(0,0):(1,0),(1,0):(0,1),(21,1):(1,1),(42,1):(1,0)}
V={(0,0):(1,1),(5,0):(1,0),(21,1):(1,0),(63,1):(0,1)}
def digits(x): return (x//16,(x//4)%4,x%4)
def undigits(t): return 16*t[0]+4*t[1]+t[2]
C={}
for (x,r),u in U.items():
 for (y,s),v in V.items():
  if r==s: C[(x,y)]=addc(C.get((x,y),Z),mulc(u,conj(v)))
results=[]
for mask in range(8):
 T={}
 for (x,y),val in C.items():
  xd,yd=digits(x),digits(y)
  if all(xd[k]==yd[k] for k in range(3) if mask&(1<<k)):
   key=(tuple(xd[k] for k in range(3) if not mask&(1<<k)),tuple(yd[k] for k in range(3) if not mask&(1<<k)))
   T[key]=addc(T.get(key,Z),val)
 direct=sum(sq(v) for v in T.values()); swap=Z
 for (x,r),u in U.items():
  for (y,s),v in V.items():
   xx=list(digits(x)); yy=list(digits(y))
   for k in range(3):
    if mask&(1<<k): xx[k],yy[k]=yy[k],xx[k]
   Uprime=U.get((undigits(xx),s),Z); Vprime=V.get((undigits(yy),r),Z)
   swap=addc(swap,mulc(mulc(conj(Uprime),conj(Vprime)),mulc(u,v)))
 assert swap==(direct,0)
 results.append(direct)
q=sum((F((-1)**mask.bit_count(),2**mask.bit_count())*v for mask,v in enumerate(results)),F(0))
print('all_8_swap_equalities=',len(results),'subset_trace_squared_norms=',results)
print('q3_exact=',q,'rank_C=2 via independent U,V columns; C_not_Hermitian=',C.get((0,5),Z)!=conj(C.get((5,0),Z)))
```

Actual output:

```text
all_8_swap_equalities= 8 subset_trace_squared_norms= [12, 8, 6, 6, 5, 5, 4, 4]
q3_exact= 23/4 rank_C=2 via independent U,V columns; C_not_Hermitian= True
```

No one sample proves the universal inequality. The direct physical lift, valid moment construction and exact certificate identity are the actual conditional bridge.

## 9. Final assurance boundary

At exact d4 scope the shared public-source data, corrected identity, independent exact PSD, and reconstructed physical bridge supply a complete conditional computer-assisted chain. MINOR M1 needs the historical wording correction; it does not alter the d4 conclusion. The raw global replay is SAME lane-author code run again, while the PSD replay is a newly implemented independent Schur path. Shared Python/numpy/FLINT, the restricted source parser, metadata, saved certificate, representation conventions and the Schur–Weyl theorem remain named dependencies. No triple-independent implementation, formal/kernel, human/configured-family or external-model review was performed, and one deliberate mutation does not exhaust possible defects. Main must read these complete bodies/results and decide any parent adoption.
