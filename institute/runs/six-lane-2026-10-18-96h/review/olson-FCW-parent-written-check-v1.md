# Olson FCW — parent written check v1 (pre-verdict)

Recorded 2026-10-20T01:42:11-0700 (`/bin/date`). Parent re-derivation of proof-FCW-v1.md (c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf) at p=4kappa−1, kappa≥3, by hand. This is not a verdict and not independent review; both-family reviews (Codex bg_3033 running; Claude queued) and the parent verdict remain required.

**Checked, no gap found:**
- W: W_0=[2kappa+2,R], W_1=[2kappa,R], W_kappa=[2,R] (2p−2kappa=6kappa−2=R), W_(kappa+1)=[0,R−2]; no full window.
- IF*: (b) a zero-sum of Y is an even-length letter set with sum T(P0)=0, so (SR) at m=1 bounds it by 2kappa−2. (c) L=R−2t≥4kappa=p+1, SC0, odd a_i. (d) (S′) arithmetic at (k′,kappa′)=(p−1,kappa−1): 2p+2kappa′−k′=R, L≥2p−k′; consequences n−≤n+, n−≤t, s_j≤2kappa−3. (f) E≤2kappa−1+n−≤3kappa−2; m1≥(10kappa−3−5t)/2≥(5kappa+2)/2.
- Light side (n=2kappa+2∈W_0) and the P0/C0 exchange (Y→−Y, g→−g).
- D*: max element ≤m1+1 (s_j≤2kappa−3; a_max−1≤E−2(r−1)≤L−r since E≤3kappa−2≤L+r−2); interval covering; B*−R=E+n+−n−≥0.
- N: nu0≤q1+3E/2+n+; 2B*−nu0−2p≥4kappa−2+E/2+n+−2n−−q1≥2kappa−1+E/2.
- Z: |O1|≥m1≥(5kappa−1+b)/2≥b for a-labels b≤3kappa−1; s_j case; even |Z0|.
- U*: realised sets in all three sign cases with exact W_kappa/W_(kappa+1) membership; translation via nu(P)=nu0+sigma(P), Pi(P)=Pi0−sigma(P); p incongruent representatives force B*≤2p−2; unique representative in [Pi0,2p−nu0] (length 2p−B*<2p, p odd); case bounds (i)–(iii) and the m=kappa, letters(P)≠A− bound −1−nu0.
- A*: Delta≡0 mod 2p, 0<2Pi0+nu0−2p≤Delta<4p. C*: total sum and interval [2Pi0,4p−2nu0].
- F1–F5: interval counts (2kappa−1, 2kappa−2, kappa−1, kappa−2≥1 at kappa≥3); |d|≤2p−R=2kappa, 4kappa<2p; gap-normalisation moves; f0=0; (F4) pigeonhole gap≥3; (F5).
- Sec.5: three CLAIM cases; empty-run case gives nonzero even theta with |theta|≤2kappa<p; exception in at most one alternating set (disjoint letter sets); B*≤2p−1−2kappa=R−1<R.

**Import dependence (to be confirmed by the reviews):** (SR) via GRX/PL Sec.2 with the LOWER erratum m(P) definition; SC0; ZSTRUCT and FB in (S′) at t≥1; NF block/run form and empty-run rule; PL gamma-normalisation and SS bijection. FCW Sec.6 instances (3,11) and (5,19) are arithmetic specialisations of the general proof.
