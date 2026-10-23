# Covering-sequence L(12,3): bounded priority audit

Recorded 2026-10-17 07:32:17 PDT. Read-only scout `Cover12Priority`; a search miss is not novelty. Raw scout report follows.

---

**Summary.** I found no statement anywhere that gives an exact value for L(12,3). The best published bounds are **34 ≤ L(12,3) ≤ 36**.

- **Lower bound 34:** it comes from Chung–Cooper's 2003/2004 table. Their exhaustive search is the only source for it that I could find [INFERENCE: by elimination, see (a)].
- **Upper bound 36:** it comes from Rosin's CPro1 preprint (arXiv:2505.23881v1, 29 May 2025) and its GitHub result file. Neither makes any claim that 36 is optimal.
- **Table I has not been updated:** Table I in Chee–Etzion–Ta–Vu (v1, v2, and the Designs, Codes and Cryptography version) still lists 34–40 for (12,3). The journal version cites Rosin only in general terms.

## (a) Table I cell for (12,3) and where its lower bound comes from

**Definition**, arXiv:2502.08424v2 (15 Jul 2025), p1: "An (n,R)-covering sequence (an (n,R)-CS for short) is a cyclic sequence whose consecutive n-tuples form an (n,R)-covering code… To find the shortest (n,R)-CS, denoted by L(n,R)…"

**The cell itself:**
- Table I is on p11: `12 | 342-597^a | 62-161^a | 34-40^b`. I read the superscripts from the v2 HTML at https://arxiv.org/html/2502.08424v2.
- The same row appears in v1 and in the journal Table 1 (https://link.springer.com/article/10.1007/s10623-025-01726-5/tables/1; DCC 93(12):5445–5471, online 25 Sep 2025, open access).
- The caption says "b-Chung and Cooper [10]". So the anchor you gave is right, and the cell is attributed to Chung–Cooper.

**How Chee et al. describe their lower bounds:**
- v2 p10: "the lower bounds are either by computer search for very small n or the known lower bound on the smallest size of an (n,R)-covering code."
- v2 p14: "We would like to see improvements in these lower bounds and not just by one or two (something which is not difficult to do)."
- v2 p14 also says: "Rosin [44]… found… some better covering sequences. The sequences themselves are not yet well documented…" The journal version drops that last sentence.

**Chung–Cooper**, "De Bruijn cycles for covering codes" (arXiv math/0310385v2, 28 Oct 2003; Random Structures & Algorithms 25(4):421–431, 2004, DOI 10.1002/rsa.20033):
- Their Table 1, p16, row R=3 for n=8…13 reads `6 | 12 | 16 | 20 | 34-40 | 34-119`.
- pp15: "A single number in an entry indicates that the exact value… is known… software that searched the string space randomly (for upper bounds), and one which searched it exhaustively (for lower bounds). A few hundred hours of computing time on a 1.8 GHz Intel-based PC…"
- No code, certificate or details of the search are published.

[INFERENCE] The 34 must come from that exhaustive search, because nothing else can produce it:
- Kéri's covering-code table (https://old.sztaki.hu/~keri/codes/2_tables.pdf) gives K(12,3) in the range 18–28. Since K(12,3) ≤ 28, no covering-code bound can give 34.
- Chung–Cooper's simple observations only give L ≥ L(11,3) = 20 and rule out lengths ≤ 17.
- I did not read the Wiley journal text; its abstract matches the arXiv version.

## (b) Statements of an exact value for (12,3)

**Not found.**

**CPro1** (Rosin) treats (12,3) only as an existence result:
- arXiv:2505.23881 has only v1. Its Table 1(b), "Open instances… solved and found to exist by CPro1", lists `(12,3,36)` and says "constructed a verified solution". It makes no optimality or lower-bound claim.
- In the repo, `designs/covering-sequence/README.md` gives only parameters and how to reproduce the runs. `result-12-3-36-seed1000.txt` contains the 36-bit sequence.
- `problem_def.py` uses `[12,3,40]` as a development instance and `[12,3,39]` as the open target.
- The covering-sequence results were last changed on 2025-06-02.
- The site constructive.codes has nothing specific about (12,3).

**Sources checked (all fail to give an exact value):**
- **Chee et al.:** arXiv:2502.08424 v1 and v2 (PDF and HTML) and the journal article with its Table 1.
- **Chung–Cooper:** the preprint (people.math.sc.edu/cooper/debruijn.pdf) and arXiv v2.
- **Later papers:**
  - Etzion, arXiv:2607.14840v2 (21 Jul 2026). It only says "Using heuristic search, some bounds for small n and R were found by [26]", where [26] is Rosin. It has no tables.
  - Ta–Vu, arXiv:2606.29236v1, also published as DCC 94:202. It is asymptotic only.
  - The 2024 ISIT version of Chee et al., arXiv:2404.13674v2. Its table covers R=1,2 only.
  - arXiv:2410.15428v2 cites Chee et al. only in its references.
- **arXiv API:** `all:"covering sequences"`, `all:"covering sequence"`, `all:"de Bruijn covering"`, and `abs:"cyclic sequence" AND abs:"covering radius"`. The older hits are unrelated.
- **OpenAlex citers** of Chee arXiv (0), DCC 2025 (2), Chung–Cooper (7) and ISIT 2024 (2). Coverage is incomplete [INFERENCE].
- **Crossref** title search from 2025 onward.
- **OEIS:** "de Bruijn covering", "covering sequence", "Chung Cooper covering", and the value strings `2,6,8,12,22,32`, `2,2,2,2,6,12,16,20`, `2,8,10,14,20,38`, `6,12,16,20`. Nothing relevant came back.
- **About 10 web searches,** for example `"(12,3)-CS"` and `"covering sequence" "(12,3)" length 36`.

**Blocked:** I did not try to get around any of these.
- Google Scholar returned HTTP 403.
- The Semantic Scholar URLs failed in the tool.
- OpenReview (the NeurIPS 2025 MATH-AI workshop paper) and DBLP showed bot checks.
- The Ta–Vu journal article and the Wiley text of Chung–Cooper are paywalled.

## (c) Bounds published after Table I for nearby (n,R)

Only upper bounds have improved, all from CPro1 (May 2025). Table I value → CPro1 value:

| Radius | Improvements |
|---|---|
| R = 3 | (12,3) 40→36; (13,3) 93→61; (14,3) 239→122; (15,3) 406→230; (16,3) 1036→426 |
| R = 2 | (11,2) 111→64; (12,2) 161→127; (13,2) 292→276 |
| R = 1 | (9,1) 93→71; (10,1) 175→138; (11,1) 283→224 |

- I found no new lower bounds or exact values in any of the sources checked.
- [INFERENCE] If L(12,3) = 36, then Theorem 3 (L(n,R) ≤ L(n+1,R)) raises the (13,3) lower bound from 34 to 36.

## (d) Calibration cells

| (n,R) | Chee Table I (v2 and journal) | Chung–Cooper Table 1 (p16) |
|---|---|---|
| (9,3) | `12^b` | `12` |
| (10,3) | `16^b` | `16` |
| (11,3) | `20^b` | `20` |
| (9,2) | `20^b` | `20` |
| (10,2) | `38^b` | `38` |
| (8,2) | outside the table (n ≥ 9); Appendix A only lists "An (8,2)-CS sequence of length 14 - [00111011010010]" | `14` |

Under Chung–Cooper's convention, a single number means the exact value is known.

## Caveats for your claim

1. **Lengths 25–33 depend on Chung–Cooper's 2003 search unless your own search covers them.** [INFERENCE]
   - Chee's Lemma 19 (Chung–Cooper observation 8) says a sequence of length k gives one of every length ≥ k+11.
   - So finding no sequence of length 34 or 35 rules out only k ≤ 24.
   - Length existence is not monotone. Chung–Cooper: "it is possible for one to exist of length M but for none to exist of length M+1."
2. **CPro1's verifier never checks the all-ones word.** Its loop is `for x in range(0,(2**n)-1)`. By hand (not tool-run), positions 15–26 of the 36-bit sequence read `110111110101`, which has weight 9. That is distance 3 from 1¹², so this instance is fine. Your own validation should still test all 4096 words.
3. **The paper's authors consider small lower-bound gains easy.** Their own remark ("not just by one or two (something which is not difficult to do)") is useful for judging how significant a 34→36 improvement is.
