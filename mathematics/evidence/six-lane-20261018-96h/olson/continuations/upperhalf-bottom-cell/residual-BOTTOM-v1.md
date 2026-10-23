# BOTTOM route ledger and closeout: earlier exact obstruction closed by the companion candidate, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T18:56:05-0700. CANDIDATE_UNVERIFIED. This is the companion named
residual-BOTTOM-v1.md by proof-BOTTOM-parity-v1.md, which was frozen as a labelled partial before the final argument existed.
Read BOTH proof files: proof-BOTTOM-parity-v1.md SHA256 b648411f7ed7b2b17fdd9bcc4a51f2df24ca7a1540eb88cd4c7fbd2e6080a9f3 (P), and
proof-BOTTOM-close-v1.md SHA256 e9e1b55315bbe4cc24b50da7c600f6c8af09626b7a4ead6731a171b775521817 (C). No older file is edited.

## 1. Exact result and boundary
Under the full existential admissible-NF antecedent, prime p>=11, terminal k=p+1, kappa_hat=(p-1)/2, e=(p+1)/2, arbitrary
placement of H=e-1 extra reflection pairs, and the empty-run rule, C supplies a full written proof excluding every
3<=c<=p-1 (A=p-1+c). With UH-A forcing that range, the whole specified bottom cell is excluded by the candidate.
There is NO remaining parameter/profile subcase within this target in the combined written argument. This is not acceptance:
parent-owned independent review/verdict is still required. Not claimed: ordered Olson, unrestricted inverse normalisation,
the lower half, o_F closure, p<11, a multiset-only statement outside the full word/NF antecedent, novelty/priority, human or
Lean verification. No other cell is promoted by this packet.

## 2. Frozen development sequence
1. Scope BOTTOM-scope-v1.md, SHA256 ab9ee0251454d4242b2d268e73eacacf875df6172467f3a24fef6c3cbc22d99e, before derivation, with
   pre-freeze exposure disclosed. Written transition authority only; runtime HOLD unchanged.
2. P: empty-run exclusion E=0, a necessary odd-g escape, four-value support and half-total target. At its freeze this was a
   labelled partial with the empty-free row-critical profile still open. P's Sec. 8 is a record of that stage, not the final
   scope of the combined proof.
3. C: use all INTERIOR low critical patterns (not only m<=k0) and minimise g. Singleton runs force an m-endpoint; sole
   endpoints bound every run length, and a pure signed-a run flips to a smaller interior g (or an even-window contradiction).
   Only e odd,g=e-2,m=(e+1)/2 can survive. The small-m caps then force a very long run; with E=0, even e is immediately
   impossible, while odd e has too many singleton runs to fit inside the e-letter minority of the top interior pattern.
Everything is re-proved in this new bottom-cell directory; RUH3/RUH2/KP3/KP4/R7 are not accepted premises.

## 3. Failed branches (kept; how the final argument replaces them)
(F1) Raw MW at odd g: q=g and w0+q=p-1, so it does not cover all residues. This is a real one-residue obstruction. Replaced
     by rigidity of equality (each difference +/-2a) and the exact missing target 2T=D_z, not by claiming q>=g+1.
(F2) The m=e alternating patterns: N=2e, only two such subsets, no single-run toggle path preserving m=e. The proof NEVER
     assumes that path. It uses m=k0=floor(e/2)+1, where N>=2k0+2 and the path is explicitly written.
(F3) Trying to deduce positivity or arbitrary additivity of empty-run lifts from UH-L: UH-L requires delta=0 and low arcs.
     Not used. The needed lifts come from the component [L,U] of M containing B0, sets with m<=ceil((e+1)/2), and a defect
     strictly between -p and p. The full subset sum set is substituted only for b<=n<=A.
(F4) Equality target 2T=D_z does NOT itself yield a subword: at a critical pattern it is precisely the omitted residue.
     The proof does not reverse this implication. It compares actual critical patterns/targets or invokes even-window MW.
(F5) Local transport alone is insufficient: a flip can leave the critical m/g window, so it does not force all H_i=0.
     The final argument keeps both m-endpoints, uses singleton-run counting there, and minimises g over ALL interior patterns
     so the pure-a flip stays in a strictly smaller interior window. No reachability assumption is made.
(F6) Empty-run exclusion alone leaves an empty-free profile with >=4 singleton runs and possible odd-g escapes. P labels
     this partial honestly. C closes it by the endpoint/minimal-g argument and the long-run/minority-count contradiction.

## 4. Review obligations
Most delicate: the exact odd-gap equality case including g=1; the empty-toggle/flat-sign distinction; the three c-ranges
in E0 (especially c=e-1 for even e); the Q-block exchange/counting; the fact that minimal g ranges over ALL interior patterns;
tracking g'=g-L for a pure signed-a run and the new m-window; the final inequalities s1>=p-1+delta and s1<=e. Check smallest
endpoints p=11,e=6 (even) and p=13,e=7 (odd), without computation. No scientific scripts/tests/solvers/Lean were used.
