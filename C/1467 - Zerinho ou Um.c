#include <stdio.h>
 
int main() {
 
    int A = 0, B = 0, C = 0;

    while (1) {
        if (scanf("%d %d %d", &A, &B, &C) == EOF) break;;

        if (A != B && B == C)
            printf("A\n");
        else if (A != B && A == C)
            printf("B\n");
        else if (A == B && A != C)
            printf("C\n");
        else
            printf("*\n");
    }
 
    return 0;
}