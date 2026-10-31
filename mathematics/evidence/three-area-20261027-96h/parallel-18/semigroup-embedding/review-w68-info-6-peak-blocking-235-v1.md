# Review w68 — info-6 peak blocking upper bound

**Reviewer:** MathSemigroup-2, math-4. **Author:** InfoBalancedNL242-2-2, info-6.

Actual first wake: **Tue Oct 27 16:32:12 PDT 2026**. Actual pre-body ACK observation: **16:32:36**. Actual native observation immediately before writing: **Tue Oct 27 16:35:29 PDT 2026**.

## 1. Verdict and counts

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** in the full candidate S18, `walsh-peak-blocking-upper-bound-v1.md`.

- New FATAL mathematical findings: **0**.
- New MAJOR mathematical findings: **0**.
- New MINOR mathematical findings: **0**.

For every **actual balanced Boolean function on F2^9** with full Walsh peak at most28, the number of coefficients of magnitude28 lies in **[92,235]**. The upper bound follows from the stated all-affine blocking inequality and the corrected no-full-peak-6-flat premise. I reconstruct the used premises, including the corrected lower92 chain, rather than treating parent status as proof.

This is a **conditional necessary multiplicity bound**, not construction of an object, exclusion of every spectrum, a nonlinearity improvement, closure of any original rank/type or (24,24,2), or novelty acceptance.

## 2. Mandatory order, complete coverage and exact process qualification

S0 and the complete frozen manifest (`d9f58fb66bf356eabe5ce632d70acdc8e4b1713391641af63f85934bf979bebf`) were read first. Before packet opening or mathematics I wrote the designated pre-body ACK, SHA `e28dc0ade7167d812bd4b15c2b0ad017765d7f16258f12b24490c1d35ed1ed8e`, actual16:32:36.

I then read **all721LF / 83645 bytes** of the exact packet, SHA `1b270676bc3d2035e8e6563bc3d2894631226fbdf2e5764c59e8ade2ca7b4e5a`, through all eighteen source endings. Actual raw windows were1–60,61–120,121–180,181–240,241–300,301–360,361–420,421–480,481–540,541–600,601–660,**661–721**.

**Reading-limit deviation, disclosed to Main:** the final range is61LF, one above the mandated <=60. It returned through the final ending without elision. I did not reread to backdate compliant chronology, and do not claim every window complied. This is a documentary/procedural qualification separate from the mathematical findings above; no extra source, selected check, execution or theorem follows from it.

Prior closed-round NL reviews v101(b)-D/v103-D/v104-B are disclosed same-problem exposure. The current same-slot continuation identity is not used to invent a first/blind contact or a global contact census. No old body, private guide, selected control or favorable verdict was imported. Own semigroup method STOP, QOA source-scope MINOR and all earlier findings persist.

No chosen small case, particular function, frequency set, affine flat, group/graph/state/sign instance or numerical sanity probe was constructed or checked, even privately. The proof below is universally quantified in the source variables or specializes only the original fixed target constants. No interpreter/calculator/Eval/CAS, enumeration, solver, test, replay, CLI, nested task, external source or author contact. Only the required ACK and this review were written.

## 3. Frozen sources and dependency scope

Outer source labels used below:

| Source | Complete LF / role | Used mathematical scope |
|---|---|---|
| S1 | 35, literal definitions | Actual f, Walsh transform, balance and original NL/peak target. |
| S2 | 25, parent/status | Binding adoption/erratum boundary only, not a mathematical proof. |
| S3 | 40, saturated-flat rigidity | Only the no-full-peak-6-flat consequence is needed; its required arithmetic is reconstructed in §5. |
| S4 | 38, w44 erratum | Mandatory orientation factor M1 and transform-versus-coset normalization M2. |
| S5 | 43, affine restriction | Exact local/global character identity, not its separate local bound/saturation claims. |
| S6 | 87, original caller/mod4 | Forward Parseval, balanced k-integrality, parity and quadratic residue on T-perpendicular. |
| S7 | 37, odd-divisor dependency | Read; its larger all-magnitude theorem is not assumed wholesale. |
| S8 | 36, local cube dependency | Read with S4 correction; not used to prove S18. |
| S9 | 29, general odd-divisor flat dependency | Read; broader claims not promoted. |
| S10 | 15, sign addendum | Read; not used by this candidate's bound. |
| S11 | 7, edge-domain clarification | Read; no unsupported low-dimensional pattern is imported. |
| S12 | 33, forced3-flat | Read; not a needed premise of S18. |
| S13 | 28, lower92 | Used with S14 and full chain in §6. |
| S14 | 30, coupled-count correction | Mandatory for the lower bound, not optional independent count estimates. |
| S15 | 35, odd-half sign dependency | Read; its stronger sign/uniqueness claims are not needed. |
| S16 | 49, support-XOR/weight fact | Used only with S14 correction; polynomial-weight induction and T!=0. |
| S17 | 49, hyperplane energy | Used half-energy divisibility; separate residue/count filters not promoted. |
| S18 | 33, candidate | Every stated claim reviewed. |

Candidate pin: `1693f189d0320c5b64909fa99a9066e24968af6abd81ae062169eaeceb8a15d2`. The manifest and packet bind all dependency pins. The status record does not authorize omission of a proof step. Conversely supplying a dependency file does not turn every statement in it into a reviewed result: only the used claims below are exported.

## 4. Original caller and corrected conventions

For an actual f on V=F2^9, put s=(-1)^f, W(a)=sum_x s(x)chi_a(x), chi_a(x)=(-1)^(a dot x). Orthogonality gives the exact inverse and Parseval:

s(x)=2^-9 sum_a W(a)chi_a(x),
sum_a W(a)^2=2^18.

Comparing with every affine Boolean function gives NL(f)=256-(1/2)max_a|W(a)|. Thus the literal balanced NL>=242 target is precisely W(0)=0 with all |W|<=28, for the **same actual Boolean inverse**, not an arbitrary real magnitude profile.

For balanced f, let M={f=1}, |M|=256 and n_a=#{x in M:a dot x=1}. Then

W(a)=512·1_(a=0)-512+4n_a.

Hence k=W/4 is integral, |k|<=7, k(0)=0, sum k²=2^14, and k(a) mod2=a dot T where T=sum_(x in M)x. The zero-frequency correction is retained, not applied only at nonzero a.

The shared moment expansion of the XOR modulo4 gives the same quadratic Z/4 coefficients at all frequencies, as S6:49–75. Its polarization is k(a+b)-k(a)-k(b)=2B(a,b) modulo4, with B bilinear and B(a,a)=a dot T. Restricting to a linear subspace of T-perpendicular makes k even; Q=k/2 modulo2 is then an ordinary Boolean quadratic with Q(0)=0. This is a **frequency residue** statement, not an imported global truth-degree/rank classification of f.

For a frequency flat a0+H with source cosets x_y+H-perpendicular, write

R(y)=sum_(x in x_y+H-perp)s(x)chi_a0(x),
C(y)=chi_a0(x_y)R(y).

Character orthogonality gives

2^dim(H) R(y)=sum_(h in H) W(a0+h)chi_h(x_y).

Thus, when W(a0+h)=M0 epsilon(h), the corrected equation is

2^dim(H) C(y)=M0 chi_a0(x_y) T_epsilon(y).

This retains S4's M1 orientation character. M2 also remains: the unnormalized transform T_epsilon and the oriented C coefficient do not have the same scale. No unprovided sign/section normalization is assumed. The proof below uses magnitudes/divisibility only, so the unit orientation factor does not disappear by a false equality of signs.

## 5. Used no-full-peak-6-flat consequence, paid directly

Suppose an **arbitrary** affine6-flat were entirely at magnitude28. Its source cosets have size2^(9-6); each R(y), and therefore C(y), is an even signed sum of that many unit terms. Hence |C(y)|<=2^(9-6).

The corrected character equation has right side divisible by7. Since7 is odd, it is coprime to2^6, so7 divides each C(y). Evenness then makes every nonzero C(y) have magnitude at least14, greater than its allowed coset size. Therefore all C(y) vanish.

But the character transform on H is invertible; all C zero would force all epsilon zero, contrary to every frequency being a peak. This contradiction proves that no affine6-flat is fully peak. It is universal over actual flats and functions, not a selected flat or a finite scan.

This is exactly the consequence S18 uses. It neither imports S3's additional radical/sign classification nor substitutes an uncorrected equation. Balance also forbids an entirely positive-magnitude full frequency space, but no such extra case is needed for the6-flat obstruction.

## 6. Used lower bound92: full corrected dependency chain

### 6.1 Polynomial weight and the T=0 contradiction

For any nonzero multilinear Boolean polynomial of degree at most d on an n-dimensional space, the source's induction gives weight at least2^(n-d): write P=P0+x_n P1. If P1=0 the count doubles; otherwise every input where P1=1 contributes one true value in the two-element fibre, and apply induction at degree d-1. Constants and zero derivatives are included symbolically, not tested as examples.

On any linear K<=T-perpendicular, Q=k/2 mod2 is quadratic and Q(0)=0. So1+Q is nonzero and has weight at least|K|/4; at most3|K|/4 points have Q=1.

If T=0, take K=V. With u the number of Q-ones, u<=384. The exact nonzero Q-zero complement is **511-u**, not an independent upper bound127. On Q=1 the even k has |k|<=6; on Q=0 it has |k|<=4, and k(0)=0. Therefore

sum k²<=36u+16(511-u)<=15856<2^14,

contradicting Parseval. This uses the **S14 coupled-count correction**, not S16's superseded independent-count wording. Hence T!=0.

### 6.2 Energy divisibility in every frequency half

For arbitrary nonzero t, let H=t-perpendicular and choose any a0 outside H. The H-transform of k on a0+H, indexed by source pairs[x]={x,x+t}, is

F([x])=-128 chi_a0(x)(f(x)-f(x+t)).

This follows by the H-character sum from the actual Boolean definition, since that frequency coset excludes0. It is independent of the source-pair representative: both signs reverse on replacement x->x+t.

If m_t counts disagreeing source pairs, Parseval on H gives E_(odd half)=64m_t. The balanced number of ones equals twice the number of double-one pairs plus m_t, so m_t is even. Thus this half's energy is divisible by128. The total energy2^14 then gives the same for its complement. No direction, input or profile is selected; the proof applies to every nonzero t.

### 6.3 Correct even-half bound and odd magnitude counts

Use the now nonzero T, with K=T-perpendicular of size256. If u is its number of Q-ones, u<=192; its exact other nonzero count is255-u. Thus, with the same mandatory correction,

E_K<=36u+16(255-u)<=7920.

The128 divisibility forces E_K<=7808, so the opposite odd half has E_odd>=8576 and is also divisible by128. Only magnitudes1,3,5,7 occur there, with counts n1+n3+n5+n7=256. Consequently

E_odd=6400-24n1-16n3+24n7,
3n7-2n3-3n1=(E_odd-6400)/8.

The right side is a multiple of16 and at least272. If n7<=90, the left side is at most270. At n7=91 it is at most273; its sole possible such multiple is272, requiring2n3+3n1=1, impossible in nonnegative integers. Thus n7>=92.

This exhausts the entire below-threshold integer-count range; it is not a chosen histogram, Walsh set or numerical sanity check. All these are actual coefficients of the one input f. This pays S18's lower premise independently of a parent confidence claim.

## 7. Candidate universal blocking inequality, every hypothesis paid

Let C have c points in an affine h-space over F2, h>=2, meeting **every** affine(h-2)-flat. Take an arbitrary affine hyperplane L. If C intersect L failed to affinely span L, it would lie in some affine hyperplane K of L. Over F2 the other parallel coset L\K is an affine(h-2)-flat missing C, contradiction. The empty-intersection case is covered by the same argument; the assumption already forbids it.

Thus C intersect L spans an(h-1)-space and contains at least h points. The complementary affine hyperplane has the same property. Therefore c>=2h, and every nonzero character splits C into two counts each at least h. Its Fourier coefficient has magnitude at most c-2h, independently of the affine origin.

For the indicator of C, Parseval gives

sum_xi |widehat(1_C)(xi)|²=2^h c.

The constant coefficient is c, and there are2^h-1 remaining characters, all bounded by c-2h. Hence

2^h c<=c²+(2^h-1)(c-2h)².

This is valid for the full stated range, including limiting block/cardinality configurations, without selecting an actual set or hyperplane. Finite counts, elementary affine span and character Parseval are the complete imports.

## 8. Application to all original peak sets and the235 bound

Every peak has odd k, so by §4 lies in the affine8-space H={a:a dot T=1}. Let S be the full peak set and C=H\S. By §5 no affine6-flat in H can be contained in S, so C meets every one. The ambient space here is **H of dimension8**, not the full nine-dimensional frequency space.

Apply §7 with h=8. It first yields c>=16. Write the integer c=16+t with t>=0. Substitution gives exactly

256t²-224t-3840>=0.

For every real t in the interval0<=t<=4, t²<=4t, so the left side is at most800t-3840<0 throughout that interval. Therefore such t is impossible; since t is an integer, t>=5. Thus c>=21, and |S|=256-c<=235. This is an interval-wide algebraic contradiction, not evaluation of a selected boundary set.

Combined with §6, this proves the full candidate interval92<=|S|<=235. No equality endpoint, actual flat, object or attained cardinality in that interval is supplied. All zero and nonpeak coefficients remain allowed in C; the complement is not assumed to consist only of nonzero frequencies.

## 9. Caller, unreviewed extensions and assurance

The full proof starts from an **actual balanced Boolean f** and its complete Walsh transform. Parseval/divisibility and the affine blocking property are necessary consequences; satisfying the interval or those isolated constraints does not enforce the exact512 Boolean inverse values or all autocorrelations. The source does not claim otherwise.

- The mandatory w44 M1/M2 overlays and S14 coupled-count correction are retained; they are not counted as newly discovered errors in the already-corrected candidate.
- Full sign/radical classification of all saturated flats, independent forced3-flat existence/sign claims, other local-flat bounds and other half-energy residue filters are not re-adopted merely because their dependency files were supplied/read.
- No essential mathematical dependency remained NR for the **used no-6-flat and lower92/upper235 chain** after the direct proofs above. Parent/status context was not used as a replacement for these proofs.
- Book/source equivalence, latest openness, original unrestricted exclusion, actual NL242 witness, full rank/weight or(24,24,2) closure, priority and novelty remain unproved or unperformed.
- The one-window61LF reading-limit deviation and all prior reviewer/author/parent process findings remain disclosed, without retrospective compliant-coverage or clean-cognition claims.

All S0/STOP/HOLD/ZERO and N4 UNKNOWN/historical child exit unestablished/auxiliary214 STOP limits persist. This is same-harness WRITTEN review only, not formal/kernel/human/configured-family/executable/independent-model acceptance. Main's actual complete operative-source and return reading is still required before adoption. No scientific execution, selected private check, external input or author contact occurred.
