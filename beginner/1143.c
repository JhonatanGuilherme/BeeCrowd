#include <stdio.h>
 
int main() {
 
    int i = 1, N = 0;
    scanf("%d", &N);

    for (i; i <= N; i++) {
        printf("%d %d %d\n", i, i * i, i * i * i);
    }
 
    return 0;
}