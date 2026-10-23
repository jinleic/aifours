# ASSEMBLY-LS parent trust-label and wording erratum v2

Recorded at 2026-10-19T11:07:30-0700. Read after immutable proof v2 ac854c31ae1446c4710f3c19bb1beb80d8c25333aeb6b350c7f7d4dc7fafcfb3 and parent erratum v1 572308b87c62237f77dab554afb29152b568b11c027dc8825c5923895b93f8f7. Disposes Claude review a95e9c6a7aa7b172a5cde4cd7fb975f0873e0ad88895365441e78c9460bf5b89: required MINOR N1 and selected optional O4/O5/O6/O8. No theorem, case split or proof step changes; all other optional items are recorded in the verdict as citation notes. Each Old span occurs exactly once in the immutable proof.

## N1 required: ROT-LS trust label

Old:
````text
There is no hypothesis on o_F(w).
````

New:
````text
There is no hypothesis on o_F(w). For p >= 11 this uses Lev 2022 Theorem 2 at statement level when the invoked normal form has floor(2p/3)+1 <= kappa^ <= p-3; p = 7 is Lev-free.
````

## N1 required: residual INV* consequence

Old:
````text
CANDIDATE_UNVERIFIED; not separately frozen as a theorem).
````

New:
````text
CANDIDATE_UNVERIFIED; not separately frozen as a theorem; conditional on Lev exactly as Proposition ROT-LS).
````

## N1 required: residual rotation coverage

Old:
````text
- Rotation half: ROT-LS covers every avoider having SOME admissible normal form with k <= p-1 (any o_F);
````

New:
````text
- Rotation half: ROT-LS, conditional on Lev exactly as stated in Section 0, covers every avoider having SOME admissible normal form with k <= p-1 (any o_F);
````

## O8 wording: p5 specialization

Old:
````text
(A) and (B) with o_F <= 4 = p-1 are verbatim items 1-2 of
````

New:
````text
(A) and (B) with o_F <= 4 = p-1 are items 1-2, specialized to p = 5, of
````

## O8 premise clarity

Old:
````text
For kappa^ >= 1 the scope's sentence there
("ROT-FB (a) ... for every terminal 2 <= k <= p-1") is used as written;
````

New:
````text
For kappa^ >= 1 the premise is ROT-FB(a) exactly as accepted at R18/olson-FB-parent-verdict-v1.md:11-12, not the planning sentence of the scope;
````

## O4 normalization wording

Old:
````text
6. The ledger and normalization preserve o_F <= p-1 from length 4p-1 to every length-(4p-2) word used
````

New:
````text
6. The ledger preserves o_F <= p-1 from length 4p-1 to every length-(4p-2) word used, and normalization gives k <= o_F <= p-1 for each such word
````

## O5 residual quantifier

Old:
````text
Residual rotation cells: every admissible normal form has terminal k >= p+1, or k = p
  with (S1) failing at some kappa^ >= floor(2p/3)+1.
````

New:
````text
Residual rotation cells: every admissible normal form has terminal k >= p+1, or has k = p
  with (S1) failing at its kappa^ (necessarily kappa^ >= floor(2p/3)+1).
````


O6 note: after E2, "below every LS threshold" refers only to LS-ALL length thresholds. It does not mean (S1) is unavailable: S1-sharp still supplies (S1) without a length hypothesis when kappa^ <= floor(2p/3).
