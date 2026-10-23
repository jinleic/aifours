VERDICT: ACCEPT-WITH-FIXES

**FATAL**: none.

**MAJOR**: none. No step makes "K1 = K2 = ∅" false or unproved. This assumes the imports listed below and that the separately reviewed encoders conform to the corrected (P1) in item 1.

**MINOR**

1. **L99–100: (P1) is false as stated on row 0.** In row-0 standard form, Q1(0,j) = Q2(0,j) = |j⟩. That support is the column coordinate, equals every classical symbol L_D(0,j) = j, and is shared by Q1 and Q2. Encoded literally, every FK2(R_k) would be UNSAT for a trivial reason.
   - The certificates are not affected. relaxed_ctrl_v1 is SAT without (P4), which rules out literal (P1) on row 0 in the production path.
   - But L103 ("exactly the clause families") is the spec the encoder review checks against.
   - Fix: add "(P0) row 0 fixed, supp Q_s(0,j) = {j}" and restrict (P1) to cells (i,j) with i ≠ 0. The same omission is in the n = 7 Lemma P (its L48).

2. **L22–24, L98–99: Lemma 3 and Lemma P are proved only by reference to the n = 7 files.** The n = 7 proof of Lemma 3 is n-independent and correct. Inline it, and write out the one-line derivations for (P1)–(P3):
   - (P2): unit columns give coverage; Lemma 2 forbids two cells sharing exactly one coordinate; column orthogonality forbids two coordinates co-occurring in exactly one cell.
   - (P3): Prop 1 combined with Lemma 2.
   - (P1): rule #3; rule #2; and (P2) applied to the classical line through (0, L_D(c)).
   - (P4): comes from the all-frames claim, not from the n = 7 argument. By W8, "weight 3" is equivalent to "weight ≥ 3".

3. **L26–28: the paraphrased construction needs two more sentences.**
   - "Apply one unitary U on span{|a⟩,|b⟩}" need not terminate for arbitrary U (e.g. U = I). Properties (i)–(iv) hold per step for any U, but classicality of Ψ′ needs the printed choice U ψ_ij = |a⟩, which strictly lowers the weight-2 count.
   - State that Ψ′ is independent of the partner Φ. That is what makes (iii) hold for all other squares at once, and in sequence: each application changes one square only, and the "no weight ≥ 3" hypothesis of unprocessed squares is untouched.
   - With these two sentences, (i)–(iv) are implied by raw.txt:345–356, including sequential application.

4. **L37: A8's heading omits its hypothesis "for a set of 5 MOQLS(8)".** The proof uses six classes: H is 6-regular and two a-cells share ≥ 4 neighbours. For t squares the bound is 2(t+1) − 8, so the argument works for t ≥ 4.

5. **L77–79: sets versus lists in E–W.** E–W define paratopism for lists (layout 145–146), but Table 6 counts reduced sets. Add the following:
   - The S_{k+2} column action absorbs ordering.
   - Reducedness affects only the Equality column (layout 737–738).
   - Parallel classes are recovered from incidence (two lines are parallel iff they are disjoint or equal).
   - Hence the Paratopism entry is the number of isomorphism classes of (k+2)-nets. With this, (8,4) gives exactly one 6-net class and (8,3) gives exactly 39 5-net classes, as claimed.

6. **L65: justify putting a net class at direction ∞.** Either note that GL(2,8) induces a transitive PGL(2,8) action on the 9 directions, or restrict K1-AG to nets containing ∞. The restriction suffices, because the bridge representative is {∞, 0, s1, …, s4}.

7. **L80, L96–97: transport along an isomorphism is not covered by Lemma R.** Lemma R covers regridding on a fixed net. Add: for a net isomorphism φ, Ψ∘φ⁻¹ satisfies Lemma R's hypotheses on φ(𝒩), with the same vector multiset and with ℓ-frame supports carried to φ(ℓ)-frame supports.

8. **L107–113, L137–138: the trust boundary can be narrowed.** Completeness already follows from three facts:
   - the 39 representatives are locally valid 3-MOLS(8);
   - their 39 nauty certificates are distinct, and distinct certificates imply non-isomorphic nets;
   - Table 6 gives exactly 39 classes.

   Archive authenticity then drops out, and only the integer 39 is imported. Table 5's "38 maximal" is not in the supplied excerpt; it serves only as a consistency check.

9. **L86–89: wording and theorem statement.**
   - Write "m ≥ 1 by A8 applied to S".
   - State the result invariantly: no set of 5 MOQLS(8) has exactly one, or exactly two, non-classical squares. Hence in every row (or column) standard form of a non-classical set, at least three squares have a weight-3 entry. Currently K_m is defined only via S′ and row 0.

10. **L12: justify "8 rays ⇔ classical ⇔ MOLS" in one line.** One row already supplies 8 orthogonal rays, so 8 rays means a single ONB, which a per-square unitary sends to the computational basis. Prop 1 turns orthogonality of two classical squares into orthogonality of their symbol arrays.

**What is established**

- **Prop 1, Lemma 2, W8:** correct.
- **Lemma 3:** correct for all n.
- **Lemma 10 (i)–(iv):** implied by the printed proof, including sequential application (given item 3).
- **A8:** correct.
  - E ⊆ V follows from (i).
  - |E ∩ M| ∈ {0, 2} follows from Lemma 3.
  - H is simple and 6-regular, since two lines through a cell meet only there; the ≥ 4 common-neighbour bound makes it connected.
  - (0,a) lies in V but not in E, by (ii).
- **Lemma R:** correct.
- **K1-AG:** every step checked in GF(8) (α³ = α + 1).
  - t0 ∉ T.
  - V = T + t0 consists of three distinct nonzero elements with sum 0, so W = V ∪ {0} is a 2-dimensional subspace, and so is rW.
  - aV = V with a ≠ 1 is impossible, since a generates the group of prime order 7 and |V| = 3.
  - dim(rW ∩ r′W) = 1, so |rV ∩ r′V| = 1.
  - supp Ψ(r,c) ⊆ c + rT follows from the lines with t ∈ A.
  - Lemma 2 then makes the seven supports disjoint, and pigeonhole on GF(8) ∖ {b} makes them singletons.
- **Reduction and all-frames claim:** correct and not circular. m ≥ 1 by A8 on S; m ≠ 1 by §4. The all-frames claim uses only W8, A8, Lemma 10 and §4.
- **(P1)–(P4):** necessary for the transported and regridded K2 set, with fix 1.
- **What follows:**
  - Unconditionally: A8, K1-AG, and m ≥ 1.
  - With E–W (8,4) = 1: K1 = ∅.
  - Adding E–W (8,3) = 39, encoder conformance and the drat-trim checks: K2 = ∅. One encoder's 39 certificates suffice; the second set is redundancy.
- **Not addressed:** K3–K5. Problem 16 at n = 8 remains open.

**Imports**

- **Ball–Simoens v2 §2.2–2.3:** definitions. Rules #1–#3 are re-derived here. The printed proof of Lemma 10 is fully re-checked, so nothing from it remains imported.
- **Egan–Wanless arXiv:1406.3681v2:**
  - the §2 definition of paratopism;
  - Table 6 Paratopism entries (8,4) = 1 and (8,3) = 39, which are computer classifications;
  - Table 5's 38 maximal, for consistency only.
- **Catalogue authenticity:** removable via item 8.
- **Machine facts:**
  - 78 drat-trim "s VERIFIED" results;
  - byte-identical regeneration of the CNFs;
  - local Latin, orthogonality and maximality checks;
  - nauty certificates.
- **Separate encoder review:** A8r2 and B8r2 must implement exactly the corrected (P0)–(P4) on R_k's grid with R_k's row-0-relabelled squares, with no extra clauses.
