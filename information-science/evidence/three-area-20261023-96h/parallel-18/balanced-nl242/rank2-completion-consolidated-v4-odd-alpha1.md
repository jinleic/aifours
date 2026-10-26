# Rank-two completion — uniform exclusion of the odd-occupancy alpha1 branch

Owner InfoBalancedNL242, info-6. Actual clock before this consolidated successor: `Sun Oct 25 08:31:25 PDT 2026`.

**NEW WRITTEN CANDIDATE, not yet independently reconstructed.** All new work here is written mathematics. No scientific eval/interpreter, arithmetic/enumeration program, symbolic program, certificate replay or solver was used; metadata/source tools only. HOLD and parent v9 remain binding. No formal, human, independent-model or novelty acceptance is claimed.

This successor attacks the entire live intrinsic class, not another Gold example. It proves a uniform full-completion obstruction for EVERY alpha1 placement with active |Hdelta|=4, including all odd-occupancy placements constructed in v3. It uses the SAME V, both Boolean spectra, canonical quadratic carry and exact ternary R closure throughout. **The entire (16,24) case is not closed:** the active-magnitude8/even-occupancy branch remains.

## 1. Current support, immutable sources and exact target

The parent-supported intrinsic base is `institute/runs/three-area-2026-10-23-96h/nl242-intrinsic-rminus-trades-parent-v1.md`, with its receipt, v9 and the separate NL242 parent wording overlay. The actual254-line review `mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/peer-review-nl242-v3-intrinsic-v1.md` has now been read completely. Its overall0F/0M/1m concerns only the corrected parent summary; new author v3 mathematics has0F/0M/0m at its stated scopes.

Retained author packets:

- `rank2-completion-consolidated-v2.md`, SHA-256 `82dbda5c851b99c7e6c855d861bdc374ce0b3d3713fd8b41a41310dd78a91fa2`;
- `rank2-completion-consolidated-v3-intrinsic.md`, SHA-256 `4847a5674def5f279e4b564898975b40fa27920f827287059bbb1a5e40bbdc2d`;
- original exact system `rank2-two-spectrum-completion-v1.md`, SHA-256 `2a0d363458746f20e9c226db71c8460869386ebc95381fc6c62e51dca8612f6e`.

No pinned predecessor is modified. The historical arithmetic observations remain unadmitted and are not proof premises. Prior reviews do not automatically cover this new obstruction.

Use G=F2^8, H²=256I, W a six-space, U=W-perp, D=1−1_W, chi=1−2D, q=2e0−1_U. The retained genuine-target pruning gives E empty and cases(16,24),(16,32),(20,24). Here we consider L=16,alpha1, hence the first case. Put

    h=Hdelta in{0,±4,±8}, b=phi(h), C=Hb,
    C=4delta on supp(delta), |C|=12 elsewhere,
    B=q−b, T={B=0}.

At alpha1 there is ONE v in U with b(v)=q(v), all other b|U=0. Thus the full system's ternary a, supported exactly on T, satisfies

    a(v)=sigma in{±1}, a=0 at the other three U sites.

Let p=Ha/4. The complete R alphabet and balance are

    p in{0,±2} on W, p in{±1,±3} off W, p(0)=0.      (1)

The same a comes from the half-subset V of T, not an independent row choice:

    a=1−2*1_V on T, a=0 off T,
    |V|=59,
    XOR(V)_i=|T intersect H_ei|/2+D(e_i) mod2,
    ||V intersect H_x|−|T intersect H_x|/2|<=3
                                          for ALL x. (2)

The norm a²+B²=1 is exact and enforces BOTH Boolean signs B+a,B−a and original N. The full512-bit map is

    F(x,0)=(1−B−a)/2, F(x,1)=(1+B−a)/2,

with balance256 and complete Walsh sectors8p and2HB. The intrinsic integer forcing is imposed throughout:

    delta star p=[h(v)*sigma/4]chi_v.                 (3)

Its amplitude is phase-bound to this same V; it is not independently chosen. The proof below gives a contradiction for BOTH signs when |h(v)|=4.

## 2. The canonical carry is quadratic — direct proof

Write C/4=zeta=delta+3eta, where eta=0 on the16 defects and±1 elsewhere. The intrinsic Boolean sign tau=eta−delta is cubic-or-lower. For the integer

    j=(zeta−1)/2,

we have Hj=32b−128e0, so j modulo2 has degree at most3; pointwise(−1)^j=−tau. Also set the INTEGER k=(p−D)/2; Hp=64a and HD divisible by64 give Hk divisible by32, so its parity also has degree at most3.

We need the stronger COMMON relation j+k quadratic, not two unrelated cubic bits. Here is its proof from both genuine Boolean spectra.

Let K=H(1−2f) be any genuine eight-variable Boolean spectrum with K=2 modulo8. Write Omega=supp(f), w=|Omega| and W_Omega=H1_Omega. Then K=256e0−2W_Omega and the canonical congruence makes W_Omega=3 modulo4 everywhere; in particular w=3 modulo4. Put I(x)=#{y in Omega:x dot y=1}. Since W_Omega=w−2I, I is even everywhere and XOR(Omega)=0.

The integer expansion of I/2 modulo2 is quadratic: its linear coefficients are half the even first moments of Omega, its quadratic coefficients are the pair moments, and all higher terms have a remaining factor2. Moreover

    (K²−4)/32 mod2
       =(W_Omega²−1)/8 mod2
       =(w²−1)/8+I/2 mod2.

Thus J=(K−2)/8 modulo2 is quadratic, because K=2+8t gives(K²−4)/32=t+2t².

Apply this to the ACTUAL second spectrum

    K_2=(2HB−2Ha)/2=−2chi−4zeta−4p.

Substituting chi=1−2D, zeta=1+2j, p=D+2k gives

    (K_2−2)/8=−1−j−k.

Consequently

    Q=j+k modulo2 is quadratic.                    (4)

This derivation uses actual inverse Boolean signs and canonical spectra, not only a magnitude profile or a freely selected cubic pair.

## 3. The active h magnitude fixes the zero count modulo4

The intrinsic phase has

    Htau=(64b−4h)/3.

On U only its coefficient at v is nonzero. If |h(v)|=4, b(v)=q(v) gives h(v)=4q(v), so Htau(v)=16q(v). If |h(v)|=8, then h(v)=−8q(v), so Htau(v)=32q(v).

Summing tau over W divides its U-coefficient sum by4. Hence the Boolean j restricted to W has weight

    32+2q(v) if |h(v)|=4;
    32+4q(v) if |h(v)|=8.                            (5)

On six bits, adding a quadratic Q does not change the weight of a cubic j modulo4. Indeed wt(Q) is divisible by4 by the elementary quadratic exponential-sum formula. Also sum jQ is even, since its degree is at most5<6. Therefore wt(j+Q)=wt(j)+wt(Q)−2|supp(j) intersect supp(Q)| is congruent to wt(j) modulo4. The same applies after adding the constant1.

On W, k modulo2 is exactly the indicator p!=0, so the zero indicator is1+j+Q by(4). Thus for its actual zero count z,

    z=2 mod4 if |h(v)|=4,
    z=0 mod4 if |h(v)|=8.                            (6)

In particular the odd-occupancy branch is not permitted to choose an unrelated zero-set residue.

## 4. All three outer low-support sets are occupied

Choose dual coordinates x=(r,t), r in F2², t in F2^6, with W the r=0 coset and U the dual s-space at y=0. Let p_r and beta_r be the four six-variable slices, beta=phi(p). Set

    P_r(y)=H6p_r(y), T_r(y)=H6beta_r(y),
    lambda_r(y)=sum_s (−1)^(r dot s)a(s,y).

The genuine Hp=64a gives

    P_r=16lambda_r,
    T_0=−P_0/2=−8lambda_0.                          (7)

The second equality uses beta_0=−p_0/2 on W. At y=0 the same complementary a has only its entry sigma at v in U. Therefore

    sum_t p_r(t)=P_r(0)=16sigma*chi_v(r).

For r!=0, if c_r=#{t:|p_r(t)|=1} were0 then beta_r would vanish and that sum would be0 modulo3. Its actual value is±16, nonzero modulo3. Hence **each c_r is positive**.

The four lambda_r(y) have the SAME parity for every y, since signs are equal modulo2. Slice Parseval gives

    sum_y lambda_0²=64−z,
    sum_y lambda_r²=144−2c_r for r!=0.

Comparison modulo4 yields

    z=2c_r mod4 for EACH outer r.                   (8)

Norm and support give wt(a)=118, so full Parseval in(1) yields

    z+2(c_1+c_2+c_3)=24.                            (9)

These statements concern the same actual slices, not independently chosen counts.

### Nonempty cubic zero sets have z>=8 and z!=10

The integer k has Walsh transform divisible by32, hence parity degree at most3. Restriction to six-dimensional W preserves that degree, and1+k is its nonempty zero indicator. The standard degree/weight induction gives z>=8.

For completeness z10 is also impossible. A six-bit degree-at-most3 zero indicator has even sums after multiplication by every monomial of degree<=2. Thus the matrix of columns(1,t), t in its zero set, has pairwise orthogonal rows over F2. For10 distinct points its rank is at most5 by self-orthogonality, and at least5 since an affine three-flat has only8 points. Hence the set lies in an affine four-flat. Its indicator then factors that codimension-two flat indicator times a function on four bits. Degree<=3 makes the latter affine, of weight0,8 or16, not10.

Combining(6),(8),(9), positivity of all c_r and z>=8,z!=10 gives, in the active-magnitude4 branch, only

    z18 with(c_1,c_2,c_3)=(1,1,1),
    z14 with(c_1,c_2,c_3)=(3,1,1), up to permutation. (10)

The next sections exclude BOTH uniformly by actual ternary closure; this table is not itself a resolution.

## 5. Exact four-entry closure tables

At every y the SAME a satisfies

    a(s,y)=phi[T_0(y)+sum_(r!=0) chi_r(s)T_r(y)],
    T_0(y)=−8sum_s a(s,y).                          (11)

Only residues of the three outer T_r affect the first equation, but T_0 in the second is the ACTUAL integer. The following small character calculations are written algebra, not executed enumeration.

### Three nonzero outer residues

Each residue is±1. At this one y, permuting the four character positions and flipping the two independent characters normalizes them to x,y,rho*x*y with rho=±1. These changes preserve lambda_0 and every nontrivial lambda magnitude; no global stream is independently re-signed.

For rho=+1, x+y+xy takes3 at one position and−1 at the other three. For t=phi(T_0)=0,+1,−1 the four lifted values have sums−3,+1,+2. Equation(11) forces T_0 respectively24,−8,−16. For rho=−1 the analogous sums are+3,−2,−1, giving T_0=−24,+16,+8. Every listed integer has exactly the stated residue.

Thus where all three outer residues are nonzero,

    |T_0| in{8,16,24}, NEVER0;
    |T_0|=8 implies |lambda_r|=1 for ALL r!=0.       (12)

For example the magnitude8 case has a single nonzero lifted entry, so every four-point Walsh component has magnitude1. The magnitude16 case has nontrivial magnitudes2; the24 case has nontrivial magnitudes1.

### Exactly two nonzero residues

Let the inactive channel be1 and choose the two independent active characters as x,y. The sums of phi(T_0+x+y), for t=0,+1,−1, are0,+1,−1. Hence the only actual T_0 values are0,−8,+8. The product character xy is the inactive channel and its Walsh component is0 at T_0=0 and has magnitude3 at T_0!=0. Therefore

    |T_0| in{0,8},
    |lambda_1|=0 or3, nonzero iff T_0!=0.            (13)

All actual residue signs are included by character permutations; their magnitudes and the exact T_0 constraint are unchanged.

## 6. Uniform contradiction for three singleton outer supports

In the z18,(1,1,1) case, every T_r for r!=0 is the transform of one signed point, hence is±1 and never0. All three residues are nonzero at all64 values of y. By(12), |T_0(y)|>=8 everywhere.

But beta_0 has64−z=46 nonzero entries, so its genuine six-bit Parseval identity is

    sum_y T_0(y)²=64*46.

The pointwise bound would make this at least64*64, contradiction. This uses the actual zero count and the exact residue closure, not a selected support placement.

## 7. Uniform contradiction for outer supports3,1,1

Put the three-point support in channel1. Its three distinct signed characters agree on an affine four-flat Y of size16; there T_1 is±3 and its residue is0. Outside Y its value is±1. Channels2 and3 are signed singletons, so their transforms are±1 everywhere.

Outside Y all three outer residues are active. On Y exactly two are active. From(12),(13),

    |T_0|>=8 outside Y;
    |T_0| in{0,8} on Y.

Here z14 makes sum T_0²=64*50. The48 outside values already cost48 units after division by64. A single outside magnitude16 would add3 units and a24 would add8, exceeding the remaining2. Therefore EVERY outside value has magnitude8, and exactly TWO points of Y have magnitude8 while the others are0.

By(12), the inactive-channel lambda_1 has magnitude1 at all48 outside points. By(13), it has magnitude3 at those two inside points and0 at the other14. Its squared sum is consequently

    48+2*9=66.

The ACTUAL slice Parseval from(7), with c_1=3, requires

    sum_y lambda_1²=144−2*3=138.

Contradiction. No affine placement, sign pattern, graph projection or independent row choice was omitted.

## 8. The new uniform theorem and first real remaining step

**Odd-alpha1 noncompletion theorem (WRITTEN CANDIDATE).** For EVERY retained full L16 S array and actual E-empty alpha1 q/U placement whose unique active coefficient has |Hdelta(v)|=4, there is no half-subset V satisfying ALL original prescribed-XOR slabs, norm, R/N, balance and both Boolean spectra. Both signs in the required rank-one forcing delta star p=±chi_v are covered.

The v3 construction gives odd unsigned occupancies in all four U-annihilator cosets exactly because this coefficient has magnitude4. Thus the ENTIRE odd-occupancy placement class—not merely a Gold or a chosen outside example—is excluded by the same theorem.

This is not a whole(16,24) theorem. Any remaining full completion must have active |h(v)|=8. Equation(6) then gives z=0 modulo4; by(8) all c_r are positive EVEN. With z>=8 and(9), only

    z8,(c_1,c_2,c_3)=(4,2,2),
    z12,(c_1,c_2,c_3)=(2,2,2), up to permutation     (14)

remain. The signed support sums on the four U-annihilator cosets have magnitude2, so their unsigned occupancies are even. No projection, slice class or independent stream is inferred from that parity.

The first real unproved step is the SAME-V coupled completion for these EVEN alpha1 placements: the intrinsic signed16-point S alphabet/triple identities, actual q/U signature, rank-one forcing with amplitude±2, canonical carry, all256 slabs and both inverse signs must hold simultaneously. The two count rows in(14) do not establish or exclude that functional problem.

## 9. Entire frontier and other cases retained

- **(16,24): OPEN as an entire case.** The odd-occupancy/magnitude4 alpha1 branch is uniformly excluded by this new candidate; magnitude8/even placements remain with the exact interface above. No Gold-covering assumption is used.
- **(16,32): OPEN.** Its intrinsic signed-set classification and exact integer annihilator delta star p=0 with the same V remain; accepted E116 is still only its structural slice class.
- **(20,24): OPEN.** The universal divisibility and exceptional budget remain, with delta star p=3He at the at-most-eight ACTUAL Fourier modes and signs bound to V. No independent mode choice or R completion is supplied.
- **U2 and unrestricted balanced NL242: UNPROVED.** No full function or entire residue-type exclusion is claimed.

The next single attack should be the even-alpha1 two-pair/three-pair residue geometry in(14), or the intrinsic collision branch with this forcing retained. It must not revert to another Gold example, assume graph/U compatibility, or count a necessary magnitude table as completion. Earlier parent-supported intrinsic statements remain intact; this new uniform completion obstruction requires its own frozen reconstruction. No deadline reset, new scientific GO, publication, formal verification, cross-model review or round closeout occurred.
