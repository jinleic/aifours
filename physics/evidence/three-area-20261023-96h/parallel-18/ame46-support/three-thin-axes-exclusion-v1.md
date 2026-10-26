# Candidate v1 — no e=0 AME(4,6) has three entirely thin active-coordinate alphabets

Observed before creation: `2026-10-23T14:19:38-0700`. PhysicsAME46, physics-6. Immutable written CANDIDATE / PARTIAL. No scientific execution or independent reconstruction. This strengthens the binary profile candidate, not the numerical bound48.

## Statement and dependencies

Use A=6ψ, T={x:|A_x|=1}, N=supp A\T, t=|T|, h=36−t, e=|supp A|−(72−t), and d_(i,a)=6−|{x∈T:x_i=a}|. A coordinate is entirely thin if every positive d_(i,a) equals2; zero deficits are allowed.

**Candidate theorem.** For an AME(4,6) with e=0 and N nonempty, at most two of the four coordinates are entirely thin.

In particular every e=0 support48 profile with three{2⁶} parts is impossible, no matter what the fourth profile is. This is an analytic whole-family exclusion, not one support graph, symmetry ansatz or SAT miss. It still does not exclude every support48 profile/case, so **no lower49 bound is claimed**.

The proof uses the exact-two-line facts and the doubled-fiber module Theorem A of `thin-slice-obstruction-v1.md`, SHA256 `ba269009d0f352e9b9fed1967cead86b5594b9ddee6d822cd8190fc67c2bce4f`. Those facts and Theorem A are proved there from all three unitary flattenings; no equal-modulus or real-amplitude assumption is made. The standard no-AME(4,2) result and its elementary Pauli derivation are supplied there too. The only external classical theorem used below is Tarry's no pair of orthogonal Latin squares of order6. The small officer-code arguments below are previously known baseline mechanisms; the new-to-this-slot step is the structural decomposition and its complete family composition.

## 1. Three thin axes force doubled qubit modules

Assume coordinates2,3,4 are entirely thin. Since their positive deficits sum to the same h, each has exactly k=h/2 active values, where1≤k≤6. Each such value occurs in exactly4 points of N, and |N|=2h=4k. Coordinate1 is unrestricted at this point.

Fix a triple z of values in coordinates2,3,4. It has at most two nonzero coefficients A_(u;z): three would violate the exact-two property on any pair of coordinates among2,3,4. If it has two, their coordinate1 values form an unordered pair{a,b}. Theorem A closes such triples into a cubic bipartite component on the SAME value pair{a,b}; its2r vertices use r≥3 values in each of coordinates2,3,4, each appearing twice. Every used thin value's four non-officer entries are already accounted for by its two doubled triples. Thus no non-officer point outside the module uses any of these values. This also prevents modules for different coordinate1 pairs from sharing an active value in the other coordinates.

After all doubled modules have been identified, restrict to the remaining active values in coordinates2,3,4. The three residual alphabets have the same size n=k−Σr. The residual has4n entries, exactly one coefficient per occurring triple z, and every line meeting it still has exactly two entries. Its pair-projection graphs among coordinates2,3,4 are simple2-regular graphs.

### Singleton residual lemma

Such a residual cannot be nonempty, even though coordinate1 may initially have more than two values.

**Proof.** The no-doubling triangle-saturation argument of `binary-shadow-exclusion-v1.md` §2 does not use the size of coordinate1 when deriving its tripartite graph. For clarity, its essential steps are: each edge(b,c) has two entries with different d-values; since each endpoint has two D-neighbors, their D-neighbor sets coincide; propagate from b's two C-neighbors and two D-neighbors to obtain a closed K_(2,2,2). Every one of its eight triples occurs once. Repeat on another component if necessary. This is a universal propagation argument, not a graph enumeration.

It remains to justify the qubit bound on coordinate1, which was automatic only in the earlier binary setting. In a K_(2,2,2) component, let q_u be the number of its eight triples assigned coordinate1 value u. For either value of any one of coordinates2,3,4, the pair-line(u,value) contains either0 or2 entries. All its non-officer entries lie in this component, because the tripartite component has no external edges. Hence q_u is0,2 or4.

The value q_u=2 is impossible: for each of the three remaining coordinates, those two entries would have to take the same coordinate value (otherwise its two pair-lines would each contain just one entry). They would therefore be the same triple, contradicting distinctness and no doubling. Thus each used u occurs four times; exactly two values u0,u1 occur.

This8-entry tensor is supported on2×2×2×2. For each of its selected pair-lines the exact two entries are in the block, so each of the three4×4 flattenings B_P is unitary with no outside row/column entries. If ω=3 times the restriction of ψ to this block, its norm is1, the flattening of2ω is B_P, and all six reductions are

    ρ^ω_12=B_12 B_12†/4=I4/4,     ρ^ω_34=(B_12†B_12)^T/4=I4/4,
    ρ^ω_13=B_13 B_13†/4=I4/4,     ρ^ω_24=(B_13†B_13)^T/4=I4/4,
    ρ^ω_14=B_14 B_14†/4=I4/4,     ρ^ω_23=(B_14†B_14)^T/4=I4/4.

The norm is9·4/36=1, by four unit rows of B_12. This contradicts no-AME(4,2). Therefore n=0. ∎

Consequently all of N is partitioned into doubled qubit modules. Each uses r≥3 active values in each thin coordinate, and their r's sum to k≤6. The only possible module-size partitions are therefore: a single module with r∈{3,4,5,6}, or two modules with r=3 each. There is no module decomposition for k=1 or2.

## 2. A single module with r=3,4 or5

A single module uses one fixed pair{a,b} in coordinate1. Its2r doubled triples contribute2r non-officer entries at a and2r at b. The exact slice formula |N∩{x1=u}|=2d_(1,u) gives coordinate1 profile{r,r}; no other value has positive deficit. The full profile is therefore

    {r,r}{2ʳ}³,      h=2r,      t=36−2r.

### r=3: elementary officer counting

This is profile{3,3}{2³}³, t=30,h=6. Let V_i be the active-value sets and c(x)=|{i:x_i∈V_i}| for an officer x. Here v=(|V_i|)=(2,3,3,3). Counting officers on active values and active pair-lines gives

    Σ_T c(x)=6Σv_i−4h=42,
    Σ_T binom(c(x),2)=Σ_(i<j)v_i v_j−6h=9.

The first identity uses Σ_(a∈V_i)d_(i,a)=h. The second uses exactly h hole lines in each active pair grid, every other pair-line containing one officer. But(c−1)(c−2)/2≥0 for integer c, whereas its officer sum is9−42+30=−3. Contradiction. This is the existing officer-counting Lemma17, not a new numerical-bound proof.

### r=4: the binary officer code

Coordinate1's active values a,b each carry6−4=2 officers, four officers total. For each other coordinate, those officers must avoid all four active values, because the(a,value) and(b,value) hole neighbors are exactly the module's four values. They consequently lie over four2-letter alphabets. Distinct officers have Hamming distance at least3. The six pairwise distances of four words would sum to at least18, but each of four binary coordinates separates at most4 pairs, giving at most16. Contradiction. This is the existing binary-code baseline mechanism.

### r=5: two officers agreeing in three coordinates

Values a,b each carry one officer. In every other coordinate each must avoid the five active values, hence both take the sole inactive value. They agree in three coordinates, contradicting the officer code's minimum distance3. This is also an existing baseline mechanism.

## 3. A single module with r=6

There are no officers on the two coordinate1 values a,b, since their deficits are6. The module's twelve unit qubit vectors alternate along a common pair of orthogonal rays. One2×2 unitary on span{|a⟩,|b⟩} makes each vector a singleton of modulus1. The other24 officers are unaffected. The result has36 officers and no other entries, yielding a pair of orthogonal Latin squares of order6, contrary to Tarry.

For every original two-party set P this local unitary preserves its exact marginal condition: it conjugates ρ_P if party1∈P, and does not change ρ_P if party1∉P because party1 is traced out. Hence this reduction preserves all six AME conditions, not merely one-body mixing.

## 4. Two modules with r=3: a direct classical pigeonhole contradiction

This is the new shorter endgame that also simplifies the earlier binary profile proof. It works whether the two coordinate1 pairs coincide, overlap in one value, or are disjoint.

The modules partition each of the thin coordinates2,3,4 into two groups of size3, indexed by module membership. A module has six doubled triples on its three3-element alphabets. Their pair-projection graph on either of its coordinate pairs has2-regular degree and therefore six hole edges among its nine within-group pair-lines.

For any fixed pair of coordinates among2,3,4:

- the two same-module3×3 grids contain18 within-group pair-lines altogether;
- the two modules occupy12 of them as hole lines (six each);
- exactly the remaining6 within-group pair-lines carry officers, one each.

Thus, summed over the three pairs among coordinates2,3,4, the number of officer incidences with a within-group pair is exactly3·6=18. On the other hand, h=12 so t=24. Every officer's three coordinates2,3,4 have only two module labels; by pigeonhole at least one pair has equal module labels. Every officer therefore contributes at least1 to that same count, forcing it to be at least24. Contradiction18<24.

No phase equality, simultaneous rotation, numerical bound, or first-coordinate pair assumption is used in this case.

All possible module-size partitions are impossible, proving the candidate theorem. ∎

## Scope, verification and exact remaining obstruction

The theorem is restricted only by e=0 and the explicitly stated three-thin-axis condition. It is valid for arbitrary complex amplitudes and arbitrary product ONBs satisfying those hypotheses, but it does not justify assuming those hypotheses for an unrestricted minimizer.

This proof checks every qubit shadow's six two-party marginals and the local-unitary preservation of every original marginal. It uses no executable arithmetic, enumeration, SAT result or old finite lower-bound certificate. Complete parent plus separate written reconstruction is pending; no formal/kernel, human or independent-model review is claimed. Priority remains unclear; the2×2 linearization and the three small officer obstructions have known provenance.

For support48, e=0, the surviving strata must have **at least two coordinates containing a value of deficit≥3**, and must also satisfy the pointwise four-thin exclusion and incidence inequality in the pinned structural candidate. Closing those two-/three-/four-thick-axis cases, together with every required e>0 stratum, is the exact remaining bridge to lower49. This manuscript does not claim their exclusion or an exact lower-support state.
