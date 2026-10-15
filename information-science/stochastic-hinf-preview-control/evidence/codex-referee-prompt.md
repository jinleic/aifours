You are a hostile referee for a mathematical control-theory claim. Work read-only. Read ONLY
files under /Users/jinleic/jinleic-workspace/ai4s/stochastic-hinf-preview-control/ (start with
work/theory.md; work/shp.py contains numerical code). Do not use the web. Do not delegate. Do not
write files.

CONTEXT. An open problem from the book "10000 Selected Problems in Sciences: Information Science"
(2011, pp. 674-676; problem by Zhang Huanshui and Wang Hongxia) asks for necessary and sufficient
(N&S) conditions and a controller for the continuous-time Ito system
  dx = [A x + B u + C w(t-h)] dt + [A0 x + B0 u] dW,  z = D0 x + D1 u,
with a full-information preview controller u(t) = F(x(t), w(s) | t-h <= s <= t), so that the
L2-induced gain from w (on [a,b-h]) to z (on [a,b]) is < gamma; finite horizon and infinite
horizon. work/theory.md formalizes this (Section 0, items F1-F7) and claims:
- Theorem 1 (finite horizon): solvable  <=>  the n x n "advanced" generalized Riccati differential
  equation (P) has a solution on [a,b]. In (P), the term gamma^-2 k k' uses
  k(t) = [P(t), -I] Phi(t,t+h) [C;0], where Phi is the transition matrix of the
  P-dependent Hamiltonian H0(P(s)) over the preview window. The explicit controller u* has the
  book's form.
- Theorem 2 (infinite horizon): solvable <=> a stationary equation (A) has a "stabilizing" solution
  (conditions T1, T2).

YOUR TASK. Try hard to break the claims. In particular check:
1. Lemma 1 (kernel identities K1, K2, M0, M1), including symplectic-inverse formulas, signs and
   transposes, and time-varying C(s).
2. Lemma 2 (completion of squares). Does every term really cancel? Is the treatment of the
   incoming value v(t+h) = w(t) and the outgoing value v(t) correct? Does the end-of-horizon
   convention k = 0 for t > b-h match the cost, whose denominator counts w only on [a, b-h]?
3. Lemma 3 (P >= 0) and Lemma 5 (continuation): is there a failure mode other than blow-up?
4. Necessity, Lemmas 6-8: the shift trick for a possibly nonlinear controller; the uniform bound
   c_*; whether u-degree "inf over all adapted u" versus the preview information structure
   matters; Lemma 8's adjoint/SMP argument and its use of the K2 identity; the claim that the
   value equals x'P x.
5. Information structure. w is adapted to the Brownian filtration, and w(t) enters the plant at
   t+h. Is the stationarity v(s) = gamma^-2 C' E[p(s) | F_{s-h}] used consistently? Could an
   adversary using anticipative or other randomized information break the necessity proof?
6. The formalization F1-F7. Is any restriction or interpretation unfaithful to the book's
   question? Is the mean-square reading justified?
7. Theorem 2: the gaps you see, and whether T1-T2 are the right "stabilizing" conditions,
   including the reduction for h = 0.
8. Any counterexample: a parameter set where (P) has a solution but no controller achieves the
   bound, or the reverse.

OUTPUT (Markdown):
(a) Overall verdict on Theorem 1: correct / correct-with-fixes / incorrect, with a one-paragraph
    justification.
(b) A numbered list of objections. Give each a severity (fatal / major / minor), the exact location
    (lemma, equation) and a concrete fix if you have one.
(c) Verdict on Theorem 2 and its precise gaps.
(d) Verdict on the formalization's fidelity.
(e) Your independent re-derivation of the kernel equation (K2) and of the P-equation's gamma term,
    stating whether it matches.
Be concrete. Do not pad.
