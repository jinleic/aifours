# R-minus critical corner — unrestricted ALL-SITES nonextension of the fixed independent repair

Owner **InfoGuessingRminus-2**, info-5. Actual returned `/bin/date` before this write: **Sun Oct 25 17:41:17 PDT 2026**.

**NEW WRITTEN complete stronger extension barrier.** This is ADDITIVE to the216LF `critical-corner-joint-extension-barriers-and-repair-v1.md`, SHA256 `f6ee79a6a624043565c9d1dd42b5bc62b87ab0c06e9d7c568ba1c7161ae3735b`. Its support-restricted theorem remains correct at its freeze; the new proof here removes that support restriction ENTIRELY. No source is edited, no earlier result is backdated and no candidate automatically inherits acceptance.

The original26-edge graph, all ten triangle columns/all thirty physical slots, SAME Z_m/allm>=2 including composite nonunits, exact actual decoder/SECTION/removal interface and common critical family are EXACTLY §§1–2 of that source. Every step below is written, not a scientific interpreter/calculator/program/CAS/enumeration/solver/replay/CLI/nestedagent/GO. Permanent findings, original root/slots/cutoff/deadline/HOLD remain.

## 1. Exact theorem and no hidden restriction

Use the whole common critical family, A,...,J order:

`eta0=0`,

`eta1=(0,0,0,d,0,f1,0,h,i,j)`,

`eta2=(a,b,0,0,0,f2,0,0,i,j)`,

`eta3=(0,c,0,0,0,0,g,h,i,j)`,

`eta4=(a,0,q,0,0,0,0,h,0,j)`.

Retain `a,b,c,q,f1,f2,h,j!=0`, `b!=c`, `f1!=f2`, `(d,i)!=(0,0)`, `(g,i)!=(0,0)`. No field division or scalar renaming is permitted.

The natural valid four-row independent repair from S={2,5,8} has all unlisted physical sites0 and

|row|physical2:(A,D,E)|physical5:(B,G,I)|physical8:(F,H,J)|
|---|---|---|---|
|0|0|0|0|
|1|(0,d,0)|(0,0,i)|(f1,h,j)|
|2|(a,0,0)|(b,0,i)|(f2,0,j)|
|3|0|(c,g,i)|(0,h,j)|

These exact rows are fixed in this theorem. They have the prescribed syndromes and are pairwise confusing because their difference support is inside the original independent set S.

> **ALL-SITES-NONEXTENSION.** There is NO representative b4 of exact syndrome eta4, on the FULL unrestricted original thirty-slot space, which is confusing with ALL THREE of the displayed b0,b2,b3. In particular no such b4 extends the full four-row repair. Its support and witnesses are NOT restricted at all.

Row1 is not needed for the proof. This is a genuine obstruction to extending a PARTICULAR valid simultaneous section, not a theorem that the four syndrome classes0/2/3/4 have no other section. The supported ANY-three-nonzero theorem remains consistent: those four labels can choose different older representatives.

## 2. Complete original-witness exhaustion for pair24

Assume b4 could extend. It must be confusing with b2 at some ORIGINAL vertex v. Recall the FULL original neighbours:

`N1=234567`, `N2={1,3,7,9,10}`, `N3={1,2,4,8,9}`,

`N4={1,3,5,8,10}`, `N5={1,4,6,9,10}`,

`N6={1,5,7,8,9}`, `N7={1,2,6,8,10}`,

`N8={3,4,6,7,9,10}`, `N9={2,3,5,6,8}`,

`N10={2,4,5,7,8}`.

A witness forces b4,Nv=b2,Nv as FULL physical symbols. Exact syndrome sums then force its own tuple via the actual decoder. We inspect ALL ten possible vertices; no chosen comparison palette or added support hypothesis appears.

Vertex2 is immediately impossible: the ACTUAL defects are equal, `d2(eta2)=d2(eta4)=(a,0,0)`. Full-neighbour equality there would force equal own symbols.

For vertices3,4,6,7,9,10 the forced symbols already make pair04 NOT confusing. The following table gives EVERY one of these cases, including each allowed extra site:

|candidate witness v for24|Forced NONZERO support F of b4|Possible additional nonzero sites|Edges showing every F vertex already has a changed neighbour|
|---|---|---|---|
|3|{2,3,8,10}|5,6,7|cycle2–3–8–10–2|
|4|{2,4,5,8,9}|6,7|cycle4–5–9–8–4, plus2–9|
|6|{3,4,5,6,8}|2,10|cycle3–4–5–6–8–3|
|7|{2,4,7,8}|3,5,9|path2–7–8–4|
|9|{2,5,8,9}|1,4,7,10|star at9 with leaves2,5,8|
|10|{1,2,5,8,10}|3,6,9|1–2,1–5,10–2,10–5,10–8|

Every listed additional site has a neighbour in F, directly from the SAME neighbour array. All other sites outside F/additional are forced0 by the witness. Thus EVERY changed physical vertex has a changed neighbour, regardless of additional symbols. Such a b4 is not confusing with baseline0 at ANY vertex.

Here are the exact slot forces producing each row; they also establish that no tuple's nonzeroness was assumed without proof:

- **v3:** witness fixes physical2=(a,0,0),8=(f2,0,j),1=4=9=0. The F sum forces own3,F=-f2; the H sum forces10,H=h. Thus2,3,8,10 are all nonzero. Sites5,6,7 are the only remaining possible additions and see respectively10,8,2/8 in F.
- **v4:** witness fixes5=(b,0,i),8=(f2,0,j),1=3=10=0. Then own4,B=-b, physical2,A=a, physical9,F=-f2. The only other allowed sites6,7 see5/8 and2/8 respectively.
- **v6:** witness fixes5=(b,0,i),8=(f2,0,j),1=7=9=0. Own6,C=q, physical3,F=-f2 and4,B=-b. The only other allowed sites2,10 see3 and4/5/8.
- **v7:** witness fixes2=(a,0,0),8=(f2,0,j),1=6=10=0. Own7,C=q and physical4,H=h. Possible additions3,5,9 see2/4/8,4,2/8 respectively.
- **v9:** witness fixes2=(a,0,0),5=(b,0,i),8=(f2,0,j),3=6=0. Own9,F=-f2. Possible additions1,4,7,10 each see at least one of2,5,8.
- **v10:** witness fixes2=(a,0,0),5=(b,0,i),8=(f2,0,j),4=7=0. Own10,H=h and physical1,B=-b. Possible additions3,6,9 see1/2/8,1/5/8,2/5/8 respectively.

These are exact additions in Z_m. The required a,b,f2,q,h,j are nonzero even if nonunits; no field rank or interpreter appears.

## 3. Vertex5 is also impossible, with the full four-cycle support

If5 witnessed24, it would force b4,N5=0, because the fixed b2 is supported on S={2,5,8} and N5 meets none of S except not5 itself. The actual d5(eta4)=0 then makes b4,5=0 too.

Thus b4 is supported entirely on `U5={2,3,7,8}`. Exact C syndrome q forces changed physical7 (the other C corners1,6 are0); exact H syndrome h forces changed physical8 (other H corners4,10 are0). The induced graph on U5 is COMPLETE bipartite with shores{2,8} and{3,7}. Changed7 and8 lie in opposite shores. Every changed vertex has a changed neighbour, so pair04 is not confusing. This excludes v5 without any restriction imposed on the candidate beforehand.

## 4. Vertex1: ALL solutions of the witness equations and the surviving baseline case

If1 witnessed24, the fixed N1 tuple forces physical2=(a,0,0),5=(b,0,i),3=4=6=7=0. ALL exact-syndrome solutions are consequently, for arbitrary actual t,s in Z_m,

|physical site|forced full b4 symbol|
|---|---|
|1|(0,-b,q)|
|2|(a,0,0)|
|5|(b,0,i)|
|8|(-t,h-s,j)|
|9|(0,t,-i)|
|10|(0,0,s)|
|3,4,6,7|0|

To check completeness, A/B/C fix own1, D/E/G fix9D/10E/10G, I fixes9I, J fixes8J; the only free F/H splits are t=9F and s=10H. Their complementary entries at8 are then forced. No other degree of freedom is omitted.

For baseline04, physical1,2,5 are always changed and have changed neighbours among themselves. Physical8 is always changed because j!=0. Any changed9or10 sees changed2/5/8, so it cannot witness. The ONLY possible baseline witness is8; its full neighbours3,4,6,7 are0 and9,10 must also vanish. Thus baseline confusion requires exactly

`i=0`, `t=0`, `s=0`.

In that case b4,8=(0,h,j), exactly b3,8. The difference b4-b3 is supported on{1,2,5}, with tuples

`physical1=(0,-b,q)`, `physical2=(a,0,0)`,

`physical5=(b-c,-g,0)`.

All three are nonzero: q,a,b-c are nonzero. Their induced graph is the star1–2 and1–5. No changed vertex is isolated. Hence pair34 fails. Vertex1 cannot supply an extension in ANY of its unrestricted solutions.

## 5. Vertex8: ALL solutions and the unavoidable pair34 failure

The fixed b2 has FULL N8=0. If8 witnessed24, the candidate therefore has3=4=6=7=9=10=0. ALL remaining exact-syndrome solutions are, for arbitrary actual u,w in Z_m,

`b4,1=(u,w,q)`,

`b4,2=(a-u,0,0)`,

`b4,5=(-w,0,0)`,

`b4,8=(0,h,j)`,

and all other sites0.

These formulas solve all ten actual sums: A splits u+(a-u), B splits w-w, C=q, H=h,J=j, and the other five sums are0. They are also necessary because every other corner has been fixed0.

At pair34, physical8 agrees exactly with b3. Physical1 is changed by its C component q. Physical5 is changed because its difference is `(-w-c,-g,-i)` and(g,i) is not both zero. Those two physical vertices are adjacent. Any changed physical2 is also adjacent to changed1. No other support is present. Thus EVERY changed vertex has a changed neighbour, and pair34 is not confusing. This excludes ALL u,w, not one selected local normalization.

## 6. Complete conclusion and exact stronger next interface

The ten possible witnesses for24 were exhausted:2 has equal defects;3/4/5/6/7/9/10 force failure against baseline;1 allows a baseline comparison only in a complete subcase which fails34;8 always fails34. Therefore no unrestricted all-sites b4 exists. ALL-SITES-NONEXTENSION is proved. ∎

This strengthens §5 of the preceding216LF manuscript: its six-site support limitation is no longer the only barrier. Keeping that particular valid old repair fixed cannot work even with an arbitrary new representative on ALL ten vertices, arbitrary component values and arbitrary comparison witnesses. At least one OLD representative b2 or b3 (or the old common anchor architecture) must move jointly with b4. Adding more sites only to the new row is not enough.

This is not a claim that ALL sections for the same critical family fail. The theorem constrains a fixed older section; other four-label sections, simultaneous motion of several rows or a data-dependent actual-removal Hall injection are still unproved possibilities. Likewise, failure to extend fixed representatives does NOT construct outside FD words with positive gain.

The original FULL residual remains the entire CRIT OR frontier, all other forest/path/fork roles and arbitrary larger class families/global optimum. No strict gn interval change:20/3..1847/276 and T300 remain unchanged. This is an exact WHOLE-family representation barrier, not a necessary-condition-only count promoted as numerical progress. New joint movement / actual-removal Hall work is the next genuine representation; earlier recoloring cycles and recursive append-only schemes are now explicitly inadequate at this input.

All author/parent/reviewer histories, own024cadenceMAJOR, old compact-clock-caption qualification, parentv101freeze/bindingMAJOR, v9/v10/v11/HOLD and original2026-10-27sciencecutoff11:05:38/deadline12:35:38 remain. WRITTEN only at the literal graph/decoder/trade inputs, not formal/kernel/human/configured-family/executable/novelty or round-completion acceptance. No frozen file was edited and no scientific execution was performed.
