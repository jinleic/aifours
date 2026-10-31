# Any odd-dimensional QLS tensored with an even cyclic Latin square has no transversal

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:02:17 PDT 2026**. This is a general, all-variable even-order tensor obstruction; it is NOT a universal no-go for arbitrary even Fourier products or unrestricted QLS10.

## Theorem

Let Q be ANY quantum Latin square of odd order n, and let L_m be the classical cyclic Latin square of EVEN order m, with labels `L_m(u,v)=u+v mod m`. Then the tensor-product QLS `Q tensor L_m`, of order nm, has **no orthogonal transversal**, whether or not its rays repeat. No assumption of a transversal or a special representation for Q is needed.

In particular, if gcd(n,m)=1, K_n is ANY complex Hadamard and Q is its cyclic Fourier-product QLS, CRT identifies this tensor with the ordinary cyclic Fourier-product QLS of order nm based on CRT-aligned `K_n tensor F_m`. Thus that entire Fourier subfamily has no transversal, for arbitrary K_n and any source-row permutation of the K_n factor. Arbitrary reordering of the F_m factor is not asserted.

## Proof

An orthogonal transversal would contain nm cells, one for each global row `(r,u)` and each global column `(c,v)`. Their second-factor classical rays have labels `t=u+v mod m`. Cells with a fixed t must project to pairwise orthogonal nonzero vectors in the n-dimensional first factor, so each t occurs at most n times. There are m labels and nm selected cells, hence EVERY t occurs exactly n times.

Likewise every u occurs exactly n times, because there is one chosen cell in each global row, and every v occurs exactly n times because there is one in each global column. Let `S=sum_(j=0)^(m-1) j` in Z_m. Summing `t=u+v` over the chosen cells gives

`n S = n S + n S (mod m)`, hence `n S=0 (mod m)`.

But m is even, so `S=m/2` in Z_m; n is odd, so `n S=m/2 != 0`. Contradiction. The proof remains valid for arbitrary Q, including repeated local rays, and uses only the n-dimensional orthogonality bound.

## Relation to earlier work and boundary

This general theorem STRICTLY SUBSUMES the EVEN-m part of the Paley-prime examples in `frontier-20261028-paley-prime-rook-graph-no-transversal-v1.md` SHA **3b25e7f80192035b3483d37336eafe097a74c4b463822668234b049421c26c97**: their even-dimensional tensor no-go does not require the Paley rook-graph theorem at all. The Paley theorem still adds its local rook-graph result and no-go for odd m coprime to p. It also supersedes the switched5-tensor2 finite search as a scientific no-go: the Z3 full-resolution attempt timed out, but the present elementary proof excludes even a single transversal for ANY order5 QLS tensored with cyclic2.

The source-row coordinate of a cyclic Fourier product may be an arbitrary mixing permutation, and K_nm may be an arbitrary complex Hadamard: neither case is covered by the stated CRT-aligned tensor premise. The result does not settle general even Fourier-product transversals, nor construct or exclude a maximal 1RQLS10. Independent review of the tensor/CRT caller is requested.
