# Independent same-harness review: full-law mixed loss and clipped competitor

Native `/bin/date` clock observed immediately before exclusive creation: **2026-10-28T19:01:56-0700 PDT**.
Manifest: `manifest-v1.json`, SHA-256 `1c754bfecc06d04d3b995a4e206d23f57e6ae1d282725ab4ed9edf8354b50bab`. Reviewer: `PrivacyMixedLossReview`. No author contact.

## Verdicts and process

1. **Full-law mixed-loss frontier** (`frontier-20261028-full-law-mixed-loss-frontier-v1.md`): **0 FATAL / 0 MAJOR / 0 MINOR** at the explicit imported-theorem and ordinary-analysis boundaries below. In particular I reconstructed the strict rearrangement equality, attainment, the diamond/rounded criterion, monotone minimizer costs, and both endpoint assertions. This is not an unconditional independent reproof of the three prior research imports.
2. **Explicit clipped competitor** (`frontier-20261028-mixed-loss-explicit-clipped-competitor-v1.md`): **0 FATAL / 0 MAJOR / 0 MINOR** at the MDA per-cost import and the stated conditional `B>0` scope. I reconstructed the actual full-shift privacy, dilation, exact cap integrals, strict gap and large-`epsilon` asymptotics. The two exact rational controls below are not the unknown optimum.

**Process findings: 0 pin mismatches.** I read the manifest first; hashed every listed input before reading it completely and in its listed order, in exact raw windows. Counts are `wc -lc` LF/bytes; the five actual SHA-256 values below equal their respective frozen pins. The additional MDA parent was read completely after the five inputs and its hash matched the candidate's stated hash.

| Input, in manifest order | LF / bytes | SHA-256 |
|---|---:|---|
| `three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md` (LAW642) | 40 / 7501 | `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979` |
| `three-area-2026-10-23-96h/privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md` | 63 / 11178 | `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138` |
| `three-area-2026-10-27-96h/dispositions/info-1-mean-versus-squared-staircase-selectors-parent-v1.md` | 51 / 6471 | `352dbd8c71fe9aa6b2ba124ebf0bfb1fa5f790197a80c916085271560874f8eb` |
| `frontier-20261028-full-law-mixed-loss-frontier-v1.md` | 110 / 10513 | `8e5a0c83dd1eece5a3d1363916333796b6819c320272c4b85c3175d3350001ac` |
| `frontier-20261028-mixed-loss-explicit-clipped-competitor-v1.md` | 130 / 8414 | `243c7d2acb3b76fbe43f4bf6e61e8b070edf5a637f99856dcbe9d1ab636cd24e` |
| Additional named `three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md` | 74 / 14208 | `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3` |

The two candidate basenames above are in `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/`; the three parent paths are under `institute/runs/`. Pins establish byte identity, not mathematical validity of the imported research results. No held, withdrawn or quarantined body was used.

## Candidate 1: reconstructed all-law argument

**Strict matching-norm equality — candidate lines 36–50; MDA parent lines 26–32, 34–46.** MDA's imported bridge gives every feasible law a density and supplies an equimeasurable, centered nonincreasing diamond-radial, *still fully private* rearrangement `p#` with no greater `W`. A `W` minimizer exists by the per-cost import and has finite `W`. For its finite-volume superlevels `A_t`, let `B_t=R_t D` have the same area. With `r=||x||_1`,

`∫_(A_t) r² - ∫_(B_t) r² = ∫_(A_t\B_t)(r²-R_t²) + ∫_(B_t\A_t)(R_t²-r²) >= 0`.

The sphere `r=R_t` has zero area. Both integrands are strictly positive off that sphere, so equality forces equality of the levels modulo null sets. Layer cake makes the total deficit `W(p)-W(p#)`; minimality makes it zero, and Fubini gives `p=p#` a.e. This proves centered radiality of **every** actual `W` optimizer, not just existence of one, while not proving its uniqueness. In quadrant coordinates `(x1,x2)=(rt,r(1-t))`, the radial angular average is `∫_0^1[t²+(1-t)²]dt=2/3`; hence each such law has `J=(2/3)W_*`. The identity is not valid for arbitrary feasible laws.

**Attainment and lower-bound equality — lines 52–60.** A finite-cost feasible law bounds any minimizing sequence of `J+lambda W`; since `J+lambda W>=J`, its second moments are bounded and it is tight. For each fixed closed-diamond shift, pass the privacy measure-order inequality through weak convergence using nonnegative compactly supported continuous tests; Radon measure order then yields every Borel event. The *same* weak subsequence works for each arbitrarily chosen shift: no common pointwise density-exception set or shift-dependent subsequence is required. Lower semicontinuity of the nonnegative cost gives an actual minimizer for every `lambda>=0`.

`H>=V+lambda W_*`. In the diamond regime the imported unique `J`-optimal law `mu_J` is radial, so `V=(2/3)W_J`. For any actual `W`-minimizer `nu`, `V<=J(nu)=(2/3)W_*`; since `W_J>=W_*`, equality follows throughout. Thus `mu_J` attains the lower bound, and uniqueness of the `J` optimum makes it the sole mixed optimizer, including `lambda=0`.

In the rounded regime, if `mu_J` were `W`-optimal, the strict equality argument would make its top positive-density superlevel a centered diamond a.e.; the LAW642 canonical top level is its full-dimensional compact convex core, and equality a.e. of convex bodies with interior makes the sets equal. This contradicts v241's genuine curved arc. Thus `W_J>W_*`. For `lambda>0`, an attained equality in the lower bound would require both separate minima, hence `mu_J` and `W_J=W_*`, a contradiction. This establishes strictness for each fixed positive weight, not a uniform gap.

**Shape and endpoints — lines 62–94.** An infimum of affine nondecreasing functions is concave and nondecreasing. Comparing any positive-weight minimizer against `mu_J` gives `W(mu_lambda)<=W_J`, and the `lambda=0` minimizer is `mu_J`; comparison at either parameter proves the global `W_J` Lipschitz bound. Adding the two optimality inequalities for `lambda<kappa` gives `W_lambda>=W_kappa` and then `J_lambda<=J_kappa`, for arbitrary minimizer choices.

As `lambda` tends to zero, `V<=J_lambda<=V+lambda W_J`. Tightness and closure make every weak cluster the unique `mu_J`, and convergence of second moments upgrades weak convergence to Euclidean `W2`; the quadratic-growth bound `W(x)<=2||x||_2²` then gives `W_lambda->W_J`. The comparison inequality sharpens this to `0<=(J_lambda-V)/lambda<=W_J-W_lambda->0`, giving `H=V+lambda W_J+o(lambda)`.

At infinity, compare with any `W` optimizer and set `C=(2/3)W_*`: `J_lambda<=C` and `0<=W_lambda-W_*<=(C-V)/lambda`. Every weak cluster is private and `W`-optimal, hence has `J=C`; lower semicontinuity and the upper bound force `J_lambda->C` along arbitrary choices. Finally `0<=lambda(W_lambda-W_*)<=C-J_lambda->0`, so `H=lambda W_*+C+o(1)`. This does not assume a unique `W` optimizer or assert convergence to a unique law. The two exact radial controls at lines 96–104 also agree with my Fraction computations in `checker-receipt-v1.json`; they are not proofs of the full-law assertions.

## Candidate 2: reconstructed geometry, scalar inequality and asymptotics

**Actual dilation and privacy — lines 31–45.** For nonnegative coordinates `a,b`, set `c=q-eta` and let `d=(a-c)_++(b-c)_+`. Clamping each coordinate to `c` and, if necessary, reducing their sum to `q` has total removed `l1` mass `max(d,a+b-q)`. If `a+b<=q+k` and each coordinate is at most `q+k-eta`, then `a+b-q<=k`; if only one coordinate exceeds `c`, `d<=k`, and if both do, `d<=k-q+2eta<k`. Thus the removal lands in `S_(q,eta)` and costs at most `k`; the reverse inclusion follows by the triangle inequalities. This proves exactly `S+kD=(q+k)D ∩ {|x_i|<=q+k-eta}`. Since `S` is nonempty and bounded, `n(x)=min{k:x∈S+kD}` is finite; `||h||_1<=1` implies `n(x+h)<=n(x)+1` and, reversing `h`, the opposite inequality. Therefore the actual normalized shell density satisfies the privacy ratio for every point and every full-closed-D shift, and integration pays every Borel event.

**Cap integrals and signed improvement — lines 47–88.** For one cap put `x1=R-u`, `|x2|<=u`, `0<=u<=eta`; independently integrating powers gives area `eta²`, Euclidean second moment `R²eta²-(4/3)R eta³+(2/3)eta⁴`, and squared-`l1` second moment `R²eta²-(2/3)R eta³+(1/6)eta⁴`. Four caps are disjoint because `eta<q/2<=R/2`. The identity `b^n=(1-b)sum_(k>=n)b^k` converts the full infinite shell sum into the geometric moments `M_j=E(q+N)^j`; this gives the candidate's exact `Z_eta`, `NJ_eta`, `NW_eta`, not a first-order approximation.

At an interior squared-`l1` staircase minimizer, differentiating `M4/(2M2)` gives `2M3 M2=M4 M1`, hence `A=M3/M1-M2=Cov(Y,Y²)/EY>0`, where `Y=q+N`; strict positivity follows from two independent copies of nondegenerate `Y>0`. For any `B>0` and `0<=lambda<B/A`, put `Delta=B-lambda A`, `C=(4/3+2lambda/3)M1`, and choose the stated `eta=min(q/4,Delta/(2C))`. It is positive, less than `q/2`, and `Z_eta>0`. Direct subtraction gives precisely

`mixed(Q_(q,eta))-mixed(Q_q) = (4eta²/Z_eta)[-Delta+C eta-(2/3+lambda/6)eta²] <= -Delta eta²/M2 < 0`.

The last step uses `C eta<=Delta/2` and `Z_eta<=2M2`. Because MDA supplies `Q_q` as an *actual all-law* `W` optimizer, its comparison value is `(lambda+2/3)W_*`. The constructed law need not itself minimize `H`; no implication is made for `B<=0` or `lambda>=B/A`.

**Interior and large-`epsilon` expansion — lines 12–29, 90–112.** Using `E[(N)_j]=j!m^j` and Stirling conversion, I derived `P=2M3M2-M4M1` exactly; `W'(q)=P/M2²` and `P(1,m)=(1+m)²(1+2m)>0`. Since the `q=0` and `q=1` staircase laws coincide, the endpoint cannot minimize, so a scalar minimizer supplied by MDA is interior. Put `m=s⁴`. For small `m`, `M2<=q²+4m` on `0<=q<=1` and `M4>=q⁴+m`; hence the stated lower bound together with the trial `q=s`, of cost `O(s²)`, gives `q²=Theta(s²)`. On compact positive `z=q/s`, the leading normalized cost is `(z²+z^-2)/2`, uniquely minimized at `z=1`, forcing `z->1` for any minimizing choice. The exact stationarity numerator divided by `s⁵` begins `z⁵-z-2sz²+2s²z³+O(s³)`; its `z` derivative at `(s,z)=(0,1)` is `4`. The implicit expansion therefore gives `q=s+s²/2-5s³/8+O(s⁴)`, `M2=s²+s³+O(s⁵)`, and `W0=s²+2s³+3s⁴/2+O(s⁵)`. Consequently `A=s³+3s⁴/2+O(s⁵)`, `B=s²/3-s³/3-s⁴+O(s⁵)`, and `B/A=1/(3s)-5/6+O(s)`. Thus `B>0` eventually and every fixed finite nonnegative weight lies in the constructive interval for sufficiently large finite `epsilon`; this is neither a sharp boundary nor a finite-`lambda` global optimizer formula.

## Independent exact checks, including a new q

I wrote and executed the body of [`checker-v1.py`](checker-v1.py) in Python's persistent evaluator with standard-library `Fraction`/integer arithmetic; execution preceded exclusive creation of the same code body (apart from its timestamp comment). It independently generates geometric moments from the falling-factorial/Stirling recurrence, integrates the cap polynomials, verifies the all-variable stationary polynomial and the displayed asymptotic coefficients by sparse rational polynomial identities, and checks both candidates' scalar controls. It did not read or execute an author checker. Script SHA-256 `fb58a4aabec67a1fdee8c401cc62ceb655a4d57fb977b15cbb89371ee0efb121`; actual results and complete exact gaps are in [`checker-receipt-v1.json`](checker-receipt-v1.json), SHA-256 `16584a831e1b013a2e6198199b556e9d9418cdf4dba0998c7559351fdc8c6083`.

Both checks below use `m=1/10000`, `lambda=1`, and compute the true two shell-law objective values from the integrated moments, not an author replay. For each, `A>0`, `B>0`, `Delta>0`, `0<eta<q/2`, `Z_eta>0`, and the displayed exact identity and `actual gap >= Delta eta²/M2 > 0` hold:

| q | Delta | eta | guaranteed positive gap `Delta eta²/M2` |
|---|---|---|---|
| Stated trial `21/200` | `19004022149/9288350000000` | `19004022149/3904822340000` | `6863356909559976007261228573949/1578559472224000942305916945200000000` |
| New trial `53/500` | `23288153779/9464350000000` | `23288153779/4016670140000` | `12630053222854858298038469748139/1734183966232160235188353297200000000` |

Both trials are explicitly **not** asserted to be the W-minimizing q: their exact stationary residuals `2M3 M2-M4 M1` are respectively `54977457/156250000000000` and `52377913047/62500000000000000`, both nonzero. Thus these exact tests establish improvement over two actual feasible trial staircases, not over `W_*` by themselves. The universal W-optimum conclusion instead uses the written argument plus the imported MDA attainment. Independently, the disclosed first trial `q=1/10` has `Delta=-1603556003/25300050000000<0`, so it does not meet the positive-eta construction; the author disclosed this at candidate-2 lines 114–126.

## Explicitly conditional imports and limits

- **LAW642** is imported for finite `V`, the actual unique original-law Euclidean optimum, its canonical convex core and geometric density. I read and hash-checked its 40-line parent record, not its underlying 642-line proof or historical reviewers in this assignment.
- **v241** is imported only for the exact diamond-versus-genuine-rounded geometry and threshold (including equality): for `s0=sinh²(epsilon/2)`, the threshold is the unique positive root of `2s0³-9s0²-108s0-81=0`. I read its 63-line disposition, not the underlying separated proof or its historical reviewers. The NORM148 entire-norm-class gap is not needed for these two reconstructed arguments. The v241 original manuscript and its held/quarantined consumers remain noninputs.
- **MDA alternative per-cost/rearrangement** is imported for full-Borel/full-closed-D feasibility, density and feasible equimeasurable centered rearrangement, and an attained all-law matching-`l1²` staircase minimizer. I read the 74-line parent and the manifest's MDA-selector disposition, but did not independently reconstruct their underlying 237-/219-line research proofs, authenticate the original printed proof, or establish source equivalence. The first-`l1` selector is not substituted for the squared-cost selector. MDA's rearrangement alone does not assert every W optimizer is radial; the strict equality argument above is the additional composition.
- Ordinary analysis is used at the cited boundaries: geometric layer cake/Tonelli and Radon measure order, weak compactness/lower semicontinuity, the standard weak-plus-second-moment `W2` criterion, and local analytic implicit-function calculus. Finite `epsilon>0` and the original additive, data-independent, full-shift privacy model are essential.
- No claim of W-law uniqueness, strictly concave `H`, global sharpness of `B/A`, a complete finite-weight phase diagram, a uniform rounded-side gap, nonadditive-channel optimality, public-source equivalence, novelty, or publication priority follows. This is a same-harness review, not external-family, human, formal/kernel, or independent publication verification. Imported previous process holds and qualifications are not relaxed.
