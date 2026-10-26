# Candidate v1 — unavoidable twisted officer matchings in the all-three deficit profile

Observed before creation of this continuation: `2026-10-23T14:38:32-0700`. PhysicsAME46, physics-6. This is resumed OWN AME research after the parent-assigned MOQLS peer reconstruction. Written only; no scientific executable, enumeration, CLI, solver or nested agent.

## Exact surviving target and limited outcome

The two-thin-axis candidate leaves support48/e0 cases with at least three thick axes. As one bounded next obligation, consider the genuinely surviving four-thick-axis deficit profile

    {3,3,3,3}⁴.

The following necessary structure actually holds for ANY AME(4,6) with this officer profile, without requiring e=0. It rules out a coherent-permutation/antisymmetric-support route, **not the whole profile**, not support48, and not the unrestricted48..60 gap. This is a candidate partial structural result; no independent reconstruction or novelty claim.

Write A=6ψ and T={x:|A_x|=1}. For coordinate i, let A_i be the four values with deficit d_(i,a)=3, and B_i their two-value complement. (Here A_i denotes a local alphabet, not the tensor A.) Let N=supp A\T.

Only the exact two-party AME line norms are used: for every one of the six coordinate pairs P and every value pair, Σ_(x on that P-line)|A_x|²=1. Hence every line is occupied; an officer is alone on every line through it; no two officers agree in two coordinates; a line without an officer contains N; and N lies in the product of active alphabets. These facts follow from the full six marginals I36/36. No one-body, approximate or equal-modulus replacement is introduced.

## 1. Officer active weight is exactly two

The profile gives h=12,t=24 and v_i=|A_i|=4 for all i. For x∈T put c(x)=|{i:x_i∈A_i}|. The historical officer-count identities, re-derived by incidence counting, give

    Σ_T c(x)=6Σ_i v_i−4h=48,
    Σ_T binom(c(x),2)=Σ_(i<j)v_i v_j−6h=24.

For the first identity, coordinate i contributes Σ_(a∈A_i)(6−d_(i,a))=6v_i−h. For the second, in the active pair grid A_i×A_j exactly h pair-lines contain N and no officer; all other v_i v_j−h lines contain one officer. Sum over six pairs.

Every integer c satisfies(c−1)(c−2)/2≥0, and its sum over T is24−48+24=0. Therefore each officer has c∈{1,2}. Since their average active weight is48/24=2, **every officer has exactly two active coordinates**. Thus T is partitioned into six sets T_ij, one for each unordered active-coordinate pair{i,j}; the other two coordinates of such an officer lie in the binary inactive alphabets.

This equality consequence of the old counting lemma is a baseline tool, not a new48 proof.

## 2. Each active pair determines a bijection

Fix i≠j and a∈A_i. Its deficit is3, so exactly three of the four pair-lines(a,b), b∈A_j, meet N; the hole-neighbor set lies in A_j and has size3. Precisely one remaining b gives an officer. Define it as

    F_ij(a)=b in A_j.

The officer on that line belongs to T_ij by §1; call it x_ij(a). The same reasoning from coordinate j proves F_ij is bijective and F_ji=F_ij^(-1). Consequently |T_ij|=4.

If{k,l} is the complementary coordinate pair, the four officers x_ij(a) lie in B_k×B_l on those coordinates. They have distinct(k,l) pairs because two officers cannot agree in two coordinates. There are exactly four such binary pairs, so they use all of them. In particular either inactive coordinate gives a balanced2+2 partition of A_i.

## 3. Every triangle holonomy flips an inactive binary partition

Choose three distinct coordinates i,j,k and let l be the fourth. Label B_l by F2. Define

    chi(a) = [coordinate l of x_ij(a)] in F2,
    H_ijk = F_ki composed F_jk composed F_ij : A_i -> A_i.

The function chi takes each bit twice by §2.

**Candidate holonomy lemma.** For every a∈A_i,

    chi(H_ijk(a)) = chi(a)+1  (mod2).

In particular H_ijk has no fixed point. Its cycle type on four symbols is therefore a4-cycle or two disjoint transpositions.

**Proof.** Follow the three officers

    x = x_ij(a),
    y = x_jk(F_ij(a)),
    z = x_ki(F_jk(F_ij(a))),

and put x′=x_ij(H_ijk(a)). The officers x,y are distinct because their active-coordinate pairs are different, and they agree in coordinate j. They cannot also agree in coordinate l, so their l-bits are opposite. Likewise y,z agree in coordinate k and have opposite l-bits. Finally z,x′ agree in coordinate i and have opposite l-bits. Three flips give the displayed identity. If H_ijk(a)=a then x′=x and its l-bit would differ from itself, impossible. ∎

No search over permutations, tensor coefficients or phases is hidden in this argument. The conclusion concerns the actual officer code induced by an AME state.

## 4. A coherent matching ansatz is impossible

Suppose there were local relabelings lambda_i:A_i -> {0,1,2,3} making all missing active-pair matchings equal-color, namely

    F_ij=lambda_j^(-1) composed lambda_i  for every i!=j.

Every triangle composition would then be the identity, contradicting §3. Thus the six matchings are necessarily **twisted**: one cannot put every active pair's forbidden matching simultaneously on the same diagonal by independent local relabelings.

This closes the tempting special route in which N is assumed to be the24 permutations of four common colors (for example, an antisymmetric-tensor support) and one tries only to solve its phase equations. That support would have coherent equal-color missing pair matchings, incompatible with the required officer profile before any phase calculation. It does not exclude all twisted matching patterns or all N-supports in this profile.

## Remaining exact obligation

A complete exclusion or construction still requires coherent amplitudes on the allowed active tuples for the genuinely twisted matching data, simultaneously unitary in12|34,13|24,14|23, together with their actual officer placements. The holonomy condition is necessary, not sufficient. A phase obstruction for one coherent matching graph would miss the actual residual problem; no such shortcut is claimed.

The source-overlap check read the existing LOWER48 officer-count lemma and searched the old accepted support manuscripts/archived49 draft for holonomy/monodromy/fixed-point formulations. No matched formulation was located there; that bounded local check is not worldwide novelty clearance. All old results remain baselines and all other profiles/e>0 obligations stay open here.
