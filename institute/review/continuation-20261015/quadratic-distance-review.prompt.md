# Hostile independent mathematical review

Read-only. Read only:
- /Users/jinleic/repos/aifours/information-science/evidence/hard-continuation-20261015/quadratic-distance/
- the parent proof.md in that evidence root (only its odd-spectrum and canonical-sign lemmas as needed)
- /Users/jinleic/repos/aifours/institute/review/continuation-20261015/boolean-residue-audit.md
No writes, shell, model delegation, credential reads, external contact or global context. Do not import the unrestricted RM(1,9) preprint result as a premise.

A new candidate UNIVERSAL necessary condition is proposed in quadratic-distance/PROOF.md, not a corpus exclusion: for ANY odd-weight eight-variable halves g,h with |G|+|H|<=28 everywhere, their quadratic square-residue bits J_g,J_h differ on at least96 points. There is a further intrinsic corollary for a balanced nine-variable target with supportXOR s!=0: at least96 of its256 frequencies a.s=0 have |W_f(a)| in{8,24}.

Audit from scratch. Try to falsify the claim, especially:
1. Are J_g,J_h always quadratic and canonical spectra genuine Walsh spectra up to affine sign? Is affine frequency translation handled correctly?
2. Is the full pointwise majorant m²+n²+4(k(m)+k(n))<=408+384(J_g+J_h mod2) correct on all allowed magnitudes, with precisely the stated equality cases?
3. Does wt(D)=64 force every equality and the 64/128/64 partition counts?
4. Does weight64 of an eight-variable quadratic really give affine coordinates D=uv? Do the three six-variable restrictions share a polar form, and does bias sum-64 force its rank<=2?
5. Most vulnerable step: does that low rank imply J_g and D together depend on <=7 affine coordinates, making S translation-invariant and its Fourier support<=128? Account for linear terms induced by coordinate changes and all u,v cross terms.
6. Is the energy contradiction45088768>33554432 valid, and is96 the next possible quadratic weight?
7. Does the intrinsic corollary correctly choose complementary origin s, prove equal half-support XORs, and identify J_g+J_h with W_f/8 mod2 on s-perp? Check all divisibilities/signs without silently assuming a zero.

Finite controls audit.json are support only, not a proof substitute. The theorem does NOT settle balanced NL242 existence and does NOT claim novelty. Known residue/canonical tools are explicitly credited.

Return JSON: verdict(correct|fixable-gap|fatal-gap|inconclusive), findings[{severity,location,objection,required_fix}], independently_checked_steps, attempted_counterexamples, strongest_supported_statement, significance_limits. A correct verdict must address the seven-coordinate step explicitly. Never bless an unsupported step to preserve a hopeful result.
