**Findings: 0 FATAL, 0 MAJOR, 4 required MINOR corrections.** The corrections concern auxiliary statements and scope remarks; the four target conclusions survive.

1. **SOURCE00:LF26–29, LF41–45 — Lemma U needs “suppose \(w\) avoids.”** Its unconditional statement is false.

   At \(p=5\), take
   \[
   w=\rho_3\rho_1^6\sigma_0^9\rho_{-1}\sigma_0.
   \]
   It satisfies the stated structural hypotheses, with \(H=4,\ \kappa=0\). Expanding and deleting two reflections gives
   \[
   u^\circ=\rho_1^9\sigma_0^7\rho_{-1}\sigma_0,
   \]
   which avoids. Indeed, its all-plus pattern permits even \(m=4,6,8,10\), with sums \(m\) or \(m-2\); the \(m=10\) all-ones choice is unavailable, and every available sum is nonzero modulo \(5\). Its mixed pattern permits \(m=2,4,6,8\), all with effective sum \(m\) and target \(0\).

   **Repair:** prepend the avoidance assumption to Lemma U. This is already the premise supplied by SOURCE00:LF72. Also record the resulting bounds \(0\le\kappa\le p-2\). The capped-case argument then works.

2. **SOURCE00:LF65–67 — the constant pattern can have \(P=\varnothing\).** After the global sign reversal making the expansion effective-positive, a negative heavy can give the all-minus pattern.

   **Repair:** replace “\(P\) is all runs” by “\(z\) is constant, so \(P\) is empty or full and \(T(z)=0\).” Since \(n=0\), the claimed absence of light \(\rho_{sc}\) and the subsequent parity argument remain valid.

3. **SOURCE02:LF24–25 — PM* does not always produce all-odd blocks at shorter lengths.** If there are no odd blocks, it leaves one even block.

   For example, at \(p=5\),
   \[
   \rho_1^9\sigma_0^8
   \]
   is a length-\(17\) avoider, with usual pair capacity \(H=4\), \(\kappa=0\), and FULL. Any identity selection of length \(10\) would require an even number \(m\in\{2,4,6,8\}\) of rotations, whose sum is nonzero modulo \(5\). PM* cannot turn its sole even block odd.

   **Repair:** qualify the reduction by requiring at least one odd block. Retain all-odd form as an explicit hypothesis of the variable-length theorem.

4. **SOURCE02:LF79–80 — SH-ROT does not supply the asserted \(\kappa=0\) equality example.** Its family has
   \[
   H=p-3,\qquad \kappa=2.
   \]
   With \(c=1\), its heavy has weight \(2p-3\), so \(E=2p-4\) and \(N+E=6p-8\); at \(p=5\), this is \(22\), rather than \(18\).

   **Repair:** remove that attribution. A valid replacement equality family is
   \[
   \widetilde w_p=\rho_3\sigma_0^{2p-1}\rho_1^{2p-5}\sigma_4.
   \]
   Here \(\kappa=0\), FULL holds, \(E=2\), and \(N+E=4p-2\). Its all-plus sums have positive even weights below \(2p\). Its mixed-pattern sums are exactly
   \[
   6-2p,\ 8-2p,\ldots,2,
   \]
   which miss the target \(4\) modulo \(p\). Thus this replacement is analytically verified.

| Target | DISPOSITION |
|---|---|
| SOURCE00 — Theorem SH3+- | **ACCEPT-WITH-FIXES**, findings 1–2 |
| SOURCE01 — Theorem SHm | **ACCEPT**, using the audited SH3+- conclusion |
| SOURCE02 — Theorem ELT0 and critical-length corollary | **ACCEPT-WITH-FIXES**, findings 3–4 |
| SOURCE03 — Proposition SH-ROT | **ACCEPT** |

For **SH3+-**, the following checks establish the conclusion throughout the requested scope.

Under avoidance, GRX’s reflection-pair selection gives \(H\le p-1\); hence
\[
0\le\kappa\le p-2,\qquad
R=2p+2\kappa-k,\qquad R\ge k\Longrightarrow R\ge p+\kappa\ge p.
\]
These are consequences of avoidance, not additional hypotheses. K1 disposes of the one-block case.

Expansion and pair deletion preserve length \(4p-2\), nonempty rotation runs, odd nonempty reflection blocks, and constant maximal cyclic reflection runs. In particular, \(u^\circ\) is a genuine RGR word. Writing \(K=\kappa(u^\circ)=\kappa+1\), its parameters satisfy
\[
H^\circ=H-1,\quad F^\circ=F-2,\quad R^\circ=R+2,\quad 1\le K\le p-1.
\]

Every branch in SOURCE00:LF31–45 is justified:

- \(A^\circ\ge2p\): the trivial rotation selection.
- \(B^\circ>K\): \(K+1\) opposite pairs give an all-plus zero sum of admissible length \(2K+2\le2p\).
- \(1\le B^\circ<K\): Corollary B′(b), with precisely its stated hypotheses.
- \(B^\circ=0<K\): the accepted C1 composition; no inherited condition is needed.
- \(B^\circ=K,\ k\ge p+1\): KBH applies with \(A^\circ\ge B^\circ=K\), \(F^\circ,R^\circ\ge1\), and \(o_F=k\ge p+1\).
- \(B^\circ=K,\ k\le p\): KB’s uncapped implication applies after the in-file exclusion below.

The use of (V) is within Davenport-alpha’s corrected scope. Choose \(H^\circ\) disjoint empty gaps pairing reflections inside the constant blocks. All rotations lie outside these gaps. A frame at a nonempty rotation gap lies outside \(I\). Here \(F^\circ\ge k\ge2\) and \(N=4p-2\le4p-1\). Thus avoidance gives
\[
R^\circ+H^\circ\le3p-2,
\qquad\text{equivalently}\qquad K\le k-1.
\]

The capped-case exclusion is sound under finding 1’s premise. Since \(A^\circ\le2p-1\), a capped segment contains exactly all \(2p-1\) majority copies and no minority copy. All-odd form makes each OR-segment a single run.

If the expansion is minority, collapsing its three copies leaves only \(K-2\) original rotations across the other \(k-1\) nonempty runs. This gives \(k-1\le K-2\), contradicting \(K\le k-1\). If it is majority, \(w\) has \(2p-4\) majority light letters and \(K=\kappa+1\) minority light letters. There are enough of both to select \(K\) opposite pairs. Their length \(2K=2\kappa+2\) is forbidden by \(w\)’s all-plus GRX condition. **D0 is therefore never assumed or transported.**

FLEX’s ordinary cases preserve the signed sum and give counts \(m^\circ\) or \(m^\circ-2\). This includes \((n,q_+)=(1,2),q_-=0\): here \(M=R-2\ge1\), so the proposed heavy-plus-negative replacement exists.

The only residual case is \((n,q_+)=(0,2)\). Failure of both alternatives forces
\[
q_-=M=R-1,\qquad m^\circ=R+1,
\]
so \(R\) is odd. If \(\Phi\ge2\), the failed count bound implies \(R\le2\kappa+2\); together with nonempty runs and \(\kappa\le p-2\), this forces
\[
H=1,\quad \kappa=p-2,\quad k=R=2p-2,
\]
contradicting odd \(R\). If \(\Phi=0\), the two count bounds and even \(M\) force \(M=2\kappa+2\). The zero equation gives \(2-M\equiv0\pmod p\), hence \(\kappa=0\), \(M=2\), and \(R=3<p\). Thus the former exceptional case is eliminated for both heavy signs and every permitted number of odd blocks.

For **SHm**, STEP and the induction in SOURCE01:LF19–49 pass.

Avoidance gives \(R\ge p\), and therefore
\[
L_1=R-\eta\ge p-\eta\ge3.
\]
Each of O1–O5 preserves the signed value, with count changes
\[
(0,-2,-2,0,+2);
\]
each of P1–P5 does so with changes
\[
(0,-2,-4,-2,0).
\]
Used and unused light letters are correctly distinguished. Other selected heavies remain fixed. The only extra endpoint checks are O5’s upper bound and P3’s lower bound, both explicitly imposed. Counts decreased by two are automatically admissible because \(m^\circ\ge s_0+2\).

The failure analysis is exhaustive:

- All O-moves failing forces \(n=l_+=l_-=0\) and \(m^\circ=s_1\). The selection then has at most \(\eta\) rotations, so
  \[
  k\ge\Phi\ge2p-\eta,
  \]
  contradicting \(k\le2p-4-\eta\).
- All P-moves failing forces \(n=l_+=0,\ l_-=M=L_1\), and \(m^\circ<s_0+4\). Since \(m^\circ\ge2+L_1\), this yields
  \[
  k>2p-4-\eta+\Phi,
  \]
  again contradicting the hypothesis.

The induction retains length \(4p-2\), changes \((F,R,H,\eta)\) to
\[
(F-2,R+2,H-1,\eta-1),
\]
and preserves \(k\) and RGR shape. Consequently \(H-1\ge\eta-1\), while the required \(k\)-bound becomes weaker by one. The remaining heavy count is exact because \(\pm3c\notin\{\pm c\}\) for \(p\ge5\). The induction reaches SH3+- with the necessary spare reflection pair.

For **ELT0**, SOURCE02:LF29–57 proves the theorem with its explicit all-odd and FULL hypotheses.

The crucial bounds are
\[
R\le2p-k\le2p-\Phi.
\]
FULL would realize weight \(2p\) if \(W\ge2p\); odd weights make its cardinality positive and even, producing a forbidden all-plus selection. Hence \(W\le2p-1\).

For a solution of the expanded word, \(\Phi=0\) is correctly excluded by this bound and parity. For \(\Phi\ge2\), setting \(t=q-q'\), the integer \(t+W_{P^c}\) lies in \([0,W]\). FULL supplies the required global subset \(S\). The construction
\[
U=S\cap P,\qquad V=P^c\setminus S
\]
preserves the signed weight exactly. Its cardinality is even and satisfies
\[
2-\Phi\le0\le |U|+|V|\le R\le2p-\Phi.
\]
Thus GRX supplies the required reflections. No fullness assumption on individual runs is needed.

The exact-length extraction is also valid: deleting
\[
d=N+E-(4p-1)\le E-1
\]
added copies preserves every original rotation’s first copy, every nonempty run, and every reflection block. The resulting ordered subword is genuinely RGR of length exactly \(4p-1\), so RGR-LONG applies at its accepted scope. Finally \(E\ge0\) gives \(E=0\) at \(N=4p-2\), proving precisely that every rotation is \(\rho_c\).

The Savchev–Chen paragraph is conditional and is not used in this argument.

For **SH-ROT**, there is a direct ordered-product verification independent of finite aids.

Let \(\varepsilon\in\{0,1\}\) indicate selection of \(\rho_{-3}\), let \(t\) count selected \(\rho_1\)’s, let \(a\) count selected \(\sigma_2\)’s, and let \(b\in\{0,1\}\) indicate the final \(\sigma_0\). Identity requires \(a+b\) even. Put \(m=\varepsilon+t\), which is therefore even.

If \(b=0\), then \(a\) is even and \(a\le2p-6\), so \(6\le m\le2p\). The product is
\[
\rho_{t-3\varepsilon}.
\]
For \(\varepsilon=0\), its value is even \(m\in[6,2p-2]\). For \(\varepsilon=1\), its value is even \(m-4\in[2,2p-4]\). Neither can vanish modulo odd \(p\).

If \(b=1\), then \(a\) is odd and \(4\le m\le2p-2\). Using the stated group law,
\[
\rho_{-3\varepsilon}\sigma_2\rho_t\sigma_0
 =\rho_{2-t-3\varepsilon}.
\]
Its value is \(2-m\) when \(\varepsilon=0\), and \(-m\) when \(\varepsilon=1\). Both are nonzero even integers strictly between \(-2p\) and \(0\), so neither is divisible by \(p\).

This exhausts every selection. Non-rigidity follows because containing \(1\) in a pair \(\{c,-c\}\) forces that pair to be \(\{1,-1\}\), while \(-3\equiv\pm1\) would require \(p\mid2\) or \(p\mid4\).

The audit re-derived the four new arguments and checked their import interfaces. GRX, PM*, K1, B′(b), C1, uncapped KB, KBH, corrected Davenport-alpha, and RGR-LONG were accepted at the supplied scopes; their underlying proofs were treated as imports. No finite aid or Savchev–Chen assertion served as a premise. All **13 snapshot SHA256 pins matched** using static reads and hashes.