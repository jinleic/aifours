# Exact symbolic replay of the causal syndrome identity

This additive check concerns equation (22) of `frontier-20261028-causal-syndrome-inequality-v1.md` SHA-256 `f71a2aba340746d2c1b910f6a013d871821fcc1e7b2aa3197ce88a3e1dc23d5b`; the pinned packet is unchanged. With all component and syndrome bits treated as formal entropy variables, the check verifies

\[
\text{right side of (22)}-3\Delta
=\sum_t\left(3H(S_t\mid Z_t,Z_{<t})-\sum_{i\in T_t}H(X_i^t\mid X_{T_t\setminus i}^t,S_t,Z_{<t})\right).
\]

All terms on the right vanish by the factor XOR definition. `frontier-20261028-causal-syndrome-identity-check.py` SHA-256 `2c697043f62e3dee4ae86bef12a9d54cdc150fd2e1ca337cbd67c359e41af4ed`, receipt SHA-256 `7deb84169d58290b0847e5192baef8b4bc3f3be958fbdce13bac9571be673195`, checks 147 symbolic entropy coordinates, 10 syndrome conditions, 90 CMI terms and 30 bit-FD rows, with two intended coefficient mutations. This is an integer identity check, not a proof-assistant formalization or an independent scientific review of the entropy interpretation.
