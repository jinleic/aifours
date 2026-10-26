# Addendum 3 — explicit multiplicity in the quasiuniform pair-size argument

This is a precision supplement to `ADDENDUM-2-quasiuniform-projection-v1.md`, SHA-256 `d813c0e6dfb9ff023208eb7764a319e207a7be54a0f3f2c0a550549f7db3ca6f`. It adds no new theorem or acceptance claim and changes no earlier bytes.

In that file §2 and item3 of the dependency list in §7, make explicit the following fact already used in its cardinality cases:

> If a pair (X_z,X_w) and both marginals are uniform on their respective supports, then `n_z | n_zw` and `n_w | n_zw`, as well as `n_zw | m` on the uniform support Omega of X_Z.

Proof: for a fixed attainable value x_z, the number of attainable x_w paired with x_z is `n_zw/n_z`, since each pair atom has probability1/n_zw and each x_z atom has probability1/n_z. This count is an integer. Reverse z,w for the other divisibility. Every pair atom has m/n_zw preimages in Omega, proving the third divisibility.

Thus the complete pair rule used in Addendum2 is: **n_zw divides m, is a multiple of both n_z and n_w, exceeds their maximum under the no-single-coordinate-dependence condition, and is at most their product**. This supplies explicitly the multiplicity hypothesis in every index12 and index15 deduction. No assumption from a subgroup lattice is being smuggled into the quasiuniform extension.

Separately, the book relationship was checked from actual source extraction, not only the historical screen. `book-pages417-424-source-v1.txt` (SHA-256 `1b67e33b28e045f782d1315f671d37cb31bb7b224dfef1651cf03d7fd5c8a8a2`) was extracted by pdftotext from PDF pages438–445. The information-science volume's freshly observed SHA-256 is `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db`, matching `books/README.md`. The readable Chinese text at extraction lines36–51 and603–633 concerns general network capacity, information-flow maximization and network coding; it does **not** pose the later R-minus graph. Some Latin formula text is font-encoding-garbled, so it is not used for an exact mathematical quotation. Our book relationship remains a modern concrete descendant, not a claimed literal book solution.
