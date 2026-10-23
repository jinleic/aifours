/* e1_blocks.c -- finite control E1 for REDUCTION.md Lemma 2 (v = 100), exhaustive over all C(100,4) 4-subsets.
 * For every 4-subset X of Z_100: |Stab(X)| computed over all 100 translations; X is "Lemma-1 compatible" if for all
 * x != y in X and all d with x+d, y+d in X we have X + d = X (Lemma 1 consequence of lambda = 1 and +1-invariance).
 * Prints the stabilizer-order distribution, the Lemma-1-compatible subsets with nontrivial stabilizer, and the
 * Lemma-1-compatible subsets containing a pair {x, x+50}; both lists must be exactly the 25 cosets of <25>.
 */
#include <stdio.h>
#include <string.h>

#define V 100
static int is_member(const int *X, int y) { for (int i = 0; i < 4; i++) if (X[i] == y) return 1; return 0; }
static int same_after(const int *X, int d) {
    for (int i = 0; i < 4; i++) if (!is_member(X, (X[i] + d) % V)) return 0;
    return 1;
}
static int lemma1_ok(const int *X) {
    for (int i = 0; i < 4; i++)
        for (int j = i + 1; j < 4; j++)
            for (int d = 1; d < V; d++)
                if (is_member(X, (X[i] + d) % V) && is_member(X, (X[j] + d) % V) && !same_after(X, d)) return 0;
    return 1;
}
static int is_coset(const int *X) { return X[1] == X[0] + 25 && X[2] == X[0] + 50 && X[3] == X[0] + 75; }

int main(void) {
    long long dist[V + 1];
    memset(dist, 0, sizeof dist);
    long long total = 0;
    int nontriv_compat = 0, nontriv_compat_coset = 0, diam_compat = 0, diam_compat_coset = 0;
    int X[4];
    for (X[0] = 0; X[0] < V; X[0]++)
        for (X[1] = X[0] + 1; X[1] < V; X[1]++)
            for (X[2] = X[1] + 1; X[2] < V; X[2]++)
                for (X[3] = X[2] + 1; X[3] < V; X[3]++) {
                    total++;
                    int o = 0;
                    for (int d = 0; d < V; d++) o += same_after(X, d);
                    dist[o]++;
                    int diam = 0;
                    for (int i = 0; i < 4; i++) if (is_member(X, (X[i] + 50) % V)) diam = 1;
                    if (o > 1 || diam) {
                        int ok = lemma1_ok(X);
                        if (o > 1 && ok) { nontriv_compat++; nontriv_compat_coset += is_coset(X); }
                        if (diam && ok) { diam_compat++; diam_compat_coset += is_coset(X); }
                    }
                }
    printf("E1 4-subsets: %lld\n", total);
    for (int o = 1; o <= V; o++) if (dist[o]) printf("E1 stabilizer order %d: %lld subsets\n", o, dist[o]);
    printf("E1 nontrivial stabilizer and Lemma-1 compatible: %d (cosets of <25> among them: %d)\n",
           nontriv_compat, nontriv_compat_coset);
    printf("E1 contains a pair {x,x+50} and Lemma-1 compatible: %d (cosets of <25> among them: %d)\n",
           diam_compat, diam_compat_coset);
    int pass = nontriv_compat == 25 && nontriv_compat_coset == 25 && diam_compat == 25 && diam_compat_coset == 25;
    printf("E1 %s\n", pass ? "PASS" : "FAIL");
    return pass ? 0 : 1;
}
