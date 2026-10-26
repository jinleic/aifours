# Rank-two completion as a canonical half-design, with literal Gold S profiles

Owner: InfoBalancedNL242, slot info-6. Actual observed clock before the accompanying literal evidence was frozen: `Sun Oct 25 04:05:00 PDT 2026`.

**Status:** the universal reduction below is **WRITTEN**. The two explicit finite profiles and the listed transform identities are **WRITTEN-checked-in-kernel**, using integer/F2/F3 arithmetic in the owner's evaluation kernel. Neither label means proof-assistant/kernel verification. Independent review was **not performed**. No full (S),(R),(N) solution, whole-case exclusion, NL242 table, novelty clearance, or change to the seven-entire-types frontier is claimed.

This successor preserves every earlier packet. It attacks (16,24) first, then identifies the exact shared barrier for all three necessary cases. It does not replace the missing universal result by a restricted search result.

## 1. Retained inputs and what is new

Retain the unpruned (S),(R),(N) system and definitions in `rank2-two-spectrum-completion-v1.md`, SHA-256 `2a0d363458746f20e9c226db71c8460869386ebc95381fc6c62e51dca8612f6e`. In particular:

- H is the unnormalized Walsh matrix on G=F2^8, with H²=256I.
- W is a six-dimensional linear space, D=1−1_W, chi=1−2D, U=W-perp, q=2e0−1_U.
- phi(z) is the representative of z modulo3 in {−1,0,1}.
- For a ternary delta, define b=phi(Hdelta), E={x in U:b(x)=−q(x)}, P=H(q1_E), C=Hb, and **B=phi(q−b)=q−b−3q1_E**. These arrays are never chosen independently.
- The complete S condition is C+3P=4delta on supp(delta), and |C+3P|=12 elsewhere. Its resulting spectrum is S=2HB.
- The retained parent-supported pruning is E empty and the three necessary count cases (L,u)=(16,24),(16,32),(20,24). This is not an existence assertion.

New contributions:

1. An exact elimination of beta, the norm equation, and the second Boolean sign: completion of **any unpruned S-consistent delta** is equivalent to a prescribed-XOR half-subset of T={B=0} satisfying 256 integer discrepancy slabs. This is not limited to the three pruned cases.
2. A direct 512-bit reconstruction in those subset coordinates, retaining every coefficient and both Boolean transforms.
3. Literal full-affine-rank S profiles for both L16 count branches. Both also have balanced canonical S+N/both-Boolean completions; those completions fail R and are not witnesses.
4. Exact exclusion of one frozen outer-R profile, and a quotient-parity constraint on all possible R completions of each displayed S profile.

## 2. Universal completion theorem: one half-subset instead of two ternary arrays

Fix any delta satisfying the **unpruned** S condition above; no assumption E empty is made in this section. Let

    T={x:B(x)=0},       n=|T|,
    H_v={x:v dot x=1},  M_v=|T intersect H_v|.

Write the quadratic D in the chosen eight-coordinate basis as

    D(v)=sum_i d_i v_i + sum_{i<j} d_ij v_i v_j over F2,

with d_i=D(e_i), since D(0)=0. Define the required XOR vector ell by

    ell_i = M_(e_i)/2 + d_i modulo2.                 (10)

The divisions by2 in this definition and below are integral.

**Theorem HD (WRITTEN).** This delta extends to a solution of the complete original (S),(R),(N) system if and only if there is a subset V of T such that

    |V|=n/2,                                         (11)
    XOR of the eight-bit indices in V = ell,          (12)
    | |V intersect H_v| − M_v/2 | <=3 for every v.     (13)

No beta coordinates or signs have been discarded: beta is recovered in the proof. Conditions (11)–(13) quantify over every half-subset, not only polynomial signs or a fixed placement. In particular the three cases have respectively n=118,116,118, and require half-subsets of sizes59,58,59.

### 2.1 Why the required moments of T are automatic

S self-consistency gives S=4+8D modulo16, so

    HB=2+4D modulo8.                                 (14)

For any integer f, the character expansion modulo8 is

    Hf(v)=sum_x f(x)
      −2 sum_i v_i sum_x f(x)x_i
      +4 sum_(i<j) v_i v_j sum_x f(x)x_i x_j mod8.

Terms of degree at least3 have a factor8. Comparing this expansion for B with (14) gives

    sum B =2 mod8,
    sum_x B(x)x_i =−2d_i mod4,
    sum_x B(x)x_i x_j =d_ij mod2.                    (15)

Because B is ternary, B and 1_(supp B) agree modulo2. The corresponding first and second moments of all256 points are even. Therefore

    n is even,
    M_(e_i) is even for each i,
    sum_(x in T) x_i x_j =d_ij mod2.                 (16)

Thus XOR(T)=0 and every M_v is even. These facts follow from the full integer S lift, not a separately selected support profile.

### 2.2 From a half-subset to R, N and both Boolean transforms

For V satisfying (11), put

    a(x)=1−2*1_V(x) on T, and a(x)=0 off T,
    p(v)=|V intersect H_v|−M_v/2.                    (17)

The half-size condition gives sum a=0, and direct expansion yields

    Ha(v)=4p(v).                                     (18)

In particular p(0)=0. Expanding (18) modulo8, its quadratic coefficients after division by4 are d_ij by (16); its linear coefficients are

    −M_(e_i)/2 + |V intersect H_(e_i)| mod2.

Condition (12), with (10), makes these exactly d_i. Hence

    p modulo2 =D.                                    (19)

Consequently (13) is precisely p in {0,+2,−2} on W and p in {+1,−1,+3,−3} off W. Define beta=phi(p). From (18), Hp=64a, and hence

    phi(Hbeta)=phi(Hp)=a,

since64=1 modulo3 and a is ternary. Thus C_R=Ha=4p, which is exactly **all** of (R): on W it equals −8beta; off W at beta!=0 it equals4beta; at beta=0 its magnitude is12; and beta(0)=0.

By construction a²+B²=1 as an exact integer identity: a has support T and B has its complement. The existing convolution proof in the retained packet therefore gives (N), without replacing its integer norm step by a congruence relaxation. The correction −3q1_E remains present in B throughout.

Finally G=B+a and J=B−a are both Boolean signs. Set

    K_1=H(G), K_2=H(J),
    R=K_1−K_2=2Ha=8p, S=K_1+K_2=2HB.

Then HK_i is pointwise ±256, both K_i are2 modulo8 by (14),(19), and max(|S|,|R|)<=28. The identity |K_1|+|K_2|=max(|S|,|R|) recovers the canonical cap.

### 2.3 Converse, with the original beta retained

Given any full (S),(R),(N) solution, set a=phi(Hbeta) as before. N supplies the integer equality a²+B²=1, so a is exactly a choice of signs on T. Let V={x:a(x)=−1}. R gives p=Ha/4, p(0)=0, p modulo2=D and |p|<=3. Its actual zero forces |V|=n/2. Equation (18) and the linear coefficient comparison prove (12), and the bound gives (13). Thus no genuine solution is lost and no extra solution is introduced.

This proves Theorem HD at the written level.

## 3. The complete512-bit map in half-design coordinates

Index the ninth bit last, so the first256 entries have last bit0. The reconstruction is especially simple:

    x in T:      F(x,0)=F(x,1)=1_V(x),
    x not in T:  F(x,0)=(1−B(x))/2,
                 F(x,1)=(1+B(x))/2.                 (20)

Both entries outside T are literal complementary bits. Its weight is

    2|V|+(256−n)=256,

so no truth-table half is fixed and balance is intrinsic. The **entire** Walsh spectrum consists of

    last frequency bit0: 8p(v),
    last frequency bit1: 2HB(v).                     (21)

Thus the discrepancy cap in (13) is the entire remaining R-sector requirement, not a proxy for only some coefficients. The map itself still is not a witness unless an S-consistent delta and an admissible V are supplied together.

## 4. Explicit algebraic S profile at the first case

Use F16=F2[X]/(X^4+X+1), with the polynomial-basis integer encoding0..15. Write an eight-bit index as x=t+16y, t,y in F16. Define

    delta_24(t,y)=−(−1)^(t_0 t_1) if y=t^3, else0.

The sixteen values of t^3, in order t=0..15, are

    0,1,8,15,12,10,1,1,10,15,15,12,8,10,8,12.

Take U={0,4,8,12}; hence W={x:x_2=x_3=0} and D=x_2+x_3+x_2x_3. The literal profile contains every entry of delta,b,C,q,B,S,T, not only their histograms.

The following are exact in-kernel integer checks:

- |supp(delta)|=16, and the augmented matrix of its points has rank9 over F2: its affine rank is8.
- Hdelta has histogram: −8:30, −4:60, 0:120, +4:36, +8:10.
- b=phi(Hdelta) has weight136.
- C=Hb equals4delta on all16 support points, and is−12 at108 off-support points and+12 at132 off-support points. Therefore the **complete S identity** holds.
- b restricted to U is (1,0,0,0); q restricted to U is (1,−1,−1,−1). Thus E is empty, alpha=1, B is ternary, wt(B)=138, and |T|=118.
- S=2HB has signed histogram: −28:33, −20:99, −12:1, −4:3, +4:3, +12:9, +20:27, +28:81. In particular its cap and all sixteen S defects are genuine.

These are actual shared-coordinate S arrays, not a scalar feasibility row. **They are not a solution of (R),(N).** The parameter u=24 is only the value that would follow from wt(a)=118 **if** an R-admissible completion existed; no actual u=24 function is being asserted.

### 4.1 Exact S+N/both-Boolean completion, but R fails

For transparency, take the first59 entries of sorted T, remove5, and add117. Call this subset V_24. It has size59 and XOR0. Here the first coordinate counts M_(e_i) are

    56,64,62,62,72,72,72,48,

and ell=0. Thus V_24 satisfies the balance and canonical XOR requirements.

Construct a,p,beta and the512 bits by (17),(20). Exact direct checks give:

- a=phi(Hbeta) on all256 coordinates.
- The original convolution N vanishes modulo3 at **all256 shifts**, computed directly with XOR convolution rather than inferred only from a histogram.
- a²+B²=1 pointwise; both inverse Boolean signs are genuine; both canonical spectra are2 modulo8.
- F has weight256, and its complete512-entry Walsh transform is exactly (8p,S).
- Off W, p has histogram −3:24, −1:84, +1:72, +3:12, so the entire outer R alphabet is legal.
- On W, p has histogram −24:1, −10:4, −2:12, 0:21, +2:24, +12:2. R fails at precisely the seven positions

        16:−10, 32:−10, 64:−10, 96:+12,
        128:−24, 224:+12, 240:−10.

This table is deliberately an **inadmissible control**, not an NL242 function. Its peak Walsh magnitude is192, not28. Its actual z+2c is333, **not24**: the formula u=4(124−wt(a)) is unavailable when |p|<=3 fails. Keeping that distinction prevents a count-case row from becoming a false witness.

### 4.2 The frozen outer profile cannot be repaired just on W

There are two complete written exclusions of this exact outer p profile, not of all possible outer profiles.

First, every sign choice a on this fixed T has sum p²=16|T|=1888. The displayed outer p values have squared sum480. If the W cap held, its64 entries could contribute at most64*4=256. But480+256<1888. Hence **no completion preserving those192 outer p values can satisfy R**.

Second, preserving all Walsh values off W makes the difference a'−a periodic on U-cosets. A partially occupied T-coset contains a forced zero, so its entire difference is zero. Only the twelve full T-cosets can change. All are constant in the displayed a. Their bases and initial signs are:

    negative: 34,35,48,50,65,66,82,83;
    positive: 176,178,209,210.

Changing a full coset flips its four signs. Balance requires equally many negative and positive cosets flipped, say k of each, with0<=k<=4. At frequency128 every such flip increases p by2. Therefore

    p'(128)=−24+4k <=−8,

which violates the W cap. This exhausts **every** same-outer-profile sign completion, not just a selected list of flips.

The mathematical escape route is explicit: any successful half-design for this S profile must alter the outer R profile itself, while retaining all192 discrepancy slabs. The frozen control does not justify rejecting those alternatives.

## 5. Second explicit S profile: the L16/alpha0 branch

Set

    delta_32(t,y)=−(−1)^(t_0 t_1+t_2) if y=t^3, else0,
    U={0,1,2,3}, W={x:x_0=x_1=0}, D=x_0+x_1+x_0x_1.

This is a character modulation of the first signed support. It retains affine rank8 and the full S identity. Now b is zero at all four U positions, so E is empty, alpha=0, wt(B)=140, and |T|=116. Thus the S-side count data for (16,32) are also realizable in actual coordinates.

A canonical balanced S+N control is obtained by taking the first58 sorted T points, removing8 and10, and adding253 and254. Its XOR is0; the required ell also is0. The direct integer norm, original N at all256 shifts, both Boolean inverse signs, and complete512-bit map all check exactly. Its p peak is22 and it fails R at twelve positions. Its actual z+2c is319, not32. These literal bytes are supplied only to show that S, N, balance and Boolean reconstruction together do not solve the cap problem.

## 6. A further quotient restriction for every R completion of these S profiles

This restriction does not fix the outer p profile. Partition G into64 U-cosets and put

    s(c)=sum_(x in c) a(x),  m(c)=|T intersect c|.

For every possible sign completion, s(c)=m(c) modulo2 and |s(c)|<=m(c). On W the transform Ha is the64-point Walsh transform of s. If R holds there, Ha is0 or±8. Parseval consequently gives

    #{v in W:p(v)!=0}=sum_c s(c)^2,
    z=64−sum_c s(c)^2,
    z=64−#{c:m(c) odd} modulo4.                      (22)

The last step uses odd squares=1 modulo4 and even squares=0 modulo4.

For the first S profile the occupancy histogram m=0,1,2,3,4 is respectively24,1,12,15,12; there are16 odd cosets. For the second it is26,0,6,24,8; there are24 odd cosets. Hence **every genuine R completion of either displayed S profile has z divisible by4**.

For the first profile, compose this with the retained R theorem u>=24, c>=2, the outer parity rule and the provisional u=24 forced by its T size. The only remaining zero/count pairs are

    (z,c)=(8,8),(12,6),(16,4).

The z=20,c=2 alternative puts two points in only one outer coset and violates the retained two-outer-coset support requirement. This is a necessary restriction for this explicit S profile, not an assertion that one of those three profiles exists and not a classification of all L16 supports.

## 7. Per-case written verdicts and the exact remaining barrier

| Necessary case | New exact scope | Verdict |
|---|---|---|
| (16,24) | A literal affine-rank8 delta has the full S identity, E empty, alpha1 and T118. A balanced canonical S+N control and its512-bit map are supplied. One complete outer p profile is excluded by exact energy and full-coset arguments. All actual R completions of this delta require z in {8,12,16}. | **UNRESOLVED.** No59-point prescribed-XOR half-design satisfying all256 slabs has been constructed or excluded for this T, much less every S-consistent T118. |
| (16,32) | A second literal full-rank S profile has alpha0 and T116; balanced canonical S+N controls exist but fail R. Every R completion of this explicit delta has z divisible by4. | **UNRESOLVED.** The exact58-point half-design problem on T116 remains. |
| (20,24) | Theorem HD reduces every S-consistent profile to the same59-point discrepancy problem on its own T118. | **UNRESOLVED.** No L20 S profile or universal S exclusion is supplied, and no universal half-design obstruction is proved. |

The replacement for the old two-ternary-array barrier is now concrete:

**HD-U2:** For every delta satisfying the **unpruned** integer S condition (with B and E defined from that same delta), the zero support T of B has no half-subset with XOR ell and discrepancies at most3 in every linear half-space.

Theorem HD proves HD-U2 equivalent to U2. After the retained pruning it is enough, and still necessary, to handle precisely the three rows above. The fixed Gold profiles prove that a contradiction in S alone cannot eliminate either L16 count branch. Their S+N controls prove that Boolean reconstruction and N alone do not supply the R cap. The missing result is a universal discrepancy obstruction, or a full admissible half-design; it is not a runtime framework, a missing coefficient map, or a request for a solver launch.

## 8. Exact computation disclosure and evidence pins

The immutable literal certificate is `rank2-half-design-literal-profiles-v1.json`, SHA-256 `95f72b0484168159c4d67dd1df872ce2b4bf1f9cf9ac109311cb4aa2948b7e6d`. It contains every256-entry array, both512-bit maps, selected subsets, actual R failures, U-coset data and individual check booleans. Integers alone were used; no floats or approximate status was accepted. The Walsh routine was first checked on a known8-entry identity H²f=8f; phi was checked on −3..3 before evaluating the candidates.

Other explicitly bounded in-kernel algebraic attempts were made and are recorded without universal proof credit: all64 homogeneous quadratic signs on this single Gold graph (48 satisfy S), a fixed407-member quadratic sign-lift family, and101 eligible character switches on coordinate affine3-flats (no L20 S profile). A simple fourth-moment congruence/lower bound on the two displayed T supports was also evaluated and gave no contradiction. These restricted checks are **not** a classification of L16, L20, all signs, all placements, or U2. They are not the claimed advance; the exact universal elimination and literal common-coordinate profiles are.

Retained parent pins, freshly observed in this resumption:

- `wave-v19-nl242-completion-parent-v1.md`: `8783a156c3fa4a15f3cb5730d1e28f601e2e977c47b1dcbd856baf63548d7f08`.
- `nl242-rank2-spatial-parent-v1.md`: `238fec41811d8d248b853bd195c0c130f936c6ad2e614554f6a9b8c50a222e13`.
- `nl242-spatial-equality-parent-v1.md`: `157a3e74f2fc5e19ad5f4330a512edc4303db66b78bfb5404116f28edebad7f6`.

All bodies requested for this assignment were read; the source packet's previously truncated bent-degree line was also read raw. The round README, scientific-admission-hold-v2, parent-evidence-erratum-v6 and checkpoint026 were consumed before this work. All historical written imports keep their named assurance boundaries. No native scientific program, background job, scientific GO, external-model CLI, nested subagent, Git mutation, publication or other-owner write was performed. New work remains owner-written and in-kernel finite arithmetic only. Universal U2 and balanced NL242 remain unproved.
