# Compactness cannot be dropped from the fixed-parity theorem

**Status: WRITTEN counterexample, not parent adoption.** The compactness condition in `frontier-20261029-fixed-parity-universal-synthesis-v1.md` (SHA-256 `8c6329652525eccc6a1e10e9d9ecf7b5a0e4cb4a2336b1f8e6fff0c260986ab1`) cannot be discarded, even for a single fixed odd part and even if all members are monic and Hurwitz.

Take the noncompact family
\[
a_N(s)=s^3+Ns^2+s+1,\qquad N>1.
\]
The cubic Routh criterion gives strict Hurwitz stability because all coefficients are positive and \(N\cdot1>1\). Its odd part is the **same** \(O(t)=1-t\) for every \(N\).

Suppose a fixed real cubic \(b\) were common strictly positive real. Since \(a_N(0)=1\), strict positivity at zero forces \(b_0>0\). Choose any sufficiently small fixed \(t>0\) such that \(E_b(t)=b_0-b_2t>0\). Then
\[
P_{a_N,b}(t)=(1-Nt)E_b(t)+t(1-t)O_b(t)\longrightarrow-\infty
\quad(N\to\infty),
\]
a contradiction. The argument excludes **every** fixed cubic numerator, not only parity scalings.

For any compact truncation \(1+\delta\le N\le M\), the fixed-parity theorem does provide a common numerator; as \(M\to\infty\), no single numerator can remain common. This deliberately noncompact family is not an admissible original finite-width box and supplies no negative answer there. The cubic stability criterion and polynomial inequalities are written mathematics; no formal proof, independent review or novelty clearance is claimed.
