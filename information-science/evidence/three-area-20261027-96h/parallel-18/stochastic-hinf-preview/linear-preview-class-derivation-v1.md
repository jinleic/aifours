# A physical symbolic family with G_prog strictly larger than G_det

**WRITTEN AUTHOR CANDIDATE — UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:03:46 PDT 2026**. This refutes the released fixed-law equality, not existential synthesis, and does not evaluate either gain exactly. No scientific interpreter, calculator, selected numerical/control probe, external source or model CLI was used.

## 1. Release, exposure timing and exact question

The entire 19-LF `info-3-linear-preview-class-controls-v1.md`, entire release JSON and entire 37-LF packet were read, followed by the packet's complete equality receipt. Packet SHA-256: `cbf78426d65a0c373cbc11d31d7eda200478025e5beafa4c970ffc86aa358ed7`. Its supplied definition fixes the actual plant

`dx=[Ax+Bu+Cw(t-h)]dt+[A0x+B0u]dW`, `z=D0x+D1u`,

zero state/history, finite T>h>=0, zero-extended input, canonical progressive E2 disturbances, and deterministic stationary laws

`u=Kx+L0 w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`.

The question is whether, for EVERY such fixed actual law and plant,

`G_prog = sup_progressive_E2 E||z||_[0,T] / E||w||_[0,T-h]`

always equals

`G_det = sup_deterministic_L2 E||z_v||_[0,T] / ||v||_[0,T-h]`.

Only nonzero denominators are admitted. All norms here are the literal pathwise L2 norm, followed by expectation; no RMS substitution is made.

**Timing PROCESS MINOR retained:** `linear-preview-class-prebody-ack-and-timing-finding-v1.json`, SHA `82d89cc8a86ed2d598b8c35465cfdf2fcc4234f4d8d8853716ab335139f8af63`, honestly records that internal symbolic reasoning began after reading the admitted controls/release but before writing the required ACK. The ACK was written before opening the definition-bearing packet, not before all internal derivation. Main explicitly dispositioned this as a PROCESS MINOR, not a quarantine, because only admitted inputs were used, and authorized prospective development and this noncolliding filename. Nothing is backdated or described as a clean restart; the prior preliminary hold is not represented as a standing scientific quarantine after that disposition. The old pinned `prerequisite-derivation-v1.md` is untouched.

All prior authorship/exposure and STOP/HOLD/ZERO findings persist; no cognitive-independence/provenance certificate is claimed. No old proof, candidate, held guide, v248-reported material, realization/storage argument or changed output is an input.

## 2. A derived Brownian stopping constant — no exit-time formula imported

Let a>0 be arbitrary and define `tau_a=inf{t>=0: |W_t|=a}` for the same canonical Brownian motion used by the physical plant. Continuity makes this a stopping time and gives tau_a>0 almost surely.

We use the Itô isometry in its exact form `E|integral_0^t g_s dW_s|^2=E integral_0^t |g_s|^2 ds` for progressive square-integrable g. Its stopped-indicator consequence is

`integral_0^t 1_(s<tau_a) dW_s = W_(t min tau_a)`.

For completeness, this identity follows directly from the integral's simple-predictable construction: approximate the stopping time from above by mesh stopping times. The corresponding integral is the finite sum of Brownian increments up to that mesh stop; the squared integrand error on [0,t] is bounded by the mesh length. Itô isometry gives convergence in L2 and Brownian continuity identifies the limit as the stopped path. No optional-stopping theorem, hitting-time density, reflection principle, scaling formula or numerical value is imported.

Because `|W_(t min tau_a)|<=a`, isometry gives

`E(t min tau_a)=E|W_(t min tau_a)|^2<=a^2`.

Monotone convergence implies E tau_a<=a^2, hence tau_a is finite almost surely. Continuity then gives `|W_tau_a|=a`; bounded convergence in the preceding equality yields **E tau_a=a^2**.

The stopping time is not constant: a positive deterministic value s would force `|W_s|=a` almost surely, contrary to the nonatomic Gaussian marginal in the definition of Brownian motion. Equality in Cauchy-Schwarz would make sqrt(tau_a) constant, so

`m_a:=E sqrt(tau_a)` and `rho_a:=m_a/a` satisfy **0<rho_a<1**.

These are exact, unevaluated distributional constants, not decimal approximations or chosen test values. Also Markov's elementary inequality gives `P(tau_a>S)<=a^2/S` for every S>0. Those are all exit-time properties used below.

## 3. Entire symbolic physical family and admissibility

Choose arbitrary real nonzero b,d,ell, arbitrary a>0 and h>=0. Put rho=rho_a. Choose a finite T satisfying

`T > max{ h+2a^2/(1-rho), 4rho^2 a^2/(1-rho)^2 }`.

Set `S=T-h` and

`eta := 1-rho-a^2/S-rho a/sqrt(T)`.

The two strict T inequalities give eta>0 and S>0. Finally choose ANY nonzero real c satisfying

`0<|c|< |b ell| eta / (2rho sqrt(T))`.                         (F)

This defines a nonempty symbolic family for every a>0, every finite h>=0 and all nonzero b,d,ell. No member is selected or evaluated. Its two strict bounds are analytic hypotheses; the positive intervals are nonempty because rho is strictly between zero and one.

Use scalar dimensions n=m=p=q=1 and the actual source matrices

`A=B=A0=0`, `C=c`, `B0=b`, `D0=d`, `D1=0`,

with fixed law

`K=Lh=0`, `H=0`, `L0=ell`, hence **u(t)=ell w(t)**.

For h=0 this is the permitted combined current tap. For h>0 the current tap lies in the permitted preview window. The law uses no extra Brownian information, stopping rule, private randomization or state memory. It is the SAME law for every disturbance. Both the physical drift disturbance channel c and control-noise channel b are nonzero; the original output is exactly z=d x.

For EVERY progressive E2 input on [0,S], zero-extended elsewhere, its unique actual strong solution is

`x_t = c R_h w(t) + b ell M_w(t)`,

`R_h w(t):=integral_0^t w(s-h)ds`, `M_w(t):=integral_0^t w(s)dW_s`.    (1)

This is direct integration of the original equation, not evaluation of a deterministic-input version along a random graph. The drift is a pathwise time integral and the martingale is the ordinary Itô integral of the actual progressive input. The fixed law makes uniqueness immediate by subtraction. Both paths are continuous and finite on the compact horizon almost surely, giving nonexplosion. Moreover `E integral_0^T |u|^2=ell^2 E||w||^2<infinity`, stronger than local pathwise control-L2.

The elementary pathwise integration bound and isometry/Tonelli give

`||R_h w||_[0,T] <= T ||w||_[0,S]`,

`E||M_w||_[0,T]^2 = integral_0^S (T-s) E|w_s|^2 ds <= T E||w||_[0,S]^2`.    (2)

The first bound follows from Cauchy-Schwarz inside each time integral and then integration over t. Thus all actual E2 inputs have square-integrable output on this finite horizon, and both literal expectations exist. No extra admissibility restriction is imposed on unknown disturbances.

## 4. Upper bound for ALL deterministic disturbances

Let kappa=|d b ell|>0. For every deterministic v in L2([0,S]), expectation of the output norm is bounded by the triangle inequality, (2), and Cauchy-Schwarz on the probability space:

`E||z_v|| <= |dc| T ||v|| + kappa sqrt(T) ||v||`.

Consequently

**G_det <= U := kappa sqrt(T)+|dc|T < infinity.**                 (3)

The square-moment isometry is used only as an upper estimate on the literal deterministic-input ratio. It neither defines the performance criterion nor claims equality with an RMS gain.

## 5. An admissible adapted family exceeding that entire bound

For every amplitude q>0 define the actual disturbance

`w_(a,q)(t)=q 1_(0<=t<S) 1_(t<tau_a)`, zero outside [0,S].          (4)

This whole symbolic family is progressively measurable in the original Brownian filtration. Its stopping time is chosen by the disturbance, not by the controller. Its expected squared energy is `q^2 E(tau_a min S)<=q^2 a^2`, and its literal expected norm is

`E||w_(a,q)|| = q m_(a,S)`, `m_(a,S):=E sqrt(tau_a min S)`,

with `0<m_(a,S)<=m_a<infinity`. Thus every member is a legal nonzero E2 disturbance. The amplitude q cancels from each ratio; no special control or numerical sample is selected.

By the stopped-integral identity, its actual martingale part is `M_w(t)=q W_(t min tau_a min S)`. On {tau_a<=S}, the absolute Brownian state after tau_a is a, so

`||M_w||_[0,T] >= q a sqrt(T-tau_a) 1_(tau_a<=S)`.

For every nonnegative r, `sqrt(T)<=sqrt(r)+sqrt((T-r)_+)`. Hence

`E sqrt((T-tau_a)_+) >= sqrt(T)-m_a`.

Removing {tau_a>S} loses at most `sqrt(T)P(tau_a>S)<=sqrt(T)a^2/S`. Therefore

`E||M_w|| >= q a [sqrt(T)-m_a-sqrt(T)a^2/S]`.

The bracket is positive under eta>0. Divide by `q m_(a,S)<=q m_a`, then use m_a=rho a, to obtain

`E||M_w|| / E||w|| >= sqrt(T) [1+eta/rho]`.                      (5)

The actual drift term cannot erase more than its pathwise integration bound: by the reverse triangle inequality and (2),

`E||z|| / E||w|| >= kappa sqrt(T)[1+eta/rho] - |dc|T =: L`.        (6)

Condition (F) makes

`L-U = kappa sqrt(T) eta/rho - 2|dc|T > 0`.

Combining (3)–(6) proves the strict physical inequality

**G_prog >= the actual ratio for w_(a,q) >= L > U >= G_det.**     (7)

The exhibited adapted ratio itself is finite by (2) and the proven nonzero denominator. No value or finiteness of the supremum G_prog is needed or claimed. This is a finite-horizon, same-law, original-output counterfamily, not graph singularity, an abstract fake response or an RMS gap.

## 6. What is refuted, all parameter boundaries and what remains

The universal assertion G_prog=G_det for every bound linear preview law/plant is **FALSE at this stated interpretation**, for h=0 and for every finite positive h (choose any family member satisfying the displayed analytic inequalities). All actual law/input/state/output callers and deterministic-input upper quantifiers are supplied above.

There is an explicit uniform-strict feasibility gap for the fixed law: any gamma with `U<gamma<L` passes the deterministic-input bound but fails the original progressive literal criterion by (7). Such an interval exists by (F). This does NOT say no different law could achieve that gamma. In this family, changing the law changes the problem being tested; no optimality or existential impossibility over laws is proved.

Required nondegeneracies a>0, S>0, b*d*ell!=0 and eta>0 are explicit. If d=0 the original output is zero and both gains are zero, outside the strict-gap family. If b*ell=0 the derived noise gap vanishes and (F) has no nonzero c solution; no strict gap is claimed there. At c=0 the same noise construction already gives a gap, but the theorem deliberately retains nonzero c to keep the physical delayed disturbance channel. At T=h the nonzero input denominator is unavailable, excluded in the released definitions. No equality-boundary eta=0, gamma endpoint, infinite horizon, nonlinear law or alternative controller information convention is asserted covered.

Named imports and exact use: ordinary linear-SDE strong existence/uniqueness and linearity are realized explicitly by (1); Itô isometry plus its simple-predictable construction gives the stopped-input identity and second moments; Tonelli gives (2); monotone/bounded convergence gives E tau_a=a^2; elementary Cauchy-Schwarz (including its equality case), Markov, triangle inequalities and Brownian continuity/nonatomic Gaussian marginals give the remaining bounds. No optional stopping, Brownian scaling, reflection formula, BDG constant, stochastic-flow/Gramian/storage or unadmitted source is used.

**NR-SOURCE** persists: supplied dossier/class definitions are not a fresh certification of book-image equivalence. **NR-SYNTHESIS** persists: a fixed-law failure of deterministic-input testing is not a general N&S criterion or a refutation of existential synthesis. No old cuts, UNREVIEWED candidates or process finding are upgraded. This candidate is written only, not peer/parent adopted, machine/formal/human/configured-family checked or novelty cleared.

## 7. Continued admitted step

Next derive a quantitative finite-horizon E2 input/output continuity estimate for the bound linear preview class and test whether the strict fixed-law gap survives a nontrivial open neighborhood of the entire matrix/law tuple. The original literal norms will remain the criterion: the E2 estimate is only a perturbation tool, with the fixed adapted caller's finite E2-to-expected-norm ratio carried explicitly. No controller synthesis or new source is self-released.
