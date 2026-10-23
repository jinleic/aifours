# USK parent erratum v2 — signed-sum routing through D*

Recorded 2026-10-20T01:15:41-0700 (`/bin/date`). Governs proof-USK-v1.md SHA256 a88c65e201a0446212d3eceb6b1d6316021d5542aa9d0ddcfa0f5d93e27f6623, read after parent erratumv1. No theorem or proof-strength change.

At proof LF89–91, the SS statement is instantiated using the locally proved density Lemma D*, NOT PL Lemma D: for fixed P put Pos=Pos(P), Neg=Neg(P). The bijection J ↦ (J∩Pos) ∪ (Neg∖J) over letter occurrences gives sum_(l∈J) eps_l c_l = sum_(l∈U)|c_l|−nu(P). D* covers every integer in[0,B*], so the signed sums cover exactly[−nu(P),Pi(P)]. Each signed odd term has parity1, hence every such sum has the parity of |J|. Flipping all letters of the runs in P gives Pi(P)=Pi0−sigma(P), nu(P)=nu0+sigma(P). PL's explicit U/A/C proofs can therefore use this SS with D*; they acquire no PL-D/Setting-fact ancestor.

Remove "covering step of D" from package LF33–34 and proof LF288's imported-input list. That covering argument is re-proved in D* LF80–87. This disposes Claude MINOR-1 (input hygiene), not a mathematical gap.

Editorial: after exchanging the zero-target arcs/light side, reapply the stated gamma-normalization and c=±b convention to that chosen frame. At LF215 read "this contradicts SR; equivalently the GRX if-direction constructs an identity2p subword." Section-local F/H/W/E/N symbols retain their definitions.

No S1(a), Setting fact, FB-E, Theorem P, conditional CR, CJ or K2/K3 lemma is imported by this proof. Full ordered Olson and the middle range remain outside its scope.
