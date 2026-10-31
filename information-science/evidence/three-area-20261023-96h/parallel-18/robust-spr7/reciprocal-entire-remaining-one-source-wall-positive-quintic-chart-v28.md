# SPR7 — COMPLETE positive-quintic stable-remainder chart for the ENTIRE remaining nonpalindromic source wall

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 07:44:02 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN BOUNDARY-REPRESENTATION CANDIDATE.** V26 proved the physical joint-two-source-zero face empty. This packet represents the ENTIRE remaining ONE inner-C2 zero-amplitude wall, with a fully general stable positive-real remainder, not a common-factor/notch subfamily. It does not establish a boundary solution, a strict-source perturbation, a physical obstruction or emptiness of that remaining wall.

Exact all-variable conventional mathematics only, including privately. No numerical/control instance, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FIVE owner findings/parentv37/current process history permanent; fifth probe and consuming guidance ZERO credit. Qualified future-only ACK SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad` preceded the later proofs. Frozen sources/gates unchanged.

## 0. What is covered, and all remaining guards

Retain the ORIGINAL reciprocal independent coefficient box, positive paired widths, a strict palindromic target B and ENTIRE global weak nonnegative pairing for ALL actual corners. The full v26 phase proof, SHA256 `2fd8b4109d64801992d7668ec5f580bc2f7d85478e1981f3da004dd30ba76d49`, implies ANY failure of nonpal source strictness has EXACTLY ONE simple C2 imaginary pair at t=p,0<p<1 in target quadrant2, and its reflected C4 zero above1. All other C2 roots are strict left. There are no imaginary-root multiplicity or second-pair cases left hidden.

Thus its source MUST have the form

`a2(s)=(s^2+p)H(s)`,

`H=s^5+h4 s^4+h3 s^3+h2 s^2+h1 s+c`,

`c=1/p`, H STRICTLY HURWITZ.

This packet gives a complete parametrization of EVERY such PAIR(B,a2) with Re(a2/B)>=0 globally. Full physical application STILL imposes the original positive widths, actual C1/C3 shapes/contact cells/global pairings/amplitudes, selected contacts and positive dual requirements. These are retained explicitly at the end, not accepted merely because one source pair has been represented.

Conventional named inputs: minimum principle, elementary holomorphic Taylor/Laurent expansion, real polynomial factorization, finite-dimensional linear algebra and the ordinary Hurwitz criterion if H's strict stability is checked through its finite leading Hurwitz determinants. The specialized pole extraction, quintic factor coverage and invertibility needed here are proved below. V26's full proof is the dependency for claiming this covers ALL remaining physical nonpal walls.

## 1. Exact lossless pole extraction with NO restricted stable remainder

Let F=a2/B. Its global boundary positivity and infinity limit1 give strictly positive real part inside the right half-plane. Thus G=1/F=B/a2 is positive real there. At its genuine simple imaginary pole s0=i sqrt(p), a Laurent residue R must be REAL POSITIVE: along s-s0=r exp(i theta), -pi/2<theta<pi/2, positivity forces Re(R exp(-i theta))>=0 for every theta; the two endpoint directions make R real, theta0 makes it positive, and a genuine pole rules out0. The conjugate pole has the same residue.

There is consequently a UNIQUE r>0 such that

`G(s)=W(s)/H(s)+r s/(s^2+p)`. (GFORM)

The remainder has no imaginary pole, is stable/proper with infinity limit1, and has the SAME nonnegative boundary real part as G away from the removed poles. By cancellation/continuity this holds there too; the minimum principle makes it positive real throughout the right half-plane.

Write

`W=s^5+w4 s^4+w3 s^3+w2 s^2+w1 s+c`.

W is monic and W(0)=c because B(0)=1=pc. No strict stability assumption on W or its strictly proper difference W/H-1 is made.

Clearing denominators gives the complete polynomial reconstruction

`B(s)=(s^2+p)W(s)+r s H(s)`. (BFORM)

Conversely choose H strictly Hurwitz, W/H weak positive real, r>0,p>0,c=1/p and a palindromic strictly Hurwitz BFORM. The lossless pole term r s/(s^2+p) has strictly positive real part inside, so GFORM and its reciprocal are positive real there. Thus a2/B is globally weak positive real and its ONLY imaginary source pair is at p, because H is strict. This proves both directions without a hidden common-factor restriction.

## 2. EVERY nonnegative positive-constant quintic has a complete positive-factor form

The boundary real numerator for W/H is the monic quintic

`K(t)=Re[W(i sqrt(t)) conjugate H(i sqrt(t))]`, K(0)=c^2>0.

Since H is strict, W/H is weak positive real IFF K(t)>=0 for EVERY t>=0.

**Factor coverage lemma.** ANY monic real quintic with positive constant which is nonnegative on the positive half-line has a factorization

`K(t)=(t+z^2)[(t-u)^2+lambda t][(t-v)^2+mu t]`,

`z,u,v>0`, `lambda,mu>=0`, `zuv=c`. (KFACT)

Proof: all positive real roots have even multiplicity, all nonreal roots come in conjugate pairs, and no root is0. Hence the number of negative real roots, with multiplicity, is ODD and nonzero. Select one negative root -z^2. Of the remaining four roots, pair each nonreal conjugate pair, each positive even-multiplicity pair, and the remaining even number of negative roots into pairs. Every resulting monic quadratic has positive constant and is nonnegative on the positive half-line. A quadratic with constant u^2>0 is uniquely (t-u)^2+lambda t once its coefficients are fixed; evaluating at t=u gives lambda>=0. Do this for both factors. The positive square root of the constant equality is zuv=c. Conversely all displayed factors are nonnegative for t>=0 and their constant is c^2. This proves coverage, including ALL extra positive double roots, coincidences, negative-root pairings and irreducible factors. No positivity sample or chosen complex branch is used.

The factorization need not be unique or a bijection. It is a complete existential real positive-factor representation with four free scalar parameters, for example z,u>0,lambda,mu>=0 and v=c/(zu)>0. A formal parameter count is not a nonempty physical-system argument.

For explicit coefficient extraction put A=lambda-2u,C=mu-2v. Then

`K4=A+C+z^2`,

`K3=u^2+v^2+AC+z^2(A+C)`,

`K2=A v^2+C u^2+z^2(u^2+v^2+AC)`,

`K1=u^2v^2+z^2(A v^2+C u^2)`.

Here K=t^5+K4 t^4+K3 t^3+K2 t^2+K1 t+c^2. The temporary coefficient letters A,C are not actual source corners or target component polynomials.

## 3. The stable-remainder numerator is uniquely reconstructed by FOUR LINEAR equations

The source components are

`E_H=c-h2 t+h4 t^2`, `O_H=h1-h3 t+t^2`,

and similarly for W with h replaced by w except the shared leading/constant coefficients. Multiplying E_W E_H+t O_W O_H gives EXACTLY

`K4=h4 w4-w3-h3`,

`K3=w1-h2 w4+h3 w3-h4 w2+h1`,

`K2=cw4+h2w2-h3w1-h1w3+ch4`,

`K1=h1w1-cw2-ch2`. (LIN)

These FOUR affine equations have a UNIQUE real solution(w4,w3,w2,w1) for EVERY real desired(K4,K3,K2,K1), at EVERY strictly Hurwitz H; there is no generic determinant caveat.

Proof of invertibility: a homogeneous solution gives a real polynomial Delta of degree at most4 and Delta(0)=0 with

`Re[Delta(iomega)/H(iomega)]=0 for EVERY real omega`.

Delta/H is strictly proper and stable, hence bounded on the right half-plane with zero infinity limit. The minimum principle applied to its real part and its negative gives zero real part inside. A holomorphic function with identically zero real part is an imaginary constant; real coefficients and/or the zero infinity limit make this constant0. Thus Delta=0. The real4-by-4 linear map is injective and therefore surjective. This proves the asserted inversion at the ENTIRE strict-H domain, including coefficient-rank cases that a guessed symbolic pivot might miss.

Consequently(KFACT)+(LIN) is a complete finite exact stable-remainder chart. No unproved degree-five source inequality, root-order scout or scientific calculation is hiding in that phrase. H's stated strict Hurwitz input remains mandatory; a monic degree-five H can equivalently be required to have all FIVE positive leading principal minors of its ordinary Hurwitz matrix.

## 4. Palindromic target reconstruction is THREE explicit affine equations

BFORM has coefficients

`B1=w4+r`,

`B2=w3+p+r h4`,

`B3=w2+p w4+r h3`,

`B4=w1+p w3+r h2`,

`B5=c+p w2+r h1`,

`B6=p w1+r c`.

Thus palindromicity is EXACTLY

`w4+r=pw1+rc`,

`w3+p+rh4=c+pw2+rh1`,

`w2+pw4+rh3=w1+pw3+rh2`. (PAL)

Target cubic coordinates are

`d=B1-1`, `e=B2-B1-2`, `f=B3-B1-B2+1`.

Retain d,e,f>0,de>f. Together with H strict, r>0 and the positive-factor chart, these give every pair(B,a2) on the stated one-source-pair face. No general affine-PAL rank or uniqueness claim is imposed; all solutions are retained.

## 5. ACTUAL widths, phase cell and full physical requirements

The actual C2 source coefficients are

`A1=h4`, `A2=h3+p`, `A3=h2+ph4`,

`A4=h1+ph3`, `A5=c+ph2`, `A6=ph1`.

Therefore the original positive paired widths are EXACTLY

`ph1-h4>0`,

`h3+p-c-ph2>0`,

`h2+ph4-h1-ph3>0`.

The full physical source-zero application also retains0<p<1 and E_B(p)<0,O_B(p)<0, i.e. the ACTUAL inner-C2 cell, not merely a generic positive frequency. C4 is the exact reversal and has its reflected source zero above1, as v26 requires.

ALL C1/C3 actual pal source/contact-shape/global-positivity/amplitude requirements are STILL required, as are the selected nonzero other contact, extra determinant contacts, full R nonnegativity, actual width conventions and the correct positive-dual conditions at strictly admitted physical points. A represented boundary pair alone does not establish any of those. The source at p is NOT strictly admitted, so one cannot call it a counterexample tuple or apply the nonzero-four-contact dual to it.

If a full physical nonpal admission failure exists, v26 guarantees exactly the factor structure used here, and the necessity proof supplies r,W,KFACT,LIN,PAL. Conversely any solution of this chart AND all remaining original guards is precisely a point on that remaining one-source-pair boundary. This is complete boundary coverage at the stated physical hypotheses, not a new omitted family left behind v25.

## 6. New representation versus results actually established

The physical joint-two-source-zero route is already excluded by v26. The remaining one-zero route is now represented with a GENERAL degree-five stable positive-real remainder and a complete nonnegative quintic factorization, with a globally invertible spectral linear map. It is not reduced to W=H, a single notch, a rational parameter restriction or an unjustified generic-rank condition.

The actual remaining work is to solve or exclude this full finite real boundary system together with all pal/width/contact guards, and separately the strict-source W_I/W_II_strict/W_III intersection and pal/width/target faces. No boundary point, full feasibility, strict perturbation, global attainment, global emptiness or unrestricted SPR7 theorem follows here.

All claims are WRITTEN, no formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty/parent acceptance. Later v21-v28 remain outside the pre-event v11-v20 manifest and old freezes until a fresh complete union gate. Same original18/HOLD/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38, actual-clock substantive cadence, no GO/early park/round closeout; primary active.
