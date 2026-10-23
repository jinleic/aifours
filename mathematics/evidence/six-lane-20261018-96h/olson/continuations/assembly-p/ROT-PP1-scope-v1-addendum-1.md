# Frozen scope addendum 1 to ROT-PP1-scope-v1.md: exact statements before the written proof

Owner OlsonAssemblyP. Frozen after /bin/date 2026-10-19T12:06:22-0700, BEFORE the written proof file for Target 2 is created.
Applies after ROT-PP1-scope-v1.md (sha256 698521494bcfbd951f417e182698102e3ba1f49559adc15d6a23d709d93686e0, frozen 11:57:04),
which is unchanged. Status: CANDIDATE_UNVERIFIED targets, not proofs and not verdicts. Written research only.
Parent instruction received at 12:05 (IRC): keep Target 2 (k = p+1) separate from the ASSEMBLY-P packet; ASSEMBLY-P residual
wording is governed by the parent erratum review/olson-ASSEMBLY-P-parent-erratum-v1.md; nothing here edits it.

## Exact candidate statements (replacing the planning wording of items (a)-(c) of the scope v1; (d)-(e) unchanged)
Throughout: p >= 7 prime, w an avoider of length 4p-2 over D_(2p), w^ an admissible normal form of w with terminal k blocks,
kappa^ = p-1-(F-k)/2, R = 4p-2-F.

(a) Proposition VAC. If k >= p+1 then kappa^ >= 1 (no admissible normal form of an avoider has k >= p+1 and kappa^ = 0).

(b) Lemma P (pairing; strengthened from scope v1 item (b): ALL non-constant sign patterns). Let k = p+1 and
    (p-1)/2 <= kappa^ <= p-2. For every sign pattern z in {+1,-1}^k that is not constant, the multiset of signed rotation
    values of w^ has a value of multiplicity at least R-p+2 = 2kappa^+1.
    Lemma U (dominant pair). In the same setting there is a NONZERO a in Z_p such that for every non-constant z that value
    lies in {a, -a}; in particular at most p-2 rotation letters of w have a value outside {a, -a}.

(c) Theorem ROT-PP1-TOP. If SOME admissible normal form of w has terminal k = p+1 and kappa^ = p-2, then every rotation
    letter of w lies in one set {rho_c, rho_-c} with c != 0. More precisely, for a suitable such c the rotation multiset of w is
    rho_c^A rho_(-c)^(3p-5-A) with 2p-3 <= A <= 2p-1.

## Route to be checked (not assumed)
GRX selection sizes for all-odd terminal blocks; Cauchy-Davenport sumsets for the swap argument; (ZP) and CT for the multiset
bounds; a window argument on e(P) = #rho_a(P) - #rho_(-a)(P) over sets P of runs; the NF empty-run rule; finite case analysis by
|B| = number of rotation letters with value != a. Any step that fails is recorded with its exact obstruction in the
obstruction note; no weaker statement is substituted silently.

## Not claimed
Anything for 1 <= kappa^ <= p-3 at k = p+1 beyond (a)-(b); kappa^ = p-1 (separate pending ROT-SING+); reflection rigidity
beyond o_F <= p; any word-level assembly at o_F >= p+1; p = 5; novelty or priority; Lean; human review.
