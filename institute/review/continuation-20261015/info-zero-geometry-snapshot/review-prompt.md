# Hostile independent proof review

Read ONLY `/Users/jinleic/repos/aifours/institute/review/continuation-20261015/info-zero-geometry-snapshot/`. No file changes, no delegation, no network, and no local reads outside that directory. This is mathematical proof review, not a literature or novelty search. Snapshot hashes are in manifest.json.

Review candidate.md adversarially, using the three accompanying proof files only for the previously reviewed definitions and tools. The candidate is untrusted Codex output. It claims new necessary conditions for odd 8-variable half functions g,h with |G|+|H|<=28. No known example satisfies those full hypotheses, so do not mistake finite controls in weaker relaxed settings for existence.

Highest-priority claims:
1. For R=Kg-Kh and p=R/8, p-hat is 0 or +/-64. Then H(p^2) is divisible by32, and the zero set Z has even size, XOR0, and GF(2) second moment matrix equal to the principal-six-Pfaffian cofactor matrix of the polar matrix B of D=p mod2.
2. Correct transformation law of that matrix, rank 0/2/8 for polar ranks <=4/6/8, and all zero-count/equality implications. Look carefully at the affine translation arguments, six-point argument, and ten-point rank8 Arf/weight conclusion.
3. E=(p-D)/2 mod2 has degree<=4 with quartic coefficients Pf(B_I). Check every divisibility exponent and the ANF-moment complement indexing. The residual affine dimension is93.
4. In the BALANCED (rank4,weight128) case, there are exactly8 Walsh zeros forming a linear three-flat, all 128 Q=1 coefficients on s-perp have magnitude24, and only the three listed complete magnitude histograms survive. Check exact slack identity, all seven integer triples, the mod3 exclusion, and that R genuinely matches the on-s-perp spectrum with an affine sign.
5. Scope: the report excludes NO entire one of the eight residue types and does not settle balanced NL242 existence. Check the fake-spectrum example if it reveals a real inconsistency, but prioritize universal proofs over bookkeeping.

Return JSON with verdict (correct | correct-with-fixes | wrong | incomplete), findings [{severity,location,objection,required_fix}], strongest_supported_statement, unproved_claims, audit_suggestions, significance_limits. Give explicit counterexamples for defects when possible; label uncertain objections. No cosmetic suggestions. This model review is not peer review and establishes no novelty.
