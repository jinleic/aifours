# Commault & Mocanu (2003), Int. J. Control 76(6):566-580 - primary excerpts transcribed by the review desk

Pinned PDF: primary/commault-mocanu-2003.pdf, sha256 8db1e4aa330a9d9989cb91498524d9cb0c41a95aa636906ed6e42391d5d70cfb.
Transcribed by the desk (Ph3HostileDesk, 2026-10-18 PDT) by viewing the page images primary/pages/cm2003-pdfNN-NN.png
(rendered from the pinned PDF). Words are verbatim; mathematical typesetting is rendered in Unicode/plain text
(e.g. 1⃗ = all-ones column vector, f̃ = Laplace transform; [display] marks a displayed formula). The PDF text layer
(primary/pages/*-pdftotext-layout.txt) garbles Greek letters and operators and is NOT a reliable math source.
"PDFk" = k-th page of the PDF file; "p.NNN" = printed journal page. Ellipses "[...]" mark omitted unrelated text.

## E1. p.567 (PDF3), right column - PH generator, representation, order, degree
"[display] ẋ̄(t) = x̄(t)Q, x̄(0) = ᾱ (1)
where the ith component of the row vector x̄(t) is the probability of being in state i at time t. The vector ᾱ
represents the initial probability distribution and is a stochastic vector. The (n + 1) × (n + 1) matrix Q
represents the infinitesimal generator of the Markov process and can be partitioned as
[display] Q = ( T v ; 0 0 ) (2)
T_ij ≥ 0 for i ≠ j, i = 1, ..., n; j = 1, ..., n, is the transition rate from state i to state j. v_i for
i = 1, ..., n, represents the transition rate from state i to the absorbing state. Due to the special structure of a
Markov generator we must have v = −T1⃗ where 1⃗ is the n dimensional column vector whose entries are all equal to
one. The assumption that the first n states are transient implies that the matrix T is non-singular. This matrix is
called a PH-generator. From now on we will assume that ᾱ = (α, 0) where α is n dimensional. This means that we
assume that the probability of being in the absorbing state at time 0 is 0. This is for the sake of simplicity but
it implies no real loss of generality. The pair (α, T) is called a representation of the corresponding distribution
which is denoted by PH(α, T). [...] The solution is then f(t) = α e^{tT} v. We will also frequently make use of the
Laplace transform of f(t) that we will denote by f̃(s). f̃(s) = α(sI − T)⁻¹v, where I denotes the order n identity
matrix. [...] The order of a representation is the number of transient states of the Markov chain which is the
dimension of the matrix T. Let f̃(s) be the Laplace transform of a PH-distribution and f̃(s) = p(s)/q(s), where p(s)
and q(s) are coprime polynomials. We call the degree of the distribution the polynomial degree of q(s). Obviously,
for any PH repre-" [continues on p.568]

## E2. p.568 (PDF4), left column - constraints (4)-(6), graph G(α,T), irreducible PH representation
"sentation the order is greater than or equal to the degree of the corresponding distribution. But, contrary to what
happens for standard linear systems, given a PH-distribution there generally does not exist a representation of
order equal to the degree of this distribution. Let us recall the constraints of the problem at hand compared to the
usual linear system model used in control.
• The non-singular matrix T represents an infinitesimal generator, then
[display] T_ij ≥ 0 for i ≠ j, i = 1, ..., n, and j = 1, ..., n ; Σ_{j=1}^{n} T_ij ≤ 0 for i = 1, ..., n (4)
• The v vector is defined as [display] v = −T1⃗ (5)
• The initial probability distribution is a stochastic vector, that is : α_i ≥ 0 for i = 1, ..., n and
[display] Σ_{i=1}^{n} α_i = 1 (6)
It is known that a lot of qualitative properties of Markov chains can be obtained from the study of their graphs.
[...] To a phase-type representation (α, T) we associate a directed graph G(α, T), where the set of vertices is
composed of (n + 2) elements. The vertices 1, ..., n + 1 correspond to the states of the representation. The vertex
0 is a dummy vertex corresponding to the initial state. There exists an edge (i, j), i ≠ j, if T_ij ≠ 0 for
i = 1, ..., n; j = 1, ..., n. There exists an edge (i, n + 1), if v_i ≠ 0 for i = 1, ..., n. There exists an edge
(0, j), if α_j ≠ 0 for j = 1, ..., n. [...]
A representation in which graph all the state vertices are connected to the initial vertex and to the absorbing
vertex is called irreducible (Neuts 1981). It is obvious that, when it is not the case, the representation may be
simplified and the corresponding states discarded without altering the distribution."

## E3. p.570 (PDF6) - positive realizations, Theorem 3, irreducible realization, Proposition 1, Theorem 4
Left column top: "[display] a_ij ≥ 0 for i ≠ j; i = 1, ..., n; j = 1, ..., n (9)  b_i ≥ 0 for i = 1, ..., n (10)
c_i ≥ 0 for i = 1, ..., n (11)
This state space representation is such that for any initial state x(0) ≥ 0 and any input function u(t) ≥ 0 for
t ≥ 0, the state and output functions remain nonnegative. [...]
A linear system defined by its rational transfer function g̃(s) is said to be (externally) positive if its impulse
response g(t), the inverse Laplace transform of g̃(s), is such that g(t) ≥ 0 for t ≥ 0. We assume that the transfer
function is strictly proper, that is g(0) = 0.
The positive realization problem is the following: given a positive system defined by its transfer function g̃(s),
find, if possible, a positive state space representation (A, B, C) such that g̃(s) = C(sI − A)⁻¹B. The problem of
existence of such a positive realization was solved in Farina (1996).
Theorem 3: A linear system with transfer function g̃(s) and impulse response g(t) has a positive realization if and
only if: 1. g̃(s) has a unique pole with maximal real part, and 2. g(t) > 0 for t > 0. [...]
3.2. From a positive realization to a PH-representation
To a positive state space representation one can associate a graph as we did for PH-representations. The vertices
are associated with input, state and output variables, therefore we have one vertex u, one vertex y and n vertices
(x_1, ..., x_n). There is an edge (x_i, x_j) (resp. (u, x_i), (x_i, y)) if a_ji > 0 (resp. b_i > 0, c_i > 0). This
graph is called the influence graph in Farina and Rinaldi (2000). We say that the representation is irreducible if
any state vertex belongs to an input–output path in the associated graph. Irreducibility is equivalent to both
excitability and transparency in the terminology of Farina and Rinaldi (2000). It is clear that when a
representation is not irreducible it can be simplified by discarding some states, therefore we may restrict our"
Right column: "attention, without loss of generality, to irreducible representations. The following result which is
specific to positive realizations is of importance.
Proposition 1: Consider a linear system with transfer function g̃(s) which admits a positive realization. For any
irreducible positive realization (A, B, C) the eigenvalue of A with maximal real part is the pole of maximal real part
of g̃(s).
Proof: The result is proved in Anderson et al. (1996) for discrete-time systems but the same arguments can be used
for continuous-time systems. Also the notion of irreducibility is not explicit in the formulation of Anderson et al.
(1996) □
Although irreducibility is weaker than the assumption of joint controllability and observability, the proposition
says that for positive irreducible representations, the dominant eigenvalue of A can never be simplified. The same
result was proved for PH-representations in Neuts (1984).
From the basic properties of a p.d.f. it follows that the impulse response g(t) of a linear positive system may be
interpreted as a p.d.f. if the corresponding transfer function g̃(s) is asymptotically stable and if the
normalization condition g̃(0) = 1 is satisfied. This allows us to give the correspondence between positive
realizations and PH-representations.
Theorem 4: Consider a linear system with transfer function g̃(s) and impulse response g(t) which admits a positive
irreducible realization of order n, (F, G, H):
1. if g̃(s) is asymptotically stable there exists an order n positive irreducible realization of g̃(s), (A, B, C),
which satisfies [display] Σ_{j=1}^{n} a_ij + b_i = 0 for i = 1, ..., n (12)
and the graph of (A, B, C) is the same as the graph of (F, G, H),
2. if moreover g̃(0) = 1 then [display] Σ_{i=1}^{n} c_i = 1 (13)
Before proving the theorem let us state a technical lemma.
Lemma 1 Consider an irreducible positive representation (F, G, H), where F is asymptotically stable, the equation"

## E4. p.571 (PDF7), left column - Lemma 1 (end) and proof of Theorem 4
"[display] Fγ = −G (14)
has a unique solution γ = (γ_1, ..., γ_n)ᵀ with γ_i > 0 for i = 1, ..., n.
Proof: The solution of the equation exists and is unique since F is asymptotically stable and then non-singular.
From Berman et al. (1989, Theorem 4.12), this solution is non-negative. Let us now prove that it has indeed only
positive entries. For i such that g_i ≠ 0 the ith equation implies that γ_i > 0. Let j ≠ i be such that f_ji > 0,
then we must have γ_j > 0. From the irreducibility assumption, each state is connected to the input and we can repeat
the reasoning for all the entries of γ. □
Proof of Theorem 4:
1. Define the n × n diagonal non-singular matrix M = Diag(γ_1, ..., γ_n) where γ is the solution of Fγ = −G. Define
the new triplet (A, B, C) where [display] A = M⁻¹FM, B = M⁻¹G, C = HM (15)
(A, B, C) is a new realization of g̃(s) and it is clearly positive. The change of basis corresponds here to a simple
rescaling of the state variables. It can easily be checked that the relation (12) follows from the definition of γ.
The change of basis amounts to a multiplication of rows and columns (resp. rows, columns) of F (resp. G, H) by
positive numbers. Then an entry of a matrix which is positive remains positive after the change of basis, an entry
of a matrix which is 0 remains 0 after the change of basis. Therefore the graph of (A, B, C) is the same as the graph
of (F, G, H).
2. Since C is a non-zero matrix with non-negative entries we can write C = δĈ where [display] δ = Σ_{i=1}^{n} c_i (16)
the entries of Ĉ are non-negative and sum up to one. Therefore the triplet (A, B, Ĉ) corresponds to a
PH-representation and the corresponding distribution has a Laplace transform which satisfies ĝ(0) = ĈA⁻¹B = 1. If we
start with g̃(0) = 1 then g̃(0) = HF⁻¹G = CA⁻¹B = δĈA⁻¹B = δ = 1 which implies [display] Σ_{i=1}^{n} c_i = 1 (17) □"
[signs as printed; Theorem 4 is background only - the reviewed proof does its own diagonal scaling in B8]

## E5. p.574 (PDF10), right column - Theorem 6
"theorem comes from the numerous studies which have been done on the eigenvalue location of stochastic matrices
following, for example, the Perron–Frobenius theorem. The result was obtained independently in Dmitriev and Dynkin
(1945) and O'Cinneide (1991).
Theorem 6 (Dmitriev and Dynkin 1945, O'Cinneide 1991): Let T be a phase-type generator of order n. Let −λ_1, λ_1 > 0,
be its eigenvalue with maximal real part and −λ_2 ± iθ, λ_2 > 0 and θ > 0, be any pair of its complex eigenvalues.
The following relation is satisfied [display] θ/(λ_2 − λ_1) ≤ cot(π/n) (27)
The previous relation may be seen as [display] n ≥ π / arctan((λ_2 − λ_1)/θ) (28)
Since the poles of the Laplace transform of the distribution are eigenvalues of the T matrix of any representation,
it follows that the order of the representation increases when the angle between the position of complex poles and
the vertical line passing through the real dominating pole decreases. This makes part 2 of Theorem 1 more precise and
gives a first bound on the order of possible representations of a given distribution. This result definitely kills
the hope that one could find a representation whose order is the degree of the distribution [...]"

## E6. p.577 (PDF13), right column - Theorem 14, Eq. (42), (43), Conjecture 1
"Theorem 14 (Commault and Chemla 1996): Consider a PH-distribution with Laplace transform f̃(s) = 1/q(s)
[display] q(s) = (1 + s/c)(1 + s/(a + ib))(1 + s/(a − ib)) (42)
where a, b, c ≥ 0. This distribution has an order 3 representation if and only if
[display] b ≤ (a − c)/√3 (43)
It is clear from Theorem 6 that condition (43) is necessary for obtaining an order 3 representation. In fact, using
Theorem 8 and some simplifying tricks we can always obtain a representation which has the graph given in figure 13.
For PH-distributions with Laplace transform f̃(s) = 1/q(s) where q(s) is as in (42), Theorem 6 gives a minimal order
n_min for a representation. An interesting question is the following.
Conjecture 1: There exists a representation of order n_min for such a distribution.
In Mocanu (1999) it is only proved that we can obtain a representation of order (n_min + 1).
A more interesting problem, both from the theoretical and practical points of view, would be the characterization of
order 3 PH-distributions. Since it can be easily proved that order 2 PH-representations must have real eigenvalues,
the order 3 representations appear to be the smallest ones with a sufficient power of representation (or
approximation). [...]"
