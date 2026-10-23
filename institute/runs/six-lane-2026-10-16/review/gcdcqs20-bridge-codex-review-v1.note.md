VERDICT: BRIDGE-HOLDS

**Fatal findings: none. Major findings: none. Minor qualifications:** order 80 requires Construction 2.1 separately, and the source defers an unused congruence case to another reference.

All line references below are LF lines in the [supplied text](/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt). I accepted the stipulated gcDCQS without re-verifying it and opened nothing under `mathematics/evidence/`.

1. **Corollary 2.6 applies with \(m=20\).**

   Its hypotheses and conclusion appear at **lines 684–685**. Every input is satisfied:

   - \(20\equiv8\pmod{12}\).
   - The required \(\operatorname{gcDCQS}(20^4:0)\) is the assumed input.
   - **Lemma 3.4, lines 903–907**, asserts an mcDSQS(20). Specifically, **line 905** attributes its minimum colourability to **[16]**, applied to the cyclic SQS(20) constructed in **[14]**. Reference [16] is M. Shi, Y. Xia and D.S. Krotov, *A family of diameter perfect constant-weight codes from Steiner systems*, J. Combin. Theory (A) **200** (2023), 105790 (**lines 1166–1167**). Reference [14] is Phelps’s cyclic SQS(20) paper (**line 1161**).
   - Theorem 2.5(1), **line 680**, supplies \(2\)-RSQS\(^*(4^n)\) for every integer \(n\ge2\), citing [21, Corollary 3.2].
   - Theorem 2.5(2), **lines 682–683**, requires
     \[
     \gcd(m,4)\ne2,\qquad \gcd(m,18)\ne3.
     \]
     Here these gcds are respectively \(4\) and \(2\), so both conditions hold. The extraction’s `6=` means \(\ne\), confirmed in the [original arXiv HTML](https://arxiv.org/html/2503.11934v1).
   - Construction 2.4 additionally requires \(4m+s\equiv2,4\pmod6\), which holds because \(80\equiv2\pmod6\) (**lines 568–572**). Its use of \(m/2\) also poses no issue.

   Construction 2.4 produces \(\operatorname{gcDCQS}(20^{\,4^n}:0)\); filling then gives
   \[
   \operatorname{mcDSQS}(20\cdot4^n),\qquad n\ge2,
   \]
   starting with **320, 1280, 5120, …** (**lines 687–693**).

   This is exactly Section 4(2), **lines 1111–1112**: putting \(k=n+1\) gives \(20\cdot4^n=5\cdot4^k\), with \(k\ge3\). **Corollary 2.6 itself does not assert order 80.**

2. **Construction 2.1 separately gives an mcDSQS(80).**

   The three required inputs are stated at **lines 292–293**. Under the definitions, **gcDSQS(20,0) is precisely mcDSQS(20)**: with \(H=\varnothing\), the SQS hole condition becomes ordinary triple coverage, every point lies outside \(H\), and the conditions for points inside \(H\) are vacuous (**lines 227–236**, compared with **127–130**). No design with a negative hole size must be constructed.

   Fill each of the four groups with a relabelled copy of the known mcDSQS(20). The CQS covers triples outside individual groups, and the fillings cover triples inside groups, without overlap (**lines 256–266; 304–322**).

   Fix \(x\in G\). Relabel the assumed forty classes so that \(P_x^1,\ldots,P_x^{10}\) avoid \(G\setminus\{x\}\). The filled group contributes an mcSTS(19), with ten classes \(Q_x^1,\ldots,Q_x^{10}\), since \(\chi'(19)=10\) by **(1.1), lines 110–125**. The resolution prescribed at **lines 321–326** becomes
   \[
   \{P_x^j\cup Q_x^j:1\le j\le10\}
   \;\cup\;
   \{P_x^j:11\le j\le40\}.
   \]
   Each merged class is a PPC because its two parts have disjoint supports. These forty classes partition all \(970+57=1027\) derived triples.

   Their optimality also follows directly: an STS(79) has 1027 triples, and a PPC contains at most \(\lfloor79/3\rfloor=26\), so at least
   \[
   \left\lceil1027/26\right\rceil=40
   \]
   classes are necessary. Thus every derived design is minimum colourable, consistent with \(\chi'(79)=40\) in (1.1).

3. **No additional compatibility hypothesis is missing.**

   The relevant derived hole is exactly \(G(x)\setminus\{x\}\), of size 19; its GDD type is \(1^{60}19^1\) (**lines 211–215; 281–288**). The stipulated input supplies that hole and the required ten classes avoiding it.

   \(G_0\) is arbitrary (**lines 304–308**). With an empty stem, all four groups receive ordinary mcDSQS(20) fillings. The colourings can be chosen independently at each derived point; the definitions require no common colouring across points.

   **Minor source qualifications:** Construction 2.1 defers the \(gn+s\equiv4\pmod6\) case to [3] (**lines 295–296**). Every order used here is \(2\pmod6\), so the displayed proof covers this bridge. Its stem-point clauses (**lines 302–303, 310–315, 328–333**) are vacuous when \(s=0\); no step requires \(s\ge1\). Corollary 2.6 explicitly sets \(s=0\) (**line 687**).

   The exceptional derived orders 7 and 13 must also be excluded when using the displayed class counts. Here the local order is 19 and the completed derived orders are at least 79, so neither exception occurs. The source flags this issue at **lines 701–705**.

4. **The code consequence is the exact equality \(q'_0(3,4,80)=41\).**

   Theorem 1.3, **lines 177–182**, states
   \[
   q'_0(3,4,v)
   =1+\min_{S\text{ an SQS}(v)}
       \max_{D\in S'}\chi'(D).
   \]
   Corollary 1.4(1), **lines 186–187**, states that for \(v\equiv2\pmod6\), \(v\ge20\), existence of an mcDSQS(\(v\)) implies
   \[
   q'_0(3,4,v)=v/2+1.
   \]
   Consequently the mcDSQS(80) gives **\(q'_0(3,4,80)=41\)**. By the definition at **lines 170–174** and Theorem 1.2(1), **lines 157–162**, this yields a diameter-perfect constant-weight code
   \[
   (80,\tfrac14\binom{80}{3},6;4)_{41}
   =(80,20540,6;4)_{41},
   \]
   with 41 the minimum alphabet size for those parameters.

Under the assumed gcDCQS input, mcDSQS(80) and mcDSQS(\(20\cdot4^n\)) for every \(n\ge2\) follow. The bridge has no unresolved hypothesis.