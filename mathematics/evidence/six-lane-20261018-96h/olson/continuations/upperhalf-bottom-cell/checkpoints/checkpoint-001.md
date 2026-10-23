# BOTTOM checkpoint 001: odd-gap equality is rigid; deriving a necessary escape profile

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T18:36:55-0700. Scope BOTTOM-scope-v1.md SHA256
ab9ee0251454d4242b2d268e73eacacf875df6172467f3a24fef6c3cbc22d99e frozen 18:30:34, before derivation.
Written by hand, CANDIDATE_UNVERIFIED; no scientific computation.
Derived in notes (unfrozen): put k=floor(e/2)+1 and G_m=min(e-1,2m-2). Every violation of the desired low-set bound for
m<=k has g=c-d odd, 1<=g<=G_m; its MW count is q=g (even g gives q=g+1 and a contradiction). Equality at q+w0=p-1 forces
all minority signed values into {-a,3a}: for g>=3, each difference must translate a g-term interval by one step (+/-2a),
otherwise growth reaches p; for g=1, subset sums force every difference +/-u, and the >=c-1 signed -a letters force u=2a.
The unique omitted target is half the total signed rotation sum: 2T(z_P)=D_z, equivalently sum_P (tau_i+X_i)=D0/2. Thus all
non-{+/-a} letters have signed value 3a at every low odd-gap escape. Empty runs cannot be toggled while preserving m at
such a pattern (it would keep g and change T): their two neighbours must have the same sign.
Working on the no-escape implication: without any such pattern at m<=k, low-set Lemma L holds at those m; the m=k path
(still exists, unlike m=e) gives a super-heavy run; empty cluster bounds and the Q-block position argument then contradict
avoidance. If completed this yields an exact narrower residual with a necessary odd-gap, four-value rotation support and
run-sign bottleneck, not a bottom-cell closure. Next: freeze complete proof and record the still-open profile.
