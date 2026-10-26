# Peer review v79-B: NL242 normalized (16,24) joint-union completeness and applicability audit

Reviewer owner MathShor (runtime MathShor-2). The last actual `/bin/date` before composing this write returned `Sun Oct 25 11:22:26 PDT 2026`. That is an earlier-observation bound, not an invented creation second.

**Pins**

| Item | Path / range | SHA-256 | Read |
|---|---|---|---|
| Assignment | `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v79.json`, entry v79-B | `785533fb4a4cf0908d60725465e43a4e159438bb350d236eeb85562e8b9b38fe` | raw LF1–24 and LF143–476 |
| Receipt | `peer-review-wave-eighteen-v79-packet-receipt-v1.json` | `cc30b4db64f6020013ba185d391a93b90fe2cc9039fe9437ab39cd04f362e45f` | raw LF1–50 |
| Exposure ACK | `peer-review-nl242-normalized-union-completeness-ack-v1.json` | `a4ae7adfcbf4fe45ade6578123b7c1271917c86a77bbf16e197cd955ddd86744` | written 11:06:55, before any proof body |
| Own Shor primary checkpoint | `primary-continuation-20261025-102319-checkpoint-01-v1.json` | `92828815cc6284cd18f8e0f783b4e08385de9ffb67edeb4634b39571af36b371` | written 11:04:18, before this temporary review |

**Mandatory read order** was observed: v9 (b7c92143…, raw 1–35), then v10 (d61acbf7…, raw 1–31), then v11 (3ce29e3c…, raw 1–40), then the manifest entry and receipt, then the ACK, then the parts.

**Character of this review.** Same-harness, same-family, cross-domain, SERIAL written reconstruction. My exposure:
- I am the actual v69-A reviewer of the even proof (S11).
- The v69-A packet contained the complete v4 odd body (S10), which I read in full then, so the odd proof is not new to me.
- I wrote the older v19 two-spectrum completion review (S15:25).
- I wrote the NL242 reviews v30-C, v32-F, v37-A, v43-C and v53-A.

No earlier verdict is transferred. This is not blind, cross-vendor, human, formal, kernel, executable or novelty acceptance.

## 0. Verdict

| Scope | Result |
|---|---|
| Forward composition: S4 items 1–5 together with S5 §§1–4 | **0 FATAL / 0 MAJOR / 0 MINOR** at the reconstructed scope (§§2–8) |
| Separation of the global L floor and u24 frontier (S4:27, S5:44–46) | Correct. Neither is consumed by the forward case (§7.2). Both remain NOT_RECONSTRUCTED named imports, used only for the global frontier and the conditional converse. |
| Branch-internal contradictions: O §§5–7 (S10:155–215) and E §§3–8 (S11:73–257) | NAMED IMPORTS at parent scopes S12 and S13. Here I give spot re-derivations only (§7.4); this gate does not re-certify them. |
| Editorial observations | Three, not defects (§10). |

**Supported statement (CONDITIONAL, WRITTEN).** At the dependency union J_N of §9, no pair exists that satisfies all of the following:
- genuine canonical normalized pair on eight bits with both actual inverse transforms;
- cap 28;
- D = R/8 mod 2 quadratic of polar rank 2 and weight 192;
- an actual R zero normalized to 0;
- original counts (L,u) = (16,24).

Through the nine-variable bridge, there is consequently no balanced nine-variable function with peak ≤ 28 of intrinsic type (2,192) with (L,u) = (16,24).

This is not import-free. It is not a stronger acceptance of either branch and does not resolve any other stratum. The old even parent's final composition paragraph (S13:20–22) is NOT a premise. The v11 withdrawal of its 10:04 clock label (S3:16) is retained.

## 1. Coverage

**Part 1** (`f5742443…`, 99,621 bytes, 1,195 LF) was read raw at LF1–140, 141–260, 261–380, 381–480, 481–600, 601–700, 701–830, 831–960, 961–1090 and 1091–1195, ending included.

**Part 2** (`a3e06540…`, 7,327 bytes, 52 LF) was read raw at LF1–52.

Source coverage by original LF:

| Source | LF read |
|---|---|
| S1 | 1–35 |
| S2 | 1–31 |
| S3 | 1–40 |
| S4 | 1–33 |
| S5 | 1–73 |
| S6 | 7–19, 41–93, 191–227 |
| S7 | 7–77 |
| S8 | 26–46, 147–233 |
| S9 | 70–138 |
| S10 | 1–239 (complete) |
| S11 | 1–273 (complete) |
| S12 | 1–28 |
| S13 | 1–24 |
| S14 | 1–7 |
| S15 | 1–32 |

No line was cut in the raw displays. Undeclared lines of S6, S7, S8 and S9 were not supplied and receive no read credit.

**Metadata cross-check.** My v69-A file has 324 LF and SHA `dd30f82f…`. The v62-A file has 336 LF and SHA `b91ba714…`. Both match S4:9 and S4:11. I cannot attest the parent-chronology claims in S4:15 or S13:7–9. They are not mathematical premises here.

## 2. Exact original definitions, reconstructed

**Spectra.** H is the unnormalized eight-bit Walsh matrix, H² = 256I.
- Canonical spectra satisfy HK_i = ±256 pointwise. So K_i = H(1−2f_i) is the spectrum of an actual Boolean sign, and K_i ≡ 2 mod 8.
- The cap is |K_1|+|K_2| ≤ 28.
- S = K_1+K_2, R = K_1−K_2, p = R/8 and D = p mod 2.

Write K_i = 2+8t_i. Then S ≡ 4+8D mod 16 and R ≡ 8D mod 16 (S6:47–49). The cap gives R ∈ {0,±8,±16,±24} and |S| ≤ 28.

**The zero.** An actual R zero is translated to the origin. Translation permutes spectrum values and twists the inverse signs by a character, so genuineness, canonical residues, the cap and every count (L, z, c, u) are preserved (S8:28).

**W, U and q.** Since p(0) = 0, D(0) = 0. Suppose D restricted to its six-dimensional polar radical had a nonzero linear part. Then D would be balanced on every radical coset, giving weight 128 ≠ 192. So D is constant (0) on the radical and descends to the two-bit quotient, where it has weight 3. This gives:
- W = radical, D = 1−1_W, χ = (−1)^D = 2·1_W − 1;
- Hχ = 128·1_U − 256e_0 with U = W^⊥;
- q = −Hχ/128 = 2e_0 − 1_U, so q = +1 at 0, −1 on U∖{0} and 0 at the other 252 points (S8:30–39).

**T, the defects and the ternary arrays.** Let T = χS.
- If D = 0, then S ≡ 4 mod 16 and S ∈ {−28,−12,4,20}.
- If D = 1, then S ∈ {−20,−4,12,28} and T = −S.

Hence T ∈ {−28,−12,4,20}, and |S| ∈ {4,12} exactly when T ∈ {−12,4}. The signed defect array is δ = χ at T = −12, δ = −χ at T = 4, and 0 otherwise (S7:57–61). The remaining arrays are:
- A = supp δ;
- h = Hδ and b = φ(h), where φ takes the ternary residue in {−1,0,1};
- B = HS/512;
- a = HR/512 = Hp/64.

**Original counts** (S5:17–22):

```text
L = #{|S| in {4,12}} = |A|,
z = #{p=0},  c = #{|p|=1},  u = z+2c,
alpha = #{x in U: b(x)=q(x)},
E = {x in U: b(x)=-q(x)},  nu = |E|,
n = wt(a).
```

**Norm.** HK_1 and HK_2 are each ±256. Hence HS and HR take values in {0,±512} with complementary supports, and a² + B² = 1 pointwise, exactly as integers. Here n = #{B = 0} is the size of the half-design support T. It is not the number nine of variables.

**Residue relation.** Modulo 3, S ≡ −χ + δ: check the four T values. Also 512 ≡ −1 and 128 ≡ −1 mod 3. Therefore B ≡ q − b mod 3, so B = φ(q−b) = q − b − 3q·1_E. On U, B equals q, 0 or −q according as b equals 0, q or −q. Outside U, B = −b (S7:63–72; S8:171).

## 3. Exact identities

**Energy identity (B1).** On W, p ∈ {0,±2}; off W, p ∈ {±1,±3}. Hence

```text
sum p^2 = 4(64-z) + c + 9(192-c) = 1984-4u.
```

Parseval gives n = Σ R²/1024 = 64·Σ p²/1024 = 124 − u/4. This is (B1) (S6:59–63; S8:41–44).

**Zero quantization.** Fourier inversion at the zero gives 0 = R(0) = 2 Σ_x a(x), a sum of n terms equal to ±1. So n is even, u ∈ 8Z, and Σ a = 0 (S6:67–73).

**Two evaluations of Γ = Σ χS.**
1. T² + 8T = 560 − 512·1_A holds at all four T values. Both Boolean Parseval identities give Σ(S²+R²) = 4·65536 = 262144, so Σ S² = 135168 + 256u. Together these give Γ = 1024 − 64L − 32u (S6:77–83).
2. By the Plancherel pairing, Γ = (1/256) Σ (Hχ)(HS) = 2 Σ_U(−128q)B = −256 Σ_U qB. On U, qB is 1, 0 or −1 according as b is 0, q or −q. So Σ_U qB = (4−α−ν) − ν, and Γ = −256(4−α−2ν) (S7:77).

Equating the two evaluations gives **α + 2ν = 8 − L/4 − u/8** (B2). This holds for every actual candidate, with no further premise.

**Count m.** Also #{B ≠ 0} = m + 4 − 2α − ν with m = wt(b), and #{B ≠ 0} = w_S = 132 + u/4. Substituting (B2) gives m = 144 − L/2 − 3ν (S7:75,77).

## 4. The forward implication (16,24) ⇒ ν = 0, E empty, α = 1, n = 118

At (L,u) = (16,24), the right side of (B2) is 8 − 4 − 3 = 1. Since α and ν are counts of points of the four-point set U, they are nonnegative integers, so α = 1 and ν = 0, hence E is empty. Then (B1) gives n = 118. Also Σ a = 0 and a = 1 − 2·1_V on T, so |V| = 59 for the same half-subset V = {a = −1}. Finally m = 136.

This uses only §§2–3. It does not use the three-row table of S8:153–157, the floor L ≥ 16, the frontier u ≥ 24 or any converse. Conversely, at L = 16, (B2) with α = 1 and ν = 0 forces u = 24 without any floor. So the branch hypothesis set {L16, E empty, α1} and the (16,24) stratum coincide exactly. Only the converse from α1 and E-empty WITHOUT L16 needs both global bounds. That is because 2L + u = 56 has the solutions (24,8), (20,16), (16,24), (12,32), … in 4Z × 8Z. S5:46 and S4:27 state this correctly.

## 5. The complete E-empty L16 alphabet, with two DIFFERENT dual inequalities

**The exact integer lift.** HB = Hq − Hb − 3H(q·1_E). Here Hq = −Hχ²... more precisely Hq = −(1/128)·H(Hχ) = −2χ. Also HB = S/2. Hence

```text
S = -4chi - 2C - 6P,   where C = Hb, P = H(q*1_E),
T = chi*S = -4 - 2chi*(C+3P).
```

So T ∈ {−28,−12,4,20} is equivalent to (S): C + 3P = 4δ on A and |C+3P| = 12 off A (S8:177–180, 214–216, 227). With E empty, P = 0, and we get C = 4δ on A and |C| = 12 elsewhere (S9:72–74).

**Three exact sums.** Σ C² = 16L + 144(256−L) = 256·Σ b², which gives m = Σ b² = 144 − L/2. Also Σ h² = 256L, and Σ hb = Σ δ·Hb = Σ_A 4δ² = 4L (S9:76–80).

**The support XOR is zero, and h has one residue mod 4.**
- Both C² = 144 − 128·1_A and H(C²) = 256(b⋆b) hold, so H1_A = 288e_0 − 2(b⋆b).
- At a nonzero shift, (b⋆b)(w) is even, because its summands pair under x ↦ x+w.
- So H1_A ≡ 0 mod 4 everywhere, since H1_A(0) = 16. Hence every #{x ∈ A : w·x = 1} is even and XOR(A) = 0.
- Then h(w) − h(0) = −2 Σ_{x∈A, w·x=1} δ(x) ≡ 0 mod 4, so h ≡ h(0) mod 4, which is even (S9:84–90).

**First inequality, for t ≡ 2 mod 4 only:** t² − 8tφ(t) ≥ 36 − 16φ(t)². Checked case by case:

| Case | Smallest \|t\| | LHS | RHS |
|---|---|---|---|
| φ(t) = 0 | 6 | ≥ 36 | 36 |
| φ(t) = sign(t) | 10 | t² − 8\|t\| ≥ 20 | 20 |
| φ(t) = −sign(t) | 2 | t² + 8\|t\| ≥ 20 | 20 |

If h ≡ 2 mod 4, summing with b = φ(h) gives 256L − 32L ≥ 9216 − 16(144 − L/2). That is 224L ≥ 6912 + 8L, so L ≥ 32. This is false at L16, so h ≡ 0 mod 4 (S9:94–106).

**Second inequality, only after divisibility:** for multiples t of 4 with |t| ≤ 20, F(t) = t² + 4tφ(t) − 32φ(t)² ≥ 0.

| \|t\| | 0 | 4 | 8 | 12 | 16 | 20 |
|---|---|---|---|---|---|---|
| F(t), either sign | 0 | 0 | 0 | 144 | 288 | 288 |

For example, φ(4) = 1, φ(−4) = −1, φ(8) = −1 and φ(−8) = 1, so F(±4) = F(±8) = 0. Since |A| = 16, |h| ≤ 16. From the three sums, Σ F(h) = 256L + 16L − 32(144 − L/2) = 288(L−16) = 0. So every h lies in {0,±4,±8}, and b = 0 exactly when h = 0 (S9:110–125).

**The order of the two steps is necessary, not cosmetic.** F(±2) = 4 − 8 − 32 = −36 < 0. So F alone cannot exclude residue 2. This confirms the S14 wording correction: residue 2 is excluded by the first inequality, and only afterwards does F certify the alphabet.

## 6. Exactly two active cases; a on U; σ; the forcing

With ν = 0 and α = 1, exactly one v ∈ U has b(v) = q(v) = ±1, and b = 0 at the other three U sites. The alphabet gives h(v) ∈ {±4,±8} with φ(h(v)) = q(v):
- if q = 1, then h(v) ∈ {4,−8};
- if q = −1, then h(v) ∈ {−4,8}.

That is, **h(v) = 4q(v) or h(v) = −8q(v)** (B4). The values −4q and 8q have φ = −q, which would place v in E. The magnitude 12 and every other magnitude are excluded by §5.

**The values of a on U.** B(v) = φ(0) = 0, so a(v) = σ = ±1 with σ = 1 − 2·1_V(v). At the other U sites B = q ≠ 0, so a = 0.

**The forcing is derived, not imposed.** By the convolution theorem, H(δ⋆p) = h·Hp = 64·h·a. Off U, a ≠ 0 implies B = −b = 0, which implies h = 0. On U, a ≠ 0 only at v. Hence h·a = h(v)σ·e_v, and

```text
delta star p = (64/256) h(v) sigma H e_v = (h(v) sigma / 4) chi_v,
amplitude q(v)sigma  or  -2 q(v)sigma.
```

Both signs of σ and all four locations of v are possible a priori, including v = 0 with q = +1. Nothing is chosen independently of V.

## 7. Branch quantifiers and necessary-row coverage, audited as one union

### 7.1 The hypotheses match exactly

The O theorem (S10:219) quantifies over every L16 S array, every E-empty α1 placement on q and U with |h(v)| = 4, and both forcing signs. The E theorem (S11:261) quantifies over the |h(v)| = 8 branch, with both forcing signs and every v, q and U location.

By §6, |h(v)| = 4 ⇔ h(v) = 4q(v), and |h(v)| = 8 ⇔ h(v) = −8q(v). The definitions agree: S10:21–25 and S11:15–19 use the same G, W, U, D, χ, q, b and B, the same alphabet and the same "one v with b = q, other U sites b = 0". Every candidate yields the V of §6, which satisfies the constraints both branches refute. These are p = |V∩H_x| − |T∩H_x|/2 ∈ {0,±2} on W and {±1,±3} off W, the prescribed XOR modulo 2, the slabs |p| ≤ 3, p(0) = 0, and both signs B ± a.

### 7.2 Global-pruning use inside the branches is replaceable

I read the complete bodies S10:1–239 and S11:1–273. Within them, the pruning enters only in two places:
- E-empty: S10:21 and S9:72 ("as forced for every full surviving target");
- identifying L16/α1 with the first case.

Both are supplied by (B2) and (B3) directly (§4). Where the branches use z + 2Σc_r = 24 (S10:136–138, S11:55), that follows from wt(a) = 118. In the forward case this comes from (B1) at u = 24, or equivalently from m = 136 and the norm. It does not come from Theorem A. No other use of L ≥ 16, u ≥ 24, L ≥ 12 or full affine span occurs. The optional filters of S8:194 are not invoked.

So the parent wording "at the named … pruning imports" (S12:9, S13:13) does not bring the floors into the forward J_N. The global frontier statement (S8:153–157, S15:13) and the converse of S5:46 still need them.

### 7.3 The necessary rows cover the union exhaustively

These steps come from S10 §§3–4 and apply to BOTH magnitudes:
- Htau = (64b − 4h)/3, with tau = (ζ − 4δ)/3 and ζ = C/4.
- The only nonzero U coefficient of Htau is at v: 16q for magnitude 4 and 32q for magnitude 8.
- Σ_W tau = (1/4)Σ_U Htau, and (−1)^j = −tau with j = (ζ−1)/2, so wt(j|_W) = 32 + 2q or 32 + 4q respectively.
- The common carry Q = j + k is quadratic. This follows from (K²−4)/32 ≡ (K−2)/8 and (W_Ω²−1)/8 ≡ (w²−1)/8 + I/2 mod 2, with I even. Then (K_2−2)/8 = −1 − j − k, with K_2 = −2χ − 4ζ − 4p and E empty.
- The zero indicator on W is 1 + j + Q. Adding a six-bit quadratic preserves weight mod 4, since quadratic weights are ≡ 0 mod 4 and Σ jQ is even because deg ≤ 5 < 6. So z ≡ 2 mod 4 at magnitude 4 and z ≡ 0 mod 4 at magnitude 8.

The remaining constraints:
- Each c_r is positive. Σ_t p_r = P_r(0) = 16λ_r(0) = 16σχ_v(r) = ±16, which is ≢ 0 mod 3.
- The λ_r(y) share parity, so z ≡ 2c_r mod 4. The slice energies are Σλ_0² = 64 − z and Σλ_r² = 144 − 2c_r.
- Parseval over s gives z + 2Σc_r = 24.
- Degree ≤ 3 on six bits gives z ≥ 8. The self-orthogonal rank argument gives z ≠ 10.

**Magnitude 4:** each c_r is odd and ≥ 1, and z ∈ {14, 18, 22, …}. This leaves exactly z18 with (1,1,1) and z14 with (3,1,1) up to permutation; z22 would need Σc = 1.

**Magnitude 8:** each c_r is even and ≥ 2, and z ∈ {8, 12}. This leaves exactly z12 with (2,2,2) and z8 with (4,2,2) up to permutation.

The four rows partition the stratum. O excludes the first two rows (§§6–7). E excludes the last two (§4 and §§5–8). **Cross-branch dependency:** E's "entire branch" claim consumes the even-row reduction written in the ODD file (S10:223–226), which is supported by S12:26. It belongs in J_N.

### 7.4 Written spot re-derivations; branch proofs not re-certified

**O §6 (z18).** β_0 has 46 nonzeros, so ΣT_0² = 64·46. The bound |T_0| ≥ 8 everywhere would force ΣT_0² ≥ 64·64. Contradiction.

**O §7 (z14).** ΣT_0² = 64·50, and the 48 outside points already cost 48 units. A 16 or a 24 would cost 3 or 8 extra units. So the outside values are all 8, and exactly two inside values are 8. The inactive-channel energy is then 48 + 18 = 66, but Parseval gives 144 − 6 = 138. Contradiction.

**E, the aggregate (6)/(7).** The table gives

```text
E0 = 16A+4Bc+Cc+N3+3Dc+8Ec,
E1+E2+E3 = 16N1-12Bc+8N2+3Cc+3N3+9Dc.
```

Hence 24M = 16N1 + 8N2 − ΣE_r + 3E0, and E0 ≥ 4M + N3 with M = Bc + 2A + Ec.

**E, the z12 row.** M = (2N1 + N2 − 33)/3.
- Rank 3: N1 = N2 = 24 and N3 = 8, so M = 13 and E0 ≥ 60 > 52.
- Rank 2: the character product is 1, so N1 = 48 and N3 = 16. Then M = 21 and E0 ≥ 100 > 52.

These checks are arithmetic only. The closure tables (S10 §5, S11 §3), the half-band lemma and the z8 sections (S11 §§5–8) are NOT newly reconstructed in this gate. Their support rests on v62-A and S12, and on v69-A (my serial review, not transferred here) and S13.

### 7.5 No independent phases, canonical narrowing or Gold exception

- σ, the forcing amplitude and the pair signs ε_r = −σχ_v(r) are all bound to the same a.
- The local normalizations in the closure tables permute or translate the four character positions at a fixed y. They preserve λ_0 and the nontrivial magnitudes, and never re-sign a global stream.
- The canonical normalization is a WLOG twist valid for every odd-weight half (§8), not a narrowing.
- No Gold graph, quadratic-support or affine-slice assumption occurs in S4, S5, S10 or S11.

## 8. Same V and Boolean 512; the nine-variable bridge

**The Boolean reconstruction.** F(x,0) = (1−B−a)/2 and F(x,1) = (1+B−a)/2, with signs (−1)^F(x,0) = B + a and (−1)^F(x,1) = a − B. Its spectra are therefore H(2a) = 8p on one half and H(2B) = 2HB = S on the other. Its weight is Σ(1−a) = 256 by Σ a = 0. This is S8:229–233 and S5:66–71, the same objects the branches refute.

**The bridge, for balanced f on nine bits with peak ≤ 28.** This is S6:191–227, reconstructed here.
1. The support expansion gives W_f(a) ≡ 4·#{x ∈ supp f : a·x = 1} ≡ 4(a·s) mod 8.
2. **s ≠ 0.** Suppose s = 0. In the multilinear expansion of W_f/8, the degree ≥ 3 coefficients are even, and the linear coefficients m_i/2 are integers. So W_f/8 mod 2 is quadratic with value 0 at a = 0. Then 1 + W_f/8 mod 2 is a nonzero function of degree ≤ 2 on nine bits and has weight ≥ 128. At least 128 values would then lie in {0,±16}, giving Σ W_f² ≤ 128·256 + 384·576 = 253952 < 262144. Contradiction.
3. Choose v with v·s = 1. #{supp f ∩ (s+V)} ≡ v·s = 1, so h is odd and g is odd. The XOR equation gives σ_g = σ_h.
4. **Canonical phase.** (−1)^(b·σ)·W_j(b) ≡ −2w mod 8 for odd w. Multiplying by ε_j = (−1)^((w+1)/2) gives 2 mod 8. Moreover w_g + w_h = 256 forces ε_h = −ε_g. So K_g = ηG and K_h = −ηH_half with η(b) = ε_g(−1)^(b·σ). These are genuine sign spectra.
5. Since B_0^T v = 0, W_f(a) = G + H_half on s^⊥ and W_f(a+v) = G − H_half. So R = ηW_f(a), S = ηW_f(a+v), the cap is |G| + |H_half| ≤ 28, and R(0) = 0 by balance. The restriction map is bijective on s^⊥, and R-sector values are multiples of 8. So L counts all 512 original coefficients, and D is the intrinsic W_f/8 residue.

## 9. J_N: the exact forward dependency union and named gaps

**Reconstructed here, in writing:**

| Label | Content | Where |
|---|---|---|
| DEF | definitions and normalization | §2 |
| ID | identities B1, B2, m, u ∈ 8Z, Γ | §3 |
| FWD | the forward implication | §4 |
| SLIFT | the exact integer S-lift | §5 |
| ALPH | the alphabet with the two-inequality order | §5 |
| ACT | (B4) and the forcing | §6 |
| CARRY and ROWS | carry and row reduction, from S10 §§2–4 and §8 | §7.3 |
| NORM / BOOL512 | norm and Boolean reconstruction | §8 |
| NINE | the nine-variable bridge, including the canonical-phase lemma | §8 |

**Named imports, NOT_RECONSTRUCTED in this gate:**
1. **O-internal:** S10 §5 closure tables and the §6–7 contradictions, beyond the §7.4 arithmetic. Support: S12 and the v62-A body, which is not in this packet.
2. **E-internal:** S11 §2 pair-sign lemma, the §3 closure table with signs, the §5 half-band lemma and radical binding, and §§6–8. Support: S13's decision paragraph and the v69-A body, which is not in this packet and is my serial work.
3. **Cited by O but not supplied:** `rank2-completion-consolidated-v3-intrinsic.md` (4847a567…) and `nl242-intrinsic-rminus-trades-parent-v1.md`. Every identity of them that I traced (tau cubic, Htau, the forcing) is re-derivable from supplied text. I cannot certify the absence of other dependence in unsupplied bodies.
4. **Classical lemmas:**
   - Walsh 2^k-divisibility implies parity degree ≤ m − k;
   - Reed–Muller minimum weights 2^(m−r);
   - six-bit quadratic weights are ≡ 0 mod 4;
   - quadratic Gauss sums;
   - Parseval and convolution;
   - the F_2 self-orthogonality rank bound.

**Explicitly NOT in J_N for the forward case:**
- the full-S floor L ≥ 16 (the spatial four-L theorem beyond S7:77, with its review and parent per S15:27–29);
- Theorem A u ≥ 24 (S8 LF47–146 and S15:9–11);
- the P2 bound L ≥ 12 (S6 §§4–7);
- the three-case frontier (S8:147–157, S15:13);
- the S13 composition paragraph.

The first four are required only for global pruning and for the converse without L16.

## 10. Findings

**FATAL: none. MAJOR: none. MINOR: none,** at the forward-composition scope.

Editorial observations, not defects:
1. **The label "O" collides.** S4:9 uses "statement O" for the odd parent, while S5:10 and S5:34 use "O" for the spatial source. The LF numbers disambiguate.
2. **S4:18 "all others b0"** means the other three U sites, as S5:52 states precisely.
3. **S4:25 names some J_N members only by reference** ("ALL actual hypotheses/imports of O and E"). §9 lists them explicitly: the S-lift, the canonical-phase lemma, the classical lemmas, the v3 citation and the S10:223–226 cross-branch row reduction.

**Process.** The S4:15 and S13:7–9 read chronologies are not attestable by me. The S13 header clock remains withdrawn by v11. No v79 source or shared file was modified.

## 11. Original residual and assurance

The forward (16,24) closure is CONDITIONAL at J_N. The following remain OPEN:
- entire (16,32);
- entire (20,24);
- U2;
- the rank-two type and the other residue types;
- unrestricted balanced NL242.

There is no witness, no numerical nonlinearity change and no full-type resolution. The global restriction to three strata needs the NOT_RECONSTRUCTED floors. This is a written, same-harness, serial supplied-proof audit: not formal, kernel, human, configured-family, executable or novelty acceptance.

No scientific interpreter, program, enumeration, replay, solver, nested agent, external CLI or GO was used. HOLD v2 and v9/v10/v11 bind. The Shor primary resumes from its checkpoint.
