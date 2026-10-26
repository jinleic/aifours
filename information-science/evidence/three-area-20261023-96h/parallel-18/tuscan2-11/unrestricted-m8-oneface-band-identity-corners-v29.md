# Actual Tuscan11 one8/ONE face — eight Lambda-incident corners closed by exact band identities

Actual `/bin/date` before this body: **Mon Oct 26 00:12:27 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps this ladder at m<=36; it cannot settle Tuscan-2(11) by itself).

## 1. Imports and notation

v20 (SHA256 `0a1249ba2d262010efaaba699e2beccb3e9b4142ade16e53ccf515cdd04c642f`): one8/ONE face, words W1–W4, branch v-cut, band values e_m in 1..9 with e_0=0, e_10=10, gap m of length 10+e_(m+1)-e_m. v21 §2 (SHA256 `770ed4f5356e2ed1e0084f444c0dda1a33a6c79deaee2c4bb1b981fba02b8589`): (T4) opposed whole windows on the short loop Lambda cannot start 0,1,2,3 apart. v22 §2 (I) (SHA256 `1894d359e0ce0f94b6db42aee0fe678233868863ff1e627381860f7faf612949`): at a Lambda-incident cut, with y measured from the cut end, rows through that end give windows y[0,10], y[10,20]; the opposite traversal has one whole window y[delta,delta+10]; O=H' ⊔ K ⊔ {c10} with K=labels y[delta,9]=labels y[delta+11,20]; and the 10-delta vertices of the neighbouring traversal at the opposite traversal's cut-end corner carry (K minus y_delta) plus c10. Each of the three ordinary loops has length 10+x (x among alpha,beta,gamma,omega); Lambda has parts of lengths 10+p and 10+q. Every loop is traversed twice and the ten gap excesses sum to 10, so **the three ordinary excesses plus p+q sum to 5**.

## 2. Two general facts

**(a) delta is a band value.** If the opposite traversal occupies gaps j, j+1 (short copy at P_(j+1)), then delta=e_(j+2) when Lambda's traversal from the cut end starts the face (direct case) and delta=10-e_j when it ends the face (mirror case). Hence delta lies in 1..9, and (T4) against y[0,10] and y[10,20] gives delta in {4,5,6}.

**(b) delta=6 is impossible.** Then |K|=4 and K4(K) is exhausted by the disjoint paths y[6,9] and y[17,20]; the neighbouring traversal's four consecutive vertices at the opposite corner carry three K labels, two of them adjacent, repeating a physical edge. (This is the delta6 clause of v22 (I), valid in the direct and mirror cases.)

So any identity forcing **delta>=6** closes the corner.

## 3. The eight corners

Each line gives the gaps from the cut with their excesses, the formula for delta and the forcing identity (all band values lie in 1..9).

1. **W3, Lambda=A, cut A|B** (mirror). Gaps B(beta), A[L,t](q), A[t,0](p), C(gamma), B^-(beta), D(omega), C^-(gamma), D^-(omega), A[0,t](p), A[t,L](q). delta=10-e_1=10-beta and e_6=2beta+p+q+gamma+omega=beta+5=15-delta. So e_6<=9 forces delta>=6.
2. **W4, Lambda=A, cut A|B** (mirror). Gaps B, A[L,t], A[t,0], C, D, B^-, C^-, D^-, A[0,t], A[t,L]. delta=10-beta, e_6=beta+5=15-delta. delta>=6.
3. **W4, Lambda=A, cut B|A^-** (direct, y=L-x). Gaps A[L,t](q), A[t,0](p), C(gamma), D(omega), B^-(beta), C^-, D^-, A[0,t](p), A[t,L](q), B(beta). delta=e_9=10-beta and e_4=p+q+gamma+omega=5-beta=delta-5. e_4>=1 forces delta>=6.
4. **W4, Lambda=B, cut A|B** (direct, y=x). Gaps B[0,t](p), B[t,L](q), A^-(alpha), C(gamma), D(omega), B[L,t](q), B[t,0](p), C^-, D^-, A. delta=e_7=p+q+5=e_2+5>=6.
5. **W4, Lambda=B, cut B|A^-** (mirror, y=L-x). Gaps A^-(alpha), C(gamma), D(omega), B[L,t](q), B[t,0](p), C^-, D^-, A, B[0,t](p), B[t,L](q). delta=10-e_3=10-(alpha+gamma+omega)=5+p+q=5+(10-e_8)>=6.
6. **W4, Lambda=B, cut D|B^-** (direct, y=L-x). Gaps B[L,t](q), B[t,0](p), C^-(gamma), D^-(omega), A(alpha), B[0,t](p), B[t,L](q), A^-, C, D. delta=e_7=5+p+q=5+e_2>=6.
7. **W4, Lambda=B, cut B^-|C^-** (mirror, y=x). Gaps C^-(gamma), D^-(omega), A(alpha), B[0,t](p), B[t,L](q), A^-, C, D, B[L,t](q), B[t,0](p). delta=10-e_3=5+p+q=5+(10-e_8)>=6.
8. **W4, Lambda=C, cut C|D** (mirror, y=L-x). Gaps D(omega), B^-(beta), C[L,t](q), C[t,0](p), D^-(omega), A(alpha), B(beta), A^-(alpha), C[0,t](p), C[t,L](q). delta=10-e_2=10-omega-beta and e_7=(omega+beta)+5=15-delta. delta>=6.

In every case delta=6 by §2(a) and is excluded by §2(b). **These eight branch corners are impossible.**

## 4. Exact remaining one8/ONE-face cases

Combining v20–v23 and this packet: W2 is excluded (v21); W1's branch part rests on unreviewed v19. Still OPEN: W3 with Lambda=A at cuts D^-|A and B|A^-, with Lambda=B at cuts A|B, B|A^-, B^-|D (band-consistent with delta=4) and the interior cut D^-|A; W4 with Lambda=A at D^-|A and A^-|C, with Lambda=C at A^-|C and C^-|D^- (band-consistent with delta=4), and the nine interior corners of v22 §5. Every original length, cut, copy and label condition remains in these cases.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use the distance-2 condition, v24 §7). Neither is supplied. All cadence (including the new 39:33 lapse recorded in checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
