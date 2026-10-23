# Corrections to the recency-aware info-2 kill check

The scout's follow-up explicitly withdrew two statements in its original report:

- “SkewW(30,25) has no claim anywhere” means only **no claim found in the stated read scope** (DataCite, OpenAlex, arXiv API, Goldberger/Long/Macías-Quintero records, later one OEIS search). It does not certify openness.
- EPA(9,8,21) is **not** an eligible backup. The parent directly read [OEIS A005677](https://oeis.org/search?q=id:A005677&fmt=json): data `1,1,2,3,5,10,13,16,20`, offset 1, with “a(9) from Luka Tolonen, Mar 14 2026” and reference Östergård–Tolonen, *Classifying Equidistant Permutation Codes (in preparation)*. Thus the published sequence record claims R(9,1)=20, precluding EPA(9,8,21). The underlying classification paper was not read and remains in preparation. The scout withdrew EPA as its backup and raised scoop risk for adjacent parameters.

The follow-up OEIS scope found no circular-Florentine sequence; non-circular A004079 stops at n=12, with no newer parameter claim. That is a search miss, not priority clearance for CFR(4,33).

The follow-up suggested the small BTD instances as a replacement backup. They are already decided in this run and are **not** new tasks. The chosen target is CFR(4,33), with CFR(5,27) and CFR(6,21) as alternates under the frozen contract.

The original scout report is preserved unchanged in `info2-killcheck-screen-v2.md`. No failed scientific direction is rebranded as a new result by these corrections.
