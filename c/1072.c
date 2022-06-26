#include <stdio.h>
 
int main() {
 
    int C = 0, i = 0, N = 0, X = 0;
    scanf("%d", &N);

    for (i = 0; i < N; i++) {
        scanf("%d", &X);
        if (X >= 10 && X <= 20)
            C ++;
    }

    printf("%d in\n", C);
    printf("%d out\n", N - C);
 
    return 0;
}