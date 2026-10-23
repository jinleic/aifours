# k62-followon checkpoint 016 (Sun63Successor) — M13 Parts A and B frozen

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:59:30-0700.
- Previous checkpoint: `checkpoint-015-v1.md`, sha256 d5e9869fa8ff7b045f9e0372ab068f2582da216582f635b47e3bf504b3b6e090.

## Parent instruction and review state
The CAP/DT overlay 996f924c… is under the parent's narrow dual-family repair review (freeze 78cd1f69…). No verdict has
been sent. Parent permitted ONE written slice on the (1,3)/(3,1) orientations, with a scope note first, conditional on the
CAP/DT verdict where used, and no computation. This does not grant any computation GO.

## Frozen since 015
| file | sha256 |
|---|---|
| `K62-M13-SCOPE-v1.md` | e5795694e99c0d0ae535bd0b8edf6d8d58d2fd17683f1abbaf3498ac5ce5d625 |
| `K62-M13-A-v1.md` | 77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d |
| `K62-M13-B-v1.md` | 455c58f9d35cc165f666eeaec9462e6b6ab6286196450532e619d6c0b9810058 |
A uses accepted imports only and derives the second-family d-row count: DG* for alpha in (1,3), C2*, C1* and the joint
edge-class budget (all candidates). B1/B2 use accepted imports only; B3 is CONDITIONAL ON CAP/DT VERDICT. Together B gives
conditionally |K_alpha|, |K_alpha*| <= 3, hence a c0 != v with alpha*_(i*c0) <= 3 for every v.

## In progress
Part C: a chain with that witness (i* added last; k <= 6) to recover gcd(n_v, T_alpha*(V minus {v})) = 6 for unmarked v,
hence the missing alpha-row 5/6 bound and the alpha*-family cherry isolation (all CONDITIONAL ON CAP/DT VERDICT).

## Boundaries
No computation, enumeration, process or new pattern closure. No (1,3)/(3,1), full K6.2* or Sun(7) exclusion. All slice
claims are unreviewed candidates. Accepted computer-assisted Sun(5)/(6) provenance remains in the import closure.
