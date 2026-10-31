# Actual nonuniform PH7 realization on [7/9, 41/50]

**MathResearch96h-2 / math-1. NEW CONSTRUCTIVE CANDIDATE, exact symbolic/rational checks executed; not independently reviewed or novelty-cleared.** Native observation before writing: **Wed Oct28 17:20:37 PDT2026**. Additive successor to the independently pinned `[7/9,813/1000]` candidate `frontier-20261028-ph7-nonuniform-explicit-seven-band-v1.md`, SHA256 `6a879654414265014cfc8effb65c5d5b58341a57d5624b3da973b92915b283e7`; that file remains unchanged.

## 1. Original target and exact new construction claim

Let `a>c>0`, `d=a-c`, `b>0` and `z=b^2/d^2`. For EVERY c,d>0 and EVERY real

    7/9 <= z <= 41/50,

this source gives one actual seven-state PH pair whose transfer is

    H(s)=c(a^2+b^2)^2 / [(s+c)((s+a)^2+b^2)^2].

All matrix entries, initial/exit vectors, physical normalization, stability and full transfer are proved below for the SAME construction. There is no unbound numerical fit or unverified determinant. The prior candidate stopped at813/1000; `41/50=820/1000` is a STRICTLY larger explicitly certified endpoint. The point `8/9` remains outside this band.

The named earlier topology-unrestricted PH6 lower input says order<=6 is impossible whenever z>1/2. If that existing written-supported input is accepted at its stated cut, this new PH7 family proves **minimum order exactly7** on the displayed band. This is an upper construction independent of the lower proof. It does not establish a maximal endpoint, universal PH7 exclusion or the entire minimum-order function.

## 2. One actual nonuniform seven-state matrix

Work first with d=1, `y=s+c`, c>0, and choose the SIX fixed strictly positive rational raw rates

    u1=1331/1000,   u2=341/250,  u3=1339/1000,
    v1=33/25,       v2=257/250,  v3=132/125.

Let e_j be the jth elementary symmetric polynomial of these same six rates, and write

    A=e1, B2=e2, C3=e3,
    H0=B2+4A-A^2-6,
    L=B2-4A+10-2z,   N=4H0+4-C3-B2(4-A)-4z,
    p=N/L,   q=(A-4)p+H0-2z,   w=p+4-A,
    B=p-u1-u2,   C=q-u1u2-u1 B,
    Q(y)=y^2+p y+q.

The same original numerator has the exact identity

    Q(y)=(y+u1)(y+u2)+B(y+u1)+C.                (Q)

Define the actual feedback from these SAME coefficients:

    phi=e4+C3 w-[(6+2z)q+(4+4z)p+(1+z)^2],
    R2=e5+e4 w-(4+4z)q-(1+z)^2 p,
    R1=e6+e5 w-(1+z)^2 q,    R0=e6 w,
    D1=R2-phi(u1+u2+u3),
    D2=R1-phi(u1u2+u1u3+u2u3)-(v2+v3)D1,
    D3=R0-phi u1u2u3-v2v3 D1-v3 D2.

These rational functions have common denominator L. The literal raw matrix and boundary data are

    G = [ -u1  1    0    0    0    0    0
           0  -u2   1    0    0    0    0
           0   0   -u3   1    0    0    0
           0   0    0   -w    1    0    0
           D1  0    0    0   -v1   1    0
           D2  0    0    0    0   -v2   1
           D3  0    0   phi   0    0   -v3 ],
    beta=(C,B,1,0,0,0,0),
    gamma=K e7,
    D_z(y)=y[(y+1)^2+z]^2,  K=D_z(c)>0.

This is an actual nonuniform six-rate graph. The backward D entries and phi feedback are not dropped; numerator and characteristic come from THIS common matrix, not independent spectral factors.

## 3. Exact complete determinant and actual numerator

The complete SAME-matrix identities are

    det(y I-G)=D_z(y)Q(y),
    beta adj(y I-G)e7=Q(y).                      (ID)

The direct symbolic checker in §6 verifies the FULL7-by7 determinant as a polynomial identity in y,z, and also verifies

    det(yI-G+e7 beta)-det(yI-G)=Q(y),

which is exactly the rank-one determinant/adjugate identity for the actual numerator. The polynomial clearing is exact and covers repeated/coincident roots. Independently of the checker, the upstream bidiagonal adjugate column is `(1,y+u1,(y+u1)(y+u2))^T`, the downstream first-to-last adjugate entry is1, and beta gives(Q). No principal inverse at a hidden pole, independent output factor or positivity of a numerical fit is assumed.

## 4. Entire interval: exact positive Bernstein coefficients

For each function in the following table multiply by L, except the first row L itself. Its Bernstein representation on `[7/9,41/50]` has the stated degree and STRICTLY POSITIVE smallest exact coefficient:

|Polynomial|degree|least Bernstein coefficient|
|---|---:|---:|
|L|1|`1600273/1000000`|
|L p|1|`152908751/20000000`|
|L q|2|`793057212755377/81000000000000`|
|L w|1|`568762837/281250000`|
|L B|1|`5893223267/1800000000`|
|L C|2|`2404222780259/1012500000000`|
|L phi|3|`65787988944437/62500000000000000`|
|L D1|3|`9385943652095983401971/2531250000000000000000`|
|L D2|4|`24745026011159738267/62500000000000000000000`|
|L D3|4|`14989313308981887372658595357/6834375000000000000000000000`|

The complete exact coefficient lists are in the pinned JSON certificate (§6). Bernstein basis functions are nonnegative and sum to1 over a closed interval; hence EVERY listed function is strictly positive throughout the band, including both endpoints. These signs are for the actual correlated z-dependent functions, not separately optimized scalar quantities. In particular L never vanishes, p,q>0, and B,C,phi,D1,D2,D3 are all positive.

## 5. Explicit positive physical normalization for all c,d

Let `Q_c=c^2+p c+q>0`. Define

    h1=1/Q_c,
    h2=(c+u1)h1,
    h3=(c+u2)h2,
    h4=(c+u3)h3,
    h7=[K+D3 h1+phi h4]/(c+v3),
    h6=[h7+D2 h1]/(c+v2),
    h5=[h6+D1 h1]/(c+v1).

All seven components are strictly positive from §4. The upper three and lower three rows of `(cI-G)h=K e7` are immediate from the recurrence. The remaining center row follows from(ID) evaluated at y=c after multiplying by `Q_c product_j(c+v_j)`; the symbolic checker also directly verifies ALL seven equations as identities in c,z. Equation(Q) gives `beta h=1`.

With Delta=diag(h), set

    T=Delta^(-1)(G-cI)Delta,
    alpha=beta Delta,
    omega=Delta^(-1)K e7.

Then T is Metzler, alpha is a probability row, omega>=0 and **the actual identity** `-T1=omega` holds. The polynomial(ID) gives the eigenvalues of G:0, the repeated pair `-1±i sqrt(z)`, and the roots of Q. Because p,q>0, both hidden roots have negative real parts. Subtracting c>0 makes T Hurwitz. Its SAME-matrix transfer is exactly `K/D_z(s+c)` by(ID).

For arbitrary original d>0, construct this pair with `c0=c/d` and then multiply T and omega by d, leaving alpha unchanged. This gives the literal original H for `a=c+d`, `b=d sqrt(z)`. Thus the complete upper bound is proved for all positive c,d, not only the c=1 rational anchor.

## 6. Actually executed exact verification

Completed command:

    python3 frontier-20261028-ph7-band-41over50-check.py
    SymPy 1.14.0 Fraction exact determinant/numerator/normalizer/Bernstein assertions PASS

The checker verifies: the full symbolic7x7 determinant; the actual rank-one-update numerator; all seven `(cI-G)h=K e7` equations; `beta h=1`; and EVERY Bernstein coefficient of L and its nine scaled physical coefficients on the entire closed band. Symbolic identities are exact in c,y,z, signs use `fractions.Fraction`, and no float/root-fitting argument is used in this proof.

- Checker: `frontier-20261028-ph7-band-41over50-check.py`, **58LF/3162B**, SHA256 `e0172cb2005b0de9b0bcf7285d53632fe754466ebe1d9a9078d945663861aa89`.
- Full exact coefficient certificate: `frontier-20261028-ph7-band-41over50-certificate.json`, **88LF/3420B**, SHA256 `972ab75df0c85e8f1c2d7a41b8dc68f8c7fcd759b8812bc0e97f84cf59840ff6`.
- The separate numerical proposal generator `frontier-20261028-ph7-seven-endpoint-refine.py`, SHA256 `eec4d666eb35e41b77d7c6fe60d735a4fbe488839206159e95ecabf2a2fa88ef`, produced a rational `z=41/50,c=d=1` point which independently passed the exact actual-matrix determinant/numerator/PH-row verifier. Its result JSON SHA256 `a05a7d1f6abf19b726b275264186cca238ab11b3661b3e18b5d55bdfc1989506` contains the complete explicit rational T,alpha,omega. The point is redundant evidence, NOT the interval proof.

A later bounded search at higher rational ratios produced no certified witness, recorded in `frontier-20261028-ph7-further-endpoint-search.py` SHA256 `61ec6cb074490bf1dad84002f52c9461c0fc2e8d10d7693da9e0d1637c24b847` and result JSON `9aeb90ee4a1ba4de204b3aeeae81facc15b4c84b1a6324621780ba1e022bae7c`. Its optimizer misses are NOT an upper endpoint or a proof of nonexistence.

These are actual exact computational checks, not independent mathematical review, formal/kernel acceptance or novelty evidence. The local SymPy/SciPy installations are within the owner root; no global package state was altered.

## 7. Composition, exact provenance and remaining gap

The previously supported unrestricted PH6 lower proof is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`; its topology-unrestricted `z>1/2` conclusion is a named prior written-support input, NOT re-proved by this source. Combining it with §§2–5 gives candidate **exact order7** on `[7/9,41/50]`.

The old parent disposition `PH7-entire-rational-seven-ninths-band-parent-v1.md` supports exact7 directly on `[13/20,z_star]`, where z_star>7/9, at its explicit source/import/review boundaries. Its band overlaps this new band. Thus, conditional on the named existing B6 and prior parent inputs and on independent review of this new construction,

    minimum PH order = 7 for EVERY z in [13/20,41/50].

No full old-source-DAG recertification or unconditional extension down to1/2 is claimed. The old separate order8 construction remains the named contextual upper bound for the original8/9 point, not newly reverified.

The early equal-rate one-free-u chain cannot reach z>=389/500 by the independent exact candidate `frontier-20261028-ph7-three-chain-explicit-global-obstruction.md`, SHA256 `27d92a17b438888e052c9d8d0b423d76b660c2cd7c87cad104306e47a69417ca`. The new six-rate construction genuinely leaves that chart, but this does not establish global optimality or research priority.

Still OPEN: actual PH7 feasibility/exclusion at8/9, the true upper endpoint for seven states, other topologies, and the exact whole minimum-order function. No selected optimizer failure can close these. Review must reconstruct full SAME-matrix identities, every Bernstein sign, normalization for all c,d, the old lower/upper application cuts and original target; hashes/no-defect claims alone do not suffice.

Prior quarantines remain historical/unvalidated and were not used as accepted premises; no prior process failure is retroactively repaired. No Git/push/deletion/publication/secret access, unsolicited external-model/paid API campaign or infrastructure mutation. Same18/exclusive owner root/research deadline2026-10-31T21:23:27Z. No independent-family/human/formal/kernel/novelty acceptance is claimed.

**END — complete exact ACTUAL PH7 upper construction through41/50; exact-order7 conclusion retains its named earlier PH6 lower input.**
