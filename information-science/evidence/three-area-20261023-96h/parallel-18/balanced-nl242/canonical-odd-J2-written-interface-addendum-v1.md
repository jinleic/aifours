# Canonical odd-spectrum / J2 interface — exact written source reconstruction

Owner InfoBalancedNL242-2, info-6. Actual precreation clock: `Sun Oct 25 18:45:34 PDT 2026`.

**SOURCE-INTERFACE RECONSTRUCTION, NOT A NEW CASE ACCEPTANCE OR CORPUS RESULT.** This independently derives the exact odd-spectrum quadratic-bit and genuine K2 carry interface used by the primary. It does not change frozen v17/U2 bytes, unilaterally minimize J_U2, authenticate old finite-corpus computations, or expand an already frozen gate. The current U2 candidate retains its old named boundaries until an appropriate fresh review/parent decision explicitly accepts any new reconstruction.

All mathematics is WRITTEN integer/F2/Walsh reasoning. No interpreter/calculator/eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/new GO. Metadata/static source reads/clocks/hashes and own-root output only. All permanent findings, including the owner's newly disclosed cadence lapse, remain.

## 1. Exact selected source and non-consumed corpus boundary

Static source `information-science/evidence/hard-continuation-20261015/proof.md`, actual observed SHA256 `d2c1605d8ee20423e137066b62b3dac31406bd4380d075c1b85064c01cf6dff9`, selected LF1–42 and70–88 were NOW read. These contain a GENERAL single odd-table lemma and canonical-sign identity. The file as a WHOLE is a restricted fixed-half finite-corpus result. No finite corpus, certificate array, numerical histogram, parity enumeration, checker/rejection count or its claimed coverage is an input here; no checker was run or replayed.

The source attributes this mechanism to Wang–Lou–Wang arXiv2610.17871v1 equations31–32. That external paper was not freshly body-audited in this pass; no novelty or priority claim follows. The unrestricted elementary lemma needed here is reconstructed below directly, rather than borrowing an entire preprint or the corpus conclusion.

## 2. GENERAL odd eight-variable Boolean spectrum, with NO magnitude cap

Let h:F2^8->F2 have odd support S_h of size w, and let

    W_h(a)=sum_x (-1)^[h(x)+a.x],
    I(a)=sum_(x in S_h)(a.x modulo2),

where I is an ORDINARY integer count. Then exactly

    W_h(a)/2=128*1_(a=0)-w+2I(a).                  (1)

Every W_h(a)/2 is odd, so W_h(a) is nonzero2 mod4 and

    J_h(a)=(W_h(a)^2-4)/32 modulo2

is well-defined as an integer parity. The128 term in(1) changes the divided square by an EVEN integer, so it can be omitted for this parity. Expanding(-w+2I)^2 gives

    J_h=(w²-1)/8+binom(I,2)+((1-w)/2)*I modulo2.   (2)

Each l_x(a)=a.x is a LINEAR Boolean form; binom(I,2) counts unordered DISTINCT pairs of active l_x's, so its parity is sum_(x<y in S_h)l_x*l_y. Thus J_h has degree<=2 for EVERY odd Boolean table, not only a fixed half or one of the old enumerated records.

For a fully inspectable support-moment formula, set

    c_i=sum_(x in S_h)x_i,
    m_ij=sum_(x in S_h)x_i*x_j.

Then the constant, linear and quadratic coefficients are respectively

    (w²-1)/8,
    binom(c_i,2)+((1-w)/2)*c_i,
    c_i*c_j+m_ij             (i<j),               (3)

all mod2. The last formula follows because the cross coefficient in sum_(x<y)l_x*l_y is c_i*c_j-m_ij, equal to c_i*c_j+m_ij overF2. These are TRUTH-SUPPORT moments, not an identification with the primary's different signed-S defect moment matrix.

Negative Walsh values require no exception: J_h is defined by squares. No assumed spectral cap, equality case, fitted polynomial or finite parameter check enters(1)–(3).

## 3. Canonical signs are actual Boolean spectra, not chosen phases

Let s=XOR(S_h) and epsilon=(-1)^((w+1)/2). Mod4, equation(1) says

    W_h(a)/2=epsilon*chi_s(a) modulo4.

For a positive magnitude m2 mod4, exactly ONE of m,-m is2 mod8. Thus its canonical signed value K(a), chosen only by this residue, is EXACTLY

    K(a)=epsilon*chi_s(a)*W_h(a), K(a)=2 mod8.

Walsh inversion gives

    HK(x)=epsilon*256*(-1)^h(x+s).

So K is the spectrum of an ACTUAL Boolean sign table, produced by a truth-domain translation and possibly a complement. Canonical signs do not require independent phase choices at individual frequencies or a sign search.

Conversely, if an integer K satisfies HK pointwise+/-256 and K2 mod8, its inverse is an actual Boolean sign. Its truth weight w_K=(256-K(0))/2 is3 mod4 and hence odd. The general lemma above therefore applies to K itself. Writing K=2+8t,

    (K²-4)/32=t+2t²=t modulo2,

so the actual bit

    J_K=(K-2)/8 modulo2

is quadratic. This is the exact literal K2 interface the primary needs; it is not an assertion about arbitrary functions with merely similar magnitudes.

## 4. TRUE common carry for the UNPRUNED primary, including C+3P

For an actual solution of the unpruned S/R/N system, set

    zeta=(C+3P)/4, j_tilde=(zeta-1)/2,
    p=R/8, k_tilde=(p-D)/2,
    chi=1-2D.

These are INTEGER lifts; zeta is odd and p has parityD. Without setting E or P to0,

    S=-4chi-8zeta, R=8p,
    K2=(S-R)/2=-2chi-4zeta-4p
       =2+8*(-1-j_tilde-k_tilde).

The exact field-to-integer norm in the original formulation supplies HK2 pointwise+/-256, so §3 applies. With j,k the parity bits of the two lifts,

    J2=(K2-2)/8=1+j+k modulo2,
    Q=j+k=J2+1 is QUADRATIC.                       (4)

This conclusion uses the ACTUAL Boolean K2 and the shared integer lifts. It is NOT the false assertion that two arbitrary cubic bits necessarily sum to a quadratic. It holds before pruning E nonempty away and therefore does not create a hidden Eempty gap in U2.

The separately used cubic bounds for j,k follow from their actual Walsh divisibility32 at the prior interface;(4) is an additional common-pair relation, not a consequence of those two degree bounds alone. No independently re-signed physical row or mode occurs.

## 5. Exact paired-half existence normalization, with explicit limits

Suppose two eight-variable Boolean halves have ODD weights, use the SAME character coordinates, and their spectra G0,H0 obey |G0(a)|+|H0(a)|<=28. Normalize each by §3 to K1,K2. Each remains a genuine Boolean spectrum, and the pointwise magnitude capacity is unchanged. If the original nine-variable table is balanced, G0(0)+H0(0)=0, so their magnitudes at0 agree. Uniqueness of the canonical signed magnitude gives K1(0)=K2(0), hence R(0)=0 for R=K1-K2.

Define a NEW nine-variable Boolean table from the canonical inverse halves g_c,h_c by F_c(y,0)=g_c(y),F_c(y,1)=1-h_c(y). Its Walsh halves are K1-K2 and K1+K2; its balance is R(0)=0 and full capacity is

    max(|K1-K2|,|K1+K2|)=|K1|+|K2|<=28.

Its square-residue bits J_i are unchanged by normalization; therefore D=(K1-K2)/8 modulo2=J1+J2 retains that intrinsic square-residue type. This is an EXISTENCE-preserving canonical representative in the stated ODD-half class. It does NOT claim that independently translated/complemented halves leave the original nine-variable function identical, nor that ALL remaining original types have an odd-half split. That larger reduction retains its precise older named scope.

The primary's unpruned-system reconstruction already produces its canonical Boolean pair directly; it does not require guessing or fixing any original truth-table half. This subsection clarifies an old source interface only, not a new numerical bound or a finite witness.

## 6. Trust/chronology ceiling

The selected source ranges and actual hash were read/observed before this write. Equations(1)–(4) are freshly WRITTEN identities under literal hypotheses. This note is a LATER nonessential corroboration of an existing named interface, not a new pre-freeze premise of v17, the U2 candidate or an already dispatched whole-case gate. No old input is silently removed from J_U2; parent review/adoption must explicitly decide any assurance change.

No old corpus computation/output is replayed, authenticated or given new credit. No global S floor/pruning/three-case or other residue-type proof is supplied here, and no unrestricted balancedNL242/SOTA/novelty claim follows. All current case/U2 bodies remain at their actual gates, all findings remain permanent, and original primary/cutoff/deadline/HOLD continue. No formal/kernel/human/configured-family/executable acceptance or scientific GO is conferred.
