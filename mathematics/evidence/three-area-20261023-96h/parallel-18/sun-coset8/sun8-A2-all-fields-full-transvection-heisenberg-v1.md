# Sun8 — COMPLETE A2 all fields, actual full transvections and Heisenberg Sylow detection

Owner MathSun8-2. Actual preceding `/bin/date`: **Sun Oct 25 18:17:25 PDT 2026**. **NEW COMPLETE WRITTEN CANDIDATE, NOT ACCEPTED.** Original eight-coset target, not an abstract cell arrangement. This body is mathematically independent of the new A1/PSL2/SL2/PGL2 conclusions; it reconstructs its own new load-bearing lemmas and finite q2 base. No P7/Sun7/R8/least-order/minimum-sum/normalizer-rank/private-factor/centre-saturation ansatz.

Permanent OWN cadence PROCESS MAJOR057(16:58:10→17:31:20 observed33m10s, no intervening required JSON), earlier047metadata-polling lapse, M1class<=2/abelian alternative, all old source/finding histories and v9/v10/v11/HOLD remain. No cure/backdating/clean-runtime census. No scientific interpreter/Eval/calculator/program/CAS/enumeration/symbolic/solver/replay/CLI/nestedagent/newGO.

## 1. Exact theorem, original quantifiers and named boundaries

> **A2-SUN8:** for EVERY finite field F_q, original Sun8 holds in EACH of SL3(q), PSL3(q), PGL3(q): EIGHT pairwise-disjoint nonempty LEFT cosets of ARBITRARY actual subgroups have a pair of FULL ORIGINAL subgroup indices with gcd≥8.

For SL3/PSL3 and q≥3 the proof below has NO research-sized input beyond the written elementary group/field/linear arguments provided. The q2 base uses ONLY exact **NC7**: six disjoint left index7 cosets in ANY group have one left index7 coset as their complete complement. Current181LF NC7 source is `sun8-global-kernel-section-complete-v1-part2.md`, SHA `2c8949dfa512ca3d89549b04d42bea9be8a515081cb3a3ba7762dd3b2e7b46e8`, at its named A7/Eisenstein boundary. This is not global Sun7.

PGL3 uses in addition only classical **SUN3** for its possible normal index3 source: three disjoint finite-index left cosets in ANY group force some index gcd≥3. Exact statement was actually read in Zhu [0807.2207v1 Theorem1.1](https://arxiv.org/html/0807.2207v1), reader LF1–300of521; remaining proof body NOT newly read/reconstructed here. Named ordinary-written classical input, not a new full source audit. No SUN4/CFSG/Dickson/minimum-index/Jordan/Bertrand/source program is needed for this A2 theorem. Neither the old global-kernel/rank-four results nor new A1 conclusions are correctness premises.

## 2. Exact elementary-matrix conventions

Write T(v,phi)={1+t*v*phi:t in F_q} for v≠0,phi≠0,phi(v)=0. It is an ACTUAL full field-parameter transvection group, not one cyclic p-subgroup or an F_p fragment. Its elements have determinant1 and its axis is the F_q-line<v>, fixed hyperplane kerphi. Rescaling v/phi changes only the parameter, not this full group.

The full elementary groups E_ij(t)=1+t*e_i*e_j^* generate SL_n(q) for n2/3 used here: row additions reduce an invertible matrix, with a two-row pivot swap available from

u(a) l(-a^(-1)) u(a) = [[0,a],[-a^(-1),0]] = w(a),

and w(a)w(-1)=diag(a,a^(-1)). Thus determinant-one diagonal factors lie in generated SL2 blocks. For n3, diag(a,b,(ab)^(-1)) is diag(a,a^(-1),1)*diag(1,ab,(ab)^(-1)); Gaussian row reduction then gives every determinant1 matrix. These are exact algebraic identities, not executed programs.

If two full transvection groups T(v,phi),T(w,psi) have phi(w)≠0 and psi(v)=0, their rank-one matrices A=v*phi,B=w*psi satisfy BA=0,A²=B²=0,AB=phi(w)*v*psi and all higher products vanish. Hence

[1+sA,1+tB]=1+st*phi(w)*v*psi.                         (ONEWAY)

So H containing both groups contains FULL T(v,psi), as well as T(w,psi). Their independent axes v,w span kerpsi in dimension3; their commuting products are the ENTIRE actual plane radical

R_psi={1+x*psi : x in kerpsi}, |R_psi|=q².              (RADICAL)

No abstract linear combination is being declared an element: (1+a*v*psi)(1+b*w*psi)=1+(a*v+b*w)*psi, so every element is an explicit product in H.

## 3. FULL-TRANSVECTION lemma, complete irreducible three-dimensional proof

**T3.** If H<=GL3(q) acts irreducibly over F_q and contains ONE full T(v,phi), then H contains SL3(q).

First, if H contains one full R_psi, irreducibility of its dual action implies that the H-orbit of psi spans V*. Choose THREE linearly independent conjugate covectors psi1/2/3. H contains the full conjugate radicals R_psii. In their dual basis those radicals contain EVERY E_ji(t), j≠i, t in F_q. Thus H contains all six elementary groups and SL3(q). Dual irreducibility follows directly: a proper nonzero invariant dual space would have a proper nonzero invariant annihilator in V. This establishes the actual-radical lift, not an unproved field-span closure of group elements.

Now consider all full transvection groups contained in H; this set is H-stable and its axes span V, since it includes the H-orbit of the first axis. Choose another T(w,psi) with phi(w)≠0. If psi(v)=0, (ONEWAY) gives a full radical and the preceding paragraph settles T3.

Otherwise phi(w)*psi(v)≠0. Put W=<v,w> and L=kerphi cap kerpsi. The two covectors are independent on W, so V=W directsum L. The two full root groups act as the full opposite unipotent roots of SL2(q) on W and fix L pointwise. The exact §2 generation therefore places the WHOLE block SL2(W) in H. In particular it contains a full transvection at EVERY axis line in W, with covector annihilating that line and L.

Choose a third full T(x,chi) with x outside W(axes span V). Write x=xW+a*l for l spanning L,a≠0. If xW=0, then chi(l)=0, so some y in W has chi(y)≠0. The block-root at y has covector zero on x, whereas chi(y)≠0. This is (ONEWAY) with the roles reversed; a full radical follows.

If xW≠0, let theta annihilate xW and L; the block-root T(xW,theta) is in H and theta(x)=0. If chi(xW)≠0 we again have (ONEWAY). If chi(xW)=0, then chi(x)=0 forces chi(l)=0. Thus chi is a nonzero scalar multiple of theta, and H contains FULL T(xW,chi). Its axis and x are independent and both lie in kerchi. Together T(xW,chi),T(x,chi) give the entire R_chi by explicit commuting products. All cases yield a full radical and therefore SL3(q). This includes q2/characteristic2; there is no excluded orthogonal, unitary, subfield, form or small-field case. Such groups can contain only partial field-parameter roots unless reducible, as the actual argument shows.

## 4. Heisenberg index<=q detector, including the equality boundary

Let U=UT3(q), orderq³, with coordinates(x,y,z) and law

(x,y,z)*(x',y',z')=(x+x',y+y',z+z'+x*y').

Its centre Z_U={(0,0,z)} is the FULL E13(q) root, and U/Z_U is F_q² additive. For ANY P<=U with [U:P]<=q, we prove Z_U<=P; no assumption P normal or F_q-linear is inserted.

Put C=P cap Z_U, c=dim_Fp C, and A=PZ_U/Z_U<=F_q², an F_p-space. If C is proper, c<=f−1. Choose a nonzero F_p-linear functional lambda:F_q->F_p vanishing on C. The pairing

omega_lambda((x,y),(x',y'))=lambda(x*y'−x'*y)

is alternating and NONDEGENERATE on the2f-dimensional F_p-space: for x≠0 choose x'0 and y' so lambda(x*y')≠0; for x0,y≠0 choose y'0 and x' analogously. Such choices exist because multiplication by a nonzero field element is bijective and lambda nonzero. Every bracket of lifts in P lies in C, so A is isotropic for omega_lambda. Therefore dim_Fp A<=f: nondegeneracy gives dim A+dim A_perp=2f and A<=A_perp.

But |P|=p^(c+dim A)<=p^(2f−1)<q², contradicting [U:P]<=q and |U|q³. Hence C=Z_U. Crucially this works at EQUALITY [U:P]=q, not only a<f; it is what covers q3/4/5/7 without omitted finite cases. The central-root commutator and the isotropic dimension argument hold in characteristic2 as well.

## 5. Every proper large-Sylow subgroup is actually parabolic-contained

Let G=SL3(q), and H proper of actual index I with a=v_p(I)<=f. The ambient order is q³(q³−1)(q²−1), so U is a Sylow p-subgroup. Conjugate a Sylow p-subgroup of H into U, obtaining P with [U:P]=p^a<=q. Section4 gives full E13(q) inside H. If H were irreducible, T3 would put WHOLE SL3(q) inside H, contradiction. Thus H stabilizes an ACTUAL nonzero proper F_q-subspace, dimension1 or2.

The stabilizers of such points and planes both have actual index

S=q²+q+1.                                               (PARABOLIC)

For points this counts nonzero vectors modulo F_q^*; for planes apply the dual count. SL3 is transitive on each: a chosen linear map between subspaces can have its determinant corrected by scaling a complementary basis vector. Hence S divides I for EVERY proper H with v_p(I)<=f. Independent subgroup conjugations here only prove index DIVISIBILITY for each original H; no original coset is moved or separately lifted in the final family.

## 6. Original Sun8 for SL3(q) and PSL3(q), ALL q>=3

Suppose eight disjoint original cosets have all pairwise index gcds<=7. Each subgroup is proper. Define b by p^b<=7<p^(b+1). At most ONE original index is divisible by p^(b+1), otherwise their gcd>7. For q>=3 we have f>=b: p2 gives f>=2=b, p3/5/7 gives b1<=f, and p>7 gives b0. Thus at least SEVEN original indices satisfy a<=b<=f, so all are multiples of S by §5. Since q>=3, S>=13>7, contradiction. Every hidden/original subgroup and full integer index is included in this uniform valuation argument; it is not an elementary-rank count or a hand-picked vertex family.

For PSL3(q), lift ALL eight cosets by the natural surjection SL3->PSL3. Each preimage is a full LEFT coset of the subgroup preimage, disjointness is preserved, and its index is exactly the ORIGINAL index. Applying the SL theorem gives the same pairwise bound. This is a legitimate full preimage lift, not an assumption that some original quotient coset is a saturated image.

## 7. PGL3(q), actual index-three exception and SUN3

For PGL3(q), put N=PSL3(q). Determinant modulo cubes gives [G:N]=d=gcd(3,q−1), so d1 or3. If d1, G=N and the preceding result applies. For d3 an actual source coset of N(index3) is impossible at SUN3: its normal quotient is C3, so any other subgroup not contained in N projects onto all C3 and its coset would meet that entire source fibre. ALL seven others lie in N and their full cosets in the TWO remaining N-fibres. At least four share one fibre; one common translation puts them inside N with indices I_j/3. Their inner pairwise gcds<=2, contradicting SUN3 on any three. No independently chosen fibre/cut or omitted original source.

Now take an original PGL3 subgroup H with a=v_p(I)<=f and lift it fully to Hhat<=GL3(q). The scalar kernel has orderq−1 prime to p, so its index and p-index valuation are still EXACTLY I,a. A Sylow subgroup P in U has indexp^a<=q, giving the full central root by §4. If Hhat is irreducible, T3 puts SL3 inside Hhat, hence N<=H. Proper H would be N(index3), already excluded in a counterexample. Therefore every remaining such H is reducible and contained in an ACTUAL point/plane stabilizer of indexS. The same seven-index argument gives a contradiction for q>=3. The scalar torus has not been assumed to be a faithful multiplier; only a genuine full GL preimage was used.

## 8. q2 base: full original proof in the168-order group, NC7 only

For q2 all three groups coincide with GL3(2)=SL3(2), of order(8−1)(8−2)(8−4)=168. Its action on seven nonzero vectors is faithful and two-transitive(ordered distinct vectors are independent and extend to bases). The group is perfect: all elementary E_ij(1) are commutators [E_ik(1),E_kj(1)] for the third index k, and those elementary groups generate G.

Here is a full simplicity argument, not an imported small-group isomorphism. A point stabilizer P0 has abelian normal radical A={1+e1*phi:phi(e1)=0}, order4. Its G-conjugates generate all elementary groups. A nontrivial normal K is transitive by faithful primitivity. Thus G=K*P0, and modulo K all conjugates of A have the same image because A normalP0. Those images generate G/K, making it abelian; perfectness forces K=G. Hence G is simple. No PSL2(7) identification or CFSG catalogue is used.

For a Sylow7 C, its generator acts irreducibly on F2³: a1/2-dimensional constituent cannot support order7 because7 divides neither2−1 nor2²−1. Thus F2[C] is the field F8, its centralizer in G has order7, and a normalizer conjugation can send a generator only to the three roots alpha,alpha²,alpha⁴ of its minimal polynomial. All three are realized by the F2-linear Frobenius of F8, so |N_G(C)|=21. This is an actual normalizer derivation, not an asserted finite certificate.

The proper7-free index divisors of168 are2,3,4,6,8,12,24. Indices2/3/4/6 are impossible: simplicity makes the corresponding coset action faithful, perfectness puts its image in A_m, and168 cannot divide m!/2 for m2/3/4/6(the case6 has no factor7). Index12 would give a subgroup of order14, whose Sylow7 is normal(n7 divides2 and is1 mod7); it would lie in the21-order normalizer, impossible by divisibility. Hence every7-free proper index is8 or24, a multiple of8, and at most one can occur in a gcd<=7 counterfamily.

At least seven original indices are7r_j with r_j|24. Their pairwise gcd<=7 makes the r_j pairwise coprime; at most two exceed1, since24 has only prime factors2/3. Thus at least five sources have index7. A7-free source has coprime index with each index7 source and cannot be disjoint, so no7-free source actually occurs. All eight are7r_j and at least SIX are index7. NC7 gives the ONE index7 complement coset of those six original sources. It contains the remaining two WHOLE original cosets; after ONE common translation their subgroups have relative indices the original coprime r_j. Coprime-index cosets always meet, contradiction.

For completeness, the elementary coprime fact used here: if indices a,b are coprime, [G:H cap K] is a multiple ofab and at mostab by the diagonal coset injection. Thus it equalsab, [H:H cap K]=b and HK=G; all left cosets of H and K meet. The same applies inside the actual complement subgroup. No unadmitted computation, finite-group database, source-preserving gap or global Sun7 remains hidden in this q2 step.

## 9. Composition, exact assurance and remaining original gap

Sections2–6 prove SL3/PSL3 for EVERY q>=3 without the q2 NC7 input; §8 closes q2 at named NC7. Section7 adds ONLY SUN3 for the possible PGL index3 source. Together they prove the full candidate A2-SUN8 stated in §1 for EVERY field, with ALL actual eight subgroup/coset/full-index/disjointness hypotheses. The full-transvection proof reconstructs the ACTUAL matrices/radicals/SL2 blocks and all incidence cases; the Heisenberg equality boundary a=f is essential, not waived. No rank bound is substituted for a count of involutions.

This whole body needs a fresh ENTIRE written reconstruction: T3 both incidence directions/all xW cases/full radical products/dual spanning, Heisenberg proper-C functional and equality boundary, all eight original valuation strata, genuine quotient/preimage lifts, normal index3 ALL-seven-source distribution, and the entire168-order base/normalizer/NC7. Old A1/R4/v99/global-kernel/source headlines do not accept it. No formal/kernel/human/configured-family/executable/novelty acceptance. Source-pinned written is not a trusted-family or full-DAG audit of imported SUN3/NC7.

Novelty/priority/SOTA remain UNCLEAR/UNPERFORMED; these may be known or routine, and the A1/A2 shared root methods are NOT six independent discovery counts. The original full target still includes ALL other finite groups, arbitrary normal/central/semilinear extensions, higher dimensions/types and the general actual mixed-alpha<=1/maximal/private-composite Sun8 barrier. No full Sun8/globalSun7/R8/tbound/8coset witness, no automatic normal-extension/composition-factor closure. Same18/fulltarget/root/cutoff/deadline/HOLD, permanent OWN057cadence MAJOR/earlier047/M1/history retained, no clean runtime census or scientific interpreter/Eval/calculator/program/CAS/enumeration/symbolic/solver/replay/CLI/nestedagent/GO. Primary continues at that exact original residual.
