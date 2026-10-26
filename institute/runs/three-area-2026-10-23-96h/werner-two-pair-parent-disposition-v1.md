# Werner two-equal-pair reference class — parent disposition

Actual clock observation preceding this record: **2026-10-23T15:34:18-0700 PDT** (`/bin/date`). No scientific program, numerical matrix check, CAS, enumeration or proof assistant ran for this disposition.

## Decision and exact scope

**SUPPORTED at the in-harness written-check level**, with complete source/dependency reads and the parent hand checks described below:

For every nonzero two-ququart reference locally equivalent to Schmidt coefficients `(a,a,b,b)`, with a,b>=0, the complete256-dimensional reversed-co-Choi forms satisfy

    -3 C_B <= S_eta <= C_B.

For the representative `eta=(1,1,t,t)`, t>0, the lower form `3C_B+S_eta` is strictly positive and the upper kernel is exactly

    span{eta}_input tensor (C^4 tensor C^4)_output,

of dimension16. The nonstrict inequalities hold at t=0. **No endpoint kernel classification is accepted.** Local unitaries, scaling and group exchange supply the stated entire two-pair reference class.

The supported consequence is `q3(C)>=0` for rank<=2 coefficient operators whose **range or adjoint co-range contains a first-site product ray with such a two-site reference**. The other range vector and both covectors are arbitrary complex vectors. This is not a normal/Hermitian/operator-product ansatz on C.

**Unrestricted W4 remains NOT PROVED.** A general rank-two range need not contain any such ray. Symmetric `-C_B<=S_eta<=C_B` at every angle is not asserted; its known failures are compatible with this weaker sufficient asymmetric route. No negative rank-two Werner witness, all-copy result, equality classification beyond the stated co-Choi kernel, formal proof, human acceptance or novelty certification follows.

## Exact evidence and full parent read coverage

All author files are under `physics/evidence/three-area-20261023-96h/parallel-18/werner3-ququart/` relative to the repository root.

| Source | SHA256 | Parent complete body read |
|---|---|---|
| `proof-two-pair-reference-asymmetric-domination-v1.md` | `c882c5678969a80d0b7c9800dc9086070cf3f70f7b9143c0f08e77db41292478` |358lines |
| `checkpoint-002-eight-dimensional-angular-compression-v1.md` | `47a24185bbf5f1a1de7fbe64f4ec585feda2b488b1e68b53c11fe35c7ad21ecf` |208lines |
| `checkpoint-003-invariant-minus-sign-closure-v1.md` | `761e04717ce22a786352ab75b1faf6ff3c4b865e13714a8da81a290def169a5e` |152lines |
| `checkpoint-004-extremal-charge-sectors-v1.md` | `fc210c46216932b4846d7cad6c1754538d4d66ff597c951d57533ff4b7e6eaf4` |111lines |
| `checkpoint-005-higher-charge-one-sectors-v1.md` | `a7432f7d2d417f60f5bc64d3eea042ca8556b7fe936081afdf25bba4394f5147` |131lines |
| `checkpoint-006-fixed-sector-threshold-and-asymmetric-bridge-v1.md` | `cc8e1ed4830e728cd4f168d3ee3b9657f7aa684908842385a4ac719d0b281399` |223lines |
| `checkpoint-007-nonzero-charge-and-fixed-asymmetric-closure-v1.md` | `4299d5a8e3259f7d7c0911abe6a34a830c62318ad598476450dcf99daf9600b3` |273lines |

Manifest `two-pair-candidate-manifest-v1.json` was read completely and is bound at `6b16b61e9f2cae541c2f1e4df79f0b5a55e6f8cc0013c255ffbc60a63271370b`. All seven listed scientific snapshots independently matched their full SHA metadata at this parent pass.

Actual separate supplied-proof reconstruction:

`mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/peer-review-Werner-two-pair-v1.md`, SHA256 **`bb735afef41bd1907b76ca8f08be528abd0db4559fe0b0259c4fcfd26be64214`**.

Parent read the complete219-line actual return. Its verdict is **0 FATAL / 0 MAJOR / 0 MINOR at Theorems A–B and their full load-bearing closure**. It records independent physical trace contractions for every matrix-entry class, all representation dimensions and all signs. It is another in-harness model worker supplied with the proof/steering, not blind, cross-vendor, human or formal verification.

## Parent hand checks and assurance boundary

This parent performed complete mathematical reads and the following targeted hand reconstructions. **It did not independently recalculate every one of the large raw matrices a third time.** The separate reviewer explicitly reconstructed those matrices; this assurance distinction is deliberate.

1. The physical expansion yields `A_eta=D+|eta><eta|/4`, positive diagonal values a=1+2t²,b=2+t²,c=3(1+t²)/2 and the full Sherman–Morrison correction. The reversed co-Choi ordering is retained. Its rank-one correction vanishes on nonzero-charge sectors by actual support, not by dropping part of an inverse.
2. Representation accounting is exhaustive: extremal32 + higher charge-one64 + lower charge-one64 + fixed8 + spin-two10 + product-adjoint36 + adjoint42 =256. The contraction Gram matrices and the no-intertwiner argument make these reducing spaces, not merely positive principal compressions.
3. The exact reference identity supplies the candidate upper kernel before any positivity assertion. Fixed and low-charge Schur eliminations keep reference cross couplings and nonorthogonal form-versus-action distinctions. The recorded diagonal-dominance conversion divides by the actual Gram upper bound3; coefficient margin1/30 becomes physical margin1/90.
4. In the last adjoint five-block the two squares use `tU-B2` and `tV+B2`; they do not divide by t. The remaining R has `R11>5/3`, `R22>3/4`, `|R12|<=1`, so determinant>1/4. The displayed polynomial for `R22-3/4` splits as `(s²-1)²+4s⁴+6s³+5s+3`, strictly positive. At t>0 the only zero is `U-V+tB2`; endpoint PSD is kept separate.
5. The generalized trace bound uses the just-established upper PSD, not an assumed symmetric lower bound. For s>=5, l>=5/7 gives trace>=131/126; for s<=5, k+l>=2/3 and the tail>=16/9 give85/81. Thus the normalized upper deficit has largest eigenvalue at most its trace<=499/126, and `4I-deficit >=5I/126`. Congruence invariance makes this valid for the nonorthogonal form basis.
6. The one-site generalized spectrum is exactly `{1,-1/3}`. Multiplying it by the two-site spectrum in[-3,1] makes every eigenvalue of `I-T0 tensor T_B` nonnegative. This establishes complete copositivity of the switched map, a sufficient condition only. The rank-two square completion uses cross term `2Re<y,Lv>` and `A^-1 L†y` in the correct orientation, with the full product reference inverse and arbitrary remaining x,v,y.
7. Kernel dimensions for t>0 are8+2+6=16; the explicit reference subspace already has16 dimensions. Endpoint limits use continuous physical matrices with an invertible reference, not singular reciprocal coordinate changes. Scaling/unitary transport does not enlarge the allowed Schmidt pattern to arbitrary spectra.

The auxiliary symmetric quartic classification in checkpoint006 was read but is **not a premise or separate accepted result of this disposition**. Old uniform-point claims, assays and parent Fraction cells are not substituted for the new all-angle proof.

## Source and contribution limits

The author supplied a matched prior comparison against named Wu–Zou/Ulam/source sectors and an explicit hypothesis-noncontainment example. This parent disposition **does not certify that entire source comparison or worldwide priority**. A vector outside stated earlier hypotheses does not prove that its inequality is novel or hard. **NOVELTY_UNCLEAR** remains operative. The exact achieved class is the named two-pair reference theorem, not full W4 or a whole book chapter.

## Next bounded same-problem obligation

PhysicsResearch96h retains physics-1. Before deriving anything new, ACK the scope and record supplied-proof/parent-lead exposure. Keep all current sources immutable.

The next scientific obligation is the **unrestricted two-site-reference sufficient route**, with eta an arbitrary nonzero vector in C4 tensor C4. By Schmidt/unitary/scaling reduction this means all four nonnegative Schmidt coefficients, including zero/repeated values, with no equality-pair or neighborhood assumption:

    C_B-S_eta >=0 and 3C_B+S_eta >=0.

Either prove the stated all-reference inequalities with complete boundaries, or produce an exact failure of this sufficient route and state the first remaining W4 obligation. A negative co-Choi vector is **not** an admissible rank-two negative W4 witness. Success would establish the biseparable-reference range/co-range class, still not every rank-two operator. Do not replace this target by another tiny perturbation region and announce the full step closed.

Written research/source analysis only; no scientific executable, CAS, numerical root or matrix sampling, CLI or nested agents. Any proposed computation requires a separately pinned named admission. One complete candidate/obstruction and a literal residual, not per-sector discovery counts. Original round deadline and checkpoint cadence remain unchanged.
