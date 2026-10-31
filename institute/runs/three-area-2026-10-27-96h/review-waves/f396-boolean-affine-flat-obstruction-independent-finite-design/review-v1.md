# author-candidate-v1.md

## Independent finite-check design for the Boolean affine-flat obstruction

**Role:** FINITE  
**Execution status:** **NOTRUN**  
**Scientific status:** Independent written reconstruction and complete runnable checker supplied below. No executed finite certificate, parent adoption, whole-proof acceptance, actual \(U/V\) witness, or original-target resolution is claimed.

The read-only reviewer tool policy prohibits scientific execution and filesystem edits. I therefore return the complete body and source for Main’s materialization and one parent-controlled run, as expressly permitted by the frozen assignment.

## 1. Frozen-input audit and chronology

### Bindings

| Item | Supplied SHA-256 | Supplied bytes / LF |
|---|---|---:|
| Manifest | `bfa943fd72dd0521335397b08ff3a8fb09d51e397ed03538e8d4e5dc6eb016b8` | 5491 / 73 |
| Freeze receipt | `2b437c91531c28b31878adf20a12d11057b5a18388deced19905032e33579983` | 1399 / 34 |
| Literal packet | `726353c0b3ee36def5d9707a913fe15180fb4c79f5174d02bb011af113244fc1` | 25757 / 632 |
| Complete author source S1 | `3c18f0df77421c82e9c75962381d50f9202df6c69ad53b8c57f071b8062e70e5` | 21418 / 629 |

The manifest and receipt bindings agree with the assignment. The freeze receipt records source stability and selected-line byte equality before dispatch. The separate dispatch receipt records this FINITE duty.

**Hash, byte-count, LF-count, and clock evidence are parent-supplied, not independently executed by me.** Specifically, `parent-live-metadata-supply-v1.json` supplies the parent observation `2026-10-30T10:35:40-0700 PDT`; the parent’s message reports all assigned pins/bytes/LF matching. This is neither my native research-start clock nor an observed completion clock.

### Complete reads

Before opening the scientific packet, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all seven assigned permission/status controls:

1. `prospective-author-method-scope-restoration-20261030-v1.json`
2. `contract-addendum-2-frontier-first-owner-direction-v1.json`
3. `parent-L1-selected-diagnostic-release-quarantine-v1.json`
4. `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`
5. `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`
6. `parent-ame-held-compression-claim-consumer-quarantine-v1.json`
7. `parent-held-ph-registration-report-consumer-quarantine-v1.json`

I then read the complete literal packet in consecutive raw windows of at most 20 physical lines: 1–20, 21–40, …, 601–620, and 621–632. This includes the complete author body through the final `S1|630` line. The supplied LF count and rendered source-line labels were not treated as interchangeable quantities.

Only afterward did I develop the written checks and fresh finite-control fixtures below. No author executable was supplied or imported. No linked historical scientific body, held payload, held consumer, sibling outcome, external-model CLI, public-source search, scientific executable, or repository write was used. No cognition/separation certificate is claimed.

## 2. Exact finite claims and written frequencies

### 2.1 Four-bit classification

For \(f:\mathbb F_2^4\to\{\pm1\}\), let

\[
B(y)=\sum_h f(h)(-1)^{y\cdot h}.
\]

The property to check is

\[
\#\{y:B(y)\not\equiv0\pmod3\}\le4.
\]

Its two claimed classes are:

- A signed character: one nonzero coefficient, equal to \(\pm16\).
- A spectrum supported on an affine two-flat, with four coefficients of magnitude eight and negative coefficient-sign product.

The second class is **not** an ordinary bent function on four variables; it has four nonzero Walsh coefficients, rather than sixteen coefficients of magnitude four.

Here is a self-contained written reconstruction. Modulo three, the inverse factor is \(16^{-1}=1\). Thus \(f\) is the inverse character sum of at most four nonzero residues, and that sum must never vanish.

- Zero terms cannot represent a sign function.
- One term gives a signed character.
- Two distinct terms cancel somewhere.
- For three distinct frequencies, their two relative directions are independent. Their relative character values can make all three summands equal, yielding zero modulo three.
- Four frequencies either have affine dimension three or form an affine two-flat. In affine dimension three, the three relative characters attain all sign triples, including a choice giving two positive and two negative summands.
- On an affine two-flat, four coefficient signs with product \(+1\) give a real character sum that is zero at twelve of the sixteen points. Product \(-1\) gives values \(\pm2\) everywhere. In the latter case the unique sign function having those residues is minus half that character sum, and its actual Walsh coefficients are the four values \(\pm8\), with negative sign product.

Conversely, every signed character and every stated four-flat spectrum inverts to a sign function and meets the modulo-three support condition.

The resulting exact **written counts**, independently encoded as expectations in the checker, are:

| Class | Count |
|---|---:|
| Signed characters | \(16\cdot2=32\) |
| Affine two-flats in \(\mathbb F_2^4\) | \(35\cdot4=140\) |
| Negative-product sign assignments on each two-flat | \(8\) |
| Four-flat-spectrum sign functions | \(140\cdot8=1120\) |
| Total eligible sign functions | **1152** |
| Ineligible among all \(2^{16}\) sign functions | **64384** |

The 35 directions follow by counting ordered independent pairs and dividing by the six ordered bases of a two-dimensional binary space: \(15\cdot14/6=35\). Different spectral data give different functions by Fourier inversion.

**These are written mathematical counts, not reported enumeration output.**

The checker independently:

1. Generates all 65,536 sign vectors.
2. Computes their exact integer FWHT.
3. Compares every FWHT with a separate direct character-sum implementation.
4. Applies the modulo-three eligibility test.
5. Compares the resulting entire eligible mask-to-class map with a separately constructed inverse-spectrum catalog—not merely its cardinality.
6. Prints the full observed modulo-three support-size histogram if run successfully.

### 2.2 Four-point balanced signs

There are **six**, not sixteen, balanced sign functions on four points:

\[
\binom42=6.
\]

They are exactly the two signs of each of the three nontrivial characters of \(\mathbb F_2^2\). Each has direct Walsh transform supported at precisely one nonzero frequency, with value \(\pm4\). Multiplying the sign function by three therefore produces exactly one coefficient \(\pm12\).

The remaining ten sign functions comprise two constants and eight functions with one or three negative entries. The direct-transform DC-value frequencies are

\[
-4:1,\quad -2:4,\quad 0:6,\quad 2:4,\quad 4:1.
\]

The all-zero vector is outside the sign-function domain. A control explicitly rejects it before any balancing/routing interpretation.

### 2.3 Exhaustive \(\beta,\alpha\) cases

Fix a canonical affine two-flat \(T=\{0,1,2,3\}\subset\mathbb F_2^4\). There are eight choices of \(\beta:T\to\{\pm1\}\) with product \(-1\), and \(4^4=256\) maps \(\alpha:T\to\mathbb F_2^2\). Thus the assigned exhaustion has **2048 cases**.

For each nonzero \(d\), define

\[
\gamma_d(y)=-\beta(y)(-1)^{\alpha(y)\cdot d},
\qquad
x=\bigoplus_{y\in T}\alpha(y).
\]

Direct multiplication gives

\[
\prod_{y\in T}\gamma_d(y)=-(-1)^{x\cdot d}.
\]

The checker directly evaluates the sixteen real character sums and counts their nonzero modulo-three values. It does not obtain the support count merely by assigning the expected answer.

With \(d\) ordered as \(1,2,3\), the exact written frequencies are:

| \(x\) | Support-size triple | Number of \((\beta,\alpha)\) cases |
|---:|---|---:|
| 0 | \((16,16,16)\) | 512 |
| 1 | \((4,16,4)\) | 512 |
| 2 | \((16,4,4)\) | 512 |
| 3 | \((4,4,16)\) | 512 |

For any fixed \(x\), the first three labels can be chosen arbitrarily and determine the fourth, giving 64 label maps, multiplied by eight \(\beta\) assignments.

Using the canonical flat does not narrow this support-count lemma: translation of a spectral flat multiplies its real character sum by a character; an invertible linear coordinate change permutes the primal points. Neither changes zeros or absolute values. Independently, the four-bit classification catalog covers **all 140 affine two-flats**.

## 3. Consuming-side routing and deficit contradiction

For each exceptional frequency, the checker verifies the full four-point inversion, including the factor \(1/4\):

\[
\kappa(z)=\beta(3-4\mathbf1_{\{z=\alpha\}}),
\]

so

\[
B_0=8\beta,\qquad
B_d=-4\beta(-1)^{\alpha\cdot d}\quad(d\ne0).
\]

For each of the twelve remaining frequencies, the balanced four-point classification gives one—and only one—nonzero receiving coset \(d\), with coefficient \(\pm12\). Consequently the consuming-side counts satisfy

\[
n_1+n_2+n_3=12.
\]

This identity does not require enumeration of all independent sign/label choices at the twelve positions: every position routes exactly once, and its sign does not alter its receiving coset. The checker constructs all **91** nonnegative count triples summing to twelve and checks the routing/count correspondence.

For an actual even-valued coset function \(g\), Parseval and the coefficient magnitudes require

\[
\sum_h g(h)^2
=\frac{4\cdot4^2+144n_d}{16}
=4+9n_d.
\]

Evenness implies \(n_d\equiv0\pmod4\). Support size \(m_d\) further requires

\[
4+9n_d\ge4m_d.
\]

Thus:

- \(m_d=16\) requires \(n_d\ge8\).
- \(m_d=4\) requires \(n_d\ge4\).

For \(x=0\), the minimum total is \(24>12\). For \(x\ne0\), it is \(16>12\). Both formal necessary systems are impossible.

### Essential-constraint mutation controls

These are prospective controls in the supplied source, **not observed passes**:

| Mutation | Fixture / effect | Required rejection |
|---|---|---|
| Wrong modulo-three inverse factor | Factor two instead of one negates a sign function’s residues; Booleanity alone would not catch this | `MOD3_INVERSE` |
| Wrong four-coefficient sign product | Product-positive coefficients invert to zeros and values of magnitude two, not a sign function | `FOUR_SIGN_PRODUCT` |
| Missing minus sign in the coset product formula | Compares directly multiplied \(\gamma_d\) signs with the wrong prediction | `COSET_SIGN_PRODUCT` |
| Wrong 16-point Fourier inverse scaling | Divide by eight instead of sixteen | `H_SCALE` |
| Wrong four-point partial inverse scaling | Divide the transform of \(4\kappa\) by two instead of four | `PARTIAL_SCALING` |
| Drop \(n_d\in4\mathbb Z\) | \((m_d)=(16,4,4)\), \((n_d)=(7,2,3)\) meets the retained total and energy lower bounds | `NDIV4` |
| Drop the fixed total, nonzero-\(x\) branch | \((8,4,4)\) meets divisibility and lower bounds but totals sixteen | `TOTAL12` |
| Drop the fixed total, zero-\(x\) branch | \((8,8,8)\) meets divisibility and lower bounds but totals twenty-four | `TOTAL12` |

The checker also verifies that dropping divisibility alone leaves three formal solutions in each nonzero-\(x\) branch, but none in the zero-\(x\) branch. Dropping the fixed total leaves eighteen formal solutions in each nonzero-\(x\) branch and eight in the zero-\(x\) branch, with each count restricted to \(0\le n_d\le12\).

Those weakened-system fixtures are **not actual \(u\)-blocks or witnesses**. They demonstrate why the omitted necessary conditions matter.

## 4. Execution contract and exact unpaid boundaries

**Observed execution results: none.** The checker has not been run, syntax-checked, benchmarked, or independently adopted.

Parent execution argv, after materializing the source as `checker_f396_finite_v1.py`:

**`python3 -I -B checker_f396_finite_v1.py`**

Requirements: Python 3.10 or later; standard library only; no input files or arguments.

The checker explicitly opens no files, uses no network, launches no children, installs nothing, deletes nothing, and retains no campaign. It streams the 65,536 sign vectors rather than storing them all. It includes a cooperative 50-second guard and emits its final PASS only after all checks. Actual runtime and memory remain unobserved; the cooperative guard is not a hard real-time guarantee against host suspension or blocked output.

The following remain unpaid:

1. **Execution:** Main must pin the materialized checker and record its one actual run before treating it as executed finite evidence.
2. **Actual-object import:** The finite checks verify small Fourier classifications, routing identities, and impossible necessary count systems. They do not enumerate or construct actual eight-bit \(u\), holes, \(V\), or full complementarity.
3. **Condition (M):** Application to the structural actual-\(U\) obstruction retains the complete second-fibre magnitude hypothesis: four coefficients of magnitude four and sixty of magnitude twelve.
4. **Historical rank identification:** No conversion of the historical term “rank2” into the explicitly defined quadratic parity rank, or identification of historical common fibres with parity cosets, is established here.
5. **Scope:** No exclusion of non-affine \(S\), arbitrary eight-bit callers, the complete \(m=116\) residual, or the original nine-variable target is claimed.
6. **Acceptance and novelty:** Parent disposition, disjoint whole-proof review, formal verification, and novelty review are not supplied by this finite design.

## 5. Complete checker source

For lossless plain-text transport, every source line below starts with `PY|`. Remove exactly that three-character prefix from each such line, preserving the remainder and line order. The source is complete; no omitted functions or placeholders are required.

BEGIN PYTHON SOURCE
PY|from collections import Counter
PY|from itertools import product
PY|from time import monotonic
PY|import sys
PY|
PY|
PY|class CheckFailure(RuntimeError):
PY|    def __init__(self, code, detail=""):
PY|        self.code = code
PY|        super().__init__(code + (": " + detail if detail else ""))
PY|
PY|
PY|def need(condition, code, detail=""):
PY|    if not condition:
PY|        raise CheckFailure(code, detail)
PY|
PY|
PY|def deadline(start):
PY|    need(monotonic() - start < 50.0, "DEADLINE",
PY|         "Cooperative limit reached; no completed finite certificate.")
PY|
PY|
PY|def sign_product(values):
PY|    result = 1
PY|    for value in values:
PY|        result *= value
PY|    return result
PY|
PY|
PY|def character_table(n):
PY|    return tuple(
PY|        tuple(1 - 2 * ((a & b).bit_count() & 1) for b in range(n))
PY|        for a in range(n)
PY|    )
PY|
PY|
PY|W4 = character_table(4)
PY|W16 = character_table(16)
PY|T0 = (0, 1, 2, 3)
PY|BETAS = tuple(
PY|    beta for beta in product((-1, 1), repeat=4)
PY|    if sign_product(beta) == -1
PY|)
PY|
PY|
PY|def direct(values, table):
PY|    return tuple(sum(a * b for a, b in zip(values, row))
PY|                 for row in table)
PY|
PY|
PY|def fwht(values):
PY|    out = list(values)
PY|    n = len(out)
PY|    need(n > 0 and (n & (n - 1)) == 0, "POWER_OF_TWO")
PY|    width = 1
PY|    while width < n:
PY|        for base in range(0, n, 2 * width):
PY|            for offset in range(width):
PY|                i = base + offset
PY|                a, b = out[i], out[i + width]
PY|                out[i], out[i + width] = a + b, a - b
PY|        width *= 2
PY|    return tuple(out)
PY|
PY|
PY|def mask_of(values):
PY|    need(len(values) == 16 and all(v in (-1, 1) for v in values),
PY|         "NOT_SIGN_FUNCTION")
PY|    return sum((v == -1) << i for i, v in enumerate(values))
PY|
PY|
PY|def affine_two(points):
PY|    if len(points) != 4:
PY|        return False
PY|    translated = {p ^ points[0] for p in points}
PY|    return len(translated) == 4 and all(
PY|        (a ^ b) in translated for a in translated for b in translated
PY|    )
PY|
PY|
PY|def flat_values(points, beta):
PY|    phase = tuple(
PY|        sum(beta[i] * W16[points[i]][h] for i in range(4))
PY|        for h in range(16)
PY|    )
PY|    need(all(abs(v) == 2 for v in phase), "FOUR_SIGN_PRODUCT")
PY|    return tuple(v // 2 for v in phase)
PY|
PY|
PY|def make_catalog(start):
PY|    directions = {
PY|        tuple(sorted((0, a, b, a ^ b)))
PY|        for a in range(1, 16) for b in range(a + 1, 16)
PY|    }
PY|    need(len(directions) == 35, "DIRECTION_COUNT")
PY|    flats = {
PY|        tuple(sorted(t ^ v for v in direction))
PY|        for direction in directions for t in range(16)
PY|    }
PY|    need(len(flats) == 140 and all(affine_two(t) for t in flats),
PY|         "AFFINE_FLAT_CATALOG")
PY|    catalog = {}
PY|    for y in range(16):
PY|        for sign in (-1, 1):
PY|            values = tuple(sign * c for c in W16[y])
PY|            mask = mask_of(values)
PY|            need(mask not in catalog, "CATALOG_DUPLICATE")
PY|            catalog[mask] = "character"
PY|    for points in sorted(flats):
PY|        for beta in BETAS:
PY|            values = flat_values(points, beta)
PY|            coefficients = dict(zip(points, beta))
PY|            expected = tuple(8 * coefficients.get(y, 0)
PY|                             for y in range(16))
PY|            need(direct(values, W16) == expected,
PY|                 "CATALOG_INVERSE_SPECTRUM")
PY|            mask = mask_of(values)
PY|            need(mask not in catalog, "CATALOG_DUPLICATE")
PY|            catalog[mask] = "four-flat-spectrum"
PY|        deadline(start)
PY|    need(Counter(catalog.values()) == Counter({
PY|        "character": 32, "four-flat-spectrum": 1120
PY|    }), "CATALOG_CLASS_COUNTS")
PY|    return catalog
PY|
PY|
PY|def classify(spectrum):
PY|    support = tuple(i for i, value in enumerate(spectrum) if value)
PY|    if len(support) == 1 and abs(spectrum[support[0]]) == 16:
PY|        return "character"
PY|    if (len(support) == 4
PY|            and all(abs(spectrum[i]) == 8 for i in support)
PY|            and affine_two(support)
PY|            and sign_product(
PY|                1 if spectrum[i] > 0 else -1 for i in support
PY|            ) == -1):
PY|        return "four-flat-spectrum"
PY|    return None
PY|
PY|
PY|def exhaust_signs(catalog, start):
PY|    histogram = Counter()
PY|    eligible = {}
PY|    for mask in range(1 << 16):
PY|        values = tuple(1 - 2 * ((mask >> i) & 1) for i in range(16))
PY|        spectrum = fwht(values)
PY|        need(spectrum == direct(values, W16), "FWHT_DIRECT_DISAGREE",
PY|             "mask=" + str(mask))
PY|        residue_support = sum(value % 3 != 0 for value in spectrum)
PY|        histogram[residue_support] += 1
PY|        if residue_support <= 4:
PY|            label = classify(spectrum)
PY|            need(label is not None, "UNCLASSIFIED_ELIGIBLE",
PY|                 "mask=" + str(mask))
PY|            eligible[mask] = label
PY|        if (mask & 127) == 0:
PY|            deadline(start)
PY|    need(sum(histogram.values()) == 65536, "EXHAUSTION_COUNT")
PY|    need(eligible == catalog, "CLASSIFICATION_SET_COMPLETENESS")
PY|    need(histogram[1] == 32 and histogram[4] == 1120
PY|         and all(histogram[k] == 0 for k in (0, 2, 3)),
PY|         "SMALL_RESIDUE_SUPPORT_COUNTS")
PY|    return histogram, Counter(eligible.values())
PY|
PY|
PY|def balanced_route(values):
PY|    need(len(values) == 4 and all(v in (-1, 1) for v in values),
PY|         "FOUR_POINT_DOMAIN")
PY|    spectrum = direct(values, W4)
PY|    need(spectrum[0] == 0, "FOUR_POINT_UNBALANCED")
PY|    support = tuple(i for i, v in enumerate(spectrum) if v)
PY|    need(len(support) == 1 and support[0] != 0
PY|         and abs(spectrum[support[0]]) == 4, "FOUR_POINT_ROUTE")
PY|    d = support[0]
PY|    eta = spectrum[d] // 4
PY|    need(tuple(values) == tuple(eta * c for c in W4[d]),
PY|         "FOUR_POINT_CHARACTER")
PY|    return d, eta
PY|
PY|
PY|def check_partial(kappa, expected, denominator=4):
PY|    full = direct(tuple(4 * v for v in kappa), W4)
PY|    need(denominator > 0
PY|         and all(v % denominator == 0 for v in full),
PY|         "PARTIAL_SCALING")
PY|    received = tuple(v // denominator for v in full)
PY|    need(received == tuple(expected), "PARTIAL_SCALING")
PY|    return received
PY|
PY|
PY|def check_four_points():
PY|    dc_counts, routes = Counter(), Counter()
PY|    for mask in range(16):
PY|        values = tuple(1 - 2 * ((mask >> i) & 1) for i in range(4))
PY|        spectrum = direct(values, W4)
PY|        need(fwht(values) == spectrum, "FOUR_POINT_FWHT")
PY|        dc_counts[spectrum[0]] += 1
PY|        if spectrum[0] == 0:
PY|            d, eta = balanced_route(values)
PY|            routes[d] += 1
PY|            expected = tuple(12 * eta if j == d else 0
PY|                             for j in range(4))
PY|            check_partial(tuple(3 * v for v in values), expected)
PY|    need(dc_counts == Counter({-4: 1, -2: 4, 0: 6, 2: 4, 4: 1}),
PY|         "FOUR_POINT_DC_COUNTS")
PY|    need(routes == Counter({1: 2, 2: 2, 3: 2}),
PY|         "BALANCED_ROUTE_COMPLETENESS")
PY|    for beta in (-1, 1):
PY|        for alpha in range(4):
PY|            kappa = tuple(beta * (3 - 4 * (z == alpha))
PY|                          for z in range(4))
PY|            expected = tuple(
PY|                8 * beta if d == 0 else -4 * beta * W4[d][alpha]
PY|                for d in range(4)
PY|            )
PY|            check_partial(kappa, expected)
PY|    return dc_counts, routes
PY|
PY|
PY|def check_mod3_inverse(values, spectrum, factor=1):
PY|    received = tuple((factor * v) % 3
PY|                     for v in direct(spectrum, W16))
PY|    need(received == tuple(v % 3 for v in values), "MOD3_INVERSE")
PY|
PY|
PY|def check_h_inverse(values, spectrum, denominator=16):
PY|    numerator = direct(spectrum, W16)
PY|    need(denominator > 0
PY|         and all(v % denominator == 0 for v in numerator),
PY|         "H_SCALE")
PY|    need(tuple(v // denominator for v in numerator) == tuple(values),
PY|         "H_SCALE")
PY|
PY|
PY|def coset_summary(beta, labels, prediction_sign=-1):
PY|    need(len(beta) == 4 and all(v in (-1, 1) for v in beta)
PY|         and sign_product(beta) == -1, "BETA_DOMAIN")
PY|    need(len(labels) == 4 and all(a in range(4) for a in labels),
PY|         "LABEL_DOMAIN")
PY|    x = 0
PY|    for label in labels:
PY|        x ^= label
PY|    supports = []
PY|    for d in (1, 2, 3):
PY|        gamma = tuple(-beta[i] * W4[d][labels[i]] for i in range(4))
PY|        actual_product = sign_product(gamma)
PY|        need(actual_product == prediction_sign * W4[d][x],
PY|             "COSET_SIGN_PRODUCT")
PY|        phase = tuple(
PY|            sum(gamma[i] * W16[T0[i]][h] for i in range(4))
PY|            for h in range(16)
PY|        )
PY|        if actual_product == -1:
PY|            need(all(abs(v) == 2 for v in phase), "COSET_PHASE")
PY|        else:
PY|            need(phase.count(0) == 12
PY|                 and all(v in (-4, 0, 4) for v in phase), "COSET_PHASE")
PY|        m = sum(v % 3 != 0 for v in phase)
PY|        need(m == (16 if W4[d][x] == 1 else 4), "COSET_SUPPORT")
PY|        supports.append(m)
PY|    return x, tuple(supports)
PY|
PY|
PY|def exhaust_cosets(start):
PY|    patterns, xor_counts = Counter(), Counter()
PY|    total = 0
PY|    for beta in BETAS:
PY|        for labels in product(range(4), repeat=4):
PY|            x, supports = coset_summary(beta, labels)
PY|            xor_counts[x] += 1
PY|            patterns[supports] += 1
PY|            total += 1
PY|        deadline(start)
PY|    need(total == 2048, "COSET_CASE_COUNT")
PY|    need(xor_counts == Counter({0: 512, 1: 512, 2: 512, 3: 512}),
PY|         "XOR_LABEL_FREQUENCIES")
PY|    need(patterns == Counter({
PY|        (16, 16, 16): 512,
PY|        (4, 16, 4): 512,
PY|        (16, 4, 4): 512,
PY|        (4, 4, 16): 512,
PY|    }), "COSET_PATTERN_FREQUENCIES")
PY|    return patterns, xor_counts
PY|
PY|
PY|def check_shadow(ms, ns, mod4=True, total12=True):
PY|    need(len(ms) == len(ns) == 3
PY|         and all(m in (4, 16) for m in ms)
PY|         and all(isinstance(n, int) and 0 <= n <= 12 for n in ns),
PY|         "SHADOW_DOMAIN")
PY|    if total12:
PY|        need(sum(ns) == 12, "TOTAL12")
PY|    if mod4:
PY|        need(all(n % 4 == 0 for n in ns), "NDIV4")
PY|    need(all(4 + 9 * n >= 4 * m for m, n in zip(ms, ns)),
PY|         "ENERGY_LOWER")
PY|
PY|
PY|def shadow_solutions(ms, mod4=True, total12=True):
PY|    return tuple(
PY|        ns for ns in product(range(13), repeat=3)
PY|        if (not total12 or sum(ns) == 12)
PY|        and (not mod4 or all(n % 4 == 0 for n in ns))
PY|        and all(4 + 9 * n >= 4 * m for m, n in zip(ms, ns))
PY|    )
PY|
PY|
PY|def check_deficits(patterns):
PY|    partitions = set()
PY|    for a in range(13):
PY|        for b in range(13 - a):
PY|            c = 12 - a - b
PY|            receiving_labels = (1,) * a + (2,) * b + (3,) * c
PY|            ns = tuple(receiving_labels.count(d) for d in (1, 2, 3))
PY|            need(ns == (a, b, c) and sum(ns) == 12,
PY|                 "TWELVE_FREQUENCY_ROUTING")
PY|            partitions.add(ns)
PY|    need(len(partitions) == 91, "PARTITION_COUNT")
PY|    need(partitions == {
PY|        ns for ns in product(range(13), repeat=3) if sum(ns) == 12
PY|    }, "PARTITION_COMPLETENESS")
PY|    minima = {
PY|        m: min(n for n in range(13)
PY|               if n % 4 == 0 and 4 + 9 * n >= 4 * m)
PY|        for m in (4, 16)
PY|    }
PY|    need(minima == {4: 4, 16: 8}, "COUNT_LOWER_BOUNDS")
PY|    summaries = []
PY|    for ms in sorted(patterns):
PY|        need(not shadow_solutions(ms), "SHADOW_SURVIVOR", str(ms))
PY|        no_div = len(shadow_solutions(ms, mod4=False))
PY|        no_total = len(shadow_solutions(ms, total12=False))
PY|        all_large = ms == (16, 16, 16)
PY|        need(no_div == (0 if all_large else 3),
PY|             "DROPPED_DIVISIBILITY_COUNT")
PY|        need(no_total == (8 if all_large else 18),
PY|             "DROPPED_TOTAL_COUNT")
PY|        summaries.append((ms, no_div, no_total))
PY|    return minima, summaries
PY|
PY|
PY|def expect_rejection(name, expected_code, action, controls):
PY|    try:
PY|        action()
PY|    except CheckFailure as error:
PY|        need(error.code == expected_code, "WRONG_REJECTION_REASON",
PY|             name + ": received " + error.code)
PY|        controls.append((name, expected_code))
PY|        return
PY|    raise CheckFailure("CONTROL_NOT_REJECTED", name)
PY|
PY|
PY|def main():
PY|    start = monotonic()
PY|    need(len(sys.argv) == 1, "ARGV", "This checker accepts no arguments.")
PY|    catalog = make_catalog(start)
PY|    histogram, class_counts = exhaust_signs(catalog, start)
PY|    dc_counts, routes = check_four_points()
PY|    patterns, xor_counts = exhaust_cosets(start)
PY|    minima, shadow_counts = check_deficits(patterns)
PY|
PY|    constant = (1,) * 16
PY|    bent_quotient = flat_values(T0, (-1, 1, 1, 1))
PY|    constant_spectrum = direct(constant, W16)
PY|    bent_spectrum = direct(bent_quotient, W16)
PY|    for values, spectrum in (
PY|        (constant, constant_spectrum), (bent_quotient, bent_spectrum)
PY|    ):
PY|        check_mod3_inverse(values, spectrum)
PY|        check_h_inverse(values, spectrum)
PY|
PY|    controls = []
PY|    expect_rejection(
PY|        "wrong-mod3-inverse-factor", "MOD3_INVERSE",
PY|        lambda: check_mod3_inverse(constant, constant_spectrum, factor=2),
PY|        controls)
PY|    expect_rejection(
PY|        "positive-four-sign-product", "FOUR_SIGN_PRODUCT",
PY|        lambda: flat_values(T0, (1, 1, 1, 1)), controls)
PY|    expect_rejection(
PY|        "wrong-coset-product-sign", "COSET_SIGN_PRODUCT",
PY|        lambda: coset_summary((-1, 1, 1, 1), (0, 0, 0, 0),
PY|                              prediction_sign=1),
PY|        controls)
PY|    expect_rejection(
PY|        "wrong-sixteen-point-scale", "H_SCALE",
PY|        lambda: check_h_inverse(bent_quotient, bent_spectrum,
PY|                                denominator=8),
PY|        controls)
PY|    expect_rejection(
PY|        "wrong-four-point-scale", "PARTIAL_SCALING",
PY|        lambda: check_partial((-1, 3, 3, 3), (8, -4, -4, -4),
PY|                              denominator=2),
PY|        controls)
PY|
PY|    check_shadow((16, 4, 4), (7, 2, 3), mod4=False)
PY|    expect_rejection(
PY|        "dropping-n-divisible-four", "NDIV4",
PY|        lambda: check_shadow((16, 4, 4), (7, 2, 3)), controls)
PY|    check_shadow((16, 4, 4), (8, 4, 4), total12=False)
PY|    expect_rejection(
PY|        "dropping-total-nonzero-x", "TOTAL12",
PY|        lambda: check_shadow((16, 4, 4), (8, 4, 4)), controls)
PY|    check_shadow((16, 16, 16), (8, 8, 8), total12=False)
PY|    expect_rejection(
PY|        "dropping-total-zero-x", "TOTAL12",
PY|        lambda: check_shadow((16, 16, 16), (8, 8, 8)), controls)
PY|    expect_rejection(
PY|        "zero-is-not-a-sign-function", "FOUR_POINT_DOMAIN",
PY|        lambda: balanced_route((0, 0, 0, 0)), controls)
PY|    expect_rejection(
PY|        "constant-is-not-balanced", "FOUR_POINT_UNBALANCED",
PY|        lambda: balanced_route((1, 1, 1, 1)), controls)
PY|
PY|    need(len(controls) == 10, "CONTROL_COUNT")
PY|    deadline(start)
PY|    print("enumerated_sign_vectors", 65536)
PY|    print("residue_nonzero_histogram", sorted(histogram.items()))
PY|    print("eligible_class_counts", sorted(class_counts.items()))
PY|    print("ineligible_count", 65536 - sum(class_counts.values()))
PY|    print("four_point_dc_counts", sorted(dc_counts.items()))
PY|    print("balanced_receiving_routes", sorted(routes.items()))
PY|    print("coset_support_patterns", sorted(patterns.items()))
PY|    print("xor_label_counts", sorted(xor_counts.items()))
PY|    print("necessary_count_minima", sorted(minima.items()))
PY|    print("shadow_counts_ms_no_div_no_total", shadow_counts)
PY|    print("intended_rejections", controls)
PY|    print("elapsed_seconds", round(monotonic() - start, 6))
PY|    print("RESULT: PASS (finite lemmas and formal necessary shadows only)")
PY|
PY|
PY|if __name__ == "__main__":
PY|    try:
PY|        main()
PY|    except CheckFailure as error:
PY|        print("RESULT: FAIL", str(error), file=sys.stderr)
PY|        raise SystemExit(1)
END PYTHON SOURCE

## Final disposition

**NOTRUN; complete finite-check body and runnable source delivered.** The exact written frequencies are 32 signed characters, 1120 four-flat-spectrum functions, six balanced four-point sign functions, and four coset-support patterns occurring 512 times each. The finite system’s two branches contradict the fixed total twelve when both divisibility and energy lower bounds are retained.

These statements do not discharge condition (M), the historical-rank/fibre identification, actual-object existence, the full eight-bit caller, or parent acceptance.

overall_correctness: correct

explanation: No defect was established in the assigned finite classification and counting claims by the written reconstruction. This verdict is limited to those claims and the returned finite-check design; execution remains NOTRUN and the complete f384 proof remains outside this duty’s acceptance scope.

confidence: 0.96