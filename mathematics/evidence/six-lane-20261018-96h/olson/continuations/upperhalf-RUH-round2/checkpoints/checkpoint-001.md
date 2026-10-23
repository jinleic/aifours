# RUH2 checkpoint 001: uniform strong-window lemma and the range c<=e-1 (SH range) derived; c>=e open

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T17:14:23-0700. Scope frozen 17:07:02 (RUH2-scope-v1.md SHA256
b1cdfaeee6db5985a2af1f8f98c4f66cd7a8e8e8fe77cbebab372f270d4c5dd0). Hand derivation only; nothing frozen yet.

Worked so far (CANDIDATE, written in notes; to be frozen):
- Parameters: e=p-kappa in [5,(p+1)/2], R=3p-1-2e, A=2kappa+c, b=p-1-c, lambda=c-1; admissible lengths n=2p-2j with
  j in [m, m+e-1]; omitted counts K_j=p-1-2e+2j.
- SH range 3e<=p+2 (p>=13, 5<=e<=(p+2)/3): re-derivable super-heavy run h (UH Sec. 5 route), light sets, E>=2,
  E+|Q|>=c+1. NEW uniform strong-window lemma: every nonempty P avoiding h has d(P) <= c - min(e, 2m(P)-1). Proof: MW with
  g=c-d, w0=b+d, j in [max(m,ceil(e-g/2)), min(m+e-1,floor((p+1+g)/2))]; Case A (m>=e-floor(g/2)) gives q>=g+1 whenever
  g<=e-1; Case B gives q>=g+1 whenever g<=2m-2 (using p>=3e-2).
- NEW uniform exclusion for 3<=c<=e-1 (SH range): S=E u Q has independence number <=(c+1)/2 and |S|>=c+1, forcing c odd,
  S = c+1 empty runs; then every nonempty set Y of empties has t(Y)+e in M (length j=e free), and RS(b) on the c+1 nonzero
  t-values gives |M|>=c+1>c. Contradiction.
- Not closed: SH range with e<=c<=2e-1 (needs a general missing-set/empty-run classification; the counting bounds tried give
  only E<=ceil(c/2) or E>=e-floor(c/2), which is vacuous at c=e); the whole range 3e>p+2 (no super-heavy run; light sets need
  the two-high-set branch A'>=kappa+1-c/2 excluded). Next bounded action: freeze proof of the uniform partial plus an exact
  residual note in (p,kappa,c,profile) form; then package, IRC, park.
