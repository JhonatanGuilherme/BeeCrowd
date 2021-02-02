#include <stdio.h>
 
int main() {
 
    int F1 = 0, F2 = 0, F3 = 0;
    scanf("%d %d %d", &F1, &F2, &F3);

    if ((F1 - F2 == 0 || F2 - F3 == 0 || F1 - F3 == 0 || (F1 + F2) - F3 == 0 || (F1 + F3) - F2 == 0 || (F2 + F3) - F1 == 0))
        printf("S\n");
    else
        printf("N\n");
 
    return 0;
}