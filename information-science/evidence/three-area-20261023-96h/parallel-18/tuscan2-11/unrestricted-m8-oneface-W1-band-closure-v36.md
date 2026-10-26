# Actual Tuscan11 one8/ONE face — W1 closed without v19; one8/ONE face complete

Actual `/bin/date` before this body: **Mon Oct 26 01:15:49 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. W1 symmetry

W1 = A B C D A^- B^- C^- D^- (v20 §2, SHA256 `0a1249ba2d262010efaaba699e2beccb3e9b4142ade16e53ccf515cdd04c642f`). Rotating the face by one traversal and renaming B,C,D,A^- as A,B,C,D returns W1, so the word's symmetries act transitively on the four loops; take the short loop Lambda=A. Excesses beta, gamma, omega for B, C, D and p, q for A[0,t], A[t,L]; the excess sum is beta+gamma+omega+P=5 with P=p+q.

## 2. Cut location

- At the short copy: impossible by v20 §4 (all words).
- At an end of A (corners D^-|A, A|B, D|A^-, A^-|B^-): impossible by v30 (SHA256 `16159aa53d6db5bf3b08a64a534a81190da9f3680ee325be24e645c45a41bddc`, all words).
- Interior corners B|C, C|D, B^-|C^-, C^-|D^-: below.

## 3. Interior corners: band arithmetic

- Cut B|C. Face C, D, A[L,t], A[t,0], B^-, C^-, D^-, A[0,t], A[t,L], B: e_1..e_9 = gamma, gamma+omega, gamma+omega+q (=w), 5-beta, 5, 5+gamma, 5+gamma+omega, 5+gamma+omega+p (=u), 10-beta. Bands give 1<=beta<=4 and 1<=gamma+omega<=4, while D=10-u-w=beta-gamma-omega. So |D|<=3.
- Cut B^-|C^-. Face C^-, D^-, A[0,t], A[t,L], B, C, D, A[L,t], A[t,0], B^-: u=e_3=gamma+omega+p, w=e_8=5+gamma+omega+q, the same band ranges, and D=beta-gamma-omega. So |D|<=3.
- Cut C|D. Face D, A[L,t], A[t,0], B^-, C^-, D^-, A[0,t], A[t,L], B, C: e_1..e_9 = omega, omega+q (=w), 5-beta-gamma, 5-gamma, 5, 5+omega, 5+omega+p (=u), 10-beta-gamma, 10-gamma. Bands give 1<=omega<=4 and 1<=beta+gamma<=4, while D=beta+gamma-omega. So |D|<=3.
- Cut C^-|D^-. Face D^-, A[0,t], A[t,L], B, C, D, A[L,t], A[t,0], B^-, C^-: u=e_2=omega+p, w=e_7=5+omega+q, the same ranges, and D=beta+gamma-omega. So |D|<=3.

Each contradicts (T4) |D|>=4 (v21 §2, SHA256 `770ed4f5356e2ed1e0084f444c0dda1a33a6c79deaee2c4bb1b981fba02b8589`).

**Result.** W1 is impossible without using v19. With v20 (words; no short-copy cut), v21 (W2), v22, v23, v30, v32, v33, v34 (W3, W4), every one8/ONE-face system is excluded as a written candidate, independently of v19. Together with v12 (F5 impossible) and v13-v17 (F3; only v13 and part of v14 are parent-accepted), the whole one8 placement is closed at candidate level. The remaining m8 residual is that of v34 less v35 (same-centre 3+5 Type I with the short copy on C): same-centre 3+5 Type I with the short copy on A/B/D and the cut in O, and all Type II; 4+4 F2; distinct 3+5 connected or reverse-pair; and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
