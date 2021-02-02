#include <stdio.h>
 
int main() {
 
    int i = 0, N = 0, S = 0;
    scanf("%d %d", &N, &S);
    int menor = S, R = S;

    for (i; i < N; i++) {
        scanf("%d", &S);
        R += S;
        if (R < menor)
            menor = R;
    }

    printf("%d\n", menor);
 
    return 0;
}