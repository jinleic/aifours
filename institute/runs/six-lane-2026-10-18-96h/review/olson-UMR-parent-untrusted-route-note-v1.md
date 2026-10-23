# UMR parent untrusted route note — preliminary algebra, NOT an accepted input

Recorded 2026-10-20T07:28:16-0700 (`/bin/date`). Parent preliminary derivation before this note; no discovery-preregistration claim. The worker must independently re-derive everything below. No computation over mathematical objects; all reasoning by hand.

## Proposed unit reservoir in the general lower half
For p≥17 prime, 1≤kappa≤(p−3)/2, terminal k=p+1: R=p−1+2kappa, t≤kappa−1, n++n−=2t, n−≤t, sum s=n+, W+n+≤2p−1, E=W−L≤p−2kappa+n−, L=R−2t. Labels are a_i, +1 and −s_j, u1≥m1+n+.
- For a label b≥3, m1≥L−1−(E−b+1)/2. Thus u1−b≥(p+3kappa−2−b)/2≥2kappa−1 since b≤1+E≤p−kappa.
- For −s_j, n+−s_j≥n−−1, so u1−s_j≥R−n+−E/2−1≥p/2+kappa+n−/2≥2kappa+2 (n−≥1, p≥2kappa+3).
- For unit labels, u1≥(p+3kappa+1)/2≥2kappa. Hence conjectured uniform reservoir u1≥|b|+2kappa−1. Also original positive-unit count≥(p+kappa+1)/2 after the light side. The stronger lift margin M0≥4kappa−2+(B*−R)−|A| follows if nu0−|A|≤E+n+−n−=B*−R.

## Proposed uniform realisation lemma
For a proper nonempty run pattern with m, let ell=max(0,2kappa+2−2m), u=min(R,2p−2m), M=R−u; ell,M even and≤2kappa, u−ell≥p−1. Candidate exception lists for even v:
- UPPER length failure: v=Pi(P)−s with q+s≤M−2, or v=−nu(P)+s with q′+s≤M−2, s≥0 and s=q(mod2). A minimal representation above u misses≤2kappa−2 letters; unit reservoir makes it single-signed and its omitted same-sign letters units.
- LOWER length failure: v=−nu(P)+s with q+s≤ell−2, or v=Pi(P)−s with q′+s≤ell−2. Choose a representation of maximum size below ell. Its exterior must be single-signed; otherwise add a zero-signed pair or one big letter + unit letters. Such a move has size≤p−1≤u−ell, so it cannot jump over the whole window. Inflate a same-sign nonunit inside into exterior units similarly. Then all opposite-sign letters are inside, and inside same-sign letters are units, giving the listed low exceptions. This bridge argument needs full checking.
Writing epsilon=q mod2=q′ mod2, proposed shifted-realisation offsets:
  x(P)=max(epsilon, ell−q, M−q′), y(P)=max(epsilon, M−q, ell−q′),
  lambda=y−1, mu=x−1. Expected x+y≤max(ell+M,2)<B*. Re-derive, do not assume.

## Central levels (route suggestion only)
At p≡1(mod4), m=(p+3)/4 gives ell=M=delta/2+1 (delta=4kappa−p−1); table lambda=mu=max(epsilon−1,delta/2−min(q,q′)). At p≡3(mod4), adjacent central levels m=(p+1)/4,(p+5)/4 swap ell and M (difference2). These levels depend on p, not kappa, and may keep theta intervals uniformly short.
For a disjoint all-central triple, q1+q2−q12=|A|; every choice of q or q′ at its three terms sums to at least |A| or |A^c|. Combine with the stronger M0 margin to bound additive losses rather than bounding each lambda separately. This is an unproved route. Connectivity/triples and especially the final sorted-set/empty-run count remain to be proved; no uniform exclusion is claimed here.
