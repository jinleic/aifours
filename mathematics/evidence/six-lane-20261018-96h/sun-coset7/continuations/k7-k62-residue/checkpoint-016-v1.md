# Checkpoint 016 (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:01:20-0700. Previous: checkpoint-015 at 2026-10-19T06:53:10-0700.
- No computation; no process; no old/sibling/RUN artifact edited. Scratch notes frozen: `caseA-notes-v1.md`
  (6a943d0c...), `caseA-notes-v2.md` (a8d8e6ae...) - navigation only.

## Actual result since 015 (unreviewed scratch, not yet a candidate)
- Case A rows (c = 3) classified by number of W-fours with their rigidity (notes v2). Outside K7-TC-A22 some vertex has a
  single four in one orientation, so E >= 2 and that row is R3/R3' (e = 4), rigid: L_f = L_t, L_z subset L_t.
- t-side facts: u in P (alpha_tu = 4) has alpha*_tu <= 2, so its alpha*-row is not single-four (d* >= 2); a single-four
  vertex u0 (four f) forces alpha_tv in {2,4} for v != f (t-triangle rule).
- PFG-t tight structure: if Gamma^alpha is connected and t's alpha*-row on W is 44222 or 44122 (z four-type), every
  W-coset at t is {f1,f2,s}, {s,s'} or {o}, the {s,s'}-mass is 1/6 (44222) or 0 (44122), and D_z lies in {f1,f2,s}-cosets.
  With the transfers of a single-four vertex u0 that is an alpha*-two of t, its four f is not in P* (44222 case).
- Sub-structure F = K_{2,3} worked partially (twos forced on the 2-side alpha*-rows, R3 there, R1 on the 3-side when
  all three are in P); no contradiction found yet.
- (a2-zt5): the (a1) machinery (R3 at u in W' cup p, TR, CC, TZ) transfers with W = W' cup p and T = W; the analogue of
  RICH holds there (T* subset W3 impossible) - not yet written.

## Blocker
Case A beyond A22 and (a2-zt5) need a multi-structure case analysis; no single count closes them yet.

## Next bounded action
Enumerate the Case-A (F, F*) structures (degree types (1,2),(1,3),(2,1),(3,1),(2,2), twin rule, at most one 1 per row) and
test each with the TC/PFG-t counts; save notes v3. Next checkpoint by 07:35 PDT.
