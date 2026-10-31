# Global balanced-NL242 equivalence: an actual projective binary code, its hull and a nonextension barrier

Owner InfoBalancedNL242-2. Latest actual `/bin/date` returned BEFORE this write: **Mon Oct 26 06:09:34 PDT 2026**. This is an observation bound, not an invented exact creation instant. **WRITTEN AUTHOR CANDIDATE**, not reviewed/adopted, formal/kernel checked, executed, novelty/SOTA-cleared or a solution. Exact symbols/fractions/integer products only; no scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/CLI/nested agent or GO.

The code-equivalence/hull/fibre leads were ALREADY exposed and saved in whole-primary checkpoints028/030 before the last reviews. This manuscript writes the full Boolean/application bridge, not a fictitious post-ACK discovery or preregistration. New code-dual minimum/nonextension details below were derived after actual v118-D RETURN and NEW whole-primary031 ACK was WRITTEN and SENT. No own-primary proof expansion occurred during a live review.

## 1. Exact equivalence — ACTUAL code, not a weight table

The original target is a balanced f:F2^9->F2, weight256, with ALL512 Walsh magnitudes<=28. Define a binary code from its ACTUAL support S:

```text
C_S={ (b+a.x)_(x inS): a inF2^9,b inF2 } subsetF2^256.
```

**Theorem C.** The original target exists IFF there exists an ACTUAL binary linear code C of length256 and dimension10, containing the all-ones vector, with minimum distance at least121 and with no zero/repeated generator columns. Equivalently its dual minimum distance is at least4. The generator-column condition is independent of basis; over F2, 'projective' means exactly nonzero/distinct columns.

Every such C in fact has minimum distance EXACTLY121, is not an even code, has dual minimum distance EXACTLY4, and has the nonextension property proved in §6. These are necessary consequences, not existence claims. A formal weight enumerator, LP vector, hull dimension or a code-name/catalogue citation does NOT supply an actual C.

### 1.1 Forward direction and every nonzero frequency

A target S has full affine rank9. Otherwise its256 points lie in an affine hyperplane of size256, hence ARE that hyperplane, yielding a Walsh magnitude512. Thus the ten affine-evaluation rows1,x1,...,x9 are independent and C_S has dimension10. Its columns are(1,x), x inS, which are distinct/nonzero; all-ones belongs to the code.

For ANY a!=0 put n_a=|{x inS:a.x=1}|. Since both f and a.x have weight256,

```text
W_f(a)=512-2[512-2n_a]=4n_a-512.                         (1)
```

The cap gives121<=n_a<=135. Adding the ones codeword complements n_a to256-n_a, in the same interval. All other codewords are0 andones. Therefore d(C_S)>=121. Formula(1) does NOT apply to a0, which is handled separately; balance gives W_f(0)=0.

No dual word of weight1 or2 exists because the columns are nonzero/distinct. All dual words have EVEN weight becauseones is in C, so d(Cperp)>=4.

### 1.2 Converse and literal ALL512 Boolean reconstruction

Let an ACTUAL rank10 generator matrix for C have its first rowones, with nine other rows. For coordinate j, let x_j inF2^9 be the nine-bit column below the first row. Projectivity makes all256 x_j DISTINCT. Define the full truth table

```text
f(x)=1 iff x is one of these ACTUAL256 labels x_j,
f(x)=0 at every other x inF2^9.                           (2)
```

This specifies every bit and gives weight256. For every a!=0 the affine evaluation word on those columns is neither0 norones: either equality would contradict rank10 of the displayed generator rows. Its weight and its complement's weight are at least121, so both lie in[121,135]. Formula(1) gives |W_f(a)|<=28 for EVERY nonzero a, and balance gives origin0. Hence (2) is a genuine Boolean target, not independent Fourier modes glued together.

A natural literal-bit convention is x=(x1,...,x8,t), integer index `sum_(i=1)^8 2^(i-1)xi+256t`. One must supply the actual matrix/columns, not just a claimed weight distribution, to use this reconstruction. Column permutations do not change S; a different affine row basis gives an actual affine input transformation, not a fixed-half restriction.

## 2. Minimum EXACTLY121, oddness, and no imported covering-radius claim

The original elementary support-XOR lemma says s=XOR(S)!=0 under cap28. If s0, all balanced Walsh coefficients are divisible by8; their next parity is quadratic with value0 at origin. At least128 coefficients then have magnitude<=16, others<=24, giving the strict Parseval upper bound253952<262144. This is the existing support-moment proof, not a replay or adoption of a covering-radius preprint.

For C_S, weight parity of the a.x word is a.s. Thus C_S is NOT entirely even; parity is a nonzero linear functional on C.

If d(C)>=122, the converse would instead give Walsh cap24. For s!=0, exactly256 frequencies lie in s-perp and have coefficients0mod8, hence magnitude<=24; the other256 have coefficients4mod8, hence magnitude<=20. Parseval would be at most

```text
256*(24²+20²) < 256*32²=512²,
```

since576+400<1024. If s0 the previous support-moment bound already contradicts cap24. Thus d(C)>=122 is impossible here. Every target code has minimum EXACTLY121, and the corresponding Boolean target has peak EXACTLY28. No unrestricted nonlinearity result or finite experiment is imported.

The dual minimum is also EXACTLY4. Distinct unordered pairs of256 support points give more than511 pair sums, whereas F2^9 has only511 nonzero vectors. Equal sums of two DIFFERENT unordered pairs cannot share a point, since then the other point would coincide. They therefore supply four DISTINCT columns summing0, a dual word of weight4. This uses pigeonhole, not enumeration of those pairs. Along with d(Cperp)>=4 it proves exact4.

## 3. The ACTUAL Gram/hull and intrinsic quadratic agree

Write s=e_t after an actual linear input change and use the code generator rows(1,x1,...,x8,t). Define the ACTUAL support moments overF2

```text
M_ij=sum_(x,t inS) xi xj,   c_i=sum_(x,t inS) xi t.
```

All x first moments are0, t's first moment is1, and the total support parity is0. Hence its generator Gram is

```text
G G^T = [0   0    1]
        [0   M    c]
        [1   c^T  1].                                   (3)
```

M is alternating: its diagonal equals the x first moments0. Adding c_i times the ones row to the xi row kills the xi/t cross entry because1.t=1, without changing M or the xi/ones entries. This is an actual generator-basis/input-translation operation, not diagonalization of independent streams. The congruent form is

```text
M directsum [0 1;1 1].
```

Thus if rank(M)=2r, rank(GG^T)=2r+2. Full row rank10 of G identifies the hull with the kernel of this Gram, giving

```text
dim(C intersectCperp)=8-2r.                              (4)
```

To identify M with the ORIGINAL intrinsic residue, take the even subcode C0=ker(weight parity). It has dimension9 and rows1,x1,...,x8. For every even codeword c set

```text
q_C(c)=wt(c)/2 mod2.
```

The identity wt(c+d)=wt(c)+wt(d)-2|supp(c) intersectsupp(d)| gives its polar as the ACTUAL binary inner product. Ones lies in its radical and q_C(ones)=128mod2=0; addingones leaves q_C unchanged. Hence q_C descends to the8-dimensional quotient C0/<ones>.

For a!=0 in s-perp, the evaluation word has weight n_a=128+W_f(a)/4 by(1), so

```text
q_C(a.x modones)=W_f(a)/8 mod2=Q(a).                      (5)
```

Both sides are0 at a0. Thus the quotient quadratic is EXACTLY the intrinsic Q, not merely a form with the same rank or histogram. Its polar is M. The actual code's affine choice/sign half-moments determine Q's affine part; rank and Arf/radical-linear behaviour are not freely chosen parameters.

The positive-polar-rank canonical-capacity lemma remains at its actual ordinary-WRITTEN source boundary; it gives1<=r<=4 for a target. Therefore the four possible full hull dimensions here are6,4,2,0. The completed proper rank2/U2 theorem would remove hull6 ONLY CONDITIONALLY at FULL J_U2; this representation does not promote that gate to an unconditional all-residue theorem.

There is also an exact radical relation. Hull(C) is contained in C0 and in rad(C0), because every hull word is orthogonal toones and all C0. Ones is NOT in Hull(C), since C is odd. Dimensions from(3)–(5) give

```text
rad(C0)=Hull(C) directsum<ones>.
```

The quadratic may be nonzero on this radical. Do NOT assume every hull is doubly even or use that false shortcut to eliminate intrinsic weight128.

## 4. Full weight enumerator, Gauss sum and why counts do not suffice

Let N_j count ALL512 original Walsh magnitudes, j0,4,8,12,16,20,24,28. The COMPLETE code weight distribution is forced by(1) and the actual complement pairing:

```text
A0=A256=1,
A128=2(N0-1),
A_(128-j/4)=A_(128+j/4)=N_j for each j>0,
all other A_w=0.                                        (6)
```

The subtraction of1 in A128 removes the a0 Fourier zero, whose codewords are0 andones rather than two weight128 words. Formula(6) retains all1024 affine codewords; it is not an assumed symmetry of f's signed spectrum.

Thus L=N4+N12=A127+A125, intrinsic d=N8+N24=A126+A122, and u=N0+2N8=1+A128/2+2A126. These are useful dictionary identities, not another numerical type elimination.

On C0, (5) gives exactly2d words with q_C1, so its signed quadratic sum is512-4d. On all C, odd-weight words cancel in pairs c,c+ones in sum i^wt(c), since length256 is0mod4. Therefore

```text
sum_(c inC) i^wt(c)=512-4d.                              (7)
```

This ties the physical residue type to the SAME code/hull/quadratic data. It does not prove that any proposed A_w, Gauss value or hull tuple is realized by a binary code with the actual columns and minimum distance. A MacWilliams/LP solution would still need the full generator, distinct-column condition and Boolean reconstruction. No code catalogue, LP solve, coefficient/profile test or numeric-parameter scout was run.

## 5. Folded fibres — an EXACT common-object extension problem

Project S along its actual exceptional direction s. In coordinates(x,t), let n_x be the number0,1 or2 of selected support points in that pair. Balance gives sum n_x=256, hence the counts of n0 and n2 fibres coincide. Define

```text
h(x)=D_s f(x)=n_x mod2,
e(x)=1-n_x in{1,0,-1}.
```

Then sum e=0, and the original even-sector spectrum is exactly R=2H8 e. The even subcode is weighted affine evaluation on these SAME multiplicities n_x. The odd code extension decides WHICH point occurs in a singleton fibre; empty fibres choose neither and double fibres choose both. It is not allowed to pick an independently admissible odd spectrum or a separately realizable sign pattern.

The derivative h has the degree6 leading tensor in the earlier ANF manuscript; its dual coefficient matrix is M. This connects the code extension to the literal high-degree normal form `P8+tC_r+rho_le6`, not to a magnitude table. Actual codewords, both Boolean inverse sectors, prescribed XOR/phase/carry information and all512 bits remain one object.

No proof currently constructs the odd extension at minimum121 or excludes all such extensions for r2/r3/r4. That is a precise original feasibility barrier, not an omitted computational step assumed complete.

## 6. A genuine global geometric barrier: the dual cannot be extended as an even distance4 code

Every target must satisfy S+S=F2^9. If some nonzero v is absent from S+S, then S and S+v are disjoint256-sets, hence complements. Therefore f(x+v)=1+f(x) for every x. Its Walsh spectrum is supported only on the256 characters with a.v=1. The cap28 gives total square energy at most256*28²<512², contradicting Parseval. This is an exact ALL-direction statement, not a selected-affine-flat example.

Equivalently, C has NO9-dimensional projective subcode B containingones. Such a B has a generator with first rowones and eight further rows; projectivity on256 coordinates makes its256 eight-bit column labels ALL of F2^8. Thus B is literally the full affine-evaluation code RM(1,8), up to coordinate order. Adding a tenth generator v gives C=B+<v>. The minimum weight in that new coset is the nonlinearity of the actual8-bit table v, at most120 by its Boolean Parseval/bent bound. This contradicts d(C)=121. The argument does NOT presume all projective C contain such a B.

In dual language D=Cperp is an even `[256,246,4]` code that is MAXIMAL among even linear distance-at-least4 supercodes. If an even247-dimensional E of distance>=4 contained D, then B=Eperp would be a9-dimensional projective subcode of C containingones, just ruled out. Any larger even supercode contains such a one-step extension, so is also impossible. This is a necessary nonextension property, not an imported classification saying all such D extend.

The exact next obstruction would be a theorem that no ACTUAL projective odd self-complementary `[256,10,121]` code with these coupled quadratic/hull data exists, or an actual generator realizing one. The extension barrier shows why simply assuming an RM(1,8) subcode/graph half/extended-Hamming completion would silently discard the target. No such universal extension theorem is proved or used here.

## 7. Current mathematical scope, imports and continuing original work

This manuscript gives an exact ALL-target code equivalence with literal512-bit reconstruction, the intrinsic quotient-quadratic/hull bridge, and the global no-RM-subcode/even-dual-nonextension barrier. These are source-level written candidates, not new solved-problem counts. Boolean-function/linear-code correspondences and the cited elementary tools may be prior art; novelty/priority/SOTA is UNCLEARED and not screened by this packet.

Ordinary inputs are affine evaluation, finite binary linear/Gram duality, character sums/Parseval, even-code weight parity and the existing canonical support-XOR/positive-polar-rank lemmas. The model-specific application/column/quotient/hull/extension bridges are displayed. No external best-code bound/catalogue, classification of maximal even codes, unadmitted finite object, native output or signed-eight table supplies a hidden new proof direction.

The original Walsh target and governing import boundaries are in selection-v1.md (`26b94d67d87778c8630b04bfe2b86ce105377517c7c72b449eb5539eac49d84b`), modular-saturation-protocol-v1.md (`d485c6da50c7c4c19b86ad198c7d0b6018c95334ac6a0164784b763e7091e032`) and quadratic-distance/SHARPER.md (`bfd1cea494b42f7c016cbf174772940dff4afaf2460735779e299ab095f44601`). The ANF bridge is the NEW unreviewed `global-degree8-unique-derivative-normalform-v1.md`, SHA256 `b97d004fec67f292dd559c8faadab852a7cf1a064c4fe40be5b1f90cef4e0951`; code equivalence and quotient identification were proved directly here rather than assumed from its hash.

The existing rank2 CASE32/unpruned U2 composition remains ONLY CONDITIONAL at FULL J_U2/E116/canonical/JN/J20 and all historical imports/M1/M2. No smaller dependency set, original all-residue/global pruning, actual code/truth table or numerical NL bound follows from this new language. Stronger formal/kernel/human/configured-family/executable/finite-triple and novelty gates remain unperformed. Any actual generator witness would still need the separately admitted independent definition-level verification route; no executable assay is authorized.

Original global research CONTINUES at actual code/low-degree correction geometry. The broad lower-degree polynomial and code extension problems remain unresolved; a profile, generic-dimension claim, timeout or repeated conditional gate is not completion. This is a parkable incremental source, not an early final park.

All permanent own exactness/ZERO withdrawn RQLS scout/no-guidance, documentary14-not15, older cadence/v105 false quotation and parent/owner read/freeze/root/ACK/inventory/admission/exit findings remain. The scout is not evidence or guidance for this unrelated code derivation. No current scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/build/test/CLI/nested agent/new GO or approximate private magnitude probe occurred. Exact clock/hash/source metadata and own-root writes only; no global clean-thought/runtime census. Same18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38.
