# Task: independently verify a claimed balanced ternary design witness

Definition (Francel-Hurd; repeated blocks allowed). A BTD(V,B;rho1,rho2,R;K,Lambda) is a V x B matrix M with entries in {0,1,2} such that
- every row has exactly rho1 entries equal to 1 and exactly rho2 entries equal to 2 (so its sum is R = rho1 + 2 rho2);
- every column sums to K;
- any two distinct rows i != k have inner product sum_j M[i][j] M[k][j] = Lambda.
Target: V=14, B=28, rho1=8, rho2=3, R=14, K=7, Lambda=6.

File: btd14-28-witness-v1.btd, expected SHA-256 18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1.
Format: line 1 exactly "BTD 14 28 8 3 14 7 6"; then exactly 14 lines, each exactly 28 tokens from {0,1,2} separated by single spaces; one final LF; nothing else.
