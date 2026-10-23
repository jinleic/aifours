# ASSEMBLY-P parent trust and residual erratum v2

Recorded at 2026-10-19T13:15:31-0700. Apply to [proof v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/proof-ASSEMBLY-P-v2.md) `059033b00b669e10f0fa49bdb2fdb55a135a85644f792ef2b3b3d6eb61dacfb5` after [parent erratum v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-parent-erratum-v1.md) `d6fe328fb804dd21d17cf29a11b17ba1a03c7804659a1ea2eab442a07fbfe10d`. This disposes [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ASSEMBLY-P-claude-v2.prompt.note.md) `e6086a55a354263354e954d6326aa765e7092cd51ba8a7d384438476948df531`: no FATAL/MAJOR; five MINOR groups, of which 3 and 4 are optional. All are applied. The conditional composition and all numerical ranges remain unchanged; separately accepted premises are discharged by the parent verdict, not silently rewritten in the frozen proof.

## MINOR-1: binding trust sentence on every statement

Read ASSEMBLY-P (A)/(B), ROT-P and P0 (A0)/(B0) with: "Relative to the recorded classical imports, including S(p) at KPS-SLZ item-1/M-1 secondary-statement trust through ROT-KP+. For p>=11, Lev2022 Theorem2 at statement level enters exactly in invoked ROT-LS cells floor(2p/3)+1<=kappa-hat<=p-3; for ASSEMBLY-P/ROT-P it also enters through ONE-SHORT-LS at kappa-hat in U(p)." In ROT-P itself k=p, so the ROT-LS branch is absent. P0 never needs ONE-SHORT-LS. The row p=7 is Lev-free but **still uses S(7) through ROT-KP+**, at k=p and 2<=kappa-hat<=5. "No pending premise" does not mean no classical import.

## MINOR-2: import evidence and no-computation limits

The parent has now read these exact accepting-verdict statements, which were outside the original review excerpts:

- STAB-delta `ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5`, line 40: "Accepted imports: the prerequisite CF/RS/DGM-p/ROW/dichotomy/AP verdict ... S1-sharp at its lower-range kappa0 scope, SLZ3 as a bound on the shortest long zero-sum T, RED, and the external index-one theorem at n=p or n=2p as explicitly pinned ... The external theorem's proof was not replayed here."
- LS+-chain `4005007f4e073386236016b62949cba925cb5cde12ba13c24ce27b2a2c351b55`, line 36: accepted CT, CTgen, LS+2 and BASE1+; prerequisites CF through E1, CF(b) through R4, SLZ3 for a shortest long zero-sum, and the external index-one theorem at n=p; its proof was not replayed.
- ROT-SING parent verdict `12781c7c879bc1bcb8216aff73fd461c91cec8d177ec2a5bc0e0cf0121bc194f`, lines 5 and 36: NF, full-scope CT, GRX and classical Cauchy-Davenport; no Lev, S(p), (S1), ONE-SHORT-LS or pending lemma as a premise; prior records carry no computer-assisted premise for these interfaces, with no new finite computation used.

The DEP "Lev: no" and index-one entries are readings of those declared import lists, not a fresh transitive-proof audit. Withdraw the use of STAB-delta line 5 ("no computation ... performed for this verdict") as evidence of absence of a computation PREMIS​E. Those are distinct claims. For ROT-SING, use the explicit current parent verdict above instead of the unsupplied proof section 4. Do not infer any stronger trust class from silence in a status line.

## MINOR-3: P0 membership, not monotonicity in kappa

At proof lines 232-233 replace "exactly as" by "analogous to; preservation here is by the explicit membership check at lines 229-231". P0 is not monotone in kappa. A rotation deletion that drops o_F by 2 moves into o_F<=p-1; if o_F remains p then F and kappa stay unchanged. This is the actual preservation argument.

## MINOR-4: residual and comparison precision

- Lines 289-290: the residual without ONE-SHORT-LS is an **outer bound**, not a claim that each such word is unhandled or requires that particular route.
- Line 54: p=5,o_F=5 is "not fully covered", since k=5,kappa-hat<=1 has the accepted ROT-KP route. This packet still claims no p=5 theorem.
- Lines 312-313: existential ROT-LS alone supplies the rotation half; INV* there is ROT-LS plus restricted REFL.
- Lines 305-306: the stated stall condition is necessary only, and R>=3 is implicit since R<=2 is Case 1.

## MINOR-5: unused residual references

Read proof lines 115-118's RED/K0*, small-k and ROT-SING+ list as "formerly cited; not used or certified by this packet". Erratum v1 removed the statements to which that list formerly referred.

## No unreviewed strengthening

The reviewer's observation that (B) could avoid the ROT-SING dependency is not adopted as a new theorem. The existing sufficient dependency is sound and is discharged by its separate accepted verdict. No o_F>=p+1, unrestricted INV* or full ordered-Olson assertion follows.
