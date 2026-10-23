# Point-cyclic 2-(100,4,1): bounded priority audit

## Verdict and provenance

**NO-PRIOR-FOUND-IN-BOUNDED-SEARCH; NOVELTY-UNCLEAR.** The read-only scout `Pc100Priority` found no accessible source settling existence at v=100. This is not proof of priority or of an open status. In particular, **100 is not an explicitly named open case** in the latest source; keep the frozen contract's DERIVED-OPEN label.

The parent directly read the source definitions and its explicit 88-point open statement, and independently checked the 100-point certificate. The broader literature search below is the scout's evidence, not a claim of additional parent reading. Its full report is retained in `agent://Pc100Priority`; the prior [88 audit](point-cyclic88-priority-audit.md) records the author-preprint access routes and earlier scope.

## Sources read and applicability

| Source read by scout | Located statement | Consequence for 100=4·5² |
|---|---|---|
| [Topalova–Zhelezova, Axioms 15(10):762 (13 Oct 2026)](https://doi.org/10.3390/axioms15100762), pp.2,11 | Existence for v=4q where q is a product of primes 12s+1 with s odd; 88 is the smallest undetermined order | 5 is not 1 mod12. No occurrence of 100 in the source text; the 88 statement does not name 100 |
| Genma–Mishima–Jimbo 1997, Gifu author preprint, Theorems 2.1,2.2 and Remark | Prime quotient restriction; second theorem also assumes odd block size; finite-field construction is cyclic only when the relevant field is prime | Quotient25 is not prime; block size4 is not odd. GF(25) has additive group Z5², not Z25 |
| Mishima–Jimbo 2000, Gifu author preprint, pp.13–16 | Lemmas 4.1–4.2 are necessary T2/T3 conditions; Theorem4.3/Corollary4.4 require smaller cyclically resolvable designs | Conditions allow T2 at25, but the nontrivial25=5·5 recursive route needs a2-(20,4,1) design, impossible by the replication count |
| [Lam–Miao–Mishima 2001 author preprint](../../../../information-science/evidence/six-lane-20261016/point-cyclic100/sources/lmm2001-preprint-a0801799.pdf), Lemma2.1, p.4 | For quotient p^a with p coprime to k, no type-T1 CRCS(2,k,kp^a) | Excludes T1 at100, not existence of T2 |
| [zbMATH0918.05013](https://zbmath.org/?q=an:0918.05013), Lam–Miao1999 review | 4p for primes p=12t+1 with t odd; products of those primes | Does not cover25 |
| [zbMATH1007.05037](https://zbmath.org/?q=an:1007.05037), Fuji-Hara–Miao–Shinohara2002 review | (p,4,1)-CDDF for primes p≡13 mod24 | Does not cover25 |
| [zbMATH0991.05019](https://zbmath.org/?q=an:0991.05019), Lam–Miao2001 review | A difference family plus a perfect Mendelsohn difference family yields designs over C_k⊕G | The relevant cyclic25-point difference family is unavailable; full-text hypotheses not read |
| [zbMATH0881.05015](https://zbmath.org/?q=an:0881.05015), Kageyama–Miao1996 review | Specialization to k=3 and constructions of cyclic semiframes | Review gives no k=4 case; full body unavailable |
| [Huber, arXiv:1306.4664](https://arxiv.org/abs/1306.4664), proof of Theorem5; [Gruner–Huber, arXiv:1203.6566](https://arxiv.org/abs/1203.6566), Theorem4(7) | Product-of-primes family, primes≡13 mod24 | Same exclusion of25 |
| [Lu, arXiv:2509.06663](https://arxiv.org/abs/2509.06663), conclusion | General cyclic resolution questions remain far from settled | No specific100-point statement |
| Reid–Rosa, EJC DS18 (2010), p.3 | No cyclic S(2,4,v) for v=16,25,28 | Rules out a cyclic25-point difference-family ingredient, not the100-point object |

The scout also checked about60 forward citations across the core papers through zbMATH/OpenAlex/Semantic Scholar; Topalova's ORCID and Zhelezova's homepage; and exact-order web/arXiv searches. These located no100-point construction. Search coverage is bounded and metadata/reviews are not substitutes for unread bodies.

## Theorem checks and terminology

- The nontrivial split25=5·5 in the T2 recursion would require a2-(20,4,1) design. Its replication number would be19/3, not an integer. This is an obstruction to that **construction**, not to the100-point design.
- For the T3 recursion with u=5 and vw=5, the nontrivial choices either break coprimality or again require the impossible20-point ingredient. A trivial choice supplies no new existence theorem.
- The classical necessary T3 conditions permit the5×5 possibility at100. The new lane reduction's stronger T3 exclusion is a separate mathematical claim under hostile review; the audit does not establish it.
- A construction on Z4×Z5² is not a point-cyclic construction on Z100: the additive groups are not isomorphic.
- Literature using “cyclically resolvable” for1-rotational designs is not the same convention as the source's point-cyclic resolution. A2-chromatic S(2,4,100) is also a different property.

## Access holes

- Lam–Miao1999 full text: publisher CAPTCHA/403; Elsevier API400; no accessible repository copy. Its review describes ad-hoc computer constructions, so unlisted examples remain a priority risk.
- Mishima–Jimbo1997 and Kageyama–Miao1996 full bodies were not available online. A suitable cyclic semiframe of type4^25 could already yield the100-point design.
- Blocked/paywalled bodies include Lam–Miao DCC2001, Fuji-Hara–Miao–Shinohara2002, Buratti–Pasotti2009, Fuji-Hara–Miao–Mishima2004, Ge–Miao–Yao2009 and Buratti2002.
- The Handbook of Combinatorial Designs, second edition, was not read; Google Books API429. MathSciNet, Google Scholar and ResearchGate were not reachable.
- GMJ/MJ/LMM were read as author preprints; their published bodies may differ.

## Calibrated significance

[INFERENCE] The certificate supplies one finite table entry outside every existence family whose hypotheses the scout could check. It is a modest specialist construction, not a new general mechanism or a proven priority claim. Do not call100 the next open order as a theorem, and do not count it as satisfying the contract's explicitly-named-open-target clause without additional source evidence.
