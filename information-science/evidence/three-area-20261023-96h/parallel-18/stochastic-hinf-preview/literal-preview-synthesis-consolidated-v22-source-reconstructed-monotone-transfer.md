# Literal preview upper transfer — complete primary-source/continuous proof of the sqrt2 factor

Owner **InfoHinfPreview-2 / info-3**. Actual immediately preceding `/bin/date` BEFORE this write: **Mon Oct 26 07:32:45 PDT 2026**. **NEW COMPLETE WRITTEN OWNER-CANDIDATE**, requiring its own full source/proof/dependency/application gate. SOURCE-SYMBOLIC writing only, including privately; no numerical/rational plant instance, finite-word/control trial, decimal/magnitude probe or withdrawn guidance. No scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/simulation/build/test/CLI/nestedagent/newGO. No mathematical machine check is claimed.

## 0. Exact contribution and positive PRIOR attribution

The optional sqrt2 upper transfer in older dossier records remained NOT_RECONSTRUCTED at its sharp probability/source interface. V11/v14 instead supplied a self-contained NONSHARP2sqrt2 bound. Here the ENTIRE needed continuous-process probability proof and its actual finite/infinite literal-control application are supplied. It gives

```text
G1(F)<=sqrt2*G2(F)
```

for a fixed law on the SAME progressive-input/local-PATHWISE-control domain, assuming its actual strong stopped-input consistency and a finite RMS OUTPUT bound. It does not assume expected control energy, free-control H1, a full-state mean, coercivity, stationarity, zero-input EMS or input continuity for this UPPER direction.

**This probability inequality is PRIOR**, not a new discovery. The actual primary is Sarah Geiss and Michael Scheutzow, [*Sharpness of Lenglart's domination inequality and a sharp monotone version*, arXiv2101.10884v2,22March2021](https://arxiv.org/html/2101.10884v2), Theorem2.2 and ENTIRE Section4 proof. Their general monotone theorem gives p^(-p), versus the usual nonmonotone p^(-p)/(1-p). We reconstruct the continuous accumulated-energy case directly; no whole general càdlàg/predictable announcing theorem or its global sharpness proof is silently assumed.

The new useful work here is complete proof/interface closure at the ACTUAL original input/horizon/admissibility boundary. It prospectively strengthens the currently self-contained nonsharp upper, but does not backdate old source coverage, edit a frozen assertion, accept an old application automatically or imply SAME-gamma literal/RMS synthesis.

## 1. Prospective order, actual primary reading and exact evidence

ENTIRE v120-B ACTUALLY RETURNED before the new whole-primary ACK SHA256 `00671413a6b56430de28200b355cdfdba71eb22c9e620e8fe4082b603cb2ed28`, written06:44:04 and SENT after06:44:42 BEFORE current primary work. Complete new proof/source/application state was saved in checkpoint44, actual07:30:26, SHA256 `6f710865d279b9f8623c86278a3c4ad4f69c6ef1241a28b5ebcf9dc9e3510d1f`, before this manuscript. No live review was interleaved.

Actual primary source read:

- Exact version URL: [arXiv2101.10884v2 HTML](https://arxiv.org/html/2101.10884v2), with the actual source header22March2021.
- Native reader artifact **`artifact://35058`**, COMPLETE logical1–300 from the URL response and separate raw301–410 through the final references/ending. This includes Theorem2.2, ALL Section4 including the final lambda=p choice, the supplied alternative sharpness construction and discrete-corollary ending.
- Actual reader-log metadata: **409 line feeds/49237B, no final newline**, while the reader footer counts410 logical lines. SHA256 **`f2e9ce54a37dedf404d160a814d9016ce2371262a5cfb2cc67f0dd94d12f5166`**. This is a READER-LOG checksum, NOT an authenticated original-PDF checksum.
- Whole intake record: `sharp-monotone-source-intake-v1.json`, SHA256 `5663d329a6bd0e22c9c477188b0c3b148daa97d17fb1f1036d80760728c75f17`. A metadata observation bound is not an exact private-read/creation instant.

Whole body reading is not an assertion that every transitive reference/discrete/general-sharpness result was independently reconstructed. Source numeric examples were read as context, not re-evaluated or used as probe guidance. General probability-class sharpness is not needed to prove this upper and does NOT imply that sqrt2 is attained by the original control plants.

The COMPLETE173LF own v14, SHA256 `d956c0827df54c7e9e1c5a63a0af00673208ec24c7c6bd4d4d44cd0f4395a8c8`, was actually read raw1–95/96–173 before this source work. Its lower/domain statement is context or a NAMED additional theorem only where explicitly composed below. No previous optional assertion or review headline is a new proof premise. The original COMPLETE17LF model boundary SHA256 `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a` was actually read in the current primary chain; no new pixel/library read is inferred.

The needed ordinary facts are bounded stopping-time consistency/expectation, continuity/monotonicity and level hitting times, pointwise truncated-moment integration, Tonelli/monotone convergence and elementary rescaling. All new probability and model-specific applications are displayed below. No sharp external theorem remains an opaque correctness premise of the stated continuous version.

## 2. Needed continuous monotone domination theorem — exact statement

Let X,A be nonnegative CONTINUOUS adapted NONDECREASING processes on a usual filtered probability space, with X0=A0=0. Assume for EVERY bounded stopping time tau,

```text
E X_tau<=E A_tau.                                     (DOM)
```

Extended expectations are allowed. Then, for every finite T and every SYMBOLIC exponent0<p<1,

```text
E X_T^p<=p^(-p) E A_T^p.                              (MON)
```

The same holds at infinity by increasing T. If the right side is finite the left is finite; if it is infinite the extended inequality is understood. This is the continuous accumulated-energy specialization of the PRIOR monotone Lenglart theorem. We do not claim its broader conditional/càdlàg hypothesis replacement or sharpness on physical control systems.

## 3. Full probability proof — truncate EXPECTATIONS, not just tail probabilities

Fix a truncation level r>0 and a scaling theta>0. Let

```text
tau=inf{t>=0:A_t>=theta*r} wedge T.
```

This is a bounded stopping time. A's continuity and monotonicity give EXACTLY

```text
A_tau=min(A_T,theta*r).
```

If the level is not hit before T, tau=T and there is no later increase. If it is hit, X_T wedge r differs from X_tau wedge r by at most r. Monotonicity also makes that difference nonnegative. Thus pathwise

```text
X_T wedge r<=X_tau wedge r+r*1_(A_T>=theta*r).
```

DOM and `X_tau wedge r<=X_tau` yield the improved truncated-expectation inequality

```text
E(X_T wedge r)
 <=E(A_T wedge theta*r)+r*P(A_T>=theta*r).             (TRUNC)
```

Only a stop at the INPUT-energy level was used. No announcing sequence, jump overshoot, unbounded stopping-time theorem or martingale representation is imported. Continuity is the actual feature making the energy-level equality exact. The inequality is stronger than the old ordinary probability-tail estimate, and its use of X monotonicity is essential.

For a fixed nonnegative number z, split the following integral at r=z to obtain

```text
p(1-p) integral_0^infinity (z wedge r)r^(p-2)dr=z^p.
```

Tonelli therefore gives this identity for any nonnegative random Z, including infinite moments. Apply it to X_T and substitute TRUNC. The first term rescales u=theta*r to give `theta^(1-p) E A_T^p`. The second uses ordinary tail integration:

```text
p(1-p) integral_0^infinity P(A_T>=theta*r)r^(p-1)dr
 =(1-p)theta^(-p) E A_T^p.
```

Consequently

```text
E X_T^p<=theta^(-p)(theta+1-p)E A_T^p.
```

Choose the SYMBOLIC value theta=p. Since p+1-p=1, its coefficient is exactly p^(-p), proving MON. This is an analytic theorem parameter choice, not a numerical plant/viability trial. At p=1/2 the coefficient is sqrt2. Increasing T and monotone convergence prove the infinite-time version, without an infinite stopping time in DOM or a hidden uniform-integrability assumption.

This is the entire needed probability proof, adapted from the actual prior source to the continuous energy case. The conditional-F0/general-predictable localization parts of the published theorem are NOT needed here, and no claim of newly reconstructing their full transitive foundations is made.

## 4. Exact original operator/application contract

Let ONE fixed law act on the ORIGINAL constant-data scalar-Brownian plant

```text
dX=(A X+B u+C w(t-h))dt+(A0 X+B0 u)dW,
z=D0 X+D1 u.
```

Ranks/data are arbitrary. Gain initial state/negative input history are0. Allowed w are ALL canonical progressive inputs of finite EXPECTED squared energy. Controls retain the frozen LOCAL PATHWISE time-L2 admissibility, with strong nonanticipative/event-local well-posedness/nonexplosion. No expected control energy/H1 is inserted.

Require ACTUAL stopped-input consistency: for every bounded stopping time tau, the allowed input stopped after tau, driven on the same noise, has the SAME output up to tau as the original input. This is a substantive strong causal response property, not a consequence of writing a weak deterministic mean map. A well-posed original nonanticipative current-state/current-window law supplies it by identical prefix coupling/strong uniqueness; no extra memory, controller clock or future information is added.

Assume the SAME law and SAME input class have an RMS OUTPUT bound k>=0:

```text
E||z(w)||_time-L2^2<=k^2 E||w||_time-L2^2
```

on the specified counted horizons, including the zero input. The actual zero response is retained; input stopping preserves the class. No RMS synthesis theorem, policy replacement or necessary controller regularity is inferred from this inequality.

## 5. Infinite horizon — ALL progressive inputs and all zero/infinite cases

For a fixed allowed input define the ACTUAL energy processes

```text
X_t=int_0^t |z|^2,
A_t=k^2*int_0^t |w|^2.
```

They are nonnegative continuous adapted nondecreasing, starting0. A is in particular predictable, though the continuous proof already handles its level stops directly. Local pathwise output energy is well defined by the admissible state/control paths; the RMS bound additionally gives finite expected full output energy.

For EVERY bounded stopping time tau, apply the RMS OUTPUT inequality to `w*1_(s<=tau)`. It is allowed, with expected squared energy unchanged up to tau and0 later. Strong stopped consistency identifies earlier output; discarding later nonnegative output gives

```text
E X_tau<=k^2 E int_0^tau |w|^2=E A_tau.
```

Thus every hypothesis of MON is matched on the SAME actual stochastic law. At p=1/2 and then increasing T,

```text
N1(z)=E sqrt(X_infinity)
 <=sqrt2 E sqrt(A_infinity)
 =sqrt2*k*N1(w).                                      (UP-INF)
```

This neither takes a full-state mean nor proves integrability of an individual unpriced stochastic control. X,A are PROOF energy variables, not physical controller states.

If k=0, the RMS bound makes output0 a.s. for every allowed input, so G1=0 without a division. If only G2=infinity is known, the upper comparison in extended reals is trivial and supplies no finite feasibility statement. If G2 is finite, its defining supremum supplies the pointwise RMS bound with k=G2 on every input, so

```text
G1<=sqrt2*G2.                                         (UP)
```

No stationarity, EMS, R/Q coercivity, rank, input continuity, forced-state first/second moment or external sharp transfer is required for this UPPER statement. Those may be needed for a separate lower theorem, not hidden here.

## 6. Finite counted preview horizon — no change in the book's norm placement

Fix T>h>=0 and L0=T-h. Count allowed input only on[0,L0], extend it by0 afterward, and count output on[0,T]. Suppose the SAME finite-horizon law has RMS OUTPUT bound k on that class and actual stopped-input consistency.

For any bounded tau<=T, the stopped input remains0 after L0 and

```text
E int_0^tau |z|^2
 <=E int_0^T |z(stopped w)|^2
 <=k^2 E int_0^min(tau,L0) |w|^2.
```

Set `X_t=int_0^min(t,T)|z|²` and `A_t=k²int_0^min(t,L0)|w|²`. Both are continuous adapted nondecreasing. For stopping times beyond T, cap them at T; their values are unchanged. Hence DOM holds for every bounded stop, with the ACTUAL counted input and output lengths. MON gives

```text
E||z||_L2(0,T)<=sqrt2*k*E||w||_L2(0,T-h).               (UP-FIN)
```

No square is moved through expectation and no input outside the counted interval is charged. Stopping input at tau preserves all earlier measured windows/forcing because h>=0; no pre-actuation is forbidden or reset. This is a norm implication for a FIXED admissible finite law, not a finite-time stationary-controller realization theorem or a claim that finite-horizon G2<=G1 holds.

## 7. Prospective compositions and the exact current risk example

### 7.1 Composition with the separately supported v14 lower domain

The complete v14 theorem has the specific stationary/current Hilbert-window+fixed-taps/canonical/STATE-LOC/zero-window EMS domain and proves G2<=G1. It is not a theorem about arbitrary memory/non-Feller/finite-horizon controllers. If its ENTIRE named lower scope is composed with this newly reconstructed UPPER scope, then prospectively

```text
G2<=G1<=sqrt2*G2
```

on that exact common infinite domain. This gives finite-gain equivalence, not equality of the values. Uniform G1<gamma requires G2<gamma; for a fixed such law, G2<gamma/sqrt2 conservatively suffices. No universally optimal linear/RMS controller, stronger-admissible replacement or SAME-gamma existence equivalence follows.

A NEW complete source/union gate must decide that composition before promotion. The old optional source assertion and its historical NOT_RECONSTRUCTED label are not silently rewritten by this later packet. Other old application claims require their own full hypothesis/value match, not automatic transfer of the probability headline.

### 7.2 New v21 multiplicative-noise upper, reconstructed directly

For arbitrary positive a,c,d,sigma with q0=2a-sigma²>0, h=0 and

```text
dX=(-aX+c w)dt+sigma XdW, z=dX,
gamma_star=2cd/q0,
```

the ACTUAL storage P0=2d²/q0 gives

```text
L(P0X²)+d²X²
 =-d²(X-2cw/q0)²+gamma_star²w².
```

Stopped Itô/nonnegative Fatou give RMS OUTPUT gain<=gamma_star on ALL progressive expected-L2 inputs, with no fourth moment. The scalar linear plant is strongly stopped-input consistent. Therefore the ENTIRE new upper theorem applies directly and gives

```text
G1<=sqrt2*gamma_star.                                 (RISK-UP)
```

No v21 lower proof is a premise of this upper. Its separate COMPLETE284LF source, SHA256 `918e883ec3e68fd7876c2cb198a4d177b581675eeb05308dc7158f459c5a615e`, supplies exact G2=gamma_star and the direct literal LOWER G1>=gamma_star by explicit canonical probes/common buffers. Combining that named still-unreviewed whole result with RISK-UP would narrow its prospectively supported interval to `[gamma_star,sqrt2*gamma_star]`. Exact original G1 remains OPEN. No probability-class sharpness assertion makes the upper factor attainable by this plant, and no h>0 extension is inferred.

The mean-output relaxation still has value dc/a<gamma_star. Thus the new source closure improves the upper constant but does not remove the stochastic-risk barrier identified by v21 or solve arbitrary-data literal synthesis.

## 8. Exact assurance/source boundary and original remaining work

Delivered: the COMPLETE needed continuous monotone domination proof, direct exact primary-source reading evidence, ALL stopping-time/predictability/continuity/zero/input/horizon hypotheses matched to the original law, finite and infinite counted-horizon upper transfer, and exact nonpromoted application/composition cuts. The lower proof and general full-book synthesis are not smuggled into an upper statement.

The probability result/constant has clear PRIOR attribution to Geiss–Scheutzow/Lenglart/Pratelli. General source sharpness, discrete/càdlàg/conditional variants and every transitive reference are not newly certified merely because the whole reader body was read. No authenticated publication-byte identity, numerical probability example, norm optimum, finite-step algorithm, physical-controller sharpness, novelty/SOTA/worldwide priority/publication or stronger formal/kernel/human/configured-family/executable/triple-finite gate is claimed.

The original arbitrary-plant prescribed-gamma literal synthesis/actual printed realization, unmatched stochastic state/control tradeoffs, general causal/actual-range realization, nonlinear/stronger-admissible replacement and finite-horizon optimality remain OPEN. The upper factor does not choose a controller or make a stronger expected-control RMS theorem applicable to the frozen pathwise-control class without a separate match.

All FOUR own findings remain distinct/permanent: private written-exactness ZERO credit; post-v100 ACTUALRETURN/pre-primaryACK order; actual post-v107-body/pre-ACTUALRETURN primary/review interleaving with old blanket pause assurance withdrawn; and unsupported historical receipt counts with nonexistent extra coverage withdrawn. Four old unadmitted Eval records and every withdrawn scout are not replayed/back-converted or credited. The newly read v16 parent supports ONLY its three full exact scopes; v17–v21 remain separate candidates unless individually adopted, not upgraded by v16.

Every parent/author/reviewer v9–v39/later source/root/freeze/read/clock/cadence/admission/withdrawal qualification, N4UNKNOWN/historical-exit-unestablished, auxiliary214 UNADMITTED/STOP and HOLD remains. Conventional proofs/tool chronology are not hidden model reasoning or an exhaustive clean cognition/runtime census. No source/shared/parent/frozen edit, Git/deletion/config/publication action, paid/external-model call or scientific launch occurred; only read-only primary retrieval/metadata and written mathematics.

All older sources/reviews/ACKs/checkpoint/park/addendum chains remain immutable. Same ORIGINAL stochastic-preview target/eighteen owners, science cutoff2026-10-27T11:05:38-07:00 and delivery deadline2026-10-27T12:35:38-07:00; substantive actual-clock checkpoints remain at most30minutes. This complete source/proof increment is NOT an early finalpark or96-hour closeout. Fresh complete mathematical AND dependency/application review is required before promotion.
