# Review w81 — full-spectrum projective-code source/claim gate

**Reviewer:** MathSemigroup-2, math-4. **Author:** InfoBalancedNL242-2-2, info-6.

Actual first review wake: **Tue Oct 27 17:00:55 PDT 2026**. Actual pre-body ACK observation: **17:01:11**. Actual native observation immediately before writing: **Tue Oct 27 17:03:45 PDT 2026**.

## 1. Verdict and counts

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** in the full candidate S13, `walsh-projective-code-equivalence-v1.md`.

- FATAL mathematical findings: **0**.
- MAJOR mathematical findings: **0**.
- MINOR mathematical findings: **0**.

The two original-object existence directions, generator conditions, weight moments, every dual-index character identity, divisibility, D1=D2=D256=0 and the stated D3 interval are correct. Their operative proofs are elementary character/finite-count arguments reconstructed below, not coding-theory black boxes.

**Gate limit:** this assesses the exact mathematical reconstruction from the supplied Boolean definitions. It does **not** certify historical private method noninfluence, admit a dual-enumerator primary continuation, prove a feasible weight distribution/code exists, or produce a Boolean witness or unrestricted no-go. All author/reviewer/parent STOP and quarantine records remain binding.

## 2. Required order, full coverage and exposure

I read all S0 and the complete frozen manifest (`61211edef3f79ac8412a926538cbab36ed6f55d267217b3a3524ec765be68598`) first. Before any packet body or mathematics I wrote the designated exposure ACK, SHA `a37eea4f732c7f04bdf8f80be7417593028cb0bad6a3ad7efab2a4905db3a53a`, actual17:01:11.

Then I read **all489LF / 51741 bytes** of the exact packet, SHA `2a34c1b8e75785832971e5b044f7f567c6a0a567a501ab09a17cb47abcee4aec`, through all thirteen endings in raw windows1–60,61–120,121–180,181–240,241–300,301–360,361–420,421–480,481–489. No window exceeds60LF and no long-line/ending omission remains.

| Outer source / role | Complete LF | Scope in this review |
|---|---:|---|
| S1 | 23 | Binding parent L1 quarantine, not proof. |
| S2 | 21 | Binding L1 recipient-frontier qualification, not proof. |
| S3 | 35 | Literal original Boolean/Walsh target definitions. |
| S4 | 18 | Binding post052 cross-sector method hold. |
| S5 | 17 | Binding post054 selected-diagnostic hold. |
| S6 | 15 | Binding half-split method stop. |
| S7 | 15 | Binding global-degree/ANF method stop. |
| S8 | 87 | Used Boolean/Walsh/mod4 dependencies. |
| S9 | 49 | Used half-energy divisibility dependency. |
| S10 | 28 | Used lower92 dependency, only with S12. |
| S11 | 49 | Used polynomial-weight/T!=0 dependency, only with S12. |
| S12 | 30 | Mandatory coupled-count correction. |
| S13 | 50 | Complete candidate under review, SHA `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb`. |

Prior w68 and closed-round NL review exposure survives; no old favorable verdict is used as a proof. The new author holds are read as status without recovering their private formulas, choices or diagnostic outcomes. Parent L1 itself/payload, stopped sectors/ANF/half-split guides and all consumers are NONINPUT. Own semigroup method STOP, QOA source-scope MINOR, earlier reading/process findings and all other quarantines remain. This is not blind, independent-model or clean-cognition evidence.

No chosen function, actual code/generator, spectrum/weight distribution, particular frequency/subspace, group/graph/state or numerical sanity probe was constructed or tested even privately. All arguments below quantify over the entire stated actual-object classes. No scientific interpreter/calculator/Eval/CAS, enumeration, solver, replay, test, CLI, nested task, external source, old/held body or author contact. Only the required ACK and this review were written.

## 3. Statement-by-statement dispositions

| Claim / S13 reference | Verdict and exact boundary |
|---|---|
| Boolean-to-code direction including translation, LF7–13 | CORRECT: translation is an existential symmetry over all points outside the one-support, removes the zero column without changing balance/peak, and the weight lower endpoint forces rank9. |
| Code-to-Boolean direction, LF15–17 | CORRECT: actual256 distinct nonzero columns define256 actual one-bits in F2^9; full rank and every nonzero word's **two-sided** weight window pay the full Walsh caller. |
| Dimension/length/generator hypotheses, LF7/13/15 | ESSENTIAL and correctly retained: repeated/zero columns or only a minimum-distance condition are not a replacement. No selected old rank/type is fixed. |
| Moments LF21–23 | CORRECT: sum A=511, sum tA=128 and sum t²A=16384. The zero codeword is omitted from A and must be handled separately in the calculation. |
| Odd/even counts and at-least92 peaks, LF25–28 | CORRECT with S12's count correction and the actual lower-bound chain reconstructed in §6. |
| All j dual identities/divisibility, LF30–38 | CORRECT simultaneously for j=0,...,256 by explicit character counting; no MacWilliams/Krawtchouk theorem is imported. |
| D1,D2,D256 vanishing, LF38 | CORRECT from distinct nonzero columns and actual nonzero truth-support XOR T. |
| D3 interpretation, third moment and interval, LF40–44 | CORRECT, including the zero-word third-moment correction and integer rounding. |
| Original-target/source gate limits, LF17/38/44/48–50 | ACCURATE: exact representation and necessary conditions do not establish realization, independent provenance or new primary permission. |

## 4. Original Boolean caller and both code directions

### 4.1 Literal target, signs and translation

For actual f:V=F2^9->{0,1}, let s=(-1)^f and W_f(a)=sum_x s(x)(-1)^(a dot x). Character orthogonality gives the inverse on every one of the512 points. Comparing the signs to every affine Boolean function gives

NL(f)=256-(1/2)max_a|W_f(a)|.

Thus balance W_f(0)=0 and full peak<=28 are exactly the bound target. No spectral profile alone is used as an actual Boolean input.

Let D={x:f(x)=1}, |D|=256. For **every** t outside D, f_t(x)=f(x+t) has one-support D+t not containing0. Such t exists because the complement has256 points. Substitution in the character sum gives W_(f_t)(a)=chi_a(t)W_f(a); balance and all magnitudes are preserved. This does not select/evaluate a translation or assert preservation of an earlier decomposition label. It is an existence-preserving symmetry of the unrestricted original question.

### 4.2 Forward code and rank

List the256 distinct nonzero vectors of D+t as columns of G. For every a!=0, the full-space character sum vanishes and

W_(1_D)(a)=-2 sum_(x in D)chi_a(x)
          =-2(256-2w(a^T G))=4(w(a^T G)-128).

Here D denotes the translated support when applying the forward direction. Peak<=28 gives121<=w(a^T G)<=135, so no nonzero a maps to the zero word. Therefore a->a^T G is injective and G has rank9. Its image is a binary dimension9 length256 code with the stipulated generator columns and **all** nonzero word weights in the window.

### 4.3 Converse and essential hypotheses

Take an actual code of the stipulated dimension and a full-row-rank generator G with the stipulated256 distinct nonzero columns. Their set D has exactly256 points; f=1_D is an actual balanced Boolean function on all512 inputs and has f(0)=0. Full rank ensures a!=0 gives a nonzero codeword. Applying the same exact formula to every such a gives |W_f(a)|<=28, and W_f(0)=0 follows from balance. The full Boolean object, not merely its magnitudes, has been defined.

Both the lower and upper codeword weight bounds are required: the formula depends on absolute distance from128. The zero word is not subject to the window. Distinctness ensures an actual set of256 truth points, while nonzero columns impose the chosen origin exclusion. Neither is dispensable in this stated equivalence.

Changing the generator basis by GL(9,2) preserves nonzero/distinct columns and parametrizes the same codeword set, so the condition is not a hidden fixed coordinate frame. No coding classification or old sector premise is used. This is an **existence equivalence**, not a pointwise one-to-one correspondence with every untranslated f or preservation of a selected historical type.

## 5. All weight moments, every dual index and D3

Put J(a)=sum_(x in D)chi_a(x) and u(a)=w(a^T G)-128=-J(a)/2, now for **all** messages a including0. Since the columns are nonzero,

sum_a J(a)=0.

Since they are distinct, character orthogonality gives

sum_a J(a)^2=512·256.

At a=0 the zero codeword has u(0)=-128. Removing that one message yields exactly

sum_t A_t=511,
sum_t t A_t=128,
sum_t t² A_t=16384.

The nonzero-frequency formula W_f=4u is **not** applied at a=0: W_f(0)=0, whereas u(0)=-128. This distinction pays the nonzero first moment and the later third-moment constant.

### 5.1 Entire dual character identity

For a binary position vector v of weight j, v belongs to C-perpendicular iff Gv=0. Nondegenerate character orthogonality gives its indicator as

1_(Gv=0)=(1/512)sum_(a in V)(-1)^(a dot Gv).

Sum this over **all** j-subsets of the256 coordinate positions. For fixed a of codeword weight w, choosing i positions from its ones and j-i from its zeros gives

sum_i (-1)^i binom(w,i)binom(256-w,j-i)=K_j(w),

with the standard zero convention outside valid binomial ranges. The zero message contributes K_j(0)=binom(256,j); the remaining messages contribute the A_t sum. Thus for every j at once,

512D_j=binom(256,j)+sum_t A_t K_j(128+t).

This is a direct finite character count, not an imported coding-theory transform. It includes j=0 (the dual zero vector) and j=256, and proves nonnegative512-divisibility because D_j is an actual integer subset count. It does not grant independent freedom to choose different dual data for different j.

### 5.2 Endpoint dual constraints

A weight1 dual vector would give a zero generator column, impossible. A weight2 dual vector would give two equal binary columns, impossible. Hence D1=D2=0.

The only weight256 position vector is all ones, whose column sum is T=sum_D x. Once the actual T!=0 premise is paid in §6, that vector is not dual, giving D256=0. This is not confused with whether the **primal** code contains its own all-ones word.

### 5.3 Third moment and exact integer bounds

D3 counts exactly unordered three-column subsets with XOR0. In the expansion of sum_a J(a)^3, a repeated-column triple cannot have XOR0 because no column is zero. Every contributing ordered triple therefore has three distinct entries, accounting for all six orders of one such subset. Orthogonality gives

sum_a J(a)^3=512·6D3,
sum_a u(a)^3=-384D3.

Removing u(0)^3=-2^21 gives

sum_t t³ A_t=2^21-384D3.

The window |t|<=7 implies |sum t³A_t|<=7 sum t²A_t=7·2^14. Therefore

(2^21-7·2^14)/384<=D3<=(2^21+7·2^14)/384.

The left endpoint is15488/3 and the right endpoint5760. D3 is an integer, so precisely5163<=D3<=5760 follows. These are universal algebraic consequences for the full class, not a tested code, distribution or parameter instance. Nothing contradicts existence merely from this interval.

## 6. Used truth-XOR and lower92 chain, with the correction

The parent-notified bounds are not used as a proof shortcut. For the actual balanced f, W/4=k is integral by

W(a)=512·1_(a=0)-512+4n_a,

where n_a counts the support points with a dot x=1. Hence k(0)=0, sum k²=2^14, and k(a) mod2=a dot T. The shared XOR expansion modulo4 gives the bilinear residue identity in S8:59–75. On any linear subspace of T-perpendicular, Q=k/2 modulo2 is Boolean quadratic with Q(0)=0.

For a nonzero polynomial of degree at most2, the supplied elementary induction gives weight at least a quarter of the space: separate the last variable; if its derivative vanishes double the smaller-space count, otherwise each true derivative fibre contributes once and apply induction at one lower degree. Applying this to1+Q gives a Q-zero count of at least a quarter.

If T=0, let q count Q-ones in the whole512-point frequency space, q<=384. **Use S12's coupled complement511-q**, not the superseded independent127 bound. The even |k| bound gives

sum k²<=36q+16(511-q)<=15856<2^14,

contradicting energy. Thus T!=0. Translation of the original support by any t preserves T, since its even cardinality256 makes sum_(D+t)x=T+256t=T; equivalently the newly constructed indicator itself satisfies the same theorem.

Consequently exactly256 frequencies have k odd, all on one affine half; zero frequency is even. Since t in A_t is k(a) at nonzero messages, this proves sum_(t odd)A_t=256 and sum_(t even)A_t=255.

For the stronger peak count, take the actual K=T-perpendicular. With q<=192 Q-ones there, use the corrected exact complement255-q to get E_K<=36q+16(255-q)<=7920.

For every nonzero direction z, character orthogonality on z-perpendicular expresses the local transform on its opposite frequency half as-128 chi_a0(x)(f(x)-f(x+z)), indexed by source pairs{x,x+z}. Its half-energy is64m_z, where m_z counts disagreeing pairs. Balance makes m_z even, so every half-energy is divisible by128. This is an arbitrary-direction proof, not a chosen frequency test.

Thus E_K<=7808 and E_odd>=8576, both multiples of128. If n_j counts odd-half |k|=j, j in{1,3,5,7}, then

3n7-2n3-3n1=(E_odd-6400)/8

is a multiple of16 and at least272. Values n7<=90 cannot reach272; n7=91 would require the only possible multiple272 and therefore2n3+3n1=1, impossible in nonnegative integers. This exhausts the below92 count range, so n7>=92. Under the exact code/Walsh formula these peaks are A_-7+A_7, paying S13:27–28 without an independent histogram assumption or a transferred w68 verdict.

Only these used dependency statements are exported here. The separate unused residue/congruence/phase and autocorrelation-converse extensions in those files are not blanket-adopted by this review.

## 7. Provenance gate and original-target limits

No load-bearing mathematical dependency remained NOT_RECONSTRUCTED for the candidate's stated equivalence/moments/dual constraints after the proofs above. Coding words such as projective or K_j are defined by actual generator columns and the displayed finite sum; no external enumerator theorem or coding table is used.

Mathematical correctness from those definitions does **not** establish that the author's current method/selection was historically independent of the post052, post054, half-split or global-degree episodes. S1/S2/S4–S7 remain binding. No protected formula, diagnostic value or consumer was recovered to assess them. This review itself gives no prospective primary/dual-enumerator release.

In particular:

- the code must actually exist with **all** columns and **all** nonzero word weights satisfying the hypotheses;
- integer weight counts and every displayed dual constraint are necessary only, not sufficient code or Boolean realization;
- no particular spectrum, weight distribution or dual vector was selected/generated;
- no original Boolean witness, unrestricted no-go, whole rank/weight or(24,24,2) closure, numerical nonlinearity improvement, book-source equivalence, SOTA or novelty result follows;
- the old held u8/L14/d128, sector/ANF and Gate-I routes remain NONINPUT.

All parent L1 quarantine, author/reviewer method STOPs, own source-scope MINOR/reading findings, HOLDv2, N4 UNKNOWN/historical child exit unestablished and auxiliary214 STOP remain. This is same-harness WRITTEN source/claim reconstruction only—not Main adoption, formal/kernel/human/configured-family/executable/independent-model or novelty acceptance. Main must read the complete operative sources and this return before adoption, and separately adjudicate any future source/method permission.
