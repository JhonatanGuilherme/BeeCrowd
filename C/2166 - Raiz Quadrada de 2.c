#include <stdio.h>
 
int main() {
 
    int i = 0, N = 0;
    double R = 0.0;
    scanf("%d", &N);

    for (i; i < N; i++) {
        R = 1.0 / (R + 2.0);
    }

    printf("%.10f\n", R + 1.0);
 
    return 0;
}