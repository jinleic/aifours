# F55 full-band written proof review

Observed native clock immediately before this new report: **2026-10-28T17:51:55-0700 PDT**. This is a pre-write observation, not a claimed completion time.

## Verdict and findings

**INCONCLUSIVE — do not adopt the full-band candidate on this review.** Conditional on the two explicitly imported structural dispositions and the PBW import, I reconstructed the level-one module, both free-Levi maps, whole ideal transport, Cartan and lowering formulas, critical-degree reduction, mirror, level-zero boundary and first-defect caller. I found **no demonstrated mathematical FATAL or MAJOR defect** in those written steps. This is not a finding that the complete computer-assisted theorem is correct: I did **not** independently reconstruct all of its finite quotient matrices and determinant evaluations.

- **MAJOR — unresolved certificate-assurance obligation, not an identified false theorem.** The candidate's all-parameter conclusion depends on every class of the rectangle and four critical certificates (`B:92–113,136–144`; `Q:54–64,120–146`). I inspected the actual verifier interfaces and all certificate class/polynomial metadata, and independently recomputed one exact critical caller below. I did not rederive every quotient span, kernel basis, target reduction and determinant grid. Neither the author's recorded `PASS` nor my metadata inspection proves those remaining linear-algebra identities. Until they are independently established at the frozen bytes, the all-parameter band and its LIFT caller remain unverified. The precise finite obligation is at the end of this report.
- **MINOR — rectangle replay does not itself verify the displayed polynomial degree bound.** `frontier-20261028-214-independent-replay.py:225–242` and `frontier-20261028-horizontal-independent-replay.py:88–101` compare the printed polynomial to determinants on the degree-`k` grid but do not assert that *the printed polynomial* has degree at most `k` in each variable. `Q:62–64` invokes polynomial identity, which needs the bound for both polynomials. This is an interface/checking gap, not a demonstrated error in the pinned data: my independent metadata scan verified nonnegative integer powers, per-variable degree `<=k`, unique exponent pairs, common coefficient sign and nonzero constant for **all 144 selected nonzero determinant polynomials** across the critical and rectangle inputs after applying their explicit alternate replacements. A new verifier should make that bound an enforced input invariant.
- **MINOR — verifier class-count assertions are not class-set assertions.** `frontier-20261028-levi-critical-independent-replay.py:239–249` checks 16 records per encountered degree and writes an unconditional total of 64; `frontier-20261028-predecessor-independent-replay.py:13–23` similarly checks only seven blocks and 16 rows each. Duplicated/missing degrees or parameter pairs could therefore survive these count assertions in other input bytes. For the actual pinned inputs I independently checked the exact four critical degree set, all 16 distinct `(r class,s class)` pairs in each of all 16 degree blocks, and the 12 expected rectangle degree blocks; I found no missing or duplicate pair. The three critical and two `(2,2,4)` replacement keys exactly equal the corresponding mixed-sign keys. This finding does **not** claim the present inputs omit a class. A new verifier should enforce exact sets and replacement routing itself.

Severity convention here separates an **uncompleted verification obligation** from a proven defect in a mathematical argument. No FATAL finding, counterexample, independent-family review, formal proof, human review or novelty finding is asserted.

## Exact source coverage, pins and inputs

The frozen manifest was read before any listed source, followed by **every listed source in manifest order, in full**, including the PBW transcription qualification and both parent dispositions. I then checked actual bytes, LF counts and SHA-256 for each item against the manifest: **all nine matched**. Manifest SHA-256 is `b5c8e49fd6e534145eb3f011788d3f70f7ce4200913f6dbd9be6a9cac17e6308`.

Use these exact path prefixes:

- `R = /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`
- `M = /Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/`

All LF ranges in this table are complete, not excerpts. The short source labels used below refer to these pinned files.

|Order|Label and path|Read|Bytes|SHA-256|
|---:|---|---|---:|---|
|1|`P` = `R/written-releases/math-3-positive-freeness-pbw-transcription-addendum-v1.json`|1–12|1404|`21b5b074fdf6b20784ec640037aaffa8d0964f6c2aa3d7855ff955bf2873f247`|
|2|`D` = `R/written-releases/math-3-serre-family-packet-v1.md`|1–100|9883|`8b811cbc88e55b5b48bebef299f356bf10c808968c967ab2ed4aca1065cc03a6`|
|3|`C` = `R/dispositions/math-3-full-cartan-radical-serre-containment-and-first-defect-parent-v1.md`|1–34|5272|`08217c89602bbed5bb05447144addfb1978037ad3e4c2e57271d88b794d98be9`|
|4|`F` = `R/dispositions/math-3-preliminary-free-lie-and-serre-transport-parent-v1.md`|1–26|5196|`f08daf3e2259a563a426e8982be78a36094bb58e4d56f587b2b51f14fa8df46d`|
|5|`L` = `M/frontier-20261028-fixed-levi-level1-independent-v1.md`|1–136|13805|`a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a`|
|6|`V` = `M/frontier-20261028-Levi-free-quotient-critical-reduction-v1.md`|1–144|15439|`e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`|
|7|`H` = `M/frontier-20261028-two-horizontal-chain-theorem-v1.md`|1–193|17933|`d3cf1666c9b7eac84bc052da6af932c3199c878faaca717dcb987ac85109ec67`|
|8|`Q` = `M/frontier-20261028-level4-rectangle-certificate-v1.md`|1–156|19238|`887573ecc0adb16706d97674e7f7aa57a1880ae42b7db72330cb16f5272f3abb`|
|9|`B` = `M/frontier-20261028-registered-level4-full-band-candidate-v1.md`|1–154|19131|`bf7b47ce106d515dff130831eb85e8aa4d931bd6976b0afe7386adbabed136ea`|

**Explicit imports and nonimports.** `C:14–28` is the named full-Cartan/root-grading, Serre containment and first-defect import. `F:15–25` is the named preliminary free-positive-source and full Serre-ideal transport import. I use exactly those statements, not the verdicts quoted in either disposition, and have not read or independently re-proved all of their underlying author/reviewer bodies. The PBW statement is a **named classical import**, not proved here and not primary-source authenticated; `P:9–10` specifically says its frozen wording is a normalized secondary-source transcription, not a byte-for-byte primary quotation. Finite-dimensional `sl3` matrix-unit identities and its simplicity, ordinary Lie universal properties and Jacobi are also used. No quarantined/withdrawn result is a premise.

## Written reconstruction

### 1. Actual level-one module and its boundary

Let `G` be the actual preliminary full-realization algebra, `K` the full ideal generated by the positive **and** negative Serre seeds with repeated node 1 or 2, `T=G/K`, `J` the full Serre ideal, and `S=G/J`. The individual seed-killing relation from `C:16,24–26` applies to this subset as well: Jacobi makes its positive and negative descendant spaces full ideals, so `K=K_+ ⊕ K_-`; neither has a root-zero component. Thus the full Cartan survives. The positive-free import `F:15–19` gives nonzero `e_i` in `G`; `[h_i,e_i]=2e_i` then gives nonzero `h_i`. Since `K,J` have zero Cartan intersection, the images of `h_i` remain nonzero. In particular `v=e3` survives both quotients: otherwise `[e3,f3]=h3` would vanish. The node-1/2 subalgebra in `T` satisfies the `A2` Chevalley–Serre relations, has nonzero `h1`, and is actually `sl3` by simplicity, not a formal Levi that might have collapsed (`L:17–23`; `V:21–29`).

By the imported triangular/root-sign support, an actual level-one class is positive. Every positive word with exactly one `e3` is, by Jacobi, a sum of positive-Levi operator words on `v`; hence the **whole** level-one space is `U(n_+^Levi)v`. Write `x=ad e1`, `y=ad e2`, `z=[x,y]`. The fixed Serre relations give `[x,z]=[y,z]=0`, `x²v=y²v=0`. Swapping `yx=xy-z` yields the spanning order `x^a z^b y^c`. In particular `[x²,y²]=4zxy-2z²`, so `z²v=2zxyv`; applying `x` and `y` gives `z²xv=z²yv=0`, and consequently `z³v=0`. These identities reduce the cyclic space to the eight listed words `v,xv,yv,zv,xyv,zxv,zyv,z²v` (`L:25–59`).

In the explicit matrix model `e1=E12`, `e2=E23`, `v0=E31`, these words map respectively to `E31,-E32,E21,E11-E33,E11-E22,-E12,-E23,-2E13`, a basis. Thus the universal cyclic `n_+` module has exactly dimension eight and the actual cyclic module is its quotient. Both `v0` and `v` have `h1,h2` weight `(-1,-1)` and are killed by `f1,f2`; commuting these generators through positive operator words extends the well-defined positive intertwiner to the **full** Levi. Its kernel is an ideal of the simple adjoint `sl3`, and it is not all of `sl3` because `v≠0`; hence it is an isomorphism onto the actual level-one space (`L:61–83`). No highest-weight classification is needed. The actual horizontal increments are `(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)`.

The two omitted positive node-3 seeds have levels `r+1,s+1≥2`; positive descendants cannot lower this level, and the negative ideal has negative root support. Thus `T_1→S_1` is the **actual** quotient isomorphism, not an assumed higher-level one (`L:105–113`). For `Ddef=tau/J`, the ideal intersection with this simple module is zero or the whole module. It cannot be whole, because `[f3,v]=-h3≠0` whereas `(Ddef)_0=0`. This pays level one, conditional on the named imports.

### 2. Both universal maps and the entire ideal

Let `M=T_1` be that **actual** module, `l_+=span(e1,e2,[e1,e2])`, and `P=l_+ ⋉ FreeLie(M)` with `l_+` acting as derivations. First send the original positive generators `e1,e2,e3` to their namesakes in `l_+` and `v∈M`. The four positive fixed-node seeds vanish: the two internal `A2` relations vanish in `l_+`, and the other two are `x²v=y²v=0`. The actual free-source/`K_+` presentation therefore gives `n_+(T)→P`; it is onto because `e1,e2` generate `l_+`, their orbit of `v` generates `M`, and `M` freely generates the Lie part.

Conversely include the actual `l_+` and the actual vector space `M` into `n_+(T)`. The free-Lie universal property gives `FreeLie(M)→n_+(T)`, and compatibility with the actual Levi action, extended by Jacobi, gives `P→n_+(T)`. Each composite fixes `e1,e2,e3`; these generate both relevant algebras, so the maps are inverse. This is the needed higher-level statement for **`G/K`**, not an identification of `G/J` with a free Lie algebra (`V:31–48`).

The two remaining positive seeds become `rho31=-(ad v)^r(xv)` and `rho32=-(ad v)^s(yv)`. The transported positive `J/K` is their generated ideal under **both** the entire `l_+` action and brackets with all `FreeLie(M)` elements; equivalently take the full Levi orbit first and its full free-Lie ideal, retaining all overlaps. The admitted positive/negative ideal splitting excludes additional positive-root contributions from negative seeds. Therefore the actual positive level-`n` Serre quotient is `FreeLie_n(M)/I_n` for this entire `I`, not a quotient by only seed rows (`V:50–65`). The reverse map and ideal minimality are essential: I found no unsupported identification of a compressed target with an actual quotient in this argument.

### 3. Full Cartan and all lowerings

For every full-realization row `p`, put `A_p=(2c_p1+c_p2)/3`, `B_p=(c_p1+2c_p2)/3`, `Z_p=h_p-A_p h1-B_p h2`, and `lambda_p=c_p3+c_p1+c_p2`. The fixed `A2` determinant is 3, so `Z_p` commutes with the Levi and acts on the cyclic module as `lambda_p I`. Thus on level one, `ad h_p=A_p ad H1+B_p ad H2+lambda_p I`; on a level-`n` bracket it is the derivation extension, equivalently `A_p ad H1+B_p ad H2+n lambda_p I`. On degree `(a,b,n)` this is exactly `a c_p1+b c_p2+n c_p3`. This explicitly retains arbitrary complex extra rows and requires no inverse of the full Cartan matrix (`L:85–103`).

The actual `f1,f2` actions are adjoint `sl3` actions extended as derivations. From `[f3,v]=-h3` and `[h3,e1]=-r e1`, `[h3,e2]=-s e2`, I obtain on the eight letters

`(-h3, -r e1, -s e2, -(r+s)[e1,e2], -s[e1,e2], 0, 0, 0)`.

Also `[h3,m_j]=(2-r a_j-s b_j)m_j`. The table follows by Jacobi, including `[f3,xyv]=-s[e1,e2]`; `f3` applied to an `n≥2` bracket recursively produces the **whole actual level `n-1` target modulo its full ideal**. At `n=1` the target includes the actual full Cartan and is handled separately. Ideal stability comes from `J` being the actual full ideal, not from an assumed surjection or an equality between a preliminary reached-obstruction and a compressed one (`V:67–99`; `B:53–65`).

### 4. Critical degrees and mirror

The degree-`n` free Lie power is finite-dimensional, since it is spanned by nested brackets in eight letters; the actual quotient is a quotient of that space. A degree `(a,b,n)` has `h1,h2` weights `mu1=2a-b-n` and `mu2=2b-a-n`. If nonzero `w` is killed by `f_i`, finite horizontal support makes `e_i` nilpotent; with maximal `N` such that `e_i^Nw≠0`, the elementary `sl2` commutator applied to `e_i^(N+1)w=0` gives `mu_i=-N≤0`. Thus `2a-b≤n`, `2b-a≤n`, and `0≤a,b≤n`. Direct enumeration gives exactly:

- `n=1`: `(0,0),(1,1)`;
- `n=2`: `(0,0),(0,1),(1,0),(1,1),(2,2)`;
- `n=3`: `(0,0),(0,1),(1,0),(1,1),(1,2),(2,1),(2,2),(3,3)`;
- `n=4`: `(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(2,3),(3,2),(3,3),(4,4)`.

These are **possible** horizontal-lowest degrees, not claims that a singular class exists in each. Outside `a,b≤2`, four representatives remain: `(3,3,3),(3,2,4),(3,3,4),(4,4,4)`; `(2,3,4)` is the mirror. Interchange rows 1/2 and columns 1/2 of the top Cartan block, columns 1/2 of every extra row, and the associated `e1/e2`, `f1/f2`, `h1/h2` labels. This is an invertible presentation isomorphism from `A(r,s)` to `A(s,r)` and transports the full Cartan, actual ideals and lowerings. It therefore covers the mirror for the universally quantified full realizations (`V:101–124`; `B:67–90`).

### 5. Analytic chain and the first-defect/root-zero argument

At `(1,1,n)`, the free-source leading words show the independent basis `V_k=[(ad e3)^k e1,(ad e3)^(n-k)e2]`, `0≤k≤n`. The full positive ideal cuts exactly the `k≥r+1` or `n-k≥s+1` vectors, giving quotient interval `max(0,n-s)≤k≤min(n,r)`. For its full `f3` target the corresponding `n-1` interval is used. I checked the displayed derivatives

`f3(V_k)=k(r-k+1)U_(k-1)+(n-k)(s-n+k+1)U_k`,
`f1(V_0)=(n+1)Y_n`, `f1(V_1)=-Y_n`, and `f1(V_k)=0` for `k≥2`.

The proposed left-to-right elimination for `s<n`, right-to-left elimination for `s≥n,r<n`, and the `f1` plus first `f3` coordinate argument for `r,s≥n` use strictly positive integer coefficients on their stated surviving intervals. Hence the chain kernel proof is consistent, including empty-source cases. The one-horizontal and pure-`e3` boundaries are separately handled by their surviving `f3` coefficient or nonzero root-zero `h_i`; at `n=0` the positive Levi is spanned by `e1,e2,[e1,e2]`, with other positive horizontal degrees zero (`H:46–94,96–171`; `Q:120–130`).

The band `n≤4` is downward closed. If the actual graded ideal `Ddef=tau/J` has a nonzero component in it, choose one of least total height. Every simple lowering lands in a smaller component of the same band, the root-zero defect `(Ddef)_0=0`, or a mixed-sign zero space. The class is therefore simultaneously singular. Thus **provided** every listed actual quotient kernel, including the entire rectangle and four representative critical certificates, is zero, the full registered band follows. Conversely, if `Delta_G(x)` lies in the full direct-sum target ideal and the quotient singular kernel vanishes, then `x∈J` and `j=x` is one common actual correction. This proves the stated reached-intersection identity conditional on those actual kernel results; it does not prove arbitrary abstract target tuples are reached. Pointwise `Ddef_alpha=0` must not be substituted for a first-defect argument without its predecessor boundary (`C:18,24–26`; `B:136–144`).

## Finite-certificate interface inspected and what I actually checked

After all manifest sources, I read the following code in full (line ranges and live SHA-256):

|Path under `M`|Lines read|SHA-256|
|---|---:|---|
|`frontier-20261028-levi-critical-independent-replay.py`|1–263|`4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6`|
|`frontier-20261028-214-independent-replay.py`|1–267|`02e8e0c0432f18b67edd7a75ad687e90599834d741f994a8c09100d8250a82f1`|
|`frontier-20261028-horizontal-independent-replay.py`|1–125|`ab2643d44ed90e8679d34e40f67f8ea6b8fed83a74191a72efda0f2ed81e1e4f`|
|`frontier-20261028-central-predecessor-replay.py`|1–47|`d8d42aa1fb6fe01b6f6771f98440b6a9d1f3c35a06de50a9024659467865dd2d`|
|`frontier-20261028-predecessor-independent-replay.py`|1–36|`5b3721097213da84d55b429e78fbbf9cdd2cd6fafb26d751e3b3233974e188e8`|

I inspected the code's actual interface rather than treating the reported outcome as proof: the critical replay constructs matrix-unit actions (`:21–101`), recursively applies `f3` on Lie trees (`:104–134`), generates both seeds and all bounded `e1/e2` and eight-letter ideal descendants (`:137–175`), checks source complements and full horizontal kernel (`:187–219`), then matches sign-definite determinant polynomials on exact interpolation grids (`:220–236`). The rectangle routines generate original-generator nested words, all fitting Serre seeds, target-ideal remainders and full or horizontal-kernel minors. They import the separately written `214` helper; that helper and rational arithmetic are a shared implementation dependency. I did **not** read the producer programs or independently establish every linear-algebra equality in their data. I did not rerun the author scripts or infer mathematical correctness from their saved PASS.

I parsed class labels, statuses, alternate routing and polynomial coefficient/exponent metadata—not every displayed basis vector as an independently checked identity—from these additional actual files, whose whole-byte hashes I observed:

|Path under `M`|SHA-256|
|---|---|
|`frontier-20261028-levi-critical-minors-v1.json`|`2c8796b67242f52ba63321bdf8e163138ed41594cf354c6f5547b465f401661b`|
|`frontier-20261028-levi-critical-alternates-v1.json`|`232fe13aec9be941681fa4251a535631a85bbd4cce55a8ca41abf8460bf5c980`|
|`frontier-20261028-levi-critical-independent-replay-v1.json`|`af07046bb907c9d9f9a53e336452fe3a8d0521cbb51eb000b605028b09f6fc90`|
|`frontier-20261028-214-symbolic-minors-v1.json`|`15ee23511638af13eaebe332c3dbad0ec194da1a4c9b59385c41436be4fe0683`|
|`frontier-20261028-predecessor-certificates-v1.json`|`39742fa183d9290835e25b29ab246a66e3065d1fecb1c2796210e59dbb8388c2`|
|`frontier-20261028-221-horizontal-minors-v1.json`|`aa9f38f92f58303b20d021e4c7102572bdf8239246716ce43f695ea3f2e848d7`|
|`frontier-20261028-222-horizontal-minors-v1.json`|`94e2bac395862b645f1ef463546ad6e244021a3143e67aa22d59c5f0c30536b9`|
|`frontier-20261028-223-horizontal-minors-v1.json`|`a4c58943bb39cd8624faa298ddb087596825db4ef6c183a2cd805ce2807310e2`|
|`frontier-20261028-224-horizontal-minors-v1.json`|`08725d2fdcd7b5738e677b04c2ba9b4cbfd374de49505ede4b967282414b91ba`|
|`frontier-20261028-224-alternate-minors-v1.json`|`46b037e9f5c5f2c57444e71c44200427a3acb55cc6cad14f1262aa01a6b61979`|

The metadata scan found the exact four critical blocks and 12 rectangle blocks, each with all distinct 16 threshold pairs: **64 + 192 class records**. After replacements, it checked **40 critical + 104 rectangle = 144** nonzero polynomial records for the invariant described in MINOR 1, with no metadata failures. The critical replay receipt's reported block counts are consistent with its summary, but its recorded PASS is not this review's proof of the 64 matrices.

**One separately constructed exact mathematical caller.** After reading the sources, I wrote an in-memory rational computation with no project-code import and no output file. For `(a,b,n)=(3,3,4)`, `r=s=1`, I independently built the eight matrix-unit actions; spanned the degree by all right-nested length-four tensor brackets; generated the entire bounded ideal from the two node-3 seeds by both positive-Levi actions and brackets with all eight letters; and used exact rational row reduction in source and target. The observed source and ideal dimensions were `65` and `64`, so the quotient dimension is `1`. For the candidate vector `[m0,[m0,[m3,m7]]]`, both horizontal derivatives reduced to zero in their full target quotients; the `f3` derivative reduced to a nonzero vector with coefficient **8** on tensor word `(m1,m4,m6)`. This matches the relevant certificate interface and proves that single exact caller in my model, conditional on the written source/ideal identification. It is neither a replay of the other 63 critical classes nor an unbounded-parameter proof.

## Precise remaining obligation and boundaries

Independently reconstruct, using frozen inputs and actual quotient targets, the exact source/ideal spans, complements, complete joint horizontal kernels and every advertised determinant-grid equality for **all 64 critical and 192 rectangle degree/parameter classes**, including zero-source/zero-horizontal cases and all five alternate minors. Enforce the exact degree/class/replacement sets and polynomial degree/sign conditions, verify the resulting determinants against the printed polynomials, and check the two named structural imports/PBW at the separately authorized trust level. Alternatively, a different complete proof of every required actual simultaneous kernel can replace the finite computation. Only then does the reconstructed first-defect implication support the registered `A(r,s)`, `alpha3≤4` conclusion.

The printed Su problem in `D` is the arbitrary-GCM, all-level defining-relations conjecture; the registered two-parameter, level-four band is strictly narrower. Even a future successful band review would not establish the broader book conjecture, novelty or priority. This reviewer had the assignment's description of the target and general mathematical background before reading; same-harness context is not blind or cognitively clean, and unknown inherited familiarity cannot be excluded. No other reviewer or author was consulted, no external-model CLI or paid service was called, and no secret, held result, publication, push, deletion or infrastructure mutation was used. The review is conditional, computer-assisted where explicitly noted, and not human, cross-vendor, Lean or formal verification.
