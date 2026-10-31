# Definition-first H_(1,2): an exact density threshold and an ALL-order PH obstruction

**MathResearch96h-2 / math-1. WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Actual native observation before writing: **Tue Oct 27 14:53:14 PDT 2026**. All mathematics below is exact conventional WRITTEN, not executed, machine-checked, formal/kernel, human, configured-family or novelty verification.

## 1. Input boundary, full target and actual source order

Current S1 is a narrow definition-first release, NOT a blanket original-primary restart. I read controls19LF FIRST, complete release, metadata equality receipt, then wrote `prerequisite-pre-body-exposure-ack-v1.json` at actual14:46:42 BEFORE reading the body or drafting a derivation. ACK SHA256 `0140cc3dd6731f70e27af0d4fed7895bb33d06abe293bf1e5de4a8d57cc5c40c`. I then actually read ALL43LF of packet `89fedee56db112d2fc29b1762dc18fbc58092dffabb130e9001e14a853eb5c2c`, including complete S1 and S2/endings. The complete mathematical kernel below was saved in substantive checkpoint001, SHA256 `9c45c6463a260108f3da659b29b3b8da08bb6c7ed2594f44431ebdbc1b57e05e`, at actual observation14:49:21.

The ONLY mathematical problem input used is S2's literal transform/PH definition, SHA256 `a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85`, from screened selection LF7–15. Its provenance is retained-selection text, not an independently certified book image. Main-authored transport does not certify book/source equivalence. No old proof/review/checkpoint/park/held guide, proposed672 union, L6/G7/U6, old numerical band construction or primary-comparison body was opened or used as a mathematical input. Parent-adopted safe-envelope claims remain at their own cuts; this proof does not require them.

The ORIGINAL target is the entire minimum PH-order function over its existence region, including distinguishing non-PH parameters. This manuscript proves a topology-unrestricted NON-PH result on an exact nonempty parameter region, not a one-matrix/one-topology coefficient failure. It does NOT determine the finite minimum in the remaining positive-density region or decide the critical seven-versus-eight question.

Prior authorship/exposure survives. All excluded guidance and exposed/potential v260 consumers remain ZERO; no payload is reproduced or reconstructed. The proof's printed input trail is the supplied transform plus explicitly named elementary facts, NOT a clean-cognition/private-noninfluence certificate. In particular no old circulant/control/trigonometric matrix scout, its outcomes, selection or confidence is a premise: there is no matrix ansatz or selected numerical trial here.

## 2. Statement: exact density sign and a universal non-PH parameter set

For ALL `a>c>0`, `b>0`, write `d=a-c`, `beta=b/d`, and let

    H(s)=K/[(s+c)((s+a)^2+b^2)^2],
    K=c(a^2+b^2)^2.

An actual finite PH representation has ANY finite dimension n, arbitrary real Hurwitz Metzler T, literal `omega=-T1>=0`, probability row alpha, and transform `alpha(sI-T)^(-1)omega`. Reducible graphs, arbitrary holding rates and canceled modes are retained.

Define xi as the UNIQUE solution

    tan(xi)=xi,     2*pi<xi<5*pi/2.

There exists a UNIQUE constant r_star>0 satisfying

    exp(-r_star*xi) * [(1+r_star^2)xi^2+2r_star*xi+2]
      /sqrt(1+xi^2) = 2.                           (TH)

This is an exact implicit definition with a proved unique root; no numerical root/approximation is supplied or needed. Put `beta_star=1/r_star`.

**Theorem.** The unique continuous inverse Laplace density f of H has:

1. `f(t)>0` for EVERY `t>0` iff `d/b>r_star` (equivalently `beta<beta_star`).
2. `f(t)>=0` for EVERY `t>=0` iff `d/b>=r_star`.
3. At `d/b=r_star`, f has exactly ONE positive-time zero, at `t=xi/b`; it is a strict local minimum of quadratic order.
4. For `d/b<r_star`, f is negative at `t=xi/b`.
5. Consequently **NO finite PH representation of ANY order exists whenever `beta>=beta_star`**, including equality. The excluded family is nonempty for the original symbolic parameters, not a sampled instance.

The converse “strictly positive density implies a finite PH representation” is NOT asserted. It requires an additional positive-realization/PH-characterization input or a new proof, identified in §10.

## 3. Elementary inverse Laplace calculation with exact normalization

Set `r=d/b>0`, `x=b*t`, `R=1+r^2`, and

    F_r(x)=integral_0^x exp(-r*u)(sin(u)-u*cos(u)) du.

Elementary Laplace integrals give, for real s sufficiently positive,

    L{ exp(-a*t)[sin(b*t)-b*t*cos(b*t)]/(2b^3) }
      =1/((s+a)^2+b^2)^2.

Indeed the two elementary transforms are `b/J` and `b[(s+a)^2-b^2]/J^2`, with `J=(s+a)^2+b^2`; their difference is `2b^3/J^2`. Convolving with `exp(-c*t)` therefore gives the unique continuous inverse

    f(t)=K exp(-c*t) F_r(b*t)/(2b^4).              (DENS)

The integrand defining F is bounded in absolute value by `exp(-r*u)(1+u)`, whose integral is finite for every r>0. Thus f is absolutely integrable and of exponential order, the displayed Laplace calculation is legitimate, and `integral_0^infinity f(t)dt=H(0)=1`. That last equality is signed normalization; it does not imply f>=0.

Direct integration, or the derivative check below, yields the ALL-variable formula

    F_r(x)=[2-exp(-r*x) A_r(x)]/R^2,
    A_r(x)=[R*x+r(r^2+3)]sin(x)+[2-r*R*x]cos(x).   (F)

At x=0, A_r(0)=2. Differentiation gives the exact identity

    r A_r(x)-A_r'(x)=R^2[sin(x)-x cos(x)],

so(F) has derivative `exp(-r*x)[sin(x)-x cos(x)]` and value0 at0, proving it equals the integral. No arithmetic program, boundary sample or fitted expression is used.

## 4. ALL extrema, not a chosen-time sign test

Let `g(x)=sin(x)-x*cos(x)`. Then `g'(x)=x*sin(x)`. On(0,pi), g strictly increases from0, so F_r initially strictly increases. For EACH integer n>=1, g is strictly monotone on `(n*pi,(n+1)*pi)` and changes sign exactly once. The unique zero x_n lies in `(n*pi,n*pi+pi/2)`: the endpoint values `g(n*pi)=(-1)^(n+1)n*pi` and `g(n*pi+pi/2)=(-1)^n` have opposite signs. The half-period value is nonzero, so the equation is legitimately `tan(x_n)=x_n`.

These are ALL positive zeros of g. At an x_n,

    sin(x_n)=x_n cos(x_n),
    cos(x_n)=(-1)^n/sqrt(1+x_n^2).

Define the positive function, for every r,x>0,

    W_r(x)=exp(-r*x)[R*x^2+2r*x+2]/sqrt(1+x^2).

Substitution into(F) gives

    F_r(x_n)=[2-(-1)^n W_r(x_n)]/R^2.              (EXT)

Thus odd-index roots are local MAXIMA with strictly positive values. Even-index roots are precisely ALL positive-time local MINIMA. The first of these is `xi=x_2`. Between consecutive roots F_r is monotone; prior to the first root it is positive. A proof controlling EVERY even-index root therefore controls ALL times, not just one test time.

## 5. The unique threshold exists and has the needed global monotonicity

For fixed x>0, an exact derivative is

    partial_r W_r(x)
      =-(1+r^2)x^3 exp(-r*x)/sqrt(1+x^2)<0.        (WR)

For fixed xi, W tends0 as r tends infinity, since an exponential dominates its quadratic factor. At the symbolic value `r=1/xi`,

    W_(1/xi)(xi)=(xi^2+5)/(e*sqrt(1+xi^2))
                >xi/e>2.

The first inequality follows by squaring positive quantities: `(xi^2+5)^2-xi^2(1+xi^2)=9xi^2+25>0`. The second uses `xi>2pi` and the ordinary elementary bounds `e<3<pi`. These bounds may be obtained from the exponential series and an inscribed regular hexagon; no numerical approximation or physical parameter/control probe is involved. Continuity and(WR) give EXACTLY one solution r_star of(TH), and also

    r_star*xi>1.                                  (RX)

A second exact derivative, now in x, is

    partial_x W_r(x)
      =-exp(-r*x)x^2 Q_r(x)/(1+x^2)^(3/2),
    Q_r(x)=r(1+r^2)x^2-(1-r^2)x+r(r^2+3).         (WX)

When `r*x>=1`, its factor has the useful ALL-variable positive decomposition

    Q_r(x)=x[(r*x-1)+r^2(r*x+1)]+r(r^2+3)>0.

Consequently W_r is strictly decreasing in x wherever r*x>=1. By(RX), for EVERY r>=r_star it is strictly decreasing throughout x>=xi. Therefore

    W_r(x_(2k))<W_r(xi) for EVERY integer k>=2.

This is the missing global-extrema comparison. Without it, evaluating the first minimum alone would not establish the positivity half of the theorem.

## 6. Complete density-sign proof and boundary order

If r>r_star, (WR) gives `W_r(xi)<2`; (WX) and(RX) give an even smaller value at ALL later minima. By(EXT), every positive-time local minimum is strictly positive, and every maximum is strictly positive. Initial increase and monotonicity on every intervening interval show `F_r(x)>0` for ALL x>0.

If r=r_star, its FIRST positive-time minimum is0 and every later minimum is strictly positive. The same complete interval argument shows F>=0 everywhere and identifies xi as its only positive-time zero. At xi,

    F_r'(xi)=0,
    F_r''(xi)=exp(-r*xi) g'(xi)
             =exp(-r*xi) xi*sin(xi)>0,

because xi lies in `(2pi,5pi/2)`. Hence this zero is a strict quadratic minimum. Formula(DENS) has a positive analytic prefactor, so the original f has the same positive-time zero/order at `xi/b`.

If0<r<r_star, strict monotonicity in r gives `W_r(xi)>2`, so(EXT) makes F_r(xi)<0. This proves ALL directions in the density sign statement. All parameters c>0,b>0,d>0 remain symbolic and coupled as in the original transform.

## 7. Why a touching zero, as well as negativity, excludes EVERY finite PH order

Here is the actual-object positivity lemma, valid for ANY finite dimension and ALL PH topologies.

Let T be real Hurwitz Metzler, `omega=-T1>=0`, and alpha a probability row. Choose a positive symbolic rate q at least `max_i(-T_ii)`; this is a quantified construction for an arbitrary matrix, not a selected trial. Then `M=T+qI>=0`, so

    alpha exp(T*t) omega
      =exp(-q*t) sum_(k>=0) t^k alpha M^k omega/k!,

with ALL coefficients nonnegative. Hurwitz stability and the literal row tie give

    integral_0^infinity alpha exp(T*t) omega dt
      =alpha(-T)^(-1)omega=alpha1=1.

Hence not all coefficients can be zero. At least one fixed k has `alpha M^k omega>0`, making the displayed series STRICTLY positive for EVERY t>0. Reducibility, zero input/exit coordinates, nonuniform holdings, unobservable phases and latent canceled modes do not alter this reasoning. No irreducible-only positivity theorem is being substituted.

If such a PH representation matched the original rational transform, uniqueness of Laplace transforms of integrable continuous functions would identify its density with(DENS). But r<r_star produces a negative value, and r=r_star produces a zero at positive time. Both contradict strict positivity. Thus **r<=r_star excludes ALL finite PH representations**, not merely PH6/7, companion matrices, uniform diagonals or an ansatz. Conversely, r>r_star yields only a strictly positive normalized rational density from this proof; the actual-PH converse is deliberately not asserted.

## 8. A useful all-variable location statement, without a numerical threshold

For r>=1 and x>0, the explicit form in(WX) gives

    Q_r(x)=r(1+r^2)x^2+(r^2-1)x+r(r^2+3)>0.

Thus W_r strictly decreases from `W_r(0)=2` for EVERY r>=1. In particular `W_1(xi)<2`, so uniqueness in(TH) implies `r_star<1` and `beta_star>1`. Combined with(RX), this also gives the exact implicit-location bounds

    1/xi<r_star<1,      1<beta_star<xi.

These are universal symbolic inequalities proved from the derivative, not decimal evaluations or selected parameter experiments. They show explicitly that the critical `beta^2=8/9` lies on the strictly-positive-density side; this theorem does NOT decide its PH order. It is a whole-existence-region obstruction, not a disguised endpoint solution.

## 9. What changes, what does not, and exact original-object caller

**Changed in this current definition-first written packet:** an exact implicit density threshold is proved globally over ALL times and original positive parameters, and its entire closed high-beta side is ruled out for EVERY finite PH order. Equality is excluded by an actual-PH strict-positivity argument, not by a mistaken “nonnegative implies PH” claim. The result is more than a coefficient encoding or one-time counterexample: the global positivity direction, uniqueness of the threshold and all-topology caller have complete proofs.

**Not changed:** the finite minimum on the strictly-positive side; an actual PH construction there; the critical seven-versus-eight question; any direct/conditional older numerical band; NR-OLD-UPPER; exact book-image/source equivalence; independent source priority/novelty or stronger verification. The historical selection's PH6 residual/G7 sentence is not imported as a currently proved upper/lower premise. The safe report's later adoptions remain governing at their exact stated scopes, not rediscovered by this work.

The forward actual-object implication is unconditional within the supplied PH definition: an actual PH transform forces a strictly positive density, hence beta<beta_star. The converse proved here is ONLY the exact density-sign classification, not existence of an alpha,T. This distinction is essential to the original problem and is not a reduced-scope hidden claim.

## 10. Next genuinely admitted step and exact missing premise

For `0<beta<beta_star`, this packet proves a strictly positive continuous density whose transform is the supplied rational H. Completing the PH-existence region would require either:

- a fully proved finite-dimensional positive/Markov realization for this ALL-variable family, with actual alpha,T,row/input/exit/stability and exact transfer; OR
- a precisely supplied primary theorem that this class of strictly positive rational densities, with its exact dominant-pole and normalization hypotheses, admits a finite PH representation, together with an actual verification of EVERY antecedent.

No such specialized PH-characterization theorem is in the17LF definition packet or the permitted elementary inputs. It may NOT be imported from memory, an old comparison file, a held guide, a favorable report label or an unprovided citation. Strict positivity alone is not silently promoted to a construction or an order bound. An exact maximum-order statement would require still more information than existence alone.

A separate potentially useful original-order obligation would be to prove bounded-order closure under parameter limits with all actual Markov ties, in order to constrain minimal orders near a touching-zero boundary. That is NOT an elementary compactness conclusion established here: generator rates may be unbounded, and no old compactness/hidden-factor/source guide is an input. Neither that closure lemma nor a divergence-of-orders consequence is claimed. Any further branch needing these inputs must STOP and request a frozen primary statement or prove it from currently admitted facts.

## 11. Process and acceptance limits

This is exact WRITTEN/source work only; no scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/checker/build/test/typechecker, selected numeric/state/control/decimal/boundary probe, nested agent/modelCLI/paidAPI or new GO. All calculus arguments quantify over the whole parameter family; no floating-point approximation or root finding occurred.

All original STOP/HOLD/ZERO, v260 exposed/potential consumers, prior selected-check/post-STOP/quote/contact/turn-ending/cadence/read-order/provenance findings and parent/reviewer qualifications remain permanent. A correct new supplied proof would not cure any of them, certify unaffected cognition, blind reconstruction, continuous service, or book/source/novelty equivalence. N4 remains UNKNOWN with historical child exit unestablished; auxiliary214 remains STOP. No old packet was repinned, edited, moved, mined or adopted by this author claim.

The manuscript requires its own complete mathematics AND dependency/application review. Same18/exclusiveNEWroot/scientificHOLD; research deadline2026-10-31T21:23:27.000Z; substantive20-minute target/30-minute maximum with honest gaps; no heartbeat/timer/poll/ACK loop, early final park or round closeout. No Git/deletion/publication/contact/infrastructure mutation.

**END — full universal density-threshold/ALL-finite-PH obstruction proof; positive-density PH existence and finite minimum remain separate unproved obligations.**
