# The orthodox finite-envelope argument cannot simply be reused nonorthodoxly

**NEW AUTHOR WRITTEN + EXACT FINITE-CHECKED BOUNDARY; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:28:17 PDT 2026**. This is an additive limitation on `frontier-20261028-orthodox-finite-original-reduction-v1.md`, SHA `d208670ba3ceddf6f680c51198209b9e56b23421c4067e2cc166b1e69c11924f`. It does NOT disprove the existence of finite regular envelopes in general.

## Concrete original-class source

Use the actual 45-element regular, weakly E-unitary, locally r-orthodox nonorthodox source and its actual q in `frontier-20261028-all-cs-globally-regular-band-obstruction-v1.md`, SHA `2f9f6a68a153449b61cda78305174c5b601e28fba49ec391bc1107aaba8e31af`, together with its explicit locally regular physical host in `frontier-20261028-ambiguous-source-local-band-host-v1.md`, SHA `a96cb3eeae75bba72af2cc43ff548785c74224fb7ed3509303a0f177cfb2feba`. Its base A is the pinned five-element table and

`P=((4,4,4),(4,1,3),(4,4,1))`.

The elements `e=(1,4,0)` and `f=(0,4,1)` are idempotents, so each is its OWN mutual inverse. Nevertheless the finite subsemigroup `F=⟨e,f⟩` has11 elements and is not regular. Indeed

`x=ef=(1,4,1)`, `y=fe=(0,1,0)`, and `xyx=(1,1,1)≠x`.

In fact x has NO mutual inverse anywhere in F. Hence the reversed product of these particular chosen inverses e,f fails to invert ef, and simply adding each idempotent as its own inverse to the generating set adds nothing. This is the precise point at which the orthodox envelope proof uses global closure of E(S).

There IS an ambient inverse `z=(0,4,0)` of x. Adding z yields `F'=⟨e,f,z⟩` of12 elements; the direct checker verifies F' is regular, weakly E-unitary and locally r-orthodox. Thus this finite example provides a regular envelope after one additional choice. It does NOT prove that all inverse choices fail, that the process must diverge, or that finite regular envelopes do not exist in every locally finite original source. Both F and F' have8-element actor image under the ambient q; F itself is nonregular.

`frontier-20261028-nonorthodox-idempotent-envelope-checker-v1.py`, SHA `85a82afca5d1714b5a866273655f9d0ca12bd01d2b1354dcf48c85d79e6f561e`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:28:17 PDT 2026**, exit0. It generates F and F' by closure, exhausts inverses in each, verifies e,f,z products and F' regular/WEU/local-r, and reports the exact actor-image counts. The ambient source's original-class properties are verified separately in the pinned source checker. This is same-author finite evidence, not an independent witness review or a claim about the full original problem.
