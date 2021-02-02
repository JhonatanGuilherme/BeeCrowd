#include <stdio.h>
 
int main() {
 
    int i = 0, N = 0;
    scanf("%d", &N);
    int T [N];
    int R = N * 10;

    for (i; i < N; i++) {
        scanf("%d", &T[i]);
    }

    for (i = 0; i < N - 1; i++) {
        if (T[i] + 10 > T[i + 1])
            R -= 10 - (T[i + 1] - T[i]);
    }

    printf("%d\n", R);
 
    return 0;
}