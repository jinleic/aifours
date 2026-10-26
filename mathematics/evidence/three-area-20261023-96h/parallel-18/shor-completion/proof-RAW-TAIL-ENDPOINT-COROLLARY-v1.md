# Homogeneous-tail endpoint shape forced by the layer interaction

Observed before creation: **2026-10-23T14:52:52-0700 PDT**. MathShor, math-5. **CANDIDATE corollary inside the homogeneous-tail sufficient ansatz only**. No new pure-a order lower bound, unrestricted noncompletion, witness, formal proof or novelty claim. No scientific execution occurred.

This is one consequence of the same raw completion-shape argument, not a new problem or independent discovery count. It uses the pinned two-/three-a layer theorem and gap/four-a compatibility candidate. Both retain their own written-review status.

## 1. Hypotheses and exact result

Suppose a finite UD complete extension has the special form

    M=C ∪ T_n,

where n≥5 and EVERY extra word has length n. The current sufficient Bernoulli construction uses much larger n, so it is covered if its selector ever becomes UD. Write its forced words as

    W=b^r a^2 b^t,                      r+t=n-2,
    U_a=b^(alpha_a) a b^a a^2 b^(beta_a), 1≤a<r,
    V_c=b^(gamma_c) a^2 b^c a b^(delta_c),1≤c≤t.

The prior raw theorem gives r,t≥1, beta_a≥1, alpha_1≥1 if r≥2, and gamma_c≥1 for c≥2. Homogeneous tail lengths give

    alpha_a+beta_a=n-3-a,
    gamma_c+delta_c=n-3-c.                              (1)

Then necessarily:

1. r≥3 and t≥1.
2. gamma_c≥1 for EVERY 1≤c≤t, including c=1.
3. alpha_a≥1 for 1≤a≤r-2, whereas

       alpha_(r-1)=0,       beta_(r-1)=t.               (2)

Thus EXACTLY ONE extra three-a word starts with a, namely

    U_(r-1)=a b^(r-1) a^2 b^t.                          (3)

Every other extra three-a word begins with b. The original short a^3b is not an extra word and is not counted in this last assertion.

These conditions constrain b-delay parameters of a construction ansatz. They are not new divisibility or numerical lower bounds on the pure-a order of an arbitrary completion, and are not asserted for mixed-length extensions.

## 2. First exclude r=1 without a circular endpoint argument

If r=1, then t=n-3≥2. Equation (1) at c=t gives

    gamma_t+delta_t=n-3-t=0.

But the unrestricted raw theorem already gives gamma_t≥1 for t≥2. Contradiction. Therefore r≥2. In particular, for every c≤t,

    n-3-c≥n-3-t=r-1≥1.                                 (4)

This order of deductions is important: the next step's forced positive gap uses (4).

## 3. All V_c have a positive leading b-delay

Suppose gamma_c=0. Then (1) gives delta_c=n-3-c≥1 by (4). The four-a core with gaps

    (0,c,delta_c)

has no proper parse: a first W followed by two ba's would require c≥t+1, but c≤t; V_c followed by ba would require the last gap at least delta_c+1, whereas it equals delta_c. The gap-table row (0,b,c) therefore forces a NEW four-a codeword with this core.

Its internal core already has length

    4+c+delta_c=4+c+n-3-c=n+1.

It cannot be a tail word of length n. It is not one of C, since C has no four-a word. This contradicts the ansatz. Hence gamma_c≥1 for every c≤t.

## 4. The last U endpoint is exact, and r cannot be2

At c=t, equation (1) gives gamma_t+delta_t=r-1, so gamma_t≤r-1. Apply the proved crossing restriction

    beta_a≥c OR gamma_c>a

at a=r-1,c=t. The second alternative is false, hence beta_(r-1)≥t. On the other hand (1) at a=r-1 gives alpha_(r-1)+beta_(r-1)=t. Nonnegativity forces exactly (2).

If r=2, this says alpha_1=0, contrary to the unrestricted Shor collision alpha_1≥1. Thus r≥3. This is a parameter exclusion in the sufficient tail family, not a claim that finite completion requires a new numerical n bound.

## 5. Every earlier U has a positive leading delay

For 1≤a≤r-2 suppose alpha_a=0. Then

    beta_a=n-3-a=r+t-1-a≥t+1.

Consider the four-a core with gaps (a,0,beta_a). The only proper lower-layer parses could be:

- ba,W,ba, requiring a≥r (false);
- U_a,ba, requiring beta_a≥beta_a+1 (false);
- ba,V_(beta_a), requiring beta_a≤t (false).

Hence a new four-a word with that core is forced. Its core length is

    4+a+beta_a=n+1,

again impossible in C∪T_n. Thus alpha_a≥1 for all earlier a. Combined with (2), this proves the claimed unique extra three-a word starting with a.

## 6. Exact selector remainder

The remaining parameters are not exhausted by these conditions. The tail family still must satisfy the crossing inequalities for every a,c, every forced four-a core's nonnegative outer-delay budget, and all later raw gap-parse uniqueness/universality constraints. No admissible parameter tuple or actual full tail set is supplied here.

A successful finite selector with a valid residual closure/Kraft certificate, or the gap-parser invariant certificate, would prove an actual completion. Failure of this family would not exclude mixed-length completions. This corollary only removes incorrect endpoint choices BEFORE any unjustified exponential raw-tail generation. All claims remain candidates pending separate reconstruction and parent consideration.
