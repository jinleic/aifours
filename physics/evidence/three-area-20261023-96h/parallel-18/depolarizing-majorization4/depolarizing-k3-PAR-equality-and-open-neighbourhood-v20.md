# Actual k3 continuation v20 — equality in PAR, a genuine open neighbourhood, and a sharper robust bound

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 05:53:16 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN CANDIDATE, NOT parent-adopted, NOT global closure.** Exact source-symbolic WRITTEN reasoning, including privately; no numerical parameter instances/scouts, decimals, interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO. All old sources stay immutable. The additive `v14-F3-final-clause-withdrawal-and-v19-citation-qualification-v1.md` (SHA256 `6248abd1b20b73f7a8c38442aece2392c5fb4112b68c5c83ffe154c6d214e993`) is mandatory: false FINAL F3 remains WITHDRAWN, and SEC/channel-vs-U3/global-optimizer/degenerate-first-order qualifications all remain.

Named interfaces: parent `depol-v12-v19-entire-families-and-F3-refutation-parent-v1.md`, SHA256 `05dd4952211ba4b4f223cba81483af65b5cf0716feb4b4ae16a998018424d036`, supplies exact WRITTEN-supported v18 PAR, v15 NP, universal Z<=4I and v13 all-p k3 transfer. Actual entire v18 was read in this resumption; its Kraus/parity/physical-max-pair construction is retained. This proof does NOT use the withdrawn checkpoint073 first-order aside, SEC division at poles, physical complex-SVD covariance, an alleged C4 global optimizer or unprovided historical certificates.

## 1. Statements and notation

For EVERY pure parity eigenstate phi, and EVERY physical LU image thereof,

    K3(X3(phi))=6 IFF phi is a PRODUCT state.                  (EQ-PAR)

In particular every NONPRODUCT member of the full PAR family has STRICT margin, including complex/zero-amplitude/degenerate cases. This yields a genuine open neighbourhood of the ENTIRE compact PAR pure-state family on which U3(3) holds, not merely an excess bound. No numerical radius or global theorem is asserted.

Separately, for ANY two density matrices rho,sigma,

    |K3(X3(rho))-K3(X3(sigma))| <=4 ||rho-sigma||_1.            (L4)

For pure psi and M=max_P |<psi|P|psi>|, where P ranges over all product-Pauli-axis involutions,

    K3(X3(psi)) <=6+4 sqrt(1-M^2).                            (RP4)

This improves the old coefficient8 without a derivative claim. The ORIGINAL arbitrary-state k3/CLIP-prime/quartic gap remains outside the stated regions; the neighbourhood is an added sufficient region, not a positive-cutoff substitute.

Odd parity reduces to even by an actual single-site X. In the even case use v18's SAME maximal-mass antipodal pair in BOTH blocks. Set p_x=|phi_x|^2, s=(sqrt(p_x)), m_k=p_x+p_xbar, m=max m_k, S=1-m. Let

    M0=sum_k w_k w_k^T, w_k=(sqrt(p_x),-sqrt(p_xbar))

on each disjoint pair, taking w_k=0 for zero mass. Thus M0>=0, TrM0=1, ||M0||=m and

    X_e ~2H, H=ss^T+M0, ||s||=1, TrX_e=4.

NO normalization by m_k is used here. After actual even site flips taking a maximal pair to0000/1111, write phi=a|0000>+sum c_ij|ij>+f|1111>, |a|^2+|f|^2=m, sum|c_ij|^2=S. Actual complex symmetric zero-diagonal matrices A_ji=c_ij and Atilde_li=c_([4]\{i,l}) give

    X_o=Xi Xi^*+Theta Theta^*, Xi=[aI;Atilde], Theta=[A;fI].

Parent PAR supplies X_o<=2I, K2(X_o)<=4-2m and ||X_e||<=2+2m. The rank-three allocations are exactly K_j(X_e)+K_(3-j)(X_o), j=0,1,2,3. We examine ALL four, not just the allocation that controlled the non-strict theorem.

## 2. A new elementary norm bound for the ACTUAL symmetric zero-diagonal matrices

**Lemma ZD.** For a complex symmetric zero-diagonal4x4 matrix A, with S=sum_(i<j)|A_ij|^2,

    ||A||^2 <=(3/2) S.                                      (ZD)

Proof. For arbitrary complex unit x,y, put t=sum_i |x_i|^2|y_i|^2. Pairing symmetric entries and applying Cauchy gives

    |x^* A y|^2
      <=S sum_(i<j)|conj(x_i)y_j+conj(x_j)y_i|^2
       =S[1+|sum_i x_i y_i|^2-2t].

The bilinear inner term is at most1 by Cauchy, and at most4t by Cauchy on its FOUR summands. Hence the bracket is at most `1+min(1,4t)-2t`, which is <=3/2 for BOTH t<=1/4 and t>=1/4. Taking the supremum over x,y proves ZD. This is not a physical basis change/Takagi/SVD covariance assumption. The two proof intervals are a quantified symbolic inequality split, not parameter probing.

Apply ZD to BOTH A and Atilde, whose S is identical. Actual Xi/Theta Gram matrices give

    ||X_o|| <= |a|^2+||Atilde||^2+|f|^2+||A||^2
             <=m+3S=3-2m,

so `||X_o||<=min(2,3-2m)`. Also Ky Fan subadditivity and trace give

    K2(X_e)<=min(4,2+4m).                                   (A2)

These inequalities retain complex phases and the SAME maximal pair.

## 3. The TWO-even/ONE-odd allocation is ALWAYS STRICT below6

If m<1/2, A2 plus ||X_o||<=2 gives a bound4+4m<6. If m>1/2, TrX_e=4 plus ||X_o||<=3-2m gives7-2m<6. Only the quantified equality stratum m=1/2 remains; it is not an instantiated numerical test.

At that stratum, equality6 would require K2(X_e)=4 AND ||X_o||=2. The first condition and TrX_e=4 force rankH<=2. Since H=M0+ss^T is a sum of PSD matrices, rankM0<=2 and s lies in ranM0. At least two antipodal masses are needed because m=1/2; therefore there are EXACTLY two nonzero pairs, both of mass m. On each pair, s can lie in the line spanned by w_k ONLY if one of its two probabilities vanishes. After the actual flips above, phi has exactly the two amplitudes a|0000>+c|ij>, f=0, with ONE nonzero edge c.

For this actual one-edge A, and the complementary one-edge Atilde, the operator norm squared is S (not the relaxed3S/2). Therefore

    ||X_o|| <=m+2S=2-m<2,

contradicting equality. Hence the two-even/one-odd allocation is strictly below6 in EVERY case, including all cutoff degeneracies. The three-even and zero-even allocations are at most4 by the block traces and are already strict below6.

## 4. Equality in the ONE-even/TWO-odd allocation forces a product

The parent PAR sum is `(2+2m)+(4-2m)=6`. Equality requires BOTH bounds to be sharp. First

    lambda1(H)=1+m IFF M0 s=m s.                             (WEQ)

Indeed every unit x has x^*Hx<=|s^*x|^2+m<=1+m. Equality forces x proportional to s and M0s=ms; the converse is immediate. This is division-free and does not pass through a secular pole.

On any nonzero antipodal pair, WEQ implies one probability vanishes and its mass is m: if both probabilities were positive, the signs of w_k make M0s=ms impossible. Thus all ACTIVE pairs are ONE-SIDED with the SAME mass m. If only one is active, phi is a computational product vector and K3=6 directly.

Suppose instead at least two are active. After taking an occupied maximum-pair string to0000 by physical even flips, a!=0,f=0,S>0. If K2(X_o)=4-2m, equality is necessary in BOTH stages

    K2(XiXi^*+ThetaTheta^*)
      <=K2(XiXi^*)+K2(ThetaTheta^*)
       =2|a|^2+K2(Atilde^*Atilde)+K2(A^*A)
      <=2m+2S+2S=4-2m.

A nonzero complex symmetric zero-diagonal matrix has rank>=2: a rank-one symmetric matrix is a scalar ww^T, whose zero diagonal would force w=0. Since S>0, both A and Atilde are nonzero. Trace equality in the last line therefore forces rankA=rankAtilde=2.

Now Theta=[A;0] has rank2, and its UNIQUE maximizing rank-two projector is onto `V_Theta={(z,0):z in ranA}` in the upper sector. Xi^*Xi=|a|^2 I+Atilde^*Atilde has TWO eigenvalues STRICTLY above |a|^2 and its next two equal |a|^2. Thus XiXi^* has a UNIQUE top-two subspace

    V_Xi={ (a u,Atilde u):u in ran(Atilde^*) }.

Atilde is injective on ran(Atilde^*), so V_Xi has ZERO intersection with the upper-only sector. It cannot equal V_Theta. Equality in Ky Fan subadditivity would require ONE rank-two projector maximizing BOTH summands: take a maximizer of their sum and compare its two traces to the separate maxima. No such projector exists here. Thus subadditivity is STRICT, contradicting K2(X_o)=4-2m.

Consequently the one-even/two-odd allocation can reach6 ONLY for a single active one-sided pair, i.e. a computational product vector. The other allocations were all strict. Physical LU covariance proves EQ-PAR for the ENTIRE PAR pure-state set. Arbitrary complex phases, zero masses, and spectral degeneracies were retained; no differentiability or optimizer uniqueness of the FULL rank-three problem was assumed.

## 5. L4 and the explicit local strict-margin tube

The linear map X3 is completely positive and TrX3(Y)=8TrY; hence X3/8 is trace-preserving positive. For Hermitian Delta, its positive/negative decomposition proves `||X3(Delta)||_1<=8||Delta||_1`. If Delta=rho-sigma, its trace is0 and so is X3(Delta). Every projector Pi then obeys

    |Tr Pi X3(Delta)|<=Tr[X3(Delta)]_+=||X3(Delta)||_1/2.

Taking the two Ky Fan variational maxima proves L4. This factor1/2 is legitimate because the SAME two inputs have the SAME trace, not positive-part Loewner monotonicity.

For any fixed NONPRODUCT PAR state phi define the EXACT spectral margin `mu(phi)=6-K3(X3(phi))>0`. L4 gives the explicit sufficient condition

    ||rho_psi-rho_phi||_1 <=mu(phi)/4  => K3(X3(psi))<=6.       (TUBE_phi)

Equivalently for pure inputs the left side is `2sqrt(1-|<psi|phi>|^2)`. This certificate concerns arbitrary nearby pure directions, not just parity-preserving ones. The margin is an exact spectral function, not an evaluated numerical eigenvalue or a uniform first-order expansion.

For any product-Pauli involution P, rho_D=(rho+P rho P)/2 is a convex mixture of its parity-eigenstate blocks, so parent PAR and convexity give K3(X3(rho_D))<=6. For pure rho,

    ||rho-rho_D||_1=sqrt(1-|<psi|P|psi>|^2).

L4 and compact maximization over the product axes prove RP4. Therefore a genuine U3 excess kappa=K3-6>0 implies `sqrt(1-M^2)>=kappa/4` (a weak >=, not an unproved strict inequality). This sharpened robust bound is independent of the false first-order aside and does NOT by itself establish a neighbourhood when its base margin is0.

## 6. A genuine open neighbourhood of the ENTIRE PAR set, with products handled by NP

Let P be the compact set of pure PAR densities up to physical local unitaries. It is the continuous image of the compact parity unit spheres and compact physical local-unitary group. Product states are a compact subset. Maximal product overlap G is continuous, being the maximum of a continuous function over the compact product-state set.

The parent-supported NP theorem gives U3 on `G>=124/125`, including an OPEN neighbourhood `G>124/125` of EVERY product state. EQ-PAR gives strict K3<6 for EVERY nonproduct member of P. Thus

    O={pure rho:G(rho)>124/125} UNION {pure rho:K3(X3(rho))<6}

is an OPEN set containing ALL of P, and U3 holds throughout O. By compactness there exists r_*>0 such that `dist_1(rho,P)<r_*` implies rho in O: if the complement is nonempty, minimize the continuous distance on the two disjoint compact sets; otherwise the assertion is immediate. This is an EXISTENCE theorem for a positive uniform tube, not an assessed numeric radius or a claim that O exhausts all pure states.

This construction bypasses the cutoff-degenerate derivative issue completely: use strict finite margins away from products, and the independently supported NP neighbourhood at products. It neither asserts every maximizing projector is block diagonal nor Taylor-expands through a degeneracy. Every genuine U3 violator is therefore outside this actual uniform PAR tube, in addition to the earlier exact restrictions. The unrestricted original quantifiers remain the task; no chosen positive cutoff replaces them.

## 7. Original channel application and exact remaining gap

Every state in the stated tubes and open neighbourhood has U3(3). At the named parent-supported v13 SAME-projector coefficient bounds1/6/12/10, exact channel expansion and full spin-flip interface, the ORIGINAL k3 comparison follows for ALL physical p. Fixed-projector linearity/convexity then covers their actual convex hull and LU/permutation images. This is not an unrestricted all-index theorem, finite-certificate replay or all-state result.

The arbitrary-state global U3(3), full-B CLIP-prime and common-projector quartic remain OPEN outside the precise sufficient sets. The channel-only `a>9d` condition is NOT imposed on mere U3 coefficient violators. No negative original box/state/projector/noise point is supplied; FINAL F3's stronger4 remains refuted. Old source/checkpoint bytes and every prior cadence/exactness/privateapproxZERO/pause/inventory/orientation/read-order/freeze/clock/admission finding remain. No stronger formal/kernel/human/configured-family/cross-vendor/executable/novelty adoption is claimed. Same18/HOLD/OWN root/October27 science cutoff11:05:38/deadline12:35:38 PDT. Active original-task continuation, NOT a park or round closeout.
