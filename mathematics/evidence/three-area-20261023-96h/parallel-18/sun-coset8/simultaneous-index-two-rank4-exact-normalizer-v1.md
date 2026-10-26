# Rank-four global refinement: exact C2^4 normalizer quotient and only three necessary support patterns

MathSun8 / math-6. Actual pre-write clock: **Sun Oct 25 04:33:51 PDT 2026** (`/bin/date`). **NEW WRITTEN-ONLY candidate.** This continuation was performed AFTER delivering the assigned v29-B review. No scientific eval/interpreter, finite enumeration, symbolic program or certificate replay was used. Metadata only; the HOLD correction remains binding.

## 1. New consequential endpoint

This is an additive successor, not an edit, to:

- `simultaneous-index-two-character-bound-v1.md`, SHA `a87846a5ecaeaa37427a0c13f6cf51276b2418429aab1b671acf8cdfa17ab9dd` (**N2**).
- `simultaneous-index-two-rank4-quartic-action-v1.md`, SHA `d34929a2e6abd1e5a50f08e3531e25e0de7ba6f7f2f782cd48766a1331cfee36` (**Q4**).

Both are NEW written candidates, not inherited acceptances. Their WRITTEN proofs, including classical Sun3/Sun4 imports, are the explicit mathematical hypotheses here. No historical parity/certificate output is used as a premise. Read with `resumption-hold-correction-addendum-v1.md` and parent erratumv7.

> **Theorem R4-NORMALIZER.** In an actual minimum-sum P7 witness, if the normalizer quotient Q=N_G(U_i)/U_i has an elementary abelian2 subgroup E of rank four, then **Q=E is exactly C2^4**. It is not merely a quotient of bounded2-rank, or a group with a V4/D8 quartic image. Every normalizer collider is the private-three owner e with beta_e=1 or one of exactly three/four beta-three neighbours. All other original cosets avoid the entire normalizer. Up to a linear coordinate change and relabeling C neighbours, their simultaneous collision supports are one of the THREE explicit necessary patterns in §5.

The argument constructs a genuine source-preserving enlargement whenever an extra subgroup remains in the common blind region. It thereby eliminates ALL larger/non-elementary rank-four normalizer quotients, including the D8 quartic alternative. It does not eliminate the three C2^4 patterns or produce actual original subgroup/fibre data realizing them.

## 2. Precise premises imported from N2/Q4

Work in a finite G with eight original pairwise-disjoint LEFT cosets and indices7r_j, private cofactors pairwise coprime. Choose an ACTUAL witness minimizing sum r_j in this fixed G; no simple-group classification is used below.

Normalize the even-private vertex to U. N2 proves7|[G:N] for N=N_G(U), Q=N/U has order dividing r_i, and every normalizer collider j has an actual quotient coset X_j=x_j H_j avoiding1, with

    b_j=[U:U∩U_j]=r_j beta_j,
    beta_j∈{1,2,3},
    c_j=[Q:H_j]≥2, beta_j*c_j≤7.

These are ACTUAL projected intersections, common to every overgroup of U. For any subgroup L≤Q, not just an order-two subgroup, its preimage pi^-1(L) meets the original j coset iff L meets X_j.

The rank-four E slice in a minimum witness has, by N2's written affine lemma and equality case:

- exactly one beta-one support, belonging to the other private-three owner e, with codimension-two E intersection;
- no beta-two E supports;
- three or four beta-three supports whose characters have rank three on E.

Let chi:Q→F2^3 be given by three independent present C characters and K=ker chi. N2's global character rank bound makes their span the entire C-character span, not merely an E-restricted subspace. In particular E maps onto F2^3 and E∩K is a line. Write z for its nonidentity point.

Q4 proves

    z∈X_e, X_e=zH_e,
    [Q:H_e]=4,
    chi(H_e)=S is a plane,
    M=K H_e=chi^-1(S), [Q:M]=[M:H_e]=2.

The odd-degree5/7 alternatives have already been excluded there. This successor uses these exact statements, not Q4's unexcluded D8 conclusion as a hidden assumption.

## 3. No extra normalizer colliders can hide outside E

This is the first new global step. The old rank-four profile counted only the supports meeting E; hidden supports elsewhere in Q must be ruled out before a global blind subgroup is usable.

### 3.1 No additional beta-one support

Every beta-one neighbour other than e lacks private3, because the private cofactors are pairwise coprime. Its actual U-fibre index is therefore coprime to that of EACH C neighbour. Consequently its quotient support must be disjoint from every negative C halfspace. Since the selected C characters span the whole C space, such a support X_j would lie entirely in K.

A nonempty coset x_jH_j contained in K has x_j∈K and H_j≤K. Hence

    [Q:H_j]≥[Q:K]=8.

But beta_j=1 and beta_j*c_j≤7 give c_j≤7. Contradiction. Thus e is the ONLY beta-one collider in the ENTIRE normalizer, not just in E.

### 3.2 No beta-two support

Since3|r_e and |Q| divides the coprime private r_i,3 does not divide |Q|. For beta two the only permitted quotient indices were two or three, so c_j=2. Its support is therefore a negative halfspace of a nonzero Q→C2 character.

This neighbour is not the private-three owner (already e), so its fibre index is coprime to every C fibre index. Its negative halfspace would have to be disjoint from each C negative halfspace. But two nonzero binary characters ALWAYS have a simultaneous negative point: if equal this is immediate; if distinct their map onto C2^2 is surjective. Contradiction. Thus there are no beta-two colliders anywhere in N.

### 3.3 Every global C support is already visible on E

All C characters belong to the three-dimensional global span selected above, and its restriction to E has the same rank three. No nonzero C character in that span vanishes on E. Thus every C support meets E; N2's global bound allows exactly the three or four already identified. No extra original neighbour is hidden elsewhere.

Therefore the COMPLETE normalizer collision family is

    I_N={e} union C,

with |C| equal to three or four. At least two of the other seven original cosets avoid the entire normalizer. This conclusion is not an assumption that their quotient supports were nonempty or an enumeration of a selected E.

## 4. A genuine source-preserving enlargement kills the residual subgroup

Set

    L=K∩H_e≤Q.

It is a subgroup. It avoids every C support since L≤K. It avoids X_e=zH_e since L≤H_e while z∉H_e. By §3 there are NO other normalizer colliders. Hence L misses EVERY projected original neighbour.

Its actual preimage

    U'=pi^-1(L), U≤U'≤N,

is therefore disjoint, as a LEFT coset after undoing the original common translation, from all seven other original cosets. This is exact source geometry: the old cosets are all retained, none is deleted or replaced by a fibre-capacity assignment.

If L were nontrivial, [U':U]=|L|>1 would divide |Q| and hence r_i. The new index is still7 times the actual divisor r_i/|L|, and stays pairwise-gcd-seven with all other original indices. Replacing U by this ACTUAL collision-free overgroup would preserve P7 and strictly lower sum r_j. That contradicts the chosen minimum. Consequently

    L=1.

From M=KH_e and [M:H_e]=2,

    [K:K∩H_e]=2.

Since [Q:K]=8, it follows that [Q:L]=16. Thus |Q|=16. But E≤Q already has order16, so

    Q=E≅C2^4.

This eliminates the D8 quartic-action branch without an additional solver, Cauchy/Sylow search or finite-group catalogue. More generally it eliminates every larger group whose rank-four slice had passed the earlier local necessary constraints. The only surviving normalizer quotient in that stratum is the actual elementary abelian order16 group.

This is a SOURCE-PRESERVING conclusion. The proof does not need the older coprime-to210 enlargement criterion, and does not silently strip a private prime from an arithmetic index: U' is constructed as the preimage of the actual common blind subgroup L.

## 5. Exactly three necessary support patterns, proved symbolically

Now Q itself is the four-dimensional binary vector space. Its C characters span three dimensions. H_e has index four and contains no z; its coset contains z. Therefore it can be written

    H_e={eta=0, psi=0},
    X_e={eta=0, psi=1},

where eta is the nonzero character defining M and psi is independent of the three-dimensional C span. Indeed psi(z)=1 while every C-span character vanishes on z. Choose the global coordinate basis a,b,c,psi as follows.

### Pattern I: three C neighbours, single-character exclusion

The C supports are

    {a=1}, {b=1}, {c=1},

and

    X_e={c=0, psi=1}.

Q4's odd-relation condition permits any single one of a,b,c; relabeling makes it c. The e support is globally disjoint from that C neighbour. At c=0 at most two C supports occur, so adding e gives at most three. At c=1 e is absent and the C multiplicity is at most three.

### Pattern II: three C neighbours, triple-character exclusion

The same three C supports occur, but

    X_e={a+b+c=0, psi=1}.

On e's support the number of negative C characters is even, hence zero or two; total multiplicity is at most three. Away from e, C multiplicity is at most three.

These are the only three-C alternatives: the nonzero eta must take value1 on the triple-negative image111, so eta is a single character or their triple sum.

### Pattern III: four C neighbours and one circuit

After a basis change the C characters are

    a,b,c,a+b,

and Q4 forces

    X_e={c=0, psi=1}.

The three-member circuit a,b,a+b has multiplicity zero or two at every point. When c=0, adding e raises this by at most one; when c=1 e is absent and c raises it by one. Thus again total multiplicity is at most three.

This is the only rank-three/four-C alternative by the written character-count proof: relative to three independent present characters, the only possible fourth is a pair sum. No duplicates or triple-sum extra can occur. Avoidance of all three-negative image points makes eta the unique character outside that circuit.

In EVERY pattern, if any C coordinate is nonzero at least one C collision occurs. If all three C coordinates are zero, the only nonzero group element is z with psi=1, and it lies in X_e. Hence every one of the fifteen actual index-two overgroups is collisionful, with multiplicity at most three. This is a direct symbolic check using binary character equations, not an executed fifteen-point enumeration.

The patterns describe ACTUAL necessary quotient cosets if a minimum P7 witness exists. They do not supply the original U_j or the compatible U-fibre cosets. The fibre index of e is r_e with3|r_e; each C fibre index is3r_j. At triple collisions these have pairwise gcd exactly three, the allowed Sun3 threshold. That explains why the old local capacity theorem does not itself contradict these three surviving patterns.

## 6. Sharpened exact frontier and assurance

The rank-four global barrier has been reduced from an arbitrary normalizer quotient with2-rank four to exactly Q=C2^4 and the three necessary support patterns above. Every larger/non-elementary quotient in that stratum admits an explicit source-preserving enlargement through L and is excluded in a minimum witness.

Still open: prove that none of these THREE quotient patterns lifts to the ACTUAL eight original subgroups/cosets with their private indices and all fibres, or produce such data; control all normalizer quotients of2-rank at most three; handle maximal/self-normalizing vertices; and resolve the unrestricted simple-P7/Sun8 problem. No actual eight-coset certificate, Sun8 solution, maximal-subgroup classification, novelty or formal/kernel/cross-vendor/human assurance is claimed.

This successor requires separate written reconstruction with N2 and Q4. The v29-F frozen assignment to N2 alone does not automatically cover this new theorem. Its substantive source-preserving step and global no-hidden-collider argument must be reviewed as new mathematics. No previous unadmitted computation supplies that review.
