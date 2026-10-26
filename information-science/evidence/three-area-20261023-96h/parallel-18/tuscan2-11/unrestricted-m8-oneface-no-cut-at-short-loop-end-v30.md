# Actual Tuscan11 one8/ONE face — the v-cut is never at an end of the short loop (all words)

Actual `/bin/date` before this body: **Mon Oct 26 00:21:25 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Statement

**Theorem.** In every one8/ONE-face system (words W1–W4 of v20), the unique v-cut is not at either physical end of the short loop Lambda.

With v20 §4 (the cut is not at the short copy) this leaves only branch corners whose two traversals both avoid Lambda's ends ("interior corners"). It supersedes, without editing, the corner-by-corner treatment of Lambda-incident corners in v21 §§6–7, v22 §4 and v29 (all consistent with it).

## 2. Imports

v20 (SHA256 `0a1249ba2d262010efaaba699e2beccb3e9b4142ade16e53ccf515cdd04c642f`) §3 band structure; v21 §2 (SHA256 `770ed4f5356e2ed1e0084f444c0dda1a33a6c79deaee2c4bb1b981fba02b8589`) (T4); v22 §2 (I) (SHA256 `1894d359e0ce0f94b6db42aee0fe678233868863ff1e627381860f7faf612949`) for the cases delta=5,6; v29 §2(a) (SHA256 `362cbc4ac20be4c9652a98682934c45e5d9038b805c959ea28e655555748e9b0`) that delta is a band value, hence in {4,5,6}. Two elementary facts of the split graph are used: its physical edges are the 55 edges of K_11, each exactly once; hence (F1) the ten vertices adjacent to a copy of v (eight at the branch, two at the short copy) carry ten distinct labels, all of O, and (F2) a set of r labels spans exactly r(r-1)/2 physical edges.

## 3. Proof

By global reversal of all rows (which preserves one8, one face and every word class, v20 §2) it suffices to treat the **direct case**: Lambda's traversal from the cut end starts the face. Measure y from that end; the short copy is at y=tau and Lambda has length L.

**Step 1 (structure for delta=4).** Rows 0 and 1 are y[0,10] and y[10,20] minus tau (gap 0 has length tau=10+e_1). The opposite traversal's short-copy row is y[4,14] (delta=4; delta=5,6 are excluded by v22 (I)). Subtracting these three Hamilton rows gives O = H' ⊔ K ⊔ {c10} with H'=labels y[1,3], K=labels y[4,9]=labels y[15,20], c10=label y_10, and labels(y[11,14] minus tau)=H'. If tau were 11 or 14, three consecutive H' labels in y[11,14] would add two H'-H' edges to the two of y[1,3], exceeding the three of (F2); so tau is 12 or 13. Lambda's forward traversal reaches its far end at band value e:=e_2, so L=20+e.

**Step 2 (the far-end row).** The opposite traversal starts at the far end y=L at some v-visit P_j and reaches the short copy at P_(j+1). Its short-copy row y[4,14] has TAIL(j)=y[tau+1,14], so e_(j+1)=14-tau; gap j has interior y[tau+1,L-1], and HEAD(j), TAIL(j) overlap in one vertex, giving (10-e_j)+(14-tau)=L-tau, i.e. **e_j=4-e**. Hence e<=3 and HEAD(j)=y[14,19+e]. Row j is then

`TAIL(j-1)  v  y[19+e],...,y[14]`,

so the last 4-e vertices z_1,...,z_(4-e) of the traversal Z preceding the opposite traversal (Z is not Lambda: Lambda's traversals are never consecutive, v20 §2) carry O minus labels y[14,19+e] = (H' minus label y_14) ∪ {c10} minus the labels of the tail y[21,19+e]; z_(4-e) is adjacent to the branch v. The tail labels lie in (H' minus label y_14) ∪ {c10} because HEAD(j) has distinct labels.

**Step 3 (exhaustion facts).** (U1) The three H'-H' edges are all in Lambda: y_1y_2, y_2y_3 and the unique H'-H' edge inside y[11,14] (tau in {12,13}); by (F2) no other two H' labels are adjacent. (U2) The v-neighbours y_1 (branch at y=0) and y_(tau-1), y_(tau+1) (short copy) lie in H'; by (F1) they carry the three H' labels, so no other vertex labelled from H' is adjacent to a copy of v.

**Step 4 (contradiction).** y_(L-1)=y_(19+e) is adjacent to the branch v.

- e=1: no tail; z_1,z_2,z_3 carry the two labels of H' minus label y_14 and c10. By (U2) z_3=c10, so z_1,z_2 are adjacent H' labels, contrary to (U1).
- e=2: the tail y_21=y_(L-1) is a v-neighbour, so by (U2) it is c10; then z_1,z_2 carry the two labels of H' minus label y_14, and z_2 is an H' label adjacent to v, contrary to (U2).
- e=3: y_22=y_(L-1) is a v-neighbour, hence c10; y_21 carries one label of H' minus label y_14; z_1 carries the other and is adjacent to v, contrary to (U2).

Every case is impossible, so delta=4 is impossible; delta=5,6 were already impossible. QED.

## 4. Exact remaining one8/ONE-face cases

Interior corners only. W2 is excluded (v21). W1's branch part rests on unreviewed v19. W3: only the interior cut D^-|A with Lambda=B remains (v22 §3, v23). W4: Lambda=A cuts C|D and C^-|D^-; Lambda=B cuts D^-|A, A^-|C, C|D, C^-|D^-; Lambda=C cuts D^-|A, A|B, B|A^- (v22 §5). Their opposite-window offsets are, by the band identities and the excess sum: W3 D^-|A (Lambda=B) d=alpha-gamma-2omega; W4 C|D (A) d=2omega+beta; C^-|D^- (A) d=-(beta+2gamma); D^-|A (B) d=alpha-gamma-omega; A^-|C (B) d=gamma+omega-alpha; C|D (B) d=omega-alpha-gamma; C^-|D^- (B) d=omega+alpha-gamma; D^-|A (C) d=2alpha+beta-omega; A|B (C) d=beta-omega; B|A^- (C) d=-(beta+omega); each must satisfy |d|>=4 by (T4). Every original length, cut, copy and label condition remains.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
