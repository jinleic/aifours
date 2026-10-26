# Actual Tuscan11 same-centre 4+4, two faces — rotation classes and the equal-split class excluded

Actual `/bin/date` before this body: **Mon Oct 26 01:48:01 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

v12 §4.3 (SHA256 `c2a9283d09b06781e0f1b76a42a0dcb700913dc87bddf69aabae78ff32caf6b2`, parent-accepted): two degree-4 branch copies b1, b2 of the same label v, one short copy of v, every other split vertex of degree 2; the core is (a) four parallel threads T1..T4 from b1 to b2, or (b) two threads T1, T2 plus a loop L1 at b1 and a loop L2 at b2; F4 is excluded, so there are two faces. Faces are cycles of phi = sigma alpha (v18 §2). A face with r_f rows and n_f v-visits has gap excesses summing to 10(r_f - n_f), i.e. to 10 in the face carrying the unique v-cut and to 0 in the other; a traversal of a path of length l contributes l-10 (l-20 if it contains the short copy), the same in both directions.

## 2. Core (a)

Name threads so that sigma at b1 is (a1 a2 a3 a4), and let sigma at b2 send the end of T_i to the end of T_pi(i). Then phi^2 sends a_i to a_rho(i) with rho(i)=pi(i)+1 (mod 4), so the faces correspond to the cycles of rho, a face of a rho-cycle of length l having 2l traversals. Over the six 4-cycles pi: pi(i)=i-1 gives rho=id (four faces, excluded); pi(i)=i+1 gives rho=(13)(24); the other four give a 3-cycle plus a fixed point and are conjugate under the index shift. Hence exactly two classes:

- (a)-I: F_1 = T1 T2^- T3 T4^-, F_2 = T2 T3^- T4 T1^- (every thread once in each face).
- (a)-II: P2 = T4 T3^-, P6 = T1 T2^- T3 T1^- T2 T4^- (T1, T2 self-dual in P6; T3, T4 cross).

## 3. Core (b)

A loop whose two ends are adjacent in the rotation would bound a one-branch-visit face, impossible (v4 §3 via v12). So each loop's ends alternate with the thread ends, and naming loop directions gives sigma_1=(t1 l t2 l'), sigma_2=(t1' m t2' m'). Following phi gives the unique class

- (b): F_1 = T1 L2 T1^- L1, F_2 = T2 L2^- T2^- L1^- (T1 self-dual in F_1, T2 in F_2; L1, L2 cross).

## 4. (a)-I is impossible

In (a)-I each face traverses each thread exactly once, so both faces have the same excess sum x_1+x_2+x_3+x_4 (wherever the short copy lies). One face carries the v-cut (sum 10), the other not (sum 0). Contradiction.

**Result.** Same-centre 4+4 two-face systems are of class (a)-II or (b); (a)-I is impossible. These remain open here, as do distinct-centre 4+4, distinct 3+5, and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
