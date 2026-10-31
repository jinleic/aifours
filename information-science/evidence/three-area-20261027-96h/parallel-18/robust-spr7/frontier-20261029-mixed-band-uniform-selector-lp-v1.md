# An exact LP for a uniform mixed-band Vieta selector

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:57:47 PDT 2026**. **WRITTEN exact fixed-data characterization**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It isolates a sufficient uniform construction for one minimal-support band pattern; no all-parameter LP verdict is asserted.

## 1. Fixed data and the uniform property

Fix an admissible independent odd coefficient box with root bands \([a,b],[c,d],[e,f]\), and five distinct positive nodes
\[
a<t_1<t_2<b<t_3<t_4<c<t_5<d. \tag{1}
\]
The fifth node lies in the second odd band. The odd moment signs force every nonzero positive circuit on these five finite nodes plus infinity to use the first two nodes with signs \(-,+\), the fifth with sign \(+\), and one of the negative-sign middle nodes \(t_3,t_4\). Call these rays X and Y, respectively.

For \(\theta\in[0,1]\), define
\[
\xi=(1-\theta)t_3+\theta t_4,\qquad F_\theta(t)=(-t)(\xi-t)(d-t). \tag{2}
\]
Its middle root is in the Vieta gap \([b,c]\); thus \(F_\theta\) is a convex combination of the two closed Vieta vertices with root triples \((0,b,d)\) and \((0,c,d)\).

The **uniform-selector property** is: some single \(\theta\) makes the even pairing of **each** of X and Y strictly positive for every all-Hurwitz even coefficient box paired with the fixed odd box, for every choice of actual member at each node and all permitted odd values. This property excludes every weak no-go on the support, but it is stronger than necessary: a box-dependent selector or a positive mixture of circuits might work even when no such uniform selector does.

## 2. One linear program

Write even interval variables \(\ell_k,u_k\), \(k=0,1,2,3\), for \(a_{2k}\), and use the six strictly positive stability forms
\[
S=(-E_+(a),-E_+(b),E_-(c),E_-(d),-E_+(e),-E_+(f)),
\]
four nonnegative widths \(W_k=u_k-\ell_k\), and four strictly positive lower coefficients \(\ell_k\). These 14 forms define exactly the stable even-box cone for the fixed odd box, by the six-endpoint sign criterion in `frontier-20261029-fixed-odd-box-certificate-lp-v1.md`, SHA-256 `b3a0945ac3b11e837a8692566ad0e385a0b8658310245f7388b84a2347e5de52`.

For each ray and each middle odd endpoint \(O_-,O_+\), normalize the infinity atom weight to 1, use odd extrema \(O_-(t_1),O_+(t_2),O_+(t_5)\) at the other nodes, and form the **mixed-envelope** pairing functional \(g_r^{\pm}(\theta)\). At \(t_1,t_2\) use \(E_+\), at \(t_5\) use \(E_-\), at \(t_3\) in ray X use \(E_+\), and at \(t_4\) in ray Y use \(E_-\). These are the correct minima because \(F_\theta\le0\) at X's middle node and \(F_\theta\ge0\) at Y's middle node. Each \(g_r^{\pm}\) is an eight-coordinate linear form in \((\ell,u)\), affine in \(\theta\); its fixed atom weights are the Lagrange weights \([t_iO_i(t_i)H'(t_i)]^{-1}>0\).

Seek \(\theta\), \(\delta\), and four independent sets of 14 dual multipliers satisfying
\[
\begin{aligned}
&0\le\theta\le1,\qquad \delta>0,\\
&g_r^{\pm}(\theta)=\sum_{j=1}^6\alpha_{rj}^{\pm}S_j
+\sum_{k=0}^3\beta_{rk}^{\pm}W_k+\sum_{k=0}^3\gamma_{rk}^{\pm}\ell_k,\\
&\alpha,\beta,\gamma\ge0,\qquad
\sum_{j=1}^6\alpha_{rj}^{\pm}+\sum_{k=0}^3\gamma_{rk}^{\pm}\ge\delta
\quad\text{for each of the four cases}.\tag{3}
\end{aligned}
\]
Equality of linear forms means eight scalar coefficient equalities. Since the data and all Lagrange weights are fixed, (3) is a finite **linear** feasibility problem in \(\theta,\delta\) and the dual multipliers. For rational odd coefficients and rational nodes it is an exact real-algebraic LP, rational when the odd-band endpoints are rational.

**Theorem.** System (3) is feasible if and only if the uniform-selector property of §1 holds for the restricted family (2). A feasible LP is a constructive no-go exclusion: its \(\theta\) and four dual identities certify positive pairings on both odd rays for every admissible even box and actual atom choice. An infeasible LP merely says this particular uniform selector family fails; it is **not** a no-go witness or a global SPR verdict.

## 3. Proof of equivalence

At nodes 1 and 2, every even component is negative and \(F_\theta<0\), so the positive contributions are minimized by the largest magnitudes of their required negative/positive odd values, namely \(O_-\) and \(O_+\). At node 5, both the actual even value and \(F_\theta\) are positive, so \(O_+\) minimizes its positive contribution. At the middle node the odd value is strictly negative for both endpoints; the dependence on its reciprocal is affine, so its minimum lies at \(O_-\) or \(O_+\). Independent actual members may be chosen separately at the four nodes. Thus the four mixed-envelope functionals are exactly the relevant worst cases, not merely a heuristic sample.

If (3) holds, each \(S_j,\ell_k\) is strictly positive and each \(W_k\) nonnegative for a stable box, so every \(g_r^{\pm}>0\); endpoint minimization and the mixed-envelope inequalities give the uniform property.

Conversely, fix a \(\theta\) with the uniform property and one ray/odd-endpoint case. Its mixed-envelope functional is strictly positive on the nonempty cone defined by \(S>0\), \(\ell>0\), \(W\ge0\). The finite-dimensional **Motzkin strict linear alternative** gives a representation by nonnegative multiples of these forms with at least one coefficient on a strictly positive form. The stable even-box cone is nonempty: choose any even cubic with roots in the three gaps and a sufficiently small positive-width neighborhood. Applying the alternative separately to the four cases and taking the minimum of the four positive strict-generator sums yields one \(\delta>0\). Therefore (3) holds.

## 4. Nonvacuity and gap

At odd root endpoints \((1,4,7,13,20,24)\) and nodes \((2,3,5,6,8)\), the selector \(\theta=1/2\) has four explicit strictly positive rational dual identities in `frontier-20261029-mixed-band-strict-duals-frozen-v1.json`, SHA-256 `c8dc14446d0bd35a444759948e737675698feed0856ed98ea96f615d0f5359a3`. Their explicit perturbation neighborhood is proved in `frontier-20261029-open-mixed-band-five-node-exclusion-v1.md`, SHA-256 `ebe067ec9a558dff53d5fcec48ad8f8b897845c69aa14f07d8ceb8a556021133`. These are author-written imports, with the stated finite exact checks, not independent acceptance.

The genuinely open step is to prove (3) feasible for **every** admissible odd box and node tuple satisfying (1), or exhibit a tuple where this restricted selector property fails. Neither outcome is established. Even a universal positive answer to this particular pattern would not settle the other minimal phase words or larger supports.

Named imports: Hermite–Biehler interlacing, odd-circuit Vandermonde interpolation, and Motzkin's strict linear alternative. The LP construction and proof are written mathematics; no solver was run to establish its universal feasibility. No original verdict, formal proof, independent scientific review, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
