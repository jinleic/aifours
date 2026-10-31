# F829 candidate v1 — additive phase-notation correction

In §5, subsection “Physical locations, H, residue and phase retained”, the candidate defines `P_i=⊕_{b:s_i(b)=1} b` as a vector, and then incorrectly writes `|P_i|≡k_i (mod 2)`. Its absolute value is not the number of negative graph entries. Define instead `n_i=#{b:s_i(b)=1}` and retain the distinct XOR vector `P_i=⊕_{b:s_i(b)=1}b`. The correct row-zero statement is

`n_i≡k_i (mod 2)`.

Indeed the zero profile gives `Σ_b [(-1)^{s_i(b)}+X_mate(i,b)]=0`; dividing by 2 and reducing modulo 2 gives `(2-n_i)+k_i≡0`, since precisely the `k_i` D0 mates are `±2`. The quadratic ANF coefficient of `s_i` equals `Σ_b s_i(b)=n_i mod 2`, so the subsequent ANF, the vector identity (13), and the conditional relation (14) remain exactly as stated. This is a notation correction, not an in-place change or a new source import. Read the original candidate together with this erratum and `prebody-ack-transport-disclosure-v1.md`.
