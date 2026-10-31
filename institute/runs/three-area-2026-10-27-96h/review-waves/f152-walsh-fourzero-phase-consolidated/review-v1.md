# f152 — independent same-harness review of the consolidated four-zero phase packet

## Disposition and exact scope

**SUPPORTED within the frozen mathematical scope: 0 FATAL / 0 MAJOR / 0 MINOR findings.** I independently reconstruct the Boolean caller, the T=0 exclusion, both radical phase functionals, the three pointwise constants, the character-modulated contradiction, and the translation normalization. The conclusion is conditional: an actual balanced nine-variable Boolean function with Walsh peak at most 28 and exactly four Walsh zeros would have the stated rank-six geometry and **λ≠ρ**, and would admit the stated normalized signed counts. This is not an existence proof or an exclusion of the four-zero branch.

This is an independent **same-harness written review**, with independently authored and actually executed exact controls. It is not a human review, independent-model-family review, formal/kernel proof, novelty audit, or parent adoption. The auxiliary author-control and formal-multiset existence assertions outside the two manifest inputs are **NOT VERIFIED / INCONCLUSIVE here**, not additional premises or findings against the mathematical core.

### Frozen inputs and access boundary

The manifest was read first, at SHA-256 `8f10719b5e86f5198f79d3e1ad055169d0566489c2adb87584a528ac19a32f27`. Both inputs were SHA-256/byte/LF verified before interpretation, then read completely in declared order. The independent control receipt rebinds these same pins.

| Order | Input | SHA-256 | Bytes | LF |
|---|---|---|---:|---:|
| 1 | `dispositions/info-6-four-zero-rank6-radical-parent-v1.md` | `12efd10b4a9de2ac70cd49541e36e6a0c5df6bd4deecbb74e085c2eb48795dc3` | 5831 | 31 |
| 2 | `frontier-20261028-fourzero-phase-consolidated-v1.md` | `8c6afc0d19a9707089c5aebf1240f21ef69b1418a2c7009fcaa650712fc5707a` | 17497 | 154 |

No historical held mathematical payload, underlying f131 source/review/control artifact, author Python code, cited formal-fiber file, external model, web source, Git operation, or infrastructure was used. In particular, the prior disposition's summaries of its own controls are not independently replayed evidence in this review.

## Component verdicts

| Component in the candidate | Verdict | Essential boundary |
|---|---|---|
| §2, lines 20–30: Boolean caller and converse | SUPPORTED | One frequency-labeled array; all 512 correlation identities, including the zero shift |
| §2, lines 32–38: T=0 exclusion | SUPPORTED | Balanced nine-variable f; Walsh peak ≤28; independent of f131 |
| §3: framework import and zero-count qualifications | CONFORMS / SUPPORTED | f131 used only with T≠0, nine variables, peak ≤28, and exactly four zeros for its rank-six/radical conclusion |
| §4, lines 68–76: odd Q and ρ | SUPPORTED | Polarization includes Q(0); R is the radical furnished by the four-zero framework |
| §4, lines 78–90: even mod-8 λ | SUPPORTED | Support-moment expansion, rank-six quotient, peak bound and exact zero set all matter |
| §5, lines 94–100: 640/864/1464 pointwise inequalities | SUPPORTED | The modulated single-class restrictions are essential |
| §5, lines 102–110: Parseval/correlation contradiction and λ≠ρ | SUPPORTED | Character χ=(-1)^λ; use ρ=λ only as the contradiction hypothesis |
| §6: translation normalization, Q weight, m=72/56 | SUPPORTED | Signed count is for the translated function, not an invariant original histogram |
| §7: remaining obligations and non-witness barrier | ACCURATE | A relaxation cannot replace quotient placement, all correlations, or a Boolean inverse |
| §7–8: cited tuple/author-control receipts; external peak-theorem bridge | NOT VERIFIED / INCONCLUSIVE | Outside this manifest's input scope; not used to establish any result above |

## Independent reconstruction

### 1. Exact Boolean caller and T=0

Put s(x)=(-1)^f(x), with one-support M of size 256. For nonzero a, character cancellation gives W_f(a)=-2(256-2n_a), so k(a)=n_a-128. At zero k(0)=0 by balance. Reducing n_a modulo two gives k(a)≡a·T, where T is the XOR of M. Thus all k are integers and the peak bound is exactly |k|≤7.

Walsh orthogonality applied to s(x)^2=1 gives C(b)=Σ_a k(a)k(a+b)=2^14·1_{b=0}. Conversely define U(x)=Σ_a k(a)(-1)^(a·x). Then U(x)^2=Σ_b C(b)(-1)^(b·x)=2^14, hence s=U/128 is a genuine ±1 table and its Walsh transform is 4k. The zero coefficient makes the associated 0/1 table balanced. This argument does not work with merely unlabeled spectra, individual fiber sums or three radical correlations.

For T=0, all first support moments are even. Expanding the integer parity n_a modulo four in any coordinate basis and dividing by two gives a degree-at-most-two Boolean q=k/2 mod2 on all nine variables. The special a=0 correction is 128 before division and does not affect these congruences. As q(0)=0, 1+q is nonzero and has weight at least 2^(9-2)=128. If v=|{q=0}|, peak ≤28 bounds k² by 16 on q=0 and by 36 on q=1. Therefore

Σ_a k(a)^2 ≤16v+36(512-v)≤128·16+384·36=15872<16384.

This contradicts C(0). The minimum-support lemma is justified by the stated decomposition p=p0+x_n p1: if p1 is zero, double the induction bound for p0; otherwise wt(p0)+wt(p0+p1)≥wt(p1), whose degree is at most d-1. Thus **T≠0 is proved here, not silently imported from f131**.

### 2. Framework, zero-count bounds and f131's exact use

Now K=T^⊥ has dimension eight. Odd k outside K exclude zeros there. The adopted f131 conclusion is used only at its explicit hypotheses: balanced nine-variable f, T≠0, Walsh peak ≤28, exactly four Walsh zeros. It then supplies rank(B)=6 and Z=rad(B)=R, a linear two-plane. Its 108/140 magnitude-16 counts and its four qualifications are preserved: nine variables rather than eight; no T=0 result from f131; divisibility by eight equals actual vanishing only under the peak bound; abstract forms/histograms are not Boolean witnesses. No later census, autocorrelation candidate, held outcome or out-of-manifest formal histogram is imported.

I also checked the parity mechanism displayed in §3. For an affine frequency six-flat, its spatial annihilator has dimension three. Let v_C be the 8-term signed sums over the 64 spatial cosets. They are even, Σ_C v_C is a Walsh coefficient divisible by four, and consequently Σ_C v_C² is divisible by eight. Quotient Parseval gives Σ_flat k²=4Σ_C v_C²≡0 mod32. A fixed odd L-coset can therefore be compared with every even L-coset for each five-space L≤K.

The even-square residue calculation gives E(A)≡16[n_q(A)/4+n_z(A)] mod32. Five-variable quadratic weights make n_q/4 integral; its parity is zero for restricted rank ≤2, and is 1+q(r)+B(a,r) for restricted rank four. This yields degree at most six for the divisibility indicator, or at most five when global rank ≤4, exactly as the displayed framework argument states. Its nonzero weight is consequently at least four, even, or at least eight at rank ≤4. Under |k|≤7 that indicator is the actual zero indicator. The upper bound follows from

16384≤36(256-|Z|)+49·256, giving |Z|≤149 and, by evenness, |Z|≤148.

In the four-zero branch q vanishes on R and descends to a nondegenerate six-variable quadratic. Its quotient zero count is 28 or 36, so z=|{q=0}| is 112 or 144. Excluding R itself leaves z-4=108 or 140 coefficients with |k|=4. These are necessary counts, not feasible branches certified by this review.

### 3. Odd ρ from the second support moment

The integer XOR identity for the support bits gives equation (9) modulo four, including frequencies zero after ignoring multiples of 128. Its mixed second difference based at any a0 is the same modulo four: the extra base-dependent triple product is multiplied by four. On K, dividing that even difference by two gives B. On an odd coset, with Q(x)=(k(a0+x)-1)/2 mod2, it gives the same B.

Here the polarization of the possibly nonzero-constant Q is **Q(x+y)+Q(x)+Q(y)+Q(0)**. For r∈R, Q(x+r)+Q(x)=Q(r)+Q(0) is independent of x; define this as ρ(r). Restricting the polar identity to R proves additivity. Changing a0 to a0+c merely translates Q and leaves this radical variation unchanged, so ρ is canonical. If ρ≠0, pairing by a radical vector with ρ(r)=1 makes Q balanced, of weight 128. If ρ=0, Q descends to a six-variable nondegenerate quadratic with an allowed affine/constant term, giving weight 4·28 or 4·36, namely 112 or 144.

### 4. Even λ from the first three support moments

Choose a basis of K adapted to K=F₂⁶_x⊕R and to a symplectic normal form for q on its quotient. Its squarefree integer lift g0 is x0x1+x2x3+x4x5, with x0+x1 added in the other Arf class. Every basis vector lies in K, so its first support moment m_i is even. The integer parity expansion modulo eight gives exactly

k(a)/2 ≡ Σ_i(m_i/2)a_i − Σ_(i<j)m_ij a_i a_j +2Σ_(i<j<ℓ)m_ijℓ a_i a_j a_ℓ (mod4).

Modulo two this is q. In the adapted basis its coefficient difference from g0 is even, so k/2≡g0+2h mod4 with Boolean deg(h)≤3. Decompose h=h0(x)+r1h1(x)+r2h2(x)+r1r2h12(x). On q(x)=0, k/2 is 0 mod4 at x=0 and 2 mod4 at every other x, independently of r: these are precisely the peak bound and Z=R being used. Thus h1,h2,h12 vanish on {q=0}.

For a degree-at-most-two p vanishing there, p and q+p have disjoint supports partitioning {q=1}, of size 28 or 36 in six variables. Every nonzero degree-at-most-two function in six variables has weight in {16,24,28,32,36,40,48,64}. No two such weights sum to 28 or 36, so p is 0 or q. A degree-at-most-one p must be zero. Therefore h1=λ1q, h2=λ2q, h12=0, giving

k(a+r)≡k(a)+4λ(r)q(a) (mod8), with λ(r)=λ1r1+λ2r2.

It is linear and unique because q has one-points. Equation (10) is intrinsic, so λ does not depend on the adapted coordinates or on g0. This derivation does not assert (10) for all balanced functions without the four-zero/peak assumptions, even though some outside-scope functions also happen to satisfy it.

### 5. Fiber inequalities and the character-modulated contradiction

Assume λ=ρ, set χ(r)=(-1)^λ(r), and take all 128 R-cosets. For F=a+R let E_F=Σ_r k(a+r)² and S_F=Σ_r χ(r)k(a+r). Changing the representative by s multiplies S_F by χ(s), so its square is unambiguous. The zero fiber R has E_F=S_F=0.

* On each other even q-zero fiber, all modulated entries are ±4. E_F=64, so S_F²≥10E_F−640 is just S_F²≥0.
* On an even q-one fiber, (10) makes χ(r)k(a+r) constant modulo eight. Thus all four entries belong to {-6,2}, or all belong to its negative. With n entries -6, E_F=16+32n and S_F²=(8-8n)²; the defect S_F²−10E_F+864 equals 64(n-3)(n-4), nonnegative for n=0,…,4.
* On an odd fiber, ρ=λ and the odd negation rule make the modulated entries constant modulo four. They all belong to {-7,-3,1,5}, or its negative. The separately convex expression 10Σx_i²−(Σx_i)² is maximized on the vertices of [-7,5]^4. With n entries -7 it is 600+720n−144n², whose maximum is 1464 at n=2 or 3. Thus S_F²≥10E_F−1464.

There are (z-4)/4, (256-z)/4 and 64 fibers of these types. Summing and using C(0)=16384 gives

Σ_F S_F²≥10·16384−640(z-4)/4−864(256-z)/4−1464·64=16384+56(z-16).

Independently, expand S_F² and use χ(r)χ(s)=χ(r+s). Coset summation covers every frequency exactly once, giving

Σ_F S_F²=Σ_(r∈R)χ(r)C(r)=16384.

Hence **0≥56(z-16)**, impossible for z=112 or 144: the excess is respectively 5376 or 7168. This proves **λ≠ρ**, including the case of a common nonzero character, not merely the unmodulated λ=ρ=0 case. It requires no selected histogram or solver claim.

### 6. Input translation, normalization and m

For f_t(x)=f(x+t), k_t(a)=(-1)^(a·t)k(a). The XOR T is unchanged because the support size is even; q, B, R and the zero set are unchanged. For even k, -k≡k+4q mod8. For odd k, negation toggles (k-1)/2 mod2. It follows that λ_t=λ+ψ_t and ρ_t=ρ+ψ_t, with ψ_t(r)=r·t; for Q explicitly Q_t(x)=Q(x)+(a0+x)·t.

The restriction map F₂⁹→R* is onto, with a seven-dimensional kernel, so every radical character has exactly 128 translation preimages. Taking ψ_t=ρ gives ρ_t=0 and λ_t=λ+ρ≠0. The normalized odd Q consequently has weight 112 or 144. This Q weight is not asserted to be paired with a particular value of z.

On each even q-one fiber, nonzero λ_t has two zeros and two ones. Equation (10) therefore puts exactly two of the four coefficients in k/2≡3 mod4, i.e. k∈{-2,6}. Thus the translated signed count m=A_-2+A_6 is (256-z)/2: **72 for z=112, 56 for z=144**. This is not a translation-invariance claim about the original signed spectrum. Global complementation negates k, adds 1 to Q and preserves both radical functionals, so it may set f_t(0)=0 without changing this phase conclusion or Walsh magnitudes.

## Independently authored controls actually executed

[Control script](reviewer-f152-controls-v1.py): SHA-256 `666f0cca9015c115b6a1ab5af7aa870a3fd07516030ad6ba4f2e8331adba1772`, 38859 bytes, 862 LF.
[Exact receipt](reviewer-f152-controls-v1-result.json): SHA-256 `483c4ea6b1ba0767f832b47310d6338a8d687ce238146471bef5551598573d3b`, 21400 bytes, 1015 LF.
The retained [pre-run preparation artifact](reviewer-f152-prepare-controls-v1.py) only amended this reviewer's own script before its execution; it never reads or changes author code. Its SHA-256 is `2c5f3a4138323d15eb11cbb61aa5cc45c761b50688febbf6237d9bc830f1ccc4`.

The single executed control run returned exit 0. Native clocks from /bin/date inside it were **2026-10-28T22:01:07-0700 PDT** before, **2026-10-28T22:01:08-0700 PDT** after; measured elapsed 0.72 seconds, Python 3.14.3 / NumPy 2.4.3. Result: **69/69 positive checks and 24/24 intended-reason negative checks pass**, plus one informational comparison. “Negative pass” means the deliberately invalid mutation was detected; it is not an asserted counterexample to the theorem.

### Actual Boolean functions, not formal fiber witnesses

* A generated balanced nine-variable truth table was transformed directly. Checks covered k=n_a-128, k parity from T, all 512 exact correlations, and reconstruction U/128 of the original sign table. A weight-255 mutation breaks the k-integrality/balance caller; perturbing a frequency coefficient produces 470 nonzero-shift failures and non-Boolean inverse amplitudes.
* Three further actual balanced functions checked (9) for all 512² pairs, (11) on all 256 elements of K, degree(q)≤2, and polar(Q)=B for all 256² pairs using two distinct odd base points. Dropping the cubic term breaks (11); toggling one odd residue breaks the Q polar equality.
* Three actual rank-six examples with q|R=0 checked ρ's constant radical differences and linearity, degree-at-most-two even radical differences, translation and complement laws, and the 128 preimages of each character. Their peaks |k| are 15/16/17 and zero counts 29/28/39: **none is a peak-28 four-zero witness**, and those outside-scope actual zero counts need not satisfy the target's parity bounds.
* Four constructed balanced T=0 functions checked global evenness of k, quadraticity of q, the minimum-support bound and peak |k|≥8. The structured function f0=x0x1+x2x3+x4x5+x6x7+x8 is balanced with T=0, k∈{0,±8} and exactly 256 zeros. It shows why the q-zero square bound 16 cannot be extended from peak 28 to peak 32.
* A second structured actual function is obtained from f0 by toggling the eight points e_i+e8 for i<4 and e_i for 4≤i<8. Four removed ones and four added ones preserve balance. Its truth-table SHA-256 is `4fa7de130b7f5fb94c19ef170c570d9e6cfe9e3eb75e4ff06312df9e11cd29d4`. Direct computation gives T=255, rank(B)=6, z=144, peak |k|=12, 70 zeros, and k-values {0,0,8,8} on R. Equation (10) and the odd radical law hold with **λ=ρ≠0**, while the target hypotheses fail. Sixteen genuine input translations were Walsh-recomputed from translated truth tables and obey both phase-shift laws; a normalized odd Q has weight 112. This is a scope-negative control, not a target witness or a counterexample to λ≠ρ. Misapplying the target's fiber constants fails on 63 actual fibers; e.g. one q-one fiber [-2,2,-10,-6] has 10E−S²=1376>864, and the radical fiber has energy 128 rather than zero.

### Finite arithmetic and intended-reason mutations

* Exhaustive four-entry arithmetic gives exact maxima 640 for {±4}^4, 864 for {-6,2}^4 and its negative, and 1464 for {-7,-3,1,5}^4 and its negative. The mutated constants **639, 863, 1463 fail**, respectively at tuples (4,4,-4,-4), (-6,-6,-6,-6), and (-7,-7,-7,5). Mixing sign/residue classes raises the maxima to 1440 and 1960, confirming the phase orientation is load-bearing.
* On actual Boolean spectra, all four characters of a two-plane give Σ_F S_F²=Σ_r χ(r)C(r)=16384 and the expected representative-sign law. Replacing χ by the non-character sign vector (1,1,1,-1) changes the total from **14592 to 16272** when coset representatives change. Perturbing the spectrum preserves the algebraic character identity but destroys its fixed 16384 value. These are sign-orientation and Boolean-caller negative controls.
* Independent F₂ evaluation matrices show that, for both six-variable nondegenerate normal forms, the degree-≤2 vanishing space on {q=0} has dimension one and the degree-≤1 space dimension zero. Allowing degree three enlarges those dimensions to 7 and 15, a degree-bound negative control. Independently enumerating all **2^22** six-variable degree-≤2 Boolean functions gives exactly the nonzero weight set used in the proof. A five-variable census and all pairs of three-variable functions also check the relevant minimum-weight/triangle-inequality facts.
* Direct arithmetic checks the 128 fiber counts, the bounds 21760/23552 for z=112/144, the difference 56(z-16), the sign rules and m=72/56. These are identities and inequality controls only. No tuple, quadratic, labeled relaxation, or census entry is treated as an actual four-zero witness.

## Load-bearing dependencies and limits

The written mathematical inputs are finite character orthogonality/inversion, the integer XOR support-moment expansion, the Boolean minimum-support lemma (induction above), alternating-form/symplectic normal forms, and the standard quadratic weight classification. The latter finite weight/vanishing assertions are also independently checked in the stated controls, but not kernel-certified. The only imported research framework is the pinned f131 disposition at its exact T≠0 four-zero scope; the new T=0 exclusion, phase claims and normalization do not acquire support merely from its existence.

The controls do not produce a Boolean function satisfying the target hypotheses. The actual examples verify the general callers, phase transformation mechanisms and failure boundaries; the conditional λ proof and final contradiction remain written arguments. No author “checked” or “PASS” statement is accepted as independent evidence. The packet's three formal tuple-multiset claims and its cited same-owner replay/control files were not opened or executed, and no conclusion here depends on them. The separately mentioned peak theorem and any bridge to a global NL claim are likewise outside this review.

## What remains open

1. **Existence or exclusion of the four-zero branch itself**, for both z=112 and z=144. The result only eliminates equal radical phases; neither rank-six branch is certified feasible or impossible.
2. **A common frequency geometry:** place the 128 fibers in the same seven-dimensional quotient F₂⁹/R, with its 64 even and 64 odd positions, one common rank-six q, a compatible odd Q, and magnitude/peak data arising from one array. A multiset or separate q/Q realizations do not suffice.
3. **The other 508 nonzero correlations.** The three nonzero shifts in R are only three of 511. Cross-fiber orientation and all remaining shift equations must be satisfied or excluded for a single labeling.
4. **An actual Boolean inverse / verified witness, or a complete exclusion argument.** All equations in (5), integrality, k(0)=0 and the peak constraint are a sufficient exact caller; partial callers are not. Any proposed truth table still requires independent full Walsh and weight recomputation before a witness claim.
5. **Other possible zero counts:** this phase result does not settle balanced peak-≤28 functions with even |Z|≥6 (within the stated upper bound), nor supply a global balanced NL242 result.
6. **Novelty and stronger verification:** no human, distinct-model-family, formal/kernel or SOTA/novelty conclusion has been obtained here. A separate parent disposition is needed for adoption.

Overall correctness of the frozen mathematical scope: **correct**. Confidence: **0.98**. No source edits, author contact, author-code execution, unrelated build/test/formatter run, external call, publication, deletion or infrastructure mutation occurred.
