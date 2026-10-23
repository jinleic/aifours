# Erratum 1 to proof-K2-v1.md (author audit; wording only, no mathematical change)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T23:00:44-0700. Read after the immutable proof-K2-v1.md, SHA256 04dc8c68cbe80044c040ea9d6a85acb12960094b0a06f7ce90106af6a8193272.
Each Old span occurs exactly once. The audit re-checked Secs. 1-5 line by line (window arithmetic, label counts of Lemma N,
the bound |d|<=p-5 and uniqueness in (F2), the token moves of (F3), the sets {0,2,4},{1,6,8} in (F4), the sorting and the
equality case of Lemma RIG, and the three cases of Sec. 5) and found no mathematical defect.

## E1 (Sec. 5, last sentence): garbled conclusion
Old:
````text
All cases are impossible; since u is an avoider by NF, so is the hypothesis. This proves Theorem K2. []
````
New:
````text
In every case u has an identity 2p-subword, contradicting that the NF word u is an avoider; hence no avoider w as in Sec. 0
exists. This proves Theorem K2. []
````

## E2 (Sec. 0): wording
Old:
````text
(a fully-full family replacing (H-ALT)), LEMMA RIG (rotation rigidity with tight lift data), and the final arc contradiction.
````
New:
````text
(a family of full patterns replacing (H-ALT)), LEMMA RIG (rotation rigidity with tight lift data), and the final arc contradiction.
````
