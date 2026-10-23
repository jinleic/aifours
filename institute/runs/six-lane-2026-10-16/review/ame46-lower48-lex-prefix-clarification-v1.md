# LOWER48 r2: first-position lex-prefix clarification

LOWER48 r2 LF155–157 says that the previous-prefix literals are omitted at the first non-fixed position. Precisely: set the fictitious prefix q₀ = true, simplify, and **drop the entire tautological clause (¬q₁ ∨ q₀)**. Do not turn that clause into the unit ¬q₁.

The first non-fixed position has comparison clause (¬x ∨ y), and exactly these four chain-definition clauses:

- (¬x ∨ ¬y ∨ q₁);
- (x ∨ y ∨ q₁);
- (¬q₁ ∨ ¬x ∨ y);
- (¬q₁ ∨ x ∨ ¬y).

They state q₁ ↔ (x ↔ y). Subsequent positions use all five clauses printed in r2. This is the code in the frozen `large_t_lex.py:232–238` and the parent's independent schema regeneration `ame46_lower48_lex_from_text_v1.py`. The latter matched all 37 RUP-verified final-CNF hashes. No code, certificate, theorem or proof dependency changes; this removes an ambiguity in the first-position shorthand.
