# Theorem P import closure — parent erratum v2

Recorded 2026-10-21T04:22:45-0700 (`/bin/date`). Read after erratumv1. Disposes Claude full-proof review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TheoremP-import-closure-claude-v1.prompt.note.md (ad3e8c9b8d52d6445089e1a7163a4ac751ad4fd7279bb1e85e3cf4c72ba9315d):0F/0M/3m, exposition only.

1. **Original order:** call the original word AB and the rotated word w′=BA. Cutting after a reflection only cyclically permutes the gap lengths, preserving F,N and sum floor(n_t/2). If P_A,P_B are the selected ordered products in the two parts, the rotated product is P_B P_A and the original product is P_A P_B=P_B^−1(P_B P_A)P_B. Thus the same selected2p positions give identity in the original increasing-index order, including pairs crossing the original boundary.
2. **Product formula:** induction from (A,E)(a,e)=(A+Ea,Ee) gives (a_1,e_1)…(a_k,e_k)=(sum_j (product_(l<j)e_l)a_j, product_j e_j). Prefix reflection parity therefore supplies the sign c_t stated in Step4.
3. **Notation/degrees:** use degV≤1, degZ≤2 (only upper bounds are needed); write wt(x) for the parameter-vector Hamming weight, distinct from selected length |S(x)|. Write |S(x)|=Z(x)≡0(modp) rather than an equality-to-congruence chain. Codex's exact-degree1 finding is already disposed byv1; weakening the degree2 wording changes no step.

The theorem statement and six-step argument are unchanged. No composite/prime-power/sharpness or full ordered Olson conclusion is added. No computation, source mutation or historical reclassification.
