# Frozen acceptance

1. Exact finite completion of all 16 specified words over the original two-letter alphabet, or a universal proof of nonexistence.
2. Positive path: witness.json is a finite list of distinct nonempty words over {a,b}; all original words are present; Sardinas–Patterson confirms unique decipherability; exact Kraft sum is 1. For a finite uniquely decipherable code this establishes completeness. Reviewer must check the cited theorem or supply its proof. Independent caller will replay with another implementation.
3. Negative path: Solution.lean, appended to the immutable Statement.lean, proves `ShorCompletion.noncompletion : ¬ ShorCompletion.HasFiniteCompletion` with no added hypotheses or axioms. Full scope and assumptions audited in proof.md. All-n mathematical bridge required, not a finite search or a statement about only one-b codewords.
4. `python3 -B verify.py` returns 0; frozen task/acceptance/verifier/statement unchanged. The verifier's lack of a certificate is an honest failure, not a request to weaken it.
5. Partial obstructions, literature recovery, finite computations and failed attempts are valuable but are not acceptance. Reviewer MUST return done:false on any such outcome.
6. If only the published n=330*k, k>=4 obstruction is recovered, identify it as reproduction and do not run redundant bounded searches. The claimed 660 divisor would remain partial even if correct.
7. Keep immutable source and journals; no claim of novelty without current primary-source comparison. No new paid run, external contact, config change, out-of-repo mutation or background process left behind.
