# Fresh information-science screen — final scout addendum and parent source check

The scout's final message after the parent broadcast kept its ranking: gn(R⁻), five-participant perfect versus linear secret sharing, then n=mp static-output-feedback stabilizability. It ran no model delegate, search code or solver, and its report has no independent review.

## Scout additions

- **R⁻ graph data.** Read from Baber–Christofides–Dang–Riis–Vaughan Figure 1, <https://arxiv.org/html/1410.8349v2/RGraph.png>, and consistent with Gürpınar's automorphisms: 26 edges `12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10`; R adds `9-10`. Gate: replay Shannon 114/17, Ingleton 20/3, fractional clique cover 10/3 and gn(R)=27/4 before using this transcription.
- **Guessing-number publication and citation check.** The paper is also IEEE TIT 2016, DOI 10.1109/TIT.2016.2628819; OpenAlex reported no citing work since 2023 for the checked versions. This is absence of evidence only.
- **Conditional Ingleton source.** Boege, Exp. Math. 33 (2024), arXiv:2204.03971, quoted as giving "precisely ten inclusion-minimal sets of conditional independence assumptions on four discrete random variables which make the Ingleton inequality hold."
- **Exact small-alphabet windows, unreplayed.** Winning R⁻ codes would need 102–103 configurations for s=2 and 1517–1559 for s=3 under the stated bounds.
- **Secret-sharing blocker.** The full Khazaei ePrint 2026/1646 PDF was unavailable (reader abstract only, direct fetch 403, Wayback 404), so the structure numbering, open dual pair and Γ₃₀ perfect lower bound remain unchecked.
- **SOF leads.** Eremenko–Gabrielov's 2002 LAA counterexample paper and a 2025 J. Comput. Syst. Sci. Int. n=mp modal-control paper require scope checks.

## Parent primary-source check: Eremenko, October 3 2026

The parent opened <https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf> and confirmed:

- Exact question: "For which m and p the generic system with n = mp is stabilizable?"
- Current statement of known results: n<mp generic pole placement is solvable; for both m,p even there is an open set where some pole placement is unsolvable; for m=p=2 there is an open set of non-stabilizable systems; m=1 or p=1 pole placement is linear and generically possible.
- Anderson–Byrnes criterion as stated: for given m,p and n=mp, the generic system is stabilizable **iff** every non-degenerate V in Q(m,m+p) has a real L solving `det[V(z);L] = c z^(mp)`.
- Degeneracy: V is degenerate if some L makes the determinant identically zero. Q(m,m+p) consists of m×(m+p) polynomial matrices whose maximal minors have no common factor and maximal degree n.
- Published control: `V(z)=[[z^2,1,z,0],[z+1,z^2,1,z]]`, with equation for `z^4` having no real solutions.
- Eremenko: "I am aware of no regular procedure which would permit to find such examples. The question is for which m and p they exist."

## Parent assessment [INFERENCE]

For m,p not equal to one, one exactly certified non-degenerate V with no real fibre over `z^(mp)` would settle that individual (m,p) negatively. The smallest unresolved cases named by the scout are (2,4) and (3,3), with 14 and 42 complex Schubert solutions. Exhaustive or proved positive answers would require a universal theorem. This is the leading information-science replacement because it has a current author question, explicit criterion, published positive/negative control and finite exact certificate format. It is not frozen until the exact non-degeneracy definition, coordinate convention and existing literature, including Eremenko–Gabrielov 2002 counterexamples, are checked.
