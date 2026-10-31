# f268 DISJOINT REPLACEMENT WRITTEN REVIEW — Sun8 Sections 4–5 (multiplicity bound)

Reviewer: ReviewF268Sun8Multiplicity (new identity; disjoint replacement of f265 obligation B).
Native clock before any input read: `2026-10-30T01:00:41Z` = `Thu Oct 29 18:00:41 PDT 2026` (`/bin/date`).
Native clock immediately before writing this output: `2026-10-30T01:05:26Z` = `Thu Oct 29 18:05:26 PDT 2026`.
Manifest: `.../review-waves/f268-sun8-multiplicity-disjoint-replacement/manifest-v1.json`, SHA256 `12d5765492cc0ae03fef7b4d75944d5311cab5efdeb341b62b792fee003097c7` (4978B/73LF), verified before any body display.

## 0. Verification and exact read coverage

All SHA256/bytes/LF were measured and matched BEFORE the first body display. Every input was then
displayed completely, in the declared order, in raw windows of at most 15 LF including actual endings.
Three windows initially failed on my own path typos and were immediately re-read with the exact path;
the failed reads returned "not found" and exposed no body. Nothing else was opened.

| # | Input (tail) | SHA256 (verified) | B/LF | Display |
|---|---|---|---|---|
| 1 | f265/parent-review-B-selected-control-process-major-v1.json (STATUS ONLY) | e79b23f0…93616 | 2780/22 | raw 1–15, 16–22 |
| 2 | frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json | 6c8f85cf…d793 | 6883/56 | raw 1–15, 16–30, 31–45, 46–56 |
| 3 | frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json | bdd6149c…8d04 | 3056/11 | raw 1–11 |
| 4 | frontier-20261028-alternating-p7-cardinality-addendum-v1.json | 6a9572f4…8218 | 3164/10 | raw 1–10 |
| 5 | frontier-20261029-f243-cyclic-crt-additive-erratum-v1.json | 775e251a…c26e | 2329/12 | raw 1–12 |
| 6 | frontier-20261029-f254-review-b-five-minor-additive-erratum-v1.txt | d95c7cec…44b | 10485/181 | raw 1–15,16–30,31–45,46–60,61–75,76–90,91–105,106–120,121–135,136–150,151–165,166–181 |
| 7 | frontier-20261029-f253-review-b-gcd-additive-erratum-v1.json | c0e21498…40f3 | 2825/25 | raw 1–15, 16–25 |
| 8 | dispositions/math-6-sun8-rough-finite-quotient-arbitrary-kernel-transfer-parent-v1.md | 8feffe5b…286b | 6216/28 | raw 1–15, 16–28 |
| 9 | frontier-20261029-eight-label-extension-consolidated-v1.txt (candidate) | 3b5b1c6b…4e9 | 20185/356 | raw 1–15,16–30,…,346–356 (24 contiguous windows, 1–356) |

Overlays 2–5 and errata 6–7 were read as mandatory ordered context; the f243 CRT correction
(choice of integer lift, quotient map direction) and the f253 gcd-wording correction (pairwise gcd
at least 8, not two large indices) are noted and are not contradicted by anything in my slice.
Input 1 was consumed as STATUS ONLY: no mathematical premise, verdict, count, or wording of the held
old B review (23927B body, never opened) enters this review. No sibling A/C/D output, rejected draft,
held/protected body, transcript, external source, or model was opened. No program, solver, or
computational check was run; no finite selected index tuple, multiset, example, or hypothetical
numeric diagnostic was chosen, including privately. All reasoning below is all-variable; the only
numerals are the literal theorem's own fixed constants (8, 7, 5, 2, 3, 35, 42, 30, 6, 4, 10, 253
does not occur in my slice).

## 1. Assigned scope

Sections 4–5 of the frozen consolidated candidate `3b5b1c6b…4e9` (LF181–210), i.e. the
large-small-prime polarization for p=5,7 under the ORIGINAL factor bounds B_7(N),B_7(Q)≤7; the
outsider injection excluding ≥4 p-labels and then exactly 3; |S_5|,|S_7|≤2; the ≥4 coprime-to-35
original indices and their pairwise gcd set; the saturated case |S_5|=|S_7|=2. The Section 1 lemmas
these two sections actually consume were re-derived independently below ((1.2),(1.3), the
simultaneous-coset lemma, the disjoint⇒non-coprime rule, the product formula). Section 2's exact
identity (2.1) is NOT consumed by Sections 4–5 and is outside this slice; Sections 3, 6, 7 were read
as context only and receive no verdict here beyond what my slice's claims state about them.

## 2. Independent all-variable reconstruction

Hypotheses throughout: G an arbitrary group, N◁G, Q=G/N, π:G→Q; eight pairwise-disjoint nonempty
actual left cosets C_i=g_iU_i of finite-index subgroups U_i≤G ("bad family"); all pairwise original
gcds satisfy 2≤gcd(n_i,n_j)≤7 (upper bound by hypothesis, lower bound forced by Lemma A′ below).
Notation n_i=[G:U_i], a_i=[Q:π(U_i)], b_i=[N:U_i∩N], V_i=π(U_i), A_i=π(g_i)V_i, K_i=U_i∩N.

**Lemma A (simultaneous common point for pairwise-coprime indices).** For finitely many subgroups
H_1,…,H_m of an arbitrary group X with finite pairwise-coprime indices d_i, any prescribed left
cosets x_iH_i have a common point. Proof: x(∩H_i)↦(xH_i)_i injects X/∩H_i into ∏X/H_i, so
[X:∩H_i]≤∏d_i; each d_i divides [X:∩H_i] by the tower formula, and pairwise coprimality gives
∏d_i | [X:∩H_i]; hence equality and surjectivity, so some x hits the prescribed tuple. Unit indices
and repeated labels are covered (a repeated label contributes the same factor twice, harmlessly).
**A′:** two disjoint finite-index left cosets have gcd of indices ≥2 (contrapositive of A for m=2).

**Lemma B (product formula and factor-gcd divisibility, = (1.1),(1.2)).** N◁G makes NU_i a subgroup
and N/(N∩U_i)≈NU_i/U_i as left-coset sets, so n_i=a_i b_i; both factors are finite because each is
at most the finite n_i. For i≠j, with d_A=gcd(a_i,a_j), d_B=gcd(b_i,b_j): writing a_i=d_A a′ etc.,
n_i n_j carry the factor d_A d_B, so d_A d_B | gcd(n_i,n_j). No coprimality of d_A,d_B is needed.

**Lemma C (same-fiber translation, = (1.3)).** If A_i∩A_j∋q, pick one t∈π⁻¹(q). Then C_l∩Nt is
nonempty (l=i,j) and equals x_lK_l for any x_l∈C_l∩Nt (because x_l∈Nt forces x_l⁻¹Nt=N by normality);
right translation by t⁻¹ gives actual left cosets (x_lt⁻¹)(tK_lt⁻¹) of N with subgroup indices
b_l (conjugation by t is an automorphism of N, N being normal). These two cosets are disjoint as
subsets of disjoint C_l. Hence by A′, A_i∩A_j≠∅ ⇒ gcd(b_i,b_j)≥2; combined with Lemma B this is
(1.4): A_i∩A_j≠∅ ⇒ gcd(a_i,a_j)≤⌊7/2⌋=3.

**Theorem P (polarization, Section 4).** Let p∈{5,7} (i.e. 7/2<p≤7 prime) and S_p={i:p|n_i}.
(i) For distinct i,j∈S_p, gcd(n_i,n_j)=p; consequently p² divides at most one n_i.
Proof: p|gcd(n_i,n_j) and gcd≤7; the only multiple of p in [p,7] is p since 2p≥10.
(ii) Exactly one of gcd(a_i,a_j), gcd(b_i,b_j) equals p, the other is 1. Proof: by (i) and Lemma B,
d_A d_B|p, so (d_A,d_B)∈{(1,1),(p,1),(1,p)}; (1,1) is impossible because d_A=1 makes A_i,A_j meet
(Lemma A in Q), forcing d_B≥2 by Lemma C.
(iii) Common side. Give each i∈S_p its nonempty side set T_i⊆{a,b} of sides on which p divides the
corresponding factor (nonempty since p|n_i=a_i b_i). By (ii), T_i∩T_j≠∅ for all pairs. A
pairwise-intersecting family of nonempty subsets of {a,b} has a common element: if some T_j={b},
every T_k meets it, so b∈T_k for k≠j, and any T_k={a} would be disjoint from T_j. Hence all of
S_p carries p on one common side; a both-side label would make another both-side label violate (ii),
so at most one label carries p on both sides.
(iv) Case common side a: p|a_i for all i∈S_p, so d_A=p and d_B=1 pairwise; if some A_i,A_j met,
Lemma C would force gcd(b_i,b_j)≥2, contradiction — so the A_i (i∈S_p) are pairwise-disjoint actual
left cosets of finite-index subgroups of Q with all pairwise quotient-index gcds =p.
Case common side b: d_A=1 pairwise, so by Lemma A all A_i (i∈S_p) share one quotient point q; one
lift t and Lemma C turn the fibers into pairwise-disjoint actual left cosets of N with subgroup
indices b_i and all pairwise kernel-index gcds =p (both factor gcds along the way are exact: d_B=p
since p|b_i,b_j and d_A d_B|p).
(v) Bound (4.1): in case a, if |S_p|≥s+1 those cosets violate B_7(Q)≤s (every pair has gcd p≤7);
in case b, if |S_p|≥r+1 the translated cosets violate B_7(N)≤r. Hence |S_p|≤max(r,s). With the
ORIGINAL bounds r=s=7: |S_p|≤7, in particular |S_p|≠8, so an outsider label j∉S_p exists.

**Theorem O (outsider injection and (5.1)).** Assume B_7(N)≤7 and B_7(Q)≤7. Fix p∈{5,7} and an
outsider j with p∤n_j. For each i∈S_p, gcd(n_i,n_j)≥2 by A′, is ≤7, and is not divisible by p, so
it has a prime divisor q_i∈{2,3,5,7}\{p}, and q_i|n_i, q_i|n_j... in particular q_i|n_i.
Injectivity: if q_i=q_k=q≠p for distinct i,k∈S_p, then the distinct primes p,q both divide n_i and
n_k, so pq|gcd(n_i,n_k)≥10>7 — contradiction. The prime set has three elements, so |S_p|≤3.
Elimination of |S_p|=3: there are 8−3=5 outsider labels. For any outsider m and i∈S_p, the same
construction gives a prime q_{m,i}|gcd(n_m,n_i) with q_{m,i}∈{2,3,5,7}\{p} (p∤n_m), and the same
injectivity argument (a repeated q≠p across two S_p labels would force pq>7 into their gcd) makes
q_{m,·} distinct. Three distinct primes from the three-element set {2,3,5,7}\{p} all divide n_m, so
2·3·7=42 (p=5) or 2·3·5=30 (p=7) divides n_m. Two outsider indices would then have gcd≥30>7,
contradicting the bad-family bound; five outsiders exist, so this is a contradiction. Hence
**|S_5|≤2 and |S_7|≤2** (5.1). The proof used only: bad-family structure, Lemmas A/A′/B/C, and the
factor bounds ≤7 via Theorem P(v). No normality of quotient subgroups, no solvability, no finiteness
of G, no distinctness of the U_i, no selection of indices, and no factor bound ≤2 was used;
repeated labels are covered by Lemma A.

**Corollary C1 (coprime-to-35 block).** |S_5∪S_7|≤|S_5|+|S_7|≤4, so at least 8−4=4 original
indices are coprime to 35. Any pair among these labels has gcd ≥2 (A′), ≤7, and divisible by
neither 5 nor 7, hence gcd∈{2,3,4,6}; four such labels give at least C(4,2)=6 pairs so constrained
(more labels only add pairs).

**Corollary C2 (saturated case |S_5|=|S_7|=2).** Let m be outside S_5∪S_7 (there are at least
8−4=4 such labels, more if some single label lies in both S_p, which can happen for at most one
label since 35|n would give gcd≥35 pairwise). For the two labels i₁,i₂∈S_5 and l∈{1,2}: a prime
q_{m,i_l} divides gcd(n_m,n_{i_l}); it is not 5 (m∉S_5) and not >7, so lies in {2,3,7}; and
q_{m,i₁}≠q_{m,i₂}, since a common q≠5 together with 5|n_{i₁},n_{i₂} would force 5q≥10 into
gcd(n_{i₁},n_{i₂}). So n_m carries two distinct primes of {2,3,7}; as m∉S_7, 7∤n_m, forcing both 2
and 3: **6|n_m**. Any two such labels m,m′ have gcd(n_m,n_m′)≥6, ≤7, and free of 5 and 7, so
gcd∈{6}; all pairwise original gcds among the ≥4 outside labels are exactly 6.

## 3. Per-claim verdicts (assigned slice)

| Claim (candidate location) | Verdict | Basis (my proof above) |
|---|---|---|
| gcd(n_i,n_j)=p on S_p; p² divides ≤1 index (§4) | SUPPORTED | Thm P(i) |
| exactly one of gcd(a_i,a_j),gcd(b_i,b_j) is p (§4) | SUPPORTED | Thm P(ii) |
| common-side polarization; ≤1 both-side label (§4) | SUPPORTED | Thm P(iii) |
| case a: A_i pairwise disjoint, quotient gcds =p (§4) | SUPPORTED | Thm P(iv) |
| case b: common quotient point; translated disjoint kernel fibers, kernel gcds =p (§4) | SUPPORTED | Thm P(iv), Lemmas A,C |
| (4.1) |S_p|≤max(r,s), in particular ≠8 at r=s=7 (§4) | SUPPORTED as a conditional necessity (factor bounds are hypotheses) | Thm P(v) |
| §4 lemma citations (1.2),(1.3), coprime common point, disjoint⇒gcd≥2 | SUPPORTED | Lemmas A/A′/B/C |
| outsider exists; q_i∈{2,3,5,7}\{p}; q_i pairwise distinct; |S_p|≤3 (§5) | SUPPORTED | Thm O, first half |
| |S_p|=3 impossible via 42/30 divisibility and ≥2 outsiders (§5) | SUPPORTED | Thm O, second half |
| (5.1) |S_5|≤2, |S_7|≤2 under B_7(N),B_7(Q)≤7 only (§5) | SUPPORTED | Thm O |
| ≥4 original indices coprime to 35; their ≥6 pairs have gcd∈{2,3,4,6} (§5 consequences) | SUPPORTED | Corollary C1 |
| saturated |S_5|=|S_7|=2 ⇒ every outside index divisible by 6; ≥4 such labels; pairwise gcds exactly 6 (§5 consequences) | SUPPORTED | Corollary C2 |
| "no assumption on quotient normality, solubility, finite G, distinct subgroups, selected indices, or factor B_7≤2" (§5) | SUPPORTED | my reconstruction used none of these |
| "None of these statements rules out a bad eight-family" (§5) | SUPPORTED | all statements derived are one-directional necessities inside a hypothetical family; no exclusion proved here |
| §7 sentence "Sections 3–5 apply to that actual normal cut" (context) | CONDITIONAL | accurate as a citation of my slice PROVIDED the Section 1 reductions hold in that cut; §7's own minimality argument is outside this slice |

Necessary-only scope CONFIRMED: every §4–5 statement is of the form "within any bad family with the
original factor bounds, such-and-so multiplicity/divisibility/gcd pattern must hold". No existence of
a bad family, no exclusion of one, no unrestricted/global Sun8, no factor bound ≤2, and no
realizability claim is asserted or needed; the candidate's own disclaimers to that effect match what
the proofs deliver.

## 4. Findings

**FATAL 0 / MAJOR 0 / MINOR 0** in the assigned Sections 4–5 scope (including the Section 1 lemmas
they consume). Two non-finding reading notes, no mathematical content affected: (a) §4's phrase
"these nonempty subsets of the two sides are pairwise intersecting" refers to the per-label side
sets T_i⊆{a,b}; read that way (the only way consistent with the surrounding sentences) it is exactly
my Theorem P(iii); (b) §5's "the three distinct q_i" for an outsider m compresses the identical
injection argument re-run per outside label (my q_{m,i}); the surrounding text ("apply the
three-prime injection above") says so itself. Neither note is a MINOR: no false statement, no
ambiguous quantifier changing truth value, no hidden hypothesis.

## 5. Boundary

Old B body, its counts and every consumer remain HELD/ZERO/NONINPUT and unused; input 1 gave status
only. No sibling A/C/D material, rejected draft, protected payload, external source or model, Git
operation, deletion, source edit, or publication. Historical provenance, priority, the unrestricted
Sun8 problem, existence/exclusion of bad families, Sections 2, 3, 6, 7 and the nilpotent
specialization are outside this review's result. This is same-harness written mathematics; no
human, independent-family, formal/Lean, or novelty acceptance is claimed, and no prior verdict is
rehabilitated. Output written once into this wave's exclusive path; immutable after publication.
