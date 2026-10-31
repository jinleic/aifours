# Addendum: the universal critical hidden sum exceeds 51/10

Status: **WRITTEN-checked with exact stdlib Fraction/Bernstein arithmetic**, awaiting independent mathematical review. This immutable successor strengthens `frontier-20261029-ph7-critical-all-hidden-sum-greater-five-v1.md` (SHA256 `2f01ff058c4977e5f49c77082b4353934e880b3efd0e6276857fdac848f32760`) from `p>5` to

`p>51/10`.

The theorem has the same hypothesis: a real seven-state Metzler generator whose spectrum contains the critical pair twice, zero, and two stable hidden eigenvalues, with hidden quadratic `Q(y)=y^2+p*y+q`.

If the hidden roots are real, the named all-real theorem already gives the stronger `p>3437/500`. For a nonreal pair `-r +/- ih`, `p=2r`. The original proof already forces `r>43/20`; assume `r<=51/20`. The entire rectangle is now parameterized by

`r=43/20+(2/5)*s`, `h^2=t*(45r^2-72r-58)/63`, `0<=s,t<=1`.

Both necessary-inequality cases of the parent proof hold unchanged. Exact complete Bernstein selector covers on this **larger** rectangle were checked as follows:

* If centered `tau3<=0`, `frontier-20261029-ph7-complex-hidden-third-fourth-51over20-check.py` (SHA256 `b27a34aa88f4d254f620074161b9f4afe27e2f398b3afced4af39d315494c630`) proves that either `(25/42)tau2^3-tau3^2<0` or `tau4+10tau2^2<0`: **18** and **13** strict selector leaves. The program returned PASS.
* If `tau3>0`, `frontier-20261029-ph7-complex-hidden-positive-skew-51over20-check.py` (SHA256 `e2b4b1eb0e8678203dbcb13a64b1d159b2a4f13e6832677881793ca884d4f0fa`) proves either `-tau3>=0` or both `J= tau4+10tau2^2<0` and `J^2-9tau2*tau3^2>0`: **14** and **11** selector leaves. On the strict positive-skew domain only the latter alternative applies and contradicts the parent's universal fourth-trace inequality. The program returned PASS.

Each successor checker loads only the mathematical definitions from its pinned predecessor, substitutes the affine coordinate `s -> (8/7)s`, and constructs/checks its **own** complete exact binary tree. Both are stdlib `Fraction`/integer arithmetic. They reuse the preceding implementation, so they are not independent-code replays of one another, disjoint scientific review, or formal verification. The correctness of the original centered-trace fourth-walk bound and all imported real-root results remains a required audit input.

These strict inequalities exclude `r=51/20` as well as smaller means, proving `p=2r>51/10`. No PH7/PH8 existence verdict, novelty, parent adoption, or realization at any higher `p` is claimed.
