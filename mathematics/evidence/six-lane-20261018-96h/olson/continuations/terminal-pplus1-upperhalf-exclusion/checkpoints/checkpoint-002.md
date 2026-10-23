# Checkpoint 002: UH-EXCL derivation in progress (no candidate frozen yet)

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T13:28:29-0700. Previous: checkpoint-001.md sha256
0b9890f6826f324660b9f5fd4572b4364c16d94067a19664394818f3e87897d3 (13:18:36).

- Parent notices read and applied: KP2 Codex MAJOR (antecedent discipline: every "describes no avoider" statement keeps the full NF
  antecedent k = p+1 and the cell's kappa^) will be followed in this packet; ASSEMBLY-P (o_F <= p) and RPdelta are not used.
- Actual new results worked out (not yet frozen):
  (1) Lemma MW (multi-length window, omission form): for a non-constant pattern with m sign-change pairs and any value s with
      minority W (all other letters), the omission sizes K in [max(|W|, K_min), min(R-|W|, K_max)], K_min = max(0, p-1-2e+2m),
      K_max = p-3+2m, give |attained| >= min(p, |W| + #K) by RS(b) and Cauchy-Davenport. Consequences for the dominant value:
      m = 1: |W| <= p-2 (Lemma P); in general |W| <= p-2m when |W| >= K_min; for m >= e: |W| <= kappa-1 unless
      2kappa+3-2m <= |W| <= 2m-4.
  (2) Correction found in my own sketch: the pure-case run-budget argument of checkpoint 001 used U = p-1, which is wrong
      (U = floor(E_+/2)); the corrected allowed interval for a low arc is [-ceil(alpha(P)/2), (p-3)/2 - alpha(P)]. With the
      corrected interval, lifts along low arcs are still additive, and the pure cell (all rotations equal, kappa^ = (p-1)/2)
      with a run of >= p letters is excluded by: (#empty runs - 1)/2 <= sum d <= (alpha_h - p - 1)/2 versus
      #empty >= alpha_h - p + 2. The sub-case with every run <= p-2 letters is still open in my notes.
- Blocker (unchanged in substance): no whole-interval argument; deviant letters destroy the interval structure of attained sets;
  heavy run / light sets hold only under the tracked inequalities.
- Next bounded action (<= 30 min): decide the deliverable; current plan is an obstruction packet with the whole-interval
  necessary constraints (Lemmas P/U re-derived, Lemma MW new, exact heavy-run and light-set inequalities) plus any sub-cell
  exclusion that is fully proved, each with its restriction named.
