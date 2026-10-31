# Exact operator obstruction to an unproved preview-class embedding

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:26:39 PDT 2026**. A concrete legal-controller/domain bridge obstruction inside the supplied full-information-versus-bound-linear-class distinction. No new source, numerical/control probe or scientific execution. All prior exposure/process findings remain.

## 1. The precise issue, not a monotonicity claim

The bound class has state feedback and feedforward operator

`Rw(t)=L0 w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`,

with H in L2. It does NOT contain arbitrary finitely many interior point taps by definition. A larger available preview window alone therefore does not prove a nesting of these parameterized classes under time relabeling.

For example, shifting the input argument of a smaller-window current tap by d would require `Jw(t-d)` in a larger window of length h, with 0<d<h. The result below proves that this missing caller cannot be supplied by adjusting the two endpoint gains and an L2 kernel, even in uniform operator norm. This is an obstruction to that specific embedding/approximation step, NOT a counterexample to optimal preview monotonicity and NOT an assertion that an alternative actual controller cannot work.

The original source packet allows an abstract full-information F on its window, whereas the later bound class is a precise subclass. No full-window N&S theorem or synthesis success is inferred by silently enlarging the bound class here.

## 2. Exact all-variable theorem

Let finite T>h>0, 0<d<h, and let J be ANY nonzero real m-by-p matrix. Input domain is L2([0,T-h];R^p), zero-extended; output domain is L2([0,T];R^m). Define the interior delay `D_d w(t)=w(t-d)` and let R range over ALL two-endpoint-plus-L2-kernel feedforward operators above.

**Theorem.**

`inf_R ||J D_d-R||_(L2[0,T-h]->L2[0,T]) = ||J|| > 0`.        (1)

In particular no such R equals the interior tap for every input, and no sequence of admissible kernels/taps approximates it in the uniform input/output operator norm. This does not forbid strong convergence on each fixed input or weaker approximation notions.

## 3. Reconstruction from the original window variables

Choose an arbitrary nonempty interval I strictly inside (0,T-h), with length less than min(d,h-d). Such an interval exists. Then I, I+d and I+h are pairwise disjoint and lie in the input/output ranges where used. Restrict inputs to support in I, and restrict the measured operator image to the interval I+d.

On I+d both endpoint terms vanish: w(t) is supported in I and w(t-h) in I+h. The restriction of R is therefore the integral operator

`(K_H w)(t)=integral_I H(t-s)w(s)ds`, `t in I+d`.

All its arguments t-s lie in (0,h). Its matrix kernel has finite squared integral because

`integral_(I+d) integral_I ||H(t-s)||^2 dsdt <= |I| integral_0^h ||H(r)||^2 dr`.

Thus K_H is compact: approximate its square-integrable kernel by finite separated step kernels, whose operators have finite rank; Cauchy-Schwarz bounds the operator-norm error by the kernel L2 error. This is a deterministic controller-map fact, not a transformed physical output or a stochastic performance substitution.

Let e be an arbitrary unit maximizing vector for J, so |Je|=||J||, and let phi_n be any orthonormal sequence in scalar L2(I). Inputs w_n=phi_n e have norm one and converge weakly to zero. Compactness makes K_H w_n converge strongly to zero. The restricted interior tap is `Je phi_n(t-d)` and has norm ||J|| for every n. Consequently

`liminf_n ||(J D_d-R)w_n||_[0,T] >= ||J||`.

This proves the lower bound in (1) for EVERY possible choice of endpoint gains and kernel. For the reverse bound choose the zero operator R=0: the entire input interval shifted by d still lies in [0,T], so the norm of J D_d is exactly ||J||. Equality follows. All frequency/dimension/kernel choices above are quantified symbolic objects, not selected test samples or an executed basis enumeration.

## 4. Actual-controller caller and the state-feedback qualification

The theorem directly concerns the feedforward part, not the ability of a particular plant's state to remember something about its input. A state-feedback term Kx might help on selected actual trajectories; it is NOT ruled out universally by the feedforward argument.

There is nevertheless an original physical family where the caller is exact: take B=C=B0=0, arbitrary A,A0 and zero initial state, so the unique original state is identically zero for every disturbance and every bound controller. Keep original output `z=D0x+D1u`, with any D0 and any D1 for which D1J!=0. Then Kx is identically zero, and equality of the actual output map of an interior tap with that of a bound endpoint/kernel law would require

`D1J D_d=D1R`.

Applying the same proof to the nonzero matrix D1J rules this out. This is an all-matrix zero-state structural family, not a numerical probe, and it uses the ORIGINAL physical output. No new physical output/controller realization is constructed or optimized. It establishes that no UNIVERSAL actual-state emulation can be inferred from the class definitions alone.

The hypothetical interior tap is used solely to test a class-closure claim within the supplied full-information window. It is not adopted as a new allowed controller class or a synthesis witness, and no performance target is claimed achieved by it.

## 5. Boundaries and exact failed implication

If J=0 the distance is zero. At d=0 or d=h the operator is an allowed endpoint tap and the distance can be zero; those boundaries were explicitly excluded. At h=0 there is no interior tap. T>h is needed for a nontrivial input space. All positive dimensions, signs, ranks and all L2 kernels are included. If D1J=0 the particular physical output can conceal the missing controller map, and no output-level obstruction is asserted for that case.

The exact failed step is `extra preview information -> this TWO-ENDPOINT/L2-KERNEL parameter class automatically contains the shifted old law`. It is false as a universal representation claim. The proof does not establish that the optimal gains are nonmonotone, that all larger-preview designs fail, or that the full abstract original F class has the same obstruction. A legitimate monotonicity/synthesis proof must pay its actual class embedding or use a different argument.

Named ordinary inputs: zero extension/translation, finite matrix norm attainment, compactness of square-integrable-kernel operators (with reconstruction above), and weak-null orthonormal sequences in L2. No source beyond the admitted definitions/current scope, no held guide, no stopped realization/storage method and no scientific computation is used. Book-image/controller-domain equivalence remains NR-SOURCE. General original literal synthesis is still OPEN; no stronger verification, adoption or novelty claim is made, and all STOP/HOLD/ZERO/history/N4/aux214 limitations persist.
