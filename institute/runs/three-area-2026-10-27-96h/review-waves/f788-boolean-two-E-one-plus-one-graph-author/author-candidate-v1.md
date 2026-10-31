# F788 — two E-row D0 and one graph mate in each of two rows

**Status: fresh nonblind same-harness GENERAL AUTHOR written proof candidate; NOT parent-adopted or independently checked.** Native clock observed immediately before preparing this exclusive write: **2026-10-31T01:22:28Z**. The argument below gives a conditional no-go for the entire assigned `d_E=2, graph 1+1` branch, including both physical E-site occupancies `2` and `1+1`. It is a written argument, not an executed finite result, witness, novelty claim, human/family/kernel review, or global Boolean bound.

## 1. Exact statement and physical imports

Consider one actual normalized rank-two five-span object at the packet's named local-H-zero/count interface. Keep the **same** physical `f/R, a, g, u, x=U0, y=U3`, the same inverse, the specified original-DC transported character `t`, and set only the analysis arrays `X=(-1)^t x`, `Y=(-1)^t y`. The transported balance is `xhat(t)=0`; neither `t` nor the physical phase is freely chosen. Modulation translates the entire spectra of both arrays and preserves their actual pointwise graph identity.

Use coordinates `(ell,h,i,b)`, with `ell,h` in `F2` and `i,b` in `F2^2`. In row `i` the actual graph is `(ell,h)=(1,F_i)`, its physical same-`b` mate is at `h=1+F_i`, and `sum_i F_i=1` in `F2`. There are four D0 in the 16 graph mates plus six ell-zero non-full `b=0` E sites. Here exactly two D0 are on the E sites and exactly one D0 is in each of two distinct graph rows. Thus there are 14 D3 graph mates, six ell-zero Z2 sites, one Z4 and 17 Z0; both E occupancy types `2` and `1+1` are included.

The proof uses the following actual imports, not independent free spectra or separately selected profile columns:

1. The same-X zero-flat equations `Z_(ell,i)(0,0)=0`, and all seven simultaneous nonzero profiles of
   `Z_(ell,i)(s,alpha)=(1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha(b))`: each is one entry `+/-2`, or four entries `+/-1` on one affine two-flat of `(ell,i)` with sign product `-1`. Graph X values are `+/-1`; D0 and Z2 X values are `+/-2`; D3, Z4, Z0 and the two full-site X values are zero.
2. On each graph row the same-object identity is `Y=-a g X`; `a_i(b)` has an affine sign with row covector `rho_i`, the four `rho_i` are distinct, and graph `g` has quadratic part `q(b)=b_0 b_1`. Consequently `sum_i rho_i=0`. The prescribed modulation is common to X and Y, and does not modify `a` or `g`.
3. On the graph `|Y|=1`; a graph D0 mate has `Y=0` and a graph D3 mate has `|Y|=2`. On ell zero the actual Z4 has `|Y|=4` at a nonzero `b`; its opposite-h site at the **same** `(i,b)` is another Z site with `|Y|` equal to 0 or 2. We do not assume any bound on the two full sites at `i=b=0`.
4. For this one Y, `J=1` gives every full U3 coefficient congruent to `4 mod 8`; all 64 have magnitude at most 12 and total spatial squared energy is 128. The ell-one energy is `16+14*4=72`. All seven profiles and all Y conditions are imposed simultaneously on this physical object.

These are the named packet S3/S4/S6/S7 imports. The proof neither derives the original physical phase/inverse/residue bridge from first principles nor uses the unadopted whole-family claims in S3–S5. Parent review must check these exact import boundaries.

**Candidate conclusion.** Under items 1–4, no object with `d_E=2` and graph occupancy `1+1` exists. No claim is made about graph occupancy `2`, `d_E=0`, other ranks, V, the original caller, or NL242.

## 2. Lambda and every simultaneous graph-profile type

Let the two graph-mate D0 rows be `a,a'` and the other rows `b,b'`. Set `Delta=a+a'`; because these are complementary pairs of a four-point affine `F2^2` row set, also `b+b'=Delta != 0`. Let the D0 mate in row `i=a,a'` be at `b=z_i` with X value `2 epsilon_i`, `epsilon_i=+/-1`. Zero-flat gives graph row sum `-2 epsilon_i`, so each occupied graph row has a `3:1` sign split. Each unoccupied graph row has a `2:2` split and is therefore a signed nonconstant character `sigma_i (-1)^theta_i(b)`, `theta_i != 0`.

At the lambda column `(s,alpha)=(1,0)`, the graph entries are

`Z_(1,i)(1,0)=-(-1)^F_i epsilon_i` for `i=a,a'`, and zero in the other two graph rows. Both nonzero graph entries have magnitude one. Thus lambda cannot be a singleton: it is one four-entry plane, with two ell-zero entries, whose two row indices also differ by `Delta`; the product of all four signs is `-1`. Both E occupancy patterns remain in scope. In particular, nothing here replaces this mixed plane by a graph or E singleton.

The two ell-zero lambda rows each have an odd number of actual X sites in **each** h-cell; the other two rows have even numbers. The eight ell-zero supports therefore occupy 4, 5 or 6 h-cells. With four cells, two active cells have three sites; with five cells there is either one extra active triple plus one zero-lambda pair, or one four-site zero-lambda cell; with six there are two additional zero-lambda pairs. A four-site cell includes a genuine `b=0` E D0 and cannot be a full-site cell. These are necessary location statements, not separately chosen X arrays.

The remaining six columns are also constrained on this **same** X. For a nonzero b-character `alpha`, let `L(alpha)` be the number, 0, 1 or 2, of the two unoccupied graph rows whose `theta_i` equals `alpha`. Each occupied graph row contributes a magnitude-one entry on exactly one of the two `s` slices; write that slice `s_i(alpha)`. The permitted graph support counts and E-side completions are:

| `L(alpha)` | forced relation | graph counts in the two s-slices | actual profile requirements |
|---|---|---|---|
| 0 | `s_a=s_a'` | `2,0` | the 2-graph slice has a 2-E pair of the same row difference and four-sign product `-1`; the other slice is an E-side singleton or E-side plane |
| 1 | `s_a!=s_a'` | `2,2` | each slice is a mixed plane; its E pair has the **actual** graph-pair difference and the four signs have product `-1` |
| 2 | `s_a=s_a'` | `4,2` | the four graph entries are the entire graph plane with sign product `-1`; the other slice is a mixed plane with the matching E-pair difference and product `-1` |

For the displayed pair-difference condition, the graph pair in a given slice need not always be `a,a'`. If a slice has zero graph entries, its E singleton/plane is still the transform of the same eight actual ell-zero supports; the table does **not** assert independent realizability of columns. These alternatives follow because a nontrivial affine two-flat meets either ell-half in 0, 2 or 4 points, and every graph entry here has magnitude at most one. They cover every permitted singleton/plane profile and every `alpha`, with the separate zero-flat at `(0,0)`.

## 3. A simultaneous-profile identity on the actual graph rows

Identify row covectors with two-bit vectors in fixed dual coordinates. Write `q(v)=v_0 v_1` and `J(v_0,v_1)=(v_1,v_0)`, so `q(alpha+nu)=q(alpha)+q(nu)+alpha(J nu)`.

Every `3:1` graph sign row is a signed quadratic `sigma_i(-1)^(q(b)+nu_i(b))`. Its b-Walsh transform is `2 sigma_i (-1)^q(alpha+nu_i)`. The zero-flat equation fixes its value at `alpha=0` to `-2 epsilon_i`. Directly from the actual mate at `z_i`, the occupied graph row contributes to precisely the slice

`s_i(alpha) = 1 + q(alpha) + alpha(J nu_i + z_i)`.                                                (3.1)

All equations in this section are in `F2`. For `alpha=0`, (3.1) gives `s_i=1`. For nonzero `alpha`, the even graph support condition in Section 2 gives

`s_a(alpha)+s_a'(alpha) = 1_[alpha=theta_b] + 1_[alpha=theta_b']`.                             (3.2)

This also holds at `alpha=0`, as both theta values are nonzero. If the two theta values agree, the right side is identically zero. If they differ, they are independent nonzero covectors; the right side is the linear form `alpha(J(theta_b+theta_b'))`: it is one exactly at the two named nonzero characters and zero at the other two. Combining with (3.1), valid for all four alpha, yields the **same-object identity**

`z_a+z_a' + J(nu_a+nu_a') = J(theta_b+theta_b')`.                                             (3.3)

No graph Y assumption or arbitrary row phase was used in deriving (3.3); in particular the mixed-plane and possible E-singleton alternatives of the six other columns have not been replaced by an assumed realization.

## 4. The physical phase makes one whole Y parity slice uniform

On an occupied graph row the quadratic factors in `Y=-agX` cancel, so the actual graph Y is an affine character with covector `phi_i=rho_i+nu_i`. On an unoccupied graph row, the actual graph Y is a bent quadratic with covector `mu_i=rho_i+theta_i`. Signs and additive constants are left arbitrary but fixed by the object.

For `s,alpha,beta` define the same physical partial transforms

`A_ell(s,alpha,beta)=sum_(h,i,b) Y(ell,h,i,b)(-1)^(s h+alpha(b)+beta(i))`.

The full coefficients are `A_0 +/- A_1`. We now derive, rather than assume, that the parity of `A_1/4` is independent of both alpha and beta within each fixed s slice, and switches between the two slices.

For row `i`, let `D_i(b)=Y(1,1+F_i,i,b)/2`: it is zero at the D0 position in an occupied row and `+/-1` elsewhere. Let `M_i(alpha)=sum_b D_i(b)(-1)^alpha(b)`. For an unoccupied row, `M_i(alpha)` is even and `M_i(alpha) mod 4` is independent of alpha: any nonzero character flips two signs. For an occupied row, it is odd and

`M_i(alpha) = d_i (-1)^alpha(z_i) (mod 4)`, `d_i` in `{+1,-1}`.                               (4.1)

Indeed a nonzero character flips two of the four b locations, except that the missing `z_i` removes one flipped term precisely when `alpha(z_i)=1`.

The occupied graph-Y rows have b-Walsh transforms `+/-4` at their respective `phi_i` and zero elsewhere. The two unoccupied graph-Y rows have b-Walsh transforms `2 tau_i(-1)^q(alpha+mu_i)`. Denote their signs including the row weights by

`R_i=tau_i(-1)^[beta(i)+s F_i+q(alpha+mu_i)]`, `i=b,b'`,

and the occupied mate residues including row weights by

`T_i=d_i(-1)^[beta(i)+s(1+F_i)+alpha(z_i)]`, `i=a,a'`.

The unoccupied mate contributions give one alpha-, beta- and s-independent bit `k`: their `2M_i`, including any sign, are unchanged modulo 8. The occupied graph terms, the two bent graph terms and the two odd mate residues give the actual congruence

`A_1/4 = k + 1_[alpha=phi_a] + 1_[alpha=phi_a'] + (1+R_b R_b')/2 + (1+T_a T_a')/2 (mod 2)`.  (4.2)

All fractions here are ordinary integers before reduction mod 2. This also shows `A_1` is a multiple of 4. The product `R_b R_b'` has exponent, up to a constant,

`beta(Delta)+s(F_b+F_b')+alpha(J(mu_b+mu_b'))`,

and `T_a T_a'` has exponent, up to a constant,

`beta(Delta)+s(F_a+F_a')+alpha(z_a+z_a')`.

For a bit `v`, `(1+(-1)^v)/2 = 1+v (mod 2)`. Thus the two `beta(Delta)` terms cancel in (4.2), while their s terms add to `s sum_i F_i=s`. Finally, the function `1_[alpha=phi_a]+1_[alpha=phi_a']` is affine on the four-element alpha space, with linear coefficient `J(phi_a+phi_a')`: if the two phi coincide it is zero, otherwise it is the indicator of the affine line containing those two points. Hence, for an object-dependent constant `c`,

`A_1(s,alpha,beta)/4 = s+c+alpha(z_a+z_a' + J(mu_b+mu_b'+phi_a+phi_a')) (mod 2)`.

The four `rho_i` are distinct two-bit covectors, so their sum is zero. Substituting the definitions of mu and phi and then (3.3), the coefficient of alpha is

`z_a+z_a' + J(nu_a+nu_a'+theta_b+theta_b') = 0`.

Consequently

`A_1(s,alpha,beta)/4 = s+c (mod 2)` for **every** alpha and beta.                                  (4.3)

This is the key place where the simultaneous X profiles, actual graph phase, actual missing mate positions and the odd F table meet. It is not a consequence of the U3 count table alone. Let `s_*` be the one actual slice on which (4.3) is odd. It is determined by this object, not chosen by changing `t`.

## 5. Common-Y paired caps and the physical Z4 contradiction

Residue `4 mod 8` and cap 12 make each full coefficient have absolute value 4 or 12. Parseval with total energy 128 forces exactly eight full coefficients of magnitude 4. For each actual `(s,alpha,beta)`, both caps are equivalent to `|A_0|+|A_1|<=12`, and `A_0/4` and `A_1/4` are integers of opposite parity.

There are 16 partial frequencies in each s slice. By (4.3), in the even slice `|A_1|` is 0 or 8; in the odd slice it is 4 or 12. Let `n` count the even-slice 8s and `m` the odd-slice 4s. The ell-one spatial energy 72 and partial Parseval give

`4n + m + 9(16-m) = 144`, hence `n=2m`.                                                    (5.1)

Every 8 and every 4 contributes at least one of the eight small full coefficients, so `n+m=3m<=8`; thus `m` is 0, 1 or 2. Let `H` count the odd-slice 4s whose `A_0=0`, and let `Z_4` count the even-slice zero-`A_1` pairs with `|A_0|=4`. A pair with `|A_1|=12` has `A_0=0`; a pair with `|A_1|=4` has `A_0=0` or `|A_0|=8`. Counting all eight small full coefficients gives

`8 = n+m+H+2Z_4 = 3m+H+2Z_4`, with `0<=H<=m`.                                               (5.2)

For `m=0`, `H=0`; for `m=1`, parity forces `H=1`; for `m=2`, `H` is 0 or 2. Therefore, in the **entire same odd slice** `s_*`, at most two `A_0(s_*,alpha,beta)` are nonzero, and every nonzero one has magnitude exactly 8. This conclusion is about the actual partial transforms of one Y, not a fabricated spectrum.

Invert the 16-point Walsh transform in `(alpha,beta)` on that fixed s slice. For every actual ell-zero `(i,b)`,

`Y(0,0,i,b)+(-1)^s_* Y(0,1,i,b) = (1/16) sum_(alpha,beta) A_0(s_*,alpha,beta)(-1)^[alpha(b)+beta(i)]`.

The right side has absolute value at most `2*8/16=1`. At the actual Z4, however, `b!=0`, so its opposite-h site at the **same physical `(i,b)`** is another Z site, with magnitude 0 or 2. The left side consequently has magnitude at least `4-2=2`. Contradiction.

This fixed-slice inversion is essential: the actual Z4 is paired with the physical opposite-h site at the same nonzero b, not with a virtual site, independently chosen spectrum, or potentially full `b=0` site. The proof covers both possible E occupancy types and all lambda/other-column alternatives allowed above. It does not assume a full-site Y bound or that graph Y rows are all affine.

## 6. Coverage, source pins and process

After Main's direct actual-dispatch notice I read the complete dispatch receipt and manifest. **Order disclosure:** I read prepared metadata next, to identify the freeze-receipt and final-binding paths, and then read those two through their endings. If the task's enumerated administrative-file order was intended to be strict, this is a control-read-order deviation; it was directly disclosed to Main, not backdated. I read all **22** manifest-listed controls completely as status/permission only and sent Main the direct PREBODY ACK with `22 controls; part 01 = 713 LF; no body/math/comparison`. Only after that ACK did I read part 01 serially in raw windows `1–20, 21–40, ..., 681–700, 701–713`, through its ending and including the long lines. All packet parts were fully read before mathematical work. There was no claim of clean cognition; all genuine held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remained NONINPUT. No outgoing links, old code, sibling returns or unspecified scientific source was opened.

The following administrative SHA-256 values for this wave were directly observed using the native `openssl dgst -sha256` command, after the complete packet read: actual dispatch `5a3d464f1958e93230cec23d1822134bfb72e393783a4b4f97946f583b8cef5a`; manifest `3eb67433b44fc0304053d1c4a55cbed99ce7c3867047d25b85fdbd53f9538a1a`; freeze receipt `255fc07707322ce524011ff2989c3c5a617ffd122d67908041a7efd0dc874708`; final binding `2d7936dd8b3e6ac9d23d152639795b473dac6d2713b8a88412cd4fa5760cfb54`; prepared metadata `0a3a13c4da0e70e887c8e213f63a6e370be6a15e12a2d50f7ab4f18ba7ecd363`; complete literal packet part 01 `cd38d1afd6a2a0567f508e23b7bfd0fe20982644bf58c71afeaa99e3fac3253f`. Administrative hashes do not certify mathematical correctness.

The complete source bodies rendered in that packet, with **manifest-supplied** source SHA-256 pins and LF counts, are (paths relative to `institute/runs/three-area-2026-10-27-96h/`):

| ID | Complete source path | LF | SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/parent-omitted-ell0-lambda-singleton-proof-gap-major-v1.md` | 7 | `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca` |
| S2 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-quotient-census-erratum-v1.md` | 9 | `90c4242e118be887f19b61ccba23f4af0c6062516142962b9a315557c0e03606` |
| S3 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-candidate-v1.md` | 121 | `e4e1c4a1812a03d0334dbee16dec50650d6a904e0e68b75dbcddae22e73aefa8` |
| S4 | `review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/author-candidate-v1.md` | 188 | `018c8b9b56b1d2f5d26808204b9a1217c189a2ec0de2afa8fda1361fd52555cd` |
| S5 | `review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/author-candidate-v1-addendum-1.md` | 15 | `4dddaf7084e784b8c8d2b51b857320a26438a6a669b1ad9dee2f8d19268c4114` |
| S6 | `dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md` | 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S7 | `dispositions/info-6-entire-four-E-row-d0-actual-common-y-obstruction-parent-v1.md` | 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S8 | `review-waves/f755-boolean-remaining-D0-profile-and-U3-integer-finite-author/parent-u3-local-profile-v2-run-v1-receipt.json` | 256 | `d3cdcca328bf4c902c214ddbb9b5d42fccb41f56406147681c3baf2880f5aaf1` |

All 22 complete status-only controls were read through their endings. Their manifest-supplied pins below are relative to the same run root; they are administrative input identifiers, not premises for the mathematical proof:

| # | Control path | SHA-256 |
|---:|---|---|
| 1 | `prospective-author-method-scope-restoration-20261030-v1.json` | `6ab69778c11dbfc4ac895f97b381cc70d0059a5723d6b02f62b9957c7e8dcd95` |
| 2 | `contract-addendum-2-frontier-first-owner-direction-v1.json` | `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce` |
| 3 | `parent-L1-selected-diagnostic-release-quarantine-v1.json` | `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f` |
| 4 | `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json` | `e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc` |
| 5 | `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json` | `23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4` |
| 6 | `parent-ame-held-compression-claim-consumer-quarantine-v1.json` | `c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0` |
| 7 | `parent-held-ph-registration-report-consumer-quarantine-v1.json` | `97fbd5967b472783c5ed860f0745b88d7917eb93e1c340f043c974a531ac1453` |
| 8 | `review-waves/f439-depolarizing-ancillary-all-dimensional-repair-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `74f9f9d57eb5866f68dec331b9bf4facca2bc8d4116186cd241b3bff1539dfee` |
| 9 | `review-waves/f444-spr-full-seven-coefficient-enlargement-and-all-ray-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `d00f41bf0205680ef8256f38c97d2023058da935c260ba5cc7f17cb77bd8e184` |
| 10 | `review-waves/f448-kac-actual-second-arm-exterior-module-and-character-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `f6ccc5fa10f0e30536921ea86828c437359869413919eae258cbbd82d4989805` |
| 11 | `review-waves/f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `649349cfe636c88e60bee96400512ae6db8d8e12b875d3d100fcce3312785fd8` |
| 12 | `review-waves/f513-boolean-five-span-physical-four-fibre-xor-obstruction-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `cb9a81b76acaf740e2d691664e57e46a274c208f44fb071f5f0724973ae1a1a8` |
| 13 | `review-waves/f586-semigroup-finite-pure-source-free-band-regularity-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `e4d3dca7c41456e4e48dc154719b1df9e653b656b2cbf9324c82b195e3539681` |
| 14 | `review-waves/f602-olson-deficit-six-protected-triples-independent-actual-word-check/parent-selected-diagnostic-process-major-quarantine-v1.json` | `df412094a47e89be2507d7a7809d68449f08476aabfaca44fd9ecb4dce2a40b8` |
| 15 | `review-waves/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json` | `3f4b2c6d31a420ecff35a6478ce7a302637765b1203c046619715eda634b6927` |
| 16 | `review-waves/f653-sun8-psl2-small-exception-actual-cosets-written-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `a85930a9b268d472d5ded2f31b4b9916394e99f97e854c3a3869a9c8fd7ec8de` |
| 17 | `review-waves/f654-sun8-primepower-source-and-actual-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `9aaf84aabb3ea428e3622c5e6b7961d21bd3f1a8b3a16a727be203077e784462` |
| 18 | `review-waves/f659-fresh-original-input-sun8-source-and-normalcut-consumer-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `abf867950e1425ed74e1a766f6838957b255694cf0f64e936a23321c1324913b` |
| 19 | `review-waves/f660-fresh-original-input-sun8-exceptional-actual-coset-review/parent-selected-diagnostic-process-major-quarantine-v1.json` | `f5007a354d6acb8335ad2b9cc170f457c542640e1bbd15c5439d69d0c76039ab` |
| 20 | `review-waves/f662-report-v23-werner-core-falsification-documentary-audit/parent-selected-diagnostic-process-major-quarantine-v1.json` | `7dc07513bb05a7b08ba9795b566f38c39750a8f71fc68d576ea4367d4b0e4c38` |
| 21 | `parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json` | `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c` |
| 22 | `parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json` | `27390c73fd6741217ce1d86c5f41e388ef87e3f51b306565053943e0333afbce` |

**NOT TESTED / no child scientific execution:** no scientific program, interpreter, numerical enumeration, solver, CAS, test, build, lint, formatter, external-model CLI or network was run. No new source is supplied. S8 describes an earlier parent finite run at its own local/profile and integer scope; it is not execution or verification of this new proof. The candidate requires complete independent reconstruction, import checking and a separate parent disposition. Its mathematical claims are not self-adopting. Remaining branches, V, original-caller lifting, human/kernel/cross-family and novelty are open at this return's scope.
