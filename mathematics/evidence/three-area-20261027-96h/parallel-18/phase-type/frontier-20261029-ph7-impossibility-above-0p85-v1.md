# No seven-state PH representation for any ratio z >= 17/20 = 0.85

**NEW ALL-TOPOLOGY THEOREM CANDIDATE (strengthens `frontier-20261029-ph7-impossibility-above-0p8765-v1.md`).** Written proof; exact SymPy identities for symbolic z; exact integer Bernstein certificates at the single ratio z2=17/20; an independently implemented standard-library replay. Not independently reviewed; parent adoption, formal proof and novelty clearance pending. MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 06:35:53 PDT 2026**.

## 1. Statement

For c,d>0, a=c+d, z=b²/d², `H(s)=c(a²+b²)²/[(s+c)((s+a)²+b²)²]`.

**Theorem.** If `z>=17/20`, H has no phase-type representation with at most seven states.

With the separately constructed seven-state band up to about 0.82042 (owner candidates, not re-proved here), the seven-state threshold lies in about **[0.8204, 0.85)**.

## 2. Reduction (as in the 0.8765 candidate)

1. Irreducibility caller (SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`): an irreducible 7x7 Metzler G, spectral bound0, `det(yI-G)=y[(y+1)²+z]²(y²+py+q)`, p,q>0.
2. Lemma S (`frontier-20261029-ph7-shift-monotonicity-corollary-v1.md`, SHA256 `dde16615ea1cfcc0dcac77ca5f3329cc947e58287e4c126b13979468b7a390e1`) with `t=sqrt(z/z2)-1` moves G to the ratio exactly z2=17/20.
3. Lemmas 1-4 of `frontier-20261029-ph7-eight-ninths-impossibility-v1.md` (SHA256 `599feaa589a6281316786cdd4d19050a88ba2945a12ce253d5f04678e862b2d4`): S=geometric symmetrization, A=-S positive definite with eigenvalues `v_1<=...<=v_7`, extra cycles with weights `omega_C>=0`, all of length>=3, and the cover identity.

## 3. New: the y² inequality

**Lemma 5.** With `W=sum_{|C|=3} omega_C`, `C4=sum_{|C|=4} omega_C`, `C5=sum_{|C|=5} omega_C`,

    [y^2]det(yI-G) = e5(v) - sum_{|C|=3} omega_C e2(A_{V-C}) - sum_{|C|=4} omega_C tr(A_{V-C}) - C5,

and therefore, with `S3=v1+v2+v3`, `m2=e2(v1,...,v4)`, `L4=v4+v5+v6+v7`,

    E2 := e5(v) - [(1+z)²p+(4+4z)q]  >=  E4*m2 + S3*max(0, E3-E4*L4).

*Proof.* In the cover identity a set L of disjoint extra cycles with two or more members covers at least six states, leaving a determinant of degree<=1; single cycles of length 3, 4, 5 leave `det(yI+A_U)` with |U|=4, 3, 2, whose y² coefficients are `e2(A_U)` (sum of principal 2x2 minors = e2 of its eigenvalues), `tr(A_U)`, 1. The target's y² coefficient is `(1+z)²p+(4+4z)q` (identity checked). Cauchy interlacing for a principal submatrix of size 4 gives eigenvalues `v_k<=mu_k<=v_{k+3}`, hence `e2(A_U)>=m2` (all positive) and `tr(A_U)<=L4`; for size 3, `tr(A_U)>=S3`. With `T3=sum_{|C|=3} omega_C tr(A_{V-C})`, Lemma 3 says `E3=T3+C4`, so `C4>=E3-W*L4` and `C4>=0`. Then `E2>=W*m2+S3*C4+C5>=E4*m2+S3*max(0,E3-E4*L4)` since `W=E4`. □

In particular `Y2b := E2 - E4*m2 - S3*(E3-E4*L4) >= 0`. With x=v7 and the six others fixed, Y2b is a quadratic `c2 x²+c1 x+c0` whose leading coefficient is exactly `c2=S3*A` (identity checked), where `A=f2-4f1+10-2z` as in the core.

## 4. Lemma C2 at z2=17/20

**Lemma C2.** No seven positive reals `v1<=...<=v7` satisfy `p>0, q>0, E4>=0, E3-E4*S4>=0, Y2b>=0` at z=17/20.

*Proof.* Notation of the core (x=v7; `f_k` of the six others; A, B, h0, h1, D, E). Cases (a) f1<4 (needs z>3/7), (c) f1>=4, A>0, D<=0 (Hpol(z2)>0), (d) f1>=4, A>0, D>0 (three-parameter residual at z2) are exactly as in the 0.8765 candidate with the constants of z2. Case (b) f1>=4, A<=0 used `Qpol>0`, which FAILS near six equal rates for z<0.8761. New treatment of (b):

- If the six rates are not all in `N=[3/5,9/7]`, the compactified outer cover gives `Qpol(z2)>0` and the old argument applies (`Q>0` with A<=0, q>0, E4>=0 is contradictory).
- If all six lie in N, sort them `v1<=...<=v6<=x`; the sorted affine cover of N^6 places the point in a leaf with one of: F (`4-f1>0`), A (`A>0`), Q (`Qpol>0`), **E4v6** (`A<0`, `E4(v6)<0`: then `E4(x)<=E4(v6)<0` as E4 decreases in x), **Y2v6** (`A<0`, `Y2b(v6)<0`, `Y2b'(v6)<=0`: concavity gives `Y2b(x)<0` for all `x>=v6`), **Disc** (`A<0`, `c1²-4c2c0<0`: `Y2b<0` for every x). Each contradicts the hypotheses. Leaves marked "unsorted" contain no sorted point. □

Together with Section 2 this proves the Theorem.

## 5. Certificates (exact integers) and actual runs

Generator `frontier-20261029-ph7-threshold-z2-check.py`, **302LF/17559B**, SHA256 `ff919031860c7583547dbd09d58271bbf333f2eeee880cfe4822a096f940fbc7`, run 06:31:58-06:32:31 PDT, actually printed (abridged to its result lines)

    symbolic-z identities PASS (incl. y^2 coefficient and c2=S3*A)
    Hpol(z2) leaves 9179
    outer Q/N leaves 9782 {'pos': 9470, 'N': 312}
    exact N cover leaves 22111 {'Q': 7873, 'Y2v6': 6707, 'unsorted': 6969, 'Disc': 521, 'E4v6': 41} exact refinements 0
    SymPy 1.14.0 z2=17/20 exact PASS: ... residual {'Abar<=0': 950, 'Dbar<=0': 934, 'f1-4<0': 65}

Leaf rules: compactified covers (`u_i=x_i/(1-x_i)` times `prod(1-x_i)^2`) need depth>=6, all coefficients>=0 and every interior-domain vertex coefficient>0, or (outer only) the box inside `[3/8,9/16]^6`, which is N^6; the N cover uses the affine map `v=3/5+(24/35)s` on `[0,1]^6` with STRICT positivity of all Bernstein coefficients for every certified polynomial except `-Y2b'(v6)` (>=0). The leaf search for N is float-guided, but every leaf is checked with integers.

Certificate `frontier-20261029-ph7-threshold-z2-certificate-v1.json`, **144650LF/1593287B**, SHA256 `3824b33dffd55abb03e5174c65fec1d9a353c72c1403c7b3356e9f20603fc6df`.

Separately written standard-library replay `frontier-20261029-ph7-threshold-z2-integer-replay.py`, **277LF/15941B**, SHA256 `c9c3164fa281b2422ebaab77238723532255b79173487f9923c313bd3ca2e6a5`, run 06:34:05-06:35:01 PDT, actually printed

    identities PASS (stdlib, symbolic z, incl. y^2 coefficient and c2=S3*A)
    compactified covers replayed: H {'pos': 9179} outer {'pos': 9470, 'N': 312}
    sorted N cover replayed: {'Q': 7873, 'Y2v6': 6707, 'unsorted': 6969, 'Disc': 521, 'E4v6': 41}
    Independent stdlib replay PASS at z2=17/20: ... residual {'f1-4<0': 65, 'Abar<=0': 950, 'Dbar<=0': 934}

It rebuilds every polynomial from its definition (Y2b from e1..e5 of seven variables), matches all digests, recomputes the affine Bernstein tensors by its own shift-and-convert routine, and replays all leaves. Same-owner implementation, not human/cross-vendor/Lean verification.

## 6. Limits (diagnostics, not premises)

The full y²-sharpened system (all five conditions jointly) has kernel-found feasible points at z=0.84 (Nelder-Mead margin about +0.017) and none found at 0.85; the same cover method also closed in floating arithmetic at z=169/200 (about 3.0e5 N leaves, not certified). So this route cannot go much below about 0.845; reaching the constructive value 0.82042 needs further coefficient information (y¹, y⁰) or structure.

## 7. Scope

Review targets: Lemma 5 (cover identity coefficient, interlacing directions, sign of omega, the max(0,·) step), c2=S3*A and the three new selectors, the outer/N cover rules (sorted labels, N^6 inclusion, strictness), and the inherited cases. Imports (caller, symmetrization Lemmas 1-4, Lemma S) are cited, not re-proved. No formal, kernel, human, cross-vendor, novelty or priority acceptance is claimed; historical holds and process findings are unchanged.

END - no seven-state PH representation exists for any z>=0.85; the seven-state threshold lies in about [0.8204, 0.85).
