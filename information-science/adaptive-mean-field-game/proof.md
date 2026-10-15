# Classical certification: adaptive discrete-time mean-field tracking

Date: 2026-10-14 (PT). FRONTIER label: **Certification / PARTIAL book coverage / NOVELTY-UNCLEAR**. This is a self-contained classical proof, not a Lean/kernel certificate. The identification construction uses classical instrumental Markov-parameter moments; no priority claim is made. The independent referee reviews the complete text recorded in `evidence/referee-prompt.txt`.

## 1. Scope and notation

The printed dynamics are retained, with a harmless noise-index shift:

\[
 x_i(t+1)=Ax_i(t)+Bu_i(t)+\Lambda\bar x_N(t)+w_i(t+1),\quad
 \bar x_N=N^{-1}\sum_i x_i,\quad x_i,u_i\in\mathbb R^d.
\]

All three matrices are unknown to every agent. The printed common-matrix reading is used; heterogeneous unknown local matrices are NOT covered. The cost is the printed sample-path limsup average of \(\|x_i(t+1)-\Phi(t,\bar x_N(t))\|^2\). Writing \(T^{-1}\sum_{t<T}\), instead of \(n^{-1}\sum_{t\le n}\), does not change any finite limit or limsup here. Norms without subscript are Euclidean/operator norms; parameter errors use Frobenius norm.

**Assumptions (explicit restrictions, not claims of minimality).**

* H1: \(N\ge2\); fixed finite \(d\); common time-invariant matrices. Known constants \(a,\ell\ge0\), \(0\le b<1\) satisfy
  \[
  \|A\|\le a,\quad\|B-I\|\le b,\quad\|\Lambda\|\le\ell,
  \qquad \kappa:=2a/(1-b)+\ell<1.
  \]
  Thus \(r:=a+\ell<1\) and \(B\) is invertible. This is a nonempty, full-dimensional robustly stable uncertainty class when the bounds are positive. It is much narrower than arbitrary stabilizable plants. A known nominal invertible input matrix could be absorbed into the input coordinates; here the nominal matrix is explicitly \(I\).
* H2: The vectors \(w_i(t)\) are iid over agents and time, have mean zero, covariance \(Q\), and \(\|w_i(t)\|\le W\) almost surely. Initial states, independent of future noises and probes, satisfy \(\sup_i\|x_i(0)\|\le X_0\). No positive definiteness of \(Q\) is needed.
* H3: \(\Phi\) is known, measurable, uniformly Lipschitz in its second argument with constant \(L\). A chosen deterministic orbit \(f(0)\), \(f(t+1)=\Phi(t,f(t))\), is known and obeys \(\sup_t\|f(t)\|\le F\). Global boundedness of \(\Phi\) is NOT required.
* H4: Agents know \(N,d,a,b,\ell\) and the clock. During deterministic calibration windows they may use a common prearranged Rademacher pilot \(c(t)\in\{-1,1\}^d\) and private independent Rademacher pilots \(v_i(t)\). All coordinates and time samples are independent except that \(c(t)\) is common to agents; probes are independent of noise and initial states. The algorithm uses no future probe values. This is a randomized decentralized information structure: common design randomness, not shared state observations or communication. If the book is interpreted as prohibiting even prearranged common excitation, this theorem does not cover that reading.

For precision, realize all populations on one product probability space using infinite agent/time noise and private-pilot arrays, one common-pilot time array, and one bounded initial-state array. These three objects (initial states, the whole noise array, the whole pilot array) are jointly independent; initial states need not be independent of one another. Population N uses the first N agents. A causal control at time t is measurable with respect to \(\mathcal G_t=\sigma(x(0),w(1),\ldots,w(t),c(0),\ldots,c(t),v(0),\ldots,v(t))\), enlarged if needed by independent deviation randomization available through t. Thus \(w_i(t+1)\) is independent of \(\mathcal G_t\). Constructed controls use only the stated local sub-information. “Block past” below means the history through its initial state, before that block's first pilot is revealed.

H1 ensures safe exploration and safe exploitation for every estimate, H2 makes the explicit elementary concentration and pathwise state bound possible, H3 gives a finite tracking target and cost comparison, H4 makes unknown local and global parameters separately observable without measuring any other state. These are sufficient assumptions, not a characterization of necessary ones.

## 2. Fully specified local algorithm

Let \(\mathcal P_c\) denote Frobenius projection onto the operator-norm ball of radius \(c\): take an SVD and cap every singular value at \(c\). It is the metric projection onto a closed convex set and is nonexpansive in Frobenius norm.

Set initial estimates \(\widehat A_i=\widehat\Lambda_i=0,\widehat B_i=I\), and use \(u_i=0\) for \(t<4\). For each integer \(k\ge2\), the epoch is \([2^k,2^{k+1})\). Put \(m_k=\lfloor2^{k/2}\rfloor\). The first \(m_k+1\) controls of the epoch are
\[
 u_i(t)=c(t)+v_i(t).
\]
There are \(m_k\) samples \(t=2^k,\ldots,2^k+m_k-1\). After observing the state at \(2^k+m_k+1\), agent \(i\) calculates
\[
 \widetilde B_i=\frac1{m_k}\sum_t x_i(t+1)v_i(t)^\top,
 \quad \widetilde C_i=\frac1{m_k}\sum_t x_i(t+2)c(t)^\top,
 \quad \widetilde D_i=\frac1{m_k}\sum_t x_i(t+2)v_i(t)^\top.
\]
Only its own states and its own known pilots occur. Set
\[
 \widehat B_i=I+\mathcal P_b(\widetilde B_i-I),\quad
 M_i=\widetilde C_i\widehat B_i^{-1},\quad
 D_i=\widetilde D_i\widehat B_i^{-1},
\]
\[
 \widehat A_i=\mathcal P_a\!\left(\frac{ND_i-M_i}{N-1}\right),\qquad
 \widehat\Lambda_i=\mathcal P_\ell\!\left(\frac{N(M_i-D_i)}{N-1}\right).
\]
Throughout the rest of the epoch use
\[
 u_i(t)=\widehat B_i^{-1}\big[f(t+1)-\widehat A_i x_i(t)-\widehat\Lambda_i f(t)\big].                 \tag{2.1}
\]
Hold the last estimates until the next update, including during the next calibration window. All inverses exist because \(\sigma_{\min}(\widehat B_i)\ge1-b\). The mean estimator is simply \(f(t)\), including during calibration.

Write \(\widehat\theta_i(t)=(\widehat A_i(t),\widehat B_i(t),\widehat\Lambda_i(t))\), with the product Frobenius norm. In epoch k the estimate in force comes from epoch k after time \(2^k+m_k+1\), and otherwise from epoch k-1 (or from the specified initial estimate).

## 3. Theorem

Define
\[
 H=2(1+b)\sqrt d+W,\quad q=(1+b)/(1-b),\quad
 X=\max\left\{X_0,\frac H{1-r},\frac{q(1+\ell)F+W}{1-\kappa}\right\},
\]
\[
 S=\sum_{j=0}^{\infty}\Lambda^jQ(\Lambda^j)^\top,
 \qquad \operatorname{tr}S\le\frac{\operatorname{tr}Q}{1-\ell^2}.
\]
Under H1–H4, the following hold.

**T1 (uniform stability):** \(\|x_i(t)\|\le X\) almost surely for every time, every agent and every \(N\ge2\). The constant contains no \(N\).

**T2 (identification, fixed N and explicit rate):** For \(0<\delta<1\), with probability at least \(1-\delta\), simultaneously for every epoch \(k\ge2\) and \(i\le N\), the estimates after that epoch's calibration satisfy
\[
 e_k=4dX\sqrt{\frac{\log(6Nd^2 k(k-1)/\delta)}{m_k}},
\]
\[
 \|\widehat B_i-B\|_F\le e_k,\quad
 \|\widehat A_i-A\|_F\le\frac{3(1+r)e_k}{1-b},\quad
 \|\widehat\Lambda_i-\Lambda\|_F\le\frac{4(1+r)e_k}{1-b}.                  \tag{3.1}
\]
In particular, for every fixed finite \(N\ge2\), all estimates converge almost surely to their true matrices. In physical time, after initialization,
\[
 \max_{i\le N}\|\widehat\theta_i(t)-\theta\|_F
 =O\!\left(t^{-1/4}\sqrt{\log\log t}\right)\quad\text{a.s.}                 \tag{3.2}
\]
Here the fixed-N almost-sure constant may depend on \(N\) and the sample path. The all-agent finite-probability bound (3.1), not (3.2), specifies the dependence on \(N\).

**T3 (mean estimation, correct order of limits):** For every fixed \(N\ge2\),
\[
 \lim_{T\to\infty}\frac1T\sum_{t<T}\|\bar x_N(t)-f(t)\|^2
 =\frac{\operatorname{tr}S}{N}\quad\text{a.s.}                             \tag{3.3}
\]
Thus the squared long-run error is exactly \(O(N^{-1})\), and the corresponding root-mean-square error is \(O(N^{-1/2})\). This does NOT say that the unobserved mean is recovered pointwise as time grows for fixed N.

**T4 (Nash rate for the printed random cost):** For every agent,
\[
 \operatorname{tr}Q\le J_i\le\operatorname{tr}Q+
 \frac{(\ell+L)^2\operatorname{tr}S}{N}\quad\text{a.s.}                    \tag{3.4}
\]
For every fixed causal unilateral deviation, even one using all current/past states and the true parameters, its cost is at least \(\operatorname{tr}Q\) almost surely. The global-information oracle attains exactly \(\operatorname{tr}Q\). Hence the profile is an \(\varepsilon_N\)-Nash profile with \(\varepsilon_N=(\ell+L)^2\operatorname{tr}S/N\), in the policywise almost-sure sense (or equivalently relative to the essential infimum of competing random costs). Null sets are not asserted to be uniform over an uncountable class of arbitrary deviations. Countably many N and the finitely many agents for each N can share a probability-one event.

## 4. Proof of T1: safety before identification

During calibration, with \(Z(t)=\max_i\|x_i(t)\|\),
\[
 Z(t+1)\le rZ(t)+H.
\]
For exploitation, \(\|\widehat B_i^{-1}\|\le(1-b)^{-1}\), and
\[
 \|A-B\widehat B_i^{-1}\widehat A_i\|
 \le a+(1+b)a/(1-b)=2a/(1-b).
\]
Substitution in (2.1) gives
\[
 Z(t+1)\le\kappa Z(t)+q(1+\ell)F+W.
\]
The initial zero-input steps satisfy the weaker calibration bound. Each of these recursions preserves \([0,X]\); induction proves T1 without assuming estimation accuracy. In particular, this is not a circular closed-loop boundedness assumption.

## 5. Proof of T2: local moments separate A from Lambda

Condition on the complete state and past at the start of one calibration block. During this block the dynamics are linear with prescribed independent pilots. For every sample index t,
\[
 E[x_i(t+1)v_i(t)^\top\mid\text{block past}]=B.                            \tag{5.1}
\]
The conditioning here is only on the history before the block, not on later observations. The one-step response of every agent to \(c(t)\) is \(B c(t)\). Its two-step response at agent i is therefore \((A+\Lambda)B c(t)\). The one-step response to \(v_i(t)\) is B at agent i and zero at the other agents, so its two-step response is \((A+\Lambda/N)B v_i(t)\). Independence and zero means of the other terms give exactly
\[
 E[\widetilde C_i\mid\text{block past}]=(A+\Lambda)B=:C,
 \quad E[\widetilde D_i\mid\text{block past}]=(A+\Lambda/N)B=:D_{\rm mom}.   \tag{5.2}
\]
These identities are finite-N identities; no mean-field substitution and no omitted-mean bias is involved.

For completeness, concentration can be obtained without treating the overlapping samples as independent. Group all innovations at each calibration time s into a block \((c(s),v_1(s),\ldots,v_N(s),w_1(s+1),\ldots,w_N(s+1))\). There are \(m+1\) independent blocks conditional on the initial state. Replacing one block changes any agent's next state by at most \(2H\), and changes subsequent states by at most \(2Hr^j\). In any scalar entry of any of the three empirical matrices, the sum of changes coming from changed output states is at most \(2H/(1-r)\le2X\). The changed multiplier c or v adds at most \(2X\) (only one summand uses that multiplier). Thus the normalized statistic changes by at most \(4X/m\) per block. This also covers the lag-two terms whose first affected output can occur one summand before the changed input index.

Formally, freeze the block-initial population state: the statistic is a function of that state and the \(m+1\) independent innovation blocks. The sensitivity bound holds uniformly over all initial states with maximum norm at most X and all supported block values. T1's calibration invariance also applies to the counterfactual trajectory with one block replaced, which justifies its output bound X in the multiplier term.

For \(\widetilde K\in\{\widetilde B_i,\widetilde C_i,\widetilde D_i\}\), the bounded-differences inequality consequently gives, for each entry,
\[
 P(|\widetilde K_{ab}-E\widetilde K_{ab}|>z\mid\text{block past})
 \le2\exp\!\left(-\frac{2z^2m^2}{16X^2(m+1)}\right)
 \le2\exp\left(-\frac{mz^2}{16X^2}\right).                               \tag{5.3}
\]
A union bound over \(3Nd^2\) entries, followed by \(\|\mathcal E\|_F\le d\max|\mathcal E_{ab}|\) for an entrywise error matrix \(\mathcal E\), says all three empirical matrices for all agents have Frobenius error at most \(e_k\), except with probability \(\delta/[k(k-1)]\). Since \(\sum_{k\ge2}1/[k(k-1)]=1\), the assertion is simultaneous in k.

Projection of B gives \(\|\widehat B_i-B\|_F\le e_k\). With \(M=A+\Lambda\), \(D_0=A+\Lambda/N\), both bounded in operator norm by r,
\[
 \|\widetilde C_i\widehat B_i^{-1}-M\|_F
 \le\frac{(1+r)e_k}{1-b},\qquad
 \|\widetilde D_i\widehat B_i^{-1}-D_0\|_F
 \le\frac{(1+r)e_k}{1-b}.                                               \tag{5.4}
\]
Because \(A=(ND_0-M)/(N-1)\) and \(\Lambda=N(M-D_0)/(N-1)\), the bounds \((N+1)/(N-1)\le3\) and \(2N/(N-1)\le4\), plus nonexpansive projection, prove (3.1). For the almost-sure rate apply (5.3) with per-epoch failure probability \(k^{-2}\); Borel–Cantelli then gives an eventual error bound of order \(\sqrt{\log k/m_k}\) for fixed N. Since \(m_k\asymp2^{k/2}\) and the most recent estimate at any sufficiently large t is from epoch k or k-1 with \(2^k\le t<2^{k+1}\), this is (3.2).

## 6. Vanishing calibration density and stable convolution

Let \(\mathcal C\) be the set of calibration times. Through time \(T\),
\[
 |\mathcal C\cap[0,T)|\le4+\sum_{k\le\log_2T}(\lfloor2^{k/2}\rfloor+1)
 =O(\sqrt T+\log T).
\]
Thus its density is zero, even if T falls inside a calibration window.

Put \(e_i(t)=x_i(t)-f(t)\). At an exploitation time, exact substitution gives
\[
 e_i(t+1)=\Lambda\bar e(t)+w_i(t+1)+g_i(t),                               \tag{6.1}
\]
where
\[
 g_i=(A-B\widehat B_i^{-1}\widehat A_i)e_i+\zeta_i,
\]
\[
 \zeta_i=(A-\widehat A_i)f+(\Lambda-\widehat\Lambda_i)f
 +(B-\widehat B_i)\widehat B_i^{-1}
       [f(t+1)-(\widehat A_i+\widehat\Lambda_i)f(t)].                     \tag{6.2}
\]
Since states, f, estimates and inverse estimates are bounded and T2 holds, \(g_i(t)\to0\) along exploitation times for each fixed N, uniformly over its finitely many agents. At calibration times define \(g_i\) by (6.1); it is bounded, because every term there is bounded. Consequently
\[
 \frac1T\sum_{t<T}\max_{i\le N}\|g_i(t)\|^2\longrightarrow0\quad\text{a.s.} \tag{6.3}
\]
This proves that infinite, but increasingly sparse, learning is not silently thrown out of the cost.

We use a deterministic convolution fact. If \(\|\Lambda\|\le\ell<1\), z obeys \(z(t+1)=\Lambda z(t)+h(t)\), and \(T^{-1}\sum_{t<T}\|h(t)\|^2\to0\), then \(T^{-1}\sum_{t<T}\|z(t)\|^2\to0\). Indeed, for the zero-initial response, weighted Cauchy–Schwarz and summation give
\[
 \sum_{t<T}\left\|\sum_{s<t}\Lambda^{t-1-s}h(s)\right\|^2
 \le (1-\ell)^{-2}\sum_{s<T}\|h(s)\|^2.
\]
The initial response has finite total squared norm and so vanishing Cesaro average.

## 7. Proof of T3: the finite-population noise floor

Let \(\eta(0)=0\), \(\eta(t+1)=\Lambda\eta(t)+\bar w_N(t+1)\). Average (6.1) over agents. The difference \(\bar e-\eta\) is the stable filter of \(N^{-1}\sum_i g_i\) plus its initial condition. By (6.3) and the convolution fact, its squared Cesaro average vanishes.

The bounded iid sequence \(\bar w_N\) has mean zero and covariance \(Q/N\). The stable linear filter has stationary covariance \(S/N\). One elementary justification of its long-run covariance is to extend the iid sequence to negative times: the absolutely convergent moving average \(\eta^{\rm st}(t)=\sum_{j\ge0}\Lambda^j\bar w_N(t-j)\) is a bounded stationary ergodic process, so its squared norm has time average \(\operatorname{tr}S/N\). The initial-condition difference from \(\eta\) decays geometrically. Cauchy–Schwarz then removes the zero-Cesaro-energy difference \(\bar e-\eta\), proving (3.3). A countable intersection handles all finite N.

## 8. Proof of T4: original cost and unilateral comparison

Write the tracking error as \(w_i(t+1)+h_i(t)\). The term \(h_i(t)\) is predictable (it can depend on the current probes, which are independent of the next system noise). For the constructed profile it is bounded. Hence a bounded martingale-difference strong law yields
\[
 T^{-1}\sum_{t<T}h_i(t)^\top w_i(t+1)\to0,
 \quad T^{-1}\sum_{t<T}\|w_i(t+1)\|^2\to\operatorname{tr}Q.
\]
By (6.1),
\[
 h_i(t)=g_i(t)+\Lambda\bar e(t)+\Phi(t,f(t))-\Phi(t,f(t)+\bar e(t)).
\]
The last three terms, excluding g, have norm at most \((\ell+L)\|\bar e(t)\|\). Equation (6.3) and Cauchy–Schwarz make every contribution of g vanish in the long-run cost. Equation (3.3) proves the upper bound (3.4).

For any fixed causal deviation, not assumed stable or bounded, the same representation \(h(t)+w_i(t+1)\) holds with finite predictable h. Here is a lower-bound argument that does not incorrectly assume its energy is bounded. Set \(V_T=\sum_{t<T}\|h(t)\|^2\), \(M_T=\sum_{t<T}h(t)^\top w_i(t+1)\). Bounded, centered noise implies the conditional Hoeffding bound
\[
 E\!\left[\exp[-s h(t)^\top w_i(t+1)]\mid\mathcal G_t\right]
 \le\exp[s^2W^2\|h(t)\|^2/2].
\]
For fixed \(0<\epsilon<1/2\), take \(s=2\epsilon/W^2\) if \(W>0\). The resulting exponential supermartingale and Markov's inequality show
\[
 P(M_T<-\epsilon V_T-2s^{-1}\log T)\le T^{-2}.
\]
Borel–Cantelli gives \(M_T\ge-\epsilon V_T-O(\log T)\) eventually. Therefore
\[
 \sum_{t<T}\|h(t)+w_i(t+1)\|^2
 \ge(1-2\epsilon)V_T+\sum_{t<T}\|w_i(t+1)\|^2-O(\log T).
\]
Division by T proves the lower bound \(\operatorname{tr}Q\). If \(W=0\), this is immediate. This holds for each competitor almost surely, and therefore for the essential infimum of their random costs, without claiming one null set works for all non-countably many competitors.

With full current state and true-parameter information, the causal control
\[
 u_i(t)=B^{-1}[\Phi(t,\bar x_N(t))-Ax_i(t)-\Lambda\bar x_N(t)]
\]
makes its tracking error exactly \(w_i(t+1)\), regardless of how the other agents react. Thus the global-information best-response essential infimum is \(\operatorname{tr}Q\). The decentralized comparison follows. This concludes T1–T4.

## 9. Sharp limitations and counterexamples

These are counterexamples to unrestricted readings, not a full solution of the book's research program.

**C1 (control authority):** In one dimension take \(A=2,B=0,\Lambda=0,w=0,x_i(0)=1\). Every causal control has \(x_i(t)=2^t\); neither time-average nor pointwise stability is possible. Some stabilizability assumption is genuinely necessary for this stability requirement, not for every cost-only or Nash requirement. Full invertibility of B is sufficient for the theorem's one-step cancellation, but not necessary for every possible control design.

**C2 (target growth):** Let \(A=\Lambda=0,B=1,w=0,\Phi(t,z)=t+1\). The unrestricted optimum is zero via \(u_i(t)=t+1\). Any policy with \(\sup_T T^{-1}\sum_{t<T}\|x_i(t+1)\|^2<\infty\) has infinite tracking cost: use \((x-y)^2\ge y^2/2-x^2\), whose average right side grows quadratically. Thus stability and asymptotic optimality cannot both be guaranteed for arbitrary measurable \(\Phi\). Merely bounding \(\Phi\) is not the only repair; bounded mean-field reference plus regularity is the sufficient repair used here.

**C3 (noise and pointwise state bound):** With \(A=\Lambda=0,B=1,\Phi=0\), independent nondegenerate Gaussian noise prevents a deterministic bound on \(\sup_t|x_i(t)|\), even under oracle cancellation. For this scalar oracle example, \(x_i(t+1)=w_i(t+1)\), so the ordinary strong law gives finite long-run average square \(\sigma^2\); this is not an unbounded-noise extension of T1–T4. With identical common noise across agents, \(\bar w_N=w\), the deterministic mean proxy instead has a non-vanishing noise floor as \(N\to\infty\). Thus an unrestricted correlation class cannot enjoy the stated 1/N deterministic-proxy rate. Bounded noise is used in T1's stronger bound and in the elementary concentration argument.

**C4 (N=1 identifiability):** The observations under every causal input depend on A and Lambda only through \(A+\Lambda\). Two triples \((A,B,\Lambda)\) and \((A+\Delta,B,\Lambda-\Delta)\), with nonzero perturbation matrix \(\Delta\), have identical input-output laws. No estimator can consistently distinguish them on that class. This is why T2 explicitly begins at N=2; the instability counterexample does not stand in for this separate identifiability obstruction.

**C5 (fixed-N mean recovery):** For \(A=\Lambda=0,B=1,u_i=0\), with independent Gaussian \(w_i\) of variance \(\sigma^2\), \(x_i(t)=w_i(t)\) for t>=1. Conditional on agent i's complete local history through time t,
\[
 \operatorname{Var}(\bar x_N(t)\mid\mathcal F^i_t)=(N-1)\sigma^2/N^2>0.
\]
Every local estimator has at least this mean-square error. This refutes any universal fixed-N, time-to-infinity exact-current-mean consistency claim. It does not refute T3's population-limit consistency or T2's parameter consistency.

**C6 (proxy excitation and cost need not coincide):** With \(f\equiv0\), the proxy regression column for Lambda is identically zero, so a least-squares identifier using only \((x_i,u_i,f)\) cannot update Lambda through that column. In the noiseless zero-state, zero-control subcase, every Lambda produces the same data and zero cost. Thus failure to identify Lambda can be immaterial for the cost. This is a failure of that experiment/proxy identifier, not a universal impossibility of identifying Lambda: H4's separate common/private probes identify it even for \(f\equiv0\).

**C7 (proxy-LS endogeneity):** In the stationary scalar, known-parameter decentralized certainty-equivalence closed loop with zero target, \(x_i(t+1)=\lambda\bar x_N(t)+w_i(t+1)\), with \(A=0,B=1,u=0, |\lambda|<1\),
\[
 \operatorname{Var}\bar x_N=\frac{\sigma^2}{N(1-\lambda^2)},\quad
 \operatorname{Var}x_i=\sigma^2+\lambda^2\operatorname{Var}\bar x_N,
 \quad \operatorname{Cov}(x_i,\bar x_N)=\operatorname{Var}\bar x_N.
\]
Regressing \(x_i(t+1)\) on \(x_i(t)\), while substituting f=0 for the omitted mean, converges to
\[
 A_{\rm pseudo}=\frac{\lambda}{N(1-\lambda^2)+\lambda^2},
\]
not the true A=0 when lambda is nonzero. Thus simply importing a martingale-noise LS theorem for the proposed proxy regressor would be invalid. This does not rule out more carefully designed proxy adaptive control.

## 10. What remains outside this proof

The theorem is not the unrestricted book class. It does not handle arbitrary unknown stabilizable matrices, underactuation, heterogeneous unknown local dynamics, arbitrary measurable targets/noise laws, or a strict no-common-randomness reading. It gives all four properties only on H1–H4, including fixed-N consistency of all three matrices. The price is robustly stable full actuation and explicit sparse calibration. Those restrictions are not claimed necessary; comparisons with prior theorems must retain their different assumptions and identification targets. Extending safe decentralized identification and control beyond a known robustly stable uncertainty class, without observing the population mean, is the exact unclosed positive-design obligation here.
