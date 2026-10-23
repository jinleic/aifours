# Task: independently verify a claimed RDSQS(52)

File: rdsqs52_z52_m23.txt (expected SHA-256 7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6).

Definitions. A Steiner quadruple system SQS(v) is a set of 4-subsets (blocks) of V={0..v-1} such that every 3-subset of V lies in exactly one block. For x in V the derived triple system at x is {B minus x : x in B}; it is an STS(v-1) on V minus x. A resolution is a partition of its triples into parallel classes, each class partitioning V minus x into (v-1)/3 triples. An RDSQS(v) is an SQS(v) whose derived system at every point is resolvable. Source of the open question: Tan–Zhou arXiv:2503.11934v1 §4(1): "Find more examples of mcDSQS(v)s, for example, an mcDSQS(38) and an RDSQS(52) (the smallest unknown mcDSQS(6n + 2)s and the smallest unknown RDSQS(6n + 4)s, respectively)."

Format: lines starting with '#' are comments. Then 'RDSQS 52', 'BLOCKS', 5525 block lines of 4 points, then for x = 0..51: 'POINT x' and for j = 0..24: 'CLASS j' followed by 17 triple lines.
