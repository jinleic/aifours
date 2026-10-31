# info-6 frontier: withdrawn global-mod-three profile draft

Owner InfoBalancedNL242-2-2. Initial native clock **2026-10-29T01:03:14-0700**; withdrawal clock **2026-10-29T01:10:41-0700**. This draft and its `frontier-20261028-lowrank-corrected-mod3-check.py` / result are **INVALID AND NONINPUT**: they incorrectly derived a mod-three relation from the odd-half squared-energy sum by dropping its factor 64. They were not sent to Main or used as premises in any previously pinned theorem.

For actual f, odd-half Parseval says `Σ k²=64(256−m)`; since `64≡1 mod3`, the correct comparison with odd magnitudes is

    256−m ≡ 256−n₃,  hence m≡n₃ (mod 3).

Any successor must independently derive and enumerate its consequences. The draft's claimed D/m/peak ranges and balanced-Q exclusion are withdrawn. The faulty checker and receipt remain preserved, not deleted. **END.**
