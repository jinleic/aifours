# Erratum 1 to evidence/notes-LS-base-v1.md (sha256 dcb03fb3e4e2c314778c39063fcfc9fdc9f1fd7f525632a48d5de6e359cad7b9)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:55:16-0700.  Completes the unchecked family X2 of Sec. 3; no other change.

Family X2: Y - z = g^(2p-1) (pg)^(q+1), q := 2kappa - p (odd, >= 1), z = c g with c odd.  Adding z violates (ZP_kappa):
- c <= p - 2: zero-sums z g^(2p-c) (pg)^y with y even in [0, q + 1] have the even lengths 2p - c + 1 + y, filling every even
  number in [2p - c + 1, 2p - c + q + 2]; this range meets [2kappa + 2, 2p] = [p + q + 2, 2p] (2p - c + 1 <= 2p and
  2p - c + q + 2 >= p + q + 2), and all endpoints are even, so some zero-sum has length in the window.
- c >= p + 2: zero-sums z g^(3p-c) (pg)^y with y odd in [1, q] (and y = q + 1 is even) give the even lengths 3p - c + 1 + y,
  filling [3p - c + 2, 3p - c + q + 1]; since 3p - c + 2 <= 2p and 3p - c + q + 1 >= p + q + 1, together with the y-even
  family z g^(2p-c) (pg)^y (lengths 2p - c + 1 + y, y even in [0, q + 1]) the window [p + q + 2, 2p] is met at an even length.
- c = p: g^p (pg)^(q+2) is a zero-sum of length p + q + 2 = 2kappa + 2.
So Sec. 3's sentence 'the second is not checked here' is replaced by: 'for the second, adding any odd z creates a zero-sum of
length in [2kappa + 2, 2p] as well'.  Under S(p), branch (iii) of the LS base case therefore closes completely, and the
residue of the base case is branch (i) alone (every Y - z fails (S1_kappa)).
