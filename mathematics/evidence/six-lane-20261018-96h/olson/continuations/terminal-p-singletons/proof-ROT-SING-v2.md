# Theorem ROT-SING: terminal k = p, kappa^ = p-1 (all-singleton terminal blocks) forces one nonzero rotation pair, v2

Owner OlsonAssemblyLS. v2 written after /bin/date 2026-10-19T10:53:16-0700. It supersedes v1 (proof-ROT-SING-v1.md, sha256
72b6f222417e5b9b5ee46f886950691d3edad536c70c7e0b8acc0bed33eea702, written after 10:52:01, preserved, never sent) by ONE wording
repair from the author's audit: the second bullet of Sec. 4 (rigid case b = -a) now states exactly when the Step 3 sumset still
covers Z_p. No statement, step or inequality changes. Status: CANDIDATE_UNVERIFIED written proof (word level).
Scope frozen BEFORE derivation: TERMINAL-P-SINGLETONS-scope-v1.md, sha256
38d1b15deba4be3a924cc6416363ce8fad8dbe92ccfc5b4d3df19bd29774c543 (10:50:41). Inputs: the accepted normal form, GRX (with a
non-constant ARC sign pattern), Lemma CT, and the classical Cauchy-Davenport theorem. No Lev, no (S1), no ONE-SHORT-LS, no
ROT-KP+/ROT-FB(b), no computation, model call, novelty, priority, Lean or human-review claim.

## 0. Statement

THEOREM ROT-SING. Let p >= 7 be prime and w an avoider of length 4p-2 over D_(2p) (no 2p letters in increasing original index
order with identity product). Suppose SOME admissible normal form w^ of w has terminal k = p and kappa^ = p-1. Then every rotation
letter of w lies in one set {rho_c, rho_-c} with c != 0. More precisely, the rotation multiset of w is rho_c^(2p-1) rho_(-c)^(p-1).

Scope remarks (no further claim). There is no hypothesis on o_F(w) and nothing is asserted about reflection runs. The sequence
g^(2p-1)(3g)^(p-1) (rotation values 1 and 3) is the sequence-level obstruction at kappa = p-1; Step 3 shows that NO word of the
present shape realizes it as an avoider, because 1 + 3 != 0 (mod p). No step uses p >= 7 beyond p >= 5 (CT's range); p = 5 is not
claimed.

## 1. Conventions and accepted inputs

Group law (v,e)(v',e') = (v+ev', ee'); rho_x = (x,+1), sigma_y = (y,-1); identity selections contain an even number of
reflections. Rotation values lie in Z_p; Y(x) := (1,x) in C_2 x C_p = C_(2p).
(NF) Admissible normal form (proof-ROT-few-E-v4.md lines 28-43; accepted chain: fewodd addendum line 12; ZX overlays 1-3;
     lowodd item 2, overlays M1, M4). w^ is an avoider of length 4p-2 with the same F and the same rotation multiset as w, written
     cyclically as R_1 S_1 R_2 S_2 ... R_k S_k with k odd constant blocks S_i = sigma_(y_i)^(l_i) (block S_i between runs R_i and
     R_(i+1)), every empty run separating blocks of different values; H^ = (F-k)/2, kappa^ = p-1-H^, R = 2p+2kappa^-k.
(GRX) (notes-GRX-v1.md lines 7-20; lowodd verdict item 1). For EVERY cyclic constant-block representation (empty runs allowed) and
     every sign pattern z in {+1,-1}^k: f_i := [z_i != z_(i+1)], Phi := sum f_i, delta := #{i : l_i != f_i (mod 2)},
     C_max := F - delta, X^z := the rotation values of run i multiplied by z_i, T(z) := sum over i with z_i = +1 of
     theta_i, theta_i := y_(i-1) - y_i. Then w^ has an identity 2p-subword iff for some z there are an even C with
     Phi <= C <= C_max and 0 <= 2p-C <= R, and a sub-multiset of X^z of size 2p-C with sum T(z) (mod p).
     The non-constant two-change pattern below is the accepted ARC form (proof-ROT-KP-v1.md lines 34-38; ROT-KP verdict line 25).
(CT) (proof-LSplus-e2-v1.md lines 13-19; STAB-delta verdict item 6). p >= 5 prime, 0 <= kappa <= p-1, odd (ZP_kappa) Y,
     1 <= n <= |Y| with |Y|-n even in [2kappa+2, 2p]: sum_x min(n, v_x(Y)) <= p+n-2.
(CD) Cauchy-Davenport (classical): |B1 + B2| >= min(p, |B1| + |B2| - 1) for nonempty B1, B2 in Z_p.

## 2. The singleton shape

k = p and kappa^ = p-1 give H^ = sum (l_i - 1)/2 = 0, so every terminal block is a single reflection S_i = sigma_(y_i); F = p and
R = 4p-2-p = 3p-2. Let X be the multiset of the 3p-2 rotation values of w^ (equal to that of w) and X_i the values in run R_i.

## 3. Proof

Step 1 (all-plus pattern). For z = (+1, ..., +1): every f_i = 0, Phi = 0, every l_i = 1 is odd so delta = p, C_max = F - delta = 0;
hence C = 0, 2p-C = 2p <= R, and T(z) = sum theta_i = 0. As w^ avoids, NO 2p rotation values (at any positions) sum to 0 (mod p).
Equivalently the sequence Y of the values Y(x) satisfies (ZP_(p-1)): it has no zero-sum of length 2p.

Step 2 (the rotation multiset). Apply CT to Y with kappa = p-1 and n = p-2: 1 <= n <= |Y| = 3p-2 and |Y| - n = 2p is even and in
[2kappa+2, 2p] = {2p}. So sum_x min(p-2, v_x) <= 2p-4. Call x HEAVY if v_x >= p-1; each heavy value contributes p-2 to that sum,
so there are at most two (3(p-2) > 2p-4), and the excess sum_x (v_x - min(p-2, v_x)) >= (3p-2) - (2p-4) = p+2 sits on heavy values.
- One heavy value x0: v_(x0) >= (p-2) + (p+2) = 2p, and 2p copies of x0 sum to 2p x0 = 0 (mod p): against Step 1.
- So exactly two heavy values a != b, and they exhaust the bound 2p-4: no other value occurs, v_a + v_b = 3p-2, v_a, v_b >= p-1.
  A choice of i copies of a and j copies of b with i + j = 2p sums to 2p a + j(b - a) = j(b - a) (mod p), which vanishes iff p | j.
  j = 0 or 2p would need 2p copies of one value, impossible (each multiplicity is <= (3p-2) - (p-1) = 2p-1); j = p needs
  v_a, v_b >= p. By Step 1, min(v_a, v_b) = p-1 and the other is 2p-1.
Label so that X = a^(2p-1) b^(p-1) with a != b.

Step 3 (one arc pattern forces b = -a). Fix any two distinct blocks j != j' and the arc A := runs j+1, ..., j' (cyclically), a
nonempty proper set of runs. Let z := -1 on the runs of A and +1 on the other runs. The sign changes exactly at blocks j and j'
(f_j = f_(j') = 1, all other f_i = 0), so Phi = 2; delta = #{i : f_i = 0} = p-2 (all l_i = 1); C_max = F - delta = 2; hence C = 2
and 2p-C = 2p-2 <= R. Telescoping over the runs outside A gives T(z) = y_(j') - y_j =: tau0. By GRX (the ARC form at H^ = 0),
w^ has an identity 2p-subword as soon as some 2p-2 rotation letters have signed value sum tau0 (mod p), sign + outside A and - inside.
Let alpha_+ and alpha_- (beta_+ and beta_-) count the letters of value a (value b) outside and inside A: alpha_+ + alpha_- = 2p-1,
beta_+ + beta_- = p-1, and D := a(alpha_+ - alpha_-) + b(beta_+ - beta_-). Since alpha_+ + alpha_- = 2p-1, one of them is >= p.
(i) alpha_- >= p. For integers 0 <= y <= beta_+ and 0 <= z' <= beta_-, put om := p - y - z' (so 1 <= om <= p <= alpha_-) and select:
    all alpha_+ letters of value a outside A; alpha_- - om letters of value a inside A; beta_+ - y letters of value b outside A;
    beta_- - z' letters of value b inside A. These are 3p-2-om-y-z' = 2p-2 actual letters, with signed value sum
      a alpha_+ - a(alpha_- - om) + b(beta_+ - y) - b(beta_- - z') = D + a om - b y + b z' = D - (a+b) y - (a-b) z'  (mod p).
(ii) alpha_+ >= p. Symmetrically, with 0 <= y <= beta_-, 0 <= z' <= beta_+ and om := p - y - z' <= alpha_+: select all alpha_-
    letters of value a inside A, alpha_+ - om of value a outside, beta_- - y of value b inside, beta_+ - z' of value b outside:
    2p-2 letters with signed value sum D - a om + b y - b z' = D + (a+b) y + (a-b) z' (mod p).
Suppose a + b != 0 (mod p). In case (i) let B1 := {(a+b) y : 0 <= y <= beta_+} and B2 := {(a-b) z' : 0 <= z' <= beta_-}; in case
(ii) the same with the ranges beta_-, beta_+. The coefficients a+b and a-b are nonzero (a != b) and each range has at most
p-1+1 = p terms, so |B1| = (range length) and |B2| = (range length) exactly, and by CD
  |B1 + B2| >= min(p, (beta_+ + 1) + (beta_- + 1) - 1) = min(p, p) = p,
i.e. B1 + B2 = Z_p (if one range is {0}, the other already has p elements). Choose y, z' with
(a+b) y + (a-b) z' = D - tau0 (case (i)) or = tau0 - D (case (ii)); the corresponding selection has signed value sum tau0, so
w^ has an identity 2p-subword, contradicting avoidance. Hence a + b = 0 (mod p), i.e. b = -a; and a != b gives 2a != 0, so
a != 0.

Conclusion. X = a^(2p-1) (-a)^(p-1) with a != 0: every rotation letter of w^, hence of w (same rotation multiset), is rho_a or
rho_(-a), and the multiset is rho_c^(2p-1) rho_(-c)^(p-1) with c := a. []

## 4. Checks recorded for review

- Only one arc is needed, and any j != j' works; the reflection values y_i enter only through tau0, which the sumset covers.
- In the rigid case b = -a the set B1 collapses to {0}, so B1 + B2 = B2 has (range length) elements; it is all of Z_p only when the
  side of A holding at least p letters of value a also holds all p-1 letters of value b = -a. Then the same selection contradicts
  avoidance; otherwise this argument gives no contradiction. No existence or non-existence of such avoiders is claimed.
- Every selection is of actual letters: counts are between 0 and the available multiplicities (om <= p <= alpha_- resp. alpha_+,
  y <= beta_+ or beta_-, z' <= beta_- or beta_+), and exactly 2 reflections (S_j, S_(j')) are selected, as GRX's C = 2 prescribes.
- Relation to accepted results (context, not premises): ROT-KP covers k = p with kappa^ in {0,1}; ROT-KP+ covers k = p, kappa^ >= 1
  with (S1) at kappa^; at kappa^ = p-1, (S1) can fail at sequence level (g^(2p-1)(3g)^(p-1)), so this theorem is the word-level
  substitute for that endpoint. Combining it with any o_F = p assembly is a separate obligation (pending ASSEMBLY-LS and
  ONE-SHORT-LS acceptance); no such combination is claimed here.
- Imports and authorities (whole-file sha256): proof-ROT-few-E-v4.md ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f;
  notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; proof-ROT-KP-v1.md
  472e43cf6c2652ecbc68704dea99fc84263ea241ef3a3147feb51902c43a800e; proof-LSplus-e2-v1.md
  2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1; verdicts olson-rotation-lowodd-parent-verdict-v2.md
  0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 (item 1, line 7; M1 line 29; M4 line 32),
  olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af (overlays 1-3, lines 51-53),
  olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a (line 12),
  olson-rotkp-parent-verdict-v1.md dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3 (ARC, line 25),
  olson-STAB-delta-parent-verdict-v1.md ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 (CT, item 6, line 23).
- Trust: written proof relative to the accepted inputs above and the classical Cauchy-Davenport theorem; no computation is a premise
  and no cited input rests on a computer-assisted step. Not claimed: reflection rigidity, INV*, any o_F = p assembly, ordered Olson,
  p = 5, novelty, priority, Lean or human review.
