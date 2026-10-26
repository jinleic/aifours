# Actual Tuscan11 one8/ONE face — interior cuts: the window offset is 4, 5 or 6

Actual `/bin/date` before this body: **Mon Oct 26 00:27:10 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting and imports

After v20 §4 and v30 (SHA256 `16159aa53d6db5bf3b08a64a534a81190da9f3680ee325be24e645c45a41bddc`) the cut is an interior corner: gaps 0 and 9 are ordinary-loop traversals. Lambda=[0,L] with short copy t; its forward traversal is gaps i,i+1 (Lambda[0,t], Lambda[t,L]), its backward traversal gaps j,j+1; u=e_(i+1), w=e_(j+1). Imports: v20 band identity, v21 §2 (T4), and the split-graph facts (F1) the ten v-neighbours carry ten distinct labels and (F2) r labels span exactly r(r-1)/2 edges (v30 §2).

## 2. Window bookkeeping (both signs)

The two short-copy rows are W_F=Lambda[s_F,s_F+10], s_F=t-u, and W_B=Lambda[s_B,s_B+10], s_B=t-10+w, each containing t strictly inside. Put D=s_F-s_B=10-u-w; (T4) gives |D|>=4. With q=|D| the exclusive parts of the two windows carry one label set Q (|Q|=q) and the overlap carries K'=O minus Q (k=10-q labels) together with t strictly inside; hence the short-copy neighbours Lambda[t-1], Lambda[t+1] carry K' labels. Let E_L=Lambda[1,min(s_F,s_B)-1] and E_R=Lambda[max(s_F,s_B)+11,L-1].

Matching each gap's HEAD and TAIL (one common vertex) gives HEAD(i)=Lambda[1,s_F], TAIL(j+1)=Lambda[1,s_B], TAIL(i+1)=Lambda[s_F+10,L-1], HEAD(j)=Lambda[s_B+10,L-1].

- D<0: the Hamilton rows j+2 and i+2 contain Lambda[1,s_B]=E_L+Q-path+one K' vertex and Lambda[s_F+10,L-1]=one K' vertex+Q-path+E_R. Hence E_L, E_R are K' labels and HEAD(j+2), HEAD(i+2) (in the ordinary traversals after Lambda's backward arrival at 0 and forward arrival at L) are **pure K'** of lengths k-1-|E_L| and k-1-|E_R|.
- D>0: symmetrically rows i and j give E_L, E_R in K' and **pure-K'** TAIL(i-1), TAIL(j-1) (the ordinary traversals before Lambda's forward departure at 0 and backward departure at L), of the same lengths.

Every pure-K' segment touches the branch v at its outer end.

## 3. Lemma

**Lemma (interior offset).** At an interior cut, |D| is 4, 5 or 6. Moreover with c_0=[E_L nonempty]+[k-1-|E_L|>=1] and c_L likewise, 2+c_0+c_L<=k.

*Proof.* The short-copy neighbours, Lambda[1] when E_L is nonempty, Lambda[L-1] when E_R is nonempty, and the outer vertex of each nonempty pure-K' segment are distinct v-neighbours with K' labels; by (F1) there are at most k of them. If k>=2 then c_0,c_L>=1, so 4<=k, i.e. q<=6. If k<=1 the two short-copy neighbours would need two distinct K' labels. With (T4), q is 4, 5 or 6. QED.

**Corollary (q=6 rigidity).** If |D|=6 then k=4, each end has |E| in {0,3}, and the four K' labels have their unique v-edges exactly at Lambda[t-1], Lambda[t+1] and one vertex per end (Lambda[1] or Lambda[L-1] when that |E|=3, otherwise the outer vertex of the 3-vertex pure-K' segment); every other v-neighbour carries a Q label. The overlap carries two K'-K' edges and each end a 3-vertex K' path; when these paths share no physical edge they already carry all six edges of K4(K'), so no further two K' labels are adjacent anywhere.

## 4. Use

The ten remaining interior corners (v30 §4) have offsets d=±D given there; each now needs |d| in {4,5,6} besides its band ranges. This is a necessary condition only; no remaining corner is closed by this packet.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
