# Local right/left regularity is the corresponding seminormal identity

**Status: NEW AUTHOR WRITTEN UNIVERSAL IDENTITY PROOF, with exact free-band checks; UNREVIEWED / UNADOPTED.** This identifies the one-sided band varieties in the fresh structural decomposition with standard literature terminology. It does not prove the physical host theorem for those source subclasses.

## 1. Exact identity equivalence

For a band B, the following are equivalent:

1. Every local monoid eBe is a RIGHT regular band, `xyx=yx`.
2. B satisfies `abc=acabc` for all a,b,c.

The identity in2 is the standard **right seminormal band** identity as explicitly stated in Dolinka, <https://arxiv.org/html/1010.3737v3>, proof of Proposition2, citing Petrich–Reilly PropositionII.3.8. The dual equivalence says local LEFT regularity (`xyx=xy`) is exactly

`abc=abcac`,

the left seminormal identity. The displayed equations, rather than labels alone, fix conventions.

**2⇒1.** In an actual local monoid with identity e, substitute `(a,b,c)=(e,y,x)`: `eyx=exeyx`, hence `yx=xyx`. This is precisely the right regular law.

## 2. Band-content input and the converse proof

We use the classical Green–Rees band-content identity: if words X,Z have the same content and Y has only letters of that content, then `XYZ=XZ`. A direct standard proof in the free band places X,XY,Z in one rectangular D-class. The equation `X(XY)=XY` makes X and XY share the same R-row, so `(XY)Z=XZ`; the free universal property transfers it to all bands. In particular same-content words X,Y satisfy `XYX=X`. This is a named classical band-structure input, not an inference from a finite sample.

Assume local RIGHT regularity. First choose, in the local monoid aBa,

`X=abca`, `Y=acba`.

Their contents agree, so `XYX=X` in every band. Local right regularity gives `XYX=YX`. Reduce

`YX=acbaabca = acbabca = acbbca = acbca`:

the first/last steps delete adjacent squares aa,bb; the middle step deletes the a in `(acb) a (bca)` by the content identity. Thus

`abca=acbca`.                                            (I)

Similarly, in cBc choose `X=cabc`, `Y=cbac`. Again `XYX=X=YX`, and

`YX=cbaccabc = cbacabc = cbaabc = cbabc`,

where the middle deletion is the c in `(cba) c (abc)`. Hence

`cabc=cbabc`.                                            (II)

Multiply(I) on the right by bc. Its left side is `(abc)²=abc`; its right side is `acbcabc=acbabc`, deleting the c in `(acb) c (abc)` by content absorption. Multiply(II) on the left by a to obtain `acabc=acbabc`. Therefore `abc=acabc`, proving1⇒2. Reversing all products yields the left-sided identity `abc=abcac`. □

## 3. Exact check, source terminology and scope

A same-author Python-kernel free-band congruence extraction on the 159-element free three-generator band produced precisely the two local instances above; its dependency graph has five accepted equality/context steps. The final written proof in §2 uses only those explicit local substitutions, the stated square deletions and three content absorptions, and does not rely on the congruence program's union-find. The literal verifier `frontier-20261028-local-one-sided-identity-replay-v1.py`, SHA `8b3b10b7780083ee0204c5d5e54b438a0e6e01d61e764c328ae5adc09709e3d4`, completed in the Python eval kernel before Wed Oct 28 23:59:17 PDT 2026; it checks every word reduction and local substitution and confirms that abc and acabc are distinct in the unrestricted free band. These are exact same-author checks, not a formal proof or independent review.

Consequently, for an original source S with RRB local idempotent bands, **each of its idempotent pure-CS fibre bands is right seminormal**; the dual statement holds for localLRB sources. The source itself need not be a band or globally orthodox, so this fact does NOT put S into the published E-unitary-orthodox theorem merely by naming its fibre variety. The matching one-sided nonorthodox embedding remains the real gap. The verified S68 eight-/ten-band hosts satisfy the right seminormal identity in literal table checks, but no all-source host of that variety is asserted.

No novelty, independent proof/source review, full original Q1 or formal verification is claimed. All named Green–Rees and literature-convention inputs require the same independent checking as the fresh local Green-cover proofs.
