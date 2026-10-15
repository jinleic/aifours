# Exact semifilter Questions 2 and 3: audit and formal proof

This file is immutable. Work only in this Git repository. Date: 2026-10-14 PT.

## Goal and source

Audit and complete the exact independently stated Questions 2 and 3 of 10000 Selected Problems in Sciences, mathematics volume, book page 62 (PDF78): find left-divisible filters/semifilters L for which R_L is exactly Reg, and give a necessary and sufficient condition for R_L1=R_L2. Do not claim the entire chapter (Questions4/5 are outside scope) solved. `candidate-proof.md` is a complete but untrusted all-parameter candidate derived by the assigning agent; improve/correct it, do not merely approve it.

Let X be any finite alphabet, including empty; M=List X under concatenation, ε=[]. D_u A={v:uv∈A}. A semifilter L contains M, is closed under (A Δ B)^c, and under EVERY left quotient D_u (u∈M). There is NO upward-closure axiom for a semifilter and NO properness assumption. For filters replace complement-symmetric-difference axiom with intersection plus upward closure. Source congruence: u~v iff {w:uw∈T iff vw∈T}∈L. R_L is the languages T for which this relation has finite index. Reg means ordinary regular language, equivalently finitely many left residuals.

Complementing L gives a derivative-invariant F2-vector subspace V={A^c:A∈L}. Write C(V) for T whose residual cosets D_u T+V form a finite set, so R_L=C(V). Candidate normal form:
C(V)={K+Σ_(i=1..n) A_i a_i B_i: K,A_i regular, a_i letters, B_i∈V, n finite}.
Products count factorizations modulo 2, not existential concatenation. Candidate Q2: R_L=Reg iff L⊆Reg; for filters iff all complements finite, equivalently L=L_U={A:A^c finite subset U} for a suffix-closed U⊆M. Candidate Q3, expressed without generalized-recognizability on the criterion side: for both ordered pairs(j,k)=(1,2),(2,1), every B∈V_j admits the above finite parity expression with errors B_i∈V_k. This is equivalent to V1⊆C(V2) and V2⊆C(V1), provided idempotence C(C(V))=C(V) is actually proved.

## Required proof surface

1. Derive the complement translation from the ORIGINAL right-context congruence, with all quantifiers and ε conditions.
2. Prove the derivative split D_x(A a B)=(D_x A)aB+Σ_(x=uav,u∈A)D_vB by exhaustive disjoint factorization cuts, including x=ε.
3. Prove the finite-residual normal form by finite state representatives r_q with r_q0=ε and exact errors E_q,a=D_aD_rqT+D_rδ(q,a)T∈V. Explicitly eliminate the recurrence by word-length induction; the path languages A_q and terminal language K are regular. Error tails are NOT assumed regular unless V⊆Reg.
4. Prove regularity of parity products of regular languages, not by silently replacing parity with ordinary products. A finite residual/state vector argument is sufficient.
5. Prove C(V) closed under regular-left parity products with B∈C(V). The sums of residual cosets of B range in their finite F2 span (at most 2^m possibilities); it is WRONG to assert such sums lie in V.
6. Prove Q2 and Q3 and the filter classification, handling unary and empty alphabets and improper filters. No added assumption equivalent to the goal, no bounded n surrogate.

## Lean deliverable

Create `Formal.lean` with a substantive all-parameter formalization of the finite-residual mechanism and, if feasible, exact Q2 and Q3. Full Q2/Q3 formalization is desirable but not a license for padded helper counts or replacing finite index with the desired normal form as a definition. At minimum formalize a genuinely load-bearing theorem (e.g. finite-state residual elimination/normal form or saturation with correctly stated proved closure ingredients), clearly label any remaining written-only bridge. Use Mathlib language/MyhillNerode definitions where feasible. A theorem that merely assumes full normal form/idempotence or an equivalent full goal is NOT success. No sorry/admit/new axiom/native_decide/ofReduceBool/unsafe/opaque/custom tactics/external evaluation. Include #print and #print axioms for the theorem roots. Create `claims.json` with theorem root names ONLY, exact intended mathematical statements, assumptions, scope, and novelty status. `NegativeControl.lean` is immutable and must fail because 0=1 is false, not missing synthesis.

Use existing read-only Mathlib cache only:
  PATH=$HOME/.elan/bin:$PATH lake env lean -j 4 /ABSOLUTE/PATH/TO/THIS/REPO/Formal.lean
with cwd `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/lean-verify`.
Do not write files into that cache cwd and do not run lake build/update. Parent owns fresh Comparator verification. Read-only `math/lean/docs/134.md` and `math/lean/ComparatorChallenges/GeneralizedStarHeight.lean` give nearby finite-automaton conventions, not a semifilter solution; do not import the large OAI tree.

## Prior art and honesty

`sources/prodinger1980.pdf` is the lawful author copy; OCR is supplied for search, equations must be image-checked. The original imposes filter hypotheses in Section5 before its Boolean-algebra result. Do NOT assume Boolean closure for arbitrary semifilters.
`sources/guo-wang-shum2010.pdf` is recovered lawful publisher full text. Thms2.7,3.3,3.4 concern cofinite and suffix-generated special filters; the paper's conclusion says general semifilters are difficult. Its Thm2.4 appears to omit Prodinger's filter qualification; do not import it uncritically.
2017 DOI10.1142/S1793557117500450 and 2024 DOI10.1007/978-981-99-9171-6_3 primary full texts have not been recovered. The assigning agent is independently investigating these outside this repo while you work. No search miss proves novelty. A correct proof is NOT a discovery without comparison.

## Boundaries and acceptance

Do not alter TASK.md, ACCEPTANCE.md, verify.py, NegativeControl.lean, global model/credential/runtime configs, shared caches, math/, outside files, or other tasks. No installs, dependency downloads, deletion, reset, push, live infrastructure, or external contacts. No extra HMZ run or reviewer process. Do not commit beyond the already frozen baseline. Up to four CPU threads / twelve GB RAM. Preserve all failed attempts and journals. Finish artifacts before running checks; each final artifact has one final verification pass, necessary intermediate Lean proof attempts may be kept as research evidence.

Run `python3 verify.py` on the completed artifact. Write `RESULT.md` separating written full-goal status, exact Lean coverage, audit findings/dispositions, and novelty. The reviewer must return done:false if either exact Q2 or exact Q3 has a substantive written proof gap, if formal roots are falsely promoted as the full answer, or if claims are unsupported. A correct all-parameter written proof plus a genuinely load-bearing checked Lean component may be accepted as a written resolution with explicitly partial formalization; only partial math progress must never pass. Do not pretend prior-art clearance.
