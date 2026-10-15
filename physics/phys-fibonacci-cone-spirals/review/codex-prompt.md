# Independent hostile-referee review

Today is 2026-10-14. Review a scoped mathematical research deliverable, not a claimed solution of the full physical problem.

## Permission boundary

You may read only `/Users/jinleic/jinleic-workspace/ai4s/phys-fibonacci-cone-spirals/` and its descendants. Do not read parent/workspace policy files, credentials, unrelated projects, or user data. Do not delegate. Do not edit or write files. Do not run reproduction commands that write output files. You may run `python3 code/verify.py` if useful, or read code and derive independently. All substantive findings must be returned in your final answer; the caller handles the CLI's final-output file. No network is needed; literature scope/reading levels are declared in STATUS.md, and priority is explicitly not claimed.

## Objective and context

The book asks whether stressed Fibonacci parastichy patterns minimize elastic energy on a cone (C1) and whether changing equal-disk size toward the cone apex alternates chirality (C2). The experimental elastic functional and growth rules are unspecified. This deliverable is explicitly PARTIAL overall, with a COUNTEREXAMPLE only to a particular fixed-golden-angle packing ansatz. It must not be marketed as a refutation of all Fibonacci-contact configurations or a solution to the experiment.

Read README.md, RESULTS.md, STATUS.md, code/verify.py, code/generate_witness.py, code/diagnostics.py, and the small results JSON files. Treat RESULTS.md as the mathematical claim authority. Check every quantifier, finite/infinite transition, geometric metric, disk embedding and boundary issue, ratio/constant, and exact-versus-numerical distinction.

## Claims to attempt to falsify

F. On the intrinsic cone R^2/C6 (developed sector angle pi/3), 183 centers constrained to slant radii 10..20 admit a triangular-lattice quotient with minimum separation exactly 1. The comparison spiral has squared radii 100+150*i/91 and azimuth 2*pi*i*(3-sqrt(5))/2, i=0..182. Its pair (4,12) has squared separation <77/100, certified by rational sqrt lower bounds and cos(x)>=1-x^2/2 with pi<22/7. Disk diameter 1 fits the competitor in frustum 9.5..20.5. This is a strict comparison, not the unrestricted finite optimum.

B1. On a cone of sector angle 2*pi*beta, any equal embedded intrinsic disks centered at every point of the golden Fermat spiral r_n=c*sqrt(n), theta_n=2*pi*n*gamma after any finite prefix deletion have asymptotic density <=pi/(2*sqrt(5)). The proof chooses q_k=F_k, residual epsilon_k=phi^-k, n_k nearest q_k/(2*A*epsilon_k) where A=2*pi*beta, and obtains limiting squared separation c^2*A/sqrt(5).

B2. On the pi/3 quotient cone the maximum asymptotic density is pi/(2*sqrt(3)), by quotient triangular lattice plus planar lifting and Thue's theorem. Thus the fixed ansatz has strict bulk loss; neither general Fibonacci-contact topology nor elasticity is settled.

S. Achiral domain/boundaries/reflection-invariant energy imply mirror-degenerate minima at each diameter. This does not rule out history-dependent alternation.

T. In the explicitly reduced candidate-family model L_k(t)=F_k^2/(4*t)+A^2*t*phi^(-2*k), k>=2, the two shortest Fibonacci families pass successively through (F_k,F_(k+1)); adjacent crossings tau_k strictly increase, and pair transitions sigma_k lie between tau_(k-1) and tau_k. The residual F_k*gamma-F_(k-2)=(-1)^k*phi^-k gives alternating sign of the larger-count family. This is a defined local model, not a theorem for arbitrary sequential growth or all integer offsets.

## Required review output

Give a verdict: correct / correct-with-fixes / incorrect / insufficient-information. List numbered findings, severity, exact affected claim/file/section, a counterexample or derivation where possible, and the smallest correction. In particular distinguish a mathematical error from an unclaimed physical generalization or unclaimed novelty. Audit code witness reconstruction independently of the generator. Check that the finite controls cannot masquerade as universal proofs. Point out any citation assertion not supported by its declared reading level, without pretending you checked inaccessible sources. Also state which central claims survive your review and any remaining proof gap. Do not produce generic advice or ask for more work without naming the exact obligation.
