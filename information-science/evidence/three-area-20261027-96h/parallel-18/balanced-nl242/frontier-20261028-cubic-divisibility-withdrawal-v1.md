# info-6 frontier: additive withdrawal of false cubic divisibility claims

Owner InfoBalancedNL242-2-2. Native `/bin/date` before this record: **2026-10-29T02:16:37-0700**. This is a substantive author-found correction. The pinned original files remain immutable. No falsity is inferred for any other claim merely because it is adjacent; affected claims are explicitly identified below. None of the withdrawn results was parent-adopted.

## Finding: the six-variable divisor-eight lemma is false

The unreviewed `frontier-20261028-rank2-zero-divisibility-v1.md` incorrectly asserted that every degree≤3 Boolean polynomial on F₂⁶ has weight divisible by 8. Its inclusion-exclusion proof contains an arithmetic error: for three disjoint cubic monomials, the coefficient has only a factor 4 and their union can cover six variables, so that term need not be divisible by 8.

A concrete counterexample is

    H(x)=x₀x₁x₂ ⊕ x₃x₄x₅ ⊕ x₀x₁x₃,

which has degree 3 and weight **14**, not divisible by 8. Translating H by a support point preserves degree and weight and makes H(0)=1. The pinned checker verifies its full ANF and exact support.

The checker also embeds this translated H into a **formal even-half non-witness** with an anisotropic rank-two quadratic q (64 zeros), a degree-three mod-8 correction, k(0)=0, |k|≤6, even first sum 128, and even squared energy `64·118`. It has **Z=14** and **G₃=114**, so neither is a multiple of 8. It supplies no odd half, full correlations or Boolean inverse and does not show an actual f exists. It does directly refute the claimed general cubic-divisibility derivation, even after the stated even-half energy and first-moment filters.

## Withdrawn candidates and exact scope of effect

1. **WITHDRAW in full as a scientific input** `frontier-20261028-rank2-zero-divisibility-v1.md` SHA256 `0f84a22a93b37690b7d6d0f24e5142f6a18c2ed6cb5b973357f753395b509a4d`, 36 LF. Its claims Z divisible by 8 and the Z option table are unsupported.
2. **WITHDRAW in full as a scientific input** `frontier-20261028-rank2-parity-profile-v1.md` SHA256 `a2f2fdc481efa967f5e61d95cc72c8aea19efd10a72c43c877eb8dc16316b1ab`, 42 LF. Its Z options, n₁/n₃ parity and peak range depended on the false zero divisor. Some could have alternate proofs, but none is adopted or asserted here.
3. **WITHDRAW in full as a scientific input** `frontier-20261028-rank2-cubic-residue-v1.md` SHA256 `945f9859990b0b33fa77f68f8d6522d2f88c7c9bee8d5f69774d49176b974982`, 50 LF. Its G₃ divisor-8 and range table are unsupported.
4. `frontier-20261028-rank2-D28-profile-v1.md` SHA256 `c0a9de1ca74f7ecd8ced70d5cb45115563e1f6cca20efc07c7c77364595d48bc`, 35 LF: its standalone phrase “elementary degree-three weight divisibility” is **withdrawn**; the packet's D28 formulas and formal profile checks did not invoke the false six-variable divisor. It remains unreviewed and is not hereby adopted.

The author-written `frontier-20261028-lowrank-valid-profile-v1.md` SHA256 `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac`, 63 LF, does **not** cite or use these divisor claims. The author-written `frontier-20261028-rank2-Z8-plane-v1.md` SHA256 `3f8c57673df72ccb756c6410354e4cb5c0c878d61e2927274a30d34f84e2368b`, 41 LF, uses only the valid minimum-support bound and equality, not weight divisibility; it remains separately unreviewed. The degree≤4 full-rank quartic congruence paper uses its own correct eight-variable degree-four expansion and does not use this false divisor-eight lemma. These observations are dependency distinctions, not independent reviews or acceptance.

The formal Z14 even-half model has **not** passed the full original caller. The original witness-or-unrestricted-exclusion target, the low-rank reductions and the Z8-plane candidate remain open at their respective stated scopes. Main was notified immediately to stop use/review of the three affected files.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-cubic-divisibility-counterexample.py` | `fa3a3e7c0faea48175b619382c9d0a1531a7d12192d506990a9ca5bae042c3ff` | 48 | exact counterexample/control |
| `frontier-20261028-cubic-divisibility-counterexample-result.json` | `fdc5b02d1f3debf3351e4528268887b91646f033bdf859771e9e2e310e34261a` | 302 | explicit formal even-half NON-WITNESS |

**END.**
