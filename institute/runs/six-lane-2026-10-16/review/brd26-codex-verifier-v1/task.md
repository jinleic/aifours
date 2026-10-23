# Independently verify a Bhaskar Rao design
A BRD(V,B,R,K,Lambda) is a VxB matrix over {-1,0,1}, every row has exactlyR nonzero entries, every column exactlyK nonzero entries, and each pair of distinct rows has exactlyLambda/2 products+1 and exactlyLambda/2 products-1 (the rest0). Repeated columns allowed. Orthogonality alone is insufficient: the signed inner products AND unsigned intersection counts must match.
Target26x130,R25,K5,Lambda4: all325 rowpairs must have exactly2 positive,2 negative and126 zero products.
File brd26-130-witness-v1.brd; SHA256 eb15cba18110e8c2e4ba7798838fc0a8fd508310d8a73a04132abb49977d71fe.
Strict format: header exactly `BRD 26 130 25 5 4`; then exactly26 lines of130 tokens from {-1,0,1}, single spaces, exactly one finalLF. No comments, blank lines, CR, tabs or other tokens.
