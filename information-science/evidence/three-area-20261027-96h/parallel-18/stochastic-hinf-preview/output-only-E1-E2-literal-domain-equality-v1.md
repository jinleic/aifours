# Actual output-gain E1/E2 equality without an NR-GAIN finiteness import

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 17:18:32 PDT 2026**. Non-construction literal-domain work. This proof is independent of the pending first-moment/NR-GAIN lemma. It does NOT replace or silently narrow the stronger state/control-E1 assertions of the earlier domain candidate; those remain separately pending at their named imports.

## 1. Complete original-object class and comparison domains

Use arbitrary compatible real matrices in the original system

`dx=[Ax+Bu+Cw(t-h)]dt+[A0x+B0u]dW`, `z=D0x+D1u`,

with positive dimensions, finite h>=0, zero initial state/history, the canonical Brownian filtration, and ONE deterministic stationary linear law

`u=Kx+L0w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`,

where all matrix gains are finite and H is a deterministic L2 kernel. At h=0 combine taps and omit H. No additional Brownian history, private randomness or controller memory is allowed.

Either take finite output interval I=[0,T], T>h, and input interval J=[0,T-h], with w set to zero outside J INCLUDING (T-h,T]; or take I=J=[0,infinity), with zero negative-time history. A statement below applies separately to either horizon, not via an unproved passage between different controllers.

Define progressive input classes

`E2(J)={w:E integral_J |w|^2<infinity}`,

`E1(J)={w:E sqrt(integral_J |w|^2)<infinity}`.

For both classes admit only finite positive literal denominator E||w||. Actual control admissibility in this comparison is progressively measurable LOCAL pathwise L2 with no finite-time explosion. No expected global control-L2, internal EMS, output norm finiteness or source-book-domain equivalence is silently assumed.

Let G2dom and G1dom denote the suprema of the SAME ORIGINAL literal ratios `E||z||_I/E||w||_J` on these TWO disturbance domains, allowing numerator/gain infinity. The subscripts denote DOMAINS, not RMS gains.

**Theorem.** Every E1 input has a unique actual nonexplosive local strong solution with the stated fixed law, and

**G1dom = G2dom in [0,infinity].**                            (D)

If this common value is finite, every E1 output has finite expected pathwise L2 norm and is the L1(L2) limit of its actual E2 approximations. State/control expected pathwise energies are NOT asserted. This is a genuine physical caller, not an abstract completion with an unidentified output.

## 2. Actual local physical solution for every E1 input

The causal window operator R has pathwise L2 norm at most `r=||L0||+||Lh||+sqrt(h)||H||_L2` on zero-extended inputs and preserves progressiveness. Agreement of two inputs up to a stopping time gives agreement of all their forcing/window terms there. For E2 inputs the permitted finite-horizon linear-SDE theorem supplies unique strong E2 state/control/output on each compact interval; fixed coefficients and bounded R ensure all its hypotheses.

For a given E1 input, its total path energy is finite almost surely. Define the causal energy stopping times

`tau_N=inf{t in I:integral_0^t |w_s|^2ds>=N}`,

capped at T in the finite case and with inf(empty)=infinity in the infinite case. Let `w^N=w 1_(t<tau_N)` on J and zero elsewhere. Its total squared energy is at most N, hence it is an ACTUAL E2 input on the whole input domain. The sequence is symbolic for every N, not an executed enumeration or selected-energy test.

The inputs w^M,w^N agree through tau_N for M>=N. The original preview law is causal, so their actual states and controls agree through that stop by localized strong linear-SDE uniqueness. Intersect the countably many full-probability consistency events. The consistent states patch to one actual solution X and its original control/output.

On each finite-energy path, N eventually exceeds the TOTAL input energy, so tau_N is the full endpoint T or infinity. Consequently the patched path agrees with an actual E2 solution on every required compact interval and has no finite-time explosion; its control is pathwise L2 on compacts. Any other local strong solution agrees up to each tau_N and hence everywhere. This proves actual existence/uniqueness without any expected-norm operator bound or stochastic-flow/realization theorem.

## 3. Input approximation and a finite-gain branch, not an assumed theorem

Pathwise `||w-w^N||<=||w||`, with eventual equality w^N=w on the entire time domain for every finite-energy path. Dominated convergence gives

`E||w-w^N||_J ->0`.

Now split the proof by the ACTUAL value G2dom, rather than invoking an external result that it is finite.

If G2dom=infinity, E2 is a subset of E1 with the same actual caller by uniqueness, so G1dom>=infinity and (D) follows immediately. Nothing about E1 output integrability is asserted in this branch.

Suppose instead g=G2dom<infinity. By the definition of that finite gain, EVERY E2 input has `E||Z(v)||<=g E||v||`; the zero input also has zero output by linearity/zero state/history. For M,N the difference input w^M-w^N is globally E2. Strong linearity of the SAME original SDE gives the actual output identity, on every compact and therefore the whole domain,

`Z(w^M)-Z(w^N)=Z(w^M-w^N)`.

Thus

`E||Z(w^M)-Z(w^N)||_I <= g E||w^M-w^N||_J ->0`.

The E2 output sequence is Cauchy in the standard Banach space L1(Omega;L2(I)), which is complete for both horizons. Its limit is the ACTUAL patched output: on almost every path the inputs eventually have no energy stop and the stopped-uniqueness identity identifies the whole actual output, not a product-a.e. version at a coupled random input. Therefore

`E||Z(w^N)-Z(w)||_I ->0`, `E||Z(w)||_I<=g E||w||_J`.

No global expected state/control bound has been inserted to make this identification. Hidden/unobservable internal states may have infinite global expected energy; the theorem is deliberately output-only.

## 4. Exact gain equality, all strictness and eligibility limits

The inclusion E2 subset E1 gives G1dom>=G2dom. In the finite-gain branch, every E1 nonzero denominator is approached by the E2 denominators and outputs above; those denominators are positive for all sufficiently large N. Actual ratios converge and are bounded by g, proving G1dom<=g. This proves (D), including g=0 and the infinite case, without NR-GAIN.

Uniform-strict feasibility `G<gamma` and nonstrict gain bound `G<=gamma` therefore transfer exactly between these domains for the same law, and under an unchanged existential quantifier over these locally admissible bound laws. This is not an RMS statement.

Endpoint-only pointwise strictness requires care: E2 ratios may all be strictly below gamma while their supremum is gamma. The limiting proof gives a nonstrict E1 inequality only. No generic E2-pointwise-strict -> E1-pointwise-strict theorem or physical counterexample to it is claimed. A common margin pays the transfer; actual endpoint attainment must otherwise be decided separately.

If a proposed original admissibility rule requires expected global control-L2 for EVERY E1 input, or additional stability/memory requirements, that is a separate law/domain premise. The theorem does not infer it from output gain, and it is not established merely by an original source transcription. Nonlinear full-information F, nonzero homogeneous initial output, infinite preview or nonfinite input expected norm are not silently included.

## 5. Relationship to existing candidates and exact residual

The earlier `linear-preview-E1-E2-physical-domain-bridge-v1.md`, SHA `8ec3fd87aa936435745526ffd912c617ba361afc3d744c6348e3ed7e3a9be731`, asserts stronger finite-horizon state/control-E1 bounds using the current first-moment theorem. Those stronger assertions and their NR-GAIN dependency remain unchanged/pending. The present result independently pays only ACTUAL local well-posedness and extended output-gain equality on BOTH horizons; it neither upgrades the earlier whole file nor reduces its frozen scope.

This closes a concrete output-domain caller relevant to the literal expectation-of-path-norm formulation within the stated linear class. It does not solve general prescribed-gamma synthesis, prove that every finite/infinite gain is finite, establish book admissibility, or authorize a stopped construction route.

Only allowed finite-prefix linear-SDE existence/uniqueness/linearity, the explicitly causal bounded window operator, energy localization, dominated convergence and standard L1(L2) completeness are used. No first-moment BDG/NR-GAIN import, storage/Gramian/adjoint/old realization guide, parent physics-2 L1 material, new source, scientific interpreter/CAS/enumeration, selected diagnostic/model CLI or nested agent was used. All prior process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP and source-render/copyright controls persist; written only, no peer/parent/formal/kernel/executable/human/configured-family/novelty acceptance.
