# RT: complete residual torus obstruction by exact whole-kernel norm certificates

**Owner:** PhysicsRQLS10, slot physics-5. **Scope/level:** WRITTEN-checked-in-kernel, using exact integer and `fractions.Fraction` arithmetic in the owner's Python eval kernel. Here “kernel” means the arithmetic session, **not a proof-assistant kernel**. This is a finite exact algebraic proof with its complete literal certificate, not an execution-independent analytic classification. No native scientific process or solver was launched.

Actual pre-freeze observation: **Sun Oct 25 03:54:17 PDT 2026** (`/bin/date`, verbatim). All older pinned/reviewed files remain unchanged. The separate v28-A reconstruction is neither awaited nor imported.

## 1. Result and exact boundary

Let `s=i*sqrt(7)`, `K=Q(s)`, and retain the literal first core, index labels and involution of the frozen manuscript:

    Q0(i,j)=0 if i=j;
            +1 if i,j share a row or column of the 3x3 grid labeled x+3y;
            -1 otherwise.
    C=(J-I+s Q0)/sqrt(8),
    rho=(0,7,8,6,5,4,3,1,2),
    ordered pairs H=(4,5), J=(3,6), U=(1,7), V=(2,8).
    Q1(i,j)=Q0(p(i),p(j)), p any permutation of 0,...,8,
    M_it=conjugate(C_ti)*C'_(t,rho(i)), C'=P C P^T.

For `a != b`, define

    A_j,ab = [Qj(r_a,r_b)-Qj(r_a,rho(r_b))
              -Qj(rho(r_a),r_b)+Qj(rho(r_a),rho(r_b))]/2,
    A_j,aa=0,  L=A0+A1.

The fixed `A0` is exactly

    [0 0 0 0; 0 0 1 1; 0 1 0 2; 0 1 2 0].

**Theorem RT+.** Suppose `rank_F7 L=2`, the genuine second support is in **any** of R0/R1/R2 below, and `rank_K M=7`. Then

    ker_C(M) intersect {delta: |delta_t|=1 for every t=0,...,8} = empty.

In fact, for each such literal core and a basis `V` of its complete two-dimensional complex kernel, the affine equation

    diag(V X V*) = (1,...,1), X in Herm_2(C),

is already inconsistent. Thus the extra RT hypothesis `rank_R Phi<=3` is **unnecessary for this stronger residual result**. No field, finite alphabet, conjugation symmetry or reality condition is imposed on the physical phase vector.

The residual predicates are exactly the frozen ones:

- **R0:** H has degree zero in `A1`, its remaining triangle has magnitudes `{1,1,2}`, and `rank_F7 L=2`. This is the genuine off-axis211 same-isolate branch, not the axis222 or `L=0` branch.
- **R1:** H has degree one in a genuine paw (`A1` has four edges), and `rank_F7 L=2`. The opposite triangle edge therefore cancels the first edge, retaining every genuine heavy/tag position.
- **R2:** H has degree two and `rank_F7 L=2`. This retains **all** genuine raw catalogue types and the modulo7 cross-determinant condition, including determinants that are nonzero multiples of7 over the integers.

This proves the previously missing RT implication, not the separate all-P theorem. The new stars/matching/Herm14 mathematics remains at its independently assigned reconstruction gate. No unrestricted maximal1-RQLS10 result, all-first-profile WLOG, all-conference-class result, global ray array, novelty or priority claim follows.

## 2. New representation: linear norm consistency on the entire kernel

A family-specific phase elimination is unnecessary. Put `B=4M`. For a nonmasked position set `a=Q0(t,i)` and `b=Q1(t,rho(i))`. Direct multiplication of the two literal core entries gives

    B_it = [(1-s*a)(1+s*b)]/2
         = (1+7*a*b)/2 + s*(b-a)/2.

At `t=i` or `t=rho(i)` it is zero. Therefore every entry of `B` is exactly one of

    0, 4, -3+s, -3-s,

and all rank/minor identities take place in `Z[s]` or `Q(s)`. This formula retains the actual second core, hence its actual E1/B1/D1; no arbitrary signed-graph replacement is made.

For an exact kernel basis with physical row `V_i=(v_i,w_i)`, any complex kernel vector is `delta=V z`, with `z in C^2` completely arbitrary. Write

    X=z z*=[p, a+b*s; a-b*s, q], p,q,a,b real.

If `c_i+d_i*s=v_i*conjugate(w_i)`, its squared-coordinate norm has coefficient row

    F_i=(|v_i|^2, |w_i|^2, 2*c_i, -14*d_i),
    |delta_i|^2=F_i*(p,q,a,b)^T.

The certificate supplies an integer vector `lambda` satisfying the **exact rational identities**

    sum_i lambda_i F_i = 0,
    S=sum_i lambda_i != 0.                         (N)

Consequently every vector in the full complex kernel satisfies

    sum_i lambda_i |delta_i|^2=0.

A coordinate-unit vector would make its left side `S`, a contradiction. Even an arbitrary Hermitian `X` with all nine target diagonal entries equal to one is impossible. This is not a PSD-relaxation-to-rank1 inference: the affine relaxation itself fails.

Independent arbitrary D/E are retained exactly as in the frozen necessary-zero equation: outer nonzero column phases cancel only from zero constraints, and the remaining nine independent unit entries are the unrestricted delta quantified above.

## 3. Complete all-source coverage, not selected inputs

Translations of the F3-by-F3 grid preserve Q0. Replacing `p` by `p-p(0)` therefore normalizes `p(0)=0` without changing Q1. Enumerating all `8!=40320` normalized tuples and keeping the lexicographic first tuple for each **entire** 36-entry upper-triangle character table covers every genuine second core.

The normalized enumeration gives 5040 distinct literal tables. Equivalently, the rook graph automorphism group is `(S3 x S3) semidirect C2`; its subgroup fixing0 has order8, so each normalized literal table occurs eight times. This equivalence is explanatory: the checker constructs the complete set and does not assume a symmetry quotient or transport right-kernel feasibility through transpose.

For every literal table the checker computes `A1`, `L` over F7 and the exact residual predicates. The complete leading-residual census is:

| Residual branch | All genuine leading-rank2 candidates | Certified rank at least8 | Exact rank7 with norm contradiction |
|---|---:|---:|---:|
| R0 | 56 | 32 | 24 |
| R1 | 96 | 80 | 16 |
| R2 | 84 | 72 | 12 |
| **Total** | **236** | **184** | **52** |

The certificate has exactly these236 canonical tuples, not a sample. The checker requires **set equality** between its independently reconstructed complete predicate set and the certificate tuple set, rejects duplicates, and checks each branch label. Thus no unlisted or selected core can stand in for the global RT quantifier.

### 3.1. The184 higher-rank alternatives

For each of these184 tuples the certificate gives an8-by-8 minor of `B` whose determinant is nonzero under

    Z[s] -> F11, s -> 2,

which is valid because `2^2=-7 mod11`. An identically zero algebraic minor would map to zero. Hence each such matrix has exact K-rank at least8 and **cannot satisfy the RT rank7 hypothesis**. This step needs neither projective-K phase descent nor a physical-phase finite-field substitution.

### 3.2. The52 exact complete kernels

For each remaining tuple the certificate supplies:

1. A7-by-7 minor nonzero under the same ring homomorphism, proving rank at least7.
2. A9-by-2 rational-K matrix `V`, checked entrywise to satisfy `B V=0`.
3. Two specified physical rows of `V` equal to the2-by-2 identity, proving column independence.

Thus `rank_K B=7`, and the supplied two columns span the **entire** complex kernel after scalar extension. No hidden higher-dimensional complex phases are omitted.

For each of the52 complete kernels, the integer vector in the table below satisfies(N). The full basis entries and all236 rank minors are in the attached JSON, and the exact checker is reproduced in Appendix B.

The norm-span values are diagnostic only: R0 has8/7/9 cores of span2/3/4; R1 has8/0/8; R2 has2/4/6. The original RT norm-span<=3 subset consists of29 cores. In28 of those29, the whole kernel has coordinate0 zero. The remaining core is dealt with explicitly in Section4. The proof does **not** rely on this29-case subfilter: it certifies the stronger52-core affine obstruction.

## 4. The sole nonzero-fixed-coordinate core in the original RT subset

Its canonical tuple is

    p=(0,1,2,3,7,8,6,4,5).

With free physical coordinates `delta5=A`, `delta8=B`, its exact entire kernel is

    delta0=-(7/6)B,
    delta1=delta2=-(1/2)B,
    delta3=(-7/12+(25/84)s)B,
    delta4=-A+(1/6)B,
    delta5=A,
    delta6=(-7/12-(25/84)s)B,
    delta7=delta8=B.

Thus `|delta1|=|delta8|/2`, incompatible with both being unit. The certificate's integral identity is `-9|delta0|^2+49|delta1|^2=0`, whose unit target is40, not0. This is an explanatory example **after** complete source coverage, not a selected-input substitution for RT.

## 5. Exact verification, controls and assurance

The owner eval session used integers, rational `Fraction` arithmetic and the quadratic multiplication law `s^2=-7`; it used no floating-point phase approximation, numerical optimization, native scientific launch, external model or network. The complete serialized JSON payload was passed to the Appendix B verifier before its one filesystem write. The verifier derives B by literal core multiplication, rather than the generator's piecewise0/4/-3±s construction.

It checked complete source/predicate set equality, all184 nonzero8-minors, all52 nonzero7-minors, all52 full-kernel basis identities and free-row independence, all52 weighted coordinate-norm identities with nonzero total weight, and the stated exact norm-span ranks. Positive arithmetic controls were `s*conjugate(s)=7` and `Q0^2=9I-J`.

Six independently injected **data corruptions** were rejected at their intended checks: missing required core (`COVERAGE_SET`), duplicate core (`DUPLICATE_ENTRY`), changed modular minor (`MODULAR_MINOR`), changed K-kernel entry (`KERNEL_IDENTITY`), zeroed norm witness (`NORM_SUM`), and altered nonzero norm identity (`NORM_IDENTITY`). These are same-author verifier controls, not three independent implementations.

- Certificate: [rt-residual-exact-algebra-certificate-v1.json](rt-residual-exact-algebra-certificate-v1.json), SHA256 `7c2122d71c77e30db513f3fc2939406f5bf4ab636866226b643f3e37656c2504`.
- Exact execution receipt: [rt-residual-in-kernel-receipt-v1.json](rt-residual-in-kernel-receipt-v1.json).
- Appendix B verifier source SHA256, including its final newline: `4c196d938e05f7cd7d424e7f6df463ce215ba7c1b23a35fb7f927b22db922df7`.
- Frozen parent manuscript: `off-axis-consolidated-orientation-v1.md`, SHA256 `9f1c469002abb6cc0c7bf5cb8bf9a7ca664773b6c4b70276516a565e6a3750c7`.

**Acceptance boundary:** this is the author's exact algebraic RT proof and same-session reconstruction. It has not been independently parent-replayed, cross-vendor reviewed, formally verified, novelty-cleared or triple-certified as a finite witness. The held native assay remains unrun/superseded. The result must not be substituted for the separate v28-A shared/star/matching reconstruction or for global conference-modulus/QLS compatibility.

## Appendix A. All52 exact rank7 norm identities

A tuple is written as its nine one-digit labels. In the lambda column `i:c` means the integer coefficient of physical coordinate i is c; omitted entries are zero. All sums in the final column are strictly positive. Every row is verified against the **entire** exact complex kernel supplied in the JSON.

| Canonical p | Branch | Norm span | Nonzero lambda entries | Sum lambda |
|---|---|---:|---|---:|
| 012378645 | R0 | 3 | `0:-9, 1:49` | 40 |
| 012387645 | R0 | 4 | `0:-86, 3:343` | 257 |
| 012456837 | R2 | 3 | `0:1` | 1 |
| 012564783 | R2 | 3 | `0:1` | 1 |
| 013284657 | R2 | 2 | `0:1` | 1 |
| 013426857 | R0 | 2 | `0:1` | 1 |
| 013462857 | R0 | 3 | `0:1` | 1 |
| 013546782 | R2 | 3 | `0:1` | 1 |
| 013648257 | R2 | 2 | `0:1` | 1 |
| 013724568 | R2 | 3 | `0:1` | 1 |
| 013824657 | R1 | 2 | `0:1` | 1 |
| 013842657 | R1 | 2 | `0:1` | 1 |
| 013846257 | R1 | 2 | `0:1` | 1 |
| 013864257 | R1 | 2 | `0:1` | 1 |
| 014523786 | R0 | 2 | `0:1` | 1 |
| 014583762 | R2 | 4 | `0:1337061, 1:415030, 2:256025, 3:-1006460, 5:-709324` | 292332 |
| 014726358 | R0 | 3 | `0:1` | 1 |
| 014732586 | R0 | 4 | `0:-45189, 1:1461524, 2:-192934, 3:215446, 4:-154672` | 1284175 |
| 015378642 | R0 | 2 | `0:1` | 1 |
| 015623487 | R0 | 3 | `0:1` | 1 |
| 015637284 | R1 | 2 | `0:1` | 1 |
| 015673284 | R1 | 2 | `0:1` | 1 |
| 015687342 | R0 | 4 | `0:288927, 1:-102312, 2:-55566, 3:39592, 4:-55566` | 115075 |
| 015827436 | R2 | 4 | `0:-640403, 1:129899, 2:-707168, 3:1138760, 4:216874` | 137962 |
| 041532768 | R0 | 2 | `0:1` | 1 |
| 041538726 | R2 | 4 | `0:1337061, 1:256025, 2:415030, 3:-1006460, 4:-709324` | 292332 |
| 041723568 | R0 | 4 | `0:-1319977, 1:3847186, 2:9343076, 3:-67914, 4:-3402784` | 8399587 |
| 041762385 | R0 | 3 | `0:1` | 1 |
| 042378615 | R0 | 2 | `0:1` | 1 |
| 042631587 | R0 | 3 | `0:1` | 1 |
| 042638157 | R1 | 2 | `0:1` | 1 |
| 042683157 | R1 | 2 | `0:1` | 1 |
| 042687315 | R0 | 4 | `0:194805, 1:55566, 2:-65268, 3:7252, 4:-55566` | 136789 |
| 042781563 | R2 | 4 | `0:-640403, 1:-707168, 2:129899, 3:1138760, 5:216874` | 137962 |
| 045123867 | R0 | 4 | `0:360, 1:-441, 2:980, 3:-196` | 703 |
| 045231786 | R0 | 4 | `0:360, 1:980, 2:-441, 3:-196` | 703 |
| 045678312 | R0 | 2 | `0:1` | 1 |
| 045687312 | R0 | 2 | `0:1` | 1 |
| 045726381 | R0 | 4 | `0:452, 1:9898, 2:-105, 4:-1442, 5:-28` | 8775 |
| 045861327 | R0 | 4 | `0:452, 1:-105, 2:9898, 4:-28, 5:-1442` | 8775 |
| 048156327 | R1 | 4 | `0:2150, 1:4067, 3:-4165, 4:-3640, 5:3052` | 1464 |
| 048156723 | R1 | 4 | `0:-14848, 1:21952, 2:3528, 3:141120, 4:-14553` | 137199 |
| 048165327 | R1 | 4 | `0:389748, 1:39690, 3:21511, 4:-88662, 5:-40306` | 321981 |
| 048165723 | R1 | 4 | `0:135544, 1:-198940, 2:198744, 3:-21756, 4:-63189` | 50403 |
| 048175623 | R2 | 4 | `0:-7320, 1:-25130, 2:11116, 3:91035, 4:6132` | 75833 |
| 048237561 | R1 | 4 | `0:-9892, 1:-14994, 2:87808, 3:26019, 4:19404` | 108345 |
| 048237651 | R1 | 4 | `0:2150, 2:4067, 3:-4165, 4:3052, 5:-3640` | 1464 |
| 048273561 | R1 | 4 | `0:-820226, 1:455406, 2:901649, 3:875175, 4:-252756` | 1159248 |
| 048273651 | R1 | 4 | `0:389748, 2:39690, 3:21511, 4:-40306, 5:-88662` | 321981 |
| 048275361 | R2 | 4 | `0:-7320, 1:11116, 2:-25130, 3:91035, 5:6132` | 75833 |
| 048523761 | R0 | 3 | `0:1` | 1 |
| 048532761 | R0 | 2 | `0:1` | 1 |

## Appendix B. Complete exact certificate verifier

This is the exact function source executed in the owner eval kernel. Its only input is the parsed attached JSON. Calling `verify_rt_certificate(document)` reconstructs all source coverage and checks every algebraic certificate. It performs no file access, network, subprocess launch, symbolic/native solver call or floating arithmetic. This code is reproduced as permanent proof evidence; no executable assay file is created or authorized.

```python
def verify_rt_certificate(doc):
    from fractions import Fraction
    from itertools import permutations
    from collections import Counter
    F = Fraction
    Z = (F(0), F(0))
    U = (F(1), F(0))
    def fail(reason):
        raise ValueError(reason)
    def add(x, y):
        return (x[0]+y[0], x[1]+y[1])
    def mul(x, y):
        return (x[0]*y[0]-7*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
    def bar(x):
        return (x[0], -x[1])
    def q(i, j):
        return 0 if i == j else (1 if i % 3 == j % 3 or i // 3 == j // 3 else -1)
    def eliminate(A, prime=None):
        B = [[(int(x) % prime if prime else F(x)) for x in row] for row in A]
        r = 0
        for j in range(len(B[0])):
            k = next((i for i in range(r, len(B)) if B[i][j]), None)
            if k is None:
                continue
            B[r], B[k] = B[k], B[r]
            inverse = pow(B[r][j], -1, prime) if prime else 1 / B[r][j]
            B[r] = [(x*inverse) % prime if prime else x*inverse for x in B[r]]
            for i in range(r+1, len(B)):
                c = B[i][j]
                B[i] = [(x-c*y) % prime if prime else x-c*y for x, y in zip(B[i], B[r])]
            r += 1
            if r == len(B):
                break
        return r
    def det11(A):
        B = [[x % 11 for x in row] for row in A]
        d = 1
        for j in range(len(B)):
            k = next((i for i in range(j, len(B)) if B[i][j]), None)
            if k is None:
                return 0
            if j != k:
                B[j], B[k] = B[k], B[j]
                d = -d
            d = d*B[j][j] % 11
            inverse = pow(B[j][j], -1, 11)
            for i in range(j+1, len(B)):
                c = B[i][j]*inverse % 11
                B[i] = [(x-c*y) % 11 for x, y in zip(B[i], B[j])]
        return d % 11
    rho = (0,7,8,6,5,4,3,1,2)
    pairs = ((4,5),(3,6),(1,7),(2,8))
    if doc['hypotheses']['rho'] != list(rho) or doc['hypotheses']['ordered_pairs'] != [list(x) for x in pairs]:
        fail('LITERAL_INPUT')
    if mul((F(0),F(1)), bar((F(0),F(1)))) != (F(7),F(0)):
        fail('CONTROL_NORM')
    if any(sum(q(i,k)*q(k,j) for k in range(9)) != (8 if i==j else -1) for i in range(9) for j in range(9)):
        fail('CONTROL_CHARACTER')
    def odd(p):
        return [[0 if a == b else (q(p[r],p[t])-q(p[r],p[tt])-q(p[rr],p[t])+q(p[rr],p[tt])) // 2
                 for b,(t,tt) in enumerate(pairs)] for a,(r,rr) in enumerate(pairs)]
    A0 = odd(tuple(range(9)))
    tables = {}
    normalized = 0
    for tail in permutations(range(1,9)):
        p = (0,) + tail
        key = tuple(q(p[i],p[j]) for i in range(9) for j in range(i+1,9))
        tables.setdefault(key, p)
        normalized += 1
    expected = {}
    for p in tables.values():
        A = odd(p)
        if eliminate([[A[i][j]+A0[i][j] for j in range(4)] for i in range(4)], 7) != 2:
            continue
        degree = sum(x != 0 for x in A[0])
        magnitudes = sorted(abs(A[i][j]) for i in range(4) for j in range(i+1,4) if A[i][j])
        branch = ('R0' if degree == 0 and magnitudes == [1,1,2] else
                  'R1' if degree == 1 and len(magnitudes) == 4 else
                  'R2' if degree == 2 else None)
        if branch:
            expected[p] = branch
    if normalized != 40320 or len(tables) != 5040:
        fail('SOURCE_COVERAGE')
    supplied = {}
    for entry in doc['rows']:
        p = tuple(entry['p'])
        if p in supplied:
            fail('DUPLICATE_ENTRY')
        supplied[p] = entry
    if set(supplied) != set(expected):
        fail('COVERAGE_SET')
    counts = Counter()
    norms = Counter()
    for p, branch in expected.items():
        e = supplied[p]
        if e['branch'] != branch:
            fail('BRANCH_PREDICATE')
        B = []
        for i in range(9):
            row = []
            for t in range(9):
                a, b = q(t,i), q(p[t],p[rho[i]])
                row.append(Z if t == i or t == rho[i] else (F(1+7*a*b,2), F(b-a,2)))
            B.append(row)
        r, c = e['minor_rows'], e['minor_columns']
        n = 8 if e['kind'] == 'rank_at_least_eight' else 7
        if len(r) != n or len(c) != n or len(set(r)) != n or len(set(c)) != n or any(not 0 <= x < 9 for x in r+c):
            fail('MINOR_INDICES')
        d = det11([[int(B[i][j][0]+2*B[i][j][1]) for j in c] for i in r])
        if d == 0 or d != e['minor_mod11_s2']:
            fail('MODULAR_MINOR')
        counts[(branch,e['kind'])] += 1
        if n == 8:
            continue
        if e['kind'] != 'rank_seven_norm_contradiction':
            fail('CERTIFICATE_KIND')
        V = [[tuple(F(x) for x in a) for a in row] for row in e['kernel_basis']]
        free = e['kernel_free_rows']
        if len(V) != 9 or any(len(row) != 2 or any(len(x) != 2 for x in row) for row in V) or len(free) != 2 or len(set(free)) != 2 or any(not 0 <= x < 9 for x in free):
            fail('KERNEL_DIMENSIONS')
        if any(V[free[j]][k] != (U if j==k else Z) for j in range(2) for k in range(2)):
            fail('KERNEL_INDEPENDENCE')
        if any(tuple(sum(mul(B[i][t],V[t][k])[h] for t in range(9)) for h in range(2)) != Z for i in range(9) for k in range(2)):
            fail('KERNEL_IDENTITY')
        lam = e['lambda']
        if len(lam) != 9 or any(type(x) is not int for x in lam):
            fail('NORM_DIMENSIONS')
        forms = []
        for v,w in V:
            cross = mul(v,bar(w))
            forms.append((mul(v,bar(v))[0],mul(w,bar(w))[0],2*cross[0],-14*cross[1]))
        if any(sum(lam[i]*forms[i][j] for i in range(9)) for j in range(4)):
            fail('NORM_IDENTITY')
        if sum(lam) == 0 or sum(lam) != e['lambda_sum']:
            fail('NORM_SUM')
        normrank = eliminate(forms)
        if normrank != e['hermitian_norm_span_rank']:
            fail('NORM_SPAN')
        norms[(branch,normrank)] += 1
    return {'normalized_permutations':normalized,'distinct_literal_tables':len(tables),
            'complete_residual_leading_candidates':len(expected),
            'counts':{str(k):v for k,v in sorted(counts.items())},
            'norm_span_counts':{str(k):v for k,v in sorted(norms.items())},
            'exact_kernel_identities':sum(v for (b,k),v in counts.items() if k=='rank_seven_norm_contradiction'),
            'nonzero_integer_equal_norm_contradictions':sum(v for (b,k),v in counts.items() if k=='rank_seven_norm_contradiction'),
            'control_character_identity':True,'control_norm_s':True,
            'all_complex_phase_vectors_excluded_in_every_rank_seven_residual_input':True}
```

## Park boundary

RT's literal residual rank7 torus gap is closed at WRITTEN-checked-in-kernel level by the supplied exact algebraic certificates. Independent reconstruction remains open. The whole all-P orientation conclusion remains contingent on its separate earlier shared/family/exhaustiveness gates; unrestricted maximal1-RQLS10 remains UNKNOWN.
