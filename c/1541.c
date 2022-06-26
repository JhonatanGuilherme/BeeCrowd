#include <stdio.h>
 
int main() {
 
    int A = 0, B = 0, C = 0;

    while (1) {
        
        scanf("%d %d %d", &A, &B, &C);
        if (A == 0)
            break;

        C =  pow((A * B * 100) / C, .5);
        printf("%d\n", C);

    }
 
    return 0;
}