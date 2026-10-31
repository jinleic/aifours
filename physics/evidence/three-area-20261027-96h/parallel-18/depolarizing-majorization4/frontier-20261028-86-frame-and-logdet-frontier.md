# Projected-frame and positive-excess frontiers; a log-determinant obstruction

**Scope:** ordinary written derivations and bounded floating-point exploration, not a proof of either proposed universal inequality, an original-channel counterexample, a formal/kernel check, a peer review, or a novelty assessment. All states and projectors in the numerical searches were actual four-qubit objects. The explicit spectral countermodel in §3 is **abstract and is not claimed to arise from any physical input**. No historically held result is imported.

## 1. Two precise sufficient inequalities

For a normalized pure state `psi`, write `rho=|psi><psi|`, `Q=I-rho`, and

\[
F(\rho)=\sum_{i=1}^4\sum_{a=x,y,z}\sigma_i^a\rho\sigma_i^a,\qquad
S=\sum_{i,a}\langle\psi|\sigma_i^a|\psi\rangle^2,\qquad
M=QF(\rho)Q\big|_{\psi^\perp}.
\]

Since `Tr F=12` and `<psi|F|psi>=S`, `Tr M=12-S`. One candidate is

\[
\lambda_{\max}(M)+S/2\le4. \tag{A}
\]

If (A) holds for the actual state, then for **each** rank-three projector containing `psi`, its remaining rank-two part lies in `psi`-perpendicular. Using `T1=rho+F/4`, its trace obeys

\[
\operatorname{Tr}(PT_1)\le 1+S/4+\tfrac12\lambda_{\max}(M)\le3.
\]

Equivalently, (A) implies `K2(M)+S<=8`. At `p=0+`, degenerate first-order spectral perturbation gives

\[
K_3(\Lambda_p\rho)=1+p[-3+S/4+K_2(M)/4]+o(p),
\quad R_3(p)=1-p+O(p^2).
\]

Thus (A) gives a nonpositive first derivative of the original k3 excess, not a finite-p theorem and not a bound for projectors that do not contain `psi`.

An independent, stronger-looking auxiliary conjecture is

\[
\operatorname{Tr}(F(\rho)-2I)_+\le2.\tag{B}
\]

`Tr F=12` implies the variational expression on the left equals `max_{0<=k<=16}(K_k(F)-2k)`; all `k>=5` automatically give at most two. Hence it is enough to establish the four inequalities `K_k(F)<=2k+2` for k=1,2,3,4. In particular (B) gives `K3(F)<=8`, and then the actual common-projector bound `Tr(P T1)<=1+K3(F)/4<=3`. Convexity and affinity extend this auxiliary bound from pure to all mixed inputs. Neither (A) nor (B) is proved here, and (B) is not needed for the logically separate first-order condition from (A).

## 2. Bounded numerical searches

At the observed native clock `Wed Oct 28 19:20:01 PDT 2026`, the following scripts were pinned and their earlier runs had exited zero. Both use complex state vectors, not real-only models; negative eigenvalues at `10^-16` magnitude are floating roundoff, not exact positivity certificates.

* `frontier-20261028-84-projected-frame-scout.py`, SHA256 `3ce6d884804f65e1c4aa209b9a1e091ee4c9d75a868ac0ca5e0a02de09e0b92f`, seed 2026102884: 250 random starts, at most 100 projected-gradient steps each, seeking violations of (A). Largest final `lambda_max(M)+S/2-4 = -5.624720960861751e-05`; at that state `S=3.9526321002210594`, projected eigenvalue `2.0236277026798617`, eigenvector residual `1.1127788000064404e-15`, and orthogonality residual `3.925231146709438e-17`. Direct original channel at `p=0.2` gave top-three sum `0.8007725013169896`, below product reference `0.8019000000000001`.
* `frontier-20261028-85-frame-excess-scout.py`, SHA256 `aa1364e5d204545f1be68721e488a5bc33db3250b962ca9e3080ffe8245b4d1d`, seed 2026102885: for each k=1,2,3,4, 250 random starts and at most 150 alternating actual-state/projector updates to maximize `K_k(F)-2k`. Best values respectively were `2.0000000000000053`, `2.0000000000000124`, `2.000000000000016`, and `1.9999999999997726`. The small excesses are floating precision, not violations. Each best state was independently evaluated under the original channel at `p=0.2`; top-three sums were `0.7116865337428792`, `0.7223501176159826`, `0.7605856224515194`, and `0.8018999999999795`, respectively, against `0.8019000000000001`. Largest reported projector idempotence residual was `1.326657529852538e-15`.

These searches neither establish global optimality nor prove any claimed exact equality or violation. In particular they give no original-channel counterexample.

## 3. What the current public shifted-logdet theorem cannot settle alone

**Named external import, conditional:** Song, Wang, Tomamichel and Fang, *Approximate majorization and high-order capacity of quantum depolarizing channels*, arXiv:2609.37240v1, 29 Sep 2026, https://arxiv.org/html/2609.37240 , Theorem 4, states the shifted log-determinant ordering for every shift `u>0` and physical depolarizing parameter. The published theorem's proof has not been independently reconstructed here. Its introduction explicitly describes full output majorization as a conjecture; no general exact majorization is imported.

Assuming that theorem, put `u=p z/4` with fixed `z>0` and `p->0+`. In the decomposition `C psi` direct-sum `psi`-perpendicular, the upper-left block of `Lambda_p(rho)+u I` tends to one, the off-diagonal blocks are `O(p)`, and its lower block is `(p/4)(z I_15+M)+O(p^2)`. The Schur determinant formula, divided by `(p/4)^15`, yields the **necessary** all-z condition

\[
\det(zI_{15}+M)\ge z^{11}(z+2)^4.\tag{C}
\]

The right side is the actual product-reference projected spectrum: four 2s and eleven 0s. Condition (C), the trace identity, and even the extra hypothetical bound `lambda_max(M)<=4` do **not**, by themselves, imply (A), its weaker required `K2(M)+S<=8`, or the original k3 first-order conclusion. Here is an explicit abstract countermodel: take `S=1` and projected eigenvalues

\[
(4,4,1,1,1,0^{\times10}).
\]

They satisfy `Tr M=11=12-S` and `lambda_max(M)=4`. Moreover

\[
(z+4)^2(z+1)^3-z(z+2)^4
=3z^4+19z^3+41z^2+40z+16>0\qquad(z>0),
\]

so (C) holds, but `K2(M)+S=9>8` and `lambda_max(M)+S/2=9/2>4`. These numbers are only a nonnegative abstract spectrum meeting the listed necessary scalar constraints: no vector `psi` or physical Pauli-frame realization is asserted. The missing ingredient is a genuinely physical constraint coupling the projected spectrum, local Bloch data, and an actual common input/projector. Consequently neither the public shifted-logdet theorem nor a few numerical spectra close the original k3 gap.

No coauthor/stronger-model/human/independent-family review or formal proof is claimed. Prior process findings and quarantine dispositions remain unchanged.
