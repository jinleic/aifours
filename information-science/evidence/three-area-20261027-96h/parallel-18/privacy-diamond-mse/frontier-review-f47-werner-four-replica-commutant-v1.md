# f47 — finite four-replica commutant and d=4 certificate addendum

**VERDICT: 0 FATAL / 0 MAJOR / 0 new MINOR at the exact stated finite-computation scope.** I reconstructed the full weight/differentiation/rank-sandwich argument, reran the supplied standalone witness verifier, and independently rebuilt the actual selected integer rows with a different normalized/min-pivot sparse elimination: both selected modular minors have full rank, and duplicate-row controls reduce the ranks. I separately computed the 24 permutation columns' ranks over Q and checked EVERY selected row annihilates EVERY permutation column over the integers. I also reran the standalone exact FLINT saved-matrix check: all 1237 corrected matrices were positive definite.

This is a same-harness written/computer-assisted review, conditional on the stated finite arithmetic/runtime and the prior certificate bridge. It is NOT a general Schur–Weyl theorem, independent-vendor/human/formal/kernel certification, d>4 result, physical distillability criterion, novelty claim or final parent disposition. The prior f19 documentary MINOR remains historical; no new defect or correction is silently substituted for it.

Reviewer InfoResearch96h-2. Native pre-write observation: `Wed Oct 28 17:40:49 PDT 2026`.

## 1. Complete inputs, observed pins and exact scope

The complete f47 assignment was read FIRST. I then read both whole assigned files through their endings and measured their live SHA-256 values:

- `physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-d4-four-replica-commutant-finite-rank-proof-v1.md`, 101 LF, SHA `49df4f874bf8c4a4da60d61f1b76d9b8028e2acfca5fe6d8c2b378a324501a23`.
- `physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-d4-certificate-verification-addendum-v1.md`, 36 LF, SHA `176eac7dcf96c9819c5d73488787b18a201be0a0b5a46061b26ac83f67a14340`.

The standalone sparse witness checker was fully read and live-pinned at `5a9a0e017900e4a978e6824e4b0d4510634726c4d397f0f7c33f1deff85e8a1f`; its actual JSON witness was pinned at `1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4`. I read the dense FLINT rank source/receipt, the direct-from-saved-data FLINT PSD source/receipt, bound-identity receipt, and zeroed/single-block/coupled/equality/swap/PSD fault-control receipts named in the addendum. The pinned predecessor physical bridge was completely read for my just-returned f19 review; it is not repromoted by a filename.

I am the same-harness f19 reviewer and am not blind to the certificate or topic. The public source and same-lane code/format were previously encountered; this is not a clean-cognition, different-model-family or human review claim. Historical quarantined outcomes are not premises. No author contact occurred.

The specific new theorem is ONLY for local n=2 and n=4, with four replicas:

    Comm {U^tensor4 : U in U(n)} = span_C {V_p:p in S_4}.                (C_n)

It applies n=4 on each of the three physical sites and n=2 on the rank-two auxiliary factor. The RHS has 24 labelled permutation operators but they need not be linearly independent, in particular not for n=2. No general n claim is used.

## 2. Torus weights and the actual integer commutator rows

Index the tensor-product basis by four-letter words x over {0,...,n−1}; let wt(x) count every letter. A diagonal unitary diag(e^{i theta_j}) acts on x by character `exp(i wt(x)·theta)`. For A commuting with EVERY such unitary, each coefficient A_xy with wt(x)!=wt(y) must vanish: choose a phase that distinguishes the unequal integer weights. This is an exact all-angles statement, not a sampled diagonal matrix.

There remain `N_n=sum_w |block_w|^2` complex unknowns A_xy with wt(x)=wt(y). Independently:

- n=2: weight-block sizes `1,4,6,4,1`, so `N_2=1+16+36+16+1=70`.
- n=4: multiplicity types `(4),(3,1),(2,2),(2,1,1),(1,1,1,1)` contribute `4 + 12*16 + 6*36 + 12*144 + 576 = 2716`.

For i!=j, both `E_ij-E_ji` and `i(E_ij+E_ji)` are skew-Hermitian. Their exponentials are actual unitary paths. Differentiating `A exp(tX)^tensor4=exp(tX)^tensor4 A` at t=0 gives `[A,rho(X)]=0`, where `rho(X)=sum_(replica positions) I⊗...⊗X⊗...⊗I`. Taking complex linear combinations recovers `[A,rho(E_ij)]=0`; no assumption that E_ij itself generates a unitary path is made.

For y containing j and x with `wt(x)=wt(y)+e_i-e_j`, the (x,y) entry is precisely

    sum_(u:y_u=j) A_(x,y[u<-i]) - sum_(u:x_u=i) A_(x[u<-j],y)=0.       (R)

Each term indexes a same-weight unknown. These are integral coefficient rows. The saved witness selects finitely many rows; it need not list ALL rows to furnish a lower rank bound. Every tensor-position permutation V_p preserves wt and commutes with rho(E_ij), since rho applies the SAME E_ij in a summed replica position. Thus the 24 permutation columns lie in the exact characteristic-zero kernel of ALL rows, regardless of what the checker reports.

## 3. Modular-minor sandwich, including characteristic-zero direction

Let K be the matrix of all necessary integer rows (R), and P the integer matrix of 24 permutation columns in the weight-restricted coordinate space of dimension N. Universally `KP=0`. A nonzero r×r integer minor modulo a prime p is a nonzero integer, so

    rank_C K >= rank_Fp K,      rank_C P >= rank_Fp P.

A modular upper bound alone would NOT establish a characteristic-zero upper bound. Here the actual checks give lower bounds

    n=2: rank_C K>=56,   rank_C P>=14,     56+14=70;
    n=4: rank_C K>=2692, rank_C P>=24,     2692+24=2716.

The universal inclusion `im P subset ker K` gives `rank_C K+rank_C P<=N`. Thus both lower bounds are equalities, and `ker K=im P` as complex subspaces. Every actual U(n)-commuting A satisfies the necessary torus/commutator equations and lies in ker K; every permutation commutes with all U^tensor4. The two inclusions prove (C_2) and (C_4).

No converse “all K-solutions commute with all U” is needed, and no general Schur–Weyl statement is used. For n=4 there is also a direct characteristic-zero proof that the 24 P columns are independent: the 24 permutations send the single word (0,1,2,3) to 24 distinct basis words. My independent exact Q computation below confirms both n=4 and the nontrivial n=2 rank.

## 4. Actual modular replays and independent checks

### Supplied standalone verifier — actual reviewer rerun

I read the full verifier, checked the pinned source/witness SHA values, and executed it with `-B` and an OUT override into my exclusive root. It re-created the full weight basis and selected integer rows from labels, confirmed p=65521 by trial division, rebuilt 24 permutation columns, computed their modular ranks, applied reverse/max-pivot sparse field elimination to each supplied square minor, and checked each selected row against every permutation. The n=2 duplicate-last-row mutation was required to reduce the rank.

Actual local output:

```text
n=2: N=70, permutation rank mod p=14, selected minor rank=56,
     duplicate-row rank=55, permutation_kernel_check=PASS
n=4: N=2716, permutation rank mod p=24, selected minor rank=2692,
     permutation_kernel_check=PASS
prime_trial_division=PASS, modulus=65521, verdict=PASS
elapsed_seconds=0.855
BOUND_WITNESS_HASH_BEFORE_AND_AFTER 1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4
```

Own-root `frontier-20261028-f47-commutant-replay-results-v1.json` SHA `d504713ebff6ebc2a123c44e52a11bcf936715aaa56b647f21f52431110696ba`. This is a NEW execution of the SAME lane-authored checker, not a new independent implementation. The owner-reported dense FLINT run is a different rank engine but shares the supplied helper's row reconstruction.

The actual command was

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B -c 'import hashlib,pathlib,runpy,sys; root=pathlib.Path("/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart"); p=root/"frontier-20261028-independent-local-commutant-witness-check.py"; w=root/"frontier-20261028-local-commutant-pivot-rows.json"; out=pathlib.Path("/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-f47-commutant-replay-results-v1.json"); expect="1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4"; assert not out.exists(); assert hashlib.sha256(w.read_bytes()).hexdigest()==expect; d=runpy.run_path(str(p),run_name="f47_review"); f=d["main"]; f.__globals__["OUT"]=out; rc=f(); assert hashlib.sha256(w.read_bytes()).hexdigest()==expect; print("BOUND_WITNESS_HASH_BEFORE_AND_AFTER",expect,flush=True); raise SystemExit(rc)'
```

### Fresh rational permutation ranks and integer annihilation

I separately generated words and permutation matrices from their definitions, used a fresh sparse `fractions.Fraction` elimination for the 24 permutation columns, and evaluated each selected (R) row on EVERY column with integer arithmetic (not merely mod p). Actual Eval output:

```text
n= 2 weight_variables= 70 permutation_rank_Q= 14 selected_rows= 56 integer_annihilation_failures= 0
n= 4 weight_variables= 2716 permutation_rank_Q= 24 selected_rows= 2692 integer_annihilation_failures= 0
```

This is an independent implementation of P and the row action, reading the SAME pinned witness labels. Rational ranks are characteristic-zero ranks; integer annihilation is a finite diagnostic of selected rows, while the universal algebraic KP=0 argument covers all rows.

### Fresh full selected-minor rank and both duplicate controls

The following is my independent local Eval cell. It reads the pinned witness, reconstructs the weight-coordinate ordering and (R) independently, and performs NORMALIZED/MIN-pivot sparse modular elimination, different from the author's generator, the supplied reverse/MAX-pivot checker, and dense FLINT. Both actual square minors are full rank; I additionally duplicated the last row in BOTH dimensions and observed the expected one-rank loss.

```python
import itertools,json,hashlib,time
from pathlib import Path
wp=Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-local-commutant-pivot-rows.json')
raw=wp.read_bytes(); assert hashlib.sha256(raw).hexdigest()=='1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4'
ww=json.loads(raw); prime=ww['prime']
def coordinates(n):
 words=list(itertools.product(range(n),repeat=4)); blocks={}
 for x in words:
  sig=tuple(x.count(i) for i in range(n)); blocks.setdefault(sig,[]).append(x)
 co=[(x,y) for sig in sorted(blocks) for x in blocks[sig] for y in blocks[sig]]
 return {v:i for i,v in enumerate(co)}
def literal_row(label,loc,chosen):
 i,j,x,y=label; x,y=tuple(x),tuple(y); row={}
 for u,z in enumerate(y):
  if z==j:
   z2=list(y); z2[u]=i; q=loc[(x,tuple(z2))]
   if q in chosen: row[chosen[q]]=row.get(chosen[q],0)+1
 for u,z in enumerate(x):
  if z==i:
   z2=list(x); z2[u]=j; q=loc[(tuple(z2),y)]
   if q in chosen: row[chosen[q]]=row.get(chosen[q],0)-1
 return row
def rank_min_norm(rows,p):
 basis={}
 for source in rows:
  row={k:v%p for k,v in source.items() if v%p}
  while row:
   pivot=min(row)
   if pivot not in basis:
    scale=pow(row[pivot],-1,p); basis[pivot]={k:v*scale%p for k,v in row.items()};break
   coeff=row[pivot]
   for k,v in basis[pivot].items():
    z=(row.get(k,0)-coeff*v)%p
    if z:row[k]=z
    else:row.pop(k,None)
 return len(basis)
t0=time.monotonic()
for case in ww['cases']:
 n=case['dimension']; loc=coordinates(n); selected={v:i for i,v in enumerate(case['pivot_columns'])}
 rows=[literal_row(x,loc,selected) for x in case['witness_rows']]
 r=rank_min_norm(rows,prime); broken=rows[:-1]+[rows[0]]; rb=rank_min_norm(broken,prime)
 print('n=',n,'selected_square=',len(rows),'exact_modular_rank=',r,'duplicate_last_row_rank=',rb)
print('elapsed_seconds=',round(time.monotonic()-t0,3))
```

Actual output:

```text
n= 2 selected_square= 56 exact_modular_rank= 56 duplicate_last_row_rank= 55
n= 4 selected_square= 2692 exact_modular_rank= 2692 duplicate_last_row_rank= 2691
elapsed_seconds= 0.911
```

The check still relies on Python integer modular arithmetic, the saved witness bytes, the source-coordinate ordering and the prior primality check; it does not constitute a proof-assistant kernel, a third model family, or an all-dimension calculation.

## 5. Product-group source span and connection to the actual d4 certificate

Regroup the four-replica physical-plus-auxiliary space into THREE `(C^4)^tensor4` factors and ONE `(C^2)^tensor4` factor. For invariance under the first independent local U(4), expand an operator against a basis of all other-factor endomorphisms; coefficient uniqueness forces every first-factor coefficient into its commutant. Repeat for the second and third U(4) and the auxiliary U(2). This proves that the fixed subspace for the PRODUCT group is the tensor product of the four individual commutants, without assuming word independence.

Using (C_4) three times and (C_2) once shows every local-Haar-averaged physical moment is in the span of the four-factor permutation words. Its two-sided letter-stabilizer, site-permutation and conjugation/inversion symmetries then permit averaging its real coefficient representation into the orbit sums. Dependencies among n=2 permutation words do not matter because a SPAN, not a basis, is required. Thus this finite n=2,4 argument replaces the named general Schur–Weyl input in my f19 bridge, subject to finite-checker/runtime correctness.

At the exact original target, the source moment uses the SAME pair a,b, the actual rank<=2 complex lift and all three unnormalized partial-trace terms. My f19 review already reconstructed the 1126+111 physical PSD blocks, the five matching equality groups, objective normalization `2^31`, all 4675 orbit identities and every corrected-matrix PSD predicate. These arguments are not inferred solely from the commutant ranks. Applying the new source span supplies their formerly named general-commutant premise, not a certificate for another dimension.

## 6. Verification addendum: observed scope and fresh saved-PSD replay

The addendum's standalone `frontier-20261028-independent-saved-d4-psd-check.py`, SHA `7e564331021ed9358d760b70d3491d7f7a2e212d19d63adabec41f247a912969`, explicitly checks symmetry, positive denominators, exact fmpq Schur updates, zero-pivot/nonzero-row rejection, and counts positive pivots. I re-executed THAT SAME script after redirecting output to own root. Actual output: **1237/1237 positive definite**, zero PSD failures and zero singular matrices, input corrected SHA `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`, elapsed **29.016 s** / 29.13 s wall. Own-root receipt `frontier-20261028-f47-saved-psd-replay-results-v1.json`, SHA `675fcd0ab2ec672012440fb747cac5f79b8d7afe76f6d614ad293fd7688cb8ee`.

This is another run of the same FLINT-based script, not a new algorithm. My f19 reviewer had separately implemented Python Fraction upper-triangular Schur PSD, which passed all 1237 corrected matrices; that test measured PSD, not by itself strict PD. The addendum's owner-side fmpq rank and this rerun DO explicitly measure strict PD of the saved corrected matrices. The earlier f19 MINOR concerned an older BASE-data wording and remains an additive historical correction, not a defect in this later saved-data rank count.

I read the owner-side before/after hash receipt for its same global identity implementation and the actual zeroed, single-block, coupled-block, aab equality, swap-complement and PSD fault-control receipts. Their results match the addendum's stated expected failures; they were not independently rerun in f47. My prior f19 review separately reran the full 4675-orbit identity and an in-memory +1 aab equality mutation. These repeat/extend sensitivity checks, not exhaustive fault coverage or independent-model review.

Actual saved-PSD replay command:

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B -c 'import runpy,pathlib; p=pathlib.Path("/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-independent-saved-d4-psd-check.py"); o=pathlib.Path("/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-f47-saved-psd-replay-results-v1.json"); assert not o.exists(); d=runpy.run_path(str(p),run_name="f47_saved_psd"); f=d["main"]; f.__globals__["OUT"]=o; raise SystemExit(f())'
```

## 7. Verdict, imports and exact limits

No FATAL, MAJOR or new MINOR found in the two assigned f47 sources at their precise scopes. The finite-rank commutant theorem is valid conditional on the actual integer/modular replays and standard matrix-exponential differentiation, finite-dimensional linear algebra, prime-field arithmetic and correct runtime. The addendum accurately separates saved-data PSD, same-code identity replay and fault controls from full theorem acceptance. My distinct normalized/min-pivot implementation and the two duplicate controls provide additional finite evidence; they still share raw witness labels and Python integer arithmetic with the source.

Combined with the separately reviewed f19 physical/identity/PSD chain, the source-span import for the actual d4 q3/rank<=2 certificate no longer needs a GENERAL Schur–Weyl theorem. This remains a conditional computer-assisted/same-harness result until parent, human/configured-family and formal/kernel gates are performed. It gives no d>4 theorem, general NPT/distillability consequence, novelty/priority finding, physical witness or new mathematical discovery. No author contact, external model, nested agent, Git, deletion or infrastructure mutation occurred.
