# Essential balanced B: two actual PH3 channels, strictly positive recycling, and exact complex double contact

Owner MathResearch96h-2 / math-1. Actual `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 06:47:42 PDT 2026**. **WRITTEN AUTHOR-CANDIDATE, UNREVIEWED.** Exact conventional mathematical proof/source work only; no scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/checker/test/build/CLI/nested agent or new GO. No machine/kernel checks.

## 1. Original problem, named full proof input and exact new representation

Fix c,d>0,a=c+d,b²=8d²/9 and `D5(s)=(s+c)((s+a)²+b²)²`, K=D5(0). The full original arbitrary-topology PH7 question remains OPEN/minimum{7,8}. This packet neither constructs PH7 nor excludes all B, and ordered-A also remains open.

The named complete written input is `PH7-standalone-global-ordered-A-or-balanced-B-equivalence-v1.md`,266LF, SHA256 `3815c4d699735797090dbd974f522828363c02931b604d8f36af438f00d7ffc6`. It is a NEW unreviewed candidate, not silently parent-adopted. It contains the FULL lower<=6 proof at8/9 (AppendixA), occupation reversal/constant-side-to-A proof, physical shared-factor equations and global ordered-A/B coverage. This successor does not substitute a prior title/hash for those proof bodies: any independent gate consuming those inputs must supply/reconstruct the entire named body, or retain that exact conditional boundary. The new local arguments below apply to EVERY actual literal B pair, independent of an unproved claim that B covers the original problem by itself.

Take such an actual pair

    T=[ A3      b0      0
        r^T    −lambda  t^T
        D       f       F3 ],
    alpha=(alpha_R,0,0), omega=(0,0,omega_S)^T,
    b0=−A3 1>=0,alpha_R>=0,alpha_R1=1,
    r,t,D,f>=0,lambda=r^T1+t^T1,
    omega_S=−D1−f−F3 1>=0,

with A3,F3 actual Hurwitz Metzler, shortest boundary distances TWO+TWO, and BOTH full target characteristic/numerator equations. There are no free mode factors, equal-holding assumptions, unique initial/exit restrictions or deleted backwards D/f.

**New complete representation theorem, at the named proof input:** either this pair can physically be reblocked/reversed into complete A, OR both three-state channels are essential in the sense of §2 and admit the positive PH3 success conditioning and actual renewal factorization in §3. In the latter branch success probability p is STRICTLY between0 and1, and the SAME physical return kernel satisfies exact double-contact equations at BOTH repeated target complex poles (§§4–5). The necessary conditions are not asserted sufficient without the FULL original matrix/row/characteristic/numerator ties.

## 2. Pruning by ACTUAL reblocking, without deleting a phase

Let R_good be the old-R vertices reachable from I=supp(alpha_R) without visiting the center. Any such first-center path stays in old R. Distance TWO requires at least two good vertices, so if R_good is not all three, exactly ONE bad R vertex exists. No R_good→bad edge exists by reachability. Move that bad phase, unchanged, into S. Old R_good→oldS was already zero, so the NEW upper-right block is still zero. Input remains on the two good R phases and every exit remains in the new S. This actual partition has sizes2+4 and pre-distance2, hence its PRE numerator is constant. Actual PH reversal and the constant-post cut move of the named266LF proof give A. Every old entry is retained/reclassified; no “unreachable phase” was deleted from the full dynamics.

Similarly let S_good be the old-S vertices having a path to omega_S entirely within F3. Distance TWO needs at least two such vertices. If not all three are good, exactly ONE is bad, it has omega=0 and has NO edge into S_good (else it too could reach an exit). Move it unchanged into R. The new R→S_good block is zero because old R→oldS was zero and bad→good is zero. This has sizes4+2 and post-distance2, hence constant POST numerator; the actual constant-post cut move gives A directly. Its bad phase may return to the center/R and was never removed.

Therefore the genuinely balanced branch not already reducible to A may be restricted to **ALL THREE R phases prefix-reachable and ALL THREE F phases exit-co-reachable inside F**. The reblocking alternative is proved at actual row/input/exit identities, not by discarding a topology. It loses no original representation from the A/B UNION.

Every actual target PH7 is globally initial-reachable by the named <=6 barrier. Each S phase is then also reachable from some positive t-entry through F alone: take a simple initial-to-that-phase path, consider its LAST center visit, and note that thereafter it cannot enter R and later S without revisiting center. Thus `t^T(−F)^−1` has every component strictly positive. This fact is distinct from S_good: it is reachability FROM t, not co-reachability TO omega.

## 3. Positive PH3 conditioning and exact SAME-center renewal factorization

In the essential branch set

    h=(−F)^−1 omega_S>0, H0=diag(h), gamma=t^T h>0,
    F_star=H0^−1 F H0,
    omega_star=H0^−1 omega_S,
    beta=t^T H0/gamma.

Strict positivity of h is precisely the F-internal exit-co-reachability just retained. Then `F_star1=−omega_star`, beta>=0,beta1=1, and F_star is Hurwitz Metzler. Thus (beta,F_star) is an ACTUAL normalized three-phase pair with the same distance TWO, not a raw positive transfer awaiting a row-sum certificate. Also (alpha_R,A3) with literal exit b0 is an actual PH3. Define their normalized transforms

    phi_R(s)=alpha_R(sI−A3)^−1 b0,
    phi_S(s)=t^T(sI−F)^−1 omega_S/gamma
            =beta(sI−F_star)^−1 omega_star.

Both equal1 at0. The local positive diagonal conditioning is used as a representation of the successful channel; it is NOT asserted that replacing F alone by F_star in the WHOLE old T preserves all PH row ties. The entire actual couplings below remain those of the same old matrix.

Let

    B_return(s)=r^T(sI−A3)^−1 b0
              +t^T(sI−F)^−1 f
              +t^T(sI−F)^−1 D(sI−A3)^−1 b0,
    R_return(s)=B_return(s)/(s+lambda),
    S_success(s)=t^T(sI−F)^−1 omega_S/(s+lambda).

These are actual defective Laplace transforms. At the center, the holding time is Exp(lambda). A departing trajectory either enters R then returns to center, enters S then returns directly via f, enters S then R via D and returns, or is absorbed from S. Stable principal blocks ensure each described first-exit episode terminates. The displayed sums/products are exactly those three return cases and the success case. No independent return distribution or cross-cut matrix has been selected.

The complete physical resolvent equation gives

    H(s)=phi_R(s) S_success(s)/(1−R_return(s)).       (RENEW)

To check all normalization ties, `(−A3)^−1 b0=1` and `omega_S+f+D1=−F1`, so

    B_return(0)=r^T1+t^T(−F)^−1(f+D1)
               =r^T1+t^T1−t^Th=lambda−gamma.

Hence with p=gamma/lambda,

    S_success(0)=p, R_return(0)=1−p, 0<p<=1.

Conditional success has normalized transform `S_success/p=[lambda/(s+lambda)]phi_S`. If 0<p<1, conditional failure has normalized transform `phi_return=R_return/(1−p)`. By the strong Markov property at the SAME center, the whole absorption time is: independent initial PH3 passage; a geometric number (success parameter p) of conditional return excursions; and one successful Exp(lambda)+conditioned-PH3 excursion. The alternative algebraic statement is

    H=phi_R * [p(lambda/(s+lambda))phi_S]
               /[1−(1−p)phi_return].               (PH3-RENEW)

This is a positive physical renewal representation with all original couplings, not an arbitrary factorization of D5 or scalar necessary data.

## 4. Three-state principal pole exclusion and STRICT recycling

The actual spectral abscissa is rho(T)=−c. Here is the needed positivity comparison: global initial reachability and exit co-reachability make every dominant communicating block accessible at positive entrance/exit times; its positive Perron vectors give a density lower bound C exp(rho t). The target density is asymptotic to `K/(d²+b²)² exp(−ct)`, with all other terms polynomial times exp(−at), hence rho<=−c, and the actual pole−c gives equality. Every Metzler principal block has spectral abscissa <=rho(T), by semigroup monotonicity/path inclusion (or padding it with sufficiently negative diagonal entries and applying Metzler spectral monotonicity).

Suppose a real3×3 Metzler principal block contained the target pair −a±ib. Its remaining real eigenvalue is its Perron eigenvalue−q0, with c<=q0<=a. Put delta=a−q0 in[0,d]. Centering this block by its average eigenvalue gives eigenvalues `2delta/3,−delta/3±ib`. Since the centered matrix is still Metzler,

    trace(centered²)=2delta²/3−2b²>=0.

Thus b²<=delta²/3<=d²/3, contradicting b²=8d²/9. Consequently **neither a_R(s)=det(sI−A3) nor a_S(s)=det(sI−F3) vanishes at either repeated target complex pole**. This argument is topology-unrestricted, reducible or irreducible, and uses the actual principal spectra, not a false hidden-eigenvector localization.

Now suppose p=1. The nonnegative zero sum `B_return(0)=0` first forces r=0. The strictly positive row `t^T(−F)^−1` proved in §2 then forces f+D1=0; since f,D>=0, f=0,D=0. The full T becomes upper block triangular with diagonal blocks A3,−lambda,F3. All its complex eigenvalues would have to lie in A3 or F3, but neither can contain the target pair by the preceding argument. Contradiction. Therefore

    **0<p<1; R_return(0)>0.**                        (STRICT)

Positive recycling is necessary in the genuinely balanced branch, not a freely optional feedback relaxation. The argument does not use an external irreducibility theorem or an unreviewed assertion that the full PH7 must be irreducible.

## 5. Exact complex Hermite contact — not a positivity bound outside its domain

In B, the actual numerator factors are `N_R=L_R(s+x)`, `N_S=L_S(s+y)` with L_R,L_S,x,y>0 and `L_R L_S=K`, so `Q2=(s+x)(s+y)` is real-rooted Hurwitz; equality x=y is allowed. Let zeta=−a+ib. Section4 proves a_R(zeta)a_S(zeta)!=0, and zeta+lambda!=0 because b>0. The complete characteristic identity is

    a_R(s)a_S(s)(s+lambda)(1−R_return(s))=D5(s)Q2(s).

The real negative hidden roots cannot equal zeta. Since `D5(s)=(s+c)(s−zeta)²(s−conj(zeta))²`, the actual analytic continuation of R_return is regular at zeta and has EXACT second-order contact with1:

    R_return(zeta)=1,
    R_return'(zeta)=0,
    R_return''(zeta)
      =−2(zeta+c)(zeta−conj(zeta))² Q2(zeta)
         /[(zeta+lambda)a_R(zeta)a_S(zeta)] !=0.    (CONTACT)

Real coefficients give the conjugate conditions as well. This is not merely substituting independently chosen spectral lists: R_return is the SPECIFIC matrix-linked defective return transform in §3, with both actual PH3 channels, success probability, all feedback and exact row ties.

**Crucial limitation:** the positive Laplace-integral description is valid in its convergence half-plane, in particular Re(s)>=0. Although R_return is analytic at zeta, nothing above proves that its positive defining integrals converge at Re(s)=−a; principal Perron poles are only bounded by−c, not known to lie left of−a. One must NOT assert `|R_return(zeta)|<=R_return(−a)<1`, differentiate an inadmissible positive integral there, or infer a contradiction merely from CONTACT. Analytic continuation of a positive transform need not retain those integral inequalities. This explicitly names the first unproved functional-analysis bridge rather than using it silently.

## 6. Exact observable moment identities of the positive renewal representation

Write mu_R,mu_S,mu_return and V_R,V_S,V_return for the means/variances of the three normalized physical laws in(PH3-RENEW). They are finite by stable finite-state construction. Conditional return durations are strictly positive because every attempt includes the center's positive holding time. Geometric restart gives exactly

    mu_target=mu_R+mu_S+1/lambda+(1−p)mu_return/p,
    V_target=V_R+V_S+1/lambda²
             +(1−p)V_return/p+(1−p)mu_return²/p².

For the original target these are

    mu_target=1/c+4a/(a²+b²),
    V_target=1/c²+4(a²−b²)/(a²+b²)².

The target expressions follow by the first two derivatives of log(K/D5); the renewal expressions follow from independent conditional excursions and the geometric count mean(1−p)/p,variance(1−p)/p². No numeric instance or machine arithmetic is used. In particular STRICT forces `mu_target>mu_R+mu_S+1/lambda` and `V_target>V_R+V_S+1/lambda²`. These are exact necessary identities, not an asserted feasible/infeasible moment test or an extra premise replacing full TARGET.

## 7. Full scope, precise open intersection and assurance

This is a NEW topology-unrestricted representation of the balanced branch: actual reblocking sends every prefix-inaccessible/post-incoaccessible case to A; all remaining B has two genuine normalized PH3 channels, strictly nontrivial physical recycling, and simultaneous exact double contact at the repeated complex poles, with complete original row/coefficient ties retained. No fixed support, selected holding family, unique boundary, free phase/modulus choice or independent factor cone is imposed. The complex principal-pole exclusion and STRICT/contact/moment statements are proved for ALL essential B pairs, not at a finite sample.

**Unresolved:** whether ANY such SAME-matrix PH3/return data with full TARGET can satisfy CONTACT and the exact positivity/row constraints, or whether they are inconsistent. CONTACT and the moment equations alone are NOT sufficient; no PH7 witness or B-emptiness theorem is delivered. The complete arbitrary ordered-A outer/TEN intersection also stays OPEN. No minimum8, larger numerical band/maximal endpoint, lower/upper promotion or full8/9 verdict. This is structural mathematical progress/representation, not a solution of the remaining coefficient intersection.

The named266LF proof input remains unreviewed until an ENTIRE fresh mathematical/dependency gate reconstructs it; this successor requires its OWN whole-body gate, with that input supplied. Existing source/gate assurances are not widened by a notification. Ordinary finite CTMC strong Markov/semigroup facts, positive principal resolvents, diagonal similarity, finite matrix traces/determinants and geometric-sum moment algebra are named classical background; no unavailable new specialized lemma is hidden. No formal/kernel/configured-family/human/executable/novelty/SOTA/priority acceptance.

All substantial symbolic leads, including this complete representation, were saved in checkpoint075 before this manuscript, not called a later preregistered discovery. The unproved general post3 center-elimination Riccati/single-initial similarity leads remain UNREVIEWED, not imported here; they can fail nonnegative inverse/incoming-row constraints and are NOT claimed normal forms. Newprimarywriting follows ACTUALv119RETURN→NEWwholeACKWRITTEN/SENT, and all prior provenance/process histories remain. NEWcadence071→072FULL33m29s/firstlate30m36s/parentv32, distinctprematureturnend/v21, earlierexactness/cadence/opaque/documentary/importpin findings and ZEROwithdrawnprobe/guidancecredit are permanent, not cured by this proof. No clean cognition/runtime/count census or falsity/execution-from-process inference.

Only exact WRITTEN symbols/fractions/integer products/source/metadata. Same original18/exclusiveOWN/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/substantiveactivecheckpoints<=30min; no newGO/owner/scope reset, source edit, Git/deletion/publication, early final park or96-hour closeout.
