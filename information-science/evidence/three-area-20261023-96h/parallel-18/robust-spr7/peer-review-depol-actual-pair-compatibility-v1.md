# v49-A — actual-pair depolarizing compatibility, complete written reconstruction

Actual `/bin/date` observation before creation: **Sun Oct 25 07:10:58 PDT 2026**. Reviewer InfoSPR7-2 / information science; author PhysicsDepol4 / physics. Genuinely cross-domain, same-harness, supplied-proof review. No scientific eval/interpreter/program/symbolic computation/enumeration/sampling/replay, solver, CLI or nested agent was used. Metadata clocks/hashes and source reads only; HOLD/v7/v8 remain binding.

## 1. Inputs, exposure and complete coverage

Parent erratum v8 was read FIRST. The exact v49-A entry and common rules in `peer-review-wave-eighteen-v49-v50.json` and its packet receipt were read; the long scope line was explicitly recovered with `:raw`. Exposure ACK `peer-review-depol-actual-pair-compatibility-ack-v1.json` was written BEFORE the proof body.

Literal packet `peer-review-wave-v49-a-depol-actual-pair-compatibility-sources-v1.md`, freshly observed SHA256 **`db19a41781c7d6af79bae03e6c886b833e25c763dff6ed765093a3afc18dc068`**, was read completely, packet LF1–339, containing every original source **LF1–332**. No source line remained truncated. The packet receipt reports complete literal roundtrip equality; I did not independently regenerate it.

Source `physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/depolarizing-actual-pair-compatibility-consolidated-v2.md`, freshly observed SHA256 **`06ce3ebb7cc4287708bf191d6245a0db7c8205422c03a80b4f05e073416c4861`**, matches the frozen pin. All references below are ORIGINAL source LF.

Exposure: I knew only the round's depolarizing ledger scope and the author's prior review of my SPR manuscript. I had not read this compatibility body or received a correctness verdict. Parent supplied the required interfaces, not a conclusion. Neither old computational output nor a claimed certificate boolean is used as a premise.

## 2. Verdict and exact accepted written scope

**0 FATAL / 0 MAJOR / 0 MINOR at the reconstructed actual-pair compatibility scope.** The following reconstruct in writing for every actual mixed or pure four-qubit density rho and every complex rank-k orthogonal projector Pi, k=2,3,4:

- the normalized Choi/swap-sector energy identity `b-3d=8 Tr[P2(rho^T tensor Pi)^Gamma]>=0`;
- exact tight-face equivalence `a=0 iff b=0`, with either equality forcing `a=b=c=d=0`, including all zero/tied marginal spectra and arbitrary complex maximizing projector subspaces;
- the stated quantitative pure-state energy and product-overlap consequences;
- the SAME-PAIR relation `c=a-b-d-s`, and the reduction of the remaining actual c>0 obligation to the strict region `a>b>0`, `b>=3d`, `s>=0`.

The exact scalar quartic/noise equivalence at LF29–39 is an explicitly supplied previously supported IMPORT, not re-proved here. This review supplies its new physical sign/endpoint/face interface; it does not accept its historical executable proof or promote prior unadmitted computations. The original Zhang ancestry/uncertain novelty boundary is binding.

No full quartic inequality, complete low-noise index, all-p comparison or actual counterexample is proved by the source or this review. Those are NOT_RECONSTRUCTED, not silently treated as passed.

## 3. Independent derivation of P2, positivity and the exact trace identity

**Source LF45–95 reconstructed.** Use the source convention `J_L=sum_xy |x><y| tensor L(|x><y|)` and transpose ONLY the output copy B. For the trace-and-insert-identity map, the Choi matrix is the full identity. For the map retaining two sites and inserting unnormalized identities at the rest, its Choi matrix is the product of the two unnormalized maximally entangled projectors and identities elsewhere. Partial output transpose converts each such projector to the corresponding swap F_i. The identity map's Choi matrix is the four-projector tensor product and converts to F1F2F3F4. Therefore for `A(rho)=3Tr(rho)I-X2(rho)+3rho`,

`J_A^Gamma=3I-sum_(i<j) F_iF_j+3F1F2F3F4`.

There is no dimension factor hidden here: `(|00>+|11>)(<00|+<11|)` is UNNORMALIZED and its partial transpose is exactly F, not F/2.

Each F_i is a commuting Hermitian involution. Thus `(I±F_i)/2` are orthogonal site-sector projectors; products for distinct sign patterns are orthogonal projections whose sum is identity. Their sum over exactly two negative signs is consequently the ACTUAL orthogonal projector P2 in LF65–67.

On a sign pattern with m negatives, `sum f_i=4-2m` and `sum_(i<j) f_i f_j=((4-2m)^2-4)/2`. Substituting m=0,1,2,3,4 into the displayed Choi polynomial gives respectively 0,0,8,0,0. Hence `J_A^Gamma=8P2` exactly. This is a written five-case eigenvalue derivation, not an imported numerical spectrum.

For the ACTUAL product `omega=rho^T tensor Pi`, partial output transpose gives `omega^Gamma=rho^T tensor Pi^T>=0`. This positivity uses the product origin: a generic bipartite positive omega need not have positive partial transpose. The Choi trace identity gives

`Tr(Pi A(rho))=Tr[(rho^T tensor Pi)J_A]`.

Partial transpose is self-adjoint under the trace pairing, so this equals `Tr[omega^Gamma J_A^Gamma]=8Tr[omega^Gamma P2]`. The last trace is nonnegative because it is the trace of `(omega^Gamma)^(1/2) P2 (omega^Gamma)^(1/2)>=0`; no commutation between the two operators is assumed.

Finally `3k-Tr(Pi X2)+3r=b-3(1-r)=b-3d`. Thus ENERGY has exactly the source normalization/signs. Rank-one choices of Pi show A(rho)>=0 for every actual input. Since X2 is positive, also `A<=3I+3rho<=6I`. The consequence `X2<=3I+3rho` gives `Tr(Pi X2)<=3k+3Tr(Pi rho)<=3k+3` for every rank-k Pi. These are analytic derivations, not certificate replay.

## 4. Pure-state marginal/spin-flip compatibility

**Source LF99–145 reconstructed.** Expand a pure rho in the Hermitian Pauli-string basis and let A_j sum squared real Pauli coefficients of weight j. Then A0=1, A1=R and purity gives `1+R+A2+A3+A4=16`.

Summing the four one-versus-three purity equalities counts a weight-one string three times and a weight-two string twice in the three-qubit marginals, giving

`(4+3R+2A2+A3)/8=(4+R)/2`.

Thus `A3=12+R-2A2` and `A4=3-2R+A2`. Spin flip reverses odd Pauli weights, so its pure overlap C is

`C=(1-R+A2-A3+A4)/16=(A2-R-2)/4`.

The six two-qubit purities sum to `(6+3R+A2)/4=2+R+C`. For pure rho, expectation of each retained marginal insertion is that marginal's purity, so `<psi|A|psi>=6-(2+R+C)=4-R-C`.

Across any selected qubit, write the Schmidt form `sqrt(mu)|0>alpha+sqrt(1-mu)|1>beta`. Single-qubit spin flip exchanges the two orthogonal factors up to phases. The full spin-flip overlap is a sum of two cross terms, each bounded in modulus by `sqrt(mu(1-mu))`, since the remaining factors have unit norm. Hence `C<=4mu(1-mu)=1-t_i^2`. Arbitrary complex Schmidt vectors are allowed; no reality assumption is used. If a Schmidt coefficient vanishes, the flipped local factor is orthogonal and C=0 directly, without division. Summing over the four qubits gives `R+4C<=4`, and therefore

`4-R-C>=(3/4)(4-R)>=0`.

These identities are used only for pure inputs. They are NOT imposed on mixed R,C data.

## 5. b=0 rigidity and the correct mixed extension

**Source LF149–178 reconstructed.** Since Pi is a projector and rho a density, d>=0. ENERGY gives b>=3d>=0. If b=0, then d=0 and `Tr(Pi A)=0`.

For pure rho, `Tr(Pi rho)=1` means `Pi psi=psi`: the norm of the orthogonal complement is exactly d, not merely small. A>=0 and trace of its Pi compression zero imply its compression is zero. Indeed `Tr(A^(1/2)Pi A^(1/2))=0` forces `A^(1/2)Pi=0`, so **Ran(Pi) is contained in ker A**, including the contained vector psi. Thus `<psi|A|psi>=0`.

The pure relations then give R+C=4 and R+4C<=4. Nonnegativity of C forces C=0 and R=4, hence every t_i=1. Repeated Schmidt decomposition makes psi a physical pure product.

After physical local unitaries take it to 0000, X2 on a basis vector of Hamming weight h has eigenvalue `choose(4-h,2)`. Thus A has eigenvalues 0 on h=0,1, 2 on h=2, and 3 on h=3,4. Its kernel is exactly the vacuum plus the four-dimensional one-excitation space. Pi contains the vacuum and has its remaining k−1 dimensions in that one-excitation space, with an arbitrary COMPLEX subspace permitted. There X1,X2,X3 act respectively as scalars 3,3,1, while their vacuum values are 4,6,4. This gives the source traces `3k+1`, `3k+3`, `k+3`, and r=1; all deficits vanish.

For mixed rho, choose a finite positive-weight pure decomposition at the SAME fixed Pi. The maps X_j are linear in rho, and a,b,c,d are affine on trace-one states. Each pure component has `b_j>=3d_j>=0`. Since `b=sum lambda_j b_j=0`, every component has b_j=0 and therefore a_j=c_j=d_j=0 by the preceding proof. Affinity then gives the four zero deficits for rho.

This averages ONLY traces and affine deficits. R,C, the quartic D and any discriminant/nonlinear function are not averaged. No quartic convexity claim is used.

## 6. a=0 rigidity, all degenerate boundaries and complex projector equality

**Source LF184–228 reconstructed.** Local unitaries diagonalize the actual one-qubit marginals, with ordered Bloch lengths t1>=t2>=t3>=t4>=0. Then `X1=2I+(1/2)sum t_i Z_i`. Its signed eigenvalues are ordered by subset sums. The four smallest subset sums, WITH multiplicity including all zeros/ties, are `0,t4,t3,min(t2,t3+t4)`. Summing the top k eigenvalues yields exactly LF194–198.

For k=3, equality with 10 forces all four t_i=1 because every coefficient in the Ky-Fan formula is positive. For k=4 the second branch is at most 12, so equality with 13 forces the first branch to equal 13 and again every t_i=1. A positive density whose marginal is rank one is supported on that pure factor: zero trace against the complementary marginal projector eliminates that block and its cross blocks by positivity. Repeating this makes rho itself a pure product even when initially mixed.

For product X1 the vacuum eigenvalue 4 is separated from the one-excitation eigenvalue 3, which is separated from the next value 2. A rank-k trace maximizer must contain the vacuum, avoid lower eigenspaces and choose an arbitrary complex k−1 plane inside the degenerate one-excitation space. This is the full variational equality geometry, not a computational-basis projector assumption. The traces from §5 above then give b=c=d=0.

For k=2, equality forces t1=t2=t3=1 but allows arbitrary t4. The same positivity/support argument gives the ACTUAL factorization `rho=tau tensor |000><000|` up to local unitaries and permutation. If tau is pure, the product case already applies. If tau has eigenvalues mu>=nu>0, its two top X1 eigenvalues are `3+mu,3+nu`; the next is `2+mu`. Their boundary gap is `1+nu-mu=2nu>0`. Thus the unique rank-two maximizing SPACE is the whole `I_qubit tensor |000><000|` range. A degeneracy within that space (including mu=nu) does not change its projector. The nu=0 boundary was correctly handled separately by the product geometry, rather than dividing by a zero gap.

Compressing X2 to this space gives 3I+3tau: three retained-pure-pair terms and three mixed/pure-pair terms. Compressing X3 gives I+3tau. Their traces are 9 and 5, and Pi contains rho's support so r=1. Therefore b=c=d=0 also for every mixed-tau boundary. Together with §5, FACE is proved for all stated actual pairs.

## 7. Quantitative statements, without nonlinear mixed extrapolation

**Source LF236–278 reconstructed.** For a pure input write p=Pi psi and q=(I−Pi)psi. Triangle inequality in the A^(1/2) norm gives

`sqrt(<psi|A|psi>)<=sqrt(<p|A|p>)+sqrt(<q|A|q>)`.

The second term is bounded by sqrt(6d). On Ran(Pi), a positive compression has maximum eigenvalue bounded by its trace b−3d; hence `<p|A|p><=(1-d)(b-3d)`. Inserting the pure energy and its lower bound proves equations (7)–(8). This includes d=1 and zero-energy cases without division.

The marginal deficit inequalities follow by subtracting the exact Ky-Fan expressions from 3k+1. At k=4, a<1 forces actual trace>12 and therefore excludes the at-most-12 alternative branch. For top marginal projectors P_i on distinct sites, `I-product P_i<=sum(I-P_i)` is an operator inequality; its expectation gives the source's commuting union bound.

For a pure input the projected vector on the top three marginal factors is a fixed three-qubit product tensor a one-qubit vector, giving the k=2 full-product overlap bound after normalization when nonzero. If it vanishes, the asserted lower bound is already nonpositive. For k=3 the weighted deficit bounds sum delta_i by 2a; for k=4 under a<1 they bound the sum by a. These give the stated overlaps. No mixed-state pure-sector relation or unreviewed near-product closure is inferred.

## 8. Same-pair reduction arithmetic and the remaining quartic

**Source LF284–310 reconstructed at the imported scalar frontier.** Single-qubit spin flip is the reduction map `X↦Tr(X)I-X`, up to its transpose/unitary realization. Tensoring it over four qubits gives

`tilde(rho)=I-X1+X2-X3+rho`.

It is positive on an actual state by the global spin-flip representation. Thus s=Tr(Pi tilde(rho))>=0, and direct trace substitution gives

`c=a-b-d-s`,

`q(1)=a+b-c+d=2b+2d+s>=0`.

This uses the SAME rho and Pi in every term. U1's spectrum gives a>=0, ENERGY gives b>=3d>=0, and r<=1 gives d>=0, so the imported scalar endpoint/deficit signs are analytically supplied.

If actual c>0, the identity forces a>b. FACE excludes b=0, and therefore a>b>0. Further `c=a-b-d-s<=a<3a+2b`. Hence all actual c>0 pairs lie in the strict a>0 interior branch of the imported scalar theorem. If a=0, FACE forces all four deficits zero and there is NO physical quadratic-interior a=0,c>0 pair. Likewise no actual b=0,c>0 pair exists.

At d=0 with b>0 and hypothetical c>0, substituting into the displayed quartic leaves `-b^2c^2-4ac^3=-c^2(b^2+4ac)<0`, exactly as the source states. This conditional observation does NOT supply such a pair. It is correctly left as an actual-state sub-obligation rather than presented as a counterexample or reduction of the complete d>=0 target.

The remaining target is therefore the quartic on ALL remaining actual pairs in the stated strict region (or a genuine actual violation with its scalar optimizer). No averaging of D, no relaxed tuple, and no low-noise index closure appears in the new argument.

## 9. Findings, ancestry and exact exclusions

| Category | Disposition |
|---|---|
| FATAL | None at the complete reconstructed actual-pair scope. |
| MAJOR | None at that scope. |
| MINOR | None at that scope. |
| Exact scalar quartic/noise equivalence LF29–39 | Explicit prior supported import, not re-proved in this review; no historical executable credit inferred. |
| Universal remaining D>=0 for actual a>b>0,c>0 pairs | **NOT_PROVED / NOT_RECONSTRUCTED**; source explicitly leaves it open. |
| Actual d=0,b>0,c>0 pair or any actual counterexample | **NOT_RECONSTRUCTED / not supplied.** The conditional discriminant calculation is not evidence of existence. |
| Full low-noise k2/k3/k4 closure or all-p comparison | **NOT_RECONSTRUCTED**; none claimed by this source. |
| Historical certificate replay / unadmitted computations | No verification credit; no replay performed here. |
| Novelty / Zhang ancestry | Binding source-audit-v2 qualification retained: explicit analytic reconstruction of the inherited decomposable mechanism, no restored clean-priority claim. |
| Formal/kernel, human, cross-vendor or configured dual-family acceptance | Not performed by this supplied-proof review. |

**Scoped disposition:** the ENERGY identity, FACE rigidity with all stated complex/degenerate boundaries, quantitative actual-state consequences and exact strict-region arithmetic are WRITTEN-SUPPORTED by this reconstruction. Parent disposition remains separate. No author/shared/pinned source was modified.
