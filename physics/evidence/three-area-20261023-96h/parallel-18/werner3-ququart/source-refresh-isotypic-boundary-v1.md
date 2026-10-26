# Bounded source refresh: isotypic entanglement witnesses are not an automatic W4 bridge

Observed clock before writing: `2026-10-23T18:27:10-07:00` (`/bin/date -Iseconds`). Read-only public-source audit plus a written symmetry check; no scientific execution, external-model CLI, email, publication, or access bypass.

## Sources actually reached and limits

1. The publisher abstract and PDF endpoints for Albert Rico, Dmitry Grinko, Robin Krebs, Lin Htoo Zaw, *Entanglement Structure and Matrix Inequalities from Isotypic Measurements*, DOI `10.1103/nvk2-h8d5`, both returned **HTTP 403** to the reader:
   - <https://journals.aps.org/prl/abstract/10.1103/nvk2-h8d5>
   - <https://journals.aps.org/prl/pdf/10.1103/nvk2-h8d5>
   No authenticated route, mirror circumvention, or further publisher probing was used.

2. Public publisher-supplied metadata was actually read at <https://inspirehep.net/api/literature/3200064>. It records *Physical Review Letters* **137(10), 100203**, imprint date **4 September 2026**, `refereed:true`, a CC-BY-4.0 license, the four authors above, and the abstract. This is bibliographic/source metadata, not this lane's mathematical acceptance of the paper. Its abstract explicitly frames the complete small-system characterization around **unitary and permutation symmetry**, with Schur-Weyl isotypic witnesses.

3. An openly accessible closely related preprint by the same four authors was read at <https://arxiv.org/pdf/2511.13822>, *Detection of many-body entanglement partitions in a quantum computer*, arXiv:**2511.13822v1**, posted **17 November 2025** (PDF printed date 19 November 2025). The reader returned the body through page 9, including the main text, Definition 1, Observation 2, Proposition 3, Table I, Theorem 4 and its stated hypotheses, Proposition 5, conclusions, references, and the start of Appendix B. The later appendix proofs were not fully read or reconstructed. `[INFERENCE]` This is a likely preprint counterpart of the later differently titled PRL article, but an exact version-to-version identity was not established from the reached metadata. The inaccessible final publication must not silently be replaced by v1 when making a current theorem claim.

4. The raw official Atom record was also read at <https://export.arxiv.org/api/query?id_list=2511.13822>. It returned entry `2511.13822v1`, entry-updated/published `2025-11-17T19:00:02Z`, and **no DOI or journal-reference field**. Thus this additional reachable metadata did not establish exact identity with the differently titled PRL final version.

## Exact inspected hypothesis boundary

The preprint's witnesses have the form

```
W=sum_lambda c_lambda Pi_lambda,
```

where the `Pi_lambda` are Schur-Weyl isotypic/Young projectors. These witnesses commute with the common unitary action `U^(tensor n)` and with **every** permutation of the n local parties. Theorem 4 gives the `[n-1|1]`-separable minimum for such a W. Observation 2's reduction of product partitions also uses that witness permutation invariance. Proposition 3's completeness is for the stated symmetric three-party class. The main-text four-party Table I is explicitly described there as a numerical characterization, not a general analytic classification of arbitrary four-party operators.

These are substantive results but not a theorem for an arbitrary operator merely because it acts on three or four parties. Nor is ordinary state `[n-1|1]` separability the same hypothesis as the W4 coefficient operator's range or co-range containing one biseparable reference ray.

## A direct noncontainment check for the present four-party operator

Already the fixed positive co-Choi operator

```
C_B=(I-F_13/2)(I-F_24/2)
```

is **not** invariant under every permutation of its four ququart slots. Conjugating by the permutation `(2 3)` gives

```
C'_B=(I-F_12/2)(I-F_34/2).
```

For the unit computational vector `v=|0,1,0,1>`, both `F_13` and `F_24` fix v, so

```
<v,C_B v>=1/4.
```

In contrast `F_12`, `F_34`, and `F_12 F_34` each take v to a distinct computational vector, so

```
<v,C'_B v>=1.
```

Thus `C_B` is not a linear combination of the central isotypic projectors in that four-party representation. A general `S_eta` further depends on the nonuniform Schmidt reference; its complete-copositivity problem is not converted to the cited isotypic hypothesis by naming the reference biseparable. Twirling an operator into the symmetric class would be a different operator; preservation of the exact required inequalities would need a separate proved bridge.

## Operative conclusion

No theorem in the inspected clauses supplies positivity of the current upper-seven/lower-five or zero-nine Schur residuals. This is a precise **hypothesis noncontainment check**, not a claim that no related technique, later appendix, changed journal version, or other paper can help. The final PRL full body remained inaccessible by the attempted public routes, so its detailed current source gate remains incomplete. No novelty certification or claim of priority follows from this audit.

The all-reference target and unrestricted W4 retain their earlier unproved status. Nothing was imported as a new theorem or used as a numerical/programmatic premise.
