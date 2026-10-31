# A real strong output limit is not automatically a controller in the bound class

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:42:31 PDT 2026**. Continued admitted class-closure obstruction, not controller realization or the stopped diffusion-annihilating branch. No new source, selected diagnostic or execution.

## 1. Exact physical family and statement

Use the ENTIRE symbolic family of `literal-feasibility-does-not-bound-kernel-L2-v1.md`, SHA `32bc2c874ef770ac67a0c3aff99e3b476c5adda445905813745eb2252192c917` (UNREVIEWED): fixed h>0, 0<r0<h, alpha>0, real J and D1 with D1J!=0, original B=C=B0=0, arbitrary A,A0,D0, zero initial state/history, zero fixed feedback/taps, and kernels

`H_epsilon(r)=(alpha/epsilon)J 1_[r0,r0+epsilon](r)`, `0<epsilon<h-r0`.

The actual state is zero. Actual control/output maps are `u_epsilon=H_epsilon*w`, `z_epsilon=D1u_epsilon`. On each finite source horizon T>h and on the explicitly eligible infinite family, inputs are canonical progressive E2 with the original literal norms and zero extension. No new physical output or class is introduced.

Let the comparison maps be

`u_lim(t)=alpha J w(t-r0)`, `z_lim(t)=alpha D1J w(t-r0)`.

They are benchmark maps for an admissible-class CLOSEDNESS QUESTION, not newly authorized controller designs or synthesis witnesses.

**Theorem.**

1. For EVERY fixed actual progressive E2 input, controls and original outputs converge in E2 to these benchmark maps as epsilon decreases to zero. Hence every fixed nonzero input's literal ratio converges too.
2. On every fixed finite source horizon, the uniform deterministic/output-operator error remains at least `alpha||D1J||>0`; the same lower obstruction holds for the uniform expected-path-norm error. Thus this is NOT uniform operator convergence.
3. No bound two-endpoint/L2-kernel controller of this same physical plant has exactly the limit output map for every input. The image of the bound controller class is therefore neither strongly nor weakly operator closed, despite a common strict literal performance bound along the whole family.

The gain bound can even remain constant on the infinite horizon and converge correctly on each finite horizon while the actual limit fails the class-membership caller. This is the missing closure premise, not a synthesis impossibility.

## 2. Actual fixed-input convergence, not a guessed singular controller

Zero-extend w to the full real time line. Direct substitution gives

`u_epsilon(t)=(alpha/epsilon)J integral_0^epsilon w(t-r0-s)ds`.

Thus Minkowski yields

`||u_epsilon-u_lim||_L2 <= alpha||J|| (1/epsilon) integral_0^epsilon ||w(.-s)-w||_L2 ds`.

Translations are strongly continuous in L2: prove first on continuous compactly supported functions by ordinary uniform continuity and then use their L2 density plus the translation isometry. The right side tends to zero. Restriction to the finite or one-sided infinite output interval cannot increase it.

For a progressive E2 random input the same argument is in L2(Omega x time): finite sums of product functions are dense, and the time translations are strongly continuous there by the same isometry/density proof. Therefore it is convergence of the ACTUAL controls at their common actual input, not conditional-on-input noise arguments or separate solution versions. Multiplication by D1 gives original-output E2 convergence. Cauchy-Schwarz then gives `E||z_epsilon-z_lim||->0`, proving the claimed convergence of each literal ratio with fixed positive denominator.

The limiting maps are causal interior taps; their information is within the abstract window. That alone is not proof they belong to the narrower two-endpoint/L2-kernel parameterization or that the book's unspecified admissibility accepts a chosen extension.

## 3. Uniform operator error cannot disappear

For any fixed finite T>h, the exact earlier obstruction `two-endpoint-kernel-class-interior-tap-obstruction-v1.md`, SHA `4181508388f1d87614db22302ae48ead68f9d5056bb10373e8cf9dfe1ecd0851` (UNREVIEWED), proves that the distance from a nonzero matrix interior tap to ALL endpoint/regular-kernel maps is exactly the matrix norm. Its load-bearing argument is simple: restrict inputs to a small interval I with I,I+r0,I+h disjoint; on I+r0 the endpoint terms vanish, the regular kernel is compact, and a translated orthonormal input sequence has constant nonzero norm. A compact term cannot cancel all those inputs.

Apply that argument to the ACTUAL output matrix alpha D1J and regular output kernel D1H_epsilon. It gives

`||z_epsilon-map - z_lim-map||_(deterministic L2 operator) >= alpha||D1J||`.

Both compared maps are deterministic linear path operators in this physical zero-state family, so their expected-path-norm operator error is at least that same deterministic lower bound (deterministic inputs are actual progressive inputs). It is an approximation-norm statement, not replacement of the regulated signal or performance task.

Consequently convergence for each fixed input is strictly weaker than uniform performance-map approximation here. The strong limit lies outside the bound class, because no endpoint/kernel output map could equal the nonzero interior tap. State feedback cannot help on this same physical plant: its actual state is identically zero for all inputs/laws.

Strong operator convergence implies weak operator convergence, so the exact same actual sequence also disproves weak operator CLOSEDNESS of the image class. No compactness theorem alone can turn that outside-class limit into an allowed parameter triple.

## 4. Gain values do not repair the caller

The earlier exact physical family has `G_infinity(epsilon)=alpha||D1J||` for every epsilon. On each finite horizon the pathwise Young bound gives gain<=alpha||D1J||. Conversely choose any real maximizing direction e of D1J and any unit scalar input shape supported inside [0,T-h]. Its benchmark delayed output has norm exactly alpha||D1J|| because r0<h keeps the full shifted input support inside [0,T]. Fixed-input convergence then makes the finite-horizon gains' lower limit at least that value. Therefore their gains converge to the benchmark gain as well.

So correct convergence of scalar gain values, even along uniformly strict-feasible physical laws, does NOT pay membership of the limiting map in the original bound subclass. This does not prove lack of SOME other bounded feasible law: u=0 remains available in this structural family. It invalidates only the claimed universal closure/selection step.

## 5. Degeneracies, exact missing premise and limits

The conditions h>0, r0 strictly interior and D1J!=0 are essential to the nonrepresentation statement. If the output matrix vanishes the obstruction is zero; if r0 is an endpoint the bound class already has that point tap. All remaining matrix ranks/signs, finite/infinite comparison inputs and the entire epsilon family are covered; no member was chosen for a diagnostic.

An admissible-limit theorem or an explicitly changed controller class would be needed before using this strong/weak limit for original synthesis. Neither is supplied or self-released. The full source F may be broader than the bound subclass, but source admissibility/regularity must still be stated rather than inferred from a limit. No conclusion about every original controller or general N&S solvability follows.

Only ordinary time-translation continuity/density/Minkowski/L2 facts and the current fully stated physical kernel family/nonrepresentation proof are used. No old realization guide, direct diffusion-annihilating construction, new source, native science/CAS/enumeration, selected probe/model CLI/nested agent or source-page method is used. The parent physics-2 L1 episode/all consumers remain HELD/ZERO/NONINPUT and unrelated duties stay unchanged. All prior process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP/source-render/copyright limitations persist; written only, no peer/parent/formal/kernel/executable/human/configured-family/novelty acceptance.
