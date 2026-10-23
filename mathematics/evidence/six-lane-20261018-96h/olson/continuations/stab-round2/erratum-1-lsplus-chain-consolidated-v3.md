# Erratum 1 (consolidated) to the LS+ chain package (lsplus-chain-review-package-v1.md 99df68744f5b963cdc356f0d21024fe4f448a63ea886880dc40468ce7998e2fc), v3

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T07:34:47-0700.  v3 supersedes v1 (erratum-1-lsplus-chain-consolidated.md
a5093853ad5bec58eb5423de071f0d0b20a17c9a2cc35c2a0c22a9fa267b9ed1) and v2 (erratum-1-lsplus-chain-consolidated-v2.md b831c94aeb6e8d4511f4292ee468d20afd5ab46bbc659d98c2aeb268003598a0), neither sent.
Exact differences from v1 (checked with diff): the cross-reference list in C0 is corrected (the BASE1+ relabel is in C14, not
C13), and in C13 'long zero-sub-sequence' reads 'long zero-sum subsequence' (wording only).  v2's header sentence 'nothing else
changed' omitted the C13 wording change; v3 corrects that sentence and is otherwise identical to v2.  Disposes BOTH chain reviews, frozen in run review/olson-LSplus-chain-review-freeze-v1.json
(95a5514dd2c071a38744f555f1481c651850969d368585af433500833116fd23): Codex run review/olson-LSplus-chain-codex-v1.prompt.stdout.txt (0c82174fe2d9dc4d4cd15f75927ae8c636b3d1c0054f4dc89b203a972f33fd63;
0 FATAL / 0 MAJOR / 2 MINOR M1, M2) and Claude run review/olson-LSplus-chain-claude-v1.prompt.note.md (50452b786e18599c4f7b89b283f637e524c45cb069b1471cf6bd71be147b7bf9;
0 FATAL / 0 MAJOR / 16 MINOR, Sec. 6 items 1-16, two optional).
Frozen sources (none edited): proof-LSplus-red-v1.md 166fbac828e7e55a8f2139648930c82c5df1e8823bf9d8c4f84daf36086b4c27 ('RED'); proof-LSplus-red-v1-addendum-1.md
6a79deb851f27d9e3d33c764559085894f5cbbeda40b957aef4030bb32341299 ('A1'); proof-LSplus-red-v1-addendum-2.md f2984d80340f80569a1e9f91cde61db2edb8d3f35582b6334d8cae722f96d2b7 ('A2');
proof-LSplus-lin-v1.md 1372a691022cfef9a75c0fceec73054563e2b3d411e12c739ef27970587667cf ('LIN').  Read each source through this erratum; where they differ this erratum governs.
In 'Old' quotations, line breaks of the source are written as single spaces.  Every repair is wording, an explicit check, a
citation or a scope label: no theorem statement is changed or strengthened, no proof is redesigned, and the optional
simplifications are recorded, not adopted (except the purely definitional R-m1, item C2).  The four sources' 'UNREVIEWED' labels
are historical: after both reviews their status is CANDIDATE_UNVERIFIED until the parent verdict.

## C0  Package-wide overlays (Claude G-m1)
- Lemma CT, Lemma CTgen, Theorem LS+2 and BASE1+ are PARENT-ACCEPTED in run review/olson-STAB-delta-parent-verdict-v1.md
  (ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5), items 6, 7, 4 and 3 respectively, at the scopes stated there, read through erratum-1-delta-APprime.md
  (e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461) and erratum-2-delta-consolidated.md (16cc18235f4353605ebd55753de4304bcf80e5b2c18b42f6fa0c68117795cc27).  Every 'candidate' / 'CONDITIONAL' label on these four
  in RED, A2 and LIN is replaced accordingly (exact lines in C1, C10, C12, C14).
- CF is read through erratum-1-CF-XT-ROW-range.md E1 (767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7) everywhere, and CF (b) through erratum-2-prereq-
  consolidated.md R4 (fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5; mandatory): (L) characterises zero-sums of length >= 2p + 2, which equal the long ones only
  under (ZP_kappa).  RED uses CF (a) only; CF (b) (hence R4) is used only in A1 Step 4 and A2 Sec. 1.

## C1  RED header (G-m1)
Old: 'Lemma CT (proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1, candidate); Lemma CTgen (lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad, candidate);'
New: 'Lemma CT (proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1) and Lemma CTgen (lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad), parent-accepted
(run review/olson-STAB-delta-parent-verdict-v1.md ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5, items 6 and 7, through erratum-2-delta-consolidated.md);'
Also: 'Lemma CF (proof-CF-XT-v1.md ...)' is read 'Lemma CF (a) (proof-CF-XT-v1.md ..., through erratum-1 E1; RED does not use CF (b))', and
'the greedy subset-sum step of proof-LSplus-e2-v1.md Sec. 3 (C)' is part of the parent-accepted LS+2 (item 4).

## C2  RED Sec. 2 Step 1: signed representatives and no-wrap defects (Claude R-m1, optional; adopted as a definition only)
Old: 'Hence the signed representative t~_rho is in [1, delta0 - 1 - 2rho] or in [-(p - 1 - v1), -1], all inside [alpha, beta] :=
[-(e - 2), 4e - 8].  With x~ := t~_1, each (t~_rho + x~) - t~_(rho+1) is = 0 (mod p) and lies in [2alpha - beta, 2beta - alpha] <=
[-(6e - 12), 9e - 18], so it is 0 (p >= 9e - 13): t~_rho = rho x~.'
New: 'Define the signed representative t~_rho := t_rho if t_rho <= v1, and t~_rho := t_rho - p otherwise; so t~_rho is in
[1, delta0 - 1 - 2rho] or in [-(p - 1 - v1), -1], all inside [alpha, beta] := [-(e - 2), 4e - 8].  With x~ := t~_1, the no-wrap defect
D_rho := t~_rho + x~ - t~_(rho+1) (1 <= rho <= e - 2) is = 0 (mod p), because t~_rho, x~, t~_(rho+1) represent rho x1, x1, (rho + 1) x1; it
lies in [2alpha - beta, 2beta - alpha] = [-(6e - 12), 9e - 18], inside (-p, p) as p >= 9e - 13; so D_rho = 0, and by induction on rho,
t~_rho = rho x~.'

## C3  RED Sec. 3: no-wrap defects (Codex M1 = Claude R-m4; mandatory)
Old: 'otherwise s~_rho is in [-(p - 1 - S'), -1] with p - 1 - S' = 3e - 3 - delta' - E' <= 3e - 4.  All s~_rho lie in [-(3e - 4), 3e - 6];
consecutive differences of the lifted sequence lie in [-(9e - 14), 9e - 16] and are = 0 (mod p), hence 0 (p >= 9e - 13): s~_rho = rho x~
with x~ := s~_1.'
New: 'Define the signed representative s~_rho := s_rho if s_rho <= S', and s~_rho := s_rho - p otherwise; in the latter case s~_rho is in
[-(p - 1 - S'), -1] with p - 1 - S' = 3e - 3 - delta' - E' <= 3e - 4.  All s~_rho lie in [-(3e - 4), 3e - 6].  With x~ := s~_1, the no-wrap
DEFECT D_rho := s~_rho + x~ - s~_(rho+1) (1 <= rho <= e - 2) is = 0 (mod p) (whereas the ordinary consecutive differences
s~_(rho+1) - s~_rho are = a^(-1) (mod p), not 0); D_rho lies in [-(9e - 14), 9e - 16], inside (-p, p) as p >= 9e - 13, so D_rho = 0, and by
induction on rho, s~_rho = rho x~.'

## C4  RED Sec. 3: core, minimality, index one and greedy hypotheses (Claude R-m2, R-m3; mandatory)
Old: '|U'| = p - 3e + 2 + delta' >= p - 3e + 3, so U' (-sigma(U')) is a minimal zero-sum of length >= (p + 3)/2 = floor(p/2) + 2 and
2|U'| >= p + 1 (p >= 6e - 5): index one gives u = x_u a, S' <= p - 1 (so delta' + E' <= 3e - 3), and every integer in [0, S'] is an x-sum.'
New: '|U'| = p - 3e + 2 + delta' >= p - 3e + 3 >= 4 (p >= 9e - 13, e >= 3), so U' is nonempty; it is zero-sum-free (maximality of Z0), so
sigma(U') != 0.  U'(-sigma(U')) is a minimal zero-sum over C_p: a proper nonempty zero-sum subsequence omitting the appended term
-sigma(U') would be a nonempty zero-sum of U', and one containing it has a nonempty complement in U' that is a zero-sum.  Its length
|U'| + 1 >= p - 3e + 4 >= (p + 3)/2 = floor(p/2) + 2 (p >= 6e - 5), so the index-one theorem (record e4615144..., n = p) gives a != 0 and
integers x >= 1, one for each term, with every term equal to x a and the x summing to ord(a) = p; the coefficient of -sigma(U') is
>= 1, so S' := sum over U' of x_u <= p - 1 (and delta' + E' <= 3e - 3).  The greedy step of proof-LSplus-e2-v1.md Sec. 3 (C), applied with
r := |U'| and S := S' (its hypothesis S' <= p - 1 < p + 1 <= 2|U'| holds, as p >= 6e - 5), gives every integer in [0, S'] as the x-sum of a
sub-multiset of U'; a sub-multiset of x-sum s has at least s - E' terms.'

## C5  A1 Step 1: the garbled display (Claude A1-m1; mandatory)
Old: 'If zeta_z > n1, W := {z} u W' with W' <= U' of x-sum zeta_z has residue 0 and |W| >= 1 + zeta_z - E' >= 2 + n1 - 2E' + E'...
precisely |W| >= 2 + n1 - E' >= p - 7e + 11 >= delta0: against (F*).'
New: 'If zeta_z > n1, let W' <= U' have x-sum zeta_z (it exists by RED (B), as C4, since zeta_z <= S'), and W := {z} u W'; W has residue 0
and, by the GOVERNING chain
    |W| >= 1 + zeta_z - E' >= 2 + n1 - E' >= 2 + (p - 3e + 3 - E') - E' >= p - 3e + 5 - 2(2e - 3) = p - 7e + 11 >= 3e - 4 >= delta0,
whose inputs are n1 >= |U'| - E' >= p - 3e + 3 - E' (|U'| = p - 3e + 2 + delta', delta' >= 1), E' <= 2e - 3 (delta' + E' <= 2e - 2, delta' >= 1)
and p >= 10e - 15, it contradicts (F*).'  The garbled display is withdrawn and contributes no premise; the closing '(Editorial: ...)'
line of A1 is superseded by this governing chain.

## C6  A1 Steps 1-4: signed-representative sums (Codex M2 = Claude A1-m2; mandatory)
- Step 1, Old: 'For Z'' <= Z0, zeta~(Z'') := sum of z~ (an integer = sigma(Z'') mod p).'  New: 'For Z'' <= Z0, zeta~(Z'') := sum of z~,
  the signed-representative sum of Z'': an integer congruent to sigma(Z'') (mod p), not CF's nonnegative integer sigma(Z'').'
- Step 2, Old: 'has integer sum e - 1 and'.  New: 'has signed-representative sum zeta~(Z'') - (zeta~ - (e - 1)) = e - 1 (an integer
  congruent to sigma(W) mod p; each copy of -g contributes -1), so rho(W) = e - 1, and'.
- Step 3, Old: 'For that Z'' and W'' <= U' of x-sum p + zeta~ in [S' - 3e + 5, S'], W := Z'' u W'' has integer sum -p (residue 0) and'.
  New: 'For that Z'', p + zeta~ lies in [S' - 3e + 5, S'] <= [0, S'] (S' >= |U'| >= p - 3e + 3), so a W'' <= U' of x-sum p + zeta~ exists by
  RED (B) (C4); W := Z'' u W'' has signed-representative sum zeta~(Z'') - X(W'') = -p, an integer congruent to sigma(W) (mod p) -- not
  CF's nonnegative sigma(W) -- so rho(W) = 0, and'.  (This also disposes Claude A1-m4.)
- Step 4, Old: 'sigma~ := zeta~(Z'') - s in [-p + 1, 2e - 4], = sigma(W*) (mod p).'  New: 'sigma~ := zeta~(Z'') - s, the signed-
  representative sum of W*: an integer in [-p + 1, 2e - 4], congruent to sigma(W*) (mod p).'
- Step 4, Old: 'integer sum rho0, residue rho0 in [1, e - 1]'.  New: 'signed-representative sum rho0, hence residue rho0 in [1, e - 1]'.

## C7  A1 Step 4: CF (b) through R4 (Claude A1-m3; mandatory)
Old: 'By CF (b), a zero-sum of length >= 2p + 2 needs W* <= U with rho(W*) >= 1 and |W*| + 2rho(W*) >= 2p + delta0.'
New: 'By CF (b), read through erratum-2-prereq R4 (a zero-sum of length >= 2p + 2; under (ZP_kappa) these are exactly the long ones), such
a zero-sum needs W* <= U and an integer j >= 1 with p | sigma(W*) + j and delta0 + 2j <= |W*|.  As |W*| <= r <= p - 2, rho(W*) = 0 would force
j >= p and |W*| >= 2p: impossible; otherwise the least admissible j is p - rho(W*).  So the condition is rho(W*) >= 1 and
|W*| + 2rho(W*) >= 2p + delta0.'

## C8  A1 'Remaining (exact)' (Claude A1-m5)
Old: 'Expected lever (not executed): the mirror of Steps 1-4 with the involution as unit (residue -tau/2 for integer x-sum tau), plus even
deletion of involution pairs (any long zero-sum must contain >= 2p + 1 non-involution terms) -- the two long-zero-sum patterns are tau
even with a negative Z0 sub-sum <= |Z''| - delta0, or tau odd in (p, 2p) with a positive Z0 sub-sum >= 2e.'
New: '(Withdrawn as text of record: the former "expected lever" passage was an unproved heuristic written before addendum 2, not a
claim; it is superseded by proof-LSplus-red-v1-addendum-2.md.)'  The first sentence of 'Remaining (exact)' stands.
Also: RED Sec. 4 ('Remaining for LS+ (exact) and next lever') is a planning paragraph, not a claim; its reduction sentence is
superseded by A1 and A2 at their ranges (Claude table item 1.5; no text change).

## C9  A1 header (G-m1)
Old: 'same dependencies; no new import.'  New: 'same dependencies (with CT, CTgen and LS+2 parent-accepted, C0); additionally CF (b),
read through erratum-2-prereq R4 (mandatory, C7); no other import.'

## C10  A2 header and Sec. 1 (G-m1; R4)
Header, Old: 'Lemma CT (proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1) and Lemma CTgen (lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad), both
CONDITIONAL until their parent verdict;'  New: 'Lemma CT (proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1) and Lemma CTgen (lemma-CTgen-v1.md
462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad), parent-accepted (run review/olson-STAB-delta-parent-verdict-v1.md ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5, items 6 and 7) at their
stated scopes;'
Sec. 1 proof, Old: 'Proof.  CF (b) (M <= 2p - 1): such a zero-sum exists iff'.  New: 'Proof.  CF (b), read through erratum-2-prereq R4
(M <= 2p - 1): such a zero-sum (length >= 2p + 2; under (ZP_kappa) exactly the long ones) exists iff'.

## C11  A2 Remark 4 range (Claude A2-m1; mandatory)
Old: 'In the setting of LS+-RED (B) with a = -1/2 (any p >= 9e - 13):'
New: 'In the setting of LS+-RED (B) with a = -1/2 (any prime p >= 9e - 13: the Sec. 0 t-notation and the Sec. 1 statements (F0) and (L*)
hold verbatim there, since their proofs use only r <= p - 2 and (p + 1)/2 > e - 1; n_P, A, Lemma 0 and Sec. 3 are not used):'
Recorded (Claude A2-m2, optional; no text change): n_P <= p - 2e + 1, i.e. A >= 0 (otherwise W := P^(p-2e+2) has t(W) = p - 2e + 2 odd and
|W| + p - t(W) = p > delta0 - 1, violating (Fo)); so the 'A <= 0' branches of A2 Steps 2 and 4 are the case A = 0; harmless.

## C12  LIN 'Chain' (G-m1)
Old: '- Theorem LS+2 and Lemma CT: proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1 -- candidate in the delta review (Codex reported ACCEPT per
parent IRC; Claude and parent verdict pending): CONDITIONAL. - Lemma CTgen: lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad -- same status: CONDITIONAL.'
New: '- Theorem LS+2 and Lemma CT: proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1 -- parent-accepted (run review/olson-STAB-delta-parent-verdict-
v1.md ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5, items 4 and 6, through erratum-2-delta-consolidated.md).  - Lemma CTgen: lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad -- parent-
accepted (same verdict, item 7).'

## C13  LIN sharpness: a DIRECT CF (a) computation, not an imported accepted scope (Claude L-m1; mandatory)
Old: 'The bound is attained: E2(kappa) = h^(3kappa-p+2) (3h)^(p-1) and E3(kappa) = h^(3kappa-2p+2) (3h)^(2p-1) satisfy (ZP_kappa)
(proof-LSplus-e2-v1.md Sec. 4, CF instances valid for every kappa in the range) and contain the zero-sums h^(p+3) (3h)^(p-1) and
h^3 (3h)^(2p-1) of length 2p + 2 (exponents available as 3kappa >= 2p + 1).'
New: 'The bound is attained in every cell of the range.  E2(kappa) = h^(3kappa-p+2) (3h)^(p-1) and E3(kappa) = h^(3kappa-2p+2) (3h)^(2p-1)
(h any odd generator) have length 3kappa + 1 and satisfy (ZP_kappa) by the following DIRECT CF (a) computation (the computation of
proof-LSplus-e2-v1.md Sec. 4 carried out at general kappa; the parent's acceptance of LS+2, delta verdict item 4, covers attainment
only at kappa = p - 2 and is NOT cited for other kappa).  E2(kappa) w.r.t. g = h: M = 2p - 3e + 2 <= 2p - 1, delta0 = 3e - 2, U = 1^(p-1);
a sub-multiset W = 1^w has rho(W) = w, and rho(W) <= e - 1 forces |W| + 2rho(W) = 3w <= 3e - 3 < delta0; so CF (F) holds.  E3(kappa)
w.r.t. g = 3h (a generator, p != 3): M = 2p - 1, delta0 = 1, U = (mu*)^(p-3e+2) with 3mu* = -1 (mod p); W = (mu*)^t with
1 <= t <= p - 3e + 2 has -3rho(W) = t (mod p), so rho(W) <= e - 1 would need t mod p in {0} u {p - 3e + 3, ..., p - 3}, impossible
(the empty W has |W| + 2rho = 0 < delta0); so CF (F) holds.  Each contains an exhibited long zero-sum subsequence of length 2p + 2:
h^(p+3) (3h)^(p-1) (coefficient sum 4p) resp. h^3 (3h)^(2p-1) (coefficient sum 6p), the exponents being available as
3kappa >= 2p + 1.'

## C14  LIN exceptional cells: BASE1 exclusion cited separately; 'not covered' = undecided (Claude L-m2; mandatory)
Heading, Old: '## Exceptional cells (NOT covered by this statement or by BASE1+)'.  New: '## Exceptional cells (NOT covered by this
statement or by BASE1+; "not covered" means undecided by these arguments, not a counterexample)'.
Old: '(BASE1+, proof-STAB-base-p1mod3-v1.md 8a41189cb8d2c254394c4ac44963d7a64f7f6ace00a9ad829f7e0af96def0985, candidate)'.  New: '(BASE1+, proof-STAB-base-p1mod3-v1.md
8a41189cb8d2c254394c4ac44963d7a64f7f6ace00a9ad829f7e0af96def0985, parent-accepted in run review/olson-STAB-delta-parent-verdict-v1.md ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5, item 3; the exclusion of
these cells rests on BASE1+, not on this chain)'.  The DFS sentence ('Finite aid only ...') remains a non-premise.

## C15  LIN relation to LS: e = 2 distinct (Claude L-m3; mandatory)
Old: 'LS+ implies LS (3kappa + 1 < p + 2kappa + 1); all covered cells already lie in LS-lin's range p >= 6e - 10 (proof-LS-lin-v1.md), so
no new LS cell.'
New: 'LS+ implies LS (3kappa + 1 < p + 2kappa + 1).  The covered cells with e >= 3 lie in LS-lin's range p >= 6e - 10 (proof-LS-lin-v1.md;
10e - 13 >= 6e - 10); the covered cells with e = 2 are LS-small / LS+2 cells (proof-LS-caseI-smalldelta-v1.md; proof-LSplus-e2-v1.md),
not LS-lin cells.  So there is no new LS cell.'

## C16  LIN relation to STAB: speculation labelled (Claude L-m4; mandatory)
Old: 'STAB (classification at length 3kappa + 1) is NOT covered: at length 3kappa + 1 the analogue of (B) also allows a = 1, -1/3 (E3 is
the case a = -1/3 with g = 3h) and E2 lies in the two-heavy-value case, so the exclusions above do not transfer verbatim.'
New: 'STAB (classification at length 3kappa + 1) is NOT covered.  Proved facts: w.r.t. g = 3h, E3(kappa) has one value above kappa and
core (mu*)^(p-3e+2) = (x a) with x = 1, a = mu* = -1/3 (mod p); E2(kappa) has two values above kappa (v_h = 2p - 3e + 2 > kappa and
v_(3h) = p - 1 > kappa).  [INFERENCE, unproved:] at length 3kappa + 1 the analogue of (B) admits further values of a (e.g. a = 1, -1/3),
so the exclusions above do not transfer verbatim.'

## Recorded, not adopted (no text change)
- Claude, A1 Step 2: T1 <= max(e - 1, 2e - 4) is sharper than the stated 2e - 3; harmless.
- Claude, binding inequalities: RED (A) needs only p >= 9e - 17, RED (B) needs p >= 9e - 13; A1 Step 1 needs p >= 10e - 15 and Steps 2-4 at
  most p >= 9e - 13.  Ranges of the statements are unchanged.
- Codex: the prime-range equivalence p >= 10e - 16 <=> p >= 10e - 15 <=> p >= 10e - 13 (e >= 3) and the retained band 9e - 13 <= p <= 10e - 17 are
  as stated in A2 Sec. 0 and Sec. 5.

## Exact conclusions after this erratum (sequence level; relative to the declared imports; pending the parent verdict)
- LS+ (|Y| <= 3kappa + 1 under (ZP_kappa) with a long zero-sum), prime p >= 7, floor(2p/3) + 1 <= kappa <= p - 2: when e = 2 (accepted LS+2);
  when e >= 3 and p >= 10e - 13 (this chain); and at kappa = (2p + 1)/3 for p = 1 (mod 3) (accepted BASE1+).  Sharp in every cell (C13).
- Undecided by these arguments (not counterexamples): e >= 3, prime p <= 10e - 17, kappa != (2p + 1)/3.  Inside 9e - 13 <= p <= 10e - 17
  only RED (A), (B) and A2 Remark 4 hold; a = -1, and a = -1/2 with E'' >= delta' + 1, remain.  Below 9e - 13 this chain gives nothing.
- LS+ therefore remains PARTIAL (an upper band of the kappa-range, about its top 30 percent for large p, plus the BASE1 cells).
  STAB: only at the BASE1 cells.  No new LS cell.  No TR, INV*, ordered-Olson, novelty or priority claim.
