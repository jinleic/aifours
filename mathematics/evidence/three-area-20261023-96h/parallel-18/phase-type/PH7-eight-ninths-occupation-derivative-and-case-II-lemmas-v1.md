# PH7 at 8/9: occupation-derivative form, Case-II Gale/exit lemmas, and the zero-variance threshold

The actual `/bin/date` returned before this manuscript was **Sun Oct 25 22:19:43 PDT 2026**. Owner MathResearch96h-2, math-1.

Status: AUTHOR-WRITTEN CANDIDATE, exact necessary statements only. There is NO witness and NO exclusion at 8/9; the minimum stays in {7,8}.

No interpreter, eval, calculator, CAS, enumeration, solver or replay was used. Every claim below is exact written algebra or a rational-point sign evaluation done by hand. Earlier private approximate decimal explorations are disclosed in checkpoints 056/057. They carry ZERO credit and are used nowhere here.

Imports and notation follow `PH7-eight-ninths-companion-polytope-reformulation-v1.md` (SHA256 `5582e9747b0380e01fb5c928def88f4efb7a391aeaf21d48b4736cf2c5686b58`), called CP below. That includes B6, the SCC/Perron-coordinate theorem, and companion coordinates: x is identified with p_x(y)=x_0+x_1y+x_2y²+x_3y³, chi(y)=(y²+2y+s)², s=1+z, and A0=K/s².

## 1. Occupation-derivative form (Case I)

**Lemma 1.** In Case I, every state j satisfies EXACTLY

    psi~_j(tau) = l_j + p_j(D)F(tau)/A0
                = l_j + (x_0j F + x_1j F' + x_2j F'' + x_3j F''')/A0,

with l_j = 1 − x_0j.

*Proof.* By (OCC) of CP, L[psi~_j] = l_j/y + s²p_j/(y chi). Also L[F/A0] = s²/D_z. Since F^(m)(0)=0 for m<=3, L[F^(k)] = y^k L[F] for k<=4. ∎

**Consequences (exact).**

- The exit state is psi~_e = F/A0.
- For the unique distance-3 state o, psi~_o = (F + F'/t)/A0. So psi~_o>=0 iff e^(t tau)F(tau) is nondecreasing on [0,∞). Equivalently, t >= t_min(z) := sup_(tau>0)(−F'(tau)/F(tau)). Here t is the holding rate of e (CP §5). This is a necessary bound on the actual exit holding, not a free parameter.
- Let a single D2 state m be the only D2 predecessor of o, with no e→o edge (mu=0). Then CP §6 gives p_m=(1+y/t)(1+y t b). So psi~_m=(1+D/t)(1+tbD)F/A0, a product of two first-order smoothing operators on F.
- In general, the lambda-average of the D2 polynomials is EXACTLY

      1 + [1/t + (1+mu/t)/Lambda] y + y²/(t Lambda),

  where Lambda = sum_(j∈D2) lambda_j. Hence its y-coefficient exceeds 1/t + t·(its y²-coefficient) by exactly mu·(its y²-coefficient)>=0. Its discriminant is therefore >=0, so this average has two real negative roots.

## 2. Case II: Gale face lemma and exit-line lemma

Case II is defined in CP §7. There Pi is a c-fold pyramid over Delta_(a−1) ⊕ Delta_(b−1), with Gale classes A (z>0), B (z<0) and apexes (z=0).

**Lemma 2 (Gale face).** The non-initial set N is the face of Pi exposed by l(x,w)=1−x_0+w. Faces of pyr^c(Delta⊕Delta') are joins of an apex subset with either a proper face of the free sum, or the whole base when some apex is excluded. Faces of the free sum are exactly the sets missing a vertex of A and a vertex of B. Hence EITHER

- I meets both A and B (so |I|>=2), OR
- I consists only of apex vertices (z_j=0), and N contains all of A∪B.

**Lemma 3 (exit line).** Write psi~_v = 1 + osc_v + w e^(−q tau). Then psi~_v^(m)(0) = −x_0(C^m x) + (−q)^m w. Vanishing at orders 0,1,2,3 is equivalent to

    x_0 = 1 + w,
    x_3 = q w/c0,
    x_2 = (c3 q − q²) w/c0,
    x_1 = c3 x_2 − (c3² − c2) x_3 + q³ w/c0.

So every state at distance >=4 lies on ONE line through (e_0,0), parametrized by w. Three collinear points cannot all be vertices, so at most two states lie on that line.

Each psi~_j>=0. F vanishes to order exactly 4, so the minimal-order argument puts every exit at distance >=4. Since F has no e^(−q tau) part, (e_0,0) is the theta-weighted mean of the exits. So Case II has EITHER

- one exit, at (e_0,0); OR
- two exits on that line, with opposite signs of w.

## 3. Exact zero-variance threshold for all z (complements STRICTVAR)

Assume all holding rates are equal, i.e. A=0 in the notation of `PH7-eight-ninths-unrestricted-strict-Perron-and-regeneration-v1.md`. The same trace algebra at general z gives:

    q = q0(p) := (3p² − 4p + 6 − 14z)/7,
    DISK: p² − 4p + 3 − 7z < 0,
    tr B³ = (3/49) Phi_z(p),
    Phi_z(p) = 5p³ − 24p² + 58p − 44 + 98z(2 − p).

Two checks:

- At z=8/9, 9·Phi_z = 45p³ − 216p² − 262p + 1172, which is the packet's F.
- Each tr B^k>=0, and tr B³ = 3·(3-cycle weight)>=0.

**Proposition 4.** Let p* be the real root of 8p³ − 23p² + 20p − 20 in (9/4, 23/10). Exact signs:

    f(9/4) = −5/16,
    f(23/10) = 1666/1000.

Let z0* = (3p*² − 4p* + 6)/14. Then the zero-variance system {q0>0, DISK, Phi_z>=0} has a solution p only if z < z0*. Moreover 195/224 < z0* < 8/9.

*Proof.* q0>0 means z < zq(p) := (3p² − 4p + 6)/14. For p>2, Phi_z(p)>=0 means z <= zPhi(p), where

    zPhi(p) = [(5p² − 14p + 30) + 16/(p−2)]/98

by exact division. Its derivative is (10p − 14 − 16/(p−2)²)/98. That is negative for 2<p<=23/10, because 16/(p−2)²>=16/(3/10)²=1600/9 > 10p−14. Also zq is increasing for p>2/3.

zPhi(p) = zq(p) reduces EXACTLY to 8p³ − 23p² + 20p − 20 = 0. On the relevant branch, the binding constraint is zq for p<p* and zPhi for p>p*. So max_p min(zq, zPhi) = zq(p*) = z0*.

For p>23/10, zPhi stays below zq. Indeed zq − zPhi has the sign of (p−2)(21p² − 28p + 42 − 5p² + 14p − 30) − 16, which is positive there. So no other p can do better.

Monotonicity of zq gives z0* > zq(9/4) = 195/224. z0* < 8/9 is the STRICTVAR fact: at z=8/9 the zero-variance system is empty. At p* the DISK holds strictly, because p*² − 4p* + 3 < 0 < 7z0*. ∎

So the zero-variance mechanism (equal holdings and no 2-cycles; the B6 endpoint type at n=6) can occur ONLY strictly below z0*<8/9. Every PH7 with z>=z0* must have strictly positive holding/2-cycle variance. This is a spectrum-only bound. It is NOT a realizability statement for any z, and NOT an 8/9 decision.

## 4. Two structural facts used later

**Cycle lemma.** A pure n-cycle CTMC has only simple nonreal eigenvalues. The reason: Im sum_j 1/(y+mu_j) = −Im(y)·sum 1/|y+mu_j|² ≠ 0. So the forced Jordan block at y0 (CP §8) needs branching. This is a consistency fact only.

**Simplex/Gale duality.** The 7 states form an invariant 6-simplex in visible R⁴ ⊕ hidden R² for C⊕H. Pi is its visible projection. The scaled Gale points g~_j = gbar_j/r_j satisfy M* g~_i = sum_j G~_ij (g~_j − g~_i), where G~ = R^(−1)G^R is the row-sum-zero PH-direction chain. So the hidden configuration is invariant under the hidden 2×2 flow. It fixes the combinatorial type of Pi through Gale duality.

## 5. Status

These are necessary conditions and an exact sub-mechanism threshold. They narrow Case II, the exit structure and the zero-variance regime. The original 8/9 question is still open: the minimum is in {7,8}. No formal, kernel, cross-vendor or novelty acceptance is claimed. HOLD, root, cutoff and deadline are unchanged.
