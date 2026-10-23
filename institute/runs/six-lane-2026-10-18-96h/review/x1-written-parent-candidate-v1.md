# X1 exclusion from left-fibre counting, inversion and triangle indices

Written at 2026-10-19T01:04:18-0700. Status: CANDIDATE written proof, not yet reviewed. This is not a novelty claim; the same five-index family is already claimed in Menon/Margolis–Schnabel material. Purpose: replace the load-bearing StageA computation by a written proof if independently accepted. No computational output is a premise.

## Statement

There is no group G with five pairwise disjoint left cosets of finite-index subgroups whose indices are
(3r_1,3r_2,6r_3,6r_4,6r_5), where r_1,r_2 are odd positive integers and all five r_i are pairwise coprime.

Use the accepted finite-core quotient to take G finite. Write d_1,d_2 for the first two vertices and C={c_1,c_2,c_3} for the other three. Every pair meeting a d-vertex has index gcd3; every C–C pair has index gcd6. Let alpha_ij=[G:U_i∩U_j]/lcm(n_i,n_j), so 1≤alpha_ij≤g_ij−1.

## Imports, with exact facts

1. **LFC**: at a fixed vertexv, local indices are lambda_j=n_j alpha_vj/g_vj. If nonnegative weightsy satisfy sum_(j∈S)y_j≤1 for every hereditary allowed setS (every subset of size t≥2 contains a pair of local indices with gcd≥t), then sum_j y_j alpha_vj/g_vj<1. Only Sun(2) is used below: a pair of coprime local indices can never occur in an allowed set.
2. **INV**: inversion gives another disjoint left-coset configuration with the same labelled indices and a symmetric matrixalpha*, with alpha_ij+alpha*_ij≤g_ij.
3. **T**: in any triangle, gamma_v=gcd(n_v,lcm(n_j,n_k)), ell_v=n_v/gamma_v; tau_min=lcm_edges alpha_ij/gcd(alpha_ij,ell_k), and tau_max=min_apex gamma_v alpha_jk min(alpha_vj/g_vj,alpha_vk/g_vk). A genuine configuration has tau_min≤tau_max.

These are the accepted general LFC/INV/T statements at their existing scopes; the proof does not import Sun(3)–Sun(6), RPLP, finite leaf data, Menon's theorem or the unread Margolis–Schnabel lemma. R0 is used only to lift the finite argument to arbitrarygroups.

## Proof

**1. Choose an orientation.** On the d_1d_2 edge, alpha andalpha* lie in{1,2} and have sum≤3. At least one is1. Replace the configuration by its inverse if necessary so alpha_d1d2=1.

**2. Every d–C edge has alpha1.** At d_1, the local index of d_2 is r_2. If alpha_d1c=2 for somec∈C, its local index is4r_c. These two local indices are coprime because r_2 is odd and coprime tor_c. Put weight1 on these two neighbours and0 elsewhere. No allowed set contains both; the weights are feasible and their LFC objective is1/3+2/3=1, contradiction. Hence alpha_d1c=1 for everyc. Interchange d_1,d_2 to obtain alpha_d2c=1 as well.

**3. Every C–C edge has alpha1 or2.** Fix distinctc,c′∈C and putx=alpha_cc′∈{1,…,5}. For eachi∈{1,2}, the triangle(d_i,c,c′) has gamma_di=3, gamma_c=gamma_c′=6, ell_di=r_i and the other two edgealphas1. Therefore

tau_min=x/gcd(x,r_i),    tau_max=min(x,2).

Ifx=4, the oddness ofr_i gives tau_min4>2, impossible. Ifx=3 or5, both triangles requirex|r_1 andx|r_2, impossible bycoprimality. Thusx∈{1,2}. Values of theCcofactors, including arbitrarily high2/3/5valuations, do not enter this calculation.

**4. LFC at a C-vertex contradicts strictness.** Fixc∈C; call the otherCverticesj,k. The d-neighbour local indices arer_1,r_2, and their two LFC contributions withweight1 are1/3 each. If at least one of alpha_cj,alpha_ck equals2, giveweight1 to that neighbour and0 to the other. Its local index is2r_j, coprime toboth oddr_1,r_2; the three positively weighted local indices are pairwise coprime. Hence every allowed set contains at most one of them, and the objective is1/3+1/3+2/6=1.

Otherwise bothCedgealphas equal1. The four local indices arer_1,r_2,r_j,r_k, all pairwise coprime. Giveweight1 toallfour; objective1/3+1/3+1/6+1/6=1. Both cases contradict LFC'sstrict<1 bound. The configuration cannotexist. QED.

## Bridge and verification boundary

The accepted K5.3→X1 deletion bridge selects bothDvertices and anythreeCvertices, with exactly the hypotheses above. If this proof is accepted, K5.3 has a written exclusion independent of StageA certificate checking; the old computation, qualification controls and permanent late-freezeF-1 remain preserved as historical evidence. This candidate itself does not prove Sun(7), assess priority or supply a Lean proof.
