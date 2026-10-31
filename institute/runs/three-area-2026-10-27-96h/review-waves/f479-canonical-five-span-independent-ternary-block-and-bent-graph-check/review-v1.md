# F479 FINITE — canonical graph classification and physical ternary lift

**Status: WRITTEN_DERIVED; INDEPENDENT_CHECKER_NOT_RUN. No automatic adoption.**

Complete returned artifacts:
- [Full independent checker source — NOT_RUN](local://f479-independent-finite-checker-NOT_RUN.py)
- [Full author body](local://f479-author-candidate-v1.md)
- [Prebody acknowledgement](local://f479-finite-prebody-ack-v1.md)

## 1. Read and execution provenance

The complete manifest, receipt, dispatch receipt, parent metadata supply and all ten controls were read before the prebody acknowledgement. The literal packet was then read in ordered, contiguous RAW chunks **1–20, 21–40, 41–60, 61–80, 81–100, 101–115**. This covered **S1 LF1–76 and S2 LF1–37 completely, including endings**.

No linked parent checker, sibling mathematical return, held scientific payload, external source or excluded source-follow was opened. Quarantine controls were used only for status and permissions.

The supplied pins are:

- Manifest: `ae070cb7ddae24abc0b15a99df4b9aea0ad6828176b4e09dd17e21371555b081`
- Receipt: `d9392be50f3be01fe80a19cff42b5cc406f2f884f1d76281050765ed4e13f171`
- Packet: `16cc34893b529296f5b2c950723e30f4818ccebb9df439757da16937f9ebb046`

These are **parent-supplied metadata**, not child-native hash observations. The supplied `2026-10-30T12:13:16-0700 PDT` observation belongs to the parent. No child-native clock or source hash is claimed.

The higher-priority read-only review runtime prohibits scientific Bash execution. Consequently, **no scientific executable or execution workaround was run**. This uses the frozen assignment’s explicit constrained-role **NOT_RUN** fallback. There is no observed execution time, exit status, finite census, mutation-rejection receipt or executable acceptance.

### Complete source and argv

The complete independently authored standard-library source is returned in the source artifact above: **14,279 bytes**, as reported by the write tool. It is not an excerpt or stub, and no parent code was inspected.

Invocation specification:

- `argv[0]`: `python3`, Python ≥3.10
- `argv[1]`: `-B`
- `argv[2]`: `-c`
- `argv[3]`: the complete UTF-8 contents of the returned source artifact
- Additional inputs: none

The source contains no explicit file I/O, network, child process, randomness, installation or external dependency. It has a **50-second cooperative deadline** and returns `INCOMPLETE_BUDGET`, not `VALID`, on expiry. Actual wall time is unmeasured. The source was not syntax-checked, executed or child-hashed.

## 2. Independent written census — not observed stdout

Use variables \(x=(j_0,j_1,b_0,b_1)\), truth-table index \(j+4b\), and
\[
q=1+b_0b_1.
\]

### All four-variable bent functions are quadratic

For a bent truth function \(t\), its sign sum on a coordinate hyperplane is
\[
\frac{W_t(0)\pm W_t(e_i)}2\in\{-4,0,4\}.
\]
Its number of ones on that eight-point hyperplane is therefore even. Its full truth-table weight is six or ten, also even. The corresponding ANF parity identities eliminate every degree-three and degree-four coefficient. Thus every four-variable bent function is quadratic.

For quadratic coefficients \((a,b,c,d,e,k)\) on edges
\[
(01,02,03,12,13,23),
\]
the alternating polar form is nonsingular precisely when
\[
P=ak+be+cd=1
\]
over \(\mathbb F_2\). Squaring the quadratic Walsh transform and summing its derivative characters shows that nonsingularity is equivalent to constant Walsh magnitude four.

There are
\[
7\cdot4=28
\]
nonsingular forms: choose nonzero \((a,b,c)\), then one of four \((k,e,d)\) having dot product one. Each form has \(2^5=32\) affine additions. Hence there are exactly
\[
28\cdot32=\boxed{896}
\]
bent truth functions.

### Canonical graph ranks

For \(f=t+q\), toggling edge \(23\) changes the Pfaffian to
\[
P+a=1+a.
\]

Among the 28 nonsingular forms of \(t\):

- \(a=1\): sixteen choices, producing rank-two \(f\);
- \(a=0\): twelve choices, producing rank-four \(f\).

Therefore the labeled graph counts are:

| Property | Exact written count |
|---|---:|
| Admissible graph functions \(f\) | 896 |
| Rank-two polar form | 512 |
| Rank-four polar form | 384 |

No such \(f\) is affine: otherwise \(f+q\) would have rank two and would not be bent. Its graph consequently spans the affine five-flat, rather than an affine four-flat.

### Common phases

For a fixed nonzero graph polar form \(F\), the shared-phase condition is
\[
P(R)=P(R+F)=1.
\]

An alternating change of basis reduces:

- rank-two \(F\) to edge \(01\), imposing \(k_R=0\);
- rank-four \(F\) to edges \(01+23\), imposing \(a_R+k_R=1\).

In either case the residual equation is
\[
be+cd=1,
\]
with six choices, together with one free binary coefficient. Thus there are twelve admissible polar forms \(R\), each with 32 affine additions:
\[
\boxed{384\text{ common phases per graph}}.
\]

The resulting labeled pair count is
\[
896\cdot384=\boxed{344064}.
\]

These are fixed-coordinate counts, **not equivalence-class counts or original-caller counts**.

### Executable coverage supplied

The unexecuted source is programmed to:

- enumerate all 65,536 Boolean truth functions;
- compare direct Hamming-distance Walsh values with butterfly transforms;
- independently compute and evaluate ANF;
- check the bent/degree/rank classification;
- construct all 896 actual 64-position \(g\) arrays;
- check the named small positions, their positive signs and the complete signed Fourier identity;
- exhaust all 802,816 ordered bent-phase comparisons;
- verify 384 common phases for every graph.

It directly checks a full 64-position \(a\) spectrum for one admitted phase per graph and for the explicit phase below. It **does not directly enumerate all 344,064 physical \(a\) arrays**; coverage of every phase is supplied by the common-phase Fourier identity, not an invented executable claim.

## 3. Actual ternary four-point blocks

For \(w=0,1,2,3\), use
\[
\chi_1=(+,-,+,-),\quad
\chi_2=(+,+,-,-),\quad
\chi_3=(+,-,-,+).
\]

The exact local options are:

| Required \((U_1,U_2)\) | Options | Support |
|---|---:|---:|
| \((3a,g)\), each \(a,g\in\{\pm1\}\) | 2 per pair | 3 |
| \((0,\pm4)\) | 1 per sign | 4 |
| \((0,\pm2)\) | 4 per sign | 2 |
| \((0,0)\) | 9 | 0, 2 or 4 |

For the first row, delete one \(w_0\) from \(a\chi_1\), choosing
\[
\chi_3(w_0)=-ga.
\]
Then
\[
U_1=3a,\qquad U_2=-a\chi_3(w_0)=g.
\]

For \((0,\pm4)\), the unique block is \((g/4)\chi_2\), with \(U_0=0\).

For \((0,\pm2)\), choose one point from each \(\chi_3\)-sign class and place \((g/2)\chi_2\) there.

For \((0,0)\), the equations give exactly
\[
u=(s,t,t,s),\qquad s,t\in\{-1,0,1\}.
\]
There are one, four and four options of support zero, two and four respectively. Exactly **seven** satisfy local \(H=0\): exclude the two constant nonzero blocks with \(|U_0|=4\). The remaining support-four options \(\pm\chi_3\) do not violate this **local** criterion.

The source independently enumerates all 81 actual ternary blocks and compares their direct and butterfly transforms, but that enumeration remains **NOT_RUN**.

### Universal local-lift support count

For every admitted graph/phase pair, the prescribed blocks contribute
\[
16\cdot3+2\cdot4+22\cdot2=100
\]
nonzeros.

Add \((1,0,0,1)\) on any eight of the 24 zero-\(g\), zero-\(a\) blocks. This preserves both fibres and adds sixteen nonzeros:
\[
\boxed{100+8\cdot2=116}.
\]

Every \(U_1=0\) block then has \(|U_0|\le2\), except the full \(\pm\chi_2\) blocks, whose \(U_0\) is zero. Thus local \(H=0\).

Seven padded blocks would give **114**, not 116, despite preserving the two fibres and local \(H\).

## 4. Explicit full 256-entry physical \(u\)

Choose
\[
f=j_0j_1,\qquad r=j_0b_0+j_1b_1.
\]
Their truth masks are respectively `0x8888` and `0x6CA0`; \(q\) has mask `0x0FFF`. The functions \(f+q,r,r+f\) are bent.

Here \(S\) has \(h\in\{0,2,4,7\}\) for each \(d\in\{1,2,4,7\}\). On \(S\), omit the least \(w\) satisfying \(\chi_3(w)=-ga\). On the off-\(S\) support-two blocks use \((g/2,g/2,0,0)\).

The eight padded blocks, ordered by \(c=8h+d\), are
\[
(0,3),(0,5),(0,6),(1,3),(1,5),(1,6),(2,3),(2,5).
\]

**Each cell below contains all four entries \(w=0,1,2,3\). Thus the table explicitly specifies all 256 values.**

| \(h\) | \(d=0\) | \(d=1\) | \(d=2\) | \(d=3\) | \(d=4\) | \(d=5\) | \(d=6\) | \(d=7\) |
|---|---|---|---|---|---|---|---|---|
| 0 | (1,1,-1,-1) | (0,-1,1,-1) | (0,-1,1,-1) | (1,0,0,1) | (0,-1,1,-1) | (1,0,0,1) | (1,0,0,1) | (1,0,1,-1) |
| 1 | (1,1,-1,-1) | (1,1,0,0) | (1,1,0,0) | (1,0,0,1) | (1,1,0,0) | (1,0,0,1) | (1,0,0,1) | (-1,-1,0,0) |
| 2 | (-1,-1,0,0) | (0,-1,1,-1) | (-1,0,-1,1) | (1,0,0,1) | (0,-1,1,-1) | (1,0,0,1) | (0,0,0,0) | (0,1,-1,1) |
| 3 | (-1,-1,0,0) | (1,1,0,0) | (1,1,0,0) | (0,0,0,0) | (1,1,0,0) | (0,0,0,0) | (0,0,0,0) | (-1,-1,0,0) |
| 4 | (-1,-1,0,0) | (0,-1,1,-1) | (0,-1,1,-1) | (0,0,0,0) | (-1,0,-1,1) | (0,0,0,0) | (0,0,0,0) | (0,1,-1,1) |
| 5 | (-1,-1,0,0) | (1,1,0,0) | (1,1,0,0) | (0,0,0,0) | (1,1,0,0) | (0,0,0,0) | (0,0,0,0) | (-1,-1,0,0) |
| 6 | (-1,-1,0,0) | (1,1,0,0) | (1,1,0,0) | (0,0,0,0) | (1,1,0,0) | (0,0,0,0) | (0,0,0,0) | (-1,-1,0,0) |
| 7 | (-1,-1,0,0) | (0,-1,1,-1) | (-1,0,-1,1) | (0,0,0,0) | (-1,0,-1,1) | (0,0,0,0) | (0,0,0,0) | (1,0,1,-1) |

## 5. Exact written Walsh evaluation

**The following are written evaluations, not captured program output.**

Write \(y=2v+y_0\), \(w(z)=(z\cdot3,z\cdot5)\), and \(z_0=z\cdot1\). For the explicit pair,
\[
\widehat a(y,z)
=4(-1)^{z_0+v\cdot w+y_0w_0w_1}.
\]

For \(g\):

- \(\widehat g(0,z)=(4,4,4,-12,4,-12,-12,-12)\) in \(z=0,\dots,7\) order;
- \(\widehat g(y,z)=12\) for nonzero even \(y\);
- for odd \(y\),
  \[
  \widehat g(y,z)=-12(-1)^{z_0+v_0v_1+w_0w_1}.
  \]

Thus the actual \(U_1\) spectrum has magnitude twelve everywhere. The actual \(U_2\) spectrum has four **positive** small coefficients precisely at
\[
(y,z)=(0,0),(0,1),(0,2),(0,4),
\]
and magnitude twelve elsewhere.

Let \(F\) indicate the two full blocks, and \(T\) the eight padded blocks. Direct four-point evaluation gives
\[
U_0=g-4F+2T,\qquad U_3=-a+2T.
\]
Furthermore,
\[
\widehat T(y,z)=
(1+(-1)^{y_0})(\chi_z(3)+\chi_z(5)+\chi_z(6))
+(-1)^{y_1}(\chi_z(3)+\chi_z(5)),
\]
where \(y_1\) is the second bit of \(y\).

The resulting complete matrices have rows \(y\) and columns \(z\):

### \(\widehat U_0\)

| \(y\backslash z\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 12 | -12 | -8 | -24 | -8 | -24 | -28 | -4 |
| 1 | -8 | -16 | -12 | 12 | -12 | 12 | 8 | 16 |
| 2 | 12 | 4 | 0 | 0 | 0 | 0 | 4 | 12 |
| 3 | -16 | -8 | -12 | 12 | -12 | 12 | 16 | 8 |
| 4 | 20 | -4 | 0 | 0 | 0 | 0 | -4 | 20 |
| 5 | -8 | -16 | -12 | 12 | -12 | 12 | 8 | 16 |
| 6 | 12 | 4 | 0 | 0 | 0 | 0 | 4 | 12 |
| 7 | 8 | 16 | 12 | -12 | 12 | -12 | -8 | -16 |

### \(\widehat U_3\)

| \(y\backslash z\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 12 | -4 | -8 | 0 | -8 | 0 | -12 | 20 |
| 1 | 0 | -8 | -4 | 4 | -4 | 4 | 0 | 8 |
| 2 | 4 | -4 | 0 | 0 | -8 | -8 | 4 | 12 |
| 3 | -8 | 8 | 4 | 4 | -4 | -4 | 0 | 0 |
| 4 | 12 | -12 | -8 | -8 | 0 | 0 | -4 | 20 |
| 5 | 0 | 0 | -4 | -4 | 4 | 4 | -8 | 8 |
| 6 | 4 | 4 | 0 | -8 | 0 | -8 | -4 | 12 |
| 7 | -8 | 0 | 4 | -4 | 4 | -4 | 8 | 0 |

Descriptive values for this actual \(u\):

- Support: **116**
- Local \(H\): **0**
- \(\sum u=12\): **not balanced**
- Positive entries: 64; negative entries: 52; zero entries: 140
- Partial energies:
  \[
  (\|U_0\|^2,\|U_1\|^2,\|U_2\|^2,\|U_3\|^2)
  =(136,144,136,48).
  \]
- Their sum is \(464=4\cdot116\).
- \(\|\widehat U_0\|^2=8704=64\cdot136\).
- \(\|\widehat U_3\|^2=3072=64\cdot48\).

These \(U_0/U_3\) values are not asserted to satisfy the original caller’s remaining constraints. The 140 zero positions do **not** construct a signed complementary \(V\).

## 6. Reason-specific negative controls supplied

The source counts a rejection only when the intended `Failure.code` is raised. An unrelated exception or different rejection reason does not count.

| Mutant | Expected reason | Targeted distinction |
|---|---|---|
| Flip first \(\rho\) sign | `RHO_ALIGNMENT` | Canonical signed geometry changes |
| Drop \(q\)’s constant term | `G_OFFSET_SIGN` | Bent magnitudes alone miss the signed odd-row error |
| At \((h,d)=(0,1)\), omit \(w=1\) instead of \(w=0\) | `U2_BLOCK` | Support and \(U_1\) preserved; \(U_2\) sign wrong |
| Remove the first nonzero entry | `SUPPORT_UNDER` | Support 115 |
| Add one entry at \((2,6,0)\) | `SUPPORT_OVER` | Support 117 |
| Use seven zero support-two blocks | `EIGHT_ZERO_TWO_BLOCKS` | Two fibres and local \(H\) unchanged, but only seven pads |
| The same seven-block object | `SUPPORT_UNDER` | Support 114 |
| Multiply actual \(u\) by \(\chi_7(d)\) | `G_SMALL_POSITIONS` | Same \(g\)-magnitude histogram and flat \(U_1\); small set moves to \(\{3,5,6,7\}\) |
| Negate the \(g\) spectrum | `G_SMALL_SIGNS` | Small locations and magnitudes preserved; signs wrong |
| Put constant ones at \((h,d)=(2,6)\) | `LOCAL_H0` | Locally \(U_1=U_2=0\), but \(U_0=4\) |

**All ten controls remain unexecuted.** Their entries above describe supplied program checks and written trigger analyses, not observed rejection receipts.

## 7. Disposition

**Findings:** None in the stated canonical two-fibre classification or local-lift construction. The written derivation independently supports those precise mathematical scopes. Independent executable verification remains **NOT_RUN**.

Not established:

- simultaneous original \(U_0/U_3\) requirements or original balance;
- named rank/eight-zero/\(T\) conditions and the remaining four-fibre system;
- a common physical complementary 140-support \(V\) or global odd Walsh caps;
- six-span branches, other m116/m114 callers or NL242;
- novelty, source equivalence, human/cross-family/kernel acceptance.

The explicit lift’s imbalance does not exclude other lift choices or the full caller.

**Overall_correctness:** correct at the stated written two-fibre/local-lift scope only.

**Explanation:** The canonical census and local ternary construction admit independent exact written derivations, with an explicit 116-support physical \(u\) whose remaining two spectra and imbalance are displayed. Scientific execution was prohibited in this role, so the complete checker and controls are returned NOT_RUN rather than represented as a successful finite replay.

**Confidence:** 0.95 for the written scoped conclusion; no executable-verification confidence assigned.