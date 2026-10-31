# Exact symbolic replay of the triangle-product entropy identity

This is an additive check of equation (15) in `frontier-20261028-triangle-code-global-obstruction-v1.md` SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4`; it does not edit that pinned packet. The checker treats all 30 factor component bits as formal entropy coordinates. Before using the XOR constraints, it verifies the exact integer identity

\[
\text{right side of (15)}-3\left(\tfrac23\sum_i H(X_i)-H(X_V)\right)
=\sum_t\sum_{i\in T_t} H(X_i^t\mid X_{T_t\setminus i}^t,Z_{<t}).
\]

All 30 terms on the right are zero for the XOR-zero triangle support, yielding (15). The checker reconstructs 30 triangle pair CMIs, 30 cross-factor CMIs and all 30 conditional factor-FD rows, checks coefficient cancellation at 97 named entropy coordinates, checks the original graph's triangle edges and vertex incidences, and rejects four intended mutations.

Checker `frontier-20261028-triangle-product-identity-check.py` SHA-256 `7f31757e2f13c8a134efa2cf5dc4b38c795eb61535b31570d7a8a2fd1bedb142`, receipt SHA-256 `0186e8de8a9f0f8a12741cbccfc89e10cf90d96ac2371d1d333547a67a64f938`. This is exact symbolic coefficient verification, not a proof-assistant formalization or a substitute for independent scientific review of the support/entropy argument.
