# Erratum 1 to proof-R7-v1.md (author's line audit; list wording only)

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T17:02:01-0700. Read after the immutable proof-R7-v1.md, SHA256
2619ab5d9aa2e673a2437587287542cc18cc11575eec8ff6d3eadfd0b336c0b7 (frozen 16:59:31). No statement, case split or conclusion
changes; the proof file is not edited. The Old span occurs exactly once (Sec. 5.3, C12 case (c1)).

## E1: the list of 4-part partitions of 8 in C12 (c1) contained two meaningless fragments

Old:
````text
 (5,1,1,1) [5]; (4,2,1,1) [4+1]; (4,3,1,0)-type excluded; (3,3,1,1) [3]; (3,2,2,1) [3]; (2,2,2,2) allowed; (4,4) etc. have <4
 parts; >=5 parts: (4,1^4) [4+1]; (3,2,1,1,1) [3]; (2,2,2,1,1) [2+1]; (3,1^5) [3]; (2,2,1^4) [2+1]; (2,1^6) [2+1]; (1^8)
````

New:
````text
 (5,1,1,1) [5]; (4,2,1,1) [4+1]; (3,3,1,1) [3]; (3,2,2,1) [3]; (2,2,2,2) allowed (these five are all the 4-part partitions
 of 8); >=5 parts: (4,1^4) [4+1]; (3,2,1,1,1) [3]; (2,2,2,1,1) [2+1]; (3,1^5) [3]; (2,2,1^4) [2+1]; (2,1^6) [2+1]; (1^8)
````

Check of completeness: the 4-part partitions of 8 correspond (subtract 1 from each part) to the partitions of 4 into at most
4 parts, (4), (3,1), (2,2), (2,1,1), (1,1,1,1), i.e. exactly (5,1,1,1), (4,2,1,1), (3,3,1,1), (3,2,2,1), (2,2,2,2).
