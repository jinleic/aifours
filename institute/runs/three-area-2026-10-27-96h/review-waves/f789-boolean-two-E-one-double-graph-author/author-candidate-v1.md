# F789 — two E-row D0 and both graph mates in one row: common-Y obstruction

**Status: complete conditional written no-go candidate, nonblind same-harness GENERAL AUTHOR; not parent-adopted or independently checked.** At the actual rank-two five-span interface listed below, if exactly two of the four D0 sites are E sites and the other two are physical graph mates in the **same** graph row, the same physical object cannot also have J=1 and all 64 U3 caps. This covers E allocations `2` and `1+1`, graph λ singleton, E λ singleton and E λ plane, all signs, and the specified carried character t. It is not a global rank-two, original-caller, V, or NL242 result. The proof is written reasoning, not output of a scientific program.

## 1. Exact assumptions and what is imported

Work with one actual physical `f/R, a, g, u, x=U0, y=U3`, not separately chosen X and Y. Rows have coordinates `(ell,h,i,b)` with `ell,h in F2` and `i,b in F2^2`. In graph row i, the four graph sites are `(1,F_i,i,b)` and their physical same-b mates have `h=1+F_i`; the actual graph has `sum_i F_i=1` in F2. The two full sites are `(0,h,0,0)`, the six E sites are `(0,h,i,0)` for nonzero i, and the Z sites have `(ell,b)=(0,nonzero)`.

Use the **given** transported original-DC character t, with `xhat(t)=0`. Put `X=(-1)^t x`, `Y=(-1)^t y` for analysis only. They are modulations of the same physical x/y by the same fixed character; a, g, f, the graph, and t are not independently changed. The full Y spectrum is just the translate of the full y spectrum.

The precise imported interface from packet S4/S6/S7 is:

1. There are four D0 sites total, here exactly two in E and two graph mates in one row `j`; six Z2, a **unique** Z4 and 17 Z0. On each graph site `|X|=|Y|=1`; at a D0 graph mate `|X|=2, Y=0`; at each other graph mate `X=0, |Y|=2`. At Z4, `X=0, |Y|=4`, while every other Z has `|Y|=0 or 2`. These statements refer to actual physical sites.
2. For `eta=(s,alpha)` with `s in F2`, `alpha in (F2^2_b)^*`, define

   `Z_(ell,i)(s,alpha) = (1/4) sum_(h,b) X(ell,h,i,b)(-1)^(s h+alpha(b))`.

   All eight `Z_(ell,i)(0,0)` vanish. On the **same X**, each of the other seven columns is either a singleton `±2` or four `±1` entries supported on an affine two-flat in the three-bit quotient `(ell,i)`, with product of the four signs `-1`. We will need the zero columns and the six columns with `alpha != 0`; we also retain the λ profile, `lambda=Z(1,0)`, to identify the subcases.
3. On the graph `Y=-agX`; after absorbing row constants into signs, the actual physical phase has graph restrictions with **four distinct** b-covectors `r_i`, and the common graph g is the quadratic sign `(-1)^(1+b_0 b_1)`. Thus, whenever the graph X row is `sigma_i(-1)^theta_i(b)`, its same-object graph Y row has form

   `G_i(b):=Y(1,F_i,i,b) = tau_i (-1)^(b_0 b_1 + mu_i(b))`, with `mu_i=r_i+theta_i`.

   This is the imported actual phase bridge, not an assumption that Y graph rows are affine. The four distinct `r_i` are all the elements of the two-dimensional dual, so `sum_i r_i=0`.
4. The common Y has energy `sum Y^2=128`; J=1 gives each full Walsh coefficient congruent to `4 mod 8`; and all 64 full coefficients have absolute value at most 12. Multiplication by the specified t preserves these statements. No physical inverse, phase, support, location, profile, or spectral condition is being supplied by an independently chosen array.

These are conditional imports, not independently reconstructed claims about their original source or original caller. All additional original hypotheses may remain in force. In particular the proof never assumes `t=0`, chooses graph phases independently, replaces the Z4 by a virtual point, or assumes an affine Y graph row.

## 2. The defect direction and all λ cases

Let `p != q` be the two b-positions of the graph D0 mates in row j, and put `delta=p+q != 0`. Let `kappa` be the unique nonzero b-covector with `kappa(delta)=0`; call the other two nonzero covectors `u,v`, so `u+v=kappa` and `u(delta)=v(delta)=1`.

Write the values of X at the two mates as `2 epsilon_p, 2 epsilon_q`, with signs `epsilon_p,epsilon_q`. The row-zero equation is

`sum_b X(1,F_j,j,b) + 2 epsilon_p + 2 epsilon_q = 0`.  (2.1)

Each of the other three graph rows has no nonzero X at its mates, so its graph signs sum to zero and have the form `sigma_i (-1)^theta_i(b)` for a nonzero b-covector theta_i. In two bits, every balanced four-sign row is such a signed nonconstant character. At j, (2.1) gives exactly two possibilities:

* **Equal mate signs:** the graph row is constant, `theta_j=0`, and its graph λ entry is `±2`. The profile rule makes λ exactly this graph singleton, with every E-side entry zero.
* **Opposite mate signs:** the graph row is balanced, so `theta_j != 0`, and all graph λ entries vanish. The profile rule leaves exactly an E-side singleton `±2` or an E-side four-entry plane `±1` with sign product `-1`.

This is an exhaustive case split, not a claim that each alternative has an actual common-Y realization. The two E-D0 sites may both lie in one E row or lie in two distinct E rows; neither allocation is discarded or assumed realizable.

## 3. Same-X seven-profile lemma: `sum_i theta_i = kappa`

All sums of covectors below are in the two-dimensional F2 dual. Let `k_alpha` be the number of the three **other** graph rows whose `theta_i=alpha`. For `alpha != 0`, at one of those rows the graph-side quotient entry is `±1` exactly when `theta_i=alpha`, and is zero otherwise.

The following parity observation is essential. If a nonzero-eta column has graph-side entries all in `{0,±1}`, the number of its nonzero graph entries is even. A singleton `±2` cannot contain any graph `±1`; otherwise the four entries occupy an affine two-flat in `(ell,i)`, whose intersection with the graph plane `ell=1` has cardinality 0, 2 or 4. We do not infer this parity when a graph entry is `±2`.

At j the actual column equals

`Z_(1,j)(s,alpha) = sigma_j (-1)^(s F_j) 1_(alpha=theta_j) + (1/2)(-1)^(s(F_j+1)) [epsilon_p (-1)^alpha(p) + epsilon_q (-1)^alpha(q)]`.  (3.1)

First suppose `epsilon_p=epsilon_q`. Here `theta_j=0`. The mate term in (3.1) is `±1` for `alpha=kappa` and zero for `alpha=u,v`, for both s. The graph-side parity observation yields `k_kappa` odd and `k_u,k_v` even. Hence

`sum_i theta_i = 0 + (k_kappa mod 2) kappa + (k_u mod 2) u + (k_v mod 2) v = kappa`.

Now suppose `epsilon_p=-epsilon_q`, so `theta_j` is nonzero. The mate term in (3.1) is zero at `kappa` and has magnitude one at each of `u,v`.

* If `theta_j=kappa`, the graph-side parity observation at the three characters says that `k_kappa,k_u,k_v` are all odd. The three other rows therefore contribute one of each covector; their XOR is zero, and adding `theta_j` gives `kappa`.
* If `theta_j=u` (the `v` case is symmetric), the two terms of (3.1) at alpha=u have magnitudes one and opposite relative s-dependence. One s-slice has a graph entry `±2`; the singleton profile then forces `k_u=0`. At alpha=v the j entry is `±1`, so `k_v` is odd. At alpha=kappa the j entry is zero, so `k_kappa` is even. Therefore the XOR is `theta_j+v=u+v=kappa`.

Thus in **all** three λ cases and for either E allocation,

`sum_i theta_i = kappa`.  (3.2)

This is derived using the actual, simultaneous profile columns of the same X. It is not a free choice of row characters and does not rely on any selected numerical example.

## 4. One complete even and one complete odd partial-Y slice

For `s,alpha,beta` define actual partial Walsh transforms

`A_ell(s,alpha,beta) = sum_(h,i,b) Y(ell,h,i,b)(-1)^(s h+alpha(b)+beta(i))`.

There are 16 `(alpha,beta)` frequencies at each s. From the phase import, put `mu_i=r_i+theta_i`; (3.2) gives

`sum_i mu_i = kappa`.  (4.1)

For the graph row let `Ghat_i(alpha)=sum_b G_i(b)(-1)^alpha(b)`. The two-bit quadratic Walsh identity gives

`Ghat_i(alpha) = 2 tau_i (-1)^((alpha_0+mu_i0)(alpha_1+mu_i1))`.  (4.2)

For completeness, (4.2) follows by summing first over b_0: only `b_1=alpha_0+mu_i0` survives, giving the displayed sign and factor 2. For fixed `(s,alpha,beta)`, set

`xi_i = (-1)^(s F_i+beta(i)) Ghat_i(alpha)/2`,

so each `xi_i` is `±1`. The graph contribution to `A_1/4` is `(1/2) sum_i xi_i`, an integer whose parity is the parity of the number of negative xi_i, equivalently is encoded by `product_i xi_i`. The sum of the four beta values is zero and `sum_i F_i=1`. By (4.1),

`product_i xi_i = C (-1)^(s + alpha_0 kappa_1 + alpha_1 kappa_0)`  (4.3)

for a sign C independent of `s,alpha,beta`. Since kappa is the unique nonzero covector annihilating nonzero delta, the vector delta is `(kappa_1,kappa_0)` in these two-bit coordinates. Hence the last exponent in (4.3) is `s+alpha(delta)`.

For the 14 graph D3 mates, put `D_i(b)=Y(1,1+F_i,i,b)/2`; it is `±1` at a D3 mate and zero at the two D0 mates. For every row, `Dhat_i(alpha)` is even, and the mate contribution to `A_1/4` is an integer. For a full four-mate row, `Dhat_i(alpha)/2 mod 2` does not depend on alpha: a nonzero b-character flips exactly two signs. At row j the two nonzero D3 mates are at the complementary b-points `r,w`; since the XOR of all four b-points is zero, `r+w=p+q=delta`. Consequently the parity of `Dhat_j(alpha)/2` is a constant plus `alpha(delta)`: it is 1 precisely when the two character-weighted mate signs agree. Multiplying any row by its `(-1)^(s(F_i+1)+beta(i))` sign does not change its parity modulo 2.

The graph parity in (4.3) and the defect-mate parity therefore cancel their identical `alpha(delta)` dependence. There is a fixed `s_o in F2` such that, **for every** alpha and beta,

`A_1(s_o,alpha,beta)/4 is odd`, and `A_1(1+s_o,alpha,beta)/4 is even`.  (4.4)

This is one parity statement about one common Y, not separately tuned coefficients. No value of `s_o` is chosen in advance.

## 5. Common cap, exact small-count budget, and the physical Z4 contradiction

For each `(s,alpha,beta)` the two full Y coefficients are `A_0+A_1` and `A_0-A_1`. Both caps are equivalent to

`|A_0|+|A_1| <= 12`.  (5.1)

Their common residue `4 mod 8` implies that `A_0/4` and `A_1/4` are integers of opposite parity. Every full magnitude is 4 or 12. Full Parseval and `sum Y^2=128` give exactly eight full coefficients of magnitude 4:

`16 N_4 + 144(64-N_4)=64*128`, so `N_4=8`.  (5.2)

The physical ell=1 part of this very same Y has energy `16 + 14*4 = 72`. On the even slice of (4.4), let n count pairs with `|A_1|=8`; all other pairs there have `A_1=0`. On the odd slice let m count pairs with `|A_1|=4`; all other pairs there have `|A_1|=12`. Partial Parseval gives

`4n + m + 9(16-m) = (32*72)/16 = 144`, hence `n=2m`.  (5.3)

A pair with `|A_1|=8` contributes exactly one magnitude-4 full coefficient; a pair with `|A_1|=4` contributes at least one. Thus `n+m=3m<=8`, and `m` is 0, 1, or 2. More precisely, by (5.1) and the opposite parity rule:

* `|A_1|=12` forces `A_0=0` and contributes no small coefficient;
* `|A_1|=8` forces `|A_0|=4` and contributes one;
* `|A_1|=4` has `A_0=0` (two small coefficients) or `|A_0|=8` (one);
* `A_1=0` has `|A_0|=4` (two small coefficients) or `|A_0|=12` (none).

Let e count odd-slice `|A_1|=4` pairs with `A_0=0`, and z count even-slice `A_1=0` pairs with `|A_0|=4`. Then

`8 = n+m+e+2z = 3m+e+2z`, with `0<=e<=m`.  (5.4)

For m=0, the entire odd-slice A0 is zero. For m=1, (5.4) forces e=1, so again the entire odd-slice A0 is zero. For m=2, (5.4) gives either e=2, again with entire odd-slice A0 zero, or e=0, with **exactly two** nonzero odd-slice A0 values, each of magnitude 8. In every possibility,

`sum_(alpha,beta) |A_0(s_o,alpha,beta)| <= 16`.  (5.5)

Invert the actual 16-point `(i,b)` Walsh transform. At every physical `(i,b)`,

`Y(0,0,i,b)+(-1)^s_o Y(0,1,i,b) = (1/16) sum_(alpha,beta) A_0(s_o,alpha,beta)(-1)^(alpha(b)+beta(i))`,

so (5.5) makes the absolute value of the left side at most 1. But the actual Z4 has some physical `b != 0` and magnitude 4. Its opposite-h site has the same i,b, is a **different Z site**, and has magnitude at most 2 because Z4 is unique. Therefore the absolute value of that same left side is at least `4-2=2`. This contradiction completes the conditional no-go.

The common-Y phase/parity argument, the exact eight-small-coefficient count, and the **physical** Z4 are all load-bearing. A λ-only fixture, independent X and Y arrays, a relaxed integer census, or merely a U0 cap does not establish this conclusion.

## 6. Scope and remaining work

The result excludes the entire specified `d_E=2, graph occupancy 2` branch, including both physically possible E allocations and all three λ types in Section 2, **only if** the exact named actual-object/profile/phase/residue/cap imports hold. The proof does not require a choice of which E allocation or λ alternative occurs and gives no example of an original caller. It makes no conclusion for `d_E=2, graph occupancy 1+1`, remaining `d_E=0` branches, the V complement/odd caps, original selected-T/rank/eight-zero reconstruction, all-rank-two/five-span, NL242, novelty, source identity, independent-family, human, or kernel verification. Those remain open at this return. Packet S7's separate d_E=4 parent disposition and packet S6's existing d_E parity/census remain at their own scopes; neither is widened here.

This candidate requires the parent's complete read and independent mathematical scrutiny and disposition. No adoption, common physical witness, machine-generated numerical result, successful finite test, or execution GO is asserted. No new source is needed for this written argument.

## 7. Complete input coverage, process and SHA-256 pins

After Main's direct actual-dispatch notice and before any packet body, I read the entire actual dispatch, manifest, freeze receipt, final binding, prepared live metadata, and all 22 listed controls through their endings. All controls were status/permission only; every genuinely held episode and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. I sent Main a direct PREBODY ACK naming 22 controls and the one ordered part's 713 LF, and confirming no packet body or mathematical comparison/work yet. After that ACK I read part 01 in serial raw windows of at most 20 LF, from LF 1 through LF 713 and its ending, including long lines in full, before mathematical work. No outgoing link, old code, sibling return, held history or unlisted scientific source was opened.

For transparency: immediately after the dispatch notice I read the first three administrative lines of the required memory summary; I then invoked actual dispatch, manifest and prepared metadata in one parallel tool call, followed by freeze receipt and final binding together, followed by the controls. This presentation was disclosed in the PREBODY ACK. Main subsequently clarified directly that the administrative controls have no prescribed internal ordering as long as all precede the ACK; no event is backdated and no clean-cognition certificate is claimed.

Administrative SHA-256 values independently observed by `shasum` after the complete packet pass:

| Item | SHA-256 |
|---|---|
| actual dispatch receipt | `6ade7e2196afcb004c8b854dac56016369d42690367be50b8d3a21076b9b6ee5` |
| manifest | `2400989d05e7a36dc2a0e497a02590aed1129e713c795d9c1e69fe9fbf5aed03` |
| freeze receipt | `00050c69d76d01392e1acdfc16b217786a596b3a578da741c63d21c263d8ec47` |
| final binding | `07cb4136838d1bb10ae4885c1f14be2ba4aa3ac261e9c90f71dbc2657eaa2c8d` |
| prepared metadata | `1ef0df302898b9b46df13249c0bfc5e6fd042f79b3077c741216671409048082` |
| complete packet part 01, 713 LF | `cd38d1afd6a2a0567f508e23b7bfd0fe20982644bf58c71afeaa99e3fac3253f` |

All eight declared complete source bodies appeared in that packet and were read through their endings. The following source hashes are **parent-supplied pins** in the manifest/final binding, not independently re-hashed direct-source reads. Paths are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`:

| ID | Complete source, LF | SHA-256 |
|---|---|---|
| S1 | `review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/parent-omitted-ell0-lambda-singleton-proof-gap-major-v1.md`, 7 | `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca` |
| S2 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-quotient-census-erratum-v1.md`, 9 | `90c4242e118be887f19b61ccba23f4af0c6062516142962b9a315557c0e03606` |
| S3 | `review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/author-candidate-v1.md`, 121 | `e4e1c4a1812a03d0334dbee16dec50650d6a904e0e68b75dbcddae22e73aefa8` |
| S4 | `review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/author-candidate-v1.md`, 188 | `018c8b9b56b1d2f5d26808204b9a1217c189a2ec0de2afa8fda1361fd52555cd` |
| S5 | `review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/author-candidate-v1-addendum-1.md`, 15 | `4dddaf7084e784b8c8d2b51b857320a26438a6a669b1ad9dee2f8d19268c4114` |
| S6 | `dispositions/info-6-E-row-D0-parity-correct-lambda-cases-and-common-U3-census-parent-v1.md`, 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S7 | `dispositions/info-6-entire-four-E-row-d0-actual-common-y-obstruction-parent-v1.md`, 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S8 | `review-waves/f755-boolean-remaining-D0-profile-and-U3-integer-finite-author/parent-u3-local-profile-v2-run-v1-receipt.json`, 256 | `d3cdcca328bf4c902c214ddbb9b5d42fccb41f56406147681c3baf2880f5aaf1` |

All 22 status/permission controls were read completely. Their following pins are those supplied in the manifest and parent final binding; paths are relative to the same root (the `review-waves/...` directory identifies each repeated basename):

| # | Complete control | SHA-256 |
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

Actual UTC clock observed before creation: `2026-10-31T01:20:24Z`; it is not asserted as the file-creation time. The only shell operations were administrative `shasum` and `date`. No scientific code, interpreter, solver, CAS, test, build, lint, formatter, external-model CLI, network, Git, installation, or deletion was run. Administrative hashes establish byte bindings only, not mathematical correctness, prior-exposure isolation, or source identity.
