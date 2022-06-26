#include <stdio.h>
 
int main() {
 
    int P1 = 0, C1 = 0, P2 = 0, C2 = 0;
    scanf("%d %d %d %d", &P1, &C1, &P2, &C2);

    if (P1 * C1 > P2 * C2)
        printf("-1\n");
    else if (P1 * C1 < P2 * C2)
        printf("1\n");
    else
        printf("0\n");
 
    return 0;
}