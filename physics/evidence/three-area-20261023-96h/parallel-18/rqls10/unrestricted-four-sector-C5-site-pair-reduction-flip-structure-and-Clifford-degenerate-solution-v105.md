# RQLS10 v105 — All-sparse C5: every class pair is a vertex SITE pair; site-operator matching; adjacent-class flips; a Clifford solution of all frame/class equations that fails MAX

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 22:57:31 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written projection/Clifford algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

This is the all-sparse SIMPLE FIVE-CYCLE of v82 with a full TEN-class resolution and MAX40. Circuits C_i (i mod 5) have length two, with route {v_{i-1}, v_i}, where v_i = C_i ∩ C_{i+1}. The circuit C_i has the two columns C_i(v_{i-1}->v_i) and C_i(v_i->v_{i-1}); the + plane sits at the tail. Write R_i = 2P_{C_i} - I and Sigma_v = 2S_v - I. v86 Corollary R gives the allowed label sets:
- adjacent pairs {C_i, C_{i+1}}, with C_i at v_{i-1} and C_{i+1} at v_{i+1};
- non-adjacent pairs {C_i, C_{i+2}};
- triples {C_i, C_{i+1}, C_{i+3}} with one doubled label.

## 1. Lemma SITE

Two cells of one length-two circuit C in one class lie at the SAME vertex, in OPPOSITE rows.

Proof: C+ at v sits on column C(v->v'), and C- at v' also sits on C(v->v'); the other cross combination likewise shares C(v'->v). A class cannot use a column twice.

By the identities P S + P'(I-S) = (I + R Sigma)/2 and P(I-S) + P'S = (I - R Sigma)/2, the two opposite-row pairs of C at v span the ±1 eigenspaces of the SITE operator M_{C,v} = R_C Sigma_v. This operator is a traceless reflection commuting with R_C and Sigma_v. Note the contrast with BARBELL and THETA(1,2,2), whose length-three circuits X and Y allow cross-vertex pairs, as used in v98 and v103.

## 2. Lemma MATCH

In a two-label class, the two site pairs span complementary planes E^s(M) and E^{-s}(M'). Hence M' = ±M, and this M commutes with BOTH circuit reflections. A three-label class (2,1,1) contains one site pair spanning E^s(M_{C,v}); its two single cells lie in E^{-s}(M_{C,v}). Each single comes from a broken site pair, whose partner cell is then a single in another three-label class. Consequently, if every class is two-label, the ten sites are partitioned into groups of sites from distinct circuits sharing one site operator up to sign, and each group of k sites carries k classes.

## 3. Lemma FLIP (adjacent classes)

An adjacent class {C_i, C_{i+1}} forces C_i/C_{i+1} to be interior-isoclinic (v86; also via the vertex form at v_i). In their product frame R_i = r_i ⊗ I, R_{i+1} = r_{i+1} ⊗ I, the common site operator lies in the commutant, so M = I ⊗ sigma_n. Hence:

    Sigma_{v_{i-1}} = r_i ⊗ sigma_n,   Sigma_{v_{i+1}} = ± r_{i+1} ⊗ sigma_n,   Sigma_{v_i} = I ⊗ sigma_omega.

So both outer vertices carry PRODUCT-REFLECTION "flips". MAX between the C_i cells at v_{i-1} (r_i± ⊗ n±) and at v_i (r_i± ⊗ omega±) requires axis(n) ≠ axis(omega).

If C_{i-1}/C_i is also interior-isoclinic, write R_{i-1} = lambda r_i ⊗ I + mu N, with N off-diagonal with block V in the r_i basis. Commutation with Sigma_{v_{i-1}} = r_i ⊗ sigma_n forces {V, sigma_n} = 0, so V is a pi-rotation about an axis perpendicular to n. This is the C5 analogue of the BARBELL flip of v95 Lemma ROT.

## 4. The all-adjacent pattern and its Clifford solution

Suppose all ten classes are adjacent, two for each i. Then MATCH and FLIP reduce the frame/class equations to:
- Sigma_{v_j} commutes with R_j and R_{j+1}, with all traces zero;
- R_i Sigma_{v_{i-1}} = ± R_{i+1} Sigma_{v_{i+1}} for every i.

**Explicit solution.** Take five pairwise anticommuting traceless reflections gamma_1..gamma_5 on C4. For example: X⊗I, Y⊗I, Z⊗X, Z⊗Y, Z⊗Z, whose product is -I. Set R_i = gamma_i and Sigma_{v_j} = i gamma_{j+2} gamma_{j+4}.
- Each Sigma is a traceless reflection commuting with gamma_j and gamma_{j+1}.
- tr(Sigma_{v_j} gamma_j) = tr(Sigma_{v_j} gamma_{j+1}) = 0, since a product of three distinct gammas is traceless.
- R_i Sigma_{v_{i-1}} = i gamma_i gamma_{i+1} gamma_{i+3} = ± R_{i+1} Sigma_{v_{i+1}}, as reordering gamma_{i+1} gamma_{i+3} gamma_i takes two transpositions.

So every frame and class equation of the all-adjacent pattern holds.

**MAX fails.** Since gamma_1...gamma_5 is a scalar, gamma_i (i gamma_{i+1} gamma_{i+3}) is proportional to gamma_{i+2} gamma_{i+4}. The joint eigenbases of (R_i, Sigma_{v_{i-1}}) and (R_i, Sigma_{v_i}) therefore coincide: the C_i cells at v_{i-1} repeat those at v_i. Equivalently n = omega in Lemma FLIP. A genuine C5 sector needs the site matching WITHOUT this degeneracy, i.e. non-anticommuting isoclinic pairs or other class patterns.

## 5. Scope

These are written reductions together with an explicit degenerate solution of the frame/class equations. Neither C5 existence nor exclusion is claimed. The (3pi/4)-twisted toolkit of v98/v103 does not directly realize C5: its product-circuit site pairs would need compression offsets ±pi/4, while that toolkit yields 0 and ±3pi/4. This is stated as an observation and is NOT used as a theorem. C5 remains OPEN. The H6 sectors of BARBELL and THETA(1,2,2), dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v82 topology; v86 Corollary R and the vertex form; v78/v79 isoclinic product frames; elementary Clifford algebra (five anticommuting reflections on C4 have scalar product). No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S105, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the v29 and v40 parallel-intent minors, the v30 dangling-reference defect, the v34 capture retry, the S98 zero-credit mental-decimal disclosure, the v46 parallel post-cell capture disclosure and the S103 pre-pin draft correction.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
