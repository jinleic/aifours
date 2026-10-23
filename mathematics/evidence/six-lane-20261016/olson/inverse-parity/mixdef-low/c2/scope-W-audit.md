# Scope audit of Lemma W (proof-Rstar-partial-v2.md Sec. 2) -- requested by Main 2026-10-17 ~16:5x PDT

Owner OlsonParity2.  Written after host clock 2026-10-17T16:5x PDT (exact time in out/freeze.txt).  Audit only:
no extension of Lemma W beyond MIX_low is claimed here.

Lemma W (as frozen): normalized MIX_low avoider (all k reflection runs odd, k <= p, 1 <= B < kappa, g = kappa - B)
with B >= g + 1 has an identity 2p-subword.

## Every ingredient and the hypotheses it uses

| step | ingredient | hypotheses actually used | MIX_low-specific? |
|---|---|---|---|
| setting | Lemma H with beta = 0 (all reflection runs odd); D = 2p - k + 2g, A = D + B | all-odd (MIX_low via Lemma OR) | all-odd |
| setting | A <= 2p - 1 (else rho_1^{2p}) => 2g + B <= k - 1 | none beyond all-odd | no |
| lifts | integer lifts x_t = u_t (mod p) with sum_t x_t = p AND singleton bounds x_t >= U_t + 1 (phi_t <= gam(d_t)) | r2 Lemma S: its proof uses D >= p + 2g and 2g + B <= p - 1, i.e. k <= p (prefix-lift existence, the two vertex computations) | YES (k <= p) |
| Fact F(a) | no run with d >= 2p - 1 | 2g + B <= k - 1 | no |
| Fact F(b) | d >= 2g + B + 1 => bh >= 2 | singleton bound + F(a) | only via the singleton bound |
| Fact F(c) | d <= 2g + B => gam(d) = g - 1 => phi <= g - 1 | needs d - p <= g - 1, i.e. 2g + B <= p + g - 1 (true if 2g + B <= p - 1) | YES as written (g + B <= p - 1 suffices) |
| Lemma KL | prefix argument (c changes by <= phi_t + 1 <= g; bh <= 0 first) | general | no |
| Lemma KL | Lemma K Corollary: (i) x(P) <= p - m, (iv) x(P) >= m - p, (v) phi(P) <= D - g + m - 1, (vi) BH(P) >= -A | (i), (iv): 2g + B <= p - 1; (v): D >= 3g + 1 - 2m (from D >= p + 2g); (vi): D >= 4g - 2m (from D >= p + 2g) | YES |
| Step 1 | W(cheap) >= p + 2g - A/2 >= 2g + 1/2 | sum_t (phi_t + 1) = p + 2g (needs sum x = p exactly), A <= 2p - 1 | only via the lifts |
| Step 2 | not every run cheap: cheap runs form paths; on each path the heavier parity class has >= half the weight | none (paths, no odd cycle) | no |
| Step 2 | every run cheap: total weight is exactly p + 2g; delete one run t0 (w <= g), heavier parity class of the path [k] \ {t0} has weight >= (p + g)/2 >= g + 1; path ends not adjacent since k >= 4 | p >= g + 2, k >= 4 | no (odd-cycle issue avoided by deleting t0; no half-weight claim on a cycle is used) |
| Step 3 | <= g + 1 runs, BH(S) <= g + 1 <= B | B >= g + 1 | no |

## Consequences for a transfer to MIX_high (k >= p + 1), not claimed

A transfer would need, in the high-run setting: (1) lifts with sum x = p and the singleton bounds phi_t <= g - 1 on the
runs used (OlsonRunCount's chain lifts give sum x = p, but singleton bounds/chain independence are not automatic for
B >= 1, cf. their mixdef/README.md Sec. 6 example p = 11, k = 19); (2) the six exact window conditions of Lemma K for
the KL prefix P (c(P) in [g + 1, 2g], BH(P) <= B, D_P >= -B) re-checked with D = 2p - k + 2g < p + 2g and possibly
2g + B > p - 1 -- the automatic Corollary does NOT apply as written; (3) gam(d) = g - 1 for d <= 2g + B needs
g + B <= p - 1.  Steps 1-3 (weights, paths, all-cheap case) are generic once (1)-(3) hold.
