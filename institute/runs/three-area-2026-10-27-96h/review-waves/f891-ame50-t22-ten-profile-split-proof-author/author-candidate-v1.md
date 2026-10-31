# Actual AME(4,6), N=50/t=22: the 12+16 residual split is impossible at every global profile

**Status.** NONBLIND, same-harness PROSPECTIVE GENERAL AUTHOR written candidate (wave f891, agent AuthorF891AME22Split). Not reviewed, not adopted; parent disposition is separate. Native clock observed before this exclusive creation: 2026-10-31T04:12:12Z (observation before the write, not a creation certificate). No scientific code, eval, solver, test or child process was used; no verifier was prepared (none requested by scope). Prepared code hash: **none**.

## 0. Result

**Theorem 1.** Let psi be ONE normalized complex pure state in (C^6)^(tensor 4), written in ONE fixed local orthonormal product basis, such that all three balanced 36x36 flattenings of U=6psi are unitary, U has exactly 50 nonzero entries, and exactly 22 of them have modulus one (the set P; the other 28 form E). Then the residual agreement graph on E is **not** the disjoint union of a 12-word and a 16-word component. All amplitudes are arbitrary nonzero complex numbers; the same P, E and coefficients are used in all six physical pair systems and all three cuts.

**Corollary (assigned target).** For EACH global E-alphabet profile 4466, 4555, 4556, 4566, 4666, 5555, 5556, 5566, 5666, 6666, the 12+16 split is impossible for such a tensor. The proof is profile-independent, so it also re-proves the adopted split exclusions at 3566, 3666, 4456 (S5) by a different route. With the adopted dichotomy (S4|5: one 28-word component or components of sizes 12 and 16), **the only alternative left at N50/t22 is one connected 28-word E**. That connected alternative is **not** decided, excluded or realized here. No support-50 exclusion, global N50, minimum-51, witness, novelty or priority claim is made.

The decisive written identity (Section 4) is

    2 * sum_{w in P} f(w)  +  sum_{w in C16} f(w)  =  66,      while   f <= 1   gives   left side <= 2*22 + 16 = 60.

No phase equation, integral-kernel criterion, canonical label, K_{3,3} structure, profile moment, binary-box count or C16 local profile is needed for the contradiction; only the actual pair incidence of the SAME P and E and the 2333 alphabet/degree pattern of the 12-word component.

## 1. Imports and their status

All used facts are support consequences of unitarity of the one actual tensor. I cite the adopted dispositions and also reconstruct each needed step below, so the proof does not rest on an unadopted claim.

* I1 (adopted S4|3,5; reconstructed in S6|9, S7|9-13, S8|7-9): in every physical pair system ij, the 36 pair values split into 22 P values, each with exactly one P extension, and 14 E values, each with exactly two E extensions; P and E values are disjoint. Reconstruction: a modulus-one entry exhausts its row and column in each cut (so P is injective in each pair projection and no E word has a P pair value); the residual 14x14 unitary has 28 nonzeros, no singleton line (a unitary singleton has modulus one), hence every residual line has exactly two nonzeros.
* I2 (adopted S4|5): agreement components of E (edges = two distinct E words sharing a physical pair value) are closed under every pair-mate involution; a pair value used in a component has both E extensions there and is used by no other component. For a symbol x used at party i by component C, its number of C words is s^C(x)=2 d^C(x), where d^C(x) = number of its C-neighbours at any other fixed party (independent of that party), d^C(x)>=2, sum_x d^C(x)=|C|/2. The only component alternatives are one 28-word component or two components of sizes 12 and 16.
* I3 (adopted S5|3,7; reconstructed in S8|41-45, S9|17-23, S10|22-24 and briefly in Section 2): every 12-word component has local alphabet profile 2333: three parties with three symbols of C12-degree 2 and one party with two symbols of C12-degree 3. Only this incidence pattern is used; the canonical labels and amplitude form of S5|9-16 are not used, so the adopted gadget is used strictly within its adopted scope (a 12-word residual component of this same tensor).

Status-only controls supply no mathematical premise. Held episodes and all their consumers are NONINPUT and were not opened.

## 2. Notation for the hypothetical split and the 2333 facts

Suppose, for contradiction, E = C12 disjoint-union C16 with |C12|=12, |C16|=16, both agreement components.

**Short reconstruction of I3.** In C12 each party's degrees sum to 6 with each degree >=2, so each local alphabet has at most three symbols; a degree is at most the partner alphabet size, so no party has one symbol; two binary parties would give at most four values in their pair, but each pair needs |C12|/2=6 values. So the profile is 2333 or 3333. In 3333 every pair graph is 2-regular on 3+3 vertices, i.e. K_{3,3} minus a perfect matching, which contains no full 2x2 rectangle (two rows miss two distinct columns, and any two chosen columns contain at least one of them). Fix a symbol a: its four words use exactly two symbols, twice each, at each other party; two distinct balanced 2+2 partitions at two parties would fill a 2x2 rectangle, so all three partitions coincide and the four words take only two distinct values in the other three coordinates, repeating a word. Hence 2333.

Name the parties so that C12 is binary at D and ternary at A,B,C. Let A0,B0,C0 (size 3) and D0 (size 2) be the C12 alphabets. Every x in A0 u B0 u C0 has C12-degree 2; every d in D0 has C12-degree 3.

* (F1) **A0 x D0 is entirely C12.** Each a in A0 has two C12-neighbours at D, and |D0|=2. Likewise B0 x D0 and C0 x D0. These 6+6+6 cells are C12 pair values.
* (F2) **Ternary pairs.** C12 has exactly 6 pair values in A0 x B0 (|C12|/2 values, all inside the C12 alphabets). The remaining three cells form the set H_AB; similarly H_AC, H_BC. Let H = H_AB u H_AC u H_BC (9 cells).
* (F3) By I1/I2, each cell of H is either a P value or a C16 value. Let g = number of cells of H that are C16 values (0<=g<=9).
* For each symbol x in A0 u B0 u C0 u D0 let k(x) = d^{C16}(x) if C16 uses x, else k(x)=0. Its global E-degree is d12(x)+k(x), because the C12- and C16-neighbour sets are disjoint (a shared neighbour would be a shared pair value, contradicting I2).
* (F4) **P occurrences.** By I1, x occurs in exactly 6 - d12(x) - k(x) P words: each of its six pair values with a fixed partner party is P or E, and each P value has exactly one P word, distinct P words giving distinct values. So x in A0 u B0 u C0 occurs in 4-k(x) P words; d in D0 occurs in 3-k(d) P words.
* (F5) **C16 occurrences.** By I2, x occurs in exactly 2k(x) C16 words.

For any word w in P u C16 define

    J(w) = { i in {A,B,C} : w_i in X^12_i },   j(w)=|J(w)|,   delta(w) = [w_D in D0],
    f(w) = j(w) - C(j(w),2) + delta(w).

## 3. Local lemma: f <= 1 on P and on C16

If delta(w)=1 then j(w)=0: otherwise some w_i in A0 (say) together with w_D in D0 gives the pair value (w_i,w_D) in A0 x D0, a C12 value by (F1); a P word cannot use an E value (I1) and a C16 word cannot use a C12 value (I2). Hence (j,delta) is one of (0,0),(0,1),(1,0),(2,0),(3,0), with f = 0,1,1,1,0 respectively. So f(w) <= 1, with f(w)=0 exactly for (j,delta) in {(0,0),(3,0)}. This holds for every word of P and of C16; words of C12 are not counted anywhere.

## 4. Exact weighted counts and the contradiction

Weight each P word by 2 and each C16 word by 1, and let Sigma_omega denote the weighted sum over P u C16.

1. **Ternary incidences.** For x in A0 u B0 u C0: by (F4),(F5), weighted words containing x number 2(4-k(x)) + 2k(x) = 8. Hence Sigma_omega j = 9*8 = **72**, for every sharing pattern.
2. **Pairs inside ternary C12 alphabets.** For a word, C(j,2) counts its pairs (i,l) of ternary parties with both coordinates in C12 alphabets. Such a pair value lies in X^12_i x X^12_l, is not a C12 value, hence lies in H. Conversely, a cell of H that is a P value lies in exactly one P word (I1), and a cell of H that is a C16 value lies in exactly two C16 words (I2). So each of the 9 cells of H contributes weight exactly 2 regardless of its type: Sigma_omega C(j,2) = 2(9-g) + 2g = **18**.
3. **D0 incidences.** For d in D0: weighted words containing d number 2(3-k(d)) + 2k(d) = 6. Hence Sigma_omega delta = 2*6 = **12**.

Therefore

    Sigma_omega f = 72 - 18 + 12 = 66.

By Section 3, Sigma_omega f <= 2|P| + |C16| = 44 + 16 = 60. Since 66 > 60, the hypothetical split does not exist. QED for Theorem 1.

**Unweighted form (same content, for review).** Put sigma = sum k(x) over the 11 C12 symbols. Separately, sum_{P} f = (36 - sigma_ABC) - (9 - g) + (6 - sigma_D) = 33 - (sigma - g) and sum_{C16} f = 2 sigma_ABC - 2g + 2 sigma_D = 2(sigma - g). With N0, W0 the numbers of P and C16 words with f=0: sigma - g = 11 + N0 and sigma - g = 8 - W0/2. Thus 2 N0 + W0 = -6, impossible. In words: P needs C16 to reuse C12 symbols heavily (sigma - g >= 11), while C16 can reuse them only moderately (sigma - g <= 8).

## 5. Per-profile conclusion and boundary cases

| profile | Sigma q | 12+16 split |
|---|---:|---|
| 4466 | 20 | impossible (Theorem 1) |
| 4555 | 19 | impossible (Theorem 1) |
| 4556 | 20 | impossible (Theorem 1) |
| 4566 | 21 | impossible (Theorem 1) |
| 4666 | 22 | impossible (Theorem 1; also cross-check 6.1) |
| 5555 | 20 | impossible (Theorem 1) |
| 5556 | 21 | impossible (Theorem 1) |
| 5566 | 22 | impossible (Theorem 1; also cross-check 6.1) |
| 5666 | 23 | impossible (Theorem 1; also cross-check 6.1) |
| 6666 | 24 | impossible (Theorem 1; also cross-check 6.1) |

The global profile never enters Sections 2-4; no residual (E16 local profile, symbol-sharing pattern, P22 incidence vector or phase condition) survives for the split at any profile. Boundary cases covered explicitly by the proof:

* every physical party may be the C12-binary party D (named after the fact);
* D0 symbols may be unused by C16 (k=0) or used with any C16-degree; ternary C12 symbols likewise; all sharing patterns enter only through k(x), which cancels in the weighted counts;
* each H cell may be P or C16 (g arbitrary in 0..9), which also cancels;
* symbols unused by E and the C16-only symbols play no role (they never contribute to j or delta);
* P words or C16 words with all three ternary coordinates in C12 alphabets (j=3; necessarily on the H-triples) and words avoiding all C12 alphabets are allowed; they only have f=0 and make the inequality stronger;
* no C16 local profile (2444, 3333, 3334, 3344, 3444, 4444) or C16 phase assumption is used, so none is silently discarded;
* arbitrary nonzero complex moduli and phases: all facts are support facts of the actual unitary flattenings; the K_{3,3}/phase part of the 2333 gadget is not needed.

## 6. Independent partial cross-checks (not needed for Theorem 1)

6.1 **P side alone plus alphabet sizes.** Section 4's P equality gives sigma - g = 11 + N0 >= 11, so sigma >= 11. At party i let c_i = |X^12_i| (3 at A,B,C, 2 at D) and u_i = q_i - c_i, the number of C16 symbols at i outside X^12_i. Each such symbol has C16-degree >= 2 and C16 degrees at i sum to 8, so sigma_i <= 8 - 2u_i and sigma <= 32 - 2(Sigma q - 11) = 54 - 2 Sigma q. Hence Sigma q <= 21, independently excluding 4666, 5566, 5666, 6666.

6.2 **Consistency with S5.** S5 adopted split exclusions at 3566, 3666, 4456 by degree/pair-cell case analysis. Theorem 1 agrees and does not use those arguments; no conflict with any adopted statement is found. It also agrees with S10|95 / S8|120 that the connected case is left open.

6.3 **Sanity of the method.** Applying the same weighted count to a hypothetical 3333 twelve-word component (no binary party) gives 12*8 - 6*3*2 = 60 <= 60 with f <= 1 (j=4 gives f=-2), i.e. no contradiction. So the contradiction genuinely uses the binary C12 party; the separately adopted and reconstructed 3333 exclusion is therefore load-bearing through I3.

## 7. Exact limits

* Proved here (author claim): no actual N50/t22 tensor has a 12+16 residual split; equivalently any such tensor has a connected 28-word E. Conditional only on the actual-tensor hypotheses and I1-I3 above (each adopted and reconstructed here).
* Not proved: anything about the connected 28-word case at any of the 13 profiles; existence or nonexistence of support 50; other t values; the conditional 50-60 interval; minimum 51; original-source identity; novelty; priority; family, human or formal verification.
* First open step after this candidate: decide the connected 28-word alternative at the 13 necessary profiles (common P22, all six pair systems, all three seven-K_{2,2} cuts, then the even-sum integral-kernel criterion of S3).

## 8. Read declarations, sequence and process disclosures

* Administrative files read completely before any body: manifest-v1.json (294 LF), freeze-receipt-v1.json (271 LF), final-pre-dispatch-binding-v1.json (223 LF), parent-live-metadata-supply-v1.json (284 LF), actual-dispatch-receipt-v1.json, and all 22 manifest `controls_before_body` records through their endings. The first nonraw displays of manifest and freeze receipt elided nested lines; I reread the elided ranges in RAW before the ACK. Parent's IRC confirmation of the dispatch receipt arrived during this administrative phase.
* PREBODY: wrote prebody-ack-v1.md (clock 2026-10-31T03:27:37Z) and prebody-ack-erratum-v1.md (cosmetic abbreviated-hash slips only), then sent Main the direct PREBODY ACK (delivered) before opening any packet body.
* Before reading body text, one administrative bash/awk command computed per-20-LF-window byte totals of both parts (only numbers displayed; part 01 total 77233 bytes, max window 5804 bytes; part 02 max window 5402 bytes). No content was displayed by it.
* Packet part 01 (S1-S7, 418 LF) read RAW in windows 1-20, 21-40, 41-60, 61-80, 81-100, 101-120, 121-140, 141-160, 161-180, 181-200, 201-220, 221-240, 241-260, 261-280, 281-300, 301-320, 321-340, 341-360, 361-380, 381-400, 401-418 (ending S7|119). Then part 02 (S8-S10, 416 LF) RAW in windows 1-20, ..., 381-400, 401-416 (ending S10|139). Every window < 30000 bytes; no clipping occurred, so no recovery was needed. Deviation disclosed to Main: after window 1-20 of part 01, successive windows were fetched in parallel batches of two or three and read in ascending order; all of part 01 preceded part 02 and both endings were reached before any mathematical reasoning on the target.
* The memory summary and two process skill files (aifours research-round orchestration, written-math acceptance protocol) were read after the complete packet, as process guidance only, not mathematical sources; disclosed to Main.
* One assistant generation was truncated by the harness output limit and discarded unseen; it executed no tool call and wrote no file. The mathematics above was re-derived and written in this file.
* Source pins (manifest-declared, not recomputed): S1 6e0e7704...c63c0b6d; S2 4c201b80...591ff6; S3 85878560...f9; S4 4ae01f3c...bb; S5 876bf145...057; S6 14c09bba...49c; S7 12d2e4c7...bec; S8 edbe988b...fe; S9 34689ded...4c5; S10 c6189b12...a3d. Parts: 01 7e549ce2...2bde96, 02 62f24230...51186a. Full values are in manifest-v1.json.
* No original source path, link target, sibling return, held episode or consumer, old code, network, external model, Git, deletion, installation, build, lint, test or formatter was used. Only commands: ls, /bin/date, the awk byte count above, and administrative file writes in this wave directory.
