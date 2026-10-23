# Erratum 1 to reduction R1 and to structural note S4 (2026-10-19T05:23:45-0700, ContinueCFR21)

Base files (preserved unchanged):
- R1: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/reduction-R1-beta-route-v1.md, sha256 eabe1fc4375ed05492e684d38418bda2c294305269240503e6e96c27c1a4669b
- S4: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/structural-note-S4-v1.md, sha256 49926433125f49a59095bcecc081b21a54fbb8f840566535a80fcfb44de250dc
Both findings come from the parent audit (IRC, 2026-10-19). Lemma U remains an exact-anchor candidate, pending the
parent's independent audit; nothing here supports a broad conclusion about the existence of six MOLS(39).

## E1 (R1, Proposition R1, base lines 25-33): STATEMENT CORRECTION — withdraws the displayed restriction on g
Fact checked directly on the raw anchor (sha256 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a): row D_0 is not zero mod 13. Its first eight entries
mod 13 are [0, 1, 12, 0, 0, 10, 3, 10].
The proof in R1 yields f = mu^(-1) (D*_6 - D*_0) + D_0. If this is written as f = mu^(-1) (D*_6 - D*_0 + g), then
g = mu D_0, and g = D_0 (mod 13) is not 0 mod 13, because mu = 1 (mod 13). So the displayed clause "for a suitable
column function g with g = 0 mod 13" is false as stated, and it is WITHDRAWN. The withdrawal changes the statement (it
removes a wrong restriction) and is recorded here as a statement change, not as an editorial fix.
Corrected Proposition R1. Let D* be any (Z_39,7;1)-DM whose rows 0..5, after normalising at row 0
(D*'_x = D*_x - D*_0) and labelling its columns by C, reduce mod 13 to beta (beta_x = (D_x - D_0) mod 13). Let eps be the
sign given by Lemma U for the mod-3 part of D*'_0..5, and put mu = 1 if eps = 1 and mu = 14 if eps = -1
(mu^(-1) = mu). Then
    f := mu^(-1) (D*_6 - D*_0) + D_0
satisfies: [D; f] is a (Z_39,7;1)-DM.
Converse: if [D; f] is a one-row extension, normalising at row 0 gives the beta-route instance with new beta-row
    beta_6 = (f - D_0) mod 13,
not f mod 13 as the base text says.
Proof: as in the R1 base text, whose last two sentences already give [D; mu^(-1) D*'_6 + D_0] (that is, the formula
above). Only the statement and the converse formula change.
Effect on the consequences: none. Consequence 1, that the beta route for this anchor is equivalent to its free one-row
extension, still holds, and the status is still UNKNOWN. Consequences 2-4 do not use the withdrawn restriction.
Conditional status unchanged: R1 still depends on Lemma U for the exact anchor.

## E2 (S4, "Reading" item 1, base lines 31-33): QUALIFICATION
Base sentence: "So for these DMs the mod-3 part is determined by the mod-q skeleton up to sign and row constants."
Corrected: this holds for the five measured six-row objects (the anchor, Sage DM21/DM33/DM51 and P21; exactly 2 rainbow
classes, ±alpha). It does NOT hold for the Singer-type (57,8;1)-DM or its seven-row restriction. Each of those has
4 rainbow classes = two sign pairs (±alpha and a second pair ±alpha'), so its skeleton admits a mod-3 lift not
equivalent to ±alpha up to row constants. Lift_route2 control L3 (N_classes = 4, two 'other') agrees.
Whether the second Singer pair gives a DM that is inequivalent under the full equivalence group was not examined.
No other S4 statement changes.
