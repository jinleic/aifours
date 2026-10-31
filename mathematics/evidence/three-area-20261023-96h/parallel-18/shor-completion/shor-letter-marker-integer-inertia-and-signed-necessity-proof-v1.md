# Shor RAW finite candidates — a complete letter-marker proof of INTEGER signed-factor necessity

Owner **MathShor-2**. Actual preceding `/bin/date`: **Mon Oct 26 09:33:21 PDT 2026** (earlier actual observation bound). **NEW WRITTEN / UNREVIEWED source-proof reconstruction**, not a novel factorization theorem, completion decision or formal proof. All variables remain symbolic; no new chosen code/state/control/numeric parameter, magnitude/decimal probe, scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/CLI/nested agent or GO.

Prospective authority is the SAME whole ACK52 WRITTEN+SENT after ACTUAL v127-A RETURN and Main's explicit v56 direction, ACTUALLY read WHOLE before primary source/proof. All FOUR own process MAJORs and v49 PRECISE provenance blocker remain permanent. ENTIRE withdrawn Taylor/control/coefficient/scout guidance is ZERO; no mining/repair/retest/replay/backconversion or timestamp-only independence claim. The proof below is noncommutative polynomial/module algebra applied to the actual raw b-marker identity, NOT a Taylor/coefficient-route repair or an abstract adjunction replacing the original target.

## 1. Exact new scope and positive prior/source boundary

Let M be ANY finite RAW UD factor-complete code over{a,b} containing the fixed letter b, and X its characteristic polynomial. No order, length, b-count, gap, delay, arity or unknown added-word restriction is imposed.

**Theorem — WRITTEN candidate.** There exist FINITE polynomials P,S in Z<a,b>, possibly SIGNED, such that

    X-1=P(a+b-1)S,
    P(0,b)=S(0,b)=1.

If a^n is the unique pure-a codeword, then also

    P(a,0)S(a,0)=1+a+...+a^(n-1).

This proves the signed-necessity interface for the ENTIRE class of possible original Shor completions, because the literal C contains b. It does NOT assert that P,S are nonnegative; that would substitute the open positive-factorization conjecture. It does not prove existence of P,S whose output contains C, exclude ALL signed factors, supply a finite code, or settle original completion.

Positive PRIOR: Reutenauer1985 signed factorization is already the named I5 theorem in the earlier packets. The actual academic-hosted April9,2010 draft of Berstel–Reutenauer, *Noncommutative Rational Series With Applications*, is now read at

    http://www-igm.univ-mlv.fr/~perrin/Livres/RationalSeries9April2010.pdf

The relevant draft numbering is Chapter10 Theorem1.1, Theorem3.1/Corollaries3.2–3.3, Gauss Theorem4.1/Corollary4.3/Proposition4.4, and Chapter11 Theorem4.1/Corollary4.2. It is NOT silently identified with publisher-preview Theorem5.5 numbering or the survey's Theorem2.1 numbering. Theorem11.4.1's full proof/end and Chapter11 notes were actually read; the general degree/minimal-ideal index ancestry is not independently reconstructed here. The ORIGINAL1985 article is not newly read/authenticated. This packet supplies an independent conventional proof of the SPECIALIZED b-containing necessity actually needed, using the elementary lemmas proved below.

## 2. Actual b-marker supplies a finite positive RESET identity

Let L be M's maximum word length. UD and b in M forbid every other pure-b codeword. Any cut with L b's on both sides is therefore a codeword boundary in any actual M-parse: a crossing word of length<=L would be a forbidden pure-b word of length>=2. Completeness applied to b^(2L) w b^(2L), followed by the two central marker cuts, gives b^L w b^L in M* for EVERY raw w.

Define FINITE actual languages R,T,H as follows. R consists of the empty word and suffixes r with b^i r in M for some i>=1; T is the empty word and the mirrored prefixes t with t b^j in M; H consists of isolates h with b^i h b^j in M, i,j>=1, with the deleted pieces disjoint. Empty R/T is counted once. H has no empty word, since that would require a pure-b codeword longer than b.

Examine the unique parse of b^L w b^L at the two cuts immediately surrounding w. If both lie strictly inside the SAME word, w is an H-isolate. Otherwise the first/last fragments and intervening whole words give w=r m t with r in R,m in M*,t in T. Conversely each such isolate/triple can be padded into the same sandwich using the defining crossing word(s) and standalone b's. Any duplicate representation or different b-delay occurrence would give distinct M-word lists for that SAME sandwich, violating UD. Thus the FULL noncommutative identity is positive and unambiguous:

    (a+b)*=R(1-X)^(-1)T+H,
    R(empty)=T(empty)=1, H(empty)=0.                     (RESET)

This actual raw proof retains all words and all internal gaps. It neither assumes I5 nor invokes a residue synchronizer. R,T,H are their characteristic polynomials. Put Y=a+b-1. Formal inversion on the correct sides of RESET gives

    X-1=T(1+YH)^(-1)Y R.                               (INV)

All four polynomials T,1+YH,YR,X-1 are nonzero, and the denominator has constant1. The remaining issue is to turn this actual INTEGER rational cancellation into finite INTEGER factors, without a positivity conjecture. Sections3–6 do that completely.

## 3. Polynomial degree reduction: the exact weak-division lemma

Work first over ANY field K and the free polynomial algebra K<A>. Degree is word length, deg0=-infinity, and deg(PQ)=degP+degQ for nonzero factors. Right word quotient is (P w^(-1),v)=(P,vw). It satisfies

    deg(P w^(-1))<=degP-|w|,
    (PQ) x^(-1)=P(Q x^(-1))+(Q,empty)P x^(-1)

for a letter x. Induction on |w| consequently gives

    (PQ) w^(-1)=P(Q w^(-1))+E,
    degE<degP                                               (RQ)

when P is nonzero; P0 is trivial.

A finite family P_i is right degree-dependent if a nontrivial combination sum_i P_i Q_i has degree below max_i deg(P_i Q_i). Order degP_1<=...<=degP_s. Let r be that maximum, I the indices attaining it, and k the LARGEST index in I. Their top-degree sum R0 has degree<r. Choose a highest-degree word w of Q_k with nonzero coefficient lambda. Then Q_k w^(-1)=lambda, and RQ applied to each top term gives

    P_k+lambda^(-1)sum_(i in I, i!=k)P_i(Q_i w^(-1))
       =lambda^(-1)[R0 w^(-1)-sum_i E_i].

The right side has degree<degP_k, since |w|=degQ_k and degP_i<=degP_k for i in I. Every displayed reduction term has degree<=degP_k. Thus SOME member is reducible by earlier ones. This is the needed weak algorithm, reconstructed directly; no external Cohn theorem is used as an unproved research premise.

**Weak-division consequence.** If Y is a nonzero polynomial, Q is nonzero, degE<=degQ, and

    P Q+E=Y Z+R0, degR0<degY,

then P=Y U+R with degR<degY. If Y is constant or degP<degY this is immediate. Otherwise degP>=degY>=1 makes both E and R0 lower degree than PQ; hence P,Y are degree-dependent. Put Y first and P second in the weak algorithm, obtaining P=YU1+P1 with degP1<degP. Substitute this expression in the displayed relation and apply induction to P1. This proves the consequence with ALL hypotheses, including its nonzero-factor conditions, explicit.

## 4. A cancellative-module proof of the TWO-BY-TWO rational-cancellation factorization

For polynomial columns in K<A>^m, let E be a right submodule with the property:

    V in E and V(empty)=0  => V x^(-1) in E
    for EVERY letter x.                                 (CANCEL)

Then E is generated by p<=m polynomial columns V1,...,Vp whose constant columns are linearly independent over K. Here is the complete finite-generation proof. Let F_d be the constant columns of members of E having degree<=d. These are nested subspaces of K^m. Choose a basis adapted to all their finitely many strict dimension jumps, and lift each basis column at its first-occurrence degree to a polynomial Vi in E. For ANY V in E of degree d, its constant column is a combination of lifts with degree<=d. Subtract that constant combination; the result has constant0 and degree<=d. By CANCEL, each right letter quotient is in E and has degree<d. Induction expresses those quotients in the Vi, and summing their products with the last letters reconstructs V. The zero-degree/zero-column cases are included. Thus these p lifts generate E and their constants are independent.

Now let a nonzero formal-series row s annihilate a square polynomial matrix M. The polynomial-column kernel E={V:sV=0} satisfies CANCEL: if all constant coordinates of V vanish, the right-quotient product rule has no extra term, so s(Vx^(-1))=0. Choose the above generators. They cannot have p=m, because their square column matrix would have invertible constant matrix and hence an inverse as a formal-series matrix, forcing s0. Thus p<m and M factors through those p polynomial columns.

Apply this with m=2 to nonzero polynomials P1,P2,P3,P4, P2 formally invertible, and P1 P2^(-1) P3=P4. The nonzero row(1,-P1 P2^(-1)) annihilates

    [[P1,P4],[P2,P3]].

The kernel generation has p<2; the matrix is nonzero, so p=1. Therefore there are NONZERO polynomials q1,q2,q3,q4 over K such that

    P1=q1q2, P2=q3q2, P3=q3q4, P4=q1q4.               (FIELD)

This is the exact factor pattern needed, with correct noncommutative sides. No free-field inversion, general inertia theorem, module-freeness citation or unprovided infinite algorithm is a premise.

## 5. Gauss/content makes ALL FOUR factors INTEGER

For a nonzero rational free polynomial q let c(q)>0 be its rational content, so q/c(q) is a primitive INTEGER polynomial. Products of primitive polynomials are primitive: otherwise some prime would kill their product after reduction to a free algebra over a prime field, which is an integral domain, so that prime would kill one primitive factor. Hence c(qr)=c(q)c(r).

Apply FIELD over Q to INTEGER P1,...,P4. Put m_i=c(P_i), positive integers. Their contents satisfy

    m1*m3=m2*m4.

Let d2=gcd(m1,m2), d1=m1/d2, d3=m2/d2. Coprimality of d1,d3 and the preceding equality imply d3 divides m3; put d4=m3/d3. Then

    m1=d1d2, m2=d3d2, m3=d3d4, m4=d1d4.

Write q_i=c(q_i) qbar_i with qbar_i primitive integer. Setting R_i=d_i qbar_i yields the COMPLETE INTEGER factor pattern

    P1=R1R2, P2=R3R2, P3=R3R4, P4=R1R4.               (INTEGER)

No rational coefficient is rounded or evaluated, and no positive-coefficient conclusion is asserted. The proof handles every possible coefficient sign through the primitive factors themselves.

## 6. Primitive linear extraction with the exact right ideal

Let Y be primitive of degree1 and have an integral zero. Suppose integer P,Q obey PQ=YZ+alpha with a nonzero integer alpha. The weak-division consequence, with constant error -alpha and nonzero Q, gives

    P=YU+beta, degbeta<1,

initially over Q. Thus beta is a scalar. It cannot be0, since Y cannot divide the nonzero scalar alpha by degree. Substitution then gives Q=YV+gamma with beta*gamma=alpha. Evaluate at ANY integral zero of Y: P,Q have integer values there, so beta,gamma are integers. Finally YU=P-beta has integer coefficients; content multiplicativity and primitivity of Y make U integer (or U0 trivially). Likewise V is integer. Thus

    P≡beta, Q≡gamma mod Y Z<A>, beta*gamma=alpha.        (LINEAR)

All congruences use the RIGHT ideal Y Z<A>; no invalid two-sided quotient ring is substituted. The proof applies to Y=a+b-1, which is primitive and has an integral zero by its unit letter coefficients. No selected noise/state/control evaluation is involved: this is the algebraic source hypothesis, used for ALL such linear polynomials/integral zeros.

## 7. Apply INTEGER and LINEAR to the ACTUAL marker identity

Apply INTEGER to INV with P1=T,P2=1+YH,P3=YR,P4=X-1. Obtain finite INTEGER A,B,C,D with

    T=AB, 1+YH=CB, YR=CD, X-1=AD.

The second relation says CB≡1 mod Y Z<a,b>. LINEAR therefore gives C=eta+YU with eta in{+1,-1} and U integer. The third relation gives

    YR=(eta+YU)D,
    D=Y[eta(R-UD)].

The bracket is a FINITE integer polynomial, since every displayed factor already is. Define P=A and S=eta(R-UD). Then X-1=P Y S, proving signed necessity without a positive-factorization assumption, general code-degree theorem or an unread original1985 proof as a correctness premise.

Specialize only the existing factor identity to the pure-b part. Actual X(0,b)=b and Z[b] is an integral domain, so

    (b-1)P(0,b)S(0,b)=b-1
    => P(0,b)S(0,b)=1.

Its two integer polynomial units are simultaneous equal signs. Replace P,S by their opposites if needed to make BOTH1. For the unique pure-a word a^n, the same identity and cancellation of a-1 give P(a,0)S(a,0)=1+a+...+a^(n-1). This is the known source-fixed normalization, NOT the quarantined new Taylor/coefficient route and not a count/repair of the withdrawn seed-polynomial manuscript.

## 8. Exact original implication, source-reading limits and remaining gap

The earlier signed-factor packets used I5 as a NAMED/NOT_RECONSTRUCTED necessity import. This NEW packet gives a COMPLETE specialized conventional proof at the actual b-marker interface, including the polynomial degree/module/Gauss/primitive-linear steps previously left named. It is a CANDIDATE import discharge for ALL possible original completions, not automatic adoption or retroactive acceptance of every downstream TOP/BAL/NEG/one-sided result. A fresh ENTIRE joint gate must assess the proof and any composition before their assurance is promoted.

Together with the separately supplied self-contained signed-certificate forward proof, it would provide a self-contained necessary-and-sufficient signed-polynomial representation for THIS original letter-containing problem. Neither direction constructs the unknown finite signed factors with ALL raw coefficients nonnegative and literal C included, nor excludes every such factor pair. That original unrestricted feasibility/finite-code problem remains **NOT_PROVED** either way. Degrees, coefficients, orders, b-counts, gaps, delays and arities remain unbounded; no1320/small-period restatement or new bound is claimed.

Actual source reading: the April2010 draft's Chapter10 weak-algorithm, cancellative-module/two-by-two factorization and integer Gauss/linear-extraction proof bodies were read in reader windows4590–4750,4751–4930,4931–5110; Chapter11 definitions/completeness/degree/factorization proof through ALL eight proof steps, ending and notes were read continuously in5120–5330,5331–5520,5521–5735. This is not a whole-book reading or publisher-original-PDF/glyph authentication. The reader drops some nonzero/strict-inclusion glyphs and degrades matrices. The needed NONZERO hypotheses and factor sides are therefore explicitly stated and proved in this packet, not silently treated as a printed-publication PASS. No source examples or numeric controls were replayed or rediscovered as guidance. The unrelated general code-degree invariance/minimal-ideal ancestry remains outside the specialized proof.

All prior142/111/66/125 raw-memory/border and positiveRESET/signed/FACT sources remain separate UNREVIEWED/not verified unaffected. H*false/WITHDRAWN; I3/I4 three-prime/source boundaries and FACT660|n/n>=1320NOT1320div/R2CORE-LF57 vs LF58NR/depth3/56/U1notcounterexample stay unchanged. General I5 outside this b-containing specialization is not declared fully reconstructed from the original1985 article.

Reutenauer1985 and the Berstel–Reutenauer source receive positive PRIOR credit. This is source-proof/assurance progress, not a new factorization theorem, original finite-completion answer, novelty/SOTA/publication or stronger formal/kernel/human/family/executable gate. FOUR own MAJORs and v49 PRECISE blocker/all author-parent-reviewer histories remain permanent/ZERO withdrawn guidance; no repair/replay/backconversion or historical/global cognition/runtime census. Same18/HOLD/exclusiveOWNroot/originalcutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actualsubstantive30mincadence/noearlyfinalpark/sourceedit/git/deletion/publication/newGO.
