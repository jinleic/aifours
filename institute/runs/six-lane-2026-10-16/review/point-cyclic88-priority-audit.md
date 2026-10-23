# Point-cyclic 2-(88,4,1): bounded priority audit (read-only scout Cyclic88Priority, 2026-10-17 PT)

Preserved verbatim. A search miss is not novelty.

## Summary

**Verdict.** I did not find an earlier statement that rules out $v=88$, and none of the theorems I read applies to it. Of the four steps in `PROOF.md`, only Step 1 (types T2 and T3 are excluded, so the resolution must be type T1) is known. Steps 2–4, which exclude T1, go beyond what the known theorems state.

- **T1 results in the literature only cover prime or prime-power $v/k$.**
  - Genma–Mishima–Jimbo 1997, Theorem 2.1, needs $v/k$ prime.
  - Mishima–Jimbo 1997 has a T1 lemma, which I know only as quoted in Lam–Miao–Mishima 2001. It needs $v/k=p^\alpha$ with $\gcd(p,k)=1$.
  - For 88, $v/k = 22 = 2\cdot 11$, which is neither. The same is true of $2p$ in your $8p$ family.
- **Your proof uses the same mechanism as Genma–Mishima–Jimbo, extended.** Their proof of Theorem 2.1, case (i), shows the non-short classes are fixed by translation by $k$. So no full block contains a difference that is a multiple of $k$, and those differences cannot be covered.
  - The new observation for $v/k=2p$: the divisor 2 is too small to be a class-stabilizer order. Since $|\mathrm{Stab}|\ge 4$, the only possible orders are $p$ and $2p$, and both subgroups contain $\langle 8\rangle$.
- **Calibration.** This is a new short proof of a case that a 13 Oct 2026 source explicitly calls open. It is a short extension of a classical argument, not an immediate corollary of any theorem I found. Its significance is a modest specialist result.
- **No flaw found in `PROOF.md`.** I re-checked every step by hand, including the $8p$ ($p\equiv 11 \bmod 12$) corollary. I ran no scripts.

## Theorem applicability table

| Source (version read) | Exact statement (quote ≤40 words) | Applies to 88? | Applies to $8p$, $p\equiv 11 \pmod{12}$? |
|---|---|---|---|
| GMJ 1997, Thm 2.1. Author-version preprint, PDF p.3 | "When v is a prime, if a cyclically resolvable cyclic (kv, k, 1)-BIB design exists, then v ≡ 1 (mod k(k − 1)) holds." Their $v$ is our $v/k$. | No: 22 is not prime | No: $2p$ is not prime |
| Same, proof of case (i) (T1), pp.3–4 | "Thus t = k must hold for all resolution classes except for R." … "no multiple of k is contained in ∆B. Thus we can not construct a cyclic BIB design…" | Same mechanism as PROOF.md Lemmas 5–6, but only for prime $v/k$ | Same |
| MJ 1997 T1 lemma, as quoted in LMM 2001 Lemma 2.1, preprint p.4 | "Let v = p^α for a prime number p and assume that p is relatively prime to k. Then there does not exist any CRCS(2,k,kv) of type (T1)." | No: 22 is not a prime power | No |
| MJ 2000, preprint p.13, recalling MJ 1997 | "Lemma 4.1 If there exists a CRCB(kuv, k, 1) of type (T3) such that its regular short block orbit is arranged in a v × u array, then uv ≡ 1 mod k − 1 and v ≡ 1 mod k hold." "Lemma 4.2 If a CRCB(kv, k, 1) of type (T2) exists, then v ≡ 1 mod k(k − 1) holds." | Yes: T2 fails since 22 ≢ 1 (mod 12). T3 fails since the orbit lengths from 22 = 2·11 are 11 ≡ 3 and 2 ≡ 2 (mod 4). So T1 is forced; this covers PROOF.md Corollary 4. | Yes, the same way: $2p \equiv 10 \pmod{12}$ and $p \equiv 3 \pmod 4$. For $p\equiv 5 \pmod{12}$, e.g. 40, T3 is not excluded, which is consistent with your restriction. |
| MJ 2000, p.13 | "we will focus our attension on only two types (T2) and (T3)" | Contains no T1 condition | — |
| Lam–Miao 1999 (zbMATH review only) | "…on 4p points is shown for p=12t+1 a prime and t odd." Constructive. | Does not address 88 | No |
| MJ 1997 (zbMATH review by Buratti) | "Some elementary conditions for the existence of a CRCB(v,k,1) of each type are given." Open T1 list for $k=3$: "v∈{81,99,105,117,135}" | Full text unread. The open list (no 75, no 147) fits a prime-power T1 condition [INFERENCE]. | Unknown |
| TZ 2026, p.2 | "…if a 2-(v,k,1) design possesses point-cyclic resolutions and v/k is a prime number, then v/k ≡ 1 (mod k(k − 1)) [5]." | No | No |
| TZ 2026, p.11 | "v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v, 4, 1) designs has not yet been determined." "…possible point-cyclic resolutions are of type T1." | This is the open statement | — |

Notes on the table:
- **Lemma labels.** TZ 2026 p.5 says Lemmas 4.1 and 4.2 cover T2 and T3 "respectively". In the MJ 2000 preprint, 4.1 is T3 and 4.2 is T2. The published version may number them differently.
- **Orbit lengths alone do not settle 88.** With class orbits of length 4 or 8, the count $4a+8b=28$ has solutions. The difference argument is what excludes 88.
- **TZ use the same idea for 57.** Their STS(57) paper (Mathematics 13:212, 2025), Lemma 1, uses the same "two points in one subgroup orbit" disjointness idea. That case has $v/k = 19$, prime, so it does not cover 88.

## Earlier equivalent: not located

- **Forward-citation checks (all empty):**
  - OpenAlex lists 0 works citing TZ 2026.
  - Crossref shows `is-referenced-by-count` 0 and no correction or update notice.
  - Both authors' ORCID records have the 13 Oct 2026 paper as their latest work.
- **EulerSolve listing (292 papers):** no Steiner-design or resolution items. The "Steiner" hits are Steiner trees and billiards.
- **openai/math** remote `CONTENTS.md` (719 manuscripts): no matches for Steiner, resolvable, point-cyclic or difference family. I did not find a local clone under `/Users/jinleic/repos`.
- **Access holes:**
  - **MJ 1997** (Congr. Numer. 123:193–203): full text not online. I only have the zbMATH review and the LMM 2001 quotation. LMM includes Mishima, so the quotation is probably faithful [INFERENCE], but MJ 1997 could state more.
  - **Lam–Miao 1999:** ScienceDirect returns 403 and the Elsevier API returns 400. No repository copy exists (OpenAlex `any_repository_has_fulltext:false`).
  - **GMJ 1997, MJ 2000, LMM 2001:** read only as Gifu author-version preprints, through Wayback `id_` captures. The published versions may differ.
  - **Not checked:** MathSciNet, Google Scholar citations, the Handbook of Combinatorial Designs, Meszka–Rosa 2007 (the $k=3$ prime-power analogue, which I saw only as quoted in DCC 89:2725), and Chang–Miao 2002.

## New short proof vs known corollary

| Part | Status |
|---|---|
| Lemma 2 (short blocks; no stabilizer of order 2) and the orbit-length bounds | Classical; GMJ 1997 §1 and §2 use them |
| Corollary 4 (only T1 possible) | Known: MJ 1997 conditions as restated in MJ 2000 Lemmas 4.1–4.2, and TZ 2026 p.11 says the same |
| Lemma 5 + Lemma 6 + §5 (T1 impossible for $v/k = 2\cdot 11$) | Not covered by any theorem I found. It is a GMJ-style difference argument plus the "divisor 2 is below the threshold" observation. |
| $8p$, $p\equiv 11 \pmod{12}$ family | No earlier statement found. Same delta as above. |

## Proof scrutiny

- **No semantic flaw.** The definitions match TZ Definition 5: an automorphism of the resolution permutes the parallel classes.
- The Remark that $h=4m$ is consistent with the "v × u array" structure in MJ 2000.
- **§6 crediting.** The "excluded: exactly …" list is relative to your criterion. I would add credit to MJ 1997 for both the T2/T3 exclusion and the prime-power T1 case.
- **A stronger criterion may exclude more.** Intersecting the stabilizers of all admissible classes, including mixed ones, might also exclude cases such as $v=1372=4\cdot7^3$ [INFERENCE, unchecked].

## Recommended wording (avoid "first")

> Topalova and Zhelezova (Axioms 15 (2026) 762, §7) state that $v=88$ is the smallest $v$ for which existence of a point-cyclic resolution of a 2-$(v,4,1)$ design had not been determined. We give a short, self-contained proof that no 2-(88,4,1) design has a point-cyclic resolution. Types T2 and T3 are excluded as in Mishima–Jimbo (Congr. Numer. 123 (1997); restated in Discrete Math. 211 (2000), Lemmas 4.1–4.2). Type T1 is excluded by extending the stabilizer/difference argument of Genma–Mishima–Jimbo (J. Combin. Des. 5 (1997), Thm 2.1) and the prime-power T1 lemma of Mishima–Jimbo (quoted in Lam–Miao–Mishima, J. Statist. Plann. Inference 95 (2001), Lemma 2.1) to $v/k=2p$. The same argument excludes $v=8p$ for primes $p\equiv 11 \pmod{12}$. We did not locate an earlier statement of these cases in the sources checked; Mishima–Jimbo (1997) and Lam–Miao (1999) were not available in full text.

## Files

- `information-science/evidence/six-lane-20261016/point-cyclic88/PROOF.md`: the proof reviewed above.
- `information-science/evidence/six-lane-20261016/point-cyclic88/sources/axioms-15-00762.pdf`: TZ 2026; quotes from pp.2, 5 and 11.
- `institute/runs/six-lane-2026-10-16/screening/info-2-point-cyclic88-contract.json`: the frozen contract.

Primary sources to save into `sources/`. The direct Gifu URLs redirect to octet-stream object storage; `curl -L` works on either form.
- GMJ 1997: http://web.archive.org/web/20240420184647id_/https://gifu-u.repo.nii.ac.jp/record/77124/files/a0801798.pdf (CDX digest Y7DGCGTN…, 142509 bytes)
- MJ 2000: http://web.archive.org/web/20251019161038id_/https://gifu-u.repo.nii.ac.jp/record/77160/files/a0801873.pdf (CDX digest QGZVTO6E…)
- LMM 2001: http://web.archive.org/web/20251019161049id_/https://gifu-u.repo.nii.ac.jp/record/77183/files/a0801799.pdf (CDX digest AM3DOHBY…)

Reviews: zbMATH 0918.05015 (MJ 1997), 0918.05013 (Lam–Miao 1999), 0949.05008 (MJ 2000).

I made no edits and wrote no files.
