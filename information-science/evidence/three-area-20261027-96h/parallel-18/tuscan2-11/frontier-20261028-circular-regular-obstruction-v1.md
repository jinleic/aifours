# Circular Tuscan-2 routes to T2(11): a sufficient route and its regular-symmetry obstruction

Native `/bin/date` observed before writing: **Wed Oct 28 18:38:00 PDT 2026**. **WRITTEN all-variable statements.** They falsify one natural algebraic construction route; they do not decide the original existence question, construct a square, or claim novelty (the route may be classical folklore). No computation is used.

## 1. Circular arrays give linear squares

A circular Tuscan-2 array of size n×(n+1) has n rows, each a cyclic arrangement of all n+1 symbols, such that every ordered pair of distinct symbols occurs at most once at cyclic distance 1 and at most once at cyclic distance 2. Each distance has n(n+1) occurrences in total, equal to the number of ordered pairs, so both covers are exact. Choose any symbol ∗ and read every row starting immediately after ∗. The resulting n linear rows are permutations of the remaining n symbols. Their linear distance-1 and distance-2 events are subsets of the corresponding circular events, hence each ordered pair still occurs at most once at each distance. **Every circular Tuscan-2 11×12 array therefore yields an actual linear Tuscan-2 square of order 11.** The circular property is only sufficient, not necessary.

## 2. Regular group actions are impossible for every odd n

Let n be odd, N=n+1 (even), and suppose a group H of order N acts **regularly** on the symbols and permutes the n directed cyclic rows. Identify symbols with H, with action by left multiplication. For a row C=(x_0,...,x_{N−1}) (indices mod N), put δ_i=x_i^{−1}x_{i+1} and ε_i=x_i^{−1}x_{i+2}=δ_iδ_{i+1}. Left multiplication preserves these left differences.

The stabilizer of C acts on C by rotations, injectively, hence is cyclic. If its order is N/s, it consists of rotations by multiples of s and δ, ε are s-periodic. The orbit of C has exactly s rows. Every ordered arc (a,b) has left difference a^{−1}b≠e, and the arcs of a fixed difference form one H-orbit of size N. In the orbit of C, the arcs at positions i+ks (k=0,...,N/s−1) with difference δ_i start at the points of a coset of the cyclic stabilizer; over the s translates they cover all N arcs of difference δ_i exactly once. Exact distance-1 cover therefore forces the multiset of all period-differences δ_0,...,δ_{s−1} over all row orbits to be exactly H∖{e}, and exact distance-2 cover forces the multiset of all ε_0,...,ε_{s−1} to be exactly H∖{e} too.

The orbit sizes s are N/|Stab| and sum to n, which is odd. Hence some orbit has odd size, so its cyclic stabilizer contains a full Sylow 2-subgroup of H; **the Sylow 2-subgroups of H are cyclic**, of order 2^k with k≥1. By Burnside's normal p-complement theorem (named classical import: a finite group whose Sylow p-subgroup is cyclic, hence lies in the centre of its abelian normalizer, has a normal p-complement), H has a normal subgroup K of odd order m=N/2^k with H/K≅Z_{2^k}. Let φ:H→Z_{2^k} be this surjection. Each element of Z_{2^k} has m preimages, so

    Σ_{h≠e} φ(h) ≡ m·(0+1+...+(2^k−1)) ≡ m·2^{k−1}(2^k−1) ≡ 2^{k−1}   (mod 2^k),

because m is odd. Applying φ to each row orbit, Σ_i φ(ε_i)=Σ_i(φ(δ_i)+φ(δ_{i+1}))=2Σ_iφ(δ_i). Summing over all orbits, the ε-multiset has φ-sum 2·2^{k−1}≡0, whereas it must be H∖{e}, with φ-sum 2^{k−1}≢0 (mod 2^k). Contradiction. **Thus for every odd n, no circular Tuscan-2 n×(n+1) array admits a regular action of any group of order n+1.** For n=11 this excludes all twelve-element groups acting regularly (cyclic, dicyclic, dihedral, alternating and both abelian types); for groups with noncyclic Sylow 2-subgroup, the parity of orbit sizes already gives the contradiction.

## 3. Prime-order symmetries of circular arrays at n=11

For a circular Tuscan-1 11×12 array, let g≠1 be a symbol permutation of prime order p preserving its row set. If g fixes a row, g acts on that row as a nontrivial rotation, so it is fixed-point-free on symbols; if g fixes a symbol, every row orbit has size p and p divides 11, so p=11 with one fixed symbol ∞ and the eleven rows form one orbit. In that last case identify the moved symbols with Z_11; the ten arcs of a base row avoiding ∞ have distinct nonzero differences, which must be all of Z_11∖{0}; their sum is 0, but it also equals the difference between the two neighbours of ∞ in that row, which are distinct. So **any prime-order symmetry has p∈{2,3} and is fixed-point-free**, with the number of fixed rows ≡11 (mod p). Prime orders 5 and 7 cannot divide 11 and must fix symbols, hence are impossible.

These statements leave the semiregular order-2 and order-3 circular types, all asymmetric circular arrays, and all noncircular linear Tuscan-2 squares completely open. Separate bounded SAT checks of the order-3 types are being run and are not used here.
