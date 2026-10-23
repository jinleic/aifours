# PH three-pole candidate: parent primary comparison and attribution limits — 2026-10-18T01:48:41-07:00

**Status: priority comparison, not proof acceptance. No earlier all-parameter sharp-order theorem was located in the bounded screens, but substantial mechanisms and every upper-band boundary case are prior. Do not claim a new spectral-angle method or new boundary solution.**

## Sources actually read by the parent

### 1. Mocanu's 1999 thesis — access hole now closed for the relevant result

- Official HAL record: https://hal.science/tel-05023365v1 (thesis defended6September1999; deposited7April2025). Official PDF: https://hal.science/tel-05023365/document.
- Download succeeded through ordinary HTTPS with urllib after the read tool's binary conversion failed; no authentication, access-challenge bypass or alternate mirror. Local PDF SHA `1d08aee2137c7a803de8ab90b6d63f7009409786fde8d04f045f7d0b5e8efef5`,1,168,534bytes. [Download receipt](../screening/phase-type-complex3-priority-parent-v2/official-download-attempts-v1.json).
- Read scope: title/ToC/introduction; §2.2–2.3 on complex-pole blocks; §4.1.3, especially **Theorem50 and Lemma51**, printedpp80–82/PDF97–99. The three latter pages were also rendered and read visually, because the extracted formulas are damaged.
- **Theorem50:** a PH transform with one real pole and one complex pair, constant numerator, has a representation of order **n+1**, where n is the relative order of the complex pair. This is the exact n*+1 baseline for our family, rather than just a later paper's report about an unread thesis.
- **Lemma51:** an n-state feedback-Erlang cycle realizes the three-pole transform when the poles are λ(1−w) and λ(1−w·exp(±2πi/n)). Its normalized initial coefficients (Eq4.13) are

      α_j = [sin((j+1)π/n) sin((j+2)π/n) / (sin(π/n) sin(2π/n))] · w^j · α_0.

  The thesis proves positivity for0≤j≤n−3.
- **Parent algebraic comparison:** this family is precisely **every upper-band boundary** β=b/(a−c)=cot(π/n), not just β=1,n=4. Given c>0,δ=a−c>0 on this boundary, set R=δ/(1−cos(2π/n)), λ=c+R and w=R/λ∈(0,1). Then λ(1−w)=c, λ(1−w cos(2π/n))=a and λw sin(2π/n)=b.
- Our h_k coefficient equals a positive scale times

      sin((k+1)ψ/2) sin((k+2)ψ/2) / (sin(ψ/2) sin ψ).

  At ψ=2π/n this is the same published positivity kernel. Thus the boundary exit/initial-coefficient mechanism is also prior. The candidate's extra step is a suitable **off-boundary** cycle and coefficient-positivity/cancellation construction, if correct and not otherwise prior.

### 2. Verbeken–Ginis2026 — spectral-angle overlap verified

- https://arxiv.org/html/2606.10143v2, arXivv2 date14September2026, *On the Spectral Region of n-Cycle Stochastic Matrices*, Brecht Verbeken and Vincent Ginis; CC BY4.0. Full primary text captured with math alttext: [local text](../screening/phase-type-complex3-priority-parent-v2/verbeken-ginis-2606.10143v2.txt), SHA `7c97236b9a6b703361a5667b7ea133004be1ff2845305926686d1ad0a53cbd02`.
- Parent read abstract/introduction, §2 Lemmas2.1–2.2/Eqs2.2–2.8 and §8.2–8.3/Corollaries8.2–8.3. It classifies a **single-eigenvalue spectral union**, not all complete spectrum multisets.
- Eq2.4: "α(u)=a−b cot u"; Eq2.5: a logarithmic sine-ratio identity. It imposes a fixed sum of angles and a zero logarithmic-modulus sum.
- LF650 of the local extraction: "the reconstruction does not prescribe the rest of the spectrum."
- **Parent coordinate map:** for the candidate cycle M with positive Perron vector u, Q=diag(u)^−1(M−I)diag(u) is a unidirectional ring generator with rates r_i=1−m_i. Uniformize with q≥max r_i. Then A=I+Q/q, λ=1+(−1+iβ)/q and self-loop α_i=1−r_i/q. Their Eq2.4 yields α_i=Reλ−Imλ cot θ_i, exactly our m_i=−β cot θ_i after affine rescaling. With their M-angle=π−φ, Eq2.5 becomes the candidate's product sin(θ_i+φ)=sin(φ)^n.
- Thus our spectral placement step uses a published mechanism. The read sections do not provide nonnegative input/exit vectors realizing the specified constant-numerator transfer function. Merely embedding the poles does not resolve CM2003Conjecture1.

### 3. Kim2016 — relevant full-text access hole also closed

- Kyungsup Kim, *An Optimization Approach for Computing a Sparse Mono-Cyclic Positive Representation*, J.KSIAM20(3),225–242(2016), DOI https://doi.org/10.12941/jksiam.2016.20.225. Official PDF: https://koreascience.or.kr/article/JAKO201628663266949.pdf.
- PDF SHA `8c2c4ebc1058cbd97aaa3db1476967f6410a5e5c506fb6f9237eeeedd4ad1d3b`,1,174,053bytes. Parent read the complete technical text (all sections, references); mathematical extraction has some damaged displays, but the algorithmic caveats are clear.
- Eq3.2 gives the feedback-Coxian cycle; Lemma3.2 states spectrum independence under diagonal-rate reordering. Algorithms1–3 numerically choose an HFCB realization and check the transformed initial vector.
- Printedp236/LF218: "Most of the numerical methods ... meet a danger converging to a local minimal point or diverging, depending on initial values."
- PDF14–15/LF264: "To make the initial vector non-negative, additional states have to be added to the distribution similarly."
- This is relevant structural/algorithmic precedent, but the full text does not state an all-parameter n* realization of our three-pole family. It explicitly allows additional Erlang-tail states and numerical failure/local convergence, unlike the candidate's claimed universal exact order.

## Calibrated candidate delta

| Item | Prior status | Permitted description |
|---|---|---|
| Sector lower bound | Dmitriev–Dynkin/O'Cinneide; reproduced in CM2003Theorem6 | imported or re-derived classical result |
| Irreducible positive→PH normalization | CM2003Proposition1/Theorem4 | classical; the candidate gives direct arguments |
| n*=3 | Commault–Chemla1996/CM2003Theorem14 | known, also independently re-derived |
| Every β=cot(π/n) boundary | Mocanu1999Lemma51 | known; do not present as new |
| Cycle characteristic equation, angle/product mechanism | prior feedback-cycle literature and Verbeken–Ginis2026 | known spectral mechanism |
| General n*+1 realization | Mocanu1999Theorem50 | exact matched upper baseline |
| All off-boundary parameters at order n* | no equivalent theorem located in bounded sources | candidate conjecture resolution; priority remains uncertain |

**Significance if accepted:** a specialist solution of an explicitly stated2003conjecture for one constant-numerator three-pole family. It does not solve general PH minimal realization, arbitrary numerator families, or the book's full question. The degree is3 but the minimum PH order can be arbitrarily large, so this is not merely a finite-order sample extension.

## Remaining priority limits

The source screens' unread POSTA chapter body, O'Cinneide1999 body, some paywalled Kim papers, GoogleScholar/CNKI and possible equivalent software/theorems remain access/search gaps. The old screens' statements that Mocanu's thesis and Kim2016 were unread are now superseded at the exact read scopes above, not erased. No priority/"first" conclusion follows from a search miss.
