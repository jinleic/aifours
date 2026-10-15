# Generic three-super-soliton failure for every integer n≥4

**Exact verdict:** the generic mixed-type three-super-soliton criterion defined below
fails for every integer n≥4 in the paired system proposed by Wang–Tang–Liang2018.
Evidence: **Certification**. This does not refute their separate symmetry-integrability
hypothesis, exclude restricted solutions, or solve the broad book chapter.
The explicit source hypothesis and the limited current-literature screen are in STATUS.md.

## 1. Algebra, operators and selected solution class

### 1.1 Fermionic parameters versus the superspace coordinate

Let K be R or C and let `A=Lambda_K(zeta_1,...,zeta_r)` be a finite exterior algebra,
with its usual Z/2 grading; r may be any finite integer. The generators anticommute
and square to zero. The **external** odd coordinate theta is a further independent
generator. Coefficients are smooth scalar functions of (x,y,t), extended by A and theta.
All tau functions F,G are even in total parity. Write theta to the left when expanding:
`F=F_even+theta F_odd`, with `F_even in A_even`, `F_odd in A_odd`.

Define the parameter augmentation

    pi_zeta: A tensor Lambda(theta) -> Lambda(theta),
    zeta_i -> 0,     theta -> theta.

This is NOT the full projection setting theta to zero. Since F,G are even, their
images `f=pi_zeta(F)`, `g=pi_zeta(G)` are scalar and theta-independent: an odd scalar
coefficient of theta cannot survive augmentation.

Use **left** Grassmann derivatives: for homogeneous u,
`partial_theta(uv)=(partial_theta u)v+(-1)^parity(u)u(partial_theta v)`.
The superderivative is `D_theta=partial_theta+theta partial_y`, exactly as in
Wang–Tang–Liang2018 §2.1, p. 040203-2. With independent external theta_1,theta_2,
shared parameter algebra A, and diagonal evaluation Delta, define

    P_n = D_t + D_x^n,
    P_n F·G = Delta[(partial_t1-partial_t2
                     +(partial_x1-partial_x2)^n) F(1)G(2)],
    S_y P_n F·G = Delta[(D_theta1-D_theta2)
                         (partial_t1-partial_t2
                          +(partial_x1-partial_x2)^n)F(1)G(2)].

Delta identifies x1=x2=x, y1=y2=y, t1=t2=t and theta1=theta2=theta **after**
differentiation. The selected equations are `P_n F·G=0`, `S_y P_n F·G=0`.

### 1.2 Superphases, body seeds and the meaning of generic

The ordinary superplane wave is

    E_i=exp(eta_i+theta zeta_i)=exp(eta_i)(1+theta zeta_i),
    eta_i=k_i x+l_i y+w_i t+delta_i.

A standard three-super-soliton ansatz has finite square-free exponential body,

    f=sum_{S subset {1,2,3}} f_S exp(eta_S),
    g=sum_{S subset {1,2,3}} g_S exp(eta_S),
    eta_S=sum_{i in S}eta_i,
    f_empty=g_empty=1, f_i=a_i, g_i=b_i.

No pair-product formula is imposed on the higher coefficients f_S,g_S. They are
independent unknown scalar constants until the equations determine them.
The supertau coefficients may contain arbitrary even/odd parameter dressings,
including theta-dependent terms and modified odd interaction phases as used in
Delisle–Jaouadi2026. We allow even extra terms with identically zero parameter body:
the theorem only needs the bodies f,g to have the displayed square-free form.
Thus it is not merely a failure of the naive undressed supertau ansatz.

For a single body seed and `l_i != 0`, the two bosonic coefficient equations give

    P_n(kappa_i) a_i=0,       P_n(-kappa_i)b_i=0,
    kappa_i=(k_i,l_i,w_i),    P_n(k,l,w)=w+k^n.

Allowed generic types are:

- **F type:** `a_i != 0,b_i=0,w_i=-k_i^n`;
- **G type:** `a_i=0,b_i != 0,w_i=(-k_i)^n`;
- for odd n, both amplitudes may be independent at `w_i=-k_i^n`, since P_n is odd.

For even n and nonzero k_i the F and G branches are distinct. For odd n the mixed
F–F–G specialization below lies in the unrestricted two-amplitude parameter family.

A **generic family** means a solution on a nonempty Zariski-open set of independently
chosen body wave numbers and amplitudes on the relevant seed branch, not a family
supported on additional algebraic relations among them. All composite denominators
used below and all l_i are nonzero on that open set. Exponential phases are independent
as formal exponential monomials; the explicit witness has linearly independent
wave vectors, so no accidental coincidence can cancel its coefficients.

The question is whether arbitrary allowed seed types can be combined. Proving failure
for the F–F–G branch suffices to rule out this generic all-pattern criterion. We do NOT
assert that every three-wave solution fails. For every n, all-F linear superpositions
with G=1, suitably restricted bodies/polarizations and possibly other ansätze remain
outside that negative claim. Restrictions only on nilpotent parameters cannot repair
a forbidden generic body; families that also restrict the body may still survive.

## 2. Parameter-body projection theorem

**Theorem 2.1 (projection retaining theta).** For any constant-coefficient polynomial
P in the ordinary Hirota operators D_x,D_t and any even F,G as above,

    pi_zeta(P F·G)=P f·g,
    pi_zeta(S_y P F·G)=theta D_y P f·g.                 (2.1)

Consequently, any solution of the paired supersymmetric equations projects to a
solution `P f·g=0`, `D_y P f·g=0` of the bosonic pair.

**Proof.** The ideal I generated by all parameter generators zeta_i is preserved by
ordinary derivatives and by `partial_theta1,partial_theta2`, because none of these
derivatives removes a parameter generator. Multiplication by theta_i preserves I
as well. Thus augmentation commutes with every operator in the displayed definition,
with multiplication, and with Delta. On f(1)g(2) there is no theta dependence, so the
odd derivatives give zero and the remaining operator is

    Delta[(theta1 partial_y1-theta2 partial_y2)P f(1)g(2)]
       =theta Delta[(partial_y1-partial_y2)P f(1)g(2)]
       =theta D_y P f·g.

Since f,g are scalar, `theta h=0` in the free scalar module with basis (1,theta)
forces `h=0`. This proves the implication. No theta derivative is commuted through
diagonal evaluation; the only commutations used are with parameter augmentation. ∎

**Why nilpotent corrections cannot help.** Every such correction belongs to I.
Applying the even bilinear differential operator or a theta derivative still leaves
at least one parameter generator. It cannot cancel the zeta-degree-zero coefficient
of 1 or theta. Inverting an even coefficient with nonzero body does not change this
argument: augmentation remains an algebra homomorphism on that localization.
No division by an odd/nilpotent element is allowed.

**Invalid shortcut.** Setting theta=0 together with the parameters would turn the
second expression in (2.1) into zero and lose the constraint. For example, with
`f=x^n y,g=1`, `D_y P_n f·g=n!`, while
`pi_zeta(S_y P_n f·g)=theta n! != 0`. Full theta-zero evaluation would misleadingly
report zero. The replay explicitly checks this negative control.

## 3. Exact bosonic obstruction, re-derived independently

This section uses the earlier project's C4 algebra as an existing workspace baseline,
but gives the complete needed proof here and uses a fresh direct-differentiation
implementation. No old source or engine is edited or imported.

### 3.1 Uniqueness of the square-free coefficients

For an ordinary polynomial P, the coefficient of `exp(sum_i nu_i eta_i)` in P f·g is

    sum_{S,T: 1_S+1_T=nu} f_S g_T P(kappa_S-kappa_T).    (3.1)

At a square-free index `nu=1_U` with `|U|>=2`, the two equations for P and D_yP form
a 2-by-2 linear system in f_U,g_U, with matrix

    [ P(kappa_U)         P(-kappa_U)      ]
    [ l_U P(kappa_U)    -l_U P(-kappa_U)  ].

Its determinant is `-2 l_U P(kappa_U)P(-kappa_U)`. On the nonzero-determinant locus,
these coefficients are uniquely fixed successively at pairs and at U=123. A residual
at a repeated index is then a necessary compatibility condition, not a discretionary
choice of ansatz coefficients.

### 3.2 A mixed-type compatibility coefficient

Take type F,F,G: `b1=b2=a3=0`, with `a1 a2 b3 != 0`. Assume the four pair/triple
recursion determinants are nonzero and `l3 != 0`. Write `P_{-13}=P(-kappa1-kappa3)`,
etc. The repeated-index coefficient at `nu=(2,1,1)` in P f·g is

    R_211 = a1^2 a2 b3 l3 Phi /
              [ l_123 P(-kappa_123) P(-kappa_13) ],     (3.2)

where

    Phi=P(kappa2-kappa3) P(kappa1-kappa2-kappa3) P(-kappa1-kappa3)
        +P(kappa1-kappa3) P(kappa2-kappa1-kappa3) P(-kappa2-kappa3).  (3.3)

**Derivation.** At level12, the lower-order products vanish, so f12=g12=0. At level13,
subtracting the two equations after division by l13 gives

    g13 P(-kappa13) = -a1 b3 l3 P(kappa1-kappa3)/l13,

and analogously for g23. At level123 only
`X=a1 g23 P(kappa1-kappa2-kappa3)` and
`Y=a2 g13 P(kappa2-kappa1-kappa3)` contribute besides f123,g123. Elimination gives

    g123 P(-kappa123)=-(l23 X+l13 Y)/l123,
    g123=a1 a2 b3 l3 Phi /
            [l123 P(-kappa123)P(-kappa13)P(-kappa23)].

At (2,1,1), all ordered pairs except `(1,123)` vanish because `g1=f12=g12=0`;
the surviving term is `a1 g123 P(-kappa23)`, yielding (3.2). ∎

### 3.3 An obstruction for every integer n≥4

Set P=P_n and choose the rational body data

    k=(1,2,-4), l=(1,3,7), w=(-1,-2^n,4^n),
    a=(1,1,0), b=(0,0,1).                             (3.4)

These satisfy the three one-soliton conditions. The determinant of their three
wave vectors is `4^n+11*2^n-26>0` for n≥2, so all exponential monomials are distinct.
Equation (3.3) becomes the integer

    Phi_n=(6^n-4^n-2^n)(3^n+2^n-4^n-1)(3^n+1-4^n)
          +(5^n-4^n-1)(5^n-4^n-2^n+1)(2^(n+1)-4^n). (3.5)

**Lemma 3.1.** `Phi_2=Phi_3=0`, and `Phi_n<0` for every integer n≥4.

**Proof.** For 4≤n≤29, exact integer evaluation of the displayed formula is the finite
certificate in `results/replay.json`; the verifier prints every sign and stores every
integer value. In particular `Phi_4=-672768`, `Phi_5=-241920000`.
For n≥30, the first product is positive and strictly less than `96^n`: its factors
have signs +,-,- and respective absolute values less than `6^n,4^n,4^n`.
The first two factors in the second product are at least `5^n-2*4^n>0`, and its last
factor is at most `-4^n/2`. Hence

    Phi_n < 96^n - (100^n/2) (1-2*(4/5)^n)^2.

At n=30 the exact integer inequality

    (5^30-2*4^30)^2 >= 2*24^30

holds (also checked in the certificate). Thus `(1-2*(4/5)^n)^2 >= 2*(24/25)^n`
for all n≥30: the left side increases and the right side decreases there. Therefore
Phi_n<0 for all n≥30, completing the proof. ∎

All denominators in (3.2) and the pair/triple recursions are nonzero for (3.4).
Indeed `l12,l13,l23,l123=4,8,10,11`, and for n≥2 the relevant P-values are

| Argument | P-value | Sign/nonzero reason |
|---|---|---|
| kappa12 | `3^n-2^n-1` | positive |
| -kappa12 | `1+2^n+(-3)^n` | positive for even n, negative for odd n≥3 |
| kappa13 | `4^n-1+(-3)^n` | positive |
| -kappa13 | `1+3^n-4^n` | negative |
| kappa23 | `4^n-2^n+(-2)^n` | positive |
| -kappa23 | `2^(n+1)-4^n` | negative |
| kappa123 | `4^n-2^n-1+(-1)^n` | positive |
| -kappa123 | `2+2^n-4^n` | negative |

The signs follow directly from `4^n>3^n+1`, `3^n>2^n+1`, and `2^n>2` where needed;
all hold for n≥2 (the odd rows first occur at n=3). Consequently

    R_211 = 7 Phi_n /
              [11(2+2^n-4^n)(1+3^n-4^n)] != 0         (3.6)

for every n≥4. Thus no square-free bosonic tau pair with these body seeds exists.
Since the compatibility residual is rational in the independent parameters and is
nonzero at a point where every determinant is nonzero, it is not the zero rational
function. Its zero set is proper. This proves **generic**, not merely isolated,
failure of the F–F–G branch for even n. For odd n the amplitude specialization used
in (3.4) has no amplitude in any denominator; a zero generic two-amplitude identity
would also vanish at this specialization. It does not, so the unrestricted odd-n
family fails generically as well.

## 4. Main theorem and exact scope

**Theorem 4.1 (generic paired three-super-soliton obstruction).** For every integer
n≥4, the Wang–Tang–Liang paired supersymmetric system

    P_n F·G=0,       S_y P_n F·G=0

has no three-super-soliton family with generic independent F–F–G body data in the
class of §1.2. In particular it fails the generic all-allowed-pattern criterion,
including the independent two-amplitude interpretation at odd n. This remains true
with arbitrary nilpotent interaction dressings and extra body-zero terms in F,G.

**Proof.** Suppose such a family existed. Theorem2.1 projects it, without setting
theta=0, to a bosonic square-free solution with the same body data. Sections3.1–3.3
show a nonzero necessary rational compatibility residual for every n≥4, which cannot
vanish on a nonempty open set of independent body parameters. Contradiction. The
argument uses only the body component; no nilpotent correction can cancel it. ∎

This answers the **explicitly proposed three-super-soliton test**, in its standard
generic all-pattern interpretation fixed here. It does **not** prove absence of
infinitely many generalized symmetries, a Lax representation, constrained soliton
families, nonstandard body ansätze, or isolated/reduced supersolutions. It is not a
full refutation of every meaning of the 2018 integrability hypothesis or of the book
chapter's broad construction conjecture.

## 5. Boundary cases and controls

- At n=2 and n=3, (3.5) is zero. The independent direct-differentiation replay solves
  the full body coefficient equations for (3.4) and finds **both full residuals zero**,
  not merely the selected R211 coefficient. These controls establish that the
  obstruction is not accidentally reporting failure at the known lower-degree cases.
- Given any scalar solution f,g of the bosonic pair, a restricted but genuine even
  supertau lift is `F=f(x,y+theta zeta,t)`, `G=g(x,y+theta zeta,t)` with one odd parameter
  zeta. Because `(theta zeta)^2=0`, these are finite expansions and
  `D_theta F=(zeta+theta) f_y(x,y+theta zeta,t)`; similarly for G. Thus
  `S_y P F·G=(zeta+theta)D_y P f·g` at the shifted coordinates, so both equations vanish.
  The n=2,3 body solutions supply such nontrivial common-parameter boundary lifts.
  Their odd phase parameters obey `zeta_i=l_i zeta`; this is **not** a claim of
  unrestricted independent-fermionic-parameter three-super-soliton integrability.
- Direct exterior-algebra controls use both theta1 and theta2 before diagonal
  substitution, left odd derivatives, anticommutation signs, and nonzero nilpotent
  components. The theta-preserving projection identity is compared coefficientwise
  against ordinary Hirota differentiation.
- The n=4 and n=5 rational witnesses are rebuilt using Euler differential operators
  `Lx=sum k_i z_i partial_zi`, `Ly=sum l_i z_i partial_zi`, `Lt=sum w_i z_i partial_zi`
  on explicit tau polynomials. Their bilinear operators are expanded by the binomial
  theorem. This implementation does not import or call the old Hirota coefficient
  engine or its obstruction routine.

## 6. Claim/evidence/novelty ledger

| Claim | Evidence label | What it establishes | Novelty scope |
|---|---|---|---|
| Parameter augmentation identity (2.1) | Certification | Any even paired supersolution forces the two bosonic equations; external theta retained | Elementary algebra; no claim of a new technique |
| All-degree bosonic mixed-type obstruction | Certification | Nonzero generic compatibility residual for every n≥4 | Re-derived from earlier workspace C4; classical ingredient, no priority claim |
| Theorem4.1 | Certification | Failure of the selected generic paired three-super-soliton criterion for all n≥4 | Exact 2018 hypothesis/criterion addressed; bounded citation screen found no settling source, not exhaustive novelty clearance |
| Exterior controls and n4/n5 witnesses | Certification of the explicit identities/witnesses | Independent implementation catches projection, sign and coefficient-encoding mistakes | Supplemental controls, not the universal proof |
| n2/n3 boundaries/common-parameter lifts | Certification at specified body data and restricted lift | Obstruction vanishes; lower-degree restricted superfamilies survive | Does not certify unrestricted fermionic families |

## 7. Replay and independent review

Executed from this directory:

    /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B code/replay.py

Observed (all exact arithmetic):

    Exterior projection/sign controls PASS for n=2..6.
    Invalid theta-zero projection loses the nonzero theta*n! constraint, as expected.
    Phi2=Phi3=0; Phi_n<0 for n=4..29; exact tail inequality at n=30 PASS.
    n=2: R211=0; full residual counts P=0, DyP=0; restricted super-lift passes.
    n=3: R211=0; full residual counts P=0, DyP=0; restricted super-lift passes.
    n=4: R211=-56064/5423; full residual counts P=5, DyP=5.
    n=5: R211=-313600/1573; full residual counts P=3, DyP=3.
    n=4,5 nilpotent-dressing projection controls PASS.

The replay completed in about two seconds and wrote `results/replay.json`.
It supplies explicit rational witness tau coefficients, the direct residual polynomials,
every finite integer in the all-degree certificate, and the exact tail inequality gap.
No build/lint/test-suite run or old-engine replay was used.

Independent other-vendor referee review is requested on the pinned source/proof/replay
snapshot. Its completed output and dispositions are added below; a running invocation
is not a review result.
