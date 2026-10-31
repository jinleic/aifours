# F824 candidate addendum 1 — grade-three notation and written checks

The candidate remains unchanged. In its §3, \(q_k=(\operatorname{ad}x)^k a\), so \(q_0=a\). In its §5 only, rename the later symbols `q_0=[x,a]` and `q'_0=[x,b]` to **p** and **p′**, respectively, throughout that section, including equations (8)–(9), their definitions of \(Q_i\), and the accompanying prose. Thus \(p=q_1\) in the §3 notation. This resolves a local notational collision; no mathematical assertion or scope changes.

For a more explicit written check of the §5 construction, its lowering table gives

\[
\begin{array}{c|cccc}
&Q_1&Q_2&Q_3&Q_4\\\hline
F_1&0&0&Q_1&2Q_2\\
F_2&3p&4Q_1&0&4Q_3
\end{array}
\qquad F_1p=F_2p=0. \tag{A1}
\]

Consequently \(F_1T_{27,r}=0\), and \(F_2T_{27,r}=3[x,p]-[x,3p]=0\). For \(T_{10,r}\), its F1 terms are `[2b,p]-2[b,p]+[x,Q1]-[x,Q1]=0`, and its F2 terms are `[a,p]-4[a,p]+3[a,p]=0`. The candidate gives the cancellations for \(T_{8,r}\). For the additional vector Z, the table gives \(F_1Y=F_2Y=0\), \(F_1Y_1=Y\), \(F_2Y_2=Y\), \(F_1Y_3=2Y_2\), \(F_2Y_3=Y_1\), and the other cross lowerings of \(Y_1,Y_2\) zero. Substituting them into Z makes its F1 terms `2[x,Y2]-2[x,Y2]-[b,Y]+[b,Y]` and its F2 terms `[x,Y1]-2[a,Y]-[x,Y1]+2[a,Y]`, both zero. The formal primed substitution is a check of the interchanged table, not an automorphism claim for fixed \(A(3,s)\).

The main image calculations may likewise be seen directly. Let \(A=[x,c],B=[x,d],C=[a,b]\); then \(Q_1=B-C\), \(Q_3=[c,a]-[d,a]-[x,e]\), and

\[
F_3p=2(r-1)a,\quad F_3Q_1=2(r-1)d,\quad
F_3Q_2=4(r-1)f,\quad F_3Q_3=-2(r-1)e,\quad F_3Q_4=4(r-1)g. \tag{A2}
\]

For example,
\(F_3[b,p]=-s(B-C)-2(r-1)C\) and
\(F_3[x,Q_1]=(r+s-4)(B-C)+2(r-1)B\), yielding the candidate's first 27 column. In the 10 calculation, the total coefficient of \(Q_3\) is `4-5r-2s`, and the additional coefficients on `([c,a],[d,a],[x,e])` are `(2,-6,2)(r-1)`, giving the stated 10 column after expansion. For the adjoint column, with `(P,Q,U,T)=([x,g],[a,f],[b,e],[c,d])`, the identities \(E_1Q_2=Q_4\), \(E_2Q_3=E_{12}Q_1=Q_4/2\) and \(Q_4=2(P+Q-U+T)\) give

\[
F_3T_{8,r}=(6r+4s-4)Q_4+4(r-1)P+16(r-1)Q+8(r-1)U,
\]

which expands to the displayed \(v_r\). For Z, \(Y_1=-[a,d]-[x,e]\), \(Y_2=[b,c]-[x,f]\), \(Y_3=-P-Q-2U\), \(E_2E_1Y=P-2Q-U\), and

\[
F_3Y=(3r+2s-2)c-(2r+3s-2)d,\quad
F_3Y_1=(2-4r-s)e,\quad F_3Y_2=(2-r-4s)f,\quad F_3Y_3=(2-r-4s)g.
\]

Substitution gives the candidate's \(v_Z\), and the written determinant factorization there covers the **three complete adjoint multiplicity directions**. These are written reconstructions under the same SRC and G2 imports; they do not verify the unpaid six grade-four emitted basis/action joins, authenticate any source, or supply parent disposition.
