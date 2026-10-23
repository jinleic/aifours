## DISPOSITION: ACCEPT-WITH-FIXES

**0 FATAL · 0 MAJOR · 7 MINOR.** The findings are citations, undischarged automatic hypotheses, wording and scope. No mathematical repair is needed: every step I re-derived holds. This is advisory only; I have no gate or parent-acceptance authority. I did not check paths or hashes and ran no computation.

Abbreviations: `00` K0star-r2, `01` RED-r2, `02` PAR-K0, `03` Kplus-r2 (excerpt), `04` KBH, `10` v4 (excerpt), `11` runs verdict.

### Findings (all MINOR)

1. **`01:60`: KB\* cites the RGR-only certificate.** It says "Lemma BC (no boost)", but BC is stated for RGR words (`02:57`).
   - Repair: cite BC' (`00:119-139`). Conditions (a)–(c) proved with λ imply them with λ' ≥ λ (`00:118`).

2. **`01:105-107`: TII does not discharge KB's (V) or OR's o_F ≥ 1.** KB lists (V) as a hypothesis (`03:239`) and OR needs o_F ≥ 1 (`10:88`). The "by (V)" at `01:107` has no source.
   - Both hold for every avoider (`00:68-72`, `10:79-80`).
   - Repair: add one clause. This also explicitly closes the degenerate exits where w_end has k = 1 (C1 from k(w′)=2, or C2 from k(w′)=3). There o_F ≤ κ, so (V) fails and w_end cannot avoid.

3. **`01:32-35`: (I3), branch k ≤ p, does not discharge K0's (P) and (V)** (`02:94-96`).
   - Both are automatic for avoiders (`00:70-75`).
   - The only use (`01:155-156`) has an even reflection block, so K0's (P) step (`02:103`) is idle anyway (cf. `10:178-179`).
   - Repair: say so in the import text.

4. **`01:27-31`: (I2) is a composition of lemma-level imports, not a statement listed in `11:9-14`.** (`11:61` mentions a v4 "non-inherited B=0 remark" that is not in the excerpt.)
   - For k̃ = o_F ≤ p, the accepted route in v4 C1 is S1′/A1′/trivial cut (`10:169-173`).
   - 01 cites only C0-B′/A1. Their "ANY RGR word" scope rests on `10:132`; proof-RUNS L318-320 and L348-350 are not in the packet, so I could not audit them.
   - Repair: cite that remark, or transcribe the C1 composition with the o_F split plus Fact Z(iii) for OR. The consequence (an RGR avoider with B = 0 has κ = 0) stands on either route.

5. **`01:146-147`: P4's κ bookkeeping is overstated.** Fusion lowers κ "by one more" only if both fused blocks are odd.
   - Not load-bearing: the lexicographic step needs only the representation-level H+1.

6. **`01:20-21`, `01:38` vs `01:202-203`: stale r1 citations.**
   - The fix map says the imports now cite r2, but three places still cite proof-K0star-r1.md.
   - "(its 'Specialisations' paragraph)" has no counterpart in `00:38-76`. If it means GRX's notes, say so.
   - The GRX/PM\* acceptance claims (`01:17-22`) cannot be checked from the packet. They are irrelevant here because 00's lemmas are given.

7. **`01:134-135`, `01:164`: REFL(p) is not defined anywhere in the packet.**
   - I audited against the reading at `00:156-159` / `10:29-31`: every avoider of length 4p−2 whose rotation letters lie in one set {ρ_x, ρ_−x} has constant maximal cyclic reflection runs.
   - If the frozen README adds hypotheses (for example inherited conditions), the "trivial" converse must check them on RES_< words.
   - Repair: quote the definition in 01.

Non-load-bearing nits in Sec. 6:
- `01:168`: "2 ≤ κ" needs K0\* and K1\*, not only Z0/P0/V/SING.
- `01:179`: for K1\* it should read "κ−B = 1, B = 0".
- `01:180-184` (F2) cites Kplus-r2 L181 and L192-193, which are not in the excerpt; unaudited.

### Per-theorem verdict

| Item | Verdict | Key checks |
|---|---|---|
| SING `01:42-50` | correct | λ({t}) = B−κ+1−β_t ≤ 1 ≤ ⌊B/2⌋+1. L_t = p when A = 2p−1. The count max(0,q−1) is right since 0 ≤ q ≤ p. The hypothesis κ+β_t ≤ p is in fact automatic: each even neighbour adds ≥1 to H. |
| KB\* `01:59-71` | correct (fix 1) | (a) equals p+(k+D_N)/2 ≥ p+½. (b) lower: s = 0..3 and the capped case. (b) upper: s = 0..3, one or two capped, x<0<y. (c): all three d_j ranges. d_j ≤ 2p−2 is used only in (a). |
| CAP `01:72-75` | correct, no D0 | The equality chain forces a_i = 0 (i≠j), b_j = 0, B = k−1, A = 2p−1. SING then gives q = 0, with κ = k−1 ≤ p−1. |
| KBH\* `01:76-85` | correct | Only (2b) uses D ≥ 1 (`04:102`). If D = 0 then A = B ≥ P_Q, so no tight interval exists (not even r = 1) and θ ≡ 0. Step 0's bounds o ≤ 2p−1 and D ≤ p−1 are unused. ZS properness is unaffected by empty runs or all-empty segments. |
| Cor. B=K `01:86-87` | correct | Exhaustive: κ = 0; k ≤ p capped or uncapped; k ≥ p+1. |
| K1\* `01:91-98` | correct | g ≤ e_R ≤ 2 gives k ≤ p+2 and p ≤ R ≤ 2p−1. (a) equals p+1+e_R/2. (b) upper ≥ R+1 = 2p−k+3. |
| TII `01:102-108` | correct (fix 2) | Imports are applied only to RGR words, and KB only for its D0-free uncapped conclusion. TII describes type-(II) avoiders (which exist non-inherited, `04:111-113`) and never claims to exclude them. |
| QQ `01:109-126` | correct | Window equality holds; the shift +1 follows from v = u+2. Both a′ ranges work, and all six (l1,l2) cases are bounded (l1 = p is impossible for a′ ≤ p−1). Cross-check: Q′∖{t} in w′ itself has m=1, β=1 and the same D, so it gives the second residue directly. The recolouring is valid but dispensable. The aid at `01:127-128` is not needed. |
| Theorem RED `01:134-164` | correct, conditional | Conditional on (I1)–(I4) and the 00-r2 lemmas. |
| Remark F3 `01:185-192` | correct, non-load-bearing | Not cited in Secs 1–5. Branch A = 2p−1: I°(∅) contains −p. Branch A ≤ 2p−2: windows grow only at patterns P with D_P+B odd and the floor term strictly minimal. |

### Q1: new lemmas and extensions to empty runs

- **No import by renaming.**
  - KB\* and KBH\* are re-derived for empty runs. An empty run has d = 0 and f(0) = 1, which matches SING's λ({t}) when B = κ, β = 0.
  - CAP, K1\* and QQ are new arguments.
  - P4 is re-derived from H0; M0's own scope (r_t ≥ 3, `10:94`) excludes (1,1)-runs.
  - OR and (I1)–(I4) are applied only to words with g = 0.
- **Capped case without D0.** CAP handles G-words; TII handles RGR words but only extracts structure. KB's D0-dependent capped proof is never entered.
- **Uses of 00's lemmas stay inside their hypotheses.**
  - FUS: both QQ orientations match the corrected statement.
  - PM0: k ≥ 2, and both neighbouring runs nonempty.
  - TR: a_s, b_s ≥ 1.
  - BC': any avoider.
  - K0\*: length and rotation set.
  - AR: the R = 0 case.
  - CH is not used.
- **Uses of the imports against their cited lines.**
  - (I1) at `01:150` and `01:154` matches `10:160-164`.
  - (I2), (I3) and (I4) are correct up to findings 4, 3 and 2 respectively.

### Q2: the four-move process

- **Avoidance.** P1: SPEC+FUS. P2: PM0. P3: TR. P4: all H0 windows weakly shrink, since κ−B, D_P, m, β and u_P are fixed while B drops.

- **Parameter changes.**

  | Move | A, B | H | κ | g | k |
  |---|---|---|---|---|---|
  | P1 | unchanged | +1 only for odd–odd double fusion | −1 only then | −1 or −2 | −1 or −2 |
  | P2 | unchanged | unchanged | unchanged | unchanged | −1 |
  | P3 | unchanged | unchanged | unchanged | −1 | unchanged |
  | P4 | each −1 | +1 (+1 more if odd–odd fusion) | −1 or −2 | +1 with k unchanged, or unchanged with k −1 (fusion) | see g |

- **Genuineness.** Surviving empty runs keep distinct neighbour values under every move.

- **Termination.** The triple (κ, g, k) strictly decreases lexicographically. While g ≥ 1, κ ≥ 1 (else K0\* gives a contradiction) and R ≥ 1 (else Lemma AR).

- **Exits with g = 0.** These occur only through P1 or P3.
  - P3: (I1) gives B = κ, and TII's purity contradicts the (1,1)-run.
  - P1, setup: (I1)/(I2) give B = κ(w_end). If κ(w_end) = 0, the exit must be C2 with a, c odd, producing an even block with κ = 0, contradicting (I3).
  - P1 with κ(w_end) ≥ 1: TII gives A = 2p−1. Then:
    - C2, a and c odd: q = 2 at both runs, but u_t+u_{t+1} = 0 ≠ −2.
    - C2, exactly one of a, c odd: q = 1 at one run.
    - C2, both even: q = 2 at both runs.
    - C1, β = 1: q = 1.
    - C1, β = 2: Lemma QQ.
  - C2 forces k(w′) ≥ 3 because R ≥ 1. The k = 1 outcomes are covered by finding 2.

- **Terminal state.** No P1/P2 means no even block; no P3/P4 means every run is pure or empty. B = κ is excluded by Corollary B=K; κ = 1 forces B = 0, excluded by K1\*. The terminal state is therefore exactly an avoider in RES_< with κ ≥ 2.

- **No cases are lost.**

### Q3: converse and equivalence

- The converse is immediate under the K0\* reading of REFL(p): a genuine empty run is a non-constant maximal reflection run.
- REFL(p) ⇒ REFL-RES(p) is unconditional. The reverse needs (I1)–(I4) and 00-r2.
- The "κ ≥ 2" qualifier is immaterial, since K0\* and K1\* exclude κ ≤ 1 avoiders in RES_<.
- So REFL(p) ⇔ REFL-RES(p) exactly, conditionally.

### Q4: assumptions, circularity, finite premises, scope

- **Circularity:** none. K0\* and (I1)–(I4) do not use RED, REFL or INV\*.
- **Finite premises:** none. `01:127-128` and `01:171-175` are labelled aids, and I verified the QQ bound by hand.
- **Scope:** `01:7`, `01:13` and `01:176-193` are accurate, apart from finding 7.
- **F3:** correct, and genuinely non-load-bearing.

### Fully audited vs taken as given

- **Fully audited:**
  - 01 Secs 1–5, line by line.
  - 01 Sec. 6 relations, F1 and F3.
  - KBH\* against `04:39-108`.
  - TII against `03:24-35` and `03:238-273`.
  - Import uses against `02:94-143` and `10:127-133, 160-181`.
- **Taken as given:**
  - The 00-r2 lemmas and facts: H0, GR0, SPEC, FUS, SL, TR, PM0, BC', CH, K0\*, Z0/Pairs/V/P0/Par, AR.
  - (I1)–(I4) at their stated scopes.
  - Theorem P, Davenport-alpha, EGZ.
- **Not available, so not audited:**
  - proof-RUNS.md (C0-B′, A1, M0).
  - Kplus-r2's S1′/A1′ and lines 181/192-193.
  - The frozen README.
  - The GRX/PM\* verdict.
  - All finite aids.

### Unresolved core

REFL-RES(p) (`01:193`), "no avoider in RES_<(p) with κ ≥ 2", is open for every p. p = 5 and part of p = 7 rest on finite aids only, and the p = 7 part used unreviewed code. Therefore REFL(p) remains open, the rotation half of INV\*(p) is untouched, and nothing here establishes INV\*(p) or ordered Olson for D_2p.
