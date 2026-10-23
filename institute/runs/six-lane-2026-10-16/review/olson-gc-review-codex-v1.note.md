DISPOSITION: ACCEPT-WITH-FIXES

## FATAL

none

## MAJOR

none

## MINOR

1. **`P/c6/proof-GC.md:110` — qualify “every ZSI-B word.”**  
   The main theorem correctly assumes \(R\le2p-3\), but the parenthetical omits that restriction. Lemma ZSI-B itself has a wider domain (`P/proof-MH.md:102`).

   **Correct wording:** “in particular every item-(iii) word and every NMH word in the ZSI-B subfamily with \(R\le2p-3\).” Apply the same qualification at `P/c6/proof-GC.md:118`.

   **Hand example showing the scope difference:** take
   \[
   p=5,\quad k=6,\quad\kappa=2,\quad B=1,\quad
   (d_1,\ldots,d_6)=(3,-1,1,1,1,1).
   \]
   All runs are pure; reflection lengths \((5,1,1,1,1,1)\) give length \(18\), \(A=7\), \(R=8\), \(E=2\). Every proper interval of length \(n\) has
   \[
   D_Q\le n+2\le\min(2n+1,n+4),
   \]
   so this is ZSI-B, but \(R=8>2p-3=7\). For concreteness, \(t=2,Q=\{1\}\) gives \(D_Q=3=2|Q|+B\). This disproves the unqualified containment, not the identity-subword conclusion.

2. **`P/c6/proof-GC.md:16`, `P/c6/proof-GC.md:118` — two references violate the declared path convention.**  
   With paths relative to `mixdef-high/`, `../proof-MH.md` means `inverse-run-count/proof-MH.md`; the supplied file is `P/proof-MH.md`. Likewise, the parent-verdict reference beginning `institute/runs/…` does not resolve under that convention.

   **Corrections:** use `proof-MH.md` at LF118; identify the verdict as `review-notes/olson-c6-uniform-parent-verdict.md`, explicitly relative to **S**. Amend LF5 to allow this marked exception. These are path-resolution errors, with no mathematical counterexample involved.

The target hash matches the required pin. The six mathematical imports, two parent verdicts and three definition/context files checked also match their manifest hashes. Only file reads and SHA-256 checks were used; no controls were executed. Below, \(P\) has the meaning specified in the request.

## Q1 — GEN is an exact equivalence

The four comparisons at `P/c6/proof-GC.md:41` correctly say that each floor term is no larger than either competing term. Writing \(g=kB=\kappa-B\), doubling gives exactly
\[
\begin{array}{ll}
\text{(i)}&2m+y\ge2g+B+2-\theta,\\
\text{(ii)}&2m+y\le2p-B+\theta,\\
\text{(iii)}&2m-y\ge2\kappa+2-A-\theta',\\
\text{(iv)}&2m-y\le2p-A+\theta',
\end{array}
\]
where \(\theta=[y+B\text{ odd}]\), \(\theta'=[A-y\text{ odd}]\).

The parity elimination at LF46–49 is exact:

- If \(\theta=0\), \(2m+y\equiv B\pmod2\). Replacing the bounds \(2g+B+2,\,2p-B\) by \(2g+B+1,\,2p-B+1\) changes neither permitted endpoint.
- If \(\theta=1\), the replacement bounds already equal the original bounds.
- If \(\theta'=0\), \(2m-y\equiv A\pmod2\); the replacement endpoints similarly round inward to the original endpoints.
- If \(\theta'=1\), the bounds again coincide directly.

Thus genericity is **iff**
\[
2g+B+1\le2m+y\le2p-B+1,
\qquad
2\kappa+1-A\le2m-y\le2p-A+1.
\]
Both intervals have span \(2(p-\kappa)\), with centres
\[
p+g+1,\qquad p+\kappa+1-A.
\]
Consequently their centred coordinates \(a_1,a_2\) satisfy, using (1.1),
\[
a_1+a_2=4m-(k+2),\qquad a_1-a_2=2y-D.
\]
The identity
\[
2\max(|a_1|,|a_2|)
=|a_1+a_2|+|a_1-a_2|
\]
and \(2(p-\kappa)=E+2\Delta_0\) give precisely GEN (`P/c6/proof-GC.md:50`).

Complement symmetry at LF33–35 is also exact: proper complements have the same cyclic block count, and replacing \(y\) by \(D-y\) exchanges the two floor conditions.

The algebra works for every integer \(y\), including negative values, and every integer \(1\le m\le\lfloor k/2\rfloor\), provided the standing parameter identities hold. Equality cases are retained throughout. Empty/full patterns are correctly excluded. **No failing tuple was found.**

## Q2 — GC’s colouring construction and walk are valid

At `P/c6/proof-GC.md:67`, writing \(k=4q+r\),
\[
m=q+1,\qquad
\begin{array}{c|rrrr}
r&0&1&2&3\\ \hline
c&2&1&0&1
\end{array}
\]
which agrees with the stated table indexed by \(k+2\bmod4\). For \(k=7\), \(m=2\); for \(k\ge8\),
\[
2m\le(k+4)/2\le k-2.
\]
Thus \(m\ge2\) and the final initial block has length at least two.

Deleting \(t\) leaves a path whose endpoints \(t+1,t-1\) are not adjacent. Hence each colour’s path blocks are exactly its cyclic blocks. Both colours have \(m\) nonempty blocks, so
\[
Q=X,\quad t\notin Q,\quad Q+t=[k]\setminus Y
\]
are proper. Complement symmetry legitimately tests genericity of \(Q+t\) through \(Y\), and
\[
D_X+D_Y=D-d_t
\]
(`P/c6/proof-GC.md:60`).

The explicit exchanged colouring has block lengths
\[
\chi^*:\quad
(2,\underbrace{1,\ldots,1}_{2m-3},L-2m,1).
\]
Therefore
\[
b_j^*=j+1\quad(1\le j\le2m-2),\qquad
b_{2m-1}^*=L-1.
\]
This verifies membership in \(C\). Colour exchange complements \(X\) among the other runs; the endpoint corrections add \(d_{t+1}\) and subtract \(d_{t-1}\). Hence
\[
v(\chi_0)+v(\chi^*)=D-d+d_{t+1}-d_{t-1},
\]
exactly (3.2), LF80.

In the raising pass, the right boundary is already at least its final value, so strict order is preserved; the unchanged left boundary remains smaller. A lowering pass would preserve order because its left boundary is final and its right boundary remains larger. For these particular endpoints, however, **every coordinate increases**, so the second pass is empty. Each unit move recolours exactly one position and preserves both endpoint colours and all \(2m\) nonempty blocks (`P/c6/proof-GC.md:82`).

Neither TS nor GS requires isolation: their hypotheses are precisely properness, \(t\notin Q\), and properness of \(Q+t\) (`P/c6/proof-SEEDG-r2.md:71`, `:89`). Indeed this construction always has \(t+1\in Q\).

## Q3 — Window, bounds and crossing are correct

Intersecting
\[
|2v-D|\le W',\qquad |2(D-d-v)-D|\le W'
\]
gives exactly
\[
\mathrm{lo}=\left\lceil\frac{D-W'}2\right\rceil+\max(0,-d),
\qquad
\mathrm{hi}=\left\lfloor\frac{D+W'}2\right\rfloor-\max(0,d)
\]
(`P/c6/proof-GC.md:73`).

If \(\varepsilon=[D-W'\text{ odd}]\), then
\[
\mathrm{hi}-\mathrm{lo}+1=W'-|d|+1-\varepsilon\ge W'-|d|.
\]
In the actual NMH setting, \(\varepsilon=0\): \(E\) is even and
\[
D\equiv\Delta_0\equiv k\equiv c\equiv W'\pmod2.
\]
Thus both \(D-W'\) and \(D+W'\) are even. The proof’s weaker rounding bound remains valid.

For (S), if the target is pure,
\[
e_t=|d|-1,\qquad |d_a|\le E-e_t+1=E+2-|d|.
\]
For a pair, \(d=0,e_t=1\), giving \(|d_a|\le E\). Since \(W'\ge E+4\), both imply the claimed step bound. Moreover \(W'-|d|\ge3\) for pure targets, and is positive for pairs, so the window is nonempty (`P/c6/proof-GC.md:90`).

For (M), put \(h=d_{t+1}-d_{t-1}\). Distinctness of the three runs gives
\[
|d|+|h|
\le |d|+|d_{t+1}|+|d_{t-1}|
\le E+3\le W'.
\]
Writing \(\Sigma=D-d+h\), the two needed comparisons reduce to
\[
W'\ge |d|-h,\qquad W'\ge |d|+h.
\]
Both follow, for every sign of \(d\), establishing (3.3), LF93–95.

The crossing argument is valid without monotonicity of \(v_i\). For example, \(v_0<\mathrm{lo}\) and \(2\mathrm{lo}\le\Sigma+1\) force \(v_N\ge\mathrm{lo}\). At the first crossing, the preceding integer is at most \(\mathrm{lo}-1\); a step of at most \(\mathrm{hi}-\mathrm{lo}+1\) lands at most at \(\mathrm{hi}\). The upper crossing is symmetric (`P/c6/proof-GC.md:97`).

Here are explicit hand checks. Notation \(1^n\) means \(n\) consecutive weights \(1\); zero denotes a \((1,1)\)-pair.

| \((p;k,\kappa,B,E)\) | Cyclic weights; target; pattern | \(D,W';[\mathrm{lo},\mathrm{hi}];v\) |
|---|---|---|
| \((5;7,2,1,0)\) | \((-1,1^6)\); \(t=1\); \(Q=\{2,4\}\) | \(5,5;[1,5];2\) |
| \((7;8,2,1,2)\) | \((0,2,1^6)\); \(t=1\); \(Q=\{2,4,6\}\) | \(8,8;[0,8];4\) |
| \((7;9,3,2,2)\) | \((-2,2,1^7)\); \(t=1\); \(Q=\{2,4,6\}\) | \(7,7;[2,7];4\) |
| \((7;10,3,1,0)\) | \((-1,1^9)\); \(t=1\); \(Q=\{2,4,6\}\) | \(8,8;[1,8];3\) |
| \((11;12,3,1,4)\) | \((-1,5,1^{10})\); \(t=2\); \(Q=\{3,5,7,9\}\) | \(14,14;[0,9];4\) |

These realize actual NMH run structures: choose reflection lengths
\[
(2(p-1-\kappa)+1,1^{k-1}).
\]
They cover pure anti, pair and pure aligned targets, \(E=0\), and \(E\ge4\). At \(p=5\), the first row is the only scalar class. At \(p=7\), \(E\le3\) and even, so all scalar possibilities are
\[
(E;k,\kappa)=(0;9,2),(0;10,3),(0;11,4),(2;8,2),(2;9,3),
\]
with \(1\le B\le\kappa-1\). These include every residue of \(k\bmod4\).

A nontrivial crossing occurs for
\[
p=7,\ k=11,\ \kappa=4,\ B=3,\ E=0,\quad
d=(1,-1,1,-1,1,-1,1,1,1,1,1),\quad t=1.
\]
Here \(D=5,W'=5,[\mathrm{lo},\mathrm{hi}]=[0,4]\), and \(Q_0=\{2,4,6\}\) has \(v_0=-3\). The first three moves give \(-2,-1,0\), reaching
\[
Q=\{2,4,6,7,8,9\}.
\]
Its GEN value is \(1+|0-5|=6=E+2\Delta_0\), so the boundary equality is valid.

Finally, the exact full walk length is
\[
N=(2m-2)+(L-2m)=L-2=k-3.
\]
The second pass is never used. Thus Remark (3), LF105, is correct for a fixed target: the walk is linear, and \((2m-1)(L-2)\) is a valid loose bound. Repeating the construction separately for all targets gives \(O(k^2)\) moves.

## Q4 — The accepted imports apply inside their hypotheses

The target’s definition of generic agrees exactly with GS(b), including **both** floor equalities (`P/c6/proof-GC.md:33`; `P/c6/proof-SEEDG-r2.md:93`). No isolation, special block transition or count condition is required. GS(b) supplies the quality bounds on \(s_{\rm lo},s_{\rm hi}\); NW supplies precisely
\[
\lambda(\{t\})-s_{\rm hi}>-p,\qquad U(\{t\})-s_{\rm lo}<p,
\]
which are GS(a)’s hypotheses (`P/c6/proof-SEEDG-r2.md:80`, `:91`).

The actual-empty alternative is essential and is used correctly at `P/c6/proof-GC.md:113`. An empty interval is not a seed under the Definition, but its actual configuration forces the contradiction directly.

For an explicit check, take
\[
p=7,\ k=9,\ \kappa=3,\ B=2,\ E=2,\quad
d=(-2,2,1^7),\quad t=2,\quad Q=\{3,5,7\}.
\]
Here \(A=9,D=7,\Delta_0=3,m=3\). Direct calculation gives
\[
(\lambda(Q),\lambda(Q^c))=(3,4),\qquad
(\lambda(Q+t),\lambda((Q+t)^c))=(4,3).
\]
Both patterns are generic. Therefore \(s_{\rm lo}=s_{\rm hi}=1\), whereas the singleton canonical interval is \([2,3]\). The actual GS intersection is \([2,1]\), empty: an avoider would require \(x_t=1\) and \(x_t\ge2\). This is the accepted actual-configuration exclusion, not an inference from an empty QS window alone.

All standing hypotheses needed by the imports hold:

- NMH membership supplies length \(4p-2\), prime \(p\ge5\), \(p+1\le k\le2p-2\), normalization \(B\le A\le2p-1\), and \(1\le B\le\kappa-1\).
- All reflection runs are odd, hence \(\beta=0\); rotation runs are pure or \((1,1)\)-pairs.
- \(R\le2p-3\) gives \(\Delta_0\ge3\) and
  \[
  k=2\kappa+\Delta_0\ge2\kappa+3\ge7.
  \]
- Also \(E\ge0\) is even and \(E\le p-4\), as required by the imported run bounds.

These are stated or incorporated at `P/c6/proof-GC.md:24`, `:28`, `:109`, with the full setting at `P/c6/proof-SEEDG-r2.md:41`.

If no actual interval is empty, GC and GS provide a nonempty quality seed from an actual configuration at **every** run. Under hypothetical avoidance, canonical lifts exist uniquely by P0/ARC. SCW-G certifies every proper pattern; SL gives its bounds; the pin step places
\[
X_{[k]}\in[1,2p-1],\qquad X_{[k]}\equiv0\pmod p,
\]
hence \(X_{[k]}=p\) (`P/c6/proof-SEEDG-r2.md:66`, `:103`, `:152`). Thus the lifts satisfy (L).

The A0 Corollary’s cases (a)/(b) now apply exactly (`P/c6/proof-A0-r1.md:92`). Its C0-all finisher needs no count condition or defect bound. C0W is invoked only in C0-all’s case
\[
B\ge g+1,\qquad 3g+1\le p,
\]
matching C0W’s accepted scope (`P/c6/proof-A0-r1.md:81`; `P/c6/proof-C0WB-r2.md:55`). The relevant acceptance is explicit in `review-notes/olson-c6-uniform-parent-verdict.md:11`, `:14`, `:17`.

## Q5 — Scope and premises

After MINOR 1’s qualification, the conclusion is exactly all normalized NMH words with \(R\le2p-3\), comprising item (iii) and its complementary ZSI-B portion, for every prime \(p\ge5\).

The title, LF4–6, import list and LF109–116 respect that scope. LF121–124 gives a conditional assembly statement, not an assertion of NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR, INV, INV* or ordered Olson. This audit does not certify that assembly.

Remark (1), LF103, operates within §1’s standing identities and run budgets; those remain explicitly used in (S)/(M). It correctly imposes no additional region restriction. Remark (2)’s non-isolation claim is correct. Remark (3)’s linearity is verified above.

No census, finite control, E2 table or region theorem is a premise: LF5, LF18–20, LF119–121 and §5 expressly separate them. All operative mathematical imports are present in S. The intentionally excluded non-premise files need not be imported; the two mis-based references are addressed in MINOR 2.

**Counts: FATAL 0 / MAJOR 0 / MINOR 2.**

The proof is mathematically correct at the specified scope, relative to the accepted imports. Novelty and priority were not assessed. Its significance is the uniform actual-configuration construction completing this NMH residual; broader theorem assembly remains separate.