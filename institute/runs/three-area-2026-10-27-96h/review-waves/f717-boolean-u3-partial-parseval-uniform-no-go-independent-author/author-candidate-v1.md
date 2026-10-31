# Uniform partial-Parseval obstruction and the corrected fixed physical caller

**NONBLIND GENERAL-PROOF AUTHOR CANDIDATE; UNADOPTED.** The independent written argument below proves the stated larger-class no-go conditional on its explicit hypotheses. It applies to every locally compatible `y` for the one physical `x_t` specified in §5, for every supplied transport covector `t`: no such same-object `y` can have both `J=1` and all 64 U3 caps. This is not an exhaustive computational search. It does not exclude any other `x`, all rank-two/four-distinct-D0 callers, other D0 allocations, V, or the Boolean/NL242 target. A separate full parent read, independent gate and parent disposition are required.

## 1. Precise larger-class statement

Let `F=F_2`, write `j,b in F^2` and `ell,h in F`, and use the unnormalized Walsh transform on `F^6`:

`yhat(nu,s,beta,alpha) = sum_{ell,h,j,b} y(ell,h,j,b) (-1)^{nu ell+s h+beta(j)+alpha(b)}`.

Here `alpha,beta` are arbitrary two-bit covectors, not values selected separately at different occurrences. Let `f_j in F` for all four j with `sum_j f_j=1 in F`; let `sigma_j` and `d_{j,b}` be arbitrary signs for `b!=0`; and let each of the four covectors `kappa_j in (F^2)^*` occur an even number of times. Put `g_j(b)=sigma_j (-1)^{kappa_j(b)}`. Suppose a single real array y satisfies

* `y(1,f_j,j,b)=g_j(b)` for all 16 graph sites;
* `y(1,1+f_j,j,0)=0` and `y(1,1+f_j,j,b)=2d_{j,b}` for each of the 12 nonzero-b mate sites;
* `sum_{ell,h,j,b} y(ell,h,j,b)^2=128`;
* all 64 full Walsh coefficients belong to `4+8Z`.

Then **not all** 64 coefficients have absolute value at most 12. The 32 ell=0 entries may be arbitrary real numbers: no Z4 location, other physical signs, x, J, or additional compatibility is assumed by this lemma. The congruence for a real number means membership in the indicated integer residue class.

## 2. Residue and full-spectrum count

For `i=0,1`, let

`A_i(s,alpha,beta)=sum_{h,j,b} y(i,h,j,b)(-1)^{s h+alpha(b)+beta(j)}`.

For each of the 32 triples `(s,alpha,beta)`, the two **distinct** full coefficients are `W_+=A_0+A_1` and `W_-=A_0-A_1`, corresponding to `nu=0,1`. Let `n` be the number of negative signs among the 12 d's, used modulo 2 when in an exponent.

In the ell=1 graph contribution, b-orthogonality gives

`4 sum_{j:kappa_j=alpha} sigma_j (-1)^{s f_j+beta(j)}`.

The number of summands is even, including zero, so this is 0 modulo 8. In the mate contribution there are 12 signs `d_{j,b}(-1)^{s(1+f_j)+beta(j)+alpha(b)}`. Their product is `(-1)^{n+s}`: each beta character appears three times per j and `sum_j j=0`; `sum_{b!=0} b=0`; and `sum_j(1+f_j)=1 in F`. If m of these 12 signs are negative, their weighted sum is `2(12-2m)=24-4m`, congruent to `4(n+s)` modulo 8. Thus, for **every** triple,

`A_1(s,alpha,beta) = 4(n+s) (mod 8)`.                              (2.1)

Since both `W_+` and `W_-` lie in `4+8Z`, their half-sum and half-difference are multiples of 4, and `A_0/4` and `A_1/4` have opposite parity. Assume for contradiction that both full coefficients at every triple have magnitude at most 12. Then the elementary identity

`max(|A_0+A_1|,|A_0-A_1|)=|A_0|+|A_1|`

applies. On the 16 triples with `s=n mod 2`, (2.1) and the cap imply `A_1 in {0,8,-8}` and `A_0=4 mod 8`. On the other 16, `A_1 in {4,-4,12,-12}` and `A_0=0 mod 8`.

Every capped full coefficient is in `{4,-4,12,-12}`. Full six-bit Parseval, using energy 128, gives

`16 K + 144(64-K) = 64*128`, hence exactly `K=8` of the 64 full coefficients have magnitude 4. This uses all 64 coefficients, not an assumption about a chosen frequency set.

Let `E` count triples in the first slice with `|A_1|=8`, and `O` count triples in the other slice with `|A_1|=4`. Each of these `E+O` triples forces at least one magnitude-4 full coefficient: for E the cap and residue force `A_0=+/-4`; for O they allow only `A_0=0` or `+/-8`. The two full coefficients belonging to different triples have different frequency labels. Therefore

`E+O <= 8`.                                                         (2.2)

## 3. Both partial Parseval counts and equality forcing

The fixed ell=1 slice has energy `16*1^2+12*2^2=64`. It is an array on five bits `(h,j,b)`, so its 32 unnormalized transforms obey `sum A_1^2=32*64`. Dividing by 16 and using the two sets of allowed magnitudes gives

`4E + O + 9(16-O) = 128`, hence `O=2+E/2`.                         (3.1)

Combining with (2.2) yields `E<=4` (and makes E even).

Put `C=sum_{j,b!=0} g_j(b)d_{j,b}`, a sum of twelve signs. For fixed s the h-transform of the ell=1 data at `(j,b)` is

`(-1)^{s f_j}[g_j(b)+2(-1)^s d_{j,b} 1_{b!=0}]`.

Its squared norm over the 16 `(j,b)` positions is `64+4(-1)^s C`: the four b=0 terms contribute 4, and each other term contributes `5+4(-1)^s g_j(b)d_{j,b}`. Four-bit Parseval over `(j,b)` says that this squared norm equals `sum_{alpha,beta}(A_1/4)^2`. In the slice `s=n mod 2` this last sum is `4E`, so

`4E=64+4(-1)^n C`, i.e. `E=16+(-1)^n C >= 4`.                     (3.2)

Thus `E=4`, and equality in the twelve-sign bound is possible only sitewise:

`d_{j,b}=-(-1)^n g_j(b)` for every j and every nonzero b.            (3.3)

Taking the product of all twelve equations gives

`(-1)^n=product_j sigma_j`.                                          (3.4)

Indeed the twelve common factors multiply to 1, and for each j the product of `g_j(b)` over the three nonzero b is `sigma_j^3 (-1)^{kappa_j(p+q+r)}=sigma_j`, where `p+q+r=0` is the sum of the three nonzero two-bit vectors. No enumeration of d signs or assumption about the ell=0 data is used.

## 4. All even-multiplicity character cases yield a cap violation

Now use the **opposite** slice `s=1+n mod 2`. Equation (3.3) gives `(-1)^s d_{j,b}=g_j(b)`. Its h-transform at each j therefore has amplitude `g_j(0)` at b=0 and `3g_j(b)` at each b!=0. Its b-Walsh transform is

`sigma_j [12*1_{alpha=kappa_j}-2]`.

After including the h phase set `v_j=sigma_j(-1)^{s f_j}`. By (3.4), odd `sum f_j`, and `s=1+n`,

`product_j v_j = (-1)^n (-1)^s = -1`.                               (4.1)

Also `product_j (-1)^{beta(j)}=1` for every beta because the four j's sum to zero. Four character labels each occurring an even number of times have exactly two possible multiplicity patterns:

* **All four kappa equal.** Choose that common alpha. Every multiplier in the b-transform is 10, and the four signs `v_j(-1)^{beta(j)}` have product -1. An odd number are negative, so their sum is +2 or -2. Thus `|A_1|=20` for every beta.
* **Two distinct kappa, each twice.** Choose either occurring alpha. For its two distinct active j labels, choose beta with `(-1)^{beta(j_1+j_2)}=v_{j_1}v_{j_2}`; such a beta exists because `j_1+j_2!=0`. The two active signed v-values then agree. Their product is +1; by (4.1) and the beta-product identity, the two inactive signed values have product -1 and cancel. The active multipliers are 10, the inactive multipliers are -2, so again `|A_1|=20`.

Both cases contradict `max(|A_0+A_1|,|A_0-A_1|)>=|A_1|` and the full cap 12, no matter what A0 is. This proves the entire larger-class lemma, including all four j assignments, both f-parity patterns, both d parities, and both admissible kappa-multiplicity cases. It is not dependent on the values of the actual fixed-x ell=0 signs or site.

## 5. The one explicit physical x and its corrected U0 profiles

We now separately verify that the lemma's premises follow for the actual consumer, not for a freely chosen spectrum. Use `0=(0,0)`, `p=(1,0)`, `q=(0,1)`, `r=(1,1)` for the vectors; let `R` denote the phase rather than the vector r. Take

`f(j,b)=f_j=j_0 j_1`, `R(j,b)=j_0 b_0+j_1 b_1`, `rho_b=(-1)^{1+b_0 b_1}`.

The graph is `S={(1,f_j,j,b)}`. The actual fixed physical coefficients have `a=(-1)^R` on S and zero elsewhere; `g=rho_b` on S, `-2rho_b` on its h-mates, 4 on `(0,h,0,0)`, -2 on `(0,h,j,0)` with j!=0, and zero at the other ell=0 sites. The actual inverse is

`u(c,w)=[x(c)+3a(c)chi_1(w)+g(c)chi_2(w)+y(c)chi_3(w)]/4`.

On S the physical relation is `y=-agx`. The allowed local forms and the conditional counts used here are those in the frozen actual-caller interface: 4 D0, 18 D3, 6 Z2, 1 Z4 and 17 Z0, with graph and F forms as displayed there. We use these counts as hypotheses; the separate local-H definition is not newly verified here. The f polar form has rank 2. `f+1+b_0 b_1` is a direct sum of two nondegenerate binary quadratics and is bent; summing over b shows both R and R+f have Walsh magnitude 4 at every four-bit frequency. These are properties of this explicit normalized graph/phase, not a source-equivalence claim.

Define `x_*` by `x_*(1,f_j,j,b)=2*1_{b=j}-1`, put `x_*(1,1+f_j,j,0)=2` for every j, and set its only six nonzero ell=0 values to

| j | h | b | x_* |
|---|---:|---|---:|
| p | 1 | q | +2 |
| p | 1 | r | -2 |
| q | 1 | p | -2 |
| q | 1 | r | +2 |
| r | 0 | p | +2 |
| r | 0 | q | -2 |

All other x values are 0. For the **given**, not newly chosen, covector t set `x_t(c)=(-1)^{t(c)}x_*(c)`. Its x energy is `16+4*4+6*4=56`.

To check U0 on this same x directly, write `chi_alpha(b)=(-1)^{alpha(b)}` and

`Z_{ell,j}(s,alpha)=(1/4) sum_{h,b} x_*(ell,h,j,b)(-1)^{s h+alpha(b)}`.

The ell=1 entries are

`Z_{1,j}=(1/2)(-1)^{s f_j}[chi_alpha(j)-2*1_{alpha=0}+(-1)^s]`.

The ell=0 entries at j=0,p,q,r are respectively

`0`, `(1/2)(-1)^s[chi_alpha(q)-chi_alpha(r)]`,
`(1/2)(-1)^s[-chi_alpha(p)+chi_alpha(r)]`,
`(1/2)[chi_alpha(p)-chi_alpha(q)]`.

The `(s,alpha)=(0,0)` column is zero. In the seven other columns, the corrected nonzero entries, with `p+` denoting value +1 at j=p, are:

| `(s,alpha)` | ell=0 | ell=1 |
|---|---|---|
| `(1,0)` | none | 0-, p-, q-, r+ |
| `(0,b0)` | p+, r- | 0+, q+ |
| `(1,b0)` | p-, r- | p-, r+ |
| `(0,b1)` | q-, r+ | 0+, p+ |
| `(1,b1)` | q+, r+ | q-, r+ |
| `(0,b0+b1)` | p-, q+ | 0+, r+ |
| `(1,b0+b1)` | p+, q- | p-, q- |

Here `b0,b1` are the coordinate covectors. Each row has four distinct positions on an affine binary two-flat and sign product -1: for the six mixed rows, the XOR of the two ell=0 j labels equals that of the two ell=1 labels. Multiplying four signs on a two-flat by any character preserves their negative product, hence their sum is always +2 or -2. Since `xhat_*(nu,s,beta,alpha)=4 sum_{ell,j} Z_{ell,j}(s,alpha)(-1)^{nu ell+beta(j)}`, the first column yields eight zeros and each of the other 56 values has magnitude 8. Consequently all 64 x coefficients are divisible by 8 and capped by 8, with exactly eight zeros including 0. Character modulation translates the spectrum: for every specified t, `xhat_t(t)=xhat_*(0)=0`. No independent selection of seven columns or of t is involved.

## 6. Actual residue, same-y sign interface, and application

Any physical y compatible with this x_t is untwisted as `Y(c)=(-1)^{t(c)}y(c)`. Because `a,g` stay fixed in the inverse and x_t is the modulation of x_*, `Y=-ag x_*` on the same graph. Substitution gives exactly

`(sigma_0,sigma_p,sigma_q,sigma_r)=(+1,-1,-1,-1)`,
`(kappa_0,kappa_p,kappa_q,kappa_r)=(b0+b1,0,0,b0+b1)`.

For example `Y(1,f_j,j,b)=(-1)^{j dot b+b_0 b_1}(2*1_{b=j}-1)`, from which all four rows follow. In particular each character occurs twice and `sum_j f_j=1`. The four D0 mates at b=0 have Y=0; the other 12 graph mates have Y=`2d_{j,b}` for arbitrary signs d. The six E-row D3 values are `2e_{j,h}` at j!=0 and b=0; the six tabled Z2 values are `2z_{j,b}`; one of the other 18 ell=0, b!=0 Z sites is Z4 with value `4k`, `k=+/-1`, and the remaining 17 are zero. These are the same 24 signs at every frequency. Every such Y has energy

`16 + 18*4 + 6*4 + 16 = 128`.

The Walsh spectrum of Y is the translate of the physical y spectrum by t; in particular all 64 caps and all residues are preserved.

We verify the needed residue from the **actual inverse**, rather than assume it. Let `xi=(nu,s,beta,alpha)` and identify the coordinate vector alpha with the corresponding j when necessary. Summing a over b gives

`ahat(xi)=4(-1)^{nu+s f_alpha+beta(alpha)}`,

so `3 ahat=4 mod 8`. Also let `R_alpha=sum_b rho_b(-1)^{alpha(b)}=-2(-1)^{alpha_0 alpha_1}` and `F_s(beta)=sum_j (-1)^{s f_j+beta(j)}`. The ell=1 contribution to ghat is

`(-1)^nu [1-2(-1)^s] R_alpha F_s(beta)`.

For s=0, `F_0=4*1_{beta=0}`, so that contribution is a multiple of 8; the ell=0 E-row contribution is `12-16*1_{beta=0}`, hence 4 mod 8. For s=1 the ell=0 part vanishes, while `F_1=2(-1)^{beta_0 beta_1}`, making the ell=1 part +12 or -12. Thus `ghat=4 mod 8` at every frequency.

For any compatible local ternary inverse, `4u(c,0)=x_t(c)+3a(c)+g(c)+y(c)`. A signed Walsh sum of the ternary `u(c,0)` is congruent modulo 2 to the number of its nonzero entries, so if J is that number modulo 2, then the Fourier transform of the left side is `4J mod 8`. Since every `xhat_t` is 0 mod 8 and `3 ahat+ghat` is 0 mod 8,

`yhat(xi)=4J (mod 8)` for every xi.                                  (6.1)

In particular, J=1 supplies the lemma's 64-residue premise for Y. Conversely the actual sign form gives at the specific frequency t

`Yhat(0)=-8 + 2 sum d + 2 sum e + 2 sum z + 4k`
`         =44-4N+4(k-1) = 4-4N (mod 8)`,

where N is the number of negative d,e,z signs. Equation (6.1) therefore shows `J=1` iff N is even, including for every choice of the Z4 site and sign. The graph sum -8 follows from the two zero-sum nontrivial character rows and the two constant -1 rows. This is an exact same-object parity statement, not a finite sample.

For completeness, the two partial transforms of one such Y are, with `B_p={q,r}`, `B_q={p,r}`, `B_r={p,q}`, `h_p=h_q=1`, `h_r=0`,

`A_1 = sum_j (-1)^{beta(j)} [4 sigma_j (-1)^{s f_j} 1_{alpha=kappa_j} + 2(-1)^{s(1+f_j)} sum_{b!=0} d_{j,b}(-1)^{alpha(b)}]`,

`A_0 = 2 sum_{j!=0,h} e_{j,h}(-1)^{beta(j)+s h}`
`    + 2 sum_{j=p,q,r} sum_{b in B_j} z_{j,b}(-1)^{beta(j)+s h_j+alpha(b)}`
`    + 4k (-1)^{beta(j_*)+s h_*+alpha(b_*)}`.

The complete 64 coefficients of that same physical y are `A_0+(-1)^nu A_1` at `t+nu ell^*+s h^*+beta+alpha`. Thus the all-U3 condition is exactly the 32 simultaneous inequalities `|A_0|+|A_1|<=12`; no per-frequency re-choice of signs is allowed. By §§1–4, the actual y's forced ell=1 data, energy 128 and J=1 residue are already contradictory to those inequalities. This excludes **all** `2^24` assignments of d/e/z signs (in particular all `2^23` parity-eligible assignments), all 18 permitted Z4 sites and both Z4 signs, for this fixed x_t. It does not depend on the sampled sign count or claim feasibility for any other x.

As a consistency calculation for the reference choice t=0, all d/e/z signs +1, and Z4 value +4 at `(0,0,0,p)`, the same inverse is ternary and gives support `16*3+2*4+4*2+18*2+6*2+4=116`; it has energy 128 and 23 spatial y zeros. Its graph w=0 nonzero counts by b=`(0,p,q,r)` are `(1,2,2,4)`, and its off-graph F/D0/D3/Z2/Z4 counts are `(2,4,8,3,1)`. The total is 27, hence J=1. The graph y sum is -8, so `Yhat(0)=-8+36+12+4=44`, demonstrating failure of this reference y's U3 cap. For arbitrary t, the graph relation and local forms still hold after x/y modulation, but the fixed a and g are not modulated and we do not claim that the entire u is a character modulation; (6.1) proves J=1 for this transported reference.

## 7. Actual correction, finite-run status, and remaining boundary

The f689 original example printed both graph-side signs reversed in each of the three nonzero-alpha, s=1 profile rows. The corrected table above is the operative one. Its original w=0 graph census `(3,2,2,0)` is also wrong; `(1,2,2,4)` is correct, while the total of 9 and resulting J parity survive. The parent classified these together as **one author explicit-example MATH MAJOR**; the original f689 body remains unchanged and unadopted. This does not automatically refute its separate location or profile theorems.

The actual f710 v1 run **FAILED**, exit 1, with 193 failed checks: three row mismatches across each of 64 transports plus one census mismatch. Its 1,800 deterministic sign/site samples are not an exhaustive 24-sign analysis and its positive intermediate checks do not turn the failed run into PASS. The corrected f710 v2 was run once and returned `PASS_BOUNDED_PHYSICAL_SIGN_INTERFACE_ONLY`, scoped to the one x, 64 transports, and 1,800 sampled sign/site cases; it did **not** exhaust `2^24` signs, test V/original caller, or verify the local-H definition. There were two versions and two actual runs in total, not one run overall or an old v1 pass. The written universal contradiction above stands or falls on its algebra, not on either sample.

The remaining full problem includes all other permitted f/phase/x and D0 allocations, actual simultaneous physical y, the odd-parity signs on the same 140 zero positions and all 256 odd-half caps, and original gauge/selected-T/rank/atom/cross-fibre restoration at their actual import boundaries. Nothing here proves or refutes any whole branch, V, original Boolean target, or NL242. No human, kernel/formal, independent external-model-family, novelty, source-identity or parent-adoption claim is made.

## 8. Input, coverage, and execution disclosure

The ordered frozen packet was the only scientific input. Its parent-reported bindings were: S1 f709 complete 194 LF, SHA `095baecee33ca4d87220549ab7d17ce935a19f985f71580dd7065169f1dd8338`; S2 f689 complete 231 LF, `69ada1decb9bdf5835dc0b438647a114f1872932c52327cc2cbed5d6b7192a29`; S3 f689 correction complete 17 LF, `ba7cc22c99c615a0674d04ea827d90527494cfb0956452d8ad9588a885fd71f0`; S4 actual f710 v1 receipt complete 42 LF, `c863d8aed5ad610cc4854391f7efe5eb544fab36cd924e0a8a7ced43ff772e30`; S5 actual f710 v2 receipt complete 55 LF, `20b2bebb3cd3a0e93772a1160ff87a8b0dcfe3c658d575b7b366630f0a74cb0a`; S6 actual location baseline complete 30 LF, `fa3b4e334713a4981b267e12be567d2f328ca00203fb525a45100bd1deae2d4a`; S7 actual profile/parity baseline complete 37 LF, `44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a`. These are supplied parent metadata, not newly asserted direct source-file hashes.

Before direct PREBODY ACK to Main I read the manifest, freeze receipt, final binding, prepared live metadata, actual dispatch, all 23 listed controls, and the separately referenced multipart policy through their endings. My ACK mistakenly said 22; I sent an additive correction saying 23, without backdating or replacing the original ACK. After the ACK I read the sole packet, parent-reported SHA `d83069d70d2f15f1da84f4c0cbe735b54834aeacc1a2a60777d5f34ff40aa2e8`, all LF 1–636 in ascending serial raw windows of at most 20 LF through its ending, before deriving. Controls were used for permissions/status only; all held episodes and all their consumers were NONINPUT. No held history, outgoing scientific link, old code, or sibling proof was followed. This is nonblind because the full unadopted f709 and f689 bodies were in the packet, not an independent-family or clean-cognition certificate.

A native clock observed during work was `2026-10-30T16:50:58-0700 PDT`, not a file-creation timestamp. **CHILD SCIENTIFIC EXECUTION NOT RUN:** these are written derivations; no solver, CAS, scientific program, experiment, test, build, lint, formatter, external-model CLI, installation, Git or deletion was run. This final body requires its own full parent read and separately recorded disposition; no finite GO or additional assay is implied.
