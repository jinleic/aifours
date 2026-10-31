# Exact two-local operator form of the residual's negative Choi space

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN all-variable structural representation for the existing source-independent residual method. It does not select or evaluate a physical C/state/control, prove a rank bound for the full negative space, establish q3/2-positivity, or claim novelty, operational significance or review/formal acceptance.

## 1. Local identity and traceless projections

On operators over H=(C⁴)^tensor3 define the normalized local identity projection

`E_i(C)=(I_i/4)⊗Tr_i C`, `T_i=Id−E_i`,

with all tensor factors inserted at their original sites and with the **unnormalized** partial trace. The E_i are commuting Hilbert–Schmidt orthogonal projections onto matrices proportional to identity at site i; the T_i project onto locally traceless factors. The eight products obtained by choosing E_i or T_i decompose the full operator space orthogonally.

Under the standard global operator-vectorization and fixed regrouping by local input/output pairs, the local Bell projector `P_i=|Omega_i><Omega_i|/4` acts exactly as E_i, and its orthogonal complement Q_i acts as T_i. Consequently the complete negative eigenspace of the fixed residual Choi partial transpose from `frontier-20261028-d4-residual-choi-partial-transpose-spectrum-v1.md`, SHA256 `dba645c69cadfa5d1d1f5d487107a75b0e21bd039e1553fa431dd78daf3d549a`, corresponds exactly to

`E_- = E_1 T_2 T_3 ⊕ T_1 E_2 T_3 ⊕ T_1 T_2 E_3 ⊕ E_1 E_2 E_3`.   (1)

This statement concerns the Choi **operator space**; C below is an arbitrary complex 64×64 operator used to label a vectorization, not a selected physical input.

## 2. Equivalent exact two-local trace identities

For any complex operator C, write `E_123=E_1E_2E_3`. The following are necessary **and sufficient** for `C∈E_-`:

`E_i E_j C = E_123 C` for all i<j,                                      (2)
`C = E_1 C + E_2 C + E_3 C − 2 E_123 C`.                              (3)

Indeed, (1) makes every two-identity/one-traceless sector and the all-traceless sector vanish. This immediately gives (2); expanding `T_1T_2T_3 C=0` and substituting (2) yields (3). Conversely (2) eliminates every two-identity/one-traceless sector, and (3) makes `T_1T_2T_3 C=0`, leaving exactly the odd-identity sectors in (1).

Since `E_123 C=(Tr C/64)I_H`, these equations are literally

`Tr_(ij) C = (Tr C/4) I_k` for every complementary site k,                (2')
`C = Σ_i (I_i/4)⊗Tr_i C − (Tr C/32) I_H`,                            (3')

with the factors placed at their original sites. Thus the residual's **whole negative eigenspace** is exactly the operator subspace consisting of a scalar part plus the allowed locally traceless two-site parts. This characterization does not require choosing a basis of that subspace or assuming its elements commute or are Hermitian.

## 3. Exact remaining rank/positivity gap

The earlier universal lemma `frontier-20261028-d4-residual-negative-sector-rank-v1.md`, SHA256 `3301a558ee0d815991b05737cfc31a7447b57c4a3f53dc968cb09526824ed274`, proves Schmidt rank>=4 within any **single** one-Bell negative sector and rank64 in the all-Bell sector. Equations (2')–(3') now provide a concrete all-variable starting point for the harder **mixed-sector** question: whether a nonzero rank<=2 operator can satisfy all these identities, and, independently, how a rank<=2 operator's positive/negative sector components contribute to the quadratic form.

No such rank lower bound for the whole direct sum, no 2-block positivity, no residual PPT, and no q3 inequality/counterexample is established here. Even a future proof that the negative subspace contains no rank<=2 vector would not by itself exclude a rank<=2 vector with both positive and negative components and a negative total form. The public-source d4 certificate remains the separate conditional full-target route. No chosen physical C/control or numerical probe, all-d/novelty, operational, parent/f62, human/family or formal/Lean claim is made. Historic held outcomes and the separately disclosed earlier cadence gaps are unchanged.
