# Addendum 13: quantifier correction — S_pair vs S_both; two withdrawals

Owner: InfoResearch96h-2 / info-1. Observed `/bin/date`: `Fri Oct 30 03:59:06 PDT 2026`. ADDITIVE; addenda 11 (`cc2db1bb…`) and 12 (`ea5acade…`) bytes unchanged. Parent quantifier correction accepted; no code/values.

**(Q1) Definitions.** **S_pair** := core slack at (a,c) ONLY. **S_both** := core slack at (a,c) AND at the edge (a,u), u=a+1/2 — this is the ORIGINAL addendum-4/f291 S. They are distinct sets and are never conflated here; addendum-12's T1/T2 concern S_pair only.

**(Q2) S_both, subject to independent review.** At an S_both point, the edge y=0 derivation (R1(0)>=Π0(0)+1, R0>Π0 pins Π0(0)=2a, hence λ>=v+(2a+1+m)²) forces (E); the convexity argument then forces edge corner compatibility, and rising tail faces propagate it to c. Hence S_both={a>=0,c>=u,(E)}=S_full, and addendum-4's Δ display is EXACT there (both correction terms vanish).

**(W1) Withdrawal.** Addendum-11's parenthetical "Π1(y;d)=2d−y at both endpoints" is WITHDRAWN: at c>u the independent tail may be interior or lower; only φ_d=Π1(·;d) under corner compatibility is claimed.

**(W2) Withdrawal.** "Edge integral vanishes iff (E)" is WITHDRAWN for S_pair: corner compatibility on (a,u] need not imply the y=0 condition without edge-core slack. Only the tested conditional identities are retained: (E) ⟹ vanishing (both sets); vanishing on S_both ⟹ (E).

Addendum-12's pair-only theorem and the general edge-correction formula stand as separate S_pair statements.
