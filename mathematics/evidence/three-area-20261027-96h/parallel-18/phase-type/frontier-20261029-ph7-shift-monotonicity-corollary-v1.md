# Spectral shift monotonicity: no PH7 for ANY ratio z>=8/9

**NEW WRITTEN COROLLARY CANDIDATE** of `frontier-20261029-ph7-eight-ninths-impossibility-v1.md` (SHA256 `599feaa589a6281316786cdd4d19050a88ba2945a12ce253d5f04678e862b2d4`), with a short new lemma. Not independently reviewed; parent adoption, formal proof and novelty clearance pending. MathResearch96h-2, original math-1. Clock disclosure: no separate `/bin/date` was run immediately before this write; the last actually observed clock before writing was **Thu Oct 29 05:34:27 PDT 2026** (checkpoint), and the pin observation is recorded when the file is hashed.

## 1. Shift lemma (spectral realizability is downward closed in z)

**Lemma S.** Let G be an irreducible n-by-n Metzler matrix with spectral bound0 and positive right/left Perron vectors r,l (`Gr=0`, `l^T G=0`). For t>=0 put

    G_t = G + t (r l^T/(l^T r) - I).

Then G_t is an irreducible Metzler matrix with spectral bound0 and

    det(yI-G_t) = y * C(y+t)/(y+t),     C(y):=det(yI-G).

*Proof.* `P=r l^T/(l^T r)` satisfies `P^2=P`, `GP=PG=0`. Off the diagonal `G_t>=G` (indeed every off-diagonal entry is positive when t>0), so G_t is Metzler and irreducible. On the G-invariant splitting `range(P)⊕ker(P)`, `G_t r=0` and `G_t=G-tI` on `ker(P)`; hence the Perron eigenvalue stays0 and every other eigenvalue moves from lambda to lambda-t with the same Jordan structure. □

Consequently, if `C(y)=y[(y+1)^2+z]^2 Q(y)`, then `(1+t)^(-1)G_t` is an irreducible Metzler matrix of spectral bound0 with characteristic polynomial proportional to

    y[(y+1)^2+z/(1+t)^2]^2 Qhat(y),

so the critical-spectrum problem at ratio z yields one at every smaller ratio `z/(1+t)^2`.

## 2. Corollary

**Corollary.** For every c,d>0 and every `z=b^2/d^2>=8/9`, the transform `H(s)=c(a^2+b^2)^2/[(s+c)((s+a)^2+b^2)^2]`, a=c+d, has no phase-type representation with at most seven states.

*Proof.* Suppose one exists at some z>=8/9. Since z>1/2, the irreducibility theorem `frontier-20261028-ph7-global-irreducibility-v1.md` (SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`) supplies an irreducible 7-by-7 Metzler G of spectral bound0 with `y[(y+1)^2+z]^2` dividing its characteristic polynomial. Apply Lemma S with `t=sqrt(9z/8)-1>=0` and rescale by `1+t`: the result is an irreducible 7-by-7 Metzler matrix of spectral bound0 whose characteristic polynomial is divisible by `y[(y+1)^2+8/9]^2`. Sections 3-4 of the 8/9 impossibility candidate apply to ANY such matrix (they use only irreducibility, Metzler sign pattern, spectral bound0 and this divisibility), giving a contradiction. □

In particular the set of ratios at which a seven-state PH representation exists is contained in z<8/9, and the corresponding SPECTRAL problem (irreducible 7x7 Metzler matrices with the double critical pair) is downward closed in z. Together with the retained eight-state construction at z=8/9 this shows the minimum order is >=8 for all z>=8/9 and exactly 8 at z=8/9; minimum orders for z>8/9 are not determined here.

## 3. Checks and scope

A floating diagnostic in the owner kernel (not a premise) applied Lemma S with t=0.3 to a numerically constructed 7-state critical matrix at z=0.78: all off-diagonal entries became positive, the Perron eigenvalue stayed0, the double pair moved from `-1±0.88318i` to `-1.3±0.88318i`, and after rescaling the normalized ratio was `0.78/1.69`.

Lemma S is elementary spectral-projector algebra; the corollary inherits every import and the unreviewed status of the 8/9 candidate. No novelty, formal, kernel, human or cross-vendor acceptance is claimed. Historical holds and process findings are unchanged.

END - no seven-state PH representation exists for any ratio z>=8/9.
