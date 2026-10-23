# Task: independently verify eight claimed optimal CPCW (optical orthogonal) codes

Definition (Baicheva-Topalova, Axioms 15(1) (2026) 35, Definition 1 and p.2): a (v,k,1) CPCW code of size s is a collection of k-subsets C_1..C_s of Z_v (codewords) with |C_i ∩ (C_i+t)| <= 1 for all i and 1 <= t <= v-1, and |C_i ∩ (C_j+t)| <= 1 for all i < j and 0 <= t <= v-1. The size cannot exceed floor((v-1)/(k(k-1))); codes reaching this bound are optimal. The paper states these eight cases are open: optimal (v,5,1) codes for v = 143, 144, 146, 162, 167 and optimal (v,6,1) codes for v = 122, 123, 124.

Format of each file cpcw_V_K.txt: first line 'CPCW V K', then exactly s lines, each with K increasing integers in 0..V-1 separated by single spaces.
