# Sun k7, class K7: structure lemmas accepted (written); K7 remains open

Recorded at 2026-10-18T14:53:26-07:00.

**CORRECTNESS-ACCEPTED, with the mandatory overlay below:** the written structural statements K7-TRI, K7-U, K7-TWIN, K7-Q (in the X1 convention), K7-Q5 (for |U|≥5 only) and K7-COV (as amended by X2/X3). **K7 is not excluded.** No enumeration, finite coverage or Sun(7) claim is made. FH and §7 leads are UNUSED and not accepted.

## Texts and reviews

- [K7-structure-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/K7-structure-v1.md), SHA256 `f4534c07c556557c9113c6db6106f081486316e326c6d92db3f069d5fc539fc1`.
- [Erratum v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/K7-structure-erratum-v1.md), SHA256 `f8642cb6d18877df1d4ba76c5cbe098dae6c274161f00b404abc30f76ce97138`. It addresses exactly the Codex findings, X1–X3. The parent read it in full; it was not CLI-reviewed.
- [Codex](sun-coset7-k7-structure-codex-v1.note.md), SHA256 `dc0d2c2307fe4b17e3c3fe76a1290a57629793be3fd13f2a904a8b50efdccbf5`: TRI/U/TWIN/Q5 ACCEPT; Q AWF (MINOR); COV AWF (one MAJOR, one MINOR).
- [Claude](sun-coset7-k7-structure-claude-v1.note.md), SHA256 `4c794266001f2aa25f96788ced414a01f1a5c98bad04783c6ba2454cde4e476e`: TWIN ACCEPT; TRI/U/Q/Q5 AWF (MINORs); COV AWF with the same MAJOR plus process and notation MINORs. 0 FATAL.

## Accepted statements (class K7: all 21 pairwise index gcds equal 6; n_i=6r_i with pairwise coprime r_i)

1. **K7-TRI.** For r≤5, every triangle test depends on the markings only through d_v(r)=gcd(r,ℓ_v) (2-, 3- and 5-parts capped by the vertex's excess valuations). τ_max=ab for sorted labels, and the P-grid at apex v is exactly 1/(6·d_v(r_v)).
2. **K7-U.** Among the 35 label multisets of an all-unmarked triangle, T leaves 16. Ppair (equivalently K1+K2, per Claude) removes (1,5,5), (2,5,5), (3,4,4), (3,5,5), (4,5,5), leaving 11. These are survivals of those tests only, not realizability.
3. **K7-TWIN.** On unmarked vertices, α=1 is an equivalence relation. Twins have equal α to every vertex, marked ones included, and no α=5 edge. They satisfy U_zU_x=U_zU_y as sets.
4. **K7-Q (X1).** Put B≡B′ iff B=B′ or β(B,B′)=2. Exactly one of the following holds:
   - Q5: all blocks are singletons and every β=5;
   - Q23: every β∈{2,3}, including b=1 and the all-2 case;
   - Q24: every β∈{2,4} with at least one β=4.

   3 and 4 never coexist, because they force a (2,2,3) triangle, which fails T.
5. **K7-Q5.** A Q5 configuration needs |U|=4, since VFC at an unmarked vertex kills |U|≥5. The |U|=4 case is NOT excluded here.
6. **K7-COV (X2/X3).** Take every K7 pattern that passes:
   - T and Ppair on all triangles of U and on triangles with two vertices in one twin block, and
   - VFC-count at every unmarked vertex, for every admissible q.

   Each such pattern is the lift of reduced data (marking data, twin partition, Q-family data, block-constant marked rows, marked–marked α's). Two data sets give the same pattern orbit iff they have identical marking data and a size-preserving block bijection carries the remaining data. Any certificate must evaluate every rule on the lifted 7-vertex pattern, never on the quotient.

## Independent parent check

- **Grid.** γ=lcm(6,6)=6 and α≤5 is coprime to the w-parts. Each of 2, 3, 5 has at most one carrier, so v_p gcd(n_v,I_jk) reduces to the stated 1+min(ε,v_p r) form; this gives the grid identity.
- **TWIN.** At an unmarked pair with α_xy=1, the opposite-edge relaxation is trivial (d_z(1)=1). T then forces lcm(α_xz,α_yz)≤min(α_xz,α_yz), so the two are equal; transitivity follows.
- **No 5-edge.** For twins, K2 bars the containment when 1+5=6, so hi=0<lo=1/6.
- **Set equality.** τ_min=b at apex z gives μ(U_z(U_x∩U_y))≥b/6=μ(U_zU_x)=μ(U_zU_y), hence equality of the finite sets.
- **K7-Q5 (|U|≥5).** Unmarked neighbours of an unmarked vertex have q=1 and local index w_j, coprime to every other local index, so they are isolated in every allowed set. With at least four unmarked neighbours plus the marked contribution, the weighted VFC sum reaches 1, contradicting strictness.
- **COV hypothesis gap.** Both reviews' counterexample (all-unmarked, all α=5) passes T/Ppair, so the hypothesis gap is real. X2 repairs it by adding the VFC premise; completeness for actual configurations is unaffected.

## Mandatory overlay

- **5-valuation symbol.** Rename the 5-valuation h_i (overlay A-1). Write the grid step as u_{v;jk}. Rename d_v(r) or the VFC local index d_j to avoid the collision.
- **K7-U.** Its cut is by Ppair, equivalently K1+K2, not "not by K". The rows a=3,4,5 need their failing inequalities listed.
- **K7-Q5 example.** The |U|=4 example q=(2,2,1) is inadmissible: K7-U forces α=5 and q=1 at the marker-3 vertex. Delete it. Claude's proposed strengthening, which would remove Q5 entirely, is NOT accepted. It needs its own frozen text and review; until then Q5(|U|=4) stays in the family.
- **K7-COV.**
  - (v) depends on K7-Q5.
  - d-relaxation covers only triangle quantities. VFC and RPLP use the full capped local indices q_j·m_j·w_j.
  - Relaxation is stated per marked vertex, including triangles with two or three marked vertices.
  - Labelled data lift to exactly one pattern.
  - L6 appears only in §7, not §6.
- **Process.** Under F-4, no K7 run is credited without a separately frozen K7 certificate format and parent permission. Under X1, spec-v1's opposite family assignment must not be used; a spec v2 must adopt X1.

## Limits

No realizability of surviving reduced patterns, enumeration, VFC at marked vertices, RPLP or Bonferroni outcome is accepted. K7-BLOCK, K7-PAIR and K7-unmarked-lemmas are separate candidates with their own reviews. This is written mathematics only: no Lean, no human review, no novelty claim. **K7 remains OPEN**, as do K6.2\*, K6.3 and K5.3.
